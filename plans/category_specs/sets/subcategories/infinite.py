r"""Infinite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality

from .. import Sets


class _InfiniteSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Infinite")

    @final
    def _repr_object_names(self) -> str:
        return "infinite sets"

    @final
    def super_categories(self) -> list:
        return [SageSets().Infinite(), Sets()]

    @final
    def __contains__(self, S: Any) -> bool:
        return S in SageSets().Infinite() or (S in self.base_category() and not S.is_finite())

    class ParentMethods:
        @final
        def is_finite(self) -> bool:
            return False

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def is_empty(self) -> bool: ...
