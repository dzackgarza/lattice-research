r"""Order-theoretic lattice poset subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.categories.lattice_posets import LatticePosets as SageLatticePosets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from .. import Posets

if TYPE_CHECKING:
    from ...types import PosetElement


class _LatticePosets(Category):
    r"""Posets in which every pair has a meet and join."""

    @final
    def super_categories(self) -> list:
        return [Posets(), SageLatticePosets()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Finite(self) -> Category:
            return self._with_axiom("Finite")

    Finite = LazyImport("category_specs.posets.subcategories.finite_lattice", "_FiniteLatticePosets")

    class ParentMethods:
        @abstract_method
        def meet(self, x: PosetElement, y: PosetElement) -> PosetElement:
            r"""Return the greatest lower bound of ``x`` and ``y``."""
            ...

        @abstract_method
        def join(self, x: PosetElement, y: PosetElement) -> PosetElement:
            r"""Return the least upper bound of ``x`` and ``y``."""
            ...
