r"""Finite-dimensional algebras with basis."""

from __future__ import annotations

from typing import final
from ...cat import CategoryWithAxiom_over_base_ring
from sage.categories.finite_dimensional_algebras_with_basis import (
    FiniteDimensionalAlgebrasWithBasis as SageFiniteDimensionalAlgebrasWithBasis,
)

from .. import Algebras
from .with_basis import _AlgebrasWithBasis


class _FiniteDimensionalAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    r"""Finite-dimensional algebras with a distinguished basis."""

    _base_category_class_and_axiom = (_AlgebrasWithBasis, "FiniteDimensional")

    @final
    def super_categories(self) -> list:
        R = self.base_ring()
        return [
            Algebras(R).FiniteDimensional(),
            Algebras(R).WithBasis(),
            SageFiniteDimensionalAlgebrasWithBasis(R),
        ]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
