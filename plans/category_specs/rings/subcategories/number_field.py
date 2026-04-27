r"""NumberFields ring subcategory spec."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal, assert_never, override

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
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
from sage.rings.abc import ComplexBallField as SageComplexBallField
from sage.rings.abc import ComplexDoubleField as SageComplexDoubleField
from sage.rings.abc import ComplexField as SageComplexField
from sage.rings.abc import ComplexIntervalField as SageComplexIntervalField
from sage.rings.abc import RealBallField as SageRealBallField
from sage.rings.abc import RealDoubleField as SageRealDoubleField
from sage.rings.abc import RealField as SageRealField
from sage.rings.abc import RealIntervalField as SageRealIntervalField
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.integer import Integer
from sage.rings.laurent_series_ring import LaurentSeriesRing as SageLaurentSeriesRing
from sage.rings.lazy_series_ring import LazyLaurentSeriesRing, LazyPowerSeriesRing
from sage.rings.multi_power_series_ring import MPowerSeriesRing_generic
from sage.rings.number_field.number_field import (
    NumberField_cyclotomic,
    NumberField_quadratic,
)
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing_generic
from sage.rings.puiseux_series_ring import PuiseuxSeriesRing as SagePuiseuxSeriesRing
from sage.structure.factorization import Factorization

from .. import Rings

if TYPE_CHECKING:
    from ...types import (
        AbelianGroup,
        Cardinality,
        CompleteRing,
        ComplexInterval,
        Field,
        Group,
        Ideal,
        LocalRing,
        MaximalIdeal,
        Polynomial,
        PrimeIdeal,
        RealInterval,
        Ring,
        RingElement,
        RingMorphism,
        Valuation,
    )

_SAGE_POLYNOMIAL_RING_CLASSES = (PolynomialRing_generic, MPolynomialRing_base)
_SAGE_POWER_SERIES_RING_CLASSES = (
    PowerSeriesRing_generic,
    MPowerSeriesRing_generic,
    LazyPowerSeriesRing,
)
_SAGE_LAURENT_SERIES_RING_CLASSES = (
    SageLaurentSeriesRing,
    LazyLaurentSeriesRing,
)
_SAGE_PUISEUX_SERIES_RING_CLASSES = (SagePuiseuxSeriesRing,)
_SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES = _SAGE_LAURENT_SERIES_RING_CLASSES + _SAGE_POWER_SERIES_RING_CLASSES
_SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES = _SAGE_PUISEUX_SERIES_RING_CLASSES + _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES

_CommutativeRings = LazyImport("category_specs.rings.subcategories.commutative", "_CommutativeRings")
_FiniteRings = LazyImport("category_specs.rings.subcategories.finite", "_FiniteRings")
_DivisionRings = LazyImport("category_specs.rings.subcategories.division", "_DivisionRings")
_TopologicalRings = LazyImport("category_specs.rings.subcategories.topological", "_TopologicalRings")
_Fields = LazyImport("category_specs.rings.subcategories.field", "_Fields")
_IntegralDomains = LazyImport("category_specs.rings.subcategories.integral_domain", "_IntegralDomains")
_NoetherianRings = LazyImport("category_specs.rings.subcategories.noetherian", "_NoetherianRings")
_ReducedRings = LazyImport("category_specs.rings.subcategories.reduced", "_ReducedRings")
_GcdDomains = LazyImport("category_specs.rings.subcategories.gcd_domain", "_GcdDomains")
_UniqueFactorizationDomains = LazyImport("category_specs.rings.subcategories.unique_factorization_domain", "_UniqueFactorizationDomains")
_PrincipalIdealDomains = LazyImport("category_specs.rings.subcategories.principal_ideal_domain", "_PrincipalIdealDomains")
_EuclideanDomains = LazyImport("category_specs.rings.subcategories.euclidean_domain", "_EuclideanDomains")
_IntegrallyClosedDomains = LazyImport("category_specs.rings.subcategories.integrally_closed_domain", "_IntegrallyClosedDomains")
_DedekindDomains = LazyImport("category_specs.rings.subcategories.dedekind_domain", "_DedekindDomains")
_ValuedRings = LazyImport("category_specs.rings.subcategories.valued", "_ValuedRings")
_DiscreteValuationRings = LazyImport("category_specs.rings.subcategories.discrete_valuation_ring", "_DiscreteValuationRings")
_DiscreteValuationFields = LazyImport("category_specs.rings.subcategories.discrete_valuation_field", "_DiscreteValuationFields")
_CompleteRings = LazyImport("category_specs.rings.subcategories.complete", "_CompleteRings")
_LocalRings = LazyImport("category_specs.rings.subcategories.local", "_LocalRings")
_CompleteDiscreteValuationObjects = LazyImport("category_specs.rings.subcategories.complete_discrete_valuation_object", "_CompleteDiscreteValuationObjects")
_CompleteDiscreteValuationRings = LazyImport("category_specs.rings.subcategories.complete_discrete_valuation_ring", "_CompleteDiscreteValuationRings")
_CompleteDiscreteValuationFields = LazyImport("category_specs.rings.subcategories.complete_discrete_valuation_field", "_CompleteDiscreteValuationFields")
_FiniteFields = LazyImport("category_specs.rings.subcategories.finite_field", "_FiniteFields")
_NumberFields = LazyImport("category_specs.rings.subcategories.number_field", "_NumberFields")
_AlgebraicallyClosedFields = LazyImport("category_specs.rings.subcategories.algebraically_closed_field", "_AlgebraicallyClosedFields")
_LocalFields = LazyImport("category_specs.rings.subcategories.local_field", "_LocalFields")
_GlobalFields = LazyImport("category_specs.rings.subcategories.global_field", "_GlobalFields")
_ArchimedeanGlobalFields = LazyImport("category_specs.rings.subcategories.archimedean_global_field", "_ArchimedeanGlobalFields")
_NonArchimedeanGlobalFields = LazyImport("category_specs.rings.subcategories.nonarchimedean_global_field", "_NonArchimedeanGlobalFields")
_QuadraticNumberFields = LazyImport("category_specs.rings.subcategories.quadratic_number_field", "_QuadraticNumberFields")
_CyclotomicFields = LazyImport("category_specs.rings.subcategories.cyclotomic_field", "_CyclotomicFields")
_QuotientFields = LazyImport("category_specs.rings.subcategories.quotient_field", "_QuotientFields")
_PAdicRings = LazyImport("category_specs.rings.subcategories.p_adic_ring", "_PAdicRings")
_AlgebraicFields = LazyImport("category_specs.rings.subcategories.algebraic_field", "_AlgebraicFields")
_IntegerModRings = LazyImport("category_specs.rings.subcategories.integer_mod_ring", "_IntegerModRings")
_RealPrecisionFields = LazyImport("category_specs.rings.subcategories.real_precision_field", "_RealPrecisionFields")
_ComplexPrecisionFields = LazyImport("category_specs.rings.subcategories.complex_precision_field", "_ComplexPrecisionFields")
_ScientificNotationFields = LazyImport("category_specs.rings.subcategories.scientific_notation_field", "_ScientificNotationFields")
_RealFields = LazyImport("category_specs.rings.subcategories.real_field", "_RealFields")
_ComplexFields = LazyImport("category_specs.rings.subcategories.complex_field", "_ComplexFields")
_RealDoubleFields = LazyImport("category_specs.rings.subcategories.real_double_field", "_RealDoubleFields")
_ComplexDoubleFields = LazyImport("category_specs.rings.subcategories.complex_double_field", "_ComplexDoubleFields")
_RealIntervalFields = LazyImport("category_specs.rings.subcategories.real_interval_field", "_RealIntervalFields")
_ComplexIntervalFields = LazyImport("category_specs.rings.subcategories.complex_interval_field", "_ComplexIntervalFields")
_RealBallFields = LazyImport("category_specs.rings.subcategories.real_ball_field", "_RealBallFields")
_ComplexBallFields = LazyImport("category_specs.rings.subcategories.complex_ball_field", "_ComplexBallFields")
_QQbar = LazyImport("category_specs.rings.subcategories.algebraic_closure_of_rational_field", "_QQbar")
_AA = LazyImport("category_specs.rings.subcategories.real_algebraic_field", "_AA")
_ZZ = LazyImport("category_specs.rings.subcategories.integer_ring", "_ZZ")
_QQ = LazyImport("category_specs.rings.subcategories.rational_field", "_QQ")
_RR = LazyImport("category_specs.rings.subcategories.real_field_53", "_RR")
_CC = LazyImport("category_specs.rings.subcategories.complex_field_53", "_CC")
_Zp = LazyImport("category_specs.rings.subcategories.p_adic_integer_ring", "_Zp")
_Qp = LazyImport("category_specs.rings.subcategories.p_adic_field", "_Qp")
_PolynomialRings = LazyImport("category_specs.rings.subcategories.polynomial_ring", "_PolynomialRings")
_PuiseuxSeriesRings = LazyImport("category_specs.rings.subcategories.puiseux_series_ring", "_PuiseuxSeriesRings")
_LaurentSeriesRings = LazyImport("category_specs.rings.subcategories.laurent_series_ring", "_LaurentSeriesRings")
_PowerSeriesRings = LazyImport("category_specs.rings.subcategories.power_series_ring", "_PowerSeriesRings")

class _NumberFields(CategoryWithAxiom):
    _base_category_class_and_axiom = (_Fields, "NumberFields")

    def _repr_object_names(self) -> str:
        return "number fields"

    def super_categories(self) -> list[Category]:
        return [SageNumberFields(), _Fields()]

    def __contains__(self, R: Any) -> bool:
        return R in SageNumberFields() or (R in self.base_category() and R.is_number_field())

    Quadratic = LazyImport("category_specs.rings.subcategories.quadratic_number_field", "_QuadraticNumberFields")
    Cyclotomic = LazyImport("category_specs.rings.subcategories.cyclotomic_field", "_CyclotomicFields")

    class SubcategoryMethods:
        @cached_method
        def Quadratic(self):
            return self._with_axiom("Quadratic")

        @cached_method
        def Cyclotomic(self):
            return self._with_axiom("Cyclotomic")

    class ParentMethods:
        def is_number_field(self) -> bool:
            return True

        @abstract_method
        def is_quadratic(self) -> bool: ...

        @abstract_method
        def is_cyclotomic(self) -> bool: ...

        @abstract_method
        def degree(self) -> Integer: ...

        @abstract_method
        def absolute_degree(self) -> Integer: ...

        @abstract_method
        def signature(self) -> tuple[Integer, Integer]: ...

        @abstract_method
        def discriminant(self, v: Sequence[RingElement] | None = None) -> Integer | RingElement: ...

        @abstract_method
        def absolute_discriminant(self) -> Integer: ...

        @abstract_method
        def galois_group(
            self,
            type: str | None = None,
            algorithm: str = "pari",
            names: str | None = None,
            gc_numbering: bool | None = None,
        ) -> Group: ...

        @abstract_method
        def galois_closure(self, names: str | None = None, map: bool = False) -> Field | tuple[Field, RingMorphism]: ...

        @abstract_method
        def automorphisms(self) -> list[RingMorphism]: ...

        @abstract_method
        def class_number(self, proof: bool | None = None) -> Integer: ...

        @abstract_method
        def class_group(self, proof: bool | None = None, names: str = "c") -> AbelianGroup: ...

        @abstract_method
        def integral_basis(self, v: RingElement | Sequence[RingElement] | None = None) -> tuple[RingElement, ...]: ...

        @abstract_method
        def power_basis(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def reduced_basis(self, prec: Integer | int | None = None) -> tuple[RingElement, ...]: ...

        @abstract_method
        def different(self) -> Ideal: ...

        @abstract_method
        def places(
            self, all_complex: bool = False, prec: Integer | int | None = None
        ) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def real_embeddings(self, prec: Integer | int = 53) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def complex_embeddings(self, prec: Integer | int = 53) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def roots_of_unity(self) -> list[RingElement]: ...

        @abstract_method
        def regulator(self, proof: bool | None = None) -> RingElement: ...

        @abstract_method
        def units(self, proof: bool | None = None) -> list[RingElement]: ...

        @abstract_method
        def unit_group(self, proof: bool | None = None) -> AbelianGroup: ...

        @abstract_method
        def conductor(self, check_abelian: bool = True) -> Integer: ...

        @abstract_method
        def prime_above(self, x: RingElement, degree: Integer | int | None = None) -> PrimeIdeal: ...

        @abstract_method
        def primes_above(self, x: RingElement, degree: Integer | int | None = None) -> list[PrimeIdeal]: ...

        @abstract_method
        def S_units(self, S: Sequence[PrimeIdeal], proof: bool = True) -> list[RingElement]: ...

        @abstract_method
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup: ...

        @abstract_method
        def ring_of_integers(
            self,
            v: Integer | Sequence[Integer] | None = None,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstract_method
        def maximal_order(
            self,
            v: Integer | Sequence[Integer] | None = None,
            assume_maximal: bool | None | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstract_method
        def absolute_field(self, names: str) -> Field: ...

    class ElementMethods:
        @abstract_method
        def norm(self, K: Field | None = None) -> RingElement: ...

        @abstract_method
        def trace(self, K: Field | None = None) -> RingElement: ...

        @abstract_method
        def minpoly(self, var: str = "x", algorithm: str | None = None) -> RingElement: ...

        @abstract_method
        def charpoly(self, var: str = "x", algorithm: str | None = None) -> RingElement: ...
