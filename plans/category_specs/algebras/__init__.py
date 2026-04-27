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
    |-- CartesianProducts()
    |-- TensorProducts()
    `-- DualObjects()
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any, final

from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..modules import Modules
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.tensor_products import _TensorProducts

if TYPE_CHECKING:
    from ..types import (
        Algebra,
        AlgebraElement,
        AlgebraElementFamily,
        AlgebraMorphism,
        HochschildChainComplex,
        RModule,
        Ring,
    )


class _AlgebraParentMethods:
    @abstract_method
    def base_ring(self) -> Ring: ...

    @abstract_method
    def change_ring(self, R: Ring) -> Algebra: ...

    @abstract_method
    def algebra_generators(self) -> AlgebraElementFamily: ...

    @abstract_method
    def center(self) -> Algebra: ...

    @abstract_method
    def center_basis(self) -> Sequence[AlgebraElement]: ...

    @abstract_method
    def radical(self) -> Algebra: ...

    @abstract_method
    def radical_basis(self) -> Sequence[AlgebraElement]: ...

    @abstract_method
    def subalgebra(
        self,
        generators: Iterable[AlgebraElement],
        category: Category | None = None,
    ) -> Algebra: ...

    @abstract_method
    def derivations_basis(self) -> Sequence[AlgebraMorphism]: ...

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


class _AlgebraMorphismMethods:
    r"""Methods on algebra morphisms."""


class Algebras(Category_over_base_ring):
    r"""Category of algebras over a fixed base ring."""

    def __contains__(self, A: Any) -> bool:
        match A:
            case _ if isinstance(A, Category) and A.is_subcategory(self):
                return True
            case _ if A in SageAlgebras(self.base_ring()):
                return True
            case _:
                return False

    def _repr_object_names(self) -> str:
        return f"algebras over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        from ..rings import Rings

        R = self.base_ring()
        return [
            Rings().RingsUnder(R),
            Modules(R).Constructors().RingObjectsAsModules(),
        ]

    ParentMethods = _AlgebraParentMethods
    ElementMethods = _AlgebraElementMethods
    MorphismMethods = _AlgebraMorphismMethods

    class SubcategoryMethods:
        @cached_method
        def Commutative(self):
            return self._with_axiom("Commutative")

        @cached_method
        def WithBasis(self):
            return self._with_axiom("WithBasis")

        @cached_method
        def FiniteDimensional(self):
            return self._with_axiom("FiniteDimensional")

        @cached_method
        def Semisimple(self):
            return self._with_axiom("Semisimple")

        @cached_method
        def Subobjects(self):
            return _Subobjects.category_of(self)

        @cached_method
        def Quotients(self):
            return _Quotients.category_of(self)

        @cached_method
        def CartesianProducts(self):
            return _CartesianProducts.category_of(self)

        @cached_method
        def TensorProducts(self):
            return _TensorProducts.category_of(self)

        @cached_method
        def DualObjects(self):
            return _DualObjects.category_of(self)

    class Constructors:
        r"""Algebra constructors over a fixed base ring.

        Concrete constructor methods are admitted after the corresponding Sage
        surfaces are inventoried in ``docs/SAGE_INVENTORY.md``.
        """

        def __init__(self, category):
            self._category = category

        def category(self):
            return self._category

        def base_ring(self):
            return self.category().base_ring()

    _Constructors = Constructors

    @cached_method
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
    CartesianProducts = _CartesianProducts
    TensorProducts = _TensorProducts
    DualObjects = _DualObjects
