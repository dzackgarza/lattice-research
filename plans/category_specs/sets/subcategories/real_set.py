r"""One-object subcategory for Sage ``RealSet`` parents."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        RealInterval,
        RealNumber,
        RealOpenSet,
        RealSubset,
        Set,
        SetElement,
        SympySet,
    )


from .. import Sets


class _RealSets(Category_singleton):
    r"""Sage real subsets represented as finite unions of real intervals."""

    def super_categories(self) -> list:
        return [Sets().Topological(), Sets().Subobjects()]

    class ParentMethods:
        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def n_components(self) -> int: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def is_universe(self) -> bool: ...

        @abstract_method
        def get_interval(self, i: int) -> RealInterval: ...

        @abstract_method
        def ambient(self) -> Set: ...

        @abstract_method
        def lift(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def retract(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def union(self, *real_set_collection: RealSubset) -> RealSubset: ...

        @abstract_method
        def intersection(self, *real_set_collection: RealSubset) -> RealSubset: ...

        @abstract_method
        def inf(self) -> RealNumber: ...

        @abstract_method
        def sup(self) -> RealNumber: ...

        @abstract_method
        def complement(self) -> RealSubset: ...

        @abstract_method
        def difference(self, *other: RealSubset) -> RealSubset: ...

        @abstract_method
        def symmetric_difference(self, *other: RealSubset) -> RealSubset: ...

        @abstract_method
        def contains(self, x: SetElement) -> bool: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def is_subset(self, *other: RealSubset) -> bool: ...

        @abstract_method
        def is_open(self) -> bool: ...

        @abstract_method
        def is_closed(self) -> bool: ...

        @abstract_method
        def closure(self) -> RealSubset: ...

        @abstract_method
        def interior(self) -> RealOpenSet: ...

        @abstract_method
        def boundary(self) -> RealSubset: ...

        @abstract_method
        def convex_hull(self, *real_set_collection: RealSubset) -> RealSubset: ...

        @abstract_method
        def is_connected(self) -> bool: ...

        @abstract_method
        def is_disjoint(self, *other: RealSubset) -> bool: ...

        @abstract_method
        def are_pairwise_disjoint(self, *real_set_collection: RealSubset) -> bool: ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
