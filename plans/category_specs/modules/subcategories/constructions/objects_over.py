r"""Slice construction category of modules over a fixed module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_types import Category_over_base
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import RModMorphism, RModule


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Modules ``N`` equipped with an ``R``-linear map ``N -> M``."""

    _functor_category = "ObjectsOver"

    def _repr_object_names(self) -> str:
        return f"modules over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_module(self) -> RModule: ...

        @abstract_method
        def structure_map(self) -> RModMorphism: ...

        def structure_domain(self) -> RModule:
            return self

        def structure_codomain(self) -> RModule:
            return self.structure_module()
