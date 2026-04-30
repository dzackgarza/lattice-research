r"""Slice construction category of modules under a fixed module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import RModMorphism, RModule


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Modules ``N`` equipped with an ``R``-linear map ``M -> N``."""

    _functor_category = "ObjectsUnder"

    def _repr_object_names(self) -> str:
        return f"modules under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_module(self) -> RModule: ...

        @abstract_method
        def structure_map(self) -> RModMorphism: ...

        def structure_domain(self) -> RModule:
            return self.structure_module()

        def structure_codomain(self) -> RModule:
            return self
