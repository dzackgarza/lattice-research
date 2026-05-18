r"""One-object subcategory for Sage ``RealSet`` parents."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, final, overload, override

from sage.categories.category_singleton import Category_singleton
from sage.rings.infinity import infinity, minus_infinity

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        Integer,
        RealInterval,
        RealNumber,
        RealSubset,
        SetElement,
        SympySet,
    )


from ...cat import Category
from .. import Sets


class _RealSets(Category_singleton):
    r"""Sage real subsets represented as finite unions of real intervals.

    Constructor target:
    named real-subset constructors under ``Sets().Constructors()`` refine here
    and then into the applicable topological subobject categories.

    Topological predicates and transforms such as ``is_open()``, ``is_closed()``,
    ``closure()``, ``interior()``, and ``boundary()`` are Sage compatibility methods on
    these real-line subset parents.  The project owner is the ambient-relative
    ``TopologicalSpaces()`` surface: ``U.ambient().closure(U)``,
    ``U.ambient().is_open(U)``, and analogous calls.  This category records the
    real-subset representation; it does not create a second topological owner.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        from ...topological_spaces import TopologicalSpaces

        return [
            Sets().Topological(),
            Sets().Subobjects(),
            TopologicalSpaces().Subobjects(),
        ]

    class ParentMethods:
        @override
        @abstractmethod
        def __iter__(self) -> Iterator[RealInterval]: ...

        @abstractmethod
        def n_components(self) -> Integer:
            r"""Return the number of interval components of this real subset."""
            ...

        @override
        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @override
        @abstractmethod
        def is_empty(self) -> bool: ...

        @abstractmethod
        def is_universe(self) -> bool:
            r"""Return whether this real subset is the whole real line."""
            ...

        @abstractmethod
        def category(self) -> Category: ...

        @abstractmethod
        def is_connected(self) -> bool: ...

        @abstractmethod
        def is_open(self) -> bool: ...

        @abstractmethod
        def is_closed(self) -> bool: ...

        @override
        @final
        def is_compact(self) -> bool:
            r"""Return whether this real subset is compact in the real line."""
            return self.is_empty() or (
                self.is_closed()
                and self.inf() is not minus_infinity
                and self.sup() is not infinity
            )

        @abstractmethod
        def get_interval(self, i: Integer) -> RealInterval:
            r"""Return the ``i``-th interval component of this real subset."""
            ...

        @abstractmethod
        def ambient(self) -> RealSubset: ...

        @abstractmethod
        def closure(self) -> RealSubset: ...

        @abstractmethod
        def interior(self) -> RealSubset: ...

        @abstractmethod
        def boundary(self) -> RealSubset: ...

        @overload
        def union(self, other: RealSubset) -> RealSubset: ...

        @overload
        def union(self, other: Sequence[RealSubset]) -> RealSubset: ...

        @override
        @abstractmethod
        def union(
            self,
            other: RealSubset | Sequence[RealSubset],
        ) -> RealSubset:
            r"""Return the finite-interval-normalized union."""
            ...

        @overload
        def intersection(self, other: RealSubset) -> RealSubset: ...

        @overload
        def intersection(self, other: Sequence[RealSubset]) -> RealSubset: ...

        @override
        @abstractmethod
        def intersection(
            self,
            other: RealSubset | Sequence[RealSubset],
        ) -> RealSubset:
            r"""Return the finite-interval-normalized intersection."""
            ...

        @abstractmethod
        def inf(self) -> RealNumber:
            r"""Return the infimum of this subset of the real line."""
            ...

        @abstractmethod
        def sup(self) -> RealNumber:
            r"""Return the supremum of this subset of the real line."""
            ...

        @override
        @abstractmethod
        def complement(self) -> RealSubset:
            r"""Return the finite-interval-normalized complement in the real line."""
            ...

        @override
        @abstractmethod
        def difference(self, other: RealSubset) -> RealSubset:
            r"""Return the finite-interval-normalized set difference."""
            ...

        @override
        @abstractmethod
        def symmetric_difference(self, other: RealSubset) -> RealSubset:
            r"""Return the finite-interval-normalized symmetric difference."""
            ...

        @abstractmethod
        def is_subset(self, other: RealSubset) -> bool: ...

        @abstractmethod
        def contains(self, x: SetElement) -> bool:
            r"""Return whether the real point ``x`` lies in this real subset."""
            ...

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool: ...

        @staticmethod
        @abstractmethod
        def convex_hull(real_set_collection: Sequence[RealSubset]) -> RealSubset:
            r"""Return the least real interval containing the given real subsets."""
            ...

        @abstractmethod
        def is_disjoint(self, other: RealSubset) -> bool:
            r"""Return whether this real subset is disjoint from ``other``."""
            ...

        @staticmethod
        @abstractmethod
        def are_pairwise_disjoint(real_set_collection: Sequence[RealSubset]) -> bool:
            r"""Return whether the real subsets are pairwise disjoint."""
            ...

        @override
        @abstractmethod
        def _an_element_(self) -> SetElement: ...

        @override
        @abstractmethod
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...
