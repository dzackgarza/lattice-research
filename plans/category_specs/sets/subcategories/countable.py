r"""Countable set subcategories (countable, and finite/infinite countable)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as SageFiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as SageInfiniteEnumeratedSets
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement

from .. import Sets


class _CountableSets(CategoryWithAxiom):
    r"""Countable sets — sets admitting an explicit enumeration (injection into N).

    Sage's ``EnumeratedSets`` axiom captures exactly countability: a set is
    countable iff there exists an enumeration f: X -> N, which is an iterator.
    """

    _base_category_class_and_axiom = (Sets, "Countable")

    def _repr_object_names(self) -> str:
        return "countable sets"

    def super_categories(self) -> list:
        return [Sets(), SageEnumeratedSets()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return True

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, e: SetElement) -> SetElement: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...

        @abstract_method
        def rank(self, e: SetElement) -> int: ...

        def is_empty(self) -> bool:
            for _ in self:
                return False
            return True

        def iterator_range(self, start=None, stop=None, step=None):
            r"""Iterate over rank range ``[start, stop)`` with stride ``step``."""
            step = 1 if step is None else step
            start = 0 if start is None else start
            if stop is None:
                i = start
                while True:
                    yield self.unrank(i)
                    i += step
            else:
                for j in range(start, stop, step):
                    yield self.unrank(j)


class _FiniteCountableSets(CategoryWithAxiom):
    r"""Finite countable sets — ``Sets().Countable().Finite()``."""

    _base_category_class_and_axiom = (_CountableSets, "Finite")

    def _repr_object_names(self) -> str:
        return "finite countable sets"

    def super_categories(self) -> list:
        return [SageFiniteEnumeratedSets(), Sets().Countable(), Sets().Finite()]

    class ParentMethods:
        def random_element(self) -> SetElement:
            import random
            return random.choice(self.list())

        def _cardinality_from_iterator(self) -> Cardinality:
            from sage.rings.integer import Integer
            return Integer(sum(1 for _ in self))

        def _list_from_iterator(self) -> list[SetElement]:
            return list(iter(self))


class _InfiniteCountableSets(CategoryWithAxiom):
    r"""Infinite countable sets — ``Sets().Countable().Infinite()``."""

    _base_category_class_and_axiom = (_CountableSets, "Infinite")

    def _repr_object_names(self) -> str:
        return "infinite countable sets"

    def super_categories(self) -> list:
        return [SageInfiniteEnumeratedSets(), Sets().Countable(), Sets().Infinite()]
