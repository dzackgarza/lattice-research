r"""Algebra ideals as module subobjects."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category, Category_module
from ....modules import Modules

if TYPE_CHECKING:
    from ....types import Algebra


class _Ideals(Category_module):
    r"""``R``-submodules that are ideals in an ``R``-algebra.

    Canonical chain: ``Algebras(R).Ideals(A)``.
    """

    @final
    def __init__(self, algebra: Algebra) -> None:
        self._algebra = algebra
        Category_module.__init__(self, algebra.base_ring())

    @final
    def algebra(self) -> Algebra:
        return self._algebra

    @final
    def _repr_object_names(self) -> str:
        return f"ideals of {self.algebra()}"

    @final
    def super_categories(self) -> list[Category]:
        return [Modules(self.base_ring()).Subobjects()]

    class ParentMethods:
        @abstract_method
        def is_left_ideal(self) -> bool: ...

        @abstract_method
        def is_right_ideal(self) -> bool: ...

        @final
        def is_two_sided_ideal(self) -> bool:
            return self.is_left_ideal() and self.is_right_ideal()

    class ElementMethods: ...
    class MorphismMethods: ...


AlgebraIdealsCategory = _Ideals
AlgebraIdealsObject = _Ideals.ParentMethods
AlgebraIdealsElement = _Ideals.ElementMethods
AlgebraIdealsMorphism = _Ideals.MorphismMethods
AlgebraIdeal = AlgebraIdealsObject
