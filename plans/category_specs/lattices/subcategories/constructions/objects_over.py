r"""Slice construction category of lattices over a fixed lattice."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Lattice, LatticeMorphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Lattices ``M`` equipped with a lattice morphism ``M -> L``.

    Canonical chain: ``Lattices(R).ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @final
    def _repr_object_names(self) -> str:
        return f"lattices over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_lattice(self) -> Lattice: ...

        @abstract_method
        def structure_map(self) -> LatticeMorphism: ...

        @final
        def structure_domain(self) -> Lattice:
            return self

        @final
        def structure_codomain(self) -> Lattice:
            return self.structure_lattice()

    class ElementMethods: ...
    class MorphismMethods: ...
