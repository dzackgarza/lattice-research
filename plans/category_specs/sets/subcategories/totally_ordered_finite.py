r"""One-object subcategory for Sage ``TotallyOrderedFiniteSet`` parents."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement


from .. import Sets


class _TotallyOrderedFiniteSets(Category_singleton):
    r"""Finite sets equipped with a user-specified total order."""

    def super_categories(self) -> list:
        return [Sets().Countable().Finite(), Sets().TotallyOrdered()]

    class ParentMethods:
        @abstract_method
        def _element_constructor_(self, data: SetElement) -> SetElement: ...

        @abstract_method
        def le(self, x: SetElement, y: SetElement) -> bool: ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def rank(self, x: SetElement) -> Integer: ...

        @abstract_method
        def unrank(self, n: Integer) -> SetElement: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def min(self) -> SetElement: ...

        @abstract_method
        def max(self) -> SetElement: ...

    class ElementMethods:
        @abstract_method
        def __eq__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __ne__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __lt__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __le__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __gt__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __ge__(self, other: SetElement) -> bool: ...
