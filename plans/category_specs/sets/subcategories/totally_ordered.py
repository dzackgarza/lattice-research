r"""Totally ordered set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Integer, SetElement

from .. import Sets


class _TotallyOrdered(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "TotallyOrdered")

    def _repr_object_names(self) -> str:
        return "totally ordered sets"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def is_totally_ordered(self) -> bool:
            return True

        @abstract_method
        def rank(self, x: SetElement) -> Integer: ...

        @abstract_method
        def unrank(self, n: Integer) -> SetElement: ...

        @abstract_method
        def min(self) -> SetElement: ...

        @abstract_method
        def max(self) -> SetElement: ...

    class ElementMethods:
        @abstract_method
        def __lt__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __le__(self, other: SetElement) -> bool: ...

        def __gt__(self, other: SetElement) -> bool:
            return other.__lt__(self)

        def __ge__(self, other: SetElement) -> bool:
            return other.__le__(self)
