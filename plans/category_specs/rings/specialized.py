"""Private named ring category implementations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

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
from sage.rings.laurent_series_ring import LaurentSeriesRing as SageLaurentSeriesRing
from sage.rings.lazy_series_ring import LazyLaurentSeriesRing, LazyPowerSeriesRing
from sage.rings.multi_power_series_ring import MPowerSeriesRing_generic
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing_generic
from sage.rings.puiseux_series_ring import PuiseuxSeriesRing as SagePuiseuxSeriesRing
from sage.rings.integer import Integer

if TYPE_CHECKING:
    from ..types import Ideal, LocalRing, RingElement


def Rings(*args, **kwds):
    from . import Rings as _Rings

    return _Rings(*args, **kwds)


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
_SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES = (
    _SAGE_LAURENT_SERIES_RING_CLASSES + _SAGE_POWER_SERIES_RING_CLASSES
)
_SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES = (
    _SAGE_PUISEUX_SERIES_RING_CLASSES + _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES
)


def _construction_categories_for_sage_ring(root, R):
    if isinstance(R, _SAGE_POWER_SERIES_RING_CLASSES):
        return [root.PowerSeries().RingsUnder(R.base_ring())]
    if isinstance(R, _SAGE_LAURENT_SERIES_RING_CLASSES):
        return [root.LaurentSeries().RingsUnder(R.base_ring())]
    if isinstance(R, _SAGE_PUISEUX_SERIES_RING_CLASSES):
        return [root.PuiseuxSeries().RingsUnder(R.base_ring())]
    if isinstance(R, _SAGE_POLYNOMIAL_RING_CLASSES):
        return [root.Polynomial().RingsUnder(R.base_ring())]
    return []


def _singleton_categories_for_sage_ring(root, R):
    from sage.all import CC, QQ, RR, ZZ

    if R is ZZ:
        return [root.ZZ()]
    if R is QQ:
        return [root.QQ()]
    if R is RR:
        return [root.Fields().RR()]
    if R is CC:
        return [root.Fields().CC()]
    return []


class _CommutativeRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings(), SageCommutativeRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageCommutativeRings() or (
            R in self.base_category() and R.is_commutative_ring()
        )

    IntegralDomains = LazyImport(__name__, "_IntegralDomains")
    Field = LazyImport(__name__, "_Fields")
    Noetherian = LazyImport(__name__, "_NoetherianRings")
    Local = LazyImport(__name__, "_LocalRings")
    Reduced = LazyImport(__name__, "_ReducedRings")

    class SubcategoryMethods:
        @cached_method
        def IntegralDomains(self):
            return self._with_axiom("IntegralDomains")

        @cached_method
        def Field(self):
            return self._with_axiom("Field")

        @cached_method
        def Noetherian(self):
            return self._with_axiom("Noetherian")

        @cached_method
        def Local(self):
            return self._with_axiom("Local")

        @cached_method
        def Reduced(self):
            return self._with_axiom("Reduced")

    class ParentMethods:
        def is_commutative_ring(self) -> bool:
            return True

        @abstract_method
        def derivation(self, *args, **kwds): ...

        @abstract_method
        def derivation_module(self, *args, **kwds): ...

        @abstract_method
        def frobenius_endomorphism(self, *args, **kwds): ...

        @abstract_method
        def krull_dimension(self): ...

        @abstract_method
        def localization(self, *extra_units: RingElement, **kwds) -> LocalRing: ...

        @abstract_method
        def over(self, *args, **kwds): ...


class _FiniteRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings(), SageRings().Finite()]

    def __contains__(self, R: Any) -> bool:
        return R in SageRings().Finite() or (R in self.base_category() and R.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Integer: ...

        @abstract_method
        def order(self) -> Integer: ...


class _DivisionRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings(), SageDivisionRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageDivisionRings() or (
            R in self.base_category() and R.is_division_ring()
        )

    class ParentMethods:
        def is_division_ring(self) -> bool:
            return True


class _TopologicalRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings(), SageRings().Topological()]

    def __contains__(self, R: Any) -> bool:
        return R in SageRings().Topological() or (
            R in self.base_category() and R.is_topological_ring()
        )

    Complete = LazyImport(__name__, "_CompleteRings")

    class SubcategoryMethods:
        @cached_method
        def Complete(self):
            return self._with_axiom("Complete")

    class ParentMethods:
        def is_topological_ring(self) -> bool:
            return True


class _Fields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [
            SageFields(),
            _CommutativeRings(),
            _DivisionRings(),
            _EuclideanDomains(),
            _IntegrallyClosedDomains(),
            _NoetherianRings(),
            _ReducedRings(),
            Rings().KrullDimension(0),
        ]

    def __contains__(self, R: Any) -> bool:
        return R in SageFields() or (R in self.base_category() and R.is_field())

    Finite = LazyImport(__name__, "_FiniteFields")
    NumberFields = LazyImport(__name__, "_NumberFields")
    AlgebraicallyClosed = LazyImport(__name__, "_AlgebraicallyClosedFields")
    LocalFields = LazyImport(__name__, "_LocalFields")
    GlobalFields = LazyImport(__name__, "_GlobalFields")

    class SubcategoryMethods:
        @cached_method
        def NumberFields(self):
            return self._with_axiom("NumberFields")

        @cached_method
        def AlgebraicallyClosed(self):
            return self._with_axiom("AlgebraicallyClosed")

        @cached_method
        def LocalFields(self):
            return self._with_axiom("LocalFields")

        @cached_method
        def GlobalFields(self):
            return self._with_axiom("GlobalFields")

    @cached_method
    def QQ(self):
        return _QQ()

    @cached_method
    def RR(self):
        return _RR()

    @cached_method
    def CC(self):
        return _CC()

    class ParentMethods:
        def is_field(self) -> bool:
            return True

        @abstract_method
        def algebraic_closure(self, *args, **kwds): ...

        @abstract_method
        def an_embedding(self, *args, **kwds): ...

        @abstract_method
        def fraction_field(self): ...

        @abstract_method
        def prime_subfield(self, *args, **kwds): ...

        @abstract_method
        def vector_space(self, *args, **kwds): ...


class _IntegralDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageIntegralDomains(), _CommutativeRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageIntegralDomains() or (
            R in self.base_category() and R.is_integral_domain()
        )

    Gcd = LazyImport(__name__, "_GcdDomains")
    UniqueFactorization = LazyImport(__name__, "_UniqueFactorizationDomains")
    PrincipalIdeal = LazyImport(__name__, "_PrincipalIdealDomains")
    Euclidean = LazyImport(__name__, "_EuclideanDomains")
    IntegrallyClosed = LazyImport(__name__, "_IntegrallyClosedDomains")
    Dedekind = LazyImport(__name__, "_DedekindDomains")

    class SubcategoryMethods:
        @cached_method
        def Gcd(self):
            return self._with_axiom("Gcd")

        @cached_method
        def UniqueFactorization(self):
            return self._with_axiom("UniqueFactorization")

        @cached_method
        def PrincipalIdeal(self):
            return self._with_axiom("PrincipalIdeal")

        @cached_method
        def Euclidean(self):
            return self._with_axiom("Euclidean")

        @cached_method
        def IntegrallyClosed(self):
            return self._with_axiom("IntegrallyClosed")

        @cached_method
        def Dedekind(self):
            return self._with_axiom("Dedekind")

    class ParentMethods:
        def is_integral_domain(self) -> bool:
            return True

        @abstract_method
        def fraction_field(self): ...

        @abstract_method
        def class_group(self, *args, **kwds): ...


class _NoetherianRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageNoetherianRings(), _CommutativeRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageNoetherianRings() or (
            R in self.base_category() and R.is_noetherian()
        )

    class ParentMethods:
        def is_noetherian(self) -> bool:
            return True


class _ReducedRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_CommutativeRings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_reduced()

    class ParentMethods:
        def is_reduced(self) -> bool:
            return True

        @abstract_method
        def integral_closure(self, *args, **kwds): ...


class _GcdDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageGcdDomains(), _IntegralDomains()]

    def __contains__(self, R: Any) -> bool:
        return R in SageGcdDomains() or (R in self.base_category() and R.is_gcd_domain())

    class ParentMethods:
        def is_gcd_domain(self) -> bool:
            return True

        @abstract_method
        def gcd(self, *args, **kwds): ...


class _UniqueFactorizationDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageUniqueFactorizationDomains(), _GcdDomains()]

    def __contains__(self, R: Any) -> bool:
        return R in SageUniqueFactorizationDomains() or (
            R in self.base_category() and R.is_unique_factorization_domain()
        )

    class ParentMethods:
        def is_unique_factorization_domain(self, proof=True) -> bool:
            return True


class _PrincipalIdealDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SagePrincipalIdealDomains(), _UniqueFactorizationDomains()]

    def __contains__(self, R: Any) -> bool:
        return R in SagePrincipalIdealDomains() or (
            R in self.base_category() and R.is_pid()
        )

    class ParentMethods:
        def is_pid(self) -> bool:
            return True

        @abstract_method
        def content(self, *args, **kwds): ...


class _EuclideanDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageEuclideanDomains(), _PrincipalIdealDomains()]

    def __contains__(self, R: Any) -> bool:
        return R in SageEuclideanDomains() or (
            R in self.base_category() and R.is_euclidean_domain()
        )

    class ParentMethods:
        def is_euclidean_domain(self) -> bool:
            return True


class _IntegrallyClosedDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_IntegralDomains()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_integrally_closed()

    class ParentMethods:
        def is_integrally_closed(self) -> bool:
            return True

        def integral_closure(self, *args, **kwds):
            return self


class _DedekindDomains(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [
            SageDedekindDomains(),
            _IntegralDomains(),
            _NoetherianRings(),
            _IntegrallyClosedDomains(),
            Rings().KrullDimension(1),
        ]

    def __contains__(self, R: Any) -> bool:
        return R in SageDedekindDomains() or (
            R in self.base_category() and R.is_dedekind_domain()
        )

    class ParentMethods:
        def is_dedekind_domain(self) -> bool:
            return True

        def krull_dimension(self):
            return Integer(1)


class _ValuedRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_valued_ring()

    DiscretelyValued = LazyImport(__name__, "_DiscreteValuationRings")

    class SubcategoryMethods:
        @cached_method
        def DiscretelyValued(self):
            return self._with_axiom("DiscretelyValued")

    class ParentMethods:
        def is_valued_ring(self) -> bool:
            return True

        @abstract_method
        def valuation(self, *args, **kwds): ...


class _DiscreteValuationRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageDiscreteValuationRings(), _ValuedRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageDiscreteValuationRings() or (
            R in self.base_category() and R.is_discrete_valuation_ring()
        )

    class ParentMethods:
        def is_discrete_valuation_ring(self) -> bool:
            return True

        @abstract_method
        def uniformizer(self, *args, **kwds): ...

        @abstract_method
        def residue_field(self, *args, **kwds): ...


class _DiscreteValuationFields(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [SageDiscreteValuationFields(), _Fields(), _DiscreteValuationRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageDiscreteValuationFields() or (
            R in _Fields() and R.is_discrete_valuation_field()
        )

    class ParentMethods:
        def is_discrete_valuation_field(self) -> bool:
            return True


class _CompleteRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_TopologicalRings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_complete_ring()

    class ParentMethods:
        def is_complete_ring(self) -> bool:
            return True

        @abstract_method
        def completion(self, *args, **kwds) -> Any: ...


class _LocalRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_CommutativeRings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_local_ring()

    class ParentMethods:
        def is_local_ring(self) -> bool:
            return True

        @abstract_method
        def maximal_ideal(self) -> Ideal: ...

        @abstract_method
        def residue_field(self, *args, **kwds) -> Any: ...


class _CompleteDiscreteValuationRings(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [
            SageCompleteDiscreteValuationRings(),
            _CompleteRings(),
            _DiscreteValuationRings(),
        ]

    def __contains__(self, R: Any) -> bool:
        return R in SageCompleteDiscreteValuationRings() or (
            R in _DiscreteValuationRings()
            and R.is_complete_discrete_valuation_ring()
        )

    class ParentMethods:
        def is_complete_discrete_valuation_ring(self) -> bool:
            return True


class _CompleteDiscreteValuationFields(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [
            SageCompleteDiscreteValuationFields(),
            _CompleteRings(),
            _DiscreteValuationFields(),
        ]

    def __contains__(self, R: Any) -> bool:
        return R in SageCompleteDiscreteValuationFields() or (
            R in _DiscreteValuationFields()
            and R.is_complete_discrete_valuation_field()
        )

    class ParentMethods:
        def is_complete_discrete_valuation_field(self) -> bool:
            return True


class _FiniteFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageFiniteFields(), _Fields(), _FiniteRings()]

    def __contains__(self, R: Any) -> bool:
        return R in SageFiniteFields() or (R in self.base_category() and R.is_finite_field())

    class ParentMethods:
        def is_finite_field(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Integer: ...

        @abstract_method
        def order(self) -> Integer: ...


class _NumberFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [SageNumberFields(), _Fields()]

    def __contains__(self, R: Any) -> bool:
        return R in SageNumberFields() or (
            R in self.base_category() and R.is_number_field()
        )

    Quadratic = LazyImport(__name__, "_QuadraticNumberFields")
    Cyclotomic = LazyImport(__name__, "_CyclotomicFields")

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
        def ring_of_integers(self, *args, **kwds) -> Any: ...

        @abstract_method
        def maximal_order(self, *args, **kwds) -> Any: ...

        @abstract_method
        def absolute_field(self, *args, **kwds) -> Any: ...

        @abstract_method
        def completion(self, *args, **kwds) -> Any: ...

        @abstract_method
        def zeta_function(self, *args, **kwds) -> Any: ...


class _AlgebraicallyClosedFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_Fields()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_algebraically_closed()

    class ParentMethods:
        def is_algebraically_closed(self) -> bool:
            return True


class _LocalFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_Fields(), _TopologicalRings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_local_field()

    class ParentMethods:
        def is_local_field(self) -> bool:
            return True


class _GlobalFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_Fields()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_global_field()

    Archimedean = LazyImport(__name__, "_ArchimedeanGlobalFields")
    NonArchimedean = LazyImport(__name__, "_NonArchimedeanGlobalFields")

    class SubcategoryMethods:
        @cached_method
        def Archimedean(self):
            return self._with_axiom("Archimedean")

        @cached_method
        def NonArchimedean(self):
            return self._with_axiom("NonArchimedean")

    class ParentMethods:
        def is_global_field(self) -> bool:
            return True


class _ArchimedeanGlobalFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_GlobalFields()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_archimedean_global_field()

    class ParentMethods:
        def is_archimedean_global_field(self) -> bool:
            return True


class _NonArchimedeanGlobalFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_GlobalFields()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_nonarchimedean_global_field()

    class ParentMethods:
        def is_nonarchimedean_global_field(self) -> bool:
            return True


class _QuadraticNumberFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_NumberFields()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_quadratic_number_field()

    class ParentMethods:
        def is_quadratic_number_field(self) -> bool:
            return True


class _CyclotomicFields(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_NumberFields()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_cyclotomic_field()

    class ParentMethods:
        def is_cyclotomic_field(self) -> bool:
            return True


class _QuotientFields(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [SageQuotientFields(), _Fields()]

    def __contains__(self, R: Any) -> bool:
        return R in SageQuotientFields() or (R in _Fields() and R.is_quotient_field())

    class ParentMethods:
        def is_quotient_field(self) -> bool:
            return True


class _ZZ(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [
            _EuclideanDomains(),
            _DedekindDomains(),
            Rings().Characteristic(0),
        ]

    def __contains__(self, x):
        from sage.all import ZZ

        return x is ZZ

    def object(self):
        from sage.all import ZZ

        return ZZ


class _QQ(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [
            _Fields(),
            _QuotientFields(),
            _NumberFields(),
            _GlobalFields(),
            Rings().Characteristic(0),
        ]

    def __contains__(self, x):
        from sage.all import QQ

        return x is QQ

    def object(self):
        from sage.all import QQ

        return QQ


class _RR(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [_Fields(), _CompleteRings(), _LocalFields()]

    def __contains__(self, x):
        from sage.all import RR

        return x is RR

    def object(self):
        from sage.all import RR

        return RR


class _CC(Category_singleton):
    def super_categories(self) -> list[Any]:
        return [_Fields(), _CompleteRings(), _LocalFields(), _AlgebraicallyClosedFields()]

    def __contains__(self, x):
        from sage.all import CC

        return x is CC

    def object(self):
        from sage.all import CC

        return CC


class _PolynomialRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_POLYNOMIAL_RING_CLASSES)
            or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        def is_polynomial_ring(self) -> bool:
            return True

        @abstract_method
        def gen(self, *args, **kwds): ...

        @abstract_method
        def gens(self, *args, **kwds): ...


class _PuiseuxSeriesRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [Rings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES)
            or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        def is_puiseux_series_ring(self) -> bool:
            return True


class _LaurentSeriesRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_PuiseuxSeriesRings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES)
            or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        def is_laurent_series_ring(self) -> bool:
            return True


class _PowerSeriesRings(CategoryWithAxiom):
    def super_categories(self) -> list[Any]:
        return [_LaurentSeriesRings()]

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_POWER_SERIES_RING_CLASSES)
            or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        def is_power_series_ring(self) -> bool:
            return True

        @abstract_method
        def default_prec(self): ...
