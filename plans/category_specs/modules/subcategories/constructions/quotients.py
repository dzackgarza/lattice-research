r"""Quotient modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import RModMorphism, RModuleElement


class _Quotients(QuotientsCategory):
    r"""Quotient module category."""

    class ParentMethods:
        @abstract_method
        def projection(self) -> RModMorphism: ...

    class ElementMethods:
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)
