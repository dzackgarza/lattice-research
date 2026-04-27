r"""Slice construction category of algebras under a fixed algebra."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraMorphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Algebras ``B`` equipped with an algebra morphism ``A -> B``."""

    _functor_category = "ObjectsUnder"

    def _repr_object_names(self) -> str:
        return f"algebras under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_algebra(self) -> Algebra: ...

        @abstract_method
        def structure_map(self) -> AlgebraMorphism: ...

        def structure_domain(self) -> Algebra:
            return self.structure_algebra()

        def structure_codomain(self) -> Algebra:
            return self
