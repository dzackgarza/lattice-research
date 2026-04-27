r"""Modules over principal ideal domains."""

from __future__ import annotations

from typing import Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring

from .. import Modules


class _OverPID(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "OverPID")

    def extra_super_categories(self):
        return [self.base_category().OverDedekindDomain()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_pid()

    class ParentMethods:
        def is_over_pid(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
