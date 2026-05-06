r"""LocalRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .commutative import _CommutativeRings as _CommutativeRings


if TYPE_CHECKING:
    from ...types import (
        Field,
        MaximalIdeal,
    )

class _LocalRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Local()``."""

    _base_category_class_and_axiom = (_CommutativeRings, "Local")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "local rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_CommutativeRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_local_ring()

    class ParentMethods:
        @override
        @final
        def is_local_ring(self) -> bool:
            return True

        @abstract_method
        def maximal_ideal(self) -> MaximalIdeal: ...

        @abstract_method
        def residue_field(self) -> Field: ...

    class ElementMethods: ...

    class MorphismMethods: ...
