r"""Slice construction category of set objects under a fixed set."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import CategoryObject, Morphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Objects ``Y`` equipped with a structure morphism ``X -> Y``.

    Canonical chain: ``Sets().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @final
    def _repr_object_names(self) -> str:
        return f"objects under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_object(self) -> CategoryObject: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        @final
        def structure_domain(self) -> CategoryObject:
            return self.structure_object()

        @final
        def structure_codomain(self) -> CategoryObject:
            return self

    class ElementMethods: ...
    class MorphismMethods: ...
