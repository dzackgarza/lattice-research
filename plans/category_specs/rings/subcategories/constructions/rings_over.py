r"""Rings over a fixed ambient ring."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Ring, RingMorphism


class _RingsOver(RegressiveCovariantConstructionCategory, Category_over_base_ring):
    _functor_category = "RingsOver"

    @classmethod
    def default_super_categories(cls, category, ambient):
        from ... import Rings

        return Category.join(
            [
                Rings(),
                super().default_super_categories(category, ambient),
            ]
        )

    def _repr_object_names(self):
        return f"rings over {self.base_ring()}"

    class ParentMethods:
        def structure_ring(self) -> Ring:
            return self.base_ring()

        def structure_map(self) -> RingMorphism:
            return self.structure_ring().coerce_map_from(self)

        def structure_domain(self) -> Ring:
            return self

        def structure_codomain(self) -> Ring:
            return self.structure_ring()
