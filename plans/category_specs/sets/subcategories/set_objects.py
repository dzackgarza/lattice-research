r"""One-object subcategories for ``Set(X)`` wrapper objects.

``Set(X)`` wraps an almost arbitrary object as a Sage parent.
Two concrete implementations:
  - ``Set_object`` -- general wrapper, category inferred from X
  - ``Set_object_enumerated`` -- finite frozenset-backed wrapper
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement, Subset, SympySet


def _Sets():
    from .. import Sets as _S
    return _S()


class _SetObjects(Category_singleton):
    r"""Category of ``Set_object`` wrappers (general)."""

    def super_categories(self) -> list:
        return [_Sets()]

    class ParentMethods:
        @abstract_method
        def object(self):
            r"""Return the underlying wrapped object."""
            ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def __richcmp__(self, right: Any, op: int) -> bool:
            r"""Compare the wrapped Sage object using Sage's wrapper comparison semantics."""
            ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @abstract_method
        def union(self, X: Set) -> Set: ...

        @abstract_method
        def intersection(self, X: Subset) -> Subset: ...

        @abstract_method
        def difference(self, X: Subset) -> Subset: ...

        @abstract_method
        def symmetric_difference(self, X: Subset) -> Subset: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def is_empty(self) -> bool: ...

        @abstract_method
        def is_finite(self) -> bool: ...

        @abstract_method
        def subsets(self, size=None) -> Set: ...

        @abstract_method
        def subsets_lattice(self) -> Set:
            r"""Return the lattice of subsets ordered by containment (finite only)."""
            ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...


class _SetObjectsEnumerated(Category_singleton):
    r"""Category for ``Set_object_enumerated`` -- finite frozenset-backed ``Set(X)`` objects."""

    def super_categories(self) -> list:
        return [_SetObjects(), _Sets().Countable().Finite()]

    class ParentMethods:
        def is_finite(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __len__(self) -> int: ...

        @abstract_method
        def __richcmp__(self, other: Any, op: int) -> bool:
            r"""Compare finite wrapper sets using Sage's finite-enumerated semantics."""
            ...

        @abstract_method
        def __iter__(self): ...

        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def set(self) -> set:
            r"""Return the underlying Python ``set``."""
            ...

        @abstract_method
        def frozenset(self) -> frozenset:
            r"""Return an immutable Python ``frozenset``."""
            ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def issubset(self, other: Set) -> bool:
            r"""Return whether ``self`` is a subset of ``other``."""
            ...

        @abstract_method
        def issuperset(self, other: Set) -> bool:
            r"""Return whether ``self`` is a superset of ``other``."""
            ...

        @abstract_method
        def union(self, X: Set) -> Set: ...

        @abstract_method
        def intersection(self, X: Subset) -> Subset: ...

        @abstract_method
        def difference(self, X: Subset) -> Subset: ...

        @abstract_method
        def symmetric_difference(self, X: Subset) -> Subset: ...

        @abstract_method
        def _sympy_(self) -> SympySet: ...
