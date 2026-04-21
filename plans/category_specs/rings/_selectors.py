"""Axiom registration, subcategory selectors, and named shortcuts for Rings."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories import category_with_axiom as _category_with_axiom
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
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    pass

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


def _build_sage_category_refinements():
    from .specialized import (
        _CommutativeRings,
        _CompleteDiscreteValuationFields,
        _CompleteDiscreteValuationRings,
        _DedekindDomains,
        _DiscreteValuationFields,
        _DiscreteValuationRings,
        _DivisionRings,
        _EuclideanDomains,
        _Fields,
        _FiniteFields,
        _FiniteRings,
        _GcdDomains,
        _IntegralDomains,
        _NoetherianRings,
        _NumberFields,
        _PrincipalIdealDomains,
        _QuotientFields,
        _UniqueFactorizationDomains,
    )

    return {
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


class _RingSubcategorySelectors:
    r"""Mixin providing ``SubcategoryMethods`` axiom and functorial selectors."""

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
        from .constructions import _CharacteristicRings
        return _CharacteristicRings(self, p)

    @cached_method
    def KrullDimension(self, n):
        from .constructions import _KrullDimension
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
        from .constructions import _Subquotients
        return _Subquotients.category_of(self)

    @cached_method
    def Subobjects(self):
        from .constructions import _Subobjects
        return _Subobjects.category_of(self)

    @cached_method
    def Quotients(self):
        from .constructions import _Quotients
        return _Quotients.category_of(self)

    @cached_method
    def RingsUnder(self, structure_ring):
        from .constructions import _RingsUnder
        return _RingsUnder.category_of(self, structure_ring)

    @cached_method
    def RingsOver(self, structure_ring):
        from .constructions import _RingsOver
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


class _RingNamedShortcuts:
    r"""Mixin providing named category accessor shortcuts on ``Rings``."""

    @cached_method
    def CommutativeRings(self):
        from .specialized import _CommutativeRings
        return _CommutativeRings()

    @cached_method
    def DivisionRings(self):
        from .specialized import _DivisionRings
        return _DivisionRings()

    @cached_method
    def FiniteRings(self):
        from .specialized import _FiniteRings
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
        from .specialized import _NoetherianRings
        return _NoetherianRings()

    @cached_method
    def GcdDomains(self):
        from .specialized import _GcdDomains
        return _GcdDomains()

    @cached_method
    def UniqueFactorizationDomains(self):
        from .specialized import _UniqueFactorizationDomains
        return _UniqueFactorizationDomains()

    @cached_method
    def PrincipalIdealDomains(self):
        from .specialized import _PrincipalIdealDomains
        return _PrincipalIdealDomains()

    @cached_method
    def EuclideanDomains(self):
        from .specialized import _EuclideanDomains
        return _EuclideanDomains()

    @cached_method
    def DedekindDomains(self):
        from .specialized import _DedekindDomains
        return _DedekindDomains()

    @cached_method
    def ValuedRings(self):
        from .specialized import _ValuedRings
        return _ValuedRings()

    @cached_method
    def DiscreteValuationRings(self):
        from .specialized import _DiscreteValuationRings
        return _DiscreteValuationRings()

    @cached_method
    def DiscreteValuationFields(self):
        from .specialized import _DiscreteValuationFields
        return _DiscreteValuationFields()

    @cached_method
    def CompleteRings(self):
        from .specialized import _CompleteRings
        return _CompleteRings()

    @cached_method
    def CompleteDiscreteValuationRings(self):
        from .specialized import _CompleteDiscreteValuationRings
        return _CompleteDiscreteValuationRings()

    @cached_method
    def CompleteDiscreteValuationFields(self):
        from .specialized import _CompleteDiscreteValuationFields
        return _CompleteDiscreteValuationFields()

    @cached_method
    def LocalRings(self):
        from .specialized import _LocalRings
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
        from .specialized import _QuotientFields
        return _QuotientFields()

    @cached_method
    def ZZ(self):
        from .specialized import _ZZ
        return _ZZ()

    @cached_method
    def QQ(self):
        return self.Fields().QQ()
