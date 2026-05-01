r"""Order-theoretic join-semilattice poset subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from .. import Posets

if TYPE_CHECKING:
    from ...types import PosetElement


class _JoinSemilatticePosets(Category):
    r"""Posets in which every pair has a join."""

    @final
    def super_categories(self) -> list[Category]:
        return [Posets()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Finite(self) -> Category:
            return self._with_axiom("Finite")

    Finite = LazyImport(
        "category_specs.posets.subcategories.finite_join_semilattice",
        "_FiniteJoinSemilatticePosets",
    )

    class ParentMethods:
        @abstract_method
        def join(self, x: PosetElement, y: PosetElement) -> PosetElement:
            r"""Return the least upper bound of ``x`` and ``y``."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
