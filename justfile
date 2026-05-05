# Coble Moduli Project - Computational Verification
# Requires: sage, gap, z3 (via uv)

export PYTHONPATH := "."
export SAGE_PYTEST := "1"
test_timing_dir := env_var_or_default("COBLE_RESEARCH_TEST_TIMING_DIR", justfile_directory() / ".cache/test_timings")

# Show available recipes
default: _clean
    @just --list

uv-setup: _clean
    @echo "Setting up uv environment..."
    uv sync

[private]
_clean:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    find . \
        -path './.git' -prune -o \
        -path './.worktrees' -prune -o \
        -type f \( -name '*.orig' -o -name '*.sage.py' \) \
        -exec rm -f {} +
    find . \
        -path './.git' -prune -o \
        -path './.worktrees' -prune -o \
        -type d -empty -print0 \
        | sort -rz \
        | while IFS= read -r -d '' path; do
            rmdir "$path" 2>/dev/null || true
        done

[private]
_record-test-timing timing_dir label started_at finished_at duration_seconds exit_status:
    #!/usr/bin/env python3
    import json
    import os
    from pathlib import Path

    timing_dir = Path("{{timing_dir}}")
    label = "{{label}}"
    started_at = "{{started_at}}"
    finished_at = "{{finished_at}}"
    duration_seconds = float("{{duration_seconds}}")
    exit_status = int("{{exit_status}}")

    timing_dir.mkdir(parents=True, exist_ok=True)
    entry = {
        "label": label,
        "started_at": started_at,
        "finished_at": finished_at,
        "duration_seconds": duration_seconds,
        "exit_status": exit_status,
        "cwd": os.getcwd(),
    }

    history_path = timing_dir / "just_history.jsonl"
    with history_path.open("a", encoding="utf-8") as handle:
        json.dump(entry, handle, sort_keys=True)
        handle.write("\n")

    (timing_dir / "just_latest.json").write_text(
        json.dumps(entry, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"{label} timing: {duration_seconds:.6f}s -> {history_path}")

# ==============================================================================
# Foundation Library
# ==============================================================================

test: _clean
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    TIMING_DIR="{{test_timing_dir}}"
    START_EPOCH="${EPOCHREALTIME}"
    STARTED_AT="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    record_timing() {
        local status="$1"
        local end_epoch="${EPOCHREALTIME}"
        local finished_at
        local duration
        finished_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
        duration="$(python -c 'import sys; print(f"{float(sys.argv[2]) - float(sys.argv[1]):.6f}")' "$START_EPOCH" "$end_epoch")"
        just --justfile {{justfile()}} _record-test-timing \
            "$TIMING_DIR" \
            "just test" \
            "$STARTED_AT" \
            "$finished_at" \
            "$duration" \
            "$status"
    }
    trap 'status=$?; trap - EXIT; record_timing "$status"; exit "$status"' EXIT
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} test
    just _clean

test-ci: _clean
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just test

plan-validate:
    #!/usr/bin/env python3
    import re
    import sys
    from pathlib import Path

    import yaml

    root = Path("{{justfile_directory()}}")
    plans_root = root / "plans" / "features"
    schema_root = root / ".nimbalyst" / "trackers"
    allowed_types = {"feature", "spec", "plan", "phase", "task", "decision"}

    def error(path, message):
        errors.append(f"{path}: {message}")

    def frontmatter(path):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            raise ValueError("missing YAML frontmatter")
        try:
            raw, _ = text[4:].split("\n---\n", 1)
        except ValueError as exc:
            raise ValueError("unterminated YAML frontmatter") from exc
        return yaml.safe_load(raw) or {}

    def field_schema(schema, field_name):
        for field in schema.get("fields", []):
            if field.get("name") == field_name:
                return field
        return None

    def ref_ids(value):
        if value is None:
            return []
        if not isinstance(value, list):
            raise TypeError("must be a list")
        ids = []
        for item in value:
            if not isinstance(item, str):
                raise TypeError("must contain string references")
            match = re.fullmatch(r"\[\[([A-Z0-9-]+)\]\]", item)
            ids.append(match.group(1) if match else item)
        return ids

    def expected_kind(path, card_id):
        rel = path.relative_to(plans_root)
        parts = rel.parts
        if len(parts) == 2 and parts[0] == card_id and parts[1] == f"{card_id}.md":
            return "feature"
        if len(parts) == 3 and parts[1] == "specs":
            return "spec"
        if len(parts) == 3 and parts[1] == "decisions":
            return "decision"
        if len(parts) == 4 and parts[1] == "plans" and parts[2] == card_id:
            return "plan"
        if len(parts) == 5 and parts[1] == "plans" and parts[3] == card_id and parts[4] == f"{card_id}.md":
            return "phase"
        if len(parts) == 6 and parts[1] == "plans" and parts[4] == "tasks":
            return "task"
        return None

    errors = []
    schemas = {}
    for schema_path in sorted(schema_root.glob("*.yaml")):
        schema = yaml.safe_load(schema_path.read_text(encoding="utf-8")) or {}
        schema_type = schema.get("type")
        if schema_type in allowed_types:
            schemas[schema_type] = schema

    missing = allowed_types - set(schemas)
    if missing:
        errors.append(f".nimbalyst/trackers: missing schemas for {', '.join(sorted(missing))}")

    cards = {}
    for path in sorted(plans_root.rglob("*.md")):
        try:
            data = frontmatter(path)
        except Exception as exc:
            error(path, str(exc))
            continue

        card_id = data.get("id")
        if card_id != path.stem:
            error(path, f"id {card_id!r} must match filename stem {path.stem!r}")
        elif card_id in cards:
            error(path, f"duplicate id {card_id}; first seen at {cards[card_id]['path']}")
        else:
            cards[card_id] = {"path": path, "data": data}

        tracker = data.get("trackerStatus")
        if not isinstance(tracker, dict):
            error(path, "trackerStatus must be a mapping")
            continue

        kind = tracker.get("type")
        if kind not in allowed_types:
            error(path, f"trackerStatus.type {kind!r} must be one of {sorted(allowed_types)}")
            continue
        if kind not in schemas:
            continue

        placement = expected_kind(path, card_id)
        if placement != kind:
            error(path, f"type {kind!r} does not match root plans placement {placement!r}")

        schema = schemas[kind]
        allowed_statuses = {
            option["value"]
            for option in (field_schema(schema, "status") or {}).get("options", [])
            if isinstance(option, dict) and "value" in option
        }
        status = data.get("status")
        if allowed_statuses and status not in allowed_statuses:
            error(path, f"status {status!r} is not allowed for {kind}")

        for field in schema.get("fields", []):
            name = field.get("name")
            if field.get("required") and data.get(name) in (None, "", []):
                error(path, f"missing required field {name!r}")

        for name in ("parents", "dependsOn", "blocks", "plans", "phases", "tasks"):
            if name in data:
                try:
                    ref_ids(data[name])
                except TypeError as exc:
                    error(path, f"{name} {exc}")

    for card_id, entry in cards.items():
        data = entry["data"]
        path = entry["path"]
        for name in ("parents", "dependsOn", "blocks", "plans", "phases", "tasks"):
            try:
                ids = ref_ids(data.get(name, []))
            except TypeError:
                continue
            for ref_id in ids:
                if ref_id not in cards:
                    error(path, f"{name} references missing card {ref_id}")

    if errors:
        print("plan validation failed:", file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        sys.exit(1)

    print(f"Validated {len(cards)} root planning cards.")
