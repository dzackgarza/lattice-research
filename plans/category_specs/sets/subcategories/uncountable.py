r"""Uncountable set subcategory."""

from __future__ import annotations

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Sets


class _UncountableSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Uncountable")

    def _repr_object_names(self) -> str:
        return "uncountable sets"

    def super_categories(self) -> list:
        return [Sets().Infinite()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return False

        def is_uncountable(self) -> bool:
            return True
