#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = (
    ROOT / "reports" / "workstreams" / "category-specs-mypy-structural-full" / "latest.json"
)
DEFAULT_OUTPUT_DIR = ROOT / "reports" / "workstreams" / "category-specs-mypy-ledger"
ERROR_RE = re.compile(
    r"^(?P<path>[^:]+):(?P<line>\d+): error: (?P<message>.*?)(?:  \[(?P<code>[^\]]+)\])?$"
)


def git_sha(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def classify_owner(path: str, code: str, message: str) -> str:
    if path.startswith(".cache/"):
        return "plugin projection"
    if "no base method was found" in message:
        return "missing sidecar ordinary signature"
    if 'Module "sage.' in message and "has no attribute" in message:
        return "missing sidecar ordinary signature"
    if code == "attr-defined" and ("sage." in message or "Morphism" in message):
        return "missing sidecar ordinary signature"
    if code in {"arg-type", "return-value", "assignment", "list-item", "type-var", "operator"}:
        return "research typing/design"
    if code == "override":
        return "research typing/design"
    if code == "misc" and "Definition of" in message:
        return "research typing/design"
    return "mathematical/category-interface question"


def root_area(path: str) -> str:
    parts = Path(path).parts
    if not parts:
        return "unknown"
    if parts[0] == "category_specs" and len(parts) > 1:
        return parts[1]
    if parts[0] == ".cache":
        return ".cache"
    return parts[0]


def parse_errors(lines: list[str]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for raw in lines:
        match = ERROR_RE.match(raw)
        if not match:
            continue
        path = match.group("path")
        code = match.group("code") or "no-code"
        message = match.group("message")
        entries.append(
            {
                "path": path,
                "line": int(match.group("line")),
                "code": code,
                "root_area": root_area(path),
                "owner": classify_owner(path, code, message),
                "message": message,
                "raw": raw,
            }
        )
    return entries


def is_canary_negative_control(entry: dict[str, Any]) -> bool:
    return str(entry["path"]).startswith(".cache/") and "negative_consumer_probe.py" in str(
        entry["path"]
    )


def counts(entries: list[dict[str, Any]], key: str) -> dict[str, int]:
    counter = collections.Counter(str(entry[key]) for entry in entries)
    return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0])))


def top_examples(entries: list[dict[str, Any]], limit: int = 30) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    examples: list[dict[str, Any]] = []
    for entry in entries:
        key = (str(entry["owner"]), str(entry["code"]))
        if key in seen:
            continue
        seen.add(key)
        examples.append(entry)
        if len(examples) >= limit:
            break
    return examples


def write_markdown(payload: dict[str, Any], path: Path) -> None:
    lines = [
        "# Category Specs Mypy Error Ledger",
        "",
        f"- source_artifact: `{payload['source_artifact']}`",
        f"- structural_status: {payload['structural']['status']}",
        f"- source_mode: {payload['structural']['source_mode']}",
        f"- full_structural_mismatches: {payload['structural']['mismatched_provider_count']}",
        f"- full_structural_missing_typeinfos: {payload['structural']['missing_typeinfo_count']}",
        "- full_structural_projected_ancestor_missing_typeinfos: "
        f"{payload['structural']['projected_ancestor_missing_typeinfo_count']}",
        f"- ordinary_error_count: {payload['ordinary_error_count']}",
        f"- ignored_negative_control_count: {len(payload['ignored_diagnostics'])}",
        "",
        "## Toolchain",
        "",
    ]
    for key, value in payload["toolchain"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Counts By Owner", ""])
    for owner, count in payload["counts_by_owner"].items():
        lines.append(f"- {owner}: {count}")
    lines.extend(["", "## Counts By Code", ""])
    for code, count in payload["counts_by_code"].items():
        lines.append(f"- {code}: {count}")
    lines.extend(["", "## Counts By Root Area", ""])
    for area, count in payload["counts_by_root_area"].items():
        lines.append(f"- {area}: {count}")
    lines.extend(["", "## Representative Examples", ""])
    for entry in payload["examples"]:
        lines.append(
            f"- {entry['owner']} / {entry['code']} / {entry['root_area']}: "
            f"`{entry['raw']}`"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Group category_specs mypy diagnostics.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    source = args.input
    data = json.loads(source.read_text(encoding="utf-8"))
    parsed_entries = parse_errors(data.get("mypy_errors", []))
    ignored_entries = [entry for entry in parsed_entries if is_canary_negative_control(entry)]
    entries = [entry for entry in parsed_entries if not is_canary_negative_control(entry)]
    payload = {
        "source_artifact": str(source.relative_to(ROOT) if source.is_relative_to(ROOT) else source),
        "toolchain": {
            "research_sha": git_sha(ROOT),
            "plugin_sha": git_sha(Path("/home/dzack/sage-mypy-plugin")),
            "sidecar_sha": git_sha(Path("/home/dzack/sage-mypy-plugin/sage-stubs")),
        },
        "structural": {
            "status": data.get("status"),
            "source_mode": data.get("source_mode"),
            "source_module_count": data.get("source_module_count"),
            "projection_count": data.get("projection_count"),
            "checked_provider_count": data.get("checked_provider_count"),
            "graph_absent_provider_count": data.get("graph_absent_provider_count"),
            "missing_typeinfo_count": data.get("missing_typeinfo_count"),
            "projected_ancestor_missing_typeinfo_count": data.get(
                "projected_ancestor_missing_typeinfo_count"
            ),
            "mismatched_provider_count": data.get("mismatched_provider_count"),
        },
        "raw_diagnostic_count": len(data.get("mypy_errors", [])),
        "parsed_error_count": len(parsed_entries),
        "ordinary_error_count": len(entries),
        "ignored_diagnostics": ignored_entries,
        "counts_by_owner": counts(entries, "owner"),
        "counts_by_code": counts(entries, "code"),
        "counts_by_root_area": counts(entries, "root_area"),
        "examples": top_examples(entries),
        "errors": entries,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "latest.json"
    md_path = args.output_dir / "latest.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(payload, md_path)
    print(f"wrote {json_path}")
    print(f"wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
