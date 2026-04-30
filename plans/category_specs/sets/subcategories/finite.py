r"""Finite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.finite_sets import FiniteSets as SageFiniteSets
from sage.misc.abstract_method import abstract_method

from ...cat import Category, CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement

from .. import Sets


class _FiniteSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Finite")

    @final
    def _repr_object_names(self) -> str:
        return "finite sets"

    @final
    def super_categories(self) -> list[Category]:
        return [SageFiniteSets(), Sets().Countable()]

    @final
    def __contains__(self, S: Any) -> bool:
        return S in SageFiniteSets() or (S in self.base_category() and S.is_finite())

    class ParentMethods:
        @final
        def is_finite(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @final
        def __len__(self) -> Integer:
            return int(self.cardinality())

        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def tuple(self) -> tuple[SetElement, ...]: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        @abstract_method
        def unrank_range(
            self,
            start: Integer | None = None,
            stop: Integer | None = None,
            step: Integer | None = None,
        ) -> list[SetElement]:
            r"""Return elements at rank positions ``[start, stop)`` with stride ``step``."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
