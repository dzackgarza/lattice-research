r"""One-object subcategory for Sage ``NonNegativeIntegers()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import SetElement, SympySet


from .. import Sets


class _NonNegativeIntegersSets(Category_singleton):
    r"""The countably infinite facade set ``{0, 1, 2, ...}`` inside ``ZZ``."""

    def super_categories(self) -> list:
        return [Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        def is_finite(self) -> bool:
            return False

        @abstract_method
        def __contains__(self, elt: Any) -> bool: ...

        @abstract_method
        def _element_constructor_(self, i: SetElement) -> SetElement: ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def an_element(self) -> SetElement: ...

        @abstract_method
        def some_elements(self) -> list[SetElement]: ...

        @abstract_method
        def next(self, o: SetElement) -> SetElement: ...

        @abstract_method
        def unrank(self, rnk: int) -> SetElement: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
