r"""One-object subcategory for ``ConditionSet`` -- subset defined by predicates."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Set, SetElement, SympySet


def _Sets():
    from .. import Sets as _S
    return _S()


class _ConditionSets(Category_singleton):
    r"""Category for ``ConditionSet`` -- elements of a universe satisfying predicates.

    ``ConditionSet(ZZ, is_even)`` returns the set of even integers.
    Inherits ``Set_base``, ``Set_boolean_operators``, ``Set_add_sub_operators``.
    """

    def super_categories(self) -> list:
        return [_Sets().WithBooleanOps()]

    class ParentMethods:
        @abstract_method
        def universe(self) -> Set:
            r"""Return the ambient set from which elements are drawn."""
            ...

        @abstract_method
        def predicates(self) -> tuple:
            r"""Return the tuple of predicates that elements must satisfy."""
            ...

        @abstract_method
        def __contains__(self, x: SetElement) -> bool:
            r"""Return ``True`` iff ``x`` is in the universe and all predicates hold."""
            ...

        @abstract_method
        def union(self, X: Set) -> Set: ...

        @abstract_method
        def intersection(self, X: Set) -> Set: ...

        @abstract_method
        def difference(self, X: Set) -> Set: ...

        @abstract_method
        def symmetric_difference(self, X: Set) -> Set: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
