r"""Infinite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.sets_cat import Sets as SageSets

if TYPE_CHECKING:
    from ...types import Cardinality

from .. import Sets


class _InfiniteSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Infinite")

    def _repr_object_names(self) -> str:
        return "infinite sets"

    def super_categories(self) -> list:
        return [SageSets().Infinite(), Sets()]

    def __contains__(self, S) -> bool:
        return S in SageSets().Infinite() or (S in self.base_category() and not S.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return False

        def cardinality(self) -> Cardinality:
            from sage.rings.infinity import infinity
            return infinity
