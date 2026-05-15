r"""Fields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, assert_never, cast, final, override

from sage.categories.fields import Fields as SageFields
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings
from ._lazy_subcategories import (
    _CC,
    _QQ,
    _RR,
    _DivisionRings,
    _EuclideanDomains,
    _IntegrallyClosedDomains,
    _NoetherianRings,
    _ReducedRings,
)
from .commutative import _CommutativeRings as _CommutativeRings

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Field,
        Ideal,
        RingElement,
    )


def _field_cached_method[_FieldCachedMethod: Callable[..., object]](
    method: _FieldCachedMethod,
) -> _FieldCachedMethod:
    return cast(_FieldCachedMethod, cached_method(method))


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
        @_field_cached_method
        @final
        def NumberFields(self) -> Category:
            return cast(Category, self._with_axiom("NumberFields"))

        @_field_cached_method
        @final
        def AlgebraicallyClosed(self) -> Category:
            return cast(Category, self._with_axiom("AlgebraicallyClosed"))

        @_field_cached_method
        @final
        def LocalFields(self) -> Category:
            return cast(Category, self._with_axiom("LocalFields"))

        @_field_cached_method
        @final
        def GlobalFields(self) -> Category:
            return cast(Category, self._with_axiom("GlobalFields"))

    @_field_cached_method
    @final
    def QQ(self) -> Any:
        return _QQ()

    @_field_cached_method
    @final
    def RR(self) -> Any:
        return _RR()

    @_field_cached_method
    @final
    def CC(self) -> Any:
        return _CC()

    class ParentMethods:
        @abstractmethod
        def zero(self) -> RingElement: ...

        @abstractmethod
        def one(self) -> RingElement: ...

        @abstractmethod
        def is_algebraically_closed(self) -> bool: ...

        @abstractmethod
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
        def completion(self, ideal: Ideal) -> CompleteRing:
            # Field case split: only the zero and unit ideals exist.
            if ideal.is_zero():
                return self
            return Rings().Constructors().ZeroRing()

    class ElementMethods:
        @abstractmethod
        def inverse(self) -> RingElement: ...
