r"""Lattice category surface.

``Lattices(R)`` is the named endpoint of the actual formed-module axiom chain

``Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral().Lattice()``.

The initializer owns the readable public index for the lattice subtree: the
root category class, constructor namespace, lattice-specific subcategories, and
standard type package aliases live here.  Detailed lattice method surfaces stay
in the subcategory files.

Subcategory hierarchy::

    Lattices(R)
    |-- OverDedekindDomain()
    |   `-- OverPID()
    |       `-- OverIntegers()
    |-- Even()
    |-- Unimodular()
    |-- Subobjects()
    |-- Quotients()
    |-- Subquotients()
    |-- ObjectsOver()
    |-- ObjectsUnder()
    |-- CartesianProducts()
    |-- DualLattices()
    |-- Overlattices()
    |-- OrthogonalDirectSums()
    |-- DiscriminantGroups()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..forms.chain import (
    _IntegralNondegenerateSymmetricFiniteRankFreeBilinearModules,
)
from ..modules import Modules
from .homsets import LatticeAutCategory, LatticeEndCategory, LatticeHomCategory
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

if TYPE_CHECKING:
    from ..types import Ring


class _Lattices(CategoryWithAxiom_over_base_ring):
    r"""Lattices over ``R`` as the named endpoint of the lattice axiom chain."""

    _base_category_class_and_axiom = (_IntegralNondegenerateSymmetricFiniteRankFreeBilinearModules, "Lattice")
    _defining_predicates = ("is_lattice",)

    @final
    def _repr_object_names(self) -> str:
        return f"lattices over {self.base_ring()}"

    class Constructors:
        r"""Lattice constructor entry points over ``self.base_ring()``."""

        @final
        def __init__(self, category: _Lattices) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return f"lattice constructors over {self.base_ring()}"

        @final
        def category(self) -> _Lattices:
            return self._category

        @final
        def base_ring(self) -> Ring:
            return self.category().base_ring()

    _Constructors = Constructors

    class SubcategoryMethods:
        @cached_method
        @final
        def Constructors(self) -> _Lattices.Constructors:
            return _Lattices._Constructors(self)

        @cached_method
        @final
        def OverDedekindDomain(self) -> Category:
            return self._with_axiom("OverDedekindDomain")

        @cached_method
        @final
        def OverPID(self) -> Category:
            return self._with_axiom("OverPID")

        @cached_method
        @final
        def OverIntegers(self) -> Category:
            return self._with_axiom("OverIntegers")

        @cached_method
        @final
        def Even(self) -> Category:
            return self._with_axiom("Even")

        @cached_method
        @final
        def Unimodular(self) -> Category:
            return self._with_axiom("Unimodular")

        @cached_method
        @final
        def DualLattices(self) -> Category:
            from .subcategories.constructions.dual_lattices import _DualLattices

            return _DualLattices(self.base_ring())

        @cached_method
        @final
        def Overlattices(self) -> Category:
            from .subcategories.constructions.overlattices import _Overlattices

            return _Overlattices(self.base_ring())

        @cached_method
        @final
        def OrthogonalDirectSums(self) -> Category:
            from .subcategories.constructions.orthogonal_direct_sums import _OrthogonalDirectSums

            return _OrthogonalDirectSums(self.base_ring())

        @cached_method
        @final
        def DiscriminantGroups(self) -> Category:
            from .subcategories.constructions.discriminant_groups import _DiscriminantGroups

            return _DiscriminantGroups(self.base_ring())

    class ParentMethods:
        @final
        def is_lattice(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...

    HomCategory = LatticeHomCategory

    OverDedekindDomain = LazyImport(
        "category_specs.lattices.subcategories.over_dedekind",
        "_LatticesOverDedekindDomain",
    )
    OverPID = LazyImport("category_specs.lattices.subcategories.over_pid", "_LatticesOverPID")
    OverIntegers = LazyImport("category_specs.lattices.subcategories.over_integers", "_LatticesOverIntegers")
    Even = LazyImport("category_specs.lattices.subcategories.even", "_EvenLattices")
    Unimodular = LazyImport("category_specs.lattices.subcategories.unimodular", "_UnimodularLattices")

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts
    DualLattices = LazyImport("category_specs.lattices.subcategories.constructions.dual_lattices", "_DualLattices")
    Overlattices = LazyImport("category_specs.lattices.subcategories.constructions.overlattices", "_Overlattices")
    OrthogonalDirectSums = LazyImport(
        "category_specs.lattices.subcategories.constructions.orthogonal_direct_sums",
        "_OrthogonalDirectSums",
    )
    DiscriminantGroups = LazyImport(
        "category_specs.lattices.subcategories.constructions.discriminant_groups",
        "_DiscriminantGroups",
    )


def _lattice_chain(base_ring: Ring) -> Category:
    r"""Return the immediate ambient category for ``Lattices(base_ring)``."""
    return (
        Modules(base_ring, dispatch=False)
        .Free()
        .FiniteRank()
        .WithForms()
        .Bilinear()
        .Symmetric()
        .Nondegenerate()
        .Integral()
    )


def lattice_category(base_ring: Ring) -> _Lattices:
    r"""Return ``Lattices(base_ring)`` as the named lattice axiom endpoint."""
    return _lattice_chain(base_ring).Lattice()


@final
def Lattices(base_ring: Ring) -> _Lattices:
    r"""Return the named lattice axiom category over ``base_ring``."""
    return lattice_category(base_ring)


LatticesCategory = _Lattices
LatticesObject = _Lattices.ParentMethods
LatticesElement = _Lattices.ElementMethods
LatticesMorphism = _Lattices.MorphismMethods
LatticesHomCategory = LatticeHomCategory
LatticesEndCategory = LatticeEndCategory
LatticesAutCategory = LatticeAutCategory
LatticesHom = LatticeHomCategory.ParentMethods
LatticesEnd = LatticeEndCategory.ParentMethods
LatticesAut = LatticeAutCategory.ParentMethods
LatticesEndomorphism = LatticeEndCategory.ElementMethods
LatticesAutomorphism = LatticeAutCategory.ElementMethods
