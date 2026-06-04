r"""Discriminant-group construction category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import Category_module
from ....forms.subcategories.quadratic import QuadraticModulesMorphism
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
    from ....cat import Category
    from ....types import (
        BilinearForm,
        FormedModuleMorphism,
        Lattice,
        LatticeMorphism,
        Matrix,
        QuadraticForm,
        RingElement,
        RModuleElement,
        SetFamily,
    )


class LatticeDiscriminantGroupsCategory(Category_module):
    r"""Finite torsion modules with the discriminant form of a lattice.

    Canonical chain: ``Lattices(R).DiscriminantGroups()``.

    Invariant factors are inherited from the finitely presented PID-module
    surface.  They are not discriminant-group-specific data.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"discriminant groups over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Modules(R)
            .FinitelyPresented()
            .OverPID()
            .Torsion()
            .WithForms()
            .Bilinear()
            .Quadratic(),
        ]

    class ParentMethods:
        @abstractmethod
        def source_lattice(self) -> Lattice:
            r"""Return the lattice ``L`` whose dual inclusion defines this object."""
            ...

        @abstractmethod
        def metric_dual(self) -> Lattice:
            r"""Return the metric dual ``L^\#`` in the cokernel diagram."""
            ...

        @abstractmethod
        def inclusion_morphism(self) -> LatticeMorphism:
            r"""Return the metric inclusion ``L -> L^\#``."""
            ...

        @abstractmethod
        def projection(self) -> FormedModuleMorphism:
            r"""Return the quotient projection ``L^\# -> L^\#/L``."""
            ...

        @abstractmethod
        def bilinear_form(self) -> BilinearForm:
            r"""Return the descended bilinear form with codomain ``K/R``."""
            ...

        @abstractmethod
        def quadratic_form(self) -> QuadraticForm:
            r"""Return the descended quadratic form with codomain ``K/2R``."""
            ...

        @abstractmethod
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstractmethod
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstractmethod
        def brown_invariant(self) -> RingElement: ...

        @abstractmethod
        def is_trivial(self) -> bool: ...

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



LatticeDiscriminantGroupsObject = LatticeDiscriminantGroupsCategory.ParentMethods
LatticeDiscriminantGroupsElement = LatticeDiscriminantGroupsCategory.ElementMethods
LatticeDiscriminantGroupsMorphism = QuadraticModulesMorphism
LatticeDiscriminantGroupsHomCategory = ModulesHomCategory
LatticeDiscriminantGroupsEndCategory = ModulesEndCategory
LatticeDiscriminantGroupsAutCategory = ModulesAutCategory
LatticeDiscriminantGroupsHom = ModulesHom
LatticeDiscriminantGroupsEnd = ModulesEnd
LatticeDiscriminantGroupsAut = ModulesAut
LatticeDiscriminantGroupsEndomorphism = ModulesEndomorphism
LatticeDiscriminantGroupsAutomorphism = ModulesAutomorphism
