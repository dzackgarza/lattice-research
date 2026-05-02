r"""Slice construction category of topological spaces over a fixed space."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Morphism, TopologicalSpace


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Spaces ``Y`` equipped with a continuous map ``Y -> X``.

    Canonical chain: ``TopologicalSpaces().ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"topological spaces over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_space(self) -> TopologicalSpace:
            r"""Return the base topological space of this object-over structure."""
            ...

        @abstract_method
        def structure_map(self) -> Morphism:
            r"""Return the structure map to the base topological space."""
            ...

        @final
        def structure_domain(self) -> TopologicalSpace:
            r"""Return the domain of the structure map."""
            return self

        @final
        def structure_codomain(self) -> TopologicalSpace:
            r"""Return the codomain of the structure map."""
            return self.structure_space()

    class ElementMethods: ...
    class MorphismMethods: ...
