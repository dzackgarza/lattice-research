"""Static ring category surface for the module redesign.

This file defines a new ``Rings`` category as a staged replacement for Sage's
ring category.  Every named category below is mathematical: it records the
expected Sage-backed method surface and has immediate supercategories in
existing Sage ring categories where Sage provides them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_ideal
from sage.categories.commutative_ring_ideals import CommutativeRingIdeals
from sage.categories.rings import Rings as SageRings
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.rings.integer import Integer

from ..modules import Modules
from ..utils import refine_category
from ._selectors import (
    _register_custom_axioms,
    _RingNamedShortcuts,
    _RingSubcategorySelectors,
)
from .constructions import (
    _Quotients,
    _RingsOver,
    _RingsUnder,
    _Subobjects,
    _Subquotients,
)
from .homsets import RingHomsets
from .matrix_algebras import (
    _MatrixAlgebras,
)
from .specialized import (
    _CC as _CC,
)
from .specialized import (
    _QQ as _QQ,
)
from .specialized import (
    _RR as _RR,
)
from .specialized import (
    _ZZ as _ZZ,
)
from .specialized import (
    _AlgebraicallyClosedFields as _AlgebraicallyClosedFields,
)
from .specialized import (
    _ArchimedeanGlobalFields as _ArchimedeanGlobalFields,
)
from .specialized import (
    _CommutativeRings as _CommutativeRings,
)
from .specialized import (
    _CompleteDiscreteValuationFields as _CompleteDiscreteValuationFields,
)
from .specialized import (
    _CompleteDiscreteValuationRings as _CompleteDiscreteValuationRings,
)
from .specialized import (
    _CompleteRings as _CompleteRings,
)
from .specialized import (
    _CyclotomicFields as _CyclotomicFields,
)
from .specialized import (
    _DedekindDomains as _DedekindDomains,
)
from .specialized import (
    _DiscreteValuationFields as _DiscreteValuationFields,
)
from .specialized import (
    _DiscreteValuationRings as _DiscreteValuationRings,
)
from .specialized import (
    _DivisionRings as _DivisionRings,
)
from .specialized import (
    _EuclideanDomains as _EuclideanDomains,
)
from .specialized import (
    _Fields as _Fields,
)
from .specialized import (
    _FiniteFields as _FiniteFields,
)
from .specialized import (
    _FiniteRings as _FiniteRings,
)
from .specialized import (
    _GcdDomains as _GcdDomains,
)
from .specialized import (
    _GlobalFields as _GlobalFields,
)
from .specialized import (
    _IntegralDomains as _IntegralDomains,
)
from .specialized import (
    _IntegrallyClosedDomains as _IntegrallyClosedDomains,
)
from .specialized import (
    _LaurentSeriesRings as _LaurentSeriesRings,
)
from .specialized import (
    _LocalFields as _LocalFields,
)
from .specialized import (
    _LocalRings as _LocalRings,
)
from .specialized import (
    _NoetherianRings as _NoetherianRings,
)
from .specialized import (
    _NonArchimedeanGlobalFields as _NonArchimedeanGlobalFields,
)
from .specialized import (
    _NumberFields as _NumberFields,
)
from .specialized import (
    _PolynomialRings as _PolynomialRings,
)
from .specialized import (
    _PowerSeriesRings as _PowerSeriesRings,
)
from .specialized import (
    _PrincipalIdealDomains as _PrincipalIdealDomains,
)
from .specialized import (
    _PuiseuxSeriesRings as _PuiseuxSeriesRings,
)
from .specialized import (
    _Qp as _Qp,
)
from .specialized import (
    _QuadraticNumberFields as _QuadraticNumberFields,
)
from .specialized import (
    _QuotientFields as _QuotientFields,
)
from .specialized import (
    _ReducedRings as _ReducedRings,
)
from .specialized import (
    _TopologicalRings as _TopologicalRings,
)
from .specialized import (
    _UniqueFactorizationDomains as _UniqueFactorizationDomains,
)
from .specialized import (
    _ValuedRings as _ValuedRings,
)
from .specialized import (
    _Zp as _Zp,
)

if TYPE_CHECKING:
    from ..types import (
        Cardinality,
        FreeModule,
        Ideal,
        Monoid,
        Ring,
        RingAutset,
        RingElement,
        RingEndset,
        RingHomset,
        RingMorphism,
    )

_register_custom_axioms()


# ---------------------------------------------------------------------------
# Ring parent method surface — ABC, no default return values
# ---------------------------------------------------------------------------


class _RingObjectMethods:
    r"""Abstract parent methods for all objects in ``Rings``."""

    @abstract_method
    def is_exact(self) -> bool: ...

    @abstract_method
    def is_commutative_ring(self) -> bool: ...

    @abstract_method
    def is_division_ring(self) -> bool: ...

    @abstract_method
    def is_finite(self) -> bool: ...

    @abstract_method
    def is_topological_ring(self) -> bool: ...

    @abstract_method
    def is_valued_ring(self) -> bool: ...

    @abstract_method
    def is_discrete_valuation_ring(self) -> bool: ...

    @abstract_method
    def is_discrete_valuation_field(self) -> bool: ...

    @abstract_method
    def is_complete_discrete_valuation_ring(self) -> bool: ...

    @abstract_method
    def is_complete_discrete_valuation_field(self) -> bool: ...

    @abstract_method
    def is_pid(self) -> bool: ...

    @abstract_method
    def is_gcd_domain(self) -> bool: ...

    @abstract_method
    def is_unique_factorization_domain(self, proof: bool = True) -> bool: ...

    @abstract_method
    def is_euclidean_domain(self) -> bool: ...

    @abstract_method
    def is_reduced(self) -> bool: ...

    @abstract_method
    def is_dedekind_domain(self) -> bool: ...

    @abstract_method
    def is_finite_field(self) -> bool: ...

    @abstract_method
    def is_number_field(self) -> bool: ...

    @abstract_method
    def is_quotient_field(self) -> bool: ...

    @abstract_method
    def is_local_ring(self) -> bool: ...

    @abstract_method
    def is_complete_ring(self) -> bool: ...

    @abstract_method
    def is_polynomial_ring(self) -> bool: ...

    @abstract_method
    def is_power_series_ring(self) -> bool: ...

    @abstract_method
    def is_laurent_series_ring(self) -> bool: ...

    @abstract_method
    def is_puiseux_series_ring(self) -> bool: ...

    @abstract_method
    def is_local_field(self) -> bool: ...

    @abstract_method
    def is_global_field(self) -> bool: ...

    @abstract_method
    def is_archimedean_global_field(self) -> bool: ...

    @abstract_method
    def is_nonarchimedean_global_field(self) -> bool: ...

    @abstract_method
    def is_quadratic_number_field(self) -> bool: ...

    @abstract_method
    def is_cyclotomic_field(self) -> bool: ...

    @abstract_method
    def ideal_monoid(self) -> Monoid: ...

    @abstract_method
    def Hom(self, codomain: Ring) -> RingHomset:
        return Rings().Hom(self, codomain)

    def End(self) -> RingEndset:
        r"""Return End(self) = Hom(self, self)."""
        return Rings().End(self)

    def Aut(self) -> RingAutset:
        r"""Return Aut(self) as the invertible subset of End(self)."""
        return Rings().Autsets().from_endset(self.End())

    def __pow__(self, n: Integer) -> FreeModule:
        return Modules(self).NamedModules().FreeModule(n)


# ---------------------------------------------------------------------------
# Ring element method surface — universal ring element abstract interface
# ---------------------------------------------------------------------------


class _RingElementMethods:
    r"""Abstract element methods present on all ring elements."""

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def is_one(self) -> bool: ...

    @abstract_method
    def is_nilpotent(self) -> bool: ...

    def is_idempotent(self) -> bool:
        return self * self == self

    @abstract_method
    def additive_order(self) -> Cardinality: ...

    @abstract_method
    def multiplicative_order(self) -> Cardinality: ...

    @abstract_method
    def is_square(self) -> bool: ...

    @abstract_method
    def abs(self) -> RingElement: ...

    @abstract_method
    def nth_root(self, n: Integer, *args, **kwds) -> RingElement | list[RingElement]: ...

    @abstract_method
    def sqrt(
        self,
        extend: bool = True,
        all: bool = False,
        name: str | None = None,
    ) -> RingElement | list[RingElement]: ...

    @abstract_method
    def powers(self, n: Integer) -> list[RingElement]: ...

    def principal_ideal(self) -> Ideal:
        return self.parent().principal_ideal(self)


# ---------------------------------------------------------------------------
# Ring morphism method surface — universal ring homomorphism abstract interface
# ---------------------------------------------------------------------------


class _RingMorphismMethods:
    r"""Abstract morphism methods present on all ring homomorphisms."""

    @abstract_method
    def domain(self) -> Ring: ...

    @abstract_method
    def codomain(self) -> Ring: ...

    @abstract_method
    def image(self, I: Ideal | None = None) -> Ideal: ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    @abstract_method
    def is_endomorphism(self) -> bool: ...

    @abstract_method
    def is_identity(self) -> bool: ...

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def kernel(self) -> Ideal: ...

    @abstract_method
    def section(self) -> RingMorphism: ...

    @abstract_method
    def pre_compose(self, other: RingMorphism) -> RingMorphism: ...

    @abstract_method
    def post_compose(self, other: RingMorphism) -> RingMorphism: ...


RingHomsets.ElementMethods = _RingMorphismMethods


# ---------------------------------------------------------------------------
# Ideal category — parent/element/morphism surfaces
# ---------------------------------------------------------------------------


class _RingIdealParentMethods:
    r"""Abstract parent methods for ring ideals."""

    def is_ideal(self) -> bool:
        return True

    @abstract_method
    def ring(self) -> Ring: ...

    @abstract_method
    def gen(self, i: int = 0) -> RingElement: ...

    @abstract_method
    def gens(self) -> tuple[RingElement, ...]: ...

    @abstract_method
    def ngens(self) -> int: ...

    @abstract_method
    def gens_reduced(self) -> tuple[RingElement, ...]: ...

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def is_one(self) -> bool: ...

    @abstract_method
    def is_trivial(self) -> bool: ...

    @abstract_method
    def is_prime(self) -> bool: ...

    @abstract_method
    def is_maximal(self) -> bool: ...

    @abstract_method
    def is_primary(self) -> bool: ...

    @abstract_method
    def is_principal(self) -> bool: ...

    @abstract_method
    def is_idempotent(self) -> bool: ...

    @abstract_method
    def divides(self, other: RingElement) -> bool: ...

    @abstract_method
    def norm(self) -> RingElement: ...

    @abstract_method
    def radical(self) -> Ideal: ...

    @abstract_method
    def reduce(self, f: RingElement) -> RingElement: ...

    @abstract_method
    def random_element(self, *args, **kwds) -> RingElement: ...


class _RingIdealElementMethods:
    r"""Abstract element methods for elements of ring ideals."""

    @abstract_method
    def is_unit(self) -> bool: ...

    @abstract_method
    def is_zero(self) -> bool: ...


class _RingIdealMorphismMethods:
    r"""Abstract morphism methods for ring ideal homomorphisms."""

    @abstract_method
    def domain(self) -> Ideal: ...

    @abstract_method
    def codomain(self) -> Ideal: ...


class _RingIdeals(Category_ideal):
    r"""Ideals of a ring in the redesigned category surface."""

    def _repr_object_names(self) -> str:
        return "ring ideals"

    def super_categories(self) -> list[Category]:
        R = self.ring()
        return [CommutativeRingIdeals(R), Modules(R).RIdeals()]

    @classmethod
    def from_sage_ideal(cls, sage_ideal) -> Ideal:
        R = sage_ideal.ring()
        return refine_category(sage_ideal.parent(), [cls(R), Modules(R).RIdeals()])

    ParentMethods = _RingIdealParentMethods
    ElementMethods = _RingIdealElementMethods
    MorphismMethods = _RingIdealMorphismMethods


# ---------------------------------------------------------------------------
# Rings — the root category
# ---------------------------------------------------------------------------


class Rings(Category_singleton):
    r"""Replacement ring category, staged below Sage's existing ``Rings``."""

    # Inject named shortcuts from _RingNamedShortcuts (Category_singleton forbids
    # multiple inheritance, so we merge the mixin's methods into the class namespace).
    locals().update({k: v for k, v in vars(_RingNamedShortcuts).items() if not k.startswith("_")})

    def __contains__(self, R: object) -> bool:
        match R:
            case _ if isinstance(R, Category) and R.is_subcategory(self):
                return True
            case _ if hasattr(R, "category"):
                try:
                    if R.category().is_subcategory(self):
                        return True
                except Exception:
                    pass
            case _ if R in SageRings():
                return True
            case _:
                return False

    @final
    def super_categories(self) -> list[Category]:
        return [SageRings()]

    @final
    def additional_structure(self) -> Category | None:
        return None

    SubcategoryMethods = _RingSubcategorySelectors

    # ----- Axiomatic subcategories -----------------------------------------

    Commutative = _CommutativeRings
    Division = _DivisionRings
    Finite = _FiniteRings
    Topological = _TopologicalRings
    WithValuation = _ValuedRings
    Polynomial = _PolynomialRings
    PowerSeries = _PowerSeriesRings
    LaurentSeries = _LaurentSeriesRings
    PuiseuxSeries = _PuiseuxSeriesRings

    # ----- Functorial constructions ----------------------------------------

    Subobjects = _Subobjects
    Subquotients = _Subquotients
    Quotients = _Quotients
    RingsUnder = _RingsUnder
    RingsOver = _RingsOver
    MatrixAlgebras = _MatrixAlgebras

    Homsets = RingHomsets

    @cached_method
    def Endsets(self) -> Category:
        return self.Homsets().Endset()

    @cached_method
    def Autsets(self) -> Category:
        return self.Homsets().Autset()

    ParentMethods = _RingObjectMethods
    ElementMethods = _RingElementMethods
    MorphismMethods = _RingMorphismMethods


# ---------------------------------------------------------------------------
# Wire _base_category_class_and_axiom for subcategories rooted at Rings
# ---------------------------------------------------------------------------
# Only classes whose base is the ``Rings`` class (from this module) require
# post-definition assignment; all other chains are defined inline in
# specialized.py.

_CommutativeRings._base_category_class_and_axiom = (Rings, "Commutative")
_DivisionRings._base_category_class_and_axiom = (Rings, "Division")
_FiniteRings._base_category_class_and_axiom = (Rings, "Finite")
_TopologicalRings._base_category_class_and_axiom = (Rings, "Topological")
_ValuedRings._base_category_class_and_axiom = (Rings, "WithValuation")
_PolynomialRings._base_category_class_and_axiom = (Rings, "Polynomial")
_LaurentSeriesRings._base_category_class_and_axiom = (Rings, "LaurentSeries")
_PuiseuxSeriesRings._base_category_class_and_axiom = (Rings, "PuiseuxSeries")
_PowerSeriesRings._base_category_class_and_axiom = (Rings, "PowerSeries")
