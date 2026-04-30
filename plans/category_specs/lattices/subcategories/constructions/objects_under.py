r"""Slice construction category of lattices under a fixed lattice."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Lattice, LatticeMorphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Lattices ``M`` equipped with a lattice morphism ``L -> M``."""

    _functor_category = "ObjectsUnder"

    @final
    def _repr_object_names(self) -> str:
        return f"lattices under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_lattice(self) -> Lattice: ...

        @abstract_method
        def structure_map(self) -> LatticeMorphism: ...

        @final
        def structure_domain(self) -> Lattice:
            return self.structure_lattice()

        @final
        def structure_codomain(self) -> Lattice:
            return self

    class ElementMethods: ...
    class MorphismMethods: ...
