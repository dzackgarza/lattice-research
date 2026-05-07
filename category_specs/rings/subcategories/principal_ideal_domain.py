r"""PrincipalIdealDomains ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.principal_ideal_domains import (
    PrincipalIdealDomains as SagePrincipalIdealDomains,
)

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ._lazy_subcategories import _UniqueFactorizationDomains
from .integral_domain import _IntegralDomains as _IntegralDomains

if TYPE_CHECKING:
    from ...types import (
        Ideal,
        RingElement,
    )


class _PrincipalIdealDomains(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().IntegralDomains().PrincipalIdeal()``.
    """

    _base_category_class_and_axiom = (_IntegralDomains, "PrincipalIdeal")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "principal ideal domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SagePrincipalIdealDomains(), _UniqueFactorizationDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SagePrincipalIdealDomains() or (
            R in self.base_category() and R.is_pid()
        )

    class ParentMethods:
        @override
        @final
        def is_pid(self) -> bool:
            return True

        @final
        def ideal_generator(self, ideal: Ideal) -> RingElement:
            assert ideal.is_principal(), "PID ideal_generator expects a principal ideal"
            return ideal.gen()

        @override
        @final
        def gcd(self, r: RingElement, s: RingElement) -> RingElement:
            return self.ideal_generator(self.ideal(r, s))

    class ElementMethods: ...

    class MorphismMethods: ...
