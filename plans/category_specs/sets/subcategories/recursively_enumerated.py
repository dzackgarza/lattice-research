r"""One-object subcategory for Sage recursively enumerated sets."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import TYPE_CHECKING, Any, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, CategoryElement, DiGraph, InfinityElement, Integer, Set, SetElement


from ...cat import Category
from .. import Sets


class _RecursivelyEnumeratedSets(Category_singleton):
    r"""Sets generated from seeds and successor functions."""

    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def __len__(self) -> Integer: ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def __contains__(self, elt: Any) -> bool: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def graded_component_iterator(self) -> Iterator[Set]: ...

        @abstract_method
        def elements_of_depth_iterator(self, depth: Integer) -> Iterator[SetElement]: ...

        @abstract_method
        def breadth_first_search_iterator(
            self,
            max_depth: Integer | InfinityElement | None = None,
        ) -> Iterator[SetElement]: ...

        @abstract_method
        def naive_search_iterator(self) -> Iterator[SetElement]: ...

        @abstract_method
        def depth_first_search_iterator(self) -> Iterator[SetElement]: ...

        @abstract_method
        def to_digraph(
            self,
            max_depth: Integer | InfinityElement | None = None,
            loops: bool = True,
            multiedges: bool = True,
        ) -> DiGraph: ...

        @abstract_method
        def roots(self) -> Set: ...

        @abstract_method
        def children(self, x: SetElement) -> Set: ...

        @abstract_method
        def map_reduce(
            self,
            map_function: Callable[[SetElement], CategoryElement] | None = None,
            reduce_function: Callable[[CategoryElement, CategoryElement], CategoryElement] | None = None,
            reduce_init: CategoryElement | Integer | None = None,
        ) -> CategoryElement | Integer:
            r"""Run Sage's recursive map-reduce traversal."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
