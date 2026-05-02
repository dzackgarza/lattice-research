r"""Uncountable set subcategory."""

from __future__ import annotations

from typing import final

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Sets


class _UncountableSets(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().Uncountable()``."""
    _base_category_class_and_axiom = (Sets, "Uncountable")

    @final
    def _repr_object_names(self) -> str:
        return "uncountable sets"

    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Infinite()]

    class ParentMethods:
        @final
        def is_countable(self) -> bool:
            return False

        @final
        def is_uncountable(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
