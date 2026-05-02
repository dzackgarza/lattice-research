r"""One-object subcategory for Sage ``IntegerRange`` parents."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement


from ...cat import Category
from .. import Sets


class _IntegerRangeSets(Category_singleton):
    r"""Arithmetic progressions of integers, finite or infinite by bounds."""

    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Facade()]

    class ParentMethods:
        @abstract_method
        def _element_constructor_(self, el: SetElement) -> SetElement: ...

        @abstract_method
        def __contains__(self, elt: Any) -> bool: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def rank(self, x: SetElement) -> Integer: ...

        @abstract_method
        def __getitem__(self, i: Integer) -> SetElement: ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
