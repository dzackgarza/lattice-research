r"""Slice construction category of topological spaces over a fixed space."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Morphism, TopologicalSpace


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Spaces ``Y`` equipped with a continuous map ``Y -> X``."""

    _functor_category = "ObjectsOver"

    @final
    def _repr_object_names(self) -> str:
        return f"topological spaces over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_space(self) -> TopologicalSpace: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        @final
        def structure_domain(self) -> TopologicalSpace:
            return self

        @final
        def structure_codomain(self) -> TopologicalSpace:
            return self.structure_space()
