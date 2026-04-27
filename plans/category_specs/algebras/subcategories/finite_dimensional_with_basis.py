r"""Finite-dimensional algebras with basis."""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.finite_dimensional_algebras_with_basis import (
    FiniteDimensionalAlgebrasWithBasis as SageFiniteDimensionalAlgebrasWithBasis,
)

from .. import Algebras
from .with_basis import _AlgebrasWithBasis


class _FiniteDimensionalAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    r"""Finite-dimensional algebras with a distinguished basis."""

    _base_category_class_and_axiom = (_AlgebrasWithBasis, "FiniteDimensional")

    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Algebras(R).FiniteDimensional(),
            Algebras(R).WithBasis(),
            SageFiniteDimensionalAlgebrasWithBasis(R),
        ]
