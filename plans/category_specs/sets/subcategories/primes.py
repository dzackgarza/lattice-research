r"""One-object subcategory for Sage ``Primes()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import SetElement


from ...cat import Category
from .. import Sets


class _PrimesSets(Category_singleton):
    r"""One-object category whose object is the full Sage set of prime integers.

    Prime subsets, including primes in arithmetic progressions, are subobjects of this
    object and are expressed through ``PrimeSubset`` and
    ``PrimesInArithmeticProgressions`` type vocabulary.
    """

    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Countable().Infinite().Facade()]

    class ParentMethods:
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
