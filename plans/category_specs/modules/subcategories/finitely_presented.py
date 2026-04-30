r"""Finitely presented modules."""

from __future__ import annotations

from typing import Any, final

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _FinitelyPresented(CategoryWithAxiom_over_base_ring):
    r"""Modules presented as ``coker(f: R^m -> R^n)`` for finite ``m,n``."""

    _base_category_class_and_axiom = (Modules, "FinitelyPresented")

    @final
    def extra_super_categories(self):
        return [self.base_category().FinitelyGenerated()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_presented()

    class ParentMethods:
        @final
        def is_finitely_presented(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
