r"""Rings under a fixed structure ring."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.covariant_functorial_construction import CovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Ring, RingMorphism


class _RingsUnder(CovariantConstructionCategory, Category_over_base_ring):
    _functor_category = "RingsUnder"

    @classmethod
    def default_super_categories(cls, category, base):
        from ... import Rings

        return Category.join(
            [
                category,
                Rings(),
                super().default_super_categories(category, base),
            ]
        )

    def _repr_object_names(self):
        return f"rings under {self.base_ring()}"

    class ParentMethods:
        def structure_ring(self) -> Ring:
            return self.base_ring()

        def structure_map(self) -> RingMorphism:
            return self.coerce_map_from(self.structure_ring())

        def structure_domain(self) -> Ring:
            return self.structure_ring()

        def structure_codomain(self) -> Ring:
            return self
