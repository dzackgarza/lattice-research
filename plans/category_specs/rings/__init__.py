"""Static ring category surface for the module redesign.

This file defines a new ``Rings`` category as a staged replacement for Sage's
ring category.  Every named category below is mathematical: it records the
expected Sage-backed method surface and has immediate supercategories in
existing Sage ring categories where Sage provides them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories import category_with_axiom as _category_with_axiom
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_ideal
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
from sage.categories.complete_discrete_valuation import (
    CompleteDiscreteValuationFields as SageCompleteDiscreteValuationFields,
)
from sage.categories.complete_discrete_valuation import (
    CompleteDiscreteValuationRings as SageCompleteDiscreteValuationRings,
)
from sage.categories.dedekind_domains import DedekindDomains as SageDedekindDomains
from sage.categories.discrete_valuation import (
    DiscreteValuationFields as SageDiscreteValuationFields,
)
from sage.categories.discrete_valuation import (
    DiscreteValuationRings as SageDiscreteValuationRings,
)
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.euclidean_domains import EuclideanDomains as SageEuclideanDomains
from sage.categories.fields import Fields as SageFields
from sage.categories.finite_fields import FiniteFields as SageFiniteFields
from sage.categories.gcd_domains import GcdDomains as SageGcdDomains
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.noetherian_rings import NoetherianRings as SageNoetherianRings
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.categories.principal_ideal_domains import (
    PrincipalIdealDomains as SagePrincipalIdealDomains,
)
from sage.categories.quotient_fields import QuotientFields as SageQuotientFields
from sage.categories.rings import Rings as SageRings
from sage.categories.unique_factorization_domains import (
    UniqueFactorizationDomains as SageUniqueFactorizationDomains,
)
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer

from .constructions import (
    _CharacteristicRings,
    _KrullDimension,
    _Quotients,
    _RingsOver,
    _RingsUnder,
    _Subobjects,
    _Subquotients,
)
from .specialized import (
    _AlgebraicallyClosedFields,
    _ArchimedeanGlobalFields,
    _CC,
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
    _QQ,
    _QuotientFields,
    _RR,
    _ReducedRings,
    _TopologicalRings,
    _UniqueFactorizationDomains,
    _ValuedRings,
    _ZZ,
    _construction_categories_for_sage_ring,
    _singleton_categories_for_sage_ring,
)
from ..sage_modules import Modules

if TYPE_CHECKING:
    from ..types import FreeModule, Ideal, LocalRing, RingElement, RModule

Names = str | tuple[str, ...] | None

_CUSTOM_AXIOMS = (
    "Commutative",
    "Division",
    "Finite",
    "Topological",
    "WithValuation",
    "Characteristic",
    "Polynomial",
    "PowerSeries",
    "LaurentSeries",
    "PuiseuxSeries",
    "Field",
    "IntegralDomains",
    "Noetherian",
    "Local",
    "KrullDimension",
    "Reduced",
    "Gcd",
    "UniqueFactorization",
    "PrincipalIdeal",
    "Euclidean",
    "IntegrallyClosed",
    "Dedekind",
    "DiscretelyValued",
    "Complete",
    "NumberFields",
    "AlgebraicallyClosed",
    "LocalFields",
    "GlobalFields",
    "Archimedean",
    "NonArchimedean",
    "Quadratic",
    "Cyclotomic",
)


def _register_custom_axioms() -> None:
    missing = tuple(
        axiom
        for axiom in _CUSTOM_AXIOMS
        if axiom not in _category_with_axiom.all_axioms
    )
    if missing:
        _category_with_axiom.all_axioms += missing


_register_custom_axioms()


class _RingSubcategorySelectors:
    r"""Explicit ``Rings.SubcategoryMethods`` axiom and functorial surface."""

    @cached_method
    def Commutative(self):
        return self._with_axiom("Commutative")

    @cached_method
    def Division(self):
        return self._with_axiom("Division")

    @cached_method
    def Finite(self):
        return self._with_axiom("Finite")

    @cached_method
    def Topological(self):
        return self._with_axiom("Topological")

    @cached_method
    def WithValuation(self):
        return self._with_axiom("WithValuation")

    @cached_method
    def Characteristic(self, p):
        return _CharacteristicRings(self, p)

    @cached_method
    def KrullDimension(self, n):
        return _KrullDimension(self, n)

    @cached_method
    def Polynomial(self):
        return self._with_axiom("Polynomial")

    @cached_method
    def PowerSeries(self):
        return self._with_axiom("PowerSeries")

    @cached_method
    def LaurentSeries(self):
        return self._with_axiom("LaurentSeries")

    @cached_method
    def PuiseuxSeries(self):
        return self._with_axiom("PuiseuxSeries")

    @cached_method
    def Subquotients(self):
        return _Subquotients.category_of(self)

    @cached_method
    def Subobjects(self):
        return _Subobjects.category_of(self)

    @cached_method
    def Quotients(self):
        return _Quotients.category_of(self)

    @cached_method
    def RingsUnder(self, structure_ring):
        return _RingsUnder.category_of(self, structure_ring)

    @cached_method
    def RingsOver(self, structure_ring):
        return _RingsOver.category_of(self, structure_ring)

    @cached_method
    def PolynomialRings(self):
        return self.Polynomial()

    @cached_method
    def PolynomialRingsOver(self, structure_ring):
        return self.Polynomial().RingsUnder(structure_ring)

    @cached_method
    def PolynomialOver(self, structure_ring):
        return self.PolynomialRingsOver(structure_ring)

    @cached_method
    def PowerSeriesRings(self):
        return self.PowerSeries()

    @cached_method
    def PowerSeriesRingsOver(self, structure_ring):
        return self.PowerSeries().RingsUnder(structure_ring)

    @cached_method
    def PowerSeriesOver(self, structure_ring):
        return self.PowerSeriesRingsOver(structure_ring)

    @cached_method
    def LaurentSeriesRings(self):
        return self.LaurentSeries()

    @cached_method
    def LaurentSeriesRingsOver(self, structure_ring):
        return self.LaurentSeries().RingsUnder(structure_ring)

    @cached_method
    def LaurentSeriesOver(self, structure_ring):
        return self.LaurentSeriesRingsOver(structure_ring)

    @cached_method
    def PuiseuxSeriesRings(self):
        return self.PuiseuxSeries()

    @cached_method
    def PuiseuxSeriesRingsOver(self, structure_ring):
        return self.PuiseuxSeries().RingsUnder(structure_ring)

    @cached_method
    def PuiseuxSeriesOver(self, structure_ring):
        return self.PuiseuxSeriesRingsOver(structure_ring)

    @cached_method
    def QuotientRingsOf(self, structure_ring):
        return self.Quotients().RingsUnder(structure_ring)

    @cached_method
    def QuotientsOf(self, structure_ring):
        return self.QuotientRingsOf(structure_ring)

    @cached_method
    def SubringsOf(self, structure_ring):
        return self.Subobjects().RingsOver(structure_ring)


class _RingIdeals(Category_ideal):
    r"""Ideals of a ring in the redesigned category surface."""

    def super_categories(self) -> list[Any]:
        from sage.categories.commutative_ring_ideals import CommutativeRingIdeals

        R = self.ring()
        return [CommutativeRingIdeals(R), Modules(R).RIdeals()]

    @classmethod
    def from_ideal(cls, sage_ideal) -> Ideal:
        R = sage_ideal.ring()
        sage_ideal._refine_category_([cls(R), Modules(R).RIdeals()])
        return sage_ideal

    class ParentMethods:
        def is_ideal(self) -> bool:
            return True

        @final
        def ideal(self):
            return self

    class ElementMethods:
        pass

    class MorphismMethods:
        pass



class Rings(Category_singleton):
    r"""Replacement ring category, staged below Sage's existing ``Rings``."""

    def __contains__(self, R: Any) -> bool:
        return R in SageRings()

    @final
    def super_categories(self) -> list[Any]:
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

    SageCategoryRefinements = {
        SageCompleteDiscreteValuationFields(): _CompleteDiscreteValuationFields,
        SageCompleteDiscreteValuationRings(): _CompleteDiscreteValuationRings,
        SageDiscreteValuationFields(): _DiscreteValuationFields,
        SageDiscreteValuationRings(): _DiscreteValuationRings,
        SageFiniteFields(): _FiniteFields,
        SageNumberFields(): _NumberFields,
        SageQuotientFields(): _QuotientFields,
        SageFields(): _Fields,
        SageEuclideanDomains(): _EuclideanDomains,
        SagePrincipalIdealDomains(): _PrincipalIdealDomains,
        SageUniqueFactorizationDomains(): _UniqueFactorizationDomains,
        SageGcdDomains(): _GcdDomains,
        SageDedekindDomains(): _DedekindDomains,
        SageIntegralDomains(): _IntegralDomains,
        SageCommutativeRings(): _CommutativeRings,
        SageNoetherianRings(): _NoetherianRings,
        SageDivisionRings(): _DivisionRings,
        SageRings().Finite(): _FiniteRings,
    }

    # ----- Named shortcuts --------------------------------------------------

    @cached_method
    def CommutativeRings(self):
        return _CommutativeRings()

    @cached_method
    def DivisionRings(self):
        return _DivisionRings()

    @cached_method
    def FiniteRings(self):
        return _FiniteRings()

    @cached_method
    def IntegralDomains(self):
        return self.Commutative().IntegralDomains()

    @cached_method
    def Fields(self):
        return self.Commutative().Field()

    @cached_method
    def ReducedRings(self):
        return self.Commutative().Reduced()

    @cached_method
    def NoetherianRings(self):
        return _NoetherianRings()

    @cached_method
    def GcdDomains(self):
        return _GcdDomains()

    @cached_method
    def UniqueFactorizationDomains(self):
        return _UniqueFactorizationDomains()

    @cached_method
    def PrincipalIdealDomains(self):
        return _PrincipalIdealDomains()

    @cached_method
    def EuclideanDomains(self):
        return _EuclideanDomains()

    @cached_method
    def DedekindDomains(self):
        return _DedekindDomains()

    @cached_method
    def ValuedRings(self):
        return _ValuedRings()

    @cached_method
    def DiscreteValuationRings(self):
        return _DiscreteValuationRings()

    @cached_method
    def DiscreteValuationFields(self):
        return _DiscreteValuationFields()

    @cached_method
    def CompleteRings(self):
        return _CompleteRings()

    @cached_method
    def CompleteDiscreteValuationRings(self):
        return _CompleteDiscreteValuationRings()

    @cached_method
    def CompleteDiscreteValuationFields(self):
        return _CompleteDiscreteValuationFields()

    @cached_method
    def LocalRings(self):
        return _LocalRings()

    @cached_method
    def FiniteFields(self):
        return self.Fields().Finite()

    @cached_method
    def NumberFields(self):
        return self.Fields().NumberFields()

    @cached_method
    def AlgebraicallyClosedFields(self):
        return self.Fields().AlgebraicallyClosed()

    @cached_method
    def LocalFields(self):
        return self.Fields().LocalFields()

    @cached_method
    def GlobalFields(self):
        return self.Fields().GlobalFields()

    @cached_method
    def ArchimedeanGlobalFields(self):
        return self.GlobalFields().Archimedean()

    @cached_method
    def NonArchimedeanGlobalFields(self):
        return self.GlobalFields().NonArchimedean()

    @cached_method
    def QuadraticNumberFields(self):
        return self.NumberFields().Quadratic()

    @cached_method
    def CyclotomicFields(self):
        return self.NumberFields().Cyclotomic()

    @cached_method
    def QuotientFields(self):
        return _QuotientFields()

    @cached_method
    def ZZ(self):
        return _ZZ()

    @cached_method
    def QQ(self):
        return self.Fields().QQ()

    def from_sage_ring(self, R: Any):
        r"""Refine ``R`` into every redesigned category mirrored by Sage."""
        refined_categories = [self]
        for sage_category, refined_category in self.SageCategoryRefinements.items():
            if R in sage_category:
                refined_categories.append(refined_category())
        refined_categories.extend(_singleton_categories_for_sage_ring(self, R))
        refined_categories.extend(_construction_categories_for_sage_ring(self, R))
        R._refine_category_(refined_categories)
        return R

    class ParentMethods:
        def is_ring(self) -> bool:
            return True

        def is_commutative_ring(self) -> bool:
            return False

        def is_division_ring(self) -> bool:
            return False

        def is_finite(self) -> bool:
            return False

        def is_topological_ring(self) -> bool:
            return False

        def is_valued_ring(self) -> bool:
            return False

        def is_discrete_valuation_ring(self) -> bool:
            return False

        def is_discrete_valuation_field(self) -> bool:
            return False

        def is_complete_discrete_valuation_ring(self) -> bool:
            return False

        def is_complete_discrete_valuation_field(self) -> bool:
            return False

        def is_integral_domain(self) -> bool:
            return False

        def is_noetherian(self) -> bool:
            return False

        def is_pid(self) -> bool:
            return False

        def is_gcd_domain(self) -> bool:
            return False

        def is_unique_factorization_domain(self, proof=True) -> bool:
            return False

        def is_euclidean_domain(self) -> bool:
            return False

        def is_field(self) -> bool:
            return False

        def is_reduced(self) -> bool:
            return False

        def is_integrally_closed(self) -> bool:
            return False

        def is_dedekind_domain(self) -> bool:
            return False

        def is_finite_field(self) -> bool:
            return False

        def is_number_field(self) -> bool:
            return False

        def is_quotient_field(self) -> bool:
            return False

        def is_algebraically_closed(self) -> bool:
            return False

        def is_local_ring(self) -> bool:
            return False

        def is_complete_ring(self) -> bool:
            return False

        def is_polynomial_ring(self) -> bool:
            return False

        def is_power_series_ring(self) -> bool:
            return False

        def is_laurent_series_ring(self) -> bool:
            return False

        def is_puiseux_series_ring(self) -> bool:
            return False

        def is_local_field(self) -> bool:
            return False

        def is_global_field(self) -> bool:
            return False

        def is_archimedean_global_field(self) -> bool:
            return False

        def is_nonarchimedean_global_field(self) -> bool:
            return False

        def is_quadratic_number_field(self) -> bool:
            return False

        def is_cyclotomic_field(self) -> bool:
            return False

        @abstract_method
        def ideal(self, *args, **kwds) -> Ideal: ...

        @abstract_method
        def principal_ideal(self, generator: RingElement) -> Ideal: ...

        @abstract_method
        def quotient(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule: ...

        @abstract_method
        def quo(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule: ...

        @abstract_method
        def quotient_ring(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule: ...

        @abstract_method
        def __truediv__(self, modulus: RingElement | Ideal) -> RModule: ...

        @abstract_method
        def __pow__(self, n: Integer) -> FreeModule: ...

        @abstract_method
        def free_module(self, base=None, basis=None, map=True) -> FreeModule: ...

        @abstract_method
        def localization(self, *extra_units: RingElement, **kwds) -> LocalRing: ...

        @abstract_method
        def unit_ideal(self) -> Ideal: ...

        @abstract_method
        def nilradical(self) -> Ideal: ...

    class ElementMethods:
        def principal_ideal(self) -> Ideal:
            return self.parent().principal_ideal(self)

    class MorphismMethods:
        pass


def _constant_object_names(names):
    def _repr_object_names(self):
        return names

    return _repr_object_names


for _category_class, _object_names in (
    (_RingIdeals, "ring ideals"),
    (_CommutativeRings, "commutative rings"),
    (_FiniteRings, "finite rings"),
    (_DivisionRings, "division rings"),
    (_TopologicalRings, "topological rings"),
    (_Fields, "fields"),
    (_IntegralDomains, "integral domains"),
    (_NoetherianRings, "noetherian rings"),
    (_ReducedRings, "reduced rings"),
    (_GcdDomains, "gcd domains"),
    (_UniqueFactorizationDomains, "unique factorization domains"),
    (_PrincipalIdealDomains, "principal ideal domains"),
    (_EuclideanDomains, "euclidean domains"),
    (_IntegrallyClosedDomains, "integrally closed domains"),
    (_DedekindDomains, "Dedekind domains"),
    (_ValuedRings, "valued rings"),
    (_DiscreteValuationRings, "discrete valuation rings"),
    (_DiscreteValuationFields, "discrete valuation fields"),
    (_CompleteRings, "complete rings"),
    (_LocalRings, "local rings"),
    (_CompleteDiscreteValuationRings, "complete discrete valuation rings"),
    (_CompleteDiscreteValuationFields, "complete discrete valuation fields"),
    (_FiniteFields, "finite fields"),
    (_NumberFields, "number fields"),
    (_AlgebraicallyClosedFields, "algebraically closed fields"),
    (_LocalFields, "local fields"),
    (_GlobalFields, "global fields"),
    (_ArchimedeanGlobalFields, "archimedean global fields"),
    (_NonArchimedeanGlobalFields, "nonarchimedean global fields"),
    (_QuadraticNumberFields, "quadratic number fields"),
    (_CyclotomicFields, "cyclotomic fields"),
    (_QuotientFields, "quotient fields"),
    (_ZZ, "integer ring"),
    (_QQ, "rational field"),
    (_RR, "real field with 53 bits of precision"),
    (_CC, "complex field with 53 bits of precision"),
    (_PolynomialRings, "polynomial rings"),
    (_PuiseuxSeriesRings, "Puiseux series rings"),
    (_LaurentSeriesRings, "Laurent series rings"),
    (_PowerSeriesRings, "power series rings"),
):
    _category_class._repr_object_names = _constant_object_names(_object_names)


for _base_category_class, _axiom, _category_class in (
    (Rings, "Commutative", _CommutativeRings),
    (Rings, "Division", _DivisionRings),
    (Rings, "Finite", _FiniteRings),
    (Rings, "Topological", _TopologicalRings),
    (Rings, "WithValuation", _ValuedRings),
    (Rings, "Polynomial", _PolynomialRings),
    (Rings, "PowerSeries", _PowerSeriesRings),
    (Rings, "LaurentSeries", _LaurentSeriesRings),
    (Rings, "PuiseuxSeries", _PuiseuxSeriesRings),
    (_CommutativeRings, "IntegralDomains", _IntegralDomains),
    (_CommutativeRings, "Field", _Fields),
    (_CommutativeRings, "Noetherian", _NoetherianRings),
    (_CommutativeRings, "Local", _LocalRings),
    (_CommutativeRings, "Reduced", _ReducedRings),
    (_IntegralDomains, "Gcd", _GcdDomains),
    (_IntegralDomains, "UniqueFactorization", _UniqueFactorizationDomains),
    (_IntegralDomains, "PrincipalIdeal", _PrincipalIdealDomains),
    (_IntegralDomains, "Euclidean", _EuclideanDomains),
    (_IntegralDomains, "IntegrallyClosed", _IntegrallyClosedDomains),
    (_IntegralDomains, "Dedekind", _DedekindDomains),
    (_ValuedRings, "DiscretelyValued", _DiscreteValuationRings),
    (_TopologicalRings, "Complete", _CompleteRings),
    (_Fields, "Finite", _FiniteFields),
    (_Fields, "NumberFields", _NumberFields),
    (_Fields, "AlgebraicallyClosed", _AlgebraicallyClosedFields),
    (_Fields, "LocalFields", _LocalFields),
    (_Fields, "GlobalFields", _GlobalFields),
    (_GlobalFields, "Archimedean", _ArchimedeanGlobalFields),
    (_GlobalFields, "NonArchimedean", _NonArchimedeanGlobalFields),
    (_NumberFields, "Quadratic", _QuadraticNumberFields),
    (_NumberFields, "Cyclotomic", _CyclotomicFields),
):
    _category_class._base_category_class_and_axiom = (_base_category_class, _axiom)
