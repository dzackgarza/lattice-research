r"""Connected topological spaces."""

from __future__ import annotations

from typing import final

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import _TopologicalSpaces


class _ConnectedTopologicalSpaces(CategoryWithAxiom):
    r"""Category of connected topological spaces.

    Canonical chain: ``TopologicalSpaces().Connected()``.
    """

    _base_category_class_and_axiom = (_TopologicalSpaces, "Connected")

    @final
    def _repr_object_names(self) -> str:
        return "connected topological spaces"

    @final
    def super_categories(self) -> list[Category]:
        return [SageSets().Topological().Connected(), _TopologicalSpaces()]

    class ParentMethods:
        @final
        def is_connected(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
