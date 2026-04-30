r"""Modules over local rings."""

from __future__ import annotations

from typing import Any

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverLocalRing(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "OverLocalRing")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_local_ring()

    class ParentMethods:
        def is_over_local_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
