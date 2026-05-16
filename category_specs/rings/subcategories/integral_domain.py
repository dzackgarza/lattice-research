r"""IntegralDomains ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, TypeVar, cast, final, override

from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...utils import with_axiom
from .commutative import _CommutativeRings as _CommutativeRings

_F = TypeVar("_F", bound=Callable[..., object])
_cached_method = cast(Callable[[_F], _F], cached_method)

if TYPE_CHECKING:
    from ...types import (
        Field,
        LocalRing,
        RingElement,
        RingMorphism,
    )


class _IntegralDomains(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().IntegralDomains()``."""

    _base_category_class_and_axiom = (_CommutativeRings, "IntegralDomains")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "integral domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageIntegralDomains(), _CommutativeRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageIntegralDomains() or (
            R in self.base_category() and R.is_integral_domain()
        )

    Gcd = LazyImport("category_specs.rings.subcategories.gcd_domain", "_GcdDomains")
    UniqueFactorization = LazyImport(
        "category_specs.rings.subcategories.unique_factorization_domain",
        "_UniqueFactorizationDomains",
    )
    PrincipalIdeal = LazyImport(
        "category_specs.rings.subcategories.principal_ideal_domain",
        "_PrincipalIdealDomains",
    )
    Euclidean = LazyImport(
        "category_specs.rings.subcategories.euclidean_domain", "_EuclideanDomains"
    )
    IntegrallyClosed = LazyImport(
        "category_specs.rings.subcategories.integrally_closed_domain",
        "_IntegrallyClosedDomains",
    )
    Dedekind = LazyImport(
        "category_specs.rings.subcategories.dedekind_domain", "_DedekindDomains"
    )

    class SubcategoryMethods:
        @_cached_method
        @final
        def Gcd(self) -> Category:
            return cast(Category, with_axiom(self, "Gcd"))

        @_cached_method
        @final
        def UniqueFactorization(self) -> Category:
            return cast(Category, with_axiom(self, "UniqueFactorization"))

        @_cached_method
        @final
        def PrincipalIdeal(self) -> Category:
            return cast(Category, with_axiom(self, "PrincipalIdeal"))

        @_cached_method
        @final
        def Euclidean(self) -> Category:
            return cast(Category, with_axiom(self, "Euclidean"))

        @_cached_method
        @final
        def IntegrallyClosed(self) -> Category:
            return cast(Category, with_axiom(self, "IntegrallyClosed"))

        @_cached_method
        @final
        def Dedekind(self) -> Category:
            return cast(Category, with_axiom(self, "Dedekind"))

    class ParentMethods:
        @abstractmethod
        def fraction_field(self) -> Field: ...

        @abstractmethod
        def localization(
            self,
            additional_units: RingElement | Sequence[RingElement],
            names: str | Sequence[str] | None = None,
            normalize: bool = True,
            category: Category | None = None,
        ) -> LocalRing:
            ...

    class ElementMethods:
        @abstractmethod
        def divides(self, other: RingElement) -> bool: ...
