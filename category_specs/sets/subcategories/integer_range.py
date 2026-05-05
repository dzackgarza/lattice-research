r"""One-object subcategory for Sage ``IntegerRange`` parents."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement


from ...cat import Category
from .. import Sets


class _IntegerRangeSets(Category_singleton):
    r"""Arithmetic progressions of integers, finite or infinite by bounds.

    Constructor target:
    ``Sets().Constructors().IntegerRange(...)`` refines Sage integer ranges
    here as countable facade sets.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Facade()]

    class ParentMethods:
        @override
        @final
        def _element_constructor_(self, el: SetElement) -> SetElement:
            if el in self:
                from sage.rings.integer import Integer

                if not isinstance(el, Integer):
                    return Integer(el)
                return el
            raise ValueError(f"{el} not in {self}")

        @override
        @final
        def __contains__(self, elt: Any) -> bool:
            from sage.rings.integer import Integer

            try:
                elt = Integer(elt)
            except (TypeError, ValueError):
                return False

            if hasattr(self, "_middle_point"):
                anchor = self._middle_point
                lower = self._begin
                upper = self._end
                return abs(self._step).divides(elt - anchor) and (
                    lower <= elt < upper or lower >= elt > upper
                )

            if hasattr(self, "_end"):
                return abs(self._step).divides(elt - self._begin) and (
                    self._begin <= elt < self._end and self._step > 0
                    or self._begin >= elt > self._end and self._step < 0
                )

            return abs(self._step).divides(elt - self._begin) and (
                self._step > 0 and elt >= self._begin
                or self._step < 0 and elt <= self._begin
            )

        @override
        @final
        def cardinality(self) -> Cardinality:
            if self.is_finite():
                from sage.categories.finite_enumerated_sets import (
                    FiniteEnumeratedSets as SageFiniteEnumeratedSets,
                )

                return SageFiniteEnumeratedSets.ParentMethods.cardinality(self)

            from sage.rings.infinity import infinity

            return infinity

        @override
        @final
        def rank(self, x: SetElement) -> Integer:
            return SageEnumeratedSets.ParentMethods.rank(self, x)

        @override
        @final
        def __getitem__(self, i: Integer) -> SetElement:
            return SageEnumeratedSets.ParentMethods.__getitem__(self, i)

        @override
        @final
        def __iter__(self) -> Iterator[SetElement]:
            return SageEnumeratedSets.ParentMethods.__iter__(self)

        @override
        @final
        def _an_element_(self) -> SetElement:
            return SageEnumeratedSets.ParentMethods._an_element_(self)

    class ElementMethods: ...

    class MorphismMethods: ...
