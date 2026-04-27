r"""Coslice construction category for categories under a fixed category."""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.categories.functor import Functor
from sage.misc.abstract_method import abstract_method


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Categories ``D`` equipped with a functor ``C -> D``."""

    _functor_category = "ObjectsUnder"

    def _repr_object_names(self) -> str:
        return f"categories under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_category(self) -> Category: ...

        @abstract_method
        def structure_functor(self) -> Functor: ...

        def structure_domain(self) -> Category:
            return self.structure_category()

        def structure_codomain(self) -> Category:
            return self


CosliceCategories = _ObjectsUnder
