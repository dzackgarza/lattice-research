r"""Dual-lattice construction category."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import DualObjectsCategory

if TYPE_CHECKING:
    from ....types import Lattice, LatticeMorphism


class _DualLattices(DualObjectsCategory):
    r"""Dual lattices ``L^* = {v in L_K | b(v, L) subset R}``."""

    @final
    def extra_super_categories(self):
        return [self.base_category().Rational()]

    class ParentMethods:
        @abstract_method
        def primal_lattice(self) -> Lattice: ...

        @abstract_method
        def inclusion_morphism(self) -> LatticeMorphism: ...

    class ElementMethods: ...
    class MorphismMethods: ...
