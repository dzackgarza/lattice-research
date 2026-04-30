r"""Algebras equipped with a distinguished basis."""

from __future__ import annotations

from typing import final
from typing import TYPE_CHECKING, Any

from sage.categories.algebras_with_basis import AlgebrasWithBasis as SageAlgebrasWithBasis
from ...cat import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from .. import Algebras

if TYPE_CHECKING:
    from ...types import (
        AlgebraBasis,
        AlgebraElement,
        CategoryElement,
        HochschildChainComplex,
        RModule,
        SetFamily,
    )


class _AlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    r"""Algebras with a distinguished basis."""

    _base_category_class_and_axiom = (Algebras, "WithBasis")
    FiniteDimensional = LazyImport(
        "category_specs.algebras.subcategories.finite_dimensional_with_basis",
        "_FiniteDimensionalAlgebrasWithBasis",
    )

    @final
    def super_categories(self) -> list:
        R = self.base_ring()
        return [Algebras(R), SageAlgebrasWithBasis(R)]

    @final
    def __contains__(self, A: Any) -> bool:
        return A in self.base_category() and A in SageAlgebrasWithBasis(self.base_ring())

    class ParentMethods:
        @abstract_method
        def basis(self) -> AlgebraBasis: ...

        @abstract_method
        def one_basis(self) -> CategoryElement: ...

        @abstract_method
        def product_on_basis(self, left: CategoryElement, right: CategoryElement) -> AlgebraElement: ...

        @abstract_method
        def algebra_generators(self) -> SetFamily: ...

        @abstract_method
        def hochschild_complex(self, coefficients: RModule) -> HochschildChainComplex: ...

    class ElementMethods:
        @abstract_method
        def __invert__(self) -> AlgebraElement: ...
