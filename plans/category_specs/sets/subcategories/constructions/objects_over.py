r"""Slice construction category of set objects over a fixed set."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import CategoryObject, Morphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Objects ``Y`` equipped with a structure morphism ``Y -> X``.

    Canonical chain: ``Sets().ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @final
    def _repr_object_names(self) -> str:
        return f"objects over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_object(self) -> CategoryObject: ...

        @abstract_method
        def structure_map(self) -> Morphism: ...

        @final
        def structure_domain(self) -> CategoryObject:
            return self

        @final
        def structure_codomain(self) -> CategoryObject:
            return self.structure_object()

    class ElementMethods: ...
    class MorphismMethods: ...
