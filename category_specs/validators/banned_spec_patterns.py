#!/usr/bin/env python3
"""Report category-spec patterns that hide mathematical mistakes."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    message: str
    action: str


@dataclass(frozen=True)
class Finding:
    path: str
    line_number: int
    rule: Rule
    line: str
    staged: bool

    @property
    def location(self) -> str:
        return f"{self.path}:{self.line_number}"


RULES = (
    Rule(
        name="typing-cast-call",
        pattern=re.compile(r"\bcast\s*\("),
        message=(
            "category_specs spec code must not use typing.cast; "
            "fix the owner/type surface instead"
        ),
        action=(
            "Replace with a real annotation, protocol, public semantic type, "
            "or category/plugin model change; do not silence the checker."
        ),
    ),
    Rule(
        name="typing-cast-import",
        pattern=re.compile(r"\bimport\b.*\bcast\b"),
        message="category_specs spec code must not import typing.cast",
        action=(
            "Remove the import after replacing all casts in the file with "
            "source-grounded types or framework fixes."
        ),
    ),
    Rule(
        name="with-axiom-helper-on-self",
        pattern=re.compile(r"\bwith_axiom\s*\(\s*self\s*,\s*['\"]"),
        message=(
            "axiom SubcategoryMethods must use Sage's "
            "self._with_axiom(...) binding idiom"
        ),
        action=(
            "Use self._with_axiom(\"A\") and verify the corresponding class "
            "is bound on the base named by _base_category_class_and_axiom."
        ),
    ),
    Rule(
        name="cached-method-import",
        pattern=re.compile(r"from\s+sage\.misc\.cachefunc\s+import\s+cached_method"),
        message=(
            "category_specs spec code must not import cached_method without "
            "a source-grounded Sage runtime need"
        ),
        action=(
            "Remove cached_method plumbing from mathematical spec selectors unless "
            "the file records a Sage category identity/cache obligation; plain "
            "selectors should state the category operation directly."
        ),
    ),
    Rule(
        name="cached-method-adapter",
        pattern=re.compile(
            r"\bdef\s+_\w*cached_method\b|_\w*cached_method\s*=\s*cast\s*\("
        ),
        message=(
            "local cached_method adapters are engineering wrappers, not "
            "mathematical spec content"
        ),
        action=(
            "Delete local cached_method adapters; if caching is required by Sage "
            "runtime semantics, centralize and document that interop boundary "
            "instead of scattering wrapper aliases through spec files."
        ),
    ),
    Rule(
        name="cached-method-decorator",
        pattern=re.compile(r"^\s*@\w*cached_method\b"),
        message=(
            "cached_method decorators in category specs are suspect runtime "
            "plumbing and must be justified"
        ),
        action=(
            "Remove the decorator unless the selector's cached category identity is "
            "a documented Sage interop requirement; do not add cached_method to "
            "quiet typing or imitate prior agent output."
        ),
    ),
)

SPEC_PATH_PREFIX = "category_specs/"
EXCLUDED_PREFIXES = ("category_specs/validators/",)
AXIOM_HELPER_PATTERN = re.compile(
    r"\bwith_axiom\s*\(\s*self\s*,\s*['\"](?P<axiom>[^'\"]+)['\"]"
)


def tracked_spec_python_paths() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", SPEC_PATH_PREFIX],
        check=True,
        text=True,
        capture_output=True,
    )
    return [
        path
        for path in result.stdout.splitlines()
        if path.endswith(".py") and not path.startswith(EXCLUDED_PREFIXES)
    ]


def staged_spec_python_paths() -> set[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        check=True,
        text=True,
        capture_output=True,
    )
    return {
        path
        for path in result.stdout.splitlines()
        if path.startswith(SPEC_PATH_PREFIX)
        and path.endswith(".py")
        and not path.startswith(EXCLUDED_PREFIXES)
    }


def location_list(findings: Iterable[Finding]) -> str:
    return ", ".join(str(finding.line_number) for finding in findings)


def axiom_names(findings: Iterable[Finding]) -> str:
    names: list[str] = []
    for finding in findings:
        match = AXIOM_HELPER_PATTERN.search(finding.line)
        if match:
            names.append(match.group("axiom"))
    return ", ".join(dict.fromkeys(names))


def findings_by_path(findings: Iterable[Finding]) -> dict[str, list[Finding]]:
    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.path].append(finding)
    return dict(grouped)


def print_repair_frontier(title: str, findings: list[Finding]) -> None:
    print(title)
    if not findings:
        print("- none")
        return

    grouped = findings_by_path(findings)
    for path, file_findings in sorted(
        grouped.items(), key=lambda item: (-len(item[1]), item[0])
    ):
        by_rule: dict[str, list[Finding]] = defaultdict(list)
        for finding in file_findings:
            by_rule[finding.rule.name].append(finding)

        print(f"- {path}: {len(file_findings)} findings")

        import_findings = by_rule.get("typing-cast-import", [])
        if import_findings:
            print(
                "  - remove typing.cast imports at lines "
                f"{location_list(import_findings)} after replacing casts in this file"
            )

        cast_findings = by_rule.get("typing-cast-call", [])
        if cast_findings:
            any_casts = [
                finding for finding in cast_findings if "cast(Any" in finding.line
            ]
            print(
                "  - eliminate cast calls at lines "
                f"{location_list(cast_findings)}"
            )
            if any_casts:
                print(
                    "  - highest-risk Any casts at lines "
                    f"{location_list(any_casts)}; these require a real owner/type "
                    "surface, not a narrower local assertion"
                )

        axiom_findings = by_rule.get("with-axiom-helper-on-self", [])
        if axiom_findings:
            names = axiom_names(axiom_findings)
            suffix = f" for axioms {names}" if names else ""
            print(
                "  - replace with_axiom(self, ...) selectors at lines "
                f"{location_list(axiom_findings)} with self._with_axiom(...){suffix}"
            )
            print(
                "  - verify each named axiom is a descriptor on the exact "
                "_base_category_class_and_axiom base class identity"
            )

        cached_import_findings = by_rule.get("cached-method-import", [])
        if cached_import_findings:
            print(
                "  - remove cached_method imports at lines "
                f"{location_list(cached_import_findings)} unless this file records "
                "a concrete Sage runtime identity/cache obligation"
            )

        cached_adapter_findings = by_rule.get("cached-method-adapter", [])
        if cached_adapter_findings:
            print(
                "  - delete local cached_method adapters at lines "
                f"{location_list(cached_adapter_findings)}; wrapper aliases are "
                "engineering leakage in spec code"
            )

        cached_decorator_findings = by_rule.get("cached-method-decorator", [])
        if cached_decorator_findings:
            print(
                "  - review cached_method decorators at lines "
                f"{location_list(cached_decorator_findings)}; keep only if a "
                "source-grounded Sage category identity/cache requirement is visible"
            )


def print_exact_findings(title: str, findings: list[Finding]) -> None:
    print(title)
    if not findings:
        print("- none")
        return

    for finding in findings:
        staged_marker = " [staged]" if finding.staged else ""
        print(
            f"- {finding.location}{staged_marker}: "
            f"{finding.rule.name}: {finding.rule.message}"
        )
        print(f"  Code: {finding.line.strip()}")


def main() -> int:
    fail_on_staged = "--fail-on-staged" in sys.argv[1:]
    staged_paths = staged_spec_python_paths()
    findings: list[Finding] = []
    for path in tracked_spec_python_paths():
        text = Path(path).read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for rule in RULES:
                if rule.pattern.search(line):
                    findings.append(
                        Finding(
                            path=path,
                            line_number=line_number,
                            rule=rule,
                            line=line,
                            staged=path in staged_paths,
                        )
                    )

    if findings:
        staged_findings = [finding for finding in findings if finding.staged]
        by_rule = Counter(finding.rule.name for finding in findings)
        staged_by_rule = Counter(finding.rule.name for finding in staged_findings)
        by_file = Counter(finding.path for finding in findings)
        print("WARNING: category_specs spec code contains banned patterns.")
        print()
        print("Summary:")
        print(f"- scanned files: {len(tracked_spec_python_paths())}")
        print(f"- affected files: {len(by_file)}")
        print(f"- total findings: {len(findings)}")
        print(f"- staged affected files: {len({f.path for f in staged_findings})}")
        print(f"- staged findings: {len(staged_findings)}")
        print(f"- mode: {'fail on staged findings' if fail_on_staged else 'warning only'}")
        print()
        print_repair_frontier("Immediate staged repair frontier:", staged_findings)
        print()
        print("Findings by rule:")
        for rule in RULES:
            total = by_rule[rule.name]
            staged = staged_by_rule[rule.name]
            if total:
                print(f"- {rule.name}: {total} total, {staged} staged")
                print(f"  Action: {rule.action}")
        print()
        print("Repo-wide inherited debt by file:")
        for path, count in by_file.most_common():
            staged_marker = " staged" if path in staged_paths else ""
            print(f"- {path}: {count}{staged_marker}")
        print()
        inherited_findings = [finding for finding in findings if not finding.staged]
        print_repair_frontier("Repo-wide inherited repair frontier:", inherited_findings)
        print()
        print_exact_findings("Exact staged findings:", staged_findings)
        print()
        print_exact_findings("Exact inherited findings:", inherited_findings)

        if fail_on_staged and staged_findings:
            print()
            print(
                "Commit rejected: staged category_specs files still contain "
                f"{len(staged_findings)} banned pattern findings."
            )
            return 1
        print()
        print(
            f"Warning-only result: {len(findings)} repo-wide findings remain. "
            f"Use --fail-on-staged to reject commits touching the "
            f"{len(staged_findings)} staged findings."
        )
        return 0

    print("No banned category_specs spec patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
