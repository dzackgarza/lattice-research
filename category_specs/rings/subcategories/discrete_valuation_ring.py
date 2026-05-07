r"""DiscreteValuationRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.discrete_valuation import (
    DiscreteValuationRings as SageDiscreteValuationRings,
)
from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .valued import _ValuedRings as _ValuedRings

from ._lazy_subcategories import _EuclideanDomains


if TYPE_CHECKING:
    from ...types import (
        RingElement,
    )


class _DiscreteValuationRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().WithValuation().DiscretelyValued()``."""

    _base_category_class_and_axiom = (_ValuedRings, "DiscretelyValued")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "discrete valuation rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageDiscreteValuationRings(), _EuclideanDomains(), _ValuedRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageDiscreteValuationRings() or (
            R in self.base_category() and R.is_discrete_valuation_ring()
        )

    class ParentMethods:
        @override
        @final
        def is_discrete_valuation_ring(self) -> bool:
            return True

        @abstract_method
        def uniformizer_pow(self, n: Integer) -> RingElement: ...

        @abstract_method
        def residue_characteristic(self) -> Integer: ...

    class ElementMethods: ...

    class MorphismMethods: ...
