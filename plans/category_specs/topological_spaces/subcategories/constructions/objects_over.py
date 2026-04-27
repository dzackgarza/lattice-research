r"""Slice construction category of topological spaces over a fixed space."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import Morphism, TopologicalSpace


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Spaces ``Y`` equipped with a continuous map ``Y -> X``."""

    _functor_category = "ObjectsOver"

    def _repr_object_names(self) -> str:
        return f"topological spaces over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_space(self) -> TopologicalSpace: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        def structure_domain(self) -> TopologicalSpace:
            return self

        def structure_codomain(self) -> TopologicalSpace:
            return self.structure_space()
