r"""Finite torsion modules with quadratic forms."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Self, final

from sage.categories.category import Category

from ...cat import Category_over_base_ring
from ...modules import Modules
from .quadratic import QuadraticModulesMorphism

if TYPE_CHECKING:
    from ...types import Group, Matrix, RModule, RModuleElement, RingElement


class TorsionQuadraticModulesCategory(Category_over_base_ring):
    r"""Finite ``ZZ``-modules equipped with a torsion quadratic form.

    Canonical chain:
    ``FinitelyPresentedModulesOverPID(ZZ).Torsion().WithForms().Quadratic()``.

    The invariant-factor surface belongs to
    ``Modules(R).FinitelyPresented().OverPID()`` and is inherited here.
    """

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Modules(R)
            .FinitelyPresented()
            .OverPID()
            .Torsion()
            .WithForms()
            .Quadratic(),
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
        def brown_invariant(self) -> RingElement: ...

        @abstractmethod
        def orthogonal_group(self) -> Group:
            r"""Return the automorphism group preserving the torsion quadratic form."""
            ...

        @abstractmethod
        def isotropic_elements(self) -> tuple[RModuleElement, ...]:
            r"""Return the finite tuple of elements ``x`` with ``q(x) = 0``."""
            ...

        @abstractmethod
        def normal_form(self, *, partial: bool = False) -> Self:
            r"""Return a canonical torsion quadratic module normal form."""
            ...

        @abstractmethod
        def primary_part(self, m: RingElement) -> Self:
            r"""Return the ``m``-primary formed submodule."""
            ...

        @abstractmethod
        def value_module(self) -> RModule:
            r"""Return the quotient module containing bilinear-form values."""
            ...

        @abstractmethod
        def value_module_qf(self) -> RModule:
            r"""Return the quotient module containing quadratic-form values."""
            ...

    class ElementMethods: ...


TorsionQuadraticModulesObject = TorsionQuadraticModulesCategory.ParentMethods
TorsionQuadraticModulesElement = TorsionQuadraticModulesCategory.ElementMethods
TorsionQuadraticModulesMorphism = QuadraticModulesMorphism
