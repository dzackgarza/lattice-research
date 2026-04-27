r"""One-object subcategory for Sage disjoint unions of enumerated sets."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement


def _Sets():
    from .. import Sets as _S

    return _S()


class _DisjointUnionEnumeratedSets(Category_singleton):
    r"""Countable coproduct of an indexed family of enumerated sets."""

    def super_categories(self) -> list:
        return [_Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def _is_a(self, x: SetElement) -> bool: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def _element_constructor_default(self, el: SetElement) -> SetElement: ...

        @abstract_method
        def _element_constructor_facade(self, el: SetElement) -> SetElement: ...
