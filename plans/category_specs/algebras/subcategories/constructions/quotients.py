r"""Quotient algebras."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.quotients import QuotientsCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraElement, AlgebraMorphism


class _Quotients(QuotientsCategory):
    r"""Quotient objects in a category of algebras."""

    class ParentMethods:
        @abstract_method
        def ambient(self) -> Algebra: ...

        @abstract_method
        def lift(self, x: AlgebraElement) -> AlgebraElement: ...

        @abstract_method
        def retract(self, x: AlgebraElement) -> AlgebraElement: ...

        @abstract_method
        def quotient_projection(self) -> AlgebraMorphism: ...
