r"""One-object subcategory for Sage ``Primes()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import SetElement


def _Sets():
    from .. import Sets as _S

    return _S()


class _PrimesSets(Category_singleton):
    r"""One-object category whose object is the full Sage set of prime integers.

    Prime subsets, including primes in arithmetic progressions, are subobjects of this
    object and are expressed through ``PrimeSubset`` and
    ``PrimesInArithmeticProgressions`` type vocabulary.
    """

    def super_categories(self) -> list:
        return [_Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @abstract_method
        def first(self) -> SetElement: ...

        @abstract_method
        def next(self, pr: SetElement) -> SetElement: ...

        @abstract_method
        def unrank(self, n: int) -> SetElement: ...
