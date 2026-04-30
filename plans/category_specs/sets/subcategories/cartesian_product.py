r"""One-object subcategory for Sage Cartesian products of sets."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import CartesianProductFunctor, Integer, Set, SetElement, SetMorphism, SympySet

from .. import Sets


class _CartesianProductSets(Category_singleton):
    r"""Cartesian products of sets and their tuple-like elements."""

    @final
    def super_categories(self) -> list:
        return [Sets().CartesianProducts()]

    class ParentMethods:
        @abstract_method
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def cartesian_factors(self) -> Sequence[Set]: ...

        @abstract_method
        def _sets_keys(self) -> Sequence[Set]: ...

        @abstract_method
        def cartesian_projection(self, i: Integer) -> Set: ...

        @abstract_method
        def _cartesian_product_of_elements(self, elements: Sequence[SetElement]) -> SetElement: ...

        @abstract_method
        def construction(self) -> tuple[CartesianProductFunctor, Sequence[Set]]: ...

        @abstract_method
        def _coerce_map_from_(self, S: Set) -> bool | SetMorphism | None: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...

    class ElementMethods:
        @abstract_method
        def cartesian_projection(self, i: Integer) -> SetElement: ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def __len__(self) -> Integer: ...

        @abstract_method
        def cartesian_factors(self) -> Sequence[SetElement]: ...
