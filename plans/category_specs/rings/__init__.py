"""Static ring category surface for the module redesign.

This file defines a new ``Rings`` category as a staged replacement for Sage's
ring category.  Every named category below is mathematical: it records the
expected Sage-backed method surface and has immediate supercategories in
existing Sage ring categories where Sage provides them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_ideal
from sage.categories.commutative_ring_ideals import CommutativeRingIdeals
from sage.categories.rings import Rings as SageRings
from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from ..modules import Modules
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
from .constructions import _MatrixAlgebras
from .specialized import (
    _CC,
    _QQ,
    _Qp,
    _RR,
    _ZZ,
    _Zp,
    _AlgebraicallyClosedFields,
    _ArchimedeanGlobalFields,
    _CommutativeRings,
    _CompleteDiscreteValuationFields,
    _CompleteDiscreteValuationRings,
    _CompleteRings,
    _CyclotomicFields,
    _DedekindDomains,
    _DiscreteValuationFields,
    _DiscreteValuationRings,
    _DivisionRings,
    _EuclideanDomains,
    _Fields,
    _FiniteFields,
    _FiniteRings,
    _GcdDomains,
    _GlobalFields,
    _IntegralDomains,
    _IntegrallyClosedDomains,
    _LaurentSeriesRings,
    _LocalFields,
    _LocalRings,
    _NoetherianRings,
    _NonArchimedeanGlobalFields,
    _NumberFields,
    _PolynomialRings,
    _PowerSeriesRings,
    _PrincipalIdealDomains,
    _PuiseuxSeriesRings,
    _QuadraticNumberFields,
    _QuotientFields,
    _ReducedRings,
    _TopologicalRings,
    _UniqueFactorizationDomains,
    _ValuedRings,
)

if TYPE_CHECKING:
    from ..types import Ideal

_register_custom_axioms()


# ---------------------------------------------------------------------------
# Ring parent method surface — ABC, no default return values
# ---------------------------------------------------------------------------

class _RingObjectMethods:
    r"""Abstract parent methods for all objects in ``Rings``."""

    @abstract_method
    def is_exact(self) -> bool: ...

    @abstract_method
    def is_commutative_ring(self): ...

    @abstract_method
    def is_division_ring(self): ...

    @abstract_method
    def is_finite(self): ...

    @abstract_method
    def is_topological_ring(self): ...

    @abstract_method
    def is_valued_ring(self): ...

    @abstract_method
    def is_discrete_valuation_ring(self): ...

    @abstract_method
    def is_discrete_valuation_field(self): ...

    @abstract_method
    def is_complete_discrete_valuation_ring(self): ...

    @abstract_method
    def is_complete_discrete_valuation_field(self): ...

    @abstract_method
    def is_pid(self): ...

    @abstract_method
    def is_gcd_domain(self): ...

    @abstract_method
    def is_unique_factorization_domain(self, proof=True): ...

    @abstract_method
    def is_euclidean_domain(self): ...

    @abstract_method
    def is_reduced(self): ...

    @abstract_method
    def is_dedekind_domain(self): ...

    @abstract_method
    def is_finite_field(self): ...

    @abstract_method
    def is_number_field(self): ...

    @abstract_method
    def is_quotient_field(self): ...

    @abstract_method
    def is_algebraically_closed(self): ...

    @abstract_method
    def is_local_ring(self): ...

    @abstract_method
    def is_complete_ring(self): ...

    @abstract_method
    def is_polynomial_ring(self): ...

    @abstract_method
    def is_power_series_ring(self): ...

    @abstract_method
    def is_laurent_series_ring(self): ...

    @abstract_method
    def is_puiseux_series_ring(self): ...

    @abstract_method
    def is_local_field(self): ...

    @abstract_method
    def is_global_field(self): ...

    @abstract_method
    def is_archimedean_global_field(self): ...

    @abstract_method
    def is_nonarchimedean_global_field(self): ...

    @abstract_method
    def is_quadratic_number_field(self): ...

    @abstract_method
    def is_cyclotomic_field(self): ...


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
    def additive_order(self): ...

    @abstract_method
    def multiplicative_order(self): ...

    @abstract_method
    def is_square(self) -> bool: ...

    @abstract_method
    def abs(self): ...

    @abstract_method
    def nth_root(self, n: Integer, *args, **kwds): ...

    @abstract_method
    def sqrt(self, *args, **kwds): ...

    @abstract_method
    def powers(self, n: Integer) -> list: ...

    def principal_ideal(self) -> Ideal:
        return self.parent().principal_ideal(self)


# ---------------------------------------------------------------------------
# Ring morphism method surface — universal ring homomorphism abstract interface
# ---------------------------------------------------------------------------

class _RingMorphismMethods:
    r"""Abstract morphism methods present on all ring homomorphisms."""

    @abstract_method
    def domain(self): ...

    @abstract_method
    def codomain(self): ...

    @abstract_method
    def image(self, I=None): ...

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
    def section(self): ...

    @abstract_method
    def pre_compose(self, other): ...

    @abstract_method
    def post_compose(self, other): ...


# ---------------------------------------------------------------------------
# Ideal category — parent/element/morphism surfaces
# ---------------------------------------------------------------------------

class _RingIdealParentMethods:
    r"""Abstract parent methods for ring ideals."""

    def is_ideal(self) -> bool:
        return True

    @abstract_method
    def ring(self): ...

    @abstract_method
    def gen(self, i=0): ...

    @abstract_method
    def gens(self): ...

    @abstract_method
    def ngens(self) -> int: ...

    @abstract_method
    def gens_reduced(self): ...

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
    def divides(self, other) -> bool: ...

    @abstract_method
    def norm(self): ...

    @abstract_method
    def radical(self): ...

    @abstract_method
    def reduce(self, f): ...

    @abstract_method
    def random_element(self, *args, **kwds): ...


class _RingIdealElementMethods:
    r"""Abstract element methods for elements of ring ideals."""

    @abstract_method
    def is_unit(self) -> bool: ...

    @abstract_method
    def is_zero(self) -> bool: ...


class _RingIdealMorphismMethods:
    r"""Abstract morphism methods for ring ideal homomorphisms."""

    @abstract_method
    def domain(self): ...

    @abstract_method
    def codomain(self): ...


class _RingIdeals(Category_ideal):
    r"""Ideals of a ring in the redesigned category surface."""

    def _repr_object_names(self) -> str:
        return "ring ideals"

    def super_categories(self) -> list[Any]:
        R = self.ring()
        return [CommutativeRingIdeals(R), Modules(R).RIdeals()]

    @classmethod
    def from_sage_ideal(cls, sage_ideal) -> Ideal:
        R = sage_ideal.ring()
        sage_ideal.parent()._refine_category_([cls(R), Modules(R).RIdeals()])
        return sage_ideal

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
    locals().update(
        {k: v for k, v in vars(_RingNamedShortcuts).items() if not k.startswith("_")}
    )

    def __contains__(self, R: Any) -> bool:
        match R:
            case _ if isinstance(R, Category) and R.is_subcategory(self):
                return True
            case _ if R in SageRings():
                return True
            case _:
                # TODO: check if THIS category is anywhere in the object's ambient category hierarchy.
                return False

    @final
    def super_categories(self) -> list[Category]:
        return [SageRings()]

    @final
    def additional_structure(self):
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
