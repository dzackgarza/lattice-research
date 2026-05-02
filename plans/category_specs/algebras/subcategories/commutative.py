r"""Commutative algebras."""

from __future__ import annotations

from typing import Any, final

from sage.categories.commutative_algebras import CommutativeAlgebras as SageCommutativeAlgebras

from ...cat import Category, CategoryWithAxiom_over_base_ring
from .. import Algebras


class _CommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras whose multiplication is commutative."""

    _base_category_class_and_axiom = (Algebras, "Commutative")

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [Algebras(R), SageCommutativeAlgebras(R)]

    @final
    def __contains__(self, A: Any) -> bool:
        return A in self.base_category() and A in SageCommutativeAlgebras(self.base_ring())

    class ParentMethods:
        @final
        def is_commutative(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
