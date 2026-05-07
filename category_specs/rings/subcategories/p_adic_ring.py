r"""PAdicRings ring subcategory spec."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CompleteRings,
    _ValuedRings,
)
from .approximate import ApproximateRingsCategory

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Field,
        Polynomial,
        RealNumber,
        Ring,
        RingElement,
        RingMorphism,
    )


class _PAdicRings(Category_singleton):
    r"""Common category for Sage p-adic rings and fields.

    Constructor target: p-adic constructors under ``Rings().Constructors()``
    refine through this valued approximate family.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "p-adic rings and fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [ApproximateRingsCategory(), _CompleteRings(), _ValuedRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.rings.padics.generic_nodes import pAdicFieldGeneric, pAdicRingGeneric

        return isinstance(R, (pAdicFieldGeneric, pAdicRingGeneric))

    class ParentMethods:
        @abstract_method
        def prime(self) -> Integer: ...

        @abstract_method
        def precision_cap(self) -> Integer: ...

        @abstract_method
        def teichmuller(
            self, x: RingElement | Integer, prec: Integer | None = None
        ) -> RingElement: ...

        @abstract_method
        def teichmuller_system(self) -> list[RingElement]: ...

        @abstract_method
        def inertia_subring(self) -> CompleteRing: ...

        @abstract_method
        def residue_ring(self, n: Integer) -> Ring: ...

        @abstract_method
        def residue_system(self) -> list[RingElement]: ...

        @abstract_method
        def ground_ring(self) -> CompleteRing: ...

        @abstract_method
        def ground_ring_of_tower(self) -> CompleteRing: ...

        @abstract_method
        def ramification_index(self) -> Integer: ...

        @abstract_method
        def e(self) -> Integer: ...

        @abstract_method
        def inertia_degree(self) -> Integer: ...

        @abstract_method
        def f(self) -> Integer: ...

        @abstract_method
        def absolute_e(self) -> Integer: ...

        @abstract_method
        def absolute_f(self) -> Integer: ...

        @abstract_method
        def absolute_ramification_index(self) -> Integer: ...

        @abstract_method
        def absolute_inertia_degree(self) -> Integer: ...

        @abstract_method
        def relative_degree(self) -> Integer: ...

        @abstract_method
        def relative_e(self) -> Integer: ...

        @abstract_method
        def relative_f(self) -> Integer: ...

        @abstract_method
        def relative_ramification_index(self) -> Integer: ...

        @abstract_method
        def relative_inertia_degree(self) -> Integer: ...

        @abstract_method
        def print_mode(self) -> str: ...

        @abstract_method
        def change_precision(
            self, precision: Integer, precision_type: str | None = None
        ) -> CompleteRing: ...

        @abstract_method
        def change_prime(self, p: Integer) -> CompleteRing: ...

        @abstract_method
        def fraction_field(self) -> Field: ...

        @abstract_method
        def _change_print_mode(self, print_mode: str) -> CompleteRing: ...

        @abstract_method
        def ext(
            self,
            modulus: Polynomial,
            prec: Integer | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            implementation: str = "FLINT",
        ) -> CompleteRing: ...

        @abstract_method
        def frobenius_endomorphism(self, n: Integer = 1) -> RingMorphism: ...

        @abstract_method
        def maximal_unramified_subextension(self) -> CompleteRing: ...

        @abstract_method
        def defining_polynomial(
            self, var: str | None = None, exact: bool = False
        ) -> RingElement:
            del exact
            ...

        @abstract_method
        def integer_ring(self) -> CompleteRing: ...

        @abstract_method
        def exact_ring(self) -> Ring: ...

        @abstract_method
        def metric(self) -> Callable[[RingElement, RingElement], RealNumber]: ...

        @abstract_method
        def metric_function(
            self,
        ) -> Callable[[RingElement, RingElement], RealNumber]: ...

        @abstract_method
        def dist(self, x: RingElement, y: RingElement) -> RealNumber: ...

        @abstract_method
        def is_capped_absolute(self) -> bool: ...

        @abstract_method
        def is_capped_relative(self) -> bool: ...

        @abstract_method
        def is_fixed_mod(self) -> bool: ...

        @abstract_method
        def is_floating_point(self) -> bool: ...

        @abstract_method
        def is_relaxed(self) -> bool: ...

        @abstract_method
        def is_lattice_prec(self) -> bool: ...

        @abstract_method
        def has_pth_root(self) -> bool: ...

        @abstract_method
        def has_root_of_unity(self, n: Integer) -> bool: ...

    class ElementMethods: ...

    class MorphismMethods: ...
