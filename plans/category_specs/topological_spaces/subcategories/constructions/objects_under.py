r"""Slice construction category of topological spaces under a fixed space."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Morphism, TopologicalSpace


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Spaces ``Y`` equipped with a continuous map ``X -> Y``.

    Canonical chain: ``TopologicalSpaces().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @final
    def _repr_object_names(self) -> str:
        return f"topological spaces under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_space(self) -> TopologicalSpace: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        @final
        def structure_domain(self) -> TopologicalSpace:
            return self.structure_space()

        @final
        def structure_codomain(self) -> TopologicalSpace:
            return self

    class ElementMethods: ...
    class MorphismMethods: ...
