r"""Commutative algebras."""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.commutative_algebras import CommutativeAlgebras as SageCommutativeAlgebras

from .. import Algebras


class _CommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras whose multiplication is commutative."""

    _base_category_class_and_axiom = (Algebras, "Commutative")

    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [Algebras(R), SageCommutativeAlgebras(R)]

    def __contains__(self, A: Any) -> bool:
        return A in self.base_category() and A in SageCommutativeAlgebras(self.base_ring())

    class ParentMethods:
        def is_commutative(self) -> bool:
            return True
