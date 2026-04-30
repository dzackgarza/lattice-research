r"""Modules equipped with bilinear forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import _WithForms

if TYPE_CHECKING:
    from ...types import RModuleElement


class _BilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, b)`` with ``b`` bilinear on ``M``."""

    _base_category_class_and_axiom = (_WithForms, "Bilinear")

    class ParentMethods:
        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)
