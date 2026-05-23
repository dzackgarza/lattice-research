#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import TypedDict

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = (
    ROOT / "reports" / "workstreams" / "category-specs-mypy-ledger" / "latest.json"
)
DEFAULT_OUTPUT_DIR = (
    ROOT / "reports" / "workstreams" / "category-specs-sage-stub-backlog"
)


class StubFamily(TypedDict):
    family: str
    row_count: int
    surface: str
    selector: str
    evidence: str
    acceptance: str
    falsifier: str


FAMILY_SPECS: tuple[tuple[str, int, str], ...] = (
    ("STUB-LAZYIMPORT-CALLABLE", 208, "LazyImport callable factory behavior"),
    ("STUB-RECURSIVELY-ENUMERATED-EXPORTS", 2, "recursively enumerated set exports"),
    ("STUB-SUBSETS-INTEGER-K", 1, "Subsets accepts Sage Integer for k"),
    ("STUB-ABSTRACTFAMILY-KEYS", 2, "AbstractFamily.keys"),
    ("STUB-CATEGORY-JOIN-MEET-AND", 7, "Category join, meet, and operator surface"),
    ("STUB-CATEGORY-TYPES-BASE-OBJECTS", 4, "category_types base-object initializers"),
    (
        "STUB-COMBINATORIAL-FREE-MODULE-CONSTRUCTOR",
        3,
        "CombinatorialFreeModule constructor",
    ),
    ("STUB-MATRIXSPACE-IMPLEMENTATION", 1, "MatrixSpace implementation argument"),
    ("STUB-POSETS-PARENTMETHODS-ORDER", 8, "Posets.ParentMethods order methods"),
    (
        "STUB-INTEGER-CONSTRUCTOR-AND-PROTOCOL",
        26,
        "Integer constructor and numeric protocol",
    ),
    (
        "STUB-MATRIX-CONSTRUCTOR-AND-BASE-TYPE",
        30,
        "matrix constructor and runtime base type",
    ),
    (
        "STUB-FREEMODULE-VECTORSPACE-CONSTRUCTORS",
        6,
        "FreeModule and VectorSpace constructors",
    ),
    (
        "STUB-CONDITIONSET-UNIVERSE-PREDICATES",
        4,
        "ConditionSet universe and predicates",
    ),
    ("STUB-MATRIXSPACE-MATRIX-SPACE-INTEGER-DIMS", 4, "MatrixSpace Integer dimensions"),
    (
        "STUB-FINITEPOSETS-SEMILATTICE-AND-CERTIFICATES",
        8,
        "FinitePoset semilattice and certificates",
    ),
    ("STUB-INFINITY-NEGATION", 3, "infinity singleton negation"),
    ("STUB-SETPARTITION-DIRECT-CLASSCALL", 2, "SetPartition direct classcall"),
    ("STUB-RATIONALFIELD-MISSING-PUBLIC-METHODS", 10, "RationalField public methods"),
    ("STUB-REALSET-PARENT-AN-ELEMENT", 1, "RealSet._an_element_"),
    ("STUB-IMAGESUBOBJECT-PARENT-AN-ELEMENT", 1, "ImageSubobject._an_element_"),
    ("STUB-REAL-ABC-TO-PREC", 3, "real-field to_prec protocol"),
    ("STUB-MATRIXSPACE-PARENT-BASE", 1, "MatrixSpace inherits Parent"),
    ("STUB-SAGE-CATEGORY-MEMBERSHIP-SURFACES", 23, "Sage category membership"),
    ("STUB-TENSORPRODUCTFUNCTOR-CALLABLE", 3, "TensorProductFunctor callable surface"),
    ("STUB-CATEGORY-BASE-ADDITIONAL-STRUCTURE", 1, "Category.additional_structure"),
    ("STUB-FINITE-RANK-FREE-MODULE-METHODS", 5, "finite-rank free-module methods"),
    (
        "STUB-COMMUTATIVE-RING-EXTENSION-AND-POLYNOMIAL-COMPLETION",
        3,
        "ring extension and polynomial completion",
    ),
)


def build_families() -> tuple[StubFamily, ...]:
    return tuple(
        {
            "family": family,
            "row_count": row_count,
            "surface": surface,
            "selector": "Exact selector is recorded in the stub task card.",
            "evidence": "Source/runtime evidence is recorded in the task card.",
            "acceptance": "Covered rows disappear after the stub surface is fixed.",
            "falsifier": "The task card states the family-specific falsifier.",
        }
        for family, row_count, surface in FAMILY_SPECS
    )


FAMILIES = build_families()


def git_sha(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def write_markdown(payload: dict[str, object], path: Path) -> None:
    families = payload["families"]
    assert isinstance(families, list)
    lines = [
        "# Category Specs Sage Stub External Blockers",
        "",
        "This report is the classified `sage-stubs`-owned external subset for the",
        "current `category_specs` QC frontier. It is not an unclassified",
        "discovery queue, not a request for `sage-stubs` to analyze",
        "the research ledger, and not a claim about local wrappers.",
        "",
        f"- source_ledger: `{payload['source_ledger']}`",
        f"- ordinary_error_count: {payload['ordinary_error_count']}",
        f"- sage_stubs_owned_row_count: {payload['sage_stubs_owned_row_count']}",
        f"- non_sage_stubs_row_count: {payload['non_sage_stubs_row_count']}",
        "- external_issue: `dzackgarza/sage-stubs#5`",
        "- local_and_math_records: existing QC task cards under",
        "  `.agents/plans/features/FEATURE-QC-WARNINGS-ZERO/`",
        "",
        "## Toolchain",
        "",
    ]
    toolchain = payload["toolchain"]
    assert isinstance(toolchain, dict)
    for key, value in toolchain.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Families", ""])
    for family in families:
        lines.extend(
            [
                f"### {family['family']}",
                "",
                f"- rows: {family['row_count']}",
                f"- surface: {family['surface']}",
                f"- selector: {family['selector']}",
                f"- evidence: {family['evidence']}",
                f"- acceptance: {family['acceptance']}",
                f"- falsifier: {family['falsifier']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Explicit Non-Goals",
            "",
            "- Do not add local wrapper concepts to `sage-stubs`.",
            "- Do not ask `sage-stubs` to analyze research-owned uncertainty.",
            "- Do not turn local research typing/design rows into stub requests.",
            "- Do not use `Any`, opaque `object`, or fake surfaces.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the classified sage-stubs-owned blocker report."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    ledger = json.loads(args.input.read_text(encoding="utf-8"))
    row_count = sum(family["row_count"] for family in FAMILIES)
    payload: dict[str, object] = {
        "source_ledger": str(args.input.relative_to(ROOT)),
        "toolchain": {
            "research_sha": ledger["toolchain"]["research_sha"],
            "plugin_sha": ledger["toolchain"]["plugin_sha"],
            "sidecar_sha": ledger["toolchain"]["sidecar_sha"],
        },
        "ordinary_error_count": ledger["ordinary_error_count"],
        "sage_stubs_owned_row_count": row_count,
        "non_sage_stubs_row_count": ledger["ordinary_error_count"] - row_count,
        "external_issue": "dzackgarza/sage-stubs#5",
        "families": list(FAMILIES),
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
