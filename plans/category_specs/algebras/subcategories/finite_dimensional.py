r"""Finite-dimensional algebras."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method

from .. import Algebras

if TYPE_CHECKING:
    from ...types import Algebra, AlgebraElement, Integer


class _FiniteDimensionalAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras that are finite-dimensional over their base ring."""

    _base_category_class_and_axiom = (Algebras, "FiniteDimensional")

    def super_categories(self) -> list[Category]:
        return [Algebras(self.base_ring())]

    def __contains__(self, A: Any) -> bool:
        return A in self.base_category() and A.dimension() < float("inf")

    class ParentMethods:
        @abstract_method
        def dimension(self) -> Integer: ...

        @abstract_method
        def radical(self) -> Algebra: ...

        @abstract_method
        def radical_basis(self) -> Sequence[AlgebraElement]: ...

        @abstract_method
        def semisimple_quotient(self) -> Algebra: ...

        @abstract_method
        def idempotent_lift(self, x: AlgebraElement) -> AlgebraElement: ...
