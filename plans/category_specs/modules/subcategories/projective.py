r"""Projective modules."""

from __future__ import annotations

from typing import Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring

from .. import Modules


class _Projective(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "Projective")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_projective()

    class ParentMethods:
        def is_projective(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
