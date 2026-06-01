r"""One-object subcategory for Sage ``RealSet`` parents."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category_singleton import Category_singleton
from sage.rings.infinity import infinity, minus_infinity

if TYPE_CHECKING:
    from ...types import FiniteSet, RealInterval, RealNumber


from ...cat import Category
from .. import Sets


class _RealSets(Category_singleton):
    r"""Sage real subsets represented as finite unions of real intervals.

    Constructor target:
    named real-subset constructors under ``Sets().Constructors()`` refine here
    and then into the applicable topological subobject categories.

    A RealSet ``X`` carries a canonical basis expression as a finite set of
    disjoint intervals ``{X₁, …, Xₙ}`` with ``X = ∪ᵢ Xᵢ``, exposed via
    ``interval_components()``.  Topological predicates, closure, interior, and
    boundary are subspace operations owned by
    ``TopologicalSpaces().Subobjects()``.  Set operations such as ``union()``
    and ``intersection()`` are owned by ``Sets().Subobjects()``.
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
        @abstractmethod
        def interval_components(self) -> FiniteSet[RealInterval]:
            r"""Return the finite set of disjoint intervals whose union is ``self``."""
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
        @final
        def is_compact(self) -> bool:
            r"""Return whether this real subset is compact in the real line."""
            return self.is_empty() or (
                self.is_closed()
                and self.inf() is not minus_infinity
                and self.sup() is not infinity
            )

    class ElementMethods: ...
