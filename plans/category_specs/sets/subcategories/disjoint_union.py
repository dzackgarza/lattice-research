r"""One-object subcategory for Sage disjoint unions of enumerated sets."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement


from .. import Sets
from ...cat import Category


class _DisjointUnionEnumeratedSets(Category_singleton):
    r"""Countable coproduct of an indexed family of enumerated sets."""

    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def _is_a(self, x: SetElement) -> bool: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def _element_constructor_default(self, el: SetElement) -> SetElement: ...

        @abstract_method
        def _element_constructor_facade(self, el: SetElement) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
