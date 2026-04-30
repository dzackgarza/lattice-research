r"""One-object subcategory for ``ConditionSet`` -- subset defined by predicates."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Set, SetElement, Subset, SympySet


from .. import Sets


class _ConditionSets(Category_singleton):
    r"""Category for ``ConditionSet`` -- elements of a universe satisfying predicates.

    ``ConditionSet(ZZ, is_even)`` returns the set of even integers.
    It is a predicate-defined subobject of its ambient set.
    """

    def super_categories(self) -> list:
        return [Sets().Subobjects()]

    class ParentMethods:
        @abstract_method
        def ambient(self) -> Set:
            r"""Return the ambient set from which elements are drawn."""
            ...

        def universe(self) -> Set:
            r"""Alias for Sage's ``ambient()`` vocabulary."""
            return self.ambient()

        @abstract_method
        def arguments(self) -> tuple:
            r"""Return the tuple of defining predicates and symbolic arguments."""
            ...

        def predicates(self) -> tuple:
            r"""Alias for the predicate data exposed through ``arguments()``."""
            return self.arguments()

        @abstract_method
        def __contains__(self, x: Any) -> bool:
            r"""Return ``True`` iff ``x`` is in the universe and all predicates hold."""
            ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @abstract_method
        def union(self, X: Subset) -> Subset: ...

        @abstract_method
        def intersection(self, X: Subset) -> Subset: ...

        @abstract_method
        def difference(self, X: Subset) -> Subset: ...

        @abstract_method
        def symmetric_difference(self, X: Subset) -> Subset: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
