r"""Slice construction category of posets over a fixed poset."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Poset, PosetMorphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Posets ``Q`` equipped with an order-preserving map ``Q -> P``."""

    _functor_category = "ObjectsOver"

    @final
    def _repr_object_names(self) -> str:
        return f"posets over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_poset(self) -> Poset: ...

        @abstract_method
        def structure_map(self) -> PosetMorphism: ...

        @final
        def structure_domain(self) -> Poset:
            return self

        @final
        def structure_codomain(self) -> Poset:
            return self.structure_poset()
