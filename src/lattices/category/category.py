r"""Singular Sage category facade for algebraic lattice objects."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring

from category_specs.lattices import Lattices

from .elements import LatticeElementMethods, LatticeParentMethods
from .homsets import LatticeHomCategory

if TYPE_CHECKING:
    from category_specs.types import Ring


class LatticeCategory(Category_over_base_ring):
    r"""Category of single lattice parents over a base ring.

    The canonical mathematical endpoint remains ``Lattices(R)``. This singular
    category is an isolated implementation facade for concrete lattice parents,
    elements, and Hom objects.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"singular lattice objects over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        return [Lattices(self.base_ring())]

    ParentMethods = LatticeParentMethods
    ElementMethods = LatticeElementMethods
    HomCategory = LatticeHomCategory


def Lattice(base_ring: Ring) -> LatticeCategory:
    r"""Return the singular lattice category over ``base_ring``."""
    return LatticeCategory(base_ring)
