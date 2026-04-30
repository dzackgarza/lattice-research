r"""Vector spaces and modules over fields."""

from __future__ import annotations

from typing import Any, final

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverField(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "OverField")

    @final
    def extra_super_categories(self):
        return [self.base_category().OverPID()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_field()

    class ParentMethods:
        @final
        def is_over_field(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
