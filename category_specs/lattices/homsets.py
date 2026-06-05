r"""Hom, end, and aut categories for lattices.

``LatticeAutCategory`` is the lattice specialization of the orthogonal-group
surface: its objects are automorphism groups in the lattice category, hence
isometries of the integral formed module. The general owner remains the
modules-with-forms aut surface.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.misc.lazy_import import LazyImport

from ..forms.subcategories.free_bilinear import FreeBilinearModulesCategory
from ..homsets import (
    GenericAutCategory,
    GenericEndCategory,
    HomCategoryOf,
    UniversalAutElementMethods,
    UniversalEndElementMethods,
    UniversalHomObjectMethods,
)

if TYPE_CHECKING:
    from ...cat import Category
    from ..types import Lattice, LatticeOrthogonalGroup


class _LatticeHomCategoryObjectMethods(UniversalHomObjectMethods):
    r"""Lattice hom parent methods; generic hom methods are inherited."""


class _LatticeMorphisms(FreeBilinearModulesCategory.HomCategory.ElementMethods):
    r"""Morphisms of lattices: formed-module morphisms preserving the bilinear form."""


class _LatticeEndomorphisms(_LatticeMorphisms, UniversalEndElementMethods):
    r"""Endomorphisms (self-maps) in the lattice category."""


class _LatticeAutomorphisms(_LatticeEndomorphisms, UniversalAutElementMethods):
    r"""Lattice isometries, i.e. automorphisms in the lattice category."""

    @override
    @final
    def is_isometry(self) -> bool:
        return True


class LatticeHomCategory(HomCategoryOf):
    r"""Category of lattice hom objects ``Hom_Lattices(A, B)``.

    Canonical chain: ``Lattices(R).HomCategory()``.
    """

    @final
    def extra_super_categories(self) -> list[Category]:
        from ..modules import Modules

        R = self.base_category().base_ring()
        return [HomCategoryOf(self.base_category()), Modules(R).HomCategory()]

    ParentMethods = _LatticeHomCategoryObjectMethods
    ElementMethods = _LatticeMorphisms


    Endset = LazyImport(__name__, "LatticeEndCategory")


class LatticeEndCategory(GenericEndCategory):
    r"""Category of lattice endomorphism objects ``End_Lattices(A)``.

    Canonical chain: ``Lattices(R).EndCategory()``.
    """

    _base_category_class_and_axiom = (LatticeHomCategory, "Endset")
    Autset = LazyImport(__name__, "LatticeAutCategory")

    class ParentMethods:
        @abstractmethod
        def base_lattice(self) -> Lattice: ...

    ElementMethods = _LatticeEndomorphisms



class LatticeAutCategory(GenericAutCategory):
    r"""Category of lattice orthogonal groups ``Aut_Lattices(A)``.

    Canonical chain: ``Lattices(R).AutCategory()``.
    """

    _base_category_class_and_axiom = (LatticeEndCategory, "Autset")

    class ParentMethods:
        @abstractmethod
        def special_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return the determinant-one subgroup of this lattice orthogonal group."""
            ...

        @abstractmethod
        def stable_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return the subgroup acting trivially on the discriminant form.

            This is the stable orthogonal subgroup
            ``\widetilde O(L) = \ker(O(L) -> O(A_L, q_L))``.
            """
            ...

        @abstractmethod
        def stable_special_subgroup(self) -> LatticeOrthogonalGroup:
            r"""Return ``SO^+(L) = SO(L) \cap O^+(L)``.

            The subgroup is taken inside this lattice orthogonal group.
            """
            ...

        @final
        def special_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``SO(L)``.

            This is the determinant-one subgroup of this orthogonal group.
            """
            return self.special_subgroup()

        @final
        def stable_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``\widetilde O(L)``, the stable subgroup of this group."""
            return self.stable_subgroup()

        @final
        def stable_special_orthogonal_group(self) -> LatticeOrthogonalGroup:
            r"""Return ``SO^+(L) = SO(L) \cap O^+(L)``.

            The notation refers to the underlying lattice ``L``.
            """
            return self.stable_special_subgroup()

    ElementMethods = _LatticeAutomorphisms
