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
DEFAULT_INPUT = ROOT / "reports" / "workstreams" / "category-specs-mypy-ledger" / "latest.json"
DEFAULT_OUTPUT_DIR = ROOT / "reports" / "workstreams" / "category-specs-sage-stub-backlog"

SAGE_MODULE_RE = re.compile(r'Module "(?P<module>sage\.[^"]+)"')
SAGE_NAME_RE = re.compile(r'"(?P<name>[A-Za-z_][A-Za-z0-9_]*)"')
SAGE_TOKENS = (
    "sage.",
    "LazyImport",
    "Category",
    "Morphism",
    "Hom",
    "End",
    "Aut",
    "Integer",
    "InfinityElement",
    "MatrixSpace",
    "PolynomialRing",
    "PowerSeriesRing",
    "Laurent",
    "FreeModule",
    "VectorSpace",
    "NumberField",
    "IntegerModRing",
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


def read_source_line(path: str, line: int) -> str:
    source = ROOT / path
    try:
        lines = source.read_text(encoding="utf-8").splitlines()
    except OSError:
        return ""
    if line < 1 or line > len(lines):
        return ""
    return lines[line - 1].strip()


def sage_module_from_entry(entry: dict[str, Any], source_line: str) -> str | None:
    message = str(entry["message"])
    match = SAGE_MODULE_RE.search(message)
    if match:
        return match.group("module")
    source_match = re.search(r"\bfrom (sage\.[A-Za-z0-9_.]+) import\b", source_line)
    if source_match:
        return source_match.group(1)
    return None


def sage_symbol_from_entry(entry: dict[str, Any], source_line: str) -> str | None:
    message = str(entry["message"])
    names = SAGE_NAME_RE.findall(message)
    for name in names:
        if name not in {"sage", "Any", "object", "None"}:
            return name
    call_match = re.search(r"\b([A-Z][A-Za-z0-9_]*)\(", source_line)
    if call_match:
        return call_match.group(1)
    member_match = re.search(r"\.([A-Za-z_][A-Za-z0-9_]*)\b", source_line)
    if member_match:
        return member_match.group(1)
    return None


def is_stub_candidate(entry: dict[str, Any], source_line: str) -> bool:
    message = str(entry["message"])
    if entry["owner"] == "missing sidecar ordinary signature":
        return True
    if any(token in message or token in source_line for token in SAGE_TOKENS):
        return True
    if str(entry["root_area"]) in {"cat", "homsets"} and str(entry["code"]) in {
        "misc",
        "override",
        "attr-defined",
        "operator",
    }:
        return True
    return False


def failure_kind(entry: dict[str, Any], source_line: str) -> str:
    message = str(entry["message"])
    code = str(entry["code"])
    if 'Module "sage.' in message and "has no attribute" in message:
        return "missing sage module member"
    if code == "attr-defined" and "has no attribute" in message:
        return "missing sage class member"
    if "no base method was found" in message:
        return "missing base method in provider stub"
    if code in {"call-arg", "call-overload"}:
        return "constructor signature too narrow"
    if code in {"return-value", "type-var"}:
        return "factory return type too narrow"
    if code == "operator":
        if "not callable" in message or "LazyImport" in message:
            return "callable LazyImport / lazy factory surface"
        return "Sage numeric/operator protocol missing"
    if "Cannot override final" in message or code == "override":
        return "incorrect final/override declaration"
    if "Category" in message or "Category" in source_line:
        return "dynamic category attribute missing"
    return "generic inheritance/protocol missing"


def suggested_sidecar_file(sage_module: str | None, source_line: str) -> str | None:
    if sage_module:
        return f"{sage_module.replace('.', '/')}.pyi"
    import_match = re.search(r"\bsage\.([A-Za-z0-9_.]+)\b", source_line)
    if import_match:
        return f"sage/{import_match.group(1).replace('.', '/')}.pyi"
    return None


def agent_bundle(entry: dict[str, Any], failure: str) -> str:
    area = str(entry["root_area"])
    if area in {"cat"} or failure == "dynamic category attribute missing":
        return "category core and dynamic category constructors"
    if area in {"homsets"} or any(token in failure for token in ("base method", "final/override")):
        return "homsets, morphisms, endsets, autsets"
    if area in {"rings", "algebras"}:
        return "rings and polynomial-family constructors"
    if area in {"modules", "forms", "tensor_algebra_components"}:
        return "modules, vector spaces, matrix spaces, subobjects"
    if area in {"sets"} or "numeric/operator" in failure:
        return "sets, infinity/cardinality, numeric protocols"
    return "smaller families: algebras/forms/posets/lattices/topological spaces"


def confidence(entry: dict[str, Any], sage_module: str | None, source_line: str) -> str:
    if entry["owner"] == "missing sidecar ordinary signature" and sage_module:
        return "high"
    if sage_module or "sage." in source_line:
        return "medium"
    return "low"


def downstream_cluster(entry: dict[str, Any]) -> str:
    return f"{entry['root_area']}:{entry['code']}:{entry['owner']}"


def build_rows(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, entry in enumerate(entries, start=1):
        source_line = read_source_line(str(entry["path"]), int(entry["line"]))
        if not is_stub_candidate(entry, source_line):
            continue
        sage_module = sage_module_from_entry(entry, source_line)
        sage_symbol = sage_symbol_from_entry(entry, source_line)
        failure = failure_kind(entry, source_line)
        rows.append(
            {
                "diagnostic_id": f"sage-stub-{index:04d}",
                "research_file": entry["path"],
                "line": entry["line"],
                "mypy_code": entry["code"],
                "sage_module": sage_module,
                "sage_symbol": sage_symbol,
                "member_or_signature": sage_symbol,
                "failure_kind": failure,
                "agent_bundle": agent_bundle(entry, failure),
                "evidence": {
                    "mypy_message": entry["message"],
                    "source_line": source_line,
                    "ledger_owner": entry["owner"],
                },
                "runtime_probe_required": True,
                "suggested_sidecar_file": suggested_sidecar_file(sage_module, source_line)
                or "runtime probe must identify Sage module before editing",
                "downstream_error_cluster": downstream_cluster(entry),
                "confidence": confidence(entry, sage_module, source_line),
            }
        )
    return rows


def counts(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    counter = collections.Counter(str(row.get(key)) for row in rows)
    return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0])))


def write_markdown(payload: dict[str, Any], path: Path) -> None:
    lines = [
        "# Category Specs Sage Stub Backlog",
        "",
        "This backlog is a runtime-verification queue for Sage-stub agents. A row is not",
        "a claim that the sidecar is wrong; it is a Sage-shaped diagnostic that should",
        "be checked against actual Sage behavior before editing `sage-stubs`.",
        "",
        f"- source_ledger: `{payload['source_ledger']}`",
        f"- ordinary_error_count: {payload['ordinary_error_count']}",
        f"- stub_candidate_count: {payload['stub_candidate_count']}",
        f"- non_candidate_count: {payload['non_candidate_count']}",
        "",
        "## Toolchain",
        "",
    ]
    for key, value in payload["toolchain"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Counts By Failure Kind", ""])
    for kind, count in payload["counts_by_failure_kind"].items():
        lines.append(f"- {kind}: {count}")
    lines.extend(["", "## Counts By Agent Bundle", ""])
    for bundle, count in payload["counts_by_agent_bundle"].items():
        lines.append(f"- {bundle}: {count}")
    lines.extend(["", "## Counts By Suggested Sidecar File", ""])
    for file, count in list(payload["counts_by_sidecar_file"].items())[:40]:
        lines.append(f"- {file}: {count}")
    lines.extend(["", "## Representative Rows", ""])
    for row in payload["rows"][:60]:
        lines.append(
            "- "
            f"{row['diagnostic_id']} / {row['failure_kind']} / "
            f"{row['confidence']} / `{row['research_file']}:{row['line']}` / "
            f"{row['suggested_sidecar_file']}: {row['evidence']['mypy_message']}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract Sage-stub candidate backlog from category_specs mypy ledger."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    ledger = json.loads(args.input.read_text(encoding="utf-8"))
    errors = ledger["errors"]
    rows = build_rows(errors)
    payload = {
        "source_ledger": str(args.input.relative_to(ROOT)),
        "toolchain": {
            "research_sha": git_sha(ROOT),
            "plugin_sha": git_sha(Path("/home/dzack/sage-mypy-plugin")),
            "sidecar_sha": git_sha(Path("/home/dzack/sage-mypy-plugin/sage-stubs")),
        },
        "ordinary_error_count": ledger["ordinary_error_count"],
        "stub_candidate_count": len(rows),
        "non_candidate_count": ledger["ordinary_error_count"] - len(rows),
        "counts_by_failure_kind": counts(rows, "failure_kind"),
        "counts_by_agent_bundle": counts(rows, "agent_bundle"),
        "counts_by_sidecar_file": counts(rows, "suggested_sidecar_file"),
        "rows": rows,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "latest.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_markdown(payload, args.output_dir / "latest.md")
    print(f"wrote {args.output_dir / 'latest.json'}")
    print(f"wrote {args.output_dir / 'latest.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
