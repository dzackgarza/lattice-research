r"""Compact topological spaces."""

from __future__ import annotations

from typing import final

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import _TopologicalSpaces


class _CompactTopologicalSpaces(CategoryWithAxiom):
    r"""Category of compact topological spaces.

    Canonical chain: ``TopologicalSpaces().Compact()``.
    """

    _base_category_class_and_axiom = (_TopologicalSpaces, "Compact")

    @final
    def _repr_object_names(self) -> str:
        return "compact topological spaces"

    @final
    def super_categories(self) -> list[Category]:
        return [SageSets().Topological().Compact(), _TopologicalSpaces()]

    class ParentMethods:
        @final
        def is_compact(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
