r"""Modules over integral domains."""

from __future__ import annotations

from typing import Any

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverIntegralDomain(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (Modules, "OverIntegralDomain")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_integral_domain()

    class ParentMethods:
        def is_over_integral_domain(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...
