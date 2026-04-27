r"""Slice construction category for categories over a fixed category."""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.categories.functor import Functor
from sage.misc.abstract_method import abstract_method


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Categories ``D`` equipped with a functor ``D -> C``."""

    _functor_category = "ObjectsOver"

    def _repr_object_names(self) -> str:
        return f"categories over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_category(self) -> Category: ...

        @abstract_method
        def structure_functor(self) -> Functor: ...

        def structure_domain(self) -> Category:
            return self

        def structure_codomain(self) -> Category:
            return self.structure_category()


SliceCategories = _ObjectsOver
