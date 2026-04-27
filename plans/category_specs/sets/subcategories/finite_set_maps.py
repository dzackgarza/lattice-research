r"""One-object subcategory for Sage finite sets of maps."""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
from typing import TYPE_CHECKING, Any, overload

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        FiniteSetMap,
        Set,
        SetElement,
    )


from .. import Sets


class _FiniteSetMapsSets(Category_singleton):
    r"""Finite sets of all maps between two finite sets.

    Sage's ``FiniteSetMaps(A, B)`` represents the parent whose elements are
    functions ``A -> B``.  The endomap case ``FiniteSetMaps(A)`` is the full
    transformation monoid of ``A`` under composition; Sage names its identity
    element ``one()``.
    """

    def super_categories(self) -> list:
        return [Sets().Countable().Finite()]

    class ParentMethods:
        @abstract_method
        def domain(self) -> Set: ...

        @abstract_method
        def codomain(self) -> Set: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def __iter__(self) -> Iterator[FiniteSetMap]: ...

        @abstract_method
        def _from_list_(self, v: list[SetElement]) -> FiniteSetMap: ...

        @overload
        def _element_constructor_(self, finite_map: FiniteSetMap, check: bool = True) -> FiniteSetMap: ...

        @overload
        def _element_constructor_(
            self,
            function: Callable[[SetElement], SetElement],
            check: bool = True,
        ) -> FiniteSetMap: ...

        @overload
        def _element_constructor_(self, images: Sequence[SetElement], check: bool = True) -> FiniteSetMap: ...

        @abstract_method
        def _element_constructor_(
            self,
            data: FiniteSetMap | Callable[[SetElement], SetElement] | Sequence[SetElement],
            check: bool = True,
        ) -> FiniteSetMap: ...

        @abstract_method
        def from_dict(self, d: dict[SetElement, SetElement]) -> FiniteSetMap: ...

        @abstract_method
        def one(self) -> FiniteSetMap: ...

        def identity(self) -> FiniteSetMap:
            r"""Mathematical alias for Sage's endomap monoid identity."""
            return self.one()
