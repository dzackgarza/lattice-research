r"""Modules over commutative rings."""

from __future__ import annotations

from typing import Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring

from .. import Modules


class _OverCommutativeRing(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "OverCommutativeRing")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_commutative_ring()

    class ParentMethods:
        def is_over_commutative_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
