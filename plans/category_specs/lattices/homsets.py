r"""Hom, end, and aut categories for lattices.

``LatticeAutCategory`` is the lattice specialization of the orthogonal-group
surface: its objects are automorphism groups in the lattice category, hence
isometries of the integral formed module. The general owner remains the
modules-with-forms aut surface.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import Lattice, Matrix


class _LatticeHomCategoryObjectMethods:
    r"""Lattice hom parent methods; generic hom methods are inherited."""


class _LatticeMorphisms:
    r"""Morphisms of lattices: module morphisms preserving the bilinear form."""

    @abstract_method
    def to_matrix(self) -> Matrix: ...

    @abstract_method
    def is_isometry(self) -> bool:
        r"""Return whether this morphism preserves the bilinear form."""
        ...


class _LatticeAutomorphisms:
    r"""Lattice isometries, i.e. automorphisms in the lattice category."""

    @final
    def is_isometry(self) -> bool:
        return True


class LatticeHomCategory(HomCategoryOf):
    r"""Category of lattice hom objects ``Hom_Lattices(A, B)``."""

    @final
    def extra_super_categories(self):
        from ..modules import Modules

        R = self.base_category().base_ring()
        return [HomCategoryOf(self.base_category()), Modules(R).HomCategory()]

    ParentMethods = _LatticeHomCategoryObjectMethods
    ElementMethods = _LatticeMorphisms
    class MorphismMethods: ...

    Endset = LazyImport(__name__, "LatticeEndCategory")


class LatticeEndCategory(GenericEndCategory):
    r"""Category of lattice endomorphism objects ``End_Lattices(A)``."""

    _base_category_class_and_axiom = (LatticeHomCategory, "Endset")
    Autset = LazyImport(__name__, "LatticeAutCategory")

    class ParentMethods:
        @abstract_method
        def base_lattice(self) -> Lattice: ...

    ElementMethods = _LatticeMorphisms
    class MorphismMethods: ...


class LatticeAutCategory(GenericAutCategory):
    r"""Category of lattice orthogonal groups ``Aut_Lattices(A)``."""

    _base_category_class_and_axiom = (LatticeEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _LatticeAutomorphisms
    class MorphismMethods: ...
