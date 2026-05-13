r"""Overlattice construction category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import Category_module

if TYPE_CHECKING:
    from ....cat import Category
    from ....types import Cardinality, Lattice, LatticeMorphism


class OverlatticesCategory(Category_module):
    r"""Overlattices of a lattice inside its rational span.

    Canonical chain: ``Lattices(R).Overlattices(L)``.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"overlattices over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        from ... import Lattices

        return [Lattices(self.base_ring()).Rational()]

    class ParentMethods:
        @abstractmethod
        def base_lattice(self) -> Lattice: ...

        @abstractmethod
        def base_inclusion(self) -> LatticeMorphism: ...

        @abstractmethod
        def index(self) -> Cardinality: ...

    class ElementMethods: ...

    class MorphismMethods: ...


OverlatticesObject = OverlatticesCategory.ParentMethods
OverlatticesElement = OverlatticesCategory.ElementMethods
OverlatticesMorphism = OverlatticesCategory.MorphismMethods
