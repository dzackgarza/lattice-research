r"""Subalgebras and algebra ideals as subobjects."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraElement, AlgebraMorphism


class _Subobjects(SubobjectsCategory):
    r"""Subobjects in a category of algebras."""

    class ParentMethods:
        @abstract_method
        def ambient(self) -> Algebra: ...

        @abstract_method
        def lift(self, x: AlgebraElement) -> AlgebraElement: ...

        @abstract_method
        def retract(self, x: AlgebraElement) -> AlgebraElement: ...

        @abstract_method
        def inclusion(self) -> AlgebraMorphism: ...

    class ElementMethods: ...
    class MorphismMethods: ...
