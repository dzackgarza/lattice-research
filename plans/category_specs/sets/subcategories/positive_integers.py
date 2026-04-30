r"""One-object subcategory for Sage ``PositiveIntegers()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import SetElement, SympySet

from .. import Sets
from .integer_range import _IntegerRangeSets
from ...cat import Category


class _PositiveIntegersSets(Category_singleton):
    r"""The countably infinite facade set ``{1, 2, 3, ...}`` inside ``ZZ``."""

    @final
    def super_categories(self) -> list[Category]:
        return [_IntegerRangeSets(), Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...
    class MorphismMethods: ...
