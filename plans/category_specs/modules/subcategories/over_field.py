r"""Vector spaces and modules over fields."""

from __future__ import annotations

from typing import Any

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverField(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "OverField")

    def extra_super_categories(self):
        return [self.base_category().OverPID()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_field()

    class ParentMethods:
        def is_over_field(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
