r"""Discriminant-group construction category."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_module
from ....modules import Modules

if TYPE_CHECKING:
    from ....types import Matrix, RModuleElement, RingElement, SetFamily


class _DiscriminantGroups(Category_module):
    r"""Finite torsion modules with the discriminant form of a lattice."""

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
        @abstract_method
        def invariants(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstract_method
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstract_method
        def brown_invariant(self) -> RingElement: ...

        @abstract_method
        def primary_part(self, p: RingElement) -> "_DiscriminantGroups.ParentMethods": ...

        @abstract_method
        def orthogonal_group(self): ...

        @abstract_method
        def all_submodules(self) -> SetFamily: ...

    class ElementMethods:
        @abstract_method
        def additive_order(self) -> RingElement: ...

        @abstract_method
        def lift(self) -> RModuleElement: ...

    class MorphismMethods: ...


LatticeDiscriminantGroupsCategory = _DiscriminantGroups
LatticeDiscriminantGroupsObject = _DiscriminantGroups.ParentMethods
LatticeDiscriminantGroupsElement = _DiscriminantGroups.ElementMethods
LatticeDiscriminantGroupsMorphism = _DiscriminantGroups.MorphismMethods
