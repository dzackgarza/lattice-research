r"""Facade set subcategory."""

from __future__ import annotations

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method

from .. import Sets


class _FacadeSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Facade")

    def _repr_object_names(self) -> str:
        return "facade sets"

    def super_categories(self) -> list:
        return [SageSets().Facade(), Sets()]

    class ParentMethods:
        def is_facade(self) -> bool:
            return True

        @abstract_method
        def _element_constructor_(self, element):
            r"""Coerce ``element`` from any facade parent."""
            ...

        @abstract_method
        def facade_for(self) -> tuple:
            r"""Return the tuple of parents this set is a facade for."""
            ...
