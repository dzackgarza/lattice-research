r"""One-object subcategory for Sage Cartesian products of sets."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.sets.cartesian_product import CartesianProduct as SageCartesianProduct

if TYPE_CHECKING:
    from ...types import (
        CartesianProductFunctor,
        Integer,
        Set,
        SetElement,
        SetMorphism,
        SympySet,
    )

from ...cat import Category
from .. import Sets


class _CartesianProductSets(Category_singleton):
    r"""Cartesian products of sets and their tuple-like elements.

    Constructor target:
    ``Sets().Constructors().CartesianProduct(left, right)`` refines the binary
    product primitive here after Sage constructs the product parent. The explicit
    finite-factor compatibility surfaces
    ``Sets().Constructors().CartesianProductFromFactors(factors)`` and
    ``Sets().Constructors().cartesian_product(factors)`` refine into the same
    one-object category.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().CartesianProducts()]

    class ParentMethods:
        @override
        @final
        def cardinality(self):
            r"""Return the product cardinality of the factor sets."""
            return SageSets.CartesianProducts.ParentMethods.cardinality(self)

        @override
        @final
        def is_finite(self) -> bool:
            r"""Return whether this product set is finite."""
            return SageSets.CartesianProducts.ParentMethods.is_finite(self)

        @override
        @abstract_method
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def cartesian_factors(self) -> Sequence[Set]:
            r"""Return the factor sets of this Cartesian product."""
            ...

        @abstract_method
        def _sets_keys(self) -> Sequence[Set]: ...

        @abstract_method
        def cartesian_projection(self, i: Integer) -> Set:
            r"""Return the ``i``-th factor projection of this product set."""
            ...

        @abstract_method
        def _cartesian_product_of_elements(
            self, elements: Sequence[SetElement]
        ) -> SetElement: ...

        @override
        @abstract_method
        def construction(self) -> tuple[CartesianProductFunctor, Sequence[Set]]: ...

        @override
        @final
        def _coerce_map_from_(self, S: Set) -> bool | SetMorphism | None:
            r"""Return whether ``S`` coerces into this Cartesian product."""
            if isinstance(S, SageCartesianProduct):
                source_factors = S.cartesian_factors()
                target_factors = self.cartesian_factors()
                if len(source_factors) == len(target_factors) and all(
                    target.has_coerce_map_from(source)
                    for target, source in zip(target_factors, source_factors)
                ):
                    return True
            return None

        @override
        @final
        def _sympy_(self) -> SympySet:
            return SageSets.CartesianProducts.ParentMethods._sympy_(self)

    class ElementMethods:
        @abstract_method
        def cartesian_projection(self, i: Integer) -> SetElement:
            r"""Return the ``i``-th coordinate of this product element."""
            ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def __len__(self) -> Integer: ...

        @abstract_method
        def cartesian_factors(self) -> Sequence[SetElement]:
            r"""Return this Cartesian product element as ordered coordinates."""
            ...

    class MorphismMethods: ...
