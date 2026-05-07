r"""Fields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, assert_never, final, override

from sage.categories.fields import Fields as SageFields
from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport
from sage.misc.cachefunc import cached_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings
from .commutative import _CommutativeRings as _CommutativeRings

from ._lazy_subcategories import (
    _CC,
    _DivisionRings,
    _EuclideanDomains,
    _IntegrallyClosedDomains,
    _NoetherianRings,
    _QQ,
    _RR,
    _ReducedRings,
)

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Field,
        Ideal,
        RingElement,
    )


class _Fields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field()``."""

    _base_category_class_and_axiom = (_CommutativeRings, "Field")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
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

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageFields() or (R in self.base_category() and R.is_field())

    Finite = LazyImport(
        "category_specs.rings.subcategories.finite_field", "_FiniteFields"
    )
    NumberFields = LazyImport(
        "category_specs.rings.subcategories.number_field", "_NumberFields"
    )
    AlgebraicallyClosed = LazyImport(
        "category_specs.rings.subcategories.algebraically_closed_field",
        "_AlgebraicallyClosedFields",
    )
    LocalFields = LazyImport(
        "category_specs.rings.subcategories.local_field", "_LocalFields"
    )
    GlobalFields = LazyImport(
        "category_specs.rings.subcategories.global_field", "_GlobalFields"
    )

    class SubcategoryMethods:
        @cached_method
        @final
        def NumberFields(self) -> Category:
            return self._with_axiom("NumberFields")

        @cached_method
        @final
        def AlgebraicallyClosed(self) -> Category:
            return self._with_axiom("AlgebraicallyClosed")

        @cached_method
        @final
        def LocalFields(self) -> Category:
            return self._with_axiom("LocalFields")

        @cached_method
        @final
        def GlobalFields(self) -> Category:
            return self._with_axiom("GlobalFields")

    @cached_method
    @final
    def QQ(self):
        return _QQ()

    @cached_method
    @final
    def RR(self):
        return _RR()

    @cached_method
    @final
    def CC(self):
        return _CC()

    class ParentMethods:
        @abstract_method
        def is_algebraically_closed(self) -> bool: ...

        @abstract_method
        def algebraic_closure(self) -> Field: ...

        @override
        @final
        def gcd(self, r: RingElement, s: RingElement) -> RingElement:
            match r.is_zero() and s.is_zero():
                case True:
                    return self.zero()
                case False:
                    assert not r.is_zero() or not s.is_zero()
                    return self.one()
                case unreachable:
                    assert_never(unreachable)

        @override
        @final
        def completion(self, I: Ideal) -> CompleteRing:
            # Field case split: only the zero and unit ideals exist.
            match I:
                case _ if I.is_zero():
                    return self
                case _ if I.is_one():
                    return self
                case unreachable:
                    assert_never(unreachable)

    class ElementMethods:
        @abstract_method
        def inverse(self) -> RingElement: ...

    class MorphismMethods: ...
