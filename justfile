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

test-spec-core-vertical-slice: _clean
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    cleanup() {
        just --justfile {{justfile()}} _clean
    }
    trap cleanup EXIT
    sage -python -m pytest \
        tests/category_specs/test_spec_core_reports.py \
        tests/category_specs/test_free_module_witnesses.py \
        tests/category_specs/test_spec_core_generated_laws.py \
        tests/category_specs/test_constructor_provenance.py

plan-validate:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just --justfile /home/dzack/ai/planning/justfile validate \
        {{justfile_directory()}}/.agents/plans/features \
        {{justfile_directory()}}/.nimbalyst/trackers \
        {{justfile_directory()}}/.agents/plans/plan-dag.md

plan-progress-report:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    uv run .agents/scripts/generate_card_progress_report.py --output .agents/plans/card-progress-report.md

next-tasks n="1":
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just --justfile {{justfile()}} plan-validate >/dev/null
    uv run .agents/scripts/generate_card_progress_report.py --next-outstanding-tasks "{{n}}"

paper-build:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}/paper
    latexmk -xelatex -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex

paper-clean:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}/paper
    latexmk -C main.tex
