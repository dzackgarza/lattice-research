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
    |-- DualObjects()
    |-- DualLattices()
    |-- Overlattices()
    |-- OrthogonalDirectSums()
    |-- DiscriminantGroups()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar, cast, final

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..forms.chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
)
from ..modules import Modules
from ..utils import with_axiom
from .homsets import (
    LatticeAutCategory,
    LatticeEndCategory,
    LatticeHomCategory,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import LatticeDualObjectsCategory
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

_F = TypeVar("_F", bound=Callable[..., object])
_cached_method = cast(Callable[[_F], _F], cached_method)

if TYPE_CHECKING:
    from ..types import Ring


class LatticesCategory(CategoryWithAxiom_over_base_ring):
    r"""Lattices over ``R`` as the named endpoint of the lattice axiom chain.

    Canonical chain: ``Lattices(R)``.
    """

    _base_category_class_and_axiom = (
        IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
        "Lattice",
    )
    _defining_predicates = ("is_lattice",)

    @final
    def _repr_object_names(self) -> str:
        return f"lattices over {self.base_ring()}"

    class _Constructors:
        r"""Lattice constructor entry points over ``self.base_ring()``."""

        @final
        def __init__(self, category: LatticesCategory) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return f"lattice constructors over {self.base_ring()}"

        @final
        def category(self) -> LatticesCategory:
            return self._category

        @final
        def base_ring(self) -> Ring:
            base_ring: Ring = self.category().base_ring()
            return base_ring

    @_cached_method
    @final
    def Constructors(self) -> LatticesCategory._Constructors:
        r"""Return the lattice constructor collector over ``self.base_ring()``."""
        return self.__class__._Constructors(self)

    class SubcategoryMethods:
        @_cached_method
        @final
        def OverDedekindDomain(self) -> Category:
            return cast(Category, with_axiom(self, "OverDedekindDomain"))

        @_cached_method
        @final
        def OverPID(self) -> Category:
            return cast(Category, with_axiom(self, "OverPID"))

        @_cached_method
        @final
        def OverIntegers(self) -> Category:
            return cast(Category, with_axiom(self, "OverIntegers"))

        @_cached_method
        @final
        def Even(self) -> Category:
            return cast(Category, with_axiom(self, "Even"))

        @_cached_method
        @final
        def Unimodular(self) -> Category:
            return cast(Category, with_axiom(self, "Unimodular"))

        @_cached_method
        @final
        def DualObjects(self) -> Category:
            return cast(Category, LatticeDualObjectsCategory.category_of(self))

        @_cached_method
        @final
        def DualLattices(self) -> Category:
            r"""Return the metric-dual lattice construction category."""
            from .subcategories.constructions.dual_lattices import DualLatticesCategory

            return DualLatticesCategory(self.base_ring())

        @_cached_method
        @final
        def Overlattices(self) -> Category:
            from .subcategories.constructions.overlattices import OverlatticesCategory

            return OverlatticesCategory(self.base_ring())

        @_cached_method
        @final
        def OrthogonalDirectSums(self) -> Category:
            from .subcategories.constructions.orthogonal_direct_sums import (
                OrthogonalDirectSumsCategory,
            )

            return OrthogonalDirectSumsCategory(self.base_ring())

        @_cached_method
        @final
        def DiscriminantGroups(self) -> Category:
            from .subcategories.constructions.discriminant_groups import (
                LatticeDiscriminantGroupsCategory,
            )

            return LatticeDiscriminantGroupsCategory(self.base_ring())

    class ParentMethods:
        @final
        def is_lattice(self) -> bool:
            return True

    class ElementMethods: ...

    HomCategory = LatticeHomCategory

    OverDedekindDomain = LazyImport(
        "category_specs.lattices.subcategories.over_dedekind",
        "_LatticesOverDedekindDomain",
    )
    OverPID = LazyImport(
        "category_specs.lattices.subcategories.over_pid", "_LatticesOverPID"
    )
    OverIntegers = LazyImport(
        "category_specs.lattices.subcategories.over_integers", "_LatticesOverIntegers"
    )
    Even = LazyImport("category_specs.lattices.subcategories.even", "_EvenLattices")
    Unimodular = LazyImport(
        "category_specs.lattices.subcategories.unimodular", "_UnimodularLattices"
    )

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts
    DualObjects = LatticeDualObjectsCategory
    DualLattices = LazyImport(
        "category_specs.lattices.subcategories.constructions.dual_lattices",
        "DualLatticesCategory",
    )
    Overlattices = LazyImport(
        "category_specs.lattices.subcategories.constructions.overlattices",
        "OverlatticesCategory",
    )
    OrthogonalDirectSums = LazyImport(
        "category_specs.lattices.subcategories.constructions.orthogonal_direct_sums",
        "OrthogonalDirectSumsCategory",
    )
    DiscriminantGroups = LazyImport(
        "category_specs.lattices.subcategories.constructions.discriminant_groups",
        "LatticeDiscriminantGroupsCategory",
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


def lattice_category(base_ring: Ring) -> LatticesCategory:
    r"""Return ``Lattices(base_ring)`` as the named lattice axiom endpoint."""
    return cast(LatticesCategory, _lattice_chain(base_ring).Lattice())


def Lattices(base_ring: Ring) -> LatticesCategory:
    r"""Return the named lattice axiom category over ``base_ring``."""
    return lattice_category(base_ring)


type LatticesObject = LatticesCategory.ParentMethods
type LatticesElement = LatticesCategory.ElementMethods
type LatticesMorphism = LatticeHomCategory.ElementMethods
type LatticesHomCategory = LatticeHomCategory
type LatticesEndCategory = LatticeEndCategory
type LatticesAutCategory = LatticeAutCategory
type LatticesHom = LatticeHomCategory.ParentMethods
type LatticesEnd = LatticeEndCategory.ParentMethods
type LatticesAut = LatticeAutCategory.ParentMethods
type LatticesEndomorphism = LatticeEndCategory.ElementMethods
type LatticesAutomorphism = LatticeAutCategory.ElementMethods
