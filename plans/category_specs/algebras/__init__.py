"""Static algebra category surface for the category spec redesign.

Subcategory hierarchy::

    Algebras(R)
    |-- Commutative()
    |-- WithBasis()
    |   `-- FiniteDimensional()
    |-- FiniteDimensional()
    |-- Semisimple()
    |-- Subobjects()
    |-- Quotients()
    |-- Subquotients()
    |-- ObjectsOver()
    |-- ObjectsUnder()
    |-- Ideals(A)
    |-- CartesianProducts()
    |-- TensorProducts()
    |-- DualObjects()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any, final

from sage.categories.algebras import Algebras as SageAlgebras
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Cat, Category, Category_module
from ..modules import Modules
from ..utils import refine_category
from .homsets import AlgebraAutCategory, AlgebraEndCategory, AlgebraHomCategory
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.ideals import _Ideals
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients
from .subcategories.constructions.tensor_products import _TensorProducts

if TYPE_CHECKING:
    from ..types import (
        AdditiveGroup,
        AdditiveMonoid,
        AdditiveSemigroup,
        Algebra,
        AlgebraElement,
        AlgebraIdeal,
        Group,
        HochschildChainComplex,
        Magma,
        Monoid,
        RAlgebra,
        Ring,
        Semigroup,
        Set,
        Tensor,
        RModule,
        SetFamily,
    )


class _AlgebraParentMethods:
    @abstract_method
    def base_ring(self) -> Ring: ...

    @abstract_method
    def change_ring(self, R: Ring) -> Algebra: ...

    @abstract_method
    def algebra_generators(self) -> SetFamily: ...

    @abstract_method
    def center(self) -> Algebra: ...

    @abstract_method
    def radical(self) -> AlgebraIdeal: ...

    @abstract_method
    def subalgebra(
        self,
        generators: Iterable[AlgebraElement],
        category: Category | None = None,
    ) -> Algebra: ...

    @abstract_method
    def derivations(self) -> RModule: ...

    @abstract_method
    def annihilator(self, elements: Iterable[AlgebraElement]) -> AlgebraIdeal: ...

    @final
    def ideals(self) -> Category:
        return self.category().Ideals(self)

    @abstract_method
    def hochschild_complex(self, coefficients: RModule) -> HochschildChainComplex: ...

    @abstract_method
    def has_standard_involution(self) -> bool: ...

    @abstract_method
    def idempotent_lift(self, x: AlgebraElement) -> AlgebraElement: ...

    @abstract_method
    def peirce_decomposition(
        self,
        idempotents: Sequence[AlgebraElement] | None = None,
        check: bool = True,
    ) -> Sequence[Sequence[Algebra]]: ...

    @abstract_method
    def semisimple_quotient(self) -> Algebra: ...


class _AlgebraElementMethods:
    r"""Methods on elements of algebras."""

    @abstract_method
    def __mul__(self, other: AlgebraElement) -> AlgebraElement: ...


class _AlgebraMorphismMethods:
    r"""Methods on algebra morphisms."""


class Algebras(Category_module):
    r"""Category of algebras over a fixed base ring."""

    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageAlgebras(self.base_ring()),)

    @final
    def _repr_object_names(self) -> str:
        return f"algebras over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        from ..rings import Rings

        R = self.base_ring()
        return [
            Rings().RingsUnder(R),
            Modules(R),
            SageAlgebras(R),
        ]

    ParentMethods = _AlgebraParentMethods
    ElementMethods = _AlgebraElementMethods
    MorphismMethods = _AlgebraMorphismMethods
    HomCategory = AlgebraHomCategory

    class SubcategoryMethods:
        @cached_method
        @final
        def Commutative(self) -> Category:
            return self._with_axiom("Commutative")

        @cached_method
        @final
        def WithBasis(self) -> Category:
            return self._with_axiom("WithBasis")

        @cached_method
        @final
        def FiniteDimensional(self) -> Category:
            return self._with_axiom("FiniteDimensional")

        @cached_method
        @final
        def Semisimple(self) -> Category:
            return self._with_axiom("Semisimple")

        @cached_method
        @final
        def TensorProducts(self) -> Category:
            return _TensorProducts.category_of(self)

        @cached_method
        @final
        def DualObjects(self) -> Category:
            return _DualObjects.category_of(self)

        @final
        def Ideals(self, algebra: Algebra) -> Category:
            assert algebra in self, f"Ideals expects an algebra in {self}: {algebra}"
            return _Ideals(algebra)

    class Constructors:
        r"""Algebra constructors over a fixed base ring.

        These constructors name the free functors from specific source
        categories into the corresponding category of ``R``-algebra objects.
        Sage's generic ``S.algebra(R)`` compatibility method is not the public
        project API.
        """

        def __init__(self, category: RAlgebra) -> None:
            self._category = category

        @final
        def category(self) -> RAlgebra:
            return self._category

        @final
        def base_ring(self) -> Ring:
            return self.category().base_ring()

        @final
        def _refine_constructed_algebra(self, algebra: Algebra, categories: Sequence[Category]) -> Algebra:
            return refine_category(algebra, [self.category(), *categories])

        @final
        def free_algebra_from_set(self, generators: Set) -> Algebra:
            r"""Return the free associative unital ``R``-algebra on ``generators``."""
            from sage.algebras.free_algebra import FreeAlgebra

            assert generators.is_finite(), "free_algebra_from_set currently requires a finite generator set"
            algebra = FreeAlgebra(self.base_ring(), generators.cardinality(), "x")
            return self._refine_constructed_algebra(algebra, [self.category().WithBasis()])

        @abstract_method
        def free_algebra_from_magma(self, magma: Magma) -> Algebra:
            r"""Return the free ``R``-algebra object generated by ``magma``."""
            ...

        @abstract_method
        def free_algebra_from_semigroup(self, semigroup: Semigroup) -> Algebra:
            r"""Return the free ``R``-algebra object generated by ``semigroup``."""
            ...

        @abstract_method
        def free_algebra_from_monoid(self, monoid: Monoid) -> Algebra:
            r"""Return the monoid algebra over ``R``."""
            ...

        @abstract_method
        def free_algebra_from_group(self, group: Group) -> Algebra:
            r"""Return the group algebra over ``R``."""
            ...

        @abstract_method
        def free_algebra_from_additive_semigroup(self, semigroup: AdditiveSemigroup) -> Algebra:
            r"""Return the ``R``-algebra induced by the additive semigroup law."""
            ...

        @abstract_method
        def free_algebra_from_additive_monoid(self, monoid: AdditiveMonoid) -> Algebra:
            r"""Return the ``R``-algebra induced by the additive monoid law."""
            ...

        @abstract_method
        def free_algebra_from_additive_group(self, group: AdditiveGroup) -> Algebra:
            r"""Return the ``R``-algebra induced by the additive group law."""
            ...

        @abstract_method
        def from_multiplication_tensor(self, multiplication: Tensor) -> Algebra:
            r"""Return the algebra whose product is encoded by ``multiplication``.

            The tensor must lie in ``T_R(M)[1, 2]``. Its parent determines the
            underlying module ``M``, the base ring ``R``, and the preferred
            generating set used for coordinates; no separate basis, table, list
            of matrices, module-element matrix, or right-multiplication data
            belongs in this constructor surface.
            """
            ...

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        return self.__class__._Constructors(self)

    Commutative = LazyImport("category_specs.algebras.subcategories.commutative", "_CommutativeAlgebras")
    WithBasis = LazyImport("category_specs.algebras.subcategories.with_basis", "_AlgebrasWithBasis")
    FiniteDimensional = LazyImport(
        "category_specs.algebras.subcategories.finite_dimensional",
        "_FiniteDimensionalAlgebras",
    )
    Semisimple = LazyImport("category_specs.algebras.subcategories.semisimple", "_SemisimpleAlgebras")

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    Ideals = _Ideals
    CartesianProducts = _CartesianProducts
    TensorProducts = _TensorProducts
    DualObjects = _DualObjects


AlgebrasCategory = Algebras
AlgebrasObject = Algebras.ParentMethods
AlgebrasElement = Algebras.ElementMethods
AlgebrasMorphism = Algebras.MorphismMethods
AlgebrasHomCategory = AlgebraHomCategory
AlgebrasEndCategory = AlgebraEndCategory
AlgebrasAutCategory = AlgebraAutCategory
AlgebrasHom = AlgebraHomCategory.ParentMethods
AlgebrasEnd = AlgebraEndCategory.ParentMethods
AlgebrasAut = AlgebraAutCategory.ParentMethods
AlgebrasEndomorphism = AlgebraEndCategory.ElementMethods
AlgebrasAutomorphism = AlgebraAutCategory.ElementMethods
