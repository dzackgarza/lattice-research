r"""Torsion modules."""

from __future__ import annotations

from typing import Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring

from .. import Modules


class _Torsion(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "Torsion")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_torsion()

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
