r"""Slice construction category of set objects under a fixed set."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import CategoryObject, Morphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Objects ``Y`` equipped with a structure morphism ``X -> Y``."""

    _functor_category = "ObjectsUnder"

    def _repr_object_names(self) -> str:
        return f"objects under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_object(self) -> CategoryObject: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        def structure_domain(self) -> CategoryObject:
            return self.structure_object()

        def structure_codomain(self) -> CategoryObject:
            return self
