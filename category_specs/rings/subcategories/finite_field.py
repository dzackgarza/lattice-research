r"""FiniteFields ring subcategory spec."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.finite_fields import FiniteFields as SageFiniteFields
from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer
from sage.structure.factorization import Factorization

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .field import _Fields as _Fields

from ._lazy_subcategories import _FiniteRings


if TYPE_CHECKING:
    from ...types import (
        Group,
        RingElement,
    )


class _FiniteFields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field().Finite()``."""

    _base_category_class_and_axiom = (_Fields, "Finite")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "finite fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageFiniteFields(), _Fields(), _FiniteRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageFiniteFields() or (
            R in self.base_category() and R.is_finite_field()
        )

    class ParentMethods:
        @override
        @final
        def is_finite_field(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Integer: ...

        @abstract_method
        def order(self) -> Integer: ...

        @abstract_method
        def multiplicative_generator(self) -> RingElement: ...

        @abstract_method
        def primitive_element(self) -> RingElement: ...

        @abstract_method
        def modulus(self) -> RingElement: ...

        @abstract_method
        def factored_order(self) -> Factorization: ...

        @abstract_method
        def galois_group(self) -> Group: ...

        @abstract_method
        def dual_basis(
            self,
            basis: Sequence[RingElement] | None = None,
            check: bool = True,
        ) -> tuple[RingElement, ...]: ...

    class ElementMethods: ...

    class MorphismMethods: ...
