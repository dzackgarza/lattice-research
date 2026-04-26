r"""Finite set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.finite_sets import FiniteSets as SageFiniteSets
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, SetElement

from .. import Sets


class _FiniteSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Finite")

    def _repr_object_names(self) -> str:
        return "finite sets"

    def super_categories(self) -> list:
        return [SageFiniteSets(), Sets().Countable()]

    def __contains__(self, S) -> bool:
        return S in SageFiniteSets() or (S in self.base_category() and S.is_finite())

    class ParentMethods:
        def is_finite(self) -> bool:
            return True

        @abstract_method
        def cardinality(self) -> Cardinality: ...

        def __len__(self) -> int:
            return int(self.cardinality())

        @abstract_method
        def list(self) -> list[SetElement]: ...

        @abstract_method
        def tuple(self) -> tuple[SetElement, ...]: ...

        @abstract_method
        def random_element(self) -> SetElement: ...

        def unrank_range(self, start=None, stop=None, step=None) -> list[SetElement]:
            r"""Return elements at rank positions ``[start, stop)`` with stride ``step``."""
            return list(self.iterator_range(start, stop, step))
