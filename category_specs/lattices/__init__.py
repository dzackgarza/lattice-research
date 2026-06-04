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

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Literal, TypeVar, cast, final, overload

from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..forms.chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
)
from ..modules import Modules
from ..utils import refine_category, with_axiom
from .homsets import (
    LatticeAutCategory,
    LatticeEndCategory,
    LatticeHomCategory,
    _LatticeMorphisms,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import LatticeDualObjectsCategory
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
    from ..types import (
        DiscriminantGroupElement,
        Integer,
        Lattice,
        LatticeMorphism,
        Matrix,
        Ring,
        RingElement,
        RModuleElement,
    )

type LatticeBasisData = (
    Matrix | Sequence[RModuleElement] | Sequence[Sequence[RingElement]]
)
type CartanTypeData = str | Sequence[str | Integer | int]
type LatticeWithEmbeddings = tuple[Lattice, Sequence[LatticeMorphism]]


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
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for lattice constructors."""
            from category_specs.spec_core import constructor_registry_for_category

            return constructor_registry_for_category(
                self.category(),
                owner_category=f"Lattices({self.base_ring()})",
                id_prefix="lattices",
            )

        @final
        def category(self) -> LatticesCategory:
            return self._category

        @final
        def base_ring(self) -> Ring:
            base_ring: Ring = self.category().base_ring()
            return base_ring

        @final
        def _assert_integral_constructor_base_ring(self) -> None:
            from sage.rings.integer_ring import ZZ

            assert self.base_ring() == ZZ

        @final
        def _refine_constructed_lattice(self, lattice: Lattice) -> Lattice:
            return refine_category(lattice, self.category(), test=False)

        @overload
        def IntegralLattice(
            self, *, gram_matrix: Matrix, basis: LatticeBasisData | None = None
        ) -> Lattice: ...

        @overload
        def IntegralLattice(
            self, *, rank: Integer | int, basis: LatticeBasisData | None = None
        ) -> Lattice: ...

        @overload
        def IntegralLattice(
            self, *, cartan_type: CartanTypeData, basis: LatticeBasisData | None = None
        ) -> Lattice: ...

        @overload
        def IntegralLattice(
            self,
            *,
            hyperbolic_plane: Literal["U", "H"],
            basis: LatticeBasisData | None = None,
        ) -> Lattice: ...

        @final
        def IntegralLattice(
            self,
            *,
            gram_matrix: Matrix | None = None,
            rank: Integer | int | None = None,
            cartan_type: CartanTypeData | None = None,
            hyperbolic_plane: Literal["U", "H"] | None = None,
            basis: LatticeBasisData | None = None,
        ) -> Lattice:
            r"""Construct a Sage integral lattice and refine it into this category."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLattice,
            )

            self._assert_integral_constructor_base_ring()
            data = [
                gram_matrix,
                rank,
                cartan_type,
                hyperbolic_plane,
            ]
            supplied = [datum for datum in data if datum is not None]
            assert len(supplied) == 1
            return self._refine_constructed_lattice(
                IntegralLattice(supplied[0], basis=basis)
            )

        @overload
        def IntegralLatticeDirectSum(
            self,
            *,
            lattices: Sequence[Lattice],
            return_embeddings: Literal[False] = False,
        ) -> Lattice: ...

        @overload
        def IntegralLatticeDirectSum(
            self,
            *,
            lattices: Sequence[Lattice],
            return_embeddings: Literal[True],
        ) -> LatticeWithEmbeddings: ...

        @final
        def IntegralLatticeDirectSum(
            self,
            *,
            lattices: Sequence[Lattice],
            return_embeddings: bool = False,
        ) -> Lattice | LatticeWithEmbeddings:
            r"""Construct the orthogonal direct sum of integral lattices."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLatticeDirectSum,
            )

            self._assert_integral_constructor_base_ring()
            result = IntegralLatticeDirectSum(
                list(lattices), return_embeddings=return_embeddings
            )
            if return_embeddings:
                lattice, embeddings = result
                return (self._refine_constructed_lattice(lattice), tuple(embeddings))
            return self._refine_constructed_lattice(result)

        @overload
        def IntegralLatticeGluing(
            self,
            *,
            lattices: Sequence[Lattice],
            glue: Sequence[Sequence[DiscriminantGroupElement]],
            return_embeddings: Literal[False] = False,
        ) -> Lattice: ...

        @overload
        def IntegralLatticeGluing(
            self,
            *,
            lattices: Sequence[Lattice],
            glue: Sequence[Sequence[DiscriminantGroupElement]],
            return_embeddings: Literal[True],
        ) -> LatticeWithEmbeddings: ...

        @final
        def IntegralLatticeGluing(
            self,
            *,
            lattices: Sequence[Lattice],
            glue: Sequence[Sequence[DiscriminantGroupElement]],
            return_embeddings: bool = False,
        ) -> Lattice | LatticeWithEmbeddings:
            r"""Construct the glued overlattice from discriminant-group glue data."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLatticeGluing,
            )

            self._assert_integral_constructor_base_ring()
            result = IntegralLatticeGluing(
                list(lattices), [list(row) for row in glue], return_embeddings
            )
            if return_embeddings:
                lattice, embeddings = result
                return (self._refine_constructed_lattice(lattice), tuple(embeddings))
            return self._refine_constructed_lattice(result)
    @final
    def Constructors(self) -> LatticesCategory._Constructors:
        r"""Return the lattice constructor collector over ``self.base_ring()``."""
        return self.__class__._Constructors(self)

    class SubcategoryMethods:
        @final
        def OverDedekindDomain(self) -> Category:
            return with_axiom(self, "OverDedekindDomain")
        @final
        def OverPID(self) -> Category:
            return self.OverDedekindDomain().OverPID()
        @final
        def OverIntegers(self) -> Category:
            return self.OverPID().OverIntegers()
        @final
        def Even(self) -> Category:
            return with_axiom(self, "Even")
        @final
        def Unimodular(self) -> Category:
            return with_axiom(self, "Unimodular")
        @final
        def DualObjects(self) -> Category:
            return cast(Category, LatticeDualObjectsCategory.category_of(self))
        @final
        def DualLattices(self) -> Category:
            r"""Return the metric-dual lattice construction category."""
            from .subcategories.constructions.dual_lattices import DualLatticesCategory

            return DualLatticesCategory(self.base_ring())
        @final
        def Overlattices(self) -> Category:
            from .subcategories.constructions.overlattices import OverlatticesCategory

            return OverlatticesCategory(self.base_ring())
        @final
        def OrthogonalDirectSums(self) -> Category:
            from .subcategories.constructions.orthogonal_direct_sums import (
                OrthogonalDirectSumsCategory,
            )

            return OrthogonalDirectSumsCategory(self.base_ring())
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
    DualLatticesCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.dual_lattices",
        "DualLatticesCategory",
    )
    OverlatticesCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.overlattices",
        "OverlatticesCategory",
    )
    OrthogonalDirectSumsCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.orthogonal_direct_sums",
        "OrthogonalDirectSumsCategory",
    )
    DiscriminantGroupsCategoryClass = LazyImport(
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
LatticesHomCategory = LatticeHomCategory
LatticesEndCategory = LatticeEndCategory
LatticesAutCategory = LatticeAutCategory
LatticesHom = LatticeHomCategory.ParentMethods
LatticesEnd = LatticeEndCategory.ParentMethods
LatticesAut = LatticeAutCategory.ParentMethods
LatticesEndomorphism = LatticeEndCategory.ElementMethods
LatticesAutomorphism = LatticeAutCategory.ElementMethods
