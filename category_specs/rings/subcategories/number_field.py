r"""NumberFields ring subcategory spec."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal, final, overload, override

from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .field import _Fields as _Fields

if TYPE_CHECKING:
    from ...types import (
        AbelianGroup,
        Field,
        Group,
        Ideal,
        PrimeIdeal,
        Ring,
        RingElement,
        RingMorphism,
    )


class _NumberFields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field().NumberFields()``."""

    _base_category_class_and_axiom = (_Fields, "NumberFields")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "number fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageNumberFields(), _Fields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageNumberFields() or (
            R in self.base_category() and R.is_number_field()
        )

    QuadraticNumberField = LazyImport(
        "category_specs.rings.subcategories.quadratic_number_field",
        "_QuadraticNumberFields",
    )
    Quadratic = QuadraticNumberField
    Cyclotomic = LazyImport(
        "category_specs.rings.subcategories.cyclotomic_field", "_CyclotomicFields"
    )

    class SubcategoryMethods:
        @cached_method
        @final
        def QuadraticNumberField(self) -> Category:
            return self._with_axiom("QuadraticNumberField")

        @cached_method
        @final
        def Quadratic(self) -> Category:
            return self.QuadraticNumberField()

        @cached_method
        @final
        def Cyclotomic(self) -> Category:
            return self._with_axiom("Cyclotomic")

    class ParentMethods:
        @override
        @final
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
        def discriminant(self) -> Integer: ...

        @abstract_method
        def trace_pairing_discriminant(
            self, elements: Sequence[RingElement]
        ) -> RingElement:
            r"""Return the determinant of the trace pairing on ``elements``."""
            ...

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

        @overload
        def galois_closure(
            self, names: str | None = None, map: Literal[False] = False
        ) -> Field: ...

        @overload
        def galois_closure(
            self, names: str | None = None, map: Literal[True] = True
        ) -> tuple[Field, RingMorphism]: ...

        @overload
        def galois_closure(
            self, names: str | None = None, map: bool = False
        ) -> Field | tuple[Field, RingMorphism]: ...

        @abstract_method
        def galois_closure(
            self, names: str | None = None, map: bool = False
        ) -> Field | tuple[Field, RingMorphism]: ...

        @abstract_method
        def automorphisms(self) -> list[RingMorphism]: ...

        @abstract_method
        def class_number(self, proof: bool | None = None) -> Integer: ...

        @abstract_method
        def class_group(
            self, proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup: ...

        @abstract_method
        def integral_basis(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def integral_basis_at_prime(self, prime: Integer) -> tuple[RingElement, ...]:
            r"""Return an integral basis for an order maximal at ``prime``."""
            ...

        @abstract_method
        def integral_basis_at_primes(
            self, primes: Sequence[Integer]
        ) -> tuple[RingElement, ...]:
            r"""Return an integral basis for an order maximal at each listed prime."""
            ...

        @abstract_method
        def power_basis(self) -> tuple[RingElement, ...]: ...

        @abstract_method
        def reduced_basis(
            self, prec: Integer | None = None
        ) -> tuple[RingElement, ...]: ...

        @abstract_method
        def different(self) -> Ideal: ...

        @abstract_method
        def places(
            self, all_complex: bool = False, prec: Integer | None = None
        ) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def real_embeddings(self, prec: Integer = 53) -> tuple[RingMorphism, ...]: ...

        @abstract_method
        def complex_embeddings(
            self, prec: Integer = 53
        ) -> tuple[RingMorphism, ...]: ...

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
        def prime_above(
            self, x: RingElement, degree: Integer | None = None
        ) -> PrimeIdeal: ...

        @abstract_method
        def primes_above(
            self, x: RingElement, degree: Integer | None = None
        ) -> list[PrimeIdeal]: ...

        @abstract_method
        def S_units(
            self, S: Sequence[PrimeIdeal], proof: bool = True
        ) -> list[RingElement]: ...

        @abstract_method
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup: ...

        @abstract_method
        def ring_of_integers(
            self,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstract_method
        def ring_of_integers_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order of integers that is maximal at ``prime``."""
            ...

        @abstract_method
        def ring_of_integers_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order of integers maximal at each listed prime."""
            ...

        @abstract_method
        def maximal_order(
            self,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstract_method
        def maximal_order_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order that is maximal at ``prime``."""
            ...

        @abstract_method
        def maximal_order_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order that is maximal at each listed prime."""
            ...

        @abstract_method
        def absolute_field(self, names: str) -> Field: ...

    class ElementMethods:
        @abstract_method
        def norm(self, K: Field | None = None) -> RingElement: ...

        @abstract_method
        def trace(self, K: Field | None = None) -> RingElement: ...

        @abstract_method
        def minpoly(
            self, var: str = "x", algorithm: str | None = None
        ) -> RingElement: ...

        @abstract_method
        def charpoly(
            self, var: str = "x", algorithm: str | None = None
        ) -> RingElement: ...

    class MorphismMethods: ...
