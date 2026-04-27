r"""Slice construction category of topological spaces under a fixed space."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import Morphism, TopologicalSpace


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Spaces ``Y`` equipped with a continuous map ``X -> Y``."""

    _functor_category = "ObjectsUnder"

    def _repr_object_names(self) -> str:
        return f"topological spaces under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_space(self) -> TopologicalSpace: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        def structure_domain(self) -> TopologicalSpace:
            return self.structure_space()

        def structure_codomain(self) -> TopologicalSpace:
            return self
