"""Generated-law style tests for SpecReport outputs in the spec-core slice."""

from __future__ import annotations

from collections.abc import Callable
from math import prod

import importlib

import pytest

importlib.import_module("sage.all")
spec_core = importlib.import_module("category_specs.spec_core")
witnesses = importlib.import_module("category_specs.modules.free_module_witnesses")

SpecReport = spec_core.SpecReport
SpecCheckResult = spec_core.SpecCheckResult


_PRODUCT_CARDINALITY_OBLIGATION_ID: str = "sets.cartesian_product.cardinality"
_PRODUCT_ENUMERATION_OBLIGATION_ID: str = (
    "sets.cartesian_product.deterministic_enumeration"
)


def _result_for_obligation(
    report: SpecReport, obligation_id: str
) -> SpecCheckResult:
    return report.obligation_result_by_id(obligation_id)


def _assert_obligation_status(
    report: SpecReport,
    obligation_id: str,
    expected_status: str,
) -> None:
    result = _result_for_obligation(report, obligation_id)
    assert result.status == expected_status


def _law_finite_product_cardinality_factors(report: SpecReport) -> None:
    assert report.computed_value("cardinality").value == str(prod((5,) * 3))
    _assert_obligation_status(
        report,
        _PRODUCT_CARDINALITY_OBLIGATION_ID,
        "satisfied_by_provider",
    )
    assert report.subject == "GF(5)^3"
    assert report.computed_value("carrier").value == "CartesianPower(GF(5), 3)"


def _law_countable_product_enumeration_is_missing(report: SpecReport) -> None:
    assert report.computed_value("countability").value == "countably infinite"
    assert report.computed_value("cardinality").value == "+Infinity"
    _assert_obligation_status(
        report, _PRODUCT_ENUMERATION_OBLIGATION_ID, "missing"
    )
    enumeration_result = _result_for_obligation(
        report, _PRODUCT_ENUMERATION_OBLIGATION_ID
    )
    assert enumeration_result.provider is None
    assert enumeration_result.witness is None
    assert "module-local iteration" in enumeration_result.obligation.description


_GENERATED_LAWS: tuple[
    tuple[str, Callable[[], SpecReport], tuple[Callable[[SpecReport], None], ...]],
] = (
    (
        "gf5_rank3_cardinality_matches_factor_product",
        witnesses.gf5_rank3_report,
        (_law_finite_product_cardinality_factors,),
    ),
    (
        "zz2_missing_countable_product_enumeration",
        witnesses.zz_rank2_report,
        (_law_countable_product_enumeration_is_missing,),
    ),
)


@pytest.mark.parametrize(
    "name,report_builder,laws",
    _GENERATED_LAWS,
    ids=[name for name, _, _ in _GENERATED_LAWS],
)
def test_generated_laws_for_spec_report(
    name: str,
    report_builder: Callable[[], SpecReport],
    laws: tuple[Callable[[SpecReport], None], ...],
) -> None:
    del name
    report = report_builder()
    for law in laws:
        law(report)
