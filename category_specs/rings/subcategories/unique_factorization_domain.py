r"""UniqueFactorizationDomains ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.unique_factorization_domains import (
    UniqueFactorizationDomains as SageUniqueFactorizationDomains,
)
from sage.structure.factorization import Factorization

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ._lazy_subcategories import _GcdDomains
from .integral_domain import _IntegralDomains as _IntegralDomains

if TYPE_CHECKING:
    pass


class _UniqueFactorizationDomains(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().IntegralDomains().UniqueFactorization()``.
    """

    _base_category_class_and_axiom = (_IntegralDomains, "UniqueFactorization")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "unique factorization domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageUniqueFactorizationDomains(), _GcdDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageUniqueFactorizationDomains() or (
            R in self.base_category() and R.is_unique_factorization_domain()
        )

    class ElementMethods:
        @abstractmethod
        def factor(self) -> Factorization: ...

        @abstractmethod
        def is_irreducible(self) -> bool: ...

        @abstractmethod
        def is_prime(self) -> bool: ...

    class ParentMethods: ...

    class MorphismMethods: ...
