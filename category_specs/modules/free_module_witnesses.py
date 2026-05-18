"""Spec-core reports for free finite-rank module construction witnesses."""

from __future__ import annotations

from typing import Final

from category_specs.spec_core import (
    ComputedValue,
    ConstructionWitness,
    SpecObligation,
    SpecProvider,
    SpecRegistry,
    SpecReport,
)

_MODULE_MAPPING_SOURCE: Final = (
    ".agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    "SPEC-MAPPING-MODULES.md"
)
_SET_MAPPING_SOURCE: Final = (
    ".agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    "SPEC-MAPPING-SETS.md"
)
_MODULE_OWNERSHIP_SOURCE: Final = (
    ".agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    "SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING.md"
)
_SAGE_FREE_MODULE_SOURCE: Final = (
    "/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/"
    "sage/modules/free_module.py"
)
_SAGE_SETS_SOURCE: Final = (
    "/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/"
    "sage/categories/sets_cat.py"
)
_SAGE_ENUMERATED_SETS_SOURCE: Final = (
    "/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/"
    "sage/categories/enumerated_sets.py"
)

_CARRIER_OBLIGATION_ID: Final = "modules.free_finite_rank.cartesian_power_carrier"
_PRODUCT_CARDINALITY_OBLIGATION_ID: Final = "sets.cartesian_product.cardinality"
_PRODUCT_COUNTABILITY_OBLIGATION_ID: Final = "sets.cartesian_product.countability"
_PRODUCT_ENUMERATION_OBLIGATION_ID: Final = (
    "sets.cartesian_product.deterministic_enumeration"
)

_CARRIER_OBLIGATION: Final = SpecObligation(
    id=_CARRIER_OBLIGATION_ID,
    title="Free finite-rank modules expose their carrier as a Cartesian power",
    source=_MODULE_MAPPING_SOURCE,
    description=(
        "Owner: Modules(R).Free().FiniteRank(); prerequisite: a rank and base "
        "carrier whose finite Cartesian power is the underlying set."
    ),
)
_PRODUCT_CARDINALITY_OBLIGATION: Final = SpecObligation(
    id=_PRODUCT_CARDINALITY_OBLIGATION_ID,
    title="Cartesian products expose product cardinality",
    source="category_specs/sets/subcategories/cartesian_product.py",
    description=(
        "Owner: Sets().CartesianProducts(); prerequisite: factor cardinalities."
    ),
)
_PRODUCT_COUNTABILITY_OBLIGATION: Final = SpecObligation(
    id=_PRODUCT_COUNTABILITY_OBLIGATION_ID,
    title="Finite Cartesian powers of countable carriers remain countable",
    source=_SET_MAPPING_SOURCE,
    description=(
        "Owner: Sets().CartesianProducts(); prerequisite: countable factor "
        "enumerations and finite product arity."
    ),
)
_PRODUCT_ENUMERATION_OBLIGATION: Final = SpecObligation(
    id=_PRODUCT_ENUMERATION_OBLIGATION_ID,
    title="Countable Cartesian powers expose deterministic enumeration",
    source=_SET_MAPPING_SOURCE,
    description=(
        "Owner: Sets().CartesianProducts(); prerequisite: a canonical product "
        "enumeration provider for countable factors. This is intentionally not "
        "satisfied by module-local iteration."
    ),
)

_PRODUCT_CARDINALITY_PROVIDER: Final = SpecProvider(
    id="sets.cartesian_product.cardinality",
    category="Sets().CartesianProducts()",
    provides=(_PRODUCT_CARDINALITY_OBLIGATION_ID,),
    source="category_specs/sets/subcategories/cartesian_product.py",
    description=(
        "Delegates to Sage Sets.CartesianProducts.ParentMethods.cardinality; "
        "module reports consume this as set/product evidence."
    ),
)
_PRODUCT_COUNTABILITY_PROVIDER: Final = SpecProvider(
    id="sets.cartesian_product.countable_finite_power",
    category="Sets().CartesianProducts()",
    provides=(_PRODUCT_COUNTABILITY_OBLIGATION_ID,),
    source=_SAGE_ENUMERATED_SETS_SOURCE,
    description=(
        "Finite Cartesian powers of Sage EnumeratedSets factors carry a countable "
        "factor-enumeration witness; the project countability contract is recorded "
        "in SPEC-MAPPING-SETS."
    ),
)


def gf5_rank3_report() -> SpecReport:
    """Return the vertical-slice report for ``GF(5)^3``."""
    from sage.all import GF

    return free_finite_rank_module_report(GF(5), 3, base_label="GF(5)")


def zz_rank2_report() -> SpecReport:
    """Return the vertical-slice report for ``ZZ^2``."""
    from sage.all import ZZ

    return free_finite_rank_module_report(ZZ, 2, base_label="ZZ")


def free_finite_rank_module_report(
    base_ring: object, rank: int, *, base_label: str | None = None
) -> SpecReport:
    """Build a spec-core report for the free module ``base_ring^rank``."""
    assert rank >= 0
    label = base_label or str(base_ring)
    carrier_label = f"CartesianPower({label}, {rank})"
    declared_category = f"Modules({label}).Free().FiniteRank()"

    from sage.all import cartesian_product
    from sage.rings.infinity import infinity

    carrier = cartesian_product([base_ring] * rank)
    cardinality = carrier.cardinality()

    inherited_obligation_ids = [
        _CARRIER_OBLIGATION_ID,
        _PRODUCT_CARDINALITY_OBLIGATION_ID,
    ]
    computed_values = [
        ComputedValue(
            name="carrier",
            value=carrier_label,
            source=f"{_MODULE_MAPPING_SOURCE}; {_SET_MAPPING_SOURCE}",
        ),
        ComputedValue(
            name="cardinality",
            value=str(cardinality),
            source=f"{_SAGE_SETS_SOURCE}; {_MODULE_OWNERSHIP_SOURCE}",
        ),
    ]

    if cardinality == infinity and _base_carrier_is_countable(base_ring):
        inherited_obligation_ids.extend(
            [
                _PRODUCT_COUNTABILITY_OBLIGATION_ID,
                _PRODUCT_ENUMERATION_OBLIGATION_ID,
            ]
        )
        computed_values.append(
            ComputedValue(
                name="countability",
                value="countably infinite",
                source=f"{_SET_MAPPING_SOURCE}; {_SAGE_FREE_MODULE_SOURCE}",
            )
        )

    registry = SpecRegistry(
        obligations=(
            _CARRIER_OBLIGATION,
            _PRODUCT_CARDINALITY_OBLIGATION,
            _PRODUCT_COUNTABILITY_OBLIGATION,
            _PRODUCT_ENUMERATION_OBLIGATION,
        ),
        providers=(_PRODUCT_CARDINALITY_PROVIDER, _PRODUCT_COUNTABILITY_PROVIDER),
        witnesses=(
            ConstructionWitness(
                id=f"modules.free_finite_rank.cartesian_power.{label}.{rank}",
                construction=carrier_label,
                source_category=declared_category,
                target_category="Sets().CartesianProducts()",
                provides=(_CARRIER_OBLIGATION_ID,),
                source=_MODULE_MAPPING_SOURCE,
                description=(
                    "Witnesses the underlying set of a free finite-rank module "
                    "as the finite Cartesian power of its base carrier."
                ),
            ),
        ),
    )

    return registry.report(
        subject=f"{label}^{rank}",
        declared_category=declared_category,
        inherited_obligation_ids=tuple(inherited_obligation_ids),
        computed_values=tuple(computed_values),
    )


def _base_carrier_is_countable(base_ring: object) -> bool:
    from sage.categories.enumerated_sets import EnumeratedSets

    return bool(base_ring in EnumeratedSets())
