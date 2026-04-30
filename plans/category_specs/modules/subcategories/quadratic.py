r"""Modules equipped with quadratic forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import _WithForms

if TYPE_CHECKING:
    from ...types import RModuleElement


class _QuadraticModules(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, q)`` with ``q`` quadratic on ``M``."""

    _base_category_class_and_axiom = (_WithForms, "Quadratic")

    class ParentMethods:
        @final
        def q(self, v: RModuleElement) -> RModuleElement:
            return self.form().q(v)
