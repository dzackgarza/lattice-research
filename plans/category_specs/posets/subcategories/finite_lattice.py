r"""Finite order-theoretic lattice poset subcategory."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, final

from sage.categories.finite_lattice_posets import FiniteLatticePosets as SageFiniteLatticePosets
from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .lattice import _LatticePosets

if TYPE_CHECKING:
    from ...types import FiniteLatticePoset, LatticePoset, PosetElement


class _FiniteLatticePosets(CategoryWithAxiom):
    r"""Finite lattice posets."""

    _base_category_class_and_axiom = (_LatticePosets, "Finite")

    @final
    def super_categories(self) -> list:
        return [_LatticePosets(), SageFiniteLatticePosets()]

    class ParentMethods:
        @abstract_method
        def join_irreducibles(self) -> list[PosetElement]:
            r"""Return the join-irreducible elements."""
            ...

        @abstract_method
        def join_irreducibles_poset(self) -> FiniteLatticePoset:
            r"""Return the poset of join-irreducible elements."""
            ...

        @abstract_method
        def meet_irreducibles(self) -> list[PosetElement]:
            r"""Return the meet-irreducible elements."""
            ...

        @abstract_method
        def meet_irreducibles_poset(self) -> FiniteLatticePoset:
            r"""Return the poset of meet-irreducible elements."""
            ...

        @abstract_method
        def irreducibles_poset(self) -> FiniteLatticePoset:
            r"""Return the poset of meet- and join-irreducible elements."""
            ...

        @abstract_method
        def is_lattice_morphism(self, f: Callable[[PosetElement], PosetElement], codomain: LatticePoset) -> bool:
            r"""Return whether ``f`` preserves finite meets and joins."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
