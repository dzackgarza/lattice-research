r"""Rings under a fixed structure ring."""

from __future__ import annotations

from typing import final
from typing import TYPE_CHECKING

from ....cat import Category

from ....cat import Category_over_base_ring, CovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Ring, RingMorphism


class _RingsUnder(CovariantConstructionCategory, Category_over_base_ring):
    _functor_category = "RingsUnder"

    @classmethod
    @final
    def default_super_categories(cls, category: Category, base: Ring):
        from ... import Rings

        return Category.join(
            [
                category,
                Rings(),
                super().default_super_categories(category, base),
            ]
        )

    @final
    def _repr_object_names(self) -> str:
        return f"rings under {self.base_ring()}"

    class ParentMethods:
        @final
        def structure_ring(self) -> Ring:
            return self.base_ring()

        @final
        def structure_map(self) -> RingMorphism:
            return self.coerce_map_from(self.structure_ring())

        @final
        def structure_domain(self) -> Ring:
            return self.structure_ring()

        @final
        def structure_codomain(self) -> Ring:
            return self

    class ElementMethods: ...
    class MorphismMethods: ...
