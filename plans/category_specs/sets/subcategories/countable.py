r"""Countable set subcategories (countable, and finite/infinite countable)."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, final

from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as SageFiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as SageInfiniteEnumeratedSets
from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, Set, SetElement, SetMorphism

from .. import Sets


class _CountableSets(CategoryWithAxiom):
    r"""Countable sets — sets admitting an explicit enumeration (injection into N).

    Sage's ``EnumeratedSets`` axiom captures exactly countability: a set is
    countable iff there exists an enumeration f: X -> N, which is an iterator.
    """

    _base_category_class_and_axiom = (Sets, "Countable")

    @final
    def _repr_object_names(self) -> str:
        return "countable sets"

    @final
    def super_categories(self) -> list:
        return [Sets(), SageEnumeratedSets()]

    class ParentMethods:
        @final
        def is_countable(self) -> bool:
            return True

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def __getitem__(self, i: Integer) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, e: SetElement) -> SetElement: ...

        @abstract_method
        def unrank(self, n: Integer) -> SetElement: ...

        @abstract_method
        def rank(self, e: SetElement) -> Integer: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __len__(self) -> Integer: ...

        @abstract_method
        def tuple(self) -> tuple[SetElement, ...]: ...

        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def iterator_range(
            self,
            start: Integer | None = None,
            stop: Integer | None = None,
            step: Integer | None = None,
        ) -> Iterator[SetElement]:
            r"""Iterate over rank range ``[start, stop)`` with stride ``step``."""
            ...

        @abstract_method
        def unrank_range(
            self,
            start: Integer | None = None,
            stop: Integer | None = None,
            step: Integer | None = None,
        ) -> list[SetElement]: ...

        @abstract_method
        def _tuple_from_iterator(self) -> tuple[SetElement, ...]: ...

        @abstract_method
        def _tuple_from_list(self) -> tuple[SetElement, ...]: ...

        @abstract_method
        def _list_from_iterator(self) -> list[SetElement]: ...

        @abstract_method
        def _first_from_iterator(self) -> SetElement: ...

        @abstract_method
        def _next_from_iterator(self, obj: SetElement) -> SetElement: ...

        @abstract_method
        def _unrank_from_iterator(self, r: Integer) -> SetElement: ...

        @abstract_method
        def _rank_from_iterator(self, x: SetElement) -> Integer: ...

        @abstract_method
        def _iterator_from_list(self) -> Iterator[SetElement]: ...

        @abstract_method
        def _iterator_from_next(self) -> Iterator[SetElement]: ...

        @abstract_method
        def _iterator_from_unrank(self) -> Iterator[SetElement]: ...

        @abstract_method
        def _an_element_from_iterator(self) -> SetElement: ...

        @abstract_method
        def _some_elements_from_iterator(self) -> list[SetElement]: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def map(self, f: SetMorphism, name: str | None = None, *, is_injective: bool = True) -> Set:
            r"""Return the image of this enumerated set under ``f``."""
            ...


class _FiniteCountableSets(CategoryWithAxiom):
    r"""Finite countable sets — ``Sets().Countable().Finite()``."""

    _base_category_class_and_axiom = (_CountableSets, "Finite")

    @final
    def _repr_object_names(self) -> str:
        return "finite countable sets"

    @final
    def super_categories(self) -> list:
        return [SageFiniteEnumeratedSets(), Sets().Countable(), Sets().Finite()]

    class ParentMethods:
        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def _cardinality_from_iterator(self) -> Cardinality: ...

        @abstract_method
        def _cardinality_from_list(self) -> Cardinality: ...

        @abstract_method
        def _list_from_iterator(self) -> list[SetElement]: ...

        @abstract_method
        def _unrank_from_list(self, r: Integer) -> SetElement: ...

        @abstract_method
        def _random_element_from_unrank(self) -> SetElement: ...

        @abstract_method
        def _last_from_iterator(self) -> SetElement: ...

        @abstract_method
        def _last_from_unrank(self) -> SetElement: ...

        @abstract_method
        def last(self) -> SetElement: ...


class _InfiniteCountableSets(CategoryWithAxiom):
    r"""Infinite countable sets — ``Sets().Countable().Infinite()``."""

    _base_category_class_and_axiom = (_CountableSets, "Infinite")

    @final
    def _repr_object_names(self) -> str:
        return "infinite countable sets"

    @final
    def super_categories(self) -> list:
        return [SageInfiniteEnumeratedSets(), Sets().Countable(), Sets().Infinite()]

    class ParentMethods:
        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def tuple(self) -> tuple[SetElement, ...]: ...

        @abstract_method
        def list(self) -> list[SetElement]: ...
