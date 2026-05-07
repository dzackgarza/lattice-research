r"""ReducedRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .commutative import _CommutativeRings as _CommutativeRings

if TYPE_CHECKING:
    from ...types import (
        Ring,
    )

class _ReducedRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Reduced()``."""

    _base_category_class_and_axiom = (_CommutativeRings, "Reduced")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "reduced rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_CommutativeRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_reduced()

    class ParentMethods:
        @override
        @final
        def is_reduced(self) -> bool:
            return True

        @abstract_method
        def integral_closure(self) -> Ring: ...

    class ElementMethods: ...

    class MorphismMethods: ...
