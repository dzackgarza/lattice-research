r"""Finite poset subcategory."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, final

from sage.categories.finite_posets import FinitePosets as SageFinitePosets
from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import FiniteLatticePoset, Poset, PosetElement, PosetMorphism, PosetSubset

from .. import Posets


class _FinitePosets(CategoryWithAxiom):
    r"""Finite partially ordered sets."""

    _base_category_class_and_axiom = (Posets, "Finite")

    @final
    def super_categories(self) -> list:
        return [Posets(), SageFinitePosets()]

    class ParentMethods:
        @abstract_method
        def is_poset_morphism(self, f: PosetMorphism, codomain: Poset) -> bool:
            r"""Return whether ``f`` is order-preserving into ``codomain``."""
            ...

        @abstract_method
        def order_ideals_lattice(self, facade: bool = True) -> FiniteLatticePoset:
            r"""Return the finite distributive lattice of order ideals."""
            ...

        @abstract_method
        def chains(self) -> Iterable[PosetSubset]:
            r"""Return the chains of this finite poset."""
            ...

        @abstract_method
        def antichains(self) -> Iterable[PosetSubset]:
            r"""Return the antichains of this finite poset."""
            ...

        @abstract_method
        def linear_extensions(self) -> Iterable[list[PosetElement]]:
            r"""Return the linear extensions of this finite poset."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
