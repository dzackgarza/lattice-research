r"""Finite torsion modules with quadratic forms."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from sage.categories.category import Category

from ...cat import Category_over_base_ring
from ...modules import Modules

if TYPE_CHECKING:
    from ...types import Matrix, RingElement


class TorsionQuadraticModulesCategory(Category_over_base_ring):
    r"""Finite ``ZZ``-modules equipped with a torsion quadratic form.

    Canonical chain:
    ``FinitelyPresentedModulesOverPID(ZZ).Torsion().WithForms().Quadratic()``.
    """

    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Category.join(
                [
                    Modules(R).Torsion(),
                    Modules(R).WithForms().Quadratic(),
                    Modules(R).FinitelyPresented(),
                ]
            )
        ]

    class ParentMethods:
        @final
        def is_torsion_quadratic_module(self) -> bool:
            return True

        @abstractmethod
        def gram_matrix_quadratic(self) -> Matrix: ...

        @abstractmethod
        def gram_matrix_bilinear(self) -> Matrix: ...

        @abstractmethod
        def invariants(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def brown_invariant(self) -> RingElement: ...

    class ElementMethods: ...

    class MorphismMethods: ...


TorsionQuadraticModulesObject = TorsionQuadraticModulesCategory.ParentMethods
TorsionQuadraticModulesElement = TorsionQuadraticModulesCategory.ElementMethods
TorsionQuadraticModulesMorphism = TorsionQuadraticModulesCategory.MorphismMethods
