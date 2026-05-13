r"""ValuedRings ring subcategory spec."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar, cast, final, override

from abc import abstractmethod
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings

if TYPE_CHECKING:
    from ...types import (
        RingElement,
        Valuation,
    )


_ValuedCachedMethod = TypeVar("_ValuedCachedMethod", bound=Callable[..., object])


def _valued_cached_method(method: _ValuedCachedMethod) -> _ValuedCachedMethod:
    return cast(_ValuedCachedMethod, cached_method(method))


class _ValuedRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().WithValuation()``."""

    _base_category_class_and_axiom = (Rings, "WithValuation")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "valued rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_valued_ring()

    DiscretelyValued = LazyImport(
        "category_specs.rings.subcategories.discrete_valuation_ring",
        "_DiscreteValuationRings",
    )

    class SubcategoryMethods:
        @_valued_cached_method
        @final
        def DiscretelyValued(self) -> Category:
            return cast(Category, self._with_axiom("DiscretelyValued"))

    class ParentMethods:
        @override
        @final
        def is_valued_ring(self) -> bool:
            return True

        @abstractmethod
        def valuation(self) -> Valuation: ...

        @abstractmethod
        def roots_of_unity(self) -> list[RingElement]: ...

    class ElementMethods: ...

    class MorphismMethods: ...
