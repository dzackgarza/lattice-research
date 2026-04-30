r"""Subobject construction category for sets.

For sets, subobjects are subsets. The class still extends Sage's construction
category so it can attach to arbitrary subcategories via ``category_of``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Set, Subset


class _Subobjects(SubobjectsCategory):
    r"""Subobjects of sets, equivalently subsets with an ambient set."""

    class ParentMethods:
        @abstract_method
        def ambient_set(self) -> Set:
            r"""Return the ambient set of which ``self`` is a subset."""
            ...

        @abstract_method
        def union(self, X: Subset) -> Subset:
            r"""Return the set-theoretic union of ``self`` and ``X``."""
            ...

        @abstract_method
        def intersection(self, X: Subset) -> Subset:
            r"""Return the set-theoretic intersection of ``self`` and ``X``."""
            ...

        @abstract_method
        def difference(self, X: Subset) -> Subset:
            r"""Return the set-theoretic difference ``self \ X``."""
            ...

        @abstract_method
        def symmetric_difference(self, X: Subset) -> Subset:
            r"""Return the symmetric difference of ``self`` and ``X``."""
            ...

        @abstract_method
        def complement(self) -> Subset:
            r"""Return the complement of ``self`` in its ambient set."""
            ...

        def __or__(self, X: Subset) -> Subset:
            return self.union(X)

        def __and__(self, X: Subset) -> Subset:
            return self.intersection(X)

        def __xor__(self, X: Subset) -> Subset:
            return self.symmetric_difference(X)

        def __sub__(self, X: Subset) -> Subset:
            return self.difference(X)


Subsets = _Subobjects
