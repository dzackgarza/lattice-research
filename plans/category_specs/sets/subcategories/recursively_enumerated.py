r"""One-object subcategory for Sage recursively enumerated sets."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement


from .. import Sets


class _RecursivelyEnumeratedSets(Category_singleton):
    r"""Sets generated from seeds and successor functions."""

    def super_categories(self) -> list:
        return [Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def __len__(self) -> int: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def __contains__(self, elt: Any) -> bool: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def graded_component_iterator(self): ...

        @abstract_method
        def elements_of_depth_iterator(self, depth: int): ...

        @abstract_method
        def breadth_first_search_iterator(self, max_depth=None): ...

        @abstract_method
        def naive_search_iterator(self): ...

        @abstract_method
        def depth_first_search_iterator(self): ...

        @abstract_method
        def to_digraph(self, max_depth=None, loops: bool = True, multiedges: bool = True): ...

        @abstract_method
        def roots(self) -> Set: ...

        @abstract_method
        def children(self, x: SetElement) -> Set: ...

        @abstract_method
        def map_reduce(self, map_function=None, reduce_function=None, reduce_init=None):
            r"""Run Sage's recursive map-reduce traversal."""
            ...
