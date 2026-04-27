r"""One-object subcategory for Sage ``FiniteEnumeratedSet`` parents."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement


def _Sets():
    from .. import Sets as _S

    return _S()


class _FiniteEnumeratedSetObjects(Category_singleton):
    r"""Tuple-backed finite facade sets from ``sage.sets.finite_enumerated_set``."""

    def super_categories(self) -> list:
        return [_Sets().Countable().Finite().Facade()]

    class ParentMethods:
        @abstract_method
        def __bool__(self) -> bool: ...

        @abstract_method
        def __contains__(self, x: SetElement) -> bool: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def last(self) -> SetElement: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def rank(self, x: SetElement) -> int: ...

        @abstract_method
        def unrank(self, i: int) -> SetElement: ...

        @abstract_method
        def __call__(self, el: SetElement) -> SetElement: ...

        @abstract_method
        def _element_constructor_(self, el: SetElement) -> SetElement: ...
