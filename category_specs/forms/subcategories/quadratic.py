r"""Modules equipped with quadratic forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import FormedModulesCategory, OverPIDFormedModulesCategory

if TYPE_CHECKING:
    from ...types import RModuleElement


class QuadraticModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, q)`` with ``q`` quadratic on ``M``.

    Canonical chain: ``Modules(R).WithForms().Quadratic()``.
    """

    _base_category_class_and_axiom = (FormedModulesCategory, "Quadratic")
    _defining_predicates = ("is_quadratic",)

    class ParentMethods:
        @override
        @final
        def is_quadratic(self) -> bool:
            return True

        @final
        def q(self, v: RModuleElement) -> RModuleElement:
            r"""Introduced here: evaluate the quadratic form on a module element."""
            return self.form().q(v)

    class ElementMethods: ...

    class MorphismMethods: ...


class OverPIDQuadraticModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Quadratic formed modules over a PID.

    Canonical chain: ``Modules(R).OverPID().WithForms().Quadratic()``.
    """

    _base_category_class_and_axiom = (OverPIDFormedModulesCategory, "Quadratic")
    _defining_predicates = ("is_quadratic",)

    ParentMethods = QuadraticModulesCategory.ParentMethods
    ElementMethods = QuadraticModulesCategory.ElementMethods
    MorphismMethods = QuadraticModulesCategory.MorphismMethods


QuadraticModulesObject = QuadraticModulesCategory.ParentMethods
QuadraticModulesElement = QuadraticModulesCategory.ElementMethods
QuadraticModulesMorphism = QuadraticModulesCategory.MorphismMethods
OverPIDQuadraticModulesObject = OverPIDQuadraticModulesCategory.ParentMethods
OverPIDQuadraticModulesElement = OverPIDQuadraticModulesCategory.ElementMethods
OverPIDQuadraticModulesMorphism = OverPIDQuadraticModulesCategory.MorphismMethods
