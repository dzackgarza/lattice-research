r"""Coslice construction category of posets under a fixed poset."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Poset, PosetMorphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Posets ``Q`` equipped with an order-preserving map ``P -> Q``.

    Canonical chain: ``Posets().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"posets under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_poset(self) -> Poset:
            r"""Return the source poset of this object-under structure."""
            ...

        @abstract_method
        def structure_map(self) -> PosetMorphism:
            r"""Return the order-preserving map from the source to this poset."""
            ...

        @final
        def structure_domain(self) -> Poset:
            r"""Return the domain poset of the structure map."""
            return self.structure_poset()

        @final
        def structure_codomain(self) -> Poset:
            r"""Return the codomain poset of the structure map."""
            return self

    class ElementMethods: ...
    class MorphismMethods: ...
