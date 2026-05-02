r"""Finite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.finite_sets import FiniteSets as SageFiniteSets
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, SetElement

from .. import Sets


class _FiniteSets(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().Finite()``."""
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
        def random_element(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
