r"""One-object subcategory for Sage indexed families."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, Set, SetElement, SetFamily, SetMorphism


from .. import Sets


class _FamilySets(Category_singleton):
    r"""Indexed families ``(f_i)_{i in I}``, finite, lazy, trivial, or enumerated."""

    @final
    def super_categories(self) -> list:
        return [Sets().Countable()]

    class ParentMethods:
        @abstract_method
        def hidden_keys(self) -> Set: ...

        @abstract_method
        def keys(self) -> Set: ...

        @abstract_method
        def values(self) -> Set: ...

        @abstract_method
        def items(self) -> Set: ...

        @abstract_method
        def zip(self, f: SetMorphism, other: SetFamily, name: str | None = None) -> SetFamily: ...

        @abstract_method
        def map(self, f: SetMorphism, name: str | None = None) -> SetFamily: ...

        @abstract_method
        def inverse_family(self) -> SetFamily: ...

        @abstract_method
        def has_key(self, k: SetElement) -> bool: ...

        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def __len__(self) -> Integer: ...

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def __getitem__(self, i: SetElement) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
