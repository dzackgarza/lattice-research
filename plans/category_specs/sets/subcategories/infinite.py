r"""Infinite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality

from .. import Sets


class _InfiniteSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Infinite")

    def _repr_object_names(self) -> str:
        return "infinite sets"

    def super_categories(self) -> list:
        return [SageSets().Infinite(), Sets()]

    def __contains__(self, S: Any) -> bool:
        return S in SageSets().Infinite() or (S in self.base_category() and not S.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return False

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @abstract_method
        def is_empty(self) -> bool: ...
