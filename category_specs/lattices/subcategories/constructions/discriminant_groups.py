r"""Discriminant-group construction category."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from abc import abstractmethod

from ....cat import Category_module
from ....modules import (
    Modules,
    ModulesAut,
    ModulesAutCategory,
    ModulesAutomorphism,
    ModulesEnd,
    ModulesEndCategory,
    ModulesEndomorphism,
    ModulesHom,
    ModulesHomCategory,
)

if TYPE_CHECKING:
    from ....types import Matrix, RingElement, RModuleElement, SetFamily


class LatticeDiscriminantGroupsCategory(Category_module):
    r"""Finite torsion modules with the discriminant form of a lattice.

    Canonical chain: ``Lattices(R).DiscriminantGroups()``.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"discriminant groups over {self.base_ring()}"

    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).Torsion(),
            Modules(R).WithForms().Bilinear(),
            Modules(R).WithForms().Quadratic(),
            Modules(R).FinitelyPresented(),
        ]

    class ParentMethods:
        @abstractmethod
        def invariants(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstractmethod
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstractmethod
        def brown_invariant(self) -> RingElement: ...

        @abstractmethod
        def primary_part(
            self, p: RingElement
        ) -> LatticeDiscriminantGroupsCategory.ParentMethods: ...

        @abstractmethod
        def all_submodules(self) -> SetFamily: ...

    class ElementMethods:
        @abstractmethod
        def additive_order(self) -> RingElement: ...

        @abstractmethod
        def lift(self) -> RModuleElement: ...

    class MorphismMethods: ...


LatticeDiscriminantGroupsObject = LatticeDiscriminantGroupsCategory.ParentMethods
LatticeDiscriminantGroupsElement = LatticeDiscriminantGroupsCategory.ElementMethods
LatticeDiscriminantGroupsMorphism = LatticeDiscriminantGroupsCategory.MorphismMethods
LatticeDiscriminantGroupsHomCategory = ModulesHomCategory
LatticeDiscriminantGroupsEndCategory = ModulesEndCategory
LatticeDiscriminantGroupsAutCategory = ModulesAutCategory
LatticeDiscriminantGroupsHom = ModulesHom
LatticeDiscriminantGroupsEnd = ModulesEnd
LatticeDiscriminantGroupsAut = ModulesAut
LatticeDiscriminantGroupsEndomorphism = ModulesEndomorphism
LatticeDiscriminantGroupsAutomorphism = ModulesAutomorphism
