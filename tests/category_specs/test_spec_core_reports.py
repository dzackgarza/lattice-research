"""Focused tests for the standalone spec-core report kernel."""

from __future__ import annotations

import sys
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path
from types import ModuleType


def _load_reports_module() -> ModuleType:
    repo_root = Path(__file__).resolve().parents[2]
    reports_path = repo_root / "category_specs" / "spec_core" / "reports.py"
    loader = SourceFileLoader("spec_core_reports_under_test", str(reports_path))
    spec = spec_from_loader(loader.name, loader)
    if spec is None:
        raise RuntimeError("could not build import spec for spec-core reports")
    module = module_from_spec(spec)
    sys.modules[loader.name] = module
    loader.exec_module(module)
    return module


reports = _load_reports_module()
SpecObligation = getattr(reports, "SpecObligation")
SpecProvider = getattr(reports, "SpecProvider")
ConstructionWitness = getattr(reports, "ConstructionWitness")
ComputedValue = getattr(reports, "ComputedValue")
SpecRegistry = getattr(reports, "SpecRegistry")


def test_registry_report_partitions_provider_witness_and_missing_obligations() -> None:
    finite_cardinality = SpecObligation(
        id="finite-cardinality",
        title="Finite objects expose their cardinality",
        source="category_specs/sets/subcategories/finite.py",
    )
    enumerability = SpecObligation(
        id="enumerability",
        title="Enumerated objects expose an iterator contract",
        source="category_specs/sets/subcategories/finite_enumerated_set.py",
    )
    free_rank = SpecObligation(
        id="free-rank",
        title="Free finite-rank modules expose rank",
        source="category_specs/modules/subcategories/free.py",
    )

    registry = SpecRegistry(
        obligations=(finite_cardinality, enumerability, free_rank),
        providers=(
            SpecProvider(
                id="finite-set-cardinality-methods",
                category="Sets().Finite()",
                provides=("finite-cardinality",),
                source="category_specs/sets/subcategories/finite.py",
            ),
        ),
        witnesses=(
            ConstructionWitness(
                id="cartesian-power-free-module-witness",
                construction="cartesian_power",
                source_category="Modules(GF(5)).Free()",
                target_category="Modules(GF(5)).Free().FinitelyPresented()",
                provides=("free-rank",),
                source=(
                    ".agents/plans/features/"
                    "FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/"
                    "PLAN-SPEC-CORE-VERTICAL-SLICE/"
                    "PHASE-SPEC-CORE-VERTICAL-SLICE"
                ),
            ),
        ),
    )

    report = registry.report(
        subject="GF(5)^3",
        declared_category="Modules(GF(5)).Free().FinitelyPresented()",
        inherited_obligation_ids=(
            "finite-cardinality",
            "free-rank",
            "enumerability",
        ),
        computed_values=(
            ComputedValue(
                name="cardinality",
                value="125",
                source="Sage GF(5)^3 cardinality",
            ),
        ),
    )

    assert report.declared_category == "Modules(GF(5)).Free().FinitelyPresented()"
    assert [result.obligation.id for result in report.satisfied_by_provider] == [
        "finite-cardinality"
    ]
    assert (
        report.satisfied_by_provider[0].provider.id
        == "finite-set-cardinality-methods"
    )
    assert [result.obligation.id for result in report.satisfied_by_witness] == [
        "free-rank"
    ]
    assert (
        report.satisfied_by_witness[0].witness.id
        == "cartesian-power-free-module-witness"
    )
    assert [(value.name, value.value) for value in report.computed_values] == [
        ("cardinality", "125")
    ]
    assert [result.obligation.id for result in report.missing_obligations] == [
        "enumerability"
    ]
    assert not report.is_complete()
    assert [result.status for result in report.all_results()] == [
        "satisfied_by_provider",
        "satisfied_by_witness",
        "missing",
    ]
