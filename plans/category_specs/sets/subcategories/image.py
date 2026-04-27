r"""One-object subcategories for images of sets under maps."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement, SympySet


from .. import Sets


class _ImageSets(Category_singleton):
    r"""Image subobjects ``{f(x) | x in X}`` under a set map."""

    def super_categories(self) -> list:
        return [Sets().Subobjects()]

    class ParentMethods:
        @abstract_method
        def __eq__(self, other: Set) -> bool: ...

        @abstract_method
        def __ne__(self, other: Set) -> bool: ...

        @abstract_method
        def __hash__(self) -> int: ...

        @abstract_method
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def ambient(self) -> Set: ...

        @abstract_method
        def lift(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def retract(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
