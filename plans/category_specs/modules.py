"""Spec stub for the FGP module category used by the module redesign.

This category composes with Sage's existing ``Modules(R).FinitelyPresented()``
rather than replacing it.  It adds:

- a ``WithGenerators()`` axiom for modules with a canonical ordered generator
  tuple (distinct from ``WithBasis()``, which routes into
  ``CombinatorialFreeModule`` machinery and assumes a free structure),
- ``Free()``, ``Torsion()``, ``Ideals()``, ``Subobjects()``, and
  ``Quotients()`` subcategories, with ``SubObjects`` and
  ``QuotientObjects`` retained only as spelling aliases,
- construction methods on the category instance itself so that
  ``Modules(ZZ).free_module(n)`` etc. are the public API.

Sage's existing ``TensorProducts`` and ``CartesianProducts`` constructions are
inherited from ``Modules(R)``.  ``DualObjects`` extends Sage's dual-object
construction because these dual parents must also behave as homsets
``Hom_R(M, R)``.

The underlying implementation tracks the Smith Normal Form (SNF) diagonal
``[d_1, ..., d_k, 0, ..., 0]``.  An entry ``0`` contributes a free summand
``R``; a nonzero entry ``d_i`` contributes a torsion summand ``R/d_i``.
Construction methods auto-promote via ``_refine_category_`` when the
invariants indicate a purely free or purely torsion object.

Methods that return ideals (e.g. ``annihilator``) produce Sage
``Ideal_generic`` instances refined through the separate ring-ideal hierarchy
for the base ring and through ``Modules(R).Ideals()`` for the module-subobject
view.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator, Sequence
from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory
from sage.categories.homset import Hom, Homset
from sage.categories.modules import Modules as SageModules
from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.categories.quotients import QuotientsCategory
from sage.categories.subobjects import SubobjectsCategory
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.infinity import Infinity
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import InfinityElement, Matrix, Vector
from sage.structure.parent import Parent

from .homsets import (
    EndomorphismAlgebraCategoryObject,
    EndomorphismAlgebraElement,
    ModuleAutomorphism,
    ModuleAutomorphismGroup,
    ModuleAutomorphismSets,
    ModuleHomsets,
)

if TYPE_CHECKING:
    from .rings import ModuleBaseRingElement, ModuleBaseRingsCategoryObject

Cardinality = Integer | InfinityElement
ElementOrder = Integer | InfinityElement


class BaseChangeFunctor(ABC):
    r"""Functor that tensors an ``R``-module (or morphism) with a ring map ``R → S``."""

    @abstractmethod
    def apply_to_object(self, module: ModulesCategoryObject) -> ModulesCategoryObject:
        ...

    @abstractmethod
    def apply_to_morphism(self, morphism: ModulesMorphismObject) -> ModulesMorphismObject:
        ...


class Modules(Category_module):
    r"""
    Category of finitely presented ``R``-modules with canonical generators,
    as a subcategory of ``SageModules(R).FinitelyPresented()``.

    The category instance is the main construction interface:

    - ``Modules(R).free_module(n)`` — free module ``R^n``
    - ``Modules(R).from_elements([d_1, ..., d_k])`` — torsion module ``R/d_1 ⊕ ... ⊕ R/d_k``
    - ``Modules(R).from_presentation_matrix(A)`` — from arbitrary matrix

    Purely free or purely torsion results are auto-promoted to
    ``Modules(R).Free()`` or ``Modules(R).Torsion()`` via ``_refine_category_``.
    """

    @staticmethod
    @final
    def __classcall_private__(cls, base_ring: Ring):
        if base_ring not in PrincipalIdealDomains():
            raise TypeError(f"Modules spec requires a commutative PID; got {base_ring!r}")
        return super(Modules, cls).__classcall__(cls, base_ring)

    @final
    def super_categories(self) -> list[Category]:
        return [SageModules(self.base_ring()).FinitelyPresented()]

    @final
    def additional_structure(self):
        return None

    @final
    def _repr_object_names(self) -> str:
        return f"finitely presented modules over {self.base_ring()}"

    def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # Construction methods (called on the category instance)
    # ------------------------------------------------------------------

    @abstractmethod
    def free_module(self, n: Integer) -> FreeModuleCategoryObject:
        r"""
        Return ``R^n``.

        Constructs the SNF module with ``n`` zero diagonal entries and
        auto-promotes to ``Modules(R).Free()``.
        """
        ...

    @abstractmethod
    def from_elements(self, elements: Sequence[ModuleBaseRingElement]) -> ModulesCategoryObject:
        r"""
        Return ``R/d_1 ⊕ ... ⊕ R/d_k`` from the sequence ``[d_1, ..., d_k]``.

        Each ``d_i`` generates a torsion summand ``R/d_i`` directly.  To
        construct from SNF invariants (i.e. with automatic divisibility
        reduction), use
        ``Modules(R).from_presentation_matrix(diagonal_matrix(R, [d_1, ..., d_k]))``.
        """
        ...

    @abstractmethod
    def from_presentation_matrix(self, A: Matrix) -> ModulesCategoryObject:
        r"""
        Construct from an arbitrary presentation matrix.

        Computes the SNF of ``A`` and delegates to ``from_elements`` with the
        resulting nonzero diagonal entries.
        """
        ...

    # ------------------------------------------------------------------
    # SubcategoryMethods
    # ------------------------------------------------------------------

    class SubcategoryMethods:

        @final
        @cached_method
        # @overload category base ring
        def base_ring(self) -> ModuleBaseRingsCategoryObject:
            return self._reduction[1][0]

        @final
        @cached_method
        def Free(self) -> Modules.Free:
            return self._with_axiom("Free")

        @final
        @cached_method
        def Torsion(self) -> Modules.Torsion:
            return self._with_axiom("Torsion")

        @final
        @cached_method
        def WithGenerators(self) -> Modules.WithGenerators:
            return self._with_axiom("WithGenerators")

        @final
        @cached_method
        def Ideals(self) -> Modules.Ideals:
            return self._with_axiom("Ideals")

        @final
        @cached_method
        def Subobjects(self) -> Modules.Subobjects:
            return Modules.Subobjects.category_of(self)

        @final
        @cached_method
        def SubObjects(self) -> Modules.Subobjects:
            return self.Subobjects()

        @final
        @cached_method
        def Submodules(self) -> Modules.Subobjects:
            return self.Subobjects()

        @final
        @cached_method
        def Quotients(self) -> Modules.Quotients:
            return Modules.Quotients.category_of(self)

        @final
        @cached_method
        def QuotientObjects(self) -> Modules.Quotients:
            return self.Quotients()

        @final
        @cached_method
        def DualObjects(self) -> Modules.DualObjects:
            return Modules.DualObjects.category_of(self)

        dual_objects = DualObjects

        @final
        @cached_method
        def AutomorphismSets(self) -> Modules.AutomorphismSets:
            return Modules.AutomorphismSets.category_of(self)

        @final
        @cached_method
        def Autsets(self) -> Modules.AutomorphismSets:
            return self.AutomorphismSets()

        @final
        @cached_method
        def WithForm(self) -> Modules.WithForm:
            return self._with_axiom("WithForm")

        @abstractmethod
        def zero_module(self) -> ModulesCategoryObject: ...

        @abstractmethod
        def base_change(self, ring: ModuleBaseRingsCategoryObject) -> Modules: ...

        @abstractmethod
        def base_change_functor(self, ring: ModuleBaseRingsCategoryObject) -> BaseChangeFunctor: ...

        @abstractmethod
        def random_module(self) -> ModulesCategoryObject: ...

        @abstractmethod
        def an_object(self) -> ModulesCategoryObject: ...

    # ------------------------------------------------------------------
    # Subcategories
    # ------------------------------------------------------------------

    class WithGenerators(CategoryWithAxiom_over_base_ring):
        r"""Modules with a canonical ordered finite generator tuple."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "modules with canonical generators"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def gens(self) -> tuple[ModuleElement, ...]: ...

            @final
            def gen(self, index: int) -> ModuleElement:
                return self.gens()[index]

            @final
            def ngens(self) -> Integer:
                return Integer(len(self.gens()))

        class ElementMethods: ...
        class MorphismMethods: ...

    class Free(CategoryWithAxiom_over_base_ring):
        r"""Free ``R``-modules; SNF diagonal is all zeros."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring()).WithGenerators()]

        @final
        def _repr_object_names(self) -> str:
            return "free modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def rank(self) -> Integer: ...

            @final
            def free_rank(self) -> Integer:
                return self.rank()

            @abstractmethod
            def tensor_module(
                self, contravariant_degree: int, covariant_degree: int
            ) -> FreeModuleCategoryObject: ...

            @abstractmethod
            def tensor_algebra(self) -> Parent: ...

            @abstractmethod
            def exterior_algebra(self) -> Parent: ...

            @abstractmethod
            def symmetric_algebra(self) -> Parent: ...

            @abstractmethod
            def wedge_power(self, degree: int) -> FreeModuleCategoryObject: ...

            @abstractmethod
            def determinant_module(self) -> FreeModuleCategoryObject: ...

            @abstractmethod
            def linear_form(self, coefficients: Sequence[ModuleBaseRingElement]) -> ModulesMorphismObject:
                r"""
                Return the linear functional ``M → R`` whose value on
                generator ``g_i`` is ``coefficients[i]``.

                Concretely: given a free module ``M = R^n`` with generators
                ``e_1, ..., e_n``, returns the morphism
                ``Σ a_i e_i ↦ Σ coefficients[i] * a_i``.
                """
                ...

        class ElementMethods:
            @abstractmethod
            def __getitem__(self, index: int) -> ModuleBaseRingElement: ...

        class MorphismMethods: ...

    class Torsion(CategoryWithAxiom_over_base_ring):
        r"""Torsion ``R``-modules; SNF diagonal has no zero entries."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring()).WithGenerators()]

        @final
        def _repr_object_names(self) -> str:
            return "torsion modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def invariants(self) -> tuple[ModuleBaseRingElement, ...]:
                r"""The nonzero SNF diagonal entries ``(d_1, ..., d_k)``."""
                ...

            @abstractmethod
            def p_part(self, p: ModuleBaseRingElement) -> TorsionModuleCategoryObject: ...

            @abstractmethod
            def is_p_elementary(self, p: ModuleBaseRingElement) -> bool: ...

        class ElementMethods:
            @abstractmethod
            def order(self) -> ElementOrder: ...

        class MorphismMethods: ...

    class Ideals(CategoryWithAxiom_over_base_ring):
        r"""
        Subcategory of principal ``R``-ideals viewed as ``R``-subobjects.

        Objects are ``sage.rings.ideal.Ideal_generic`` instances whose
        categories have been refined into both ``ModuleBaseIdeals(R)`` and
        ``Modules(R).Ideals()``.

        ``ModuleBaseIdeals(R)`` supplies the ideal-side return-type overrides
        for ``Ideal_generic`` / ``Ideal_pid`` methods.  This module-facing
        category adds the fact that those ideals are subobjects of the
        ambient ``R``-module.
        """

        @final
        def super_categories(self):
            from .rings import ModuleBaseIdeals
            R = self.base_ring()
            return [Modules(R).Subobjects(), ModuleBaseIdeals(R)]

        @final
        def additional_structure(self):
            return None

        @final
        def _repr_object_names(self) -> str:
            return "principal ideal submodules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            ...

        class ElementMethods: ...
        class MorphismMethods: ...

    class Subobjects(SubobjectsCategory):
        r"""
        Subobjects of a finitely presented ``R``-module, equipped with
        a canonical inclusion morphism into an ambient module.
        """

        @final
        def super_categories(self):
            return [Modules(self.base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "subobjects of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @final
            def ambient(self) -> ModulesCategoryObject:
                return self.inclusion().codomain()

            @abstractmethod
            def inclusion(self) -> ModulesMorphismObject: ...

            @abstractmethod
            def intersect(self, other: SubmoduleCategoryObject) -> SubmoduleCategoryObject: ...

            @final
            def __and__(self, other: SubmoduleCategoryObject) -> SubmoduleCategoryObject:
                return self.intersect(other)

            @abstractmethod
            def index(self) -> Cardinality:
                r"""Cardinality of ``self.inclusion().codomain() / self``."""
                ...

        class ElementMethods: ...
        class MorphismMethods: ...

    SubObjects = Subobjects
    Submodules = Subobjects

    class Quotients(QuotientsCategory):
        r"""
        Quotient modules ``M/N``, equipped with a canonical projection
        morphism.  A quotient object is not inside an ambient module; its
        source module is ``projection().domain()``.
        """

        @final
        def super_categories(self):
            return [Modules(self.base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "quotient objects of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def projection(self) -> ModulesMorphismObject: ...

        class ElementMethods: ...
        class MorphismMethods: ...

    QuotientObjects = Quotients

    class DualObjects(DualObjectsCategory):
        r"""
        Dual objects ``M^* = Hom_R(M, R)`` in the module hierarchy.

        A dual parent is an actual Sage homset parent ``Hom_R(M, R)`` refined
        into ``Modules(R).DualObjects()``.  The homset category supplies the
        homset parent methods, and Sage's ``Homset._abstract_element_class``
        supplies the morphism-class behavior for its elements.
        """

        @final
        def extra_super_categories(self):
            base = self.base_category()
            return [base, base.Homsets()]

        @final
        def _repr_object_names(self) -> str:
            return "dual objects of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            # @override DualObjectsCategory.ParentMethods.dual_of
            @abstractmethod
            def dual_of(self) -> ModulesCategoryObject: ...

            @final
            def as_linear_dual(self) -> Homset:
                return self

            @abstractmethod
            def natural_pairing(self) -> ModulesMorphismObject: ...

            @abstractmethod
            def _repr_(self) -> str: ...

            @abstractmethod
            def _latex_(self) -> str: ...

        class ElementMethods:
            @final
            def as_linear_functional(self) -> ModulesMorphismObject:
                return self

            @final
            def evaluate(self, value: ModuleElement) -> ModuleBaseRingElement:
                return self(value)

            @abstractmethod
            def __call__(self, value: ModuleElement) -> ModuleBaseRingElement: ...

        class MorphismMethods: ...

    class AutomorphismSets(AutomorphismSetsCategory):
        r"""
        Automorphism groups of finitely presented ``R``-modules.

        ``Aut_R(M)`` is the group of units of ``End_R(M)``.  Its elements are
        represented by invertible endomorphisms and therefore carry both group
        operations and the module morphism interface.
        """

        @final
        def extra_super_categories(self):
            return [Groups()]

        @final
        def _repr_object_names(self) -> str:
            return "automorphism groups of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:

            @abstractmethod
            def module(self) -> ModulesCategoryObject: ...

            @final
            def object(self) -> ModulesCategoryObject:
                return self.module()

            @abstractmethod
            def endomorphism_algebra(self) -> EndomorphismAlgebraCategoryObject: ...

            @final
            def endomorphism_set(self) -> EndomorphismAlgebraCategoryObject:
                return self.endomorphism_algebra()

            @abstractmethod
            def inclusion(self) -> ModulesMorphismObject:
                r"""Inject ``Aut_R(M)`` into ``End_R(M)`` as the unit group."""
                ...

            @abstractmethod
            def from_endomorphism(self, value: EndomorphismAlgebraElement) -> ModuleAutomorphism:
                r"""Return the unit represented by an invertible endomorphism."""
                ...

            @abstractmethod
            def identity(self) -> ModuleAutomorphism: ...

            @final
            def one(self) -> ModuleAutomorphism:
                return self.identity()

            @abstractmethod
            def __contains__(self, value: Any) -> bool: ...

            @abstractmethod
            def _repr_(self) -> str: ...

            @abstractmethod
            def _latex_(self) -> str: ...

        class ElementMethods:

            @abstractmethod
            def parent(self) -> ModuleAutomorphismGroup: ...

            @abstractmethod
            def endomorphism(self) -> EndomorphismAlgebraElement: ...

            @abstractmethod
            def as_unit(self) -> EndomorphismAlgebraElement: ...

            # @override Modules.MorphismMethods.domain
            @abstractmethod
            def domain(self) -> ModulesCategoryObject: ...

            # @override Modules.MorphismMethods.codomain
            @final
            def codomain(self) -> ModulesCategoryObject:
                return self.domain()

            @abstractmethod
            def __call__(self, value: ModuleElement) -> ModuleElement: ...

            @abstractmethod
            def inverse(self) -> ModuleAutomorphism: ...

            @final
            def __invert__(self) -> ModuleAutomorphism:
                return self.inverse()

            @abstractmethod
            def to_matrix(self) -> Matrix: ...

            @abstractmethod
            def __mul__(self, other: ModuleAutomorphism) -> ModuleAutomorphism: ...

    # ------------------------------------------------------------------
    # ParentMethods
    # ------------------------------------------------------------------

    class ParentMethods:

        @abstractmethod
        def invariants(self) -> tuple[ModuleBaseRingElement, ...]:
            r"""
            The full SNF diagonal ``(d_1, ..., d_k, 0, ..., 0)`` for every
            module in this category, where
            nonzero ``d_i`` are torsion invariants and zeros are free ranks.
            """
            ...

        @abstractmethod
        def __iter__(self) -> Iterator[ModuleElement]: ...

        @abstractmethod
        def zero(self) -> ModuleElement: ...

        # @overload module parent base ring
        @abstractmethod
        def base_ring(self) -> ModuleBaseRingsCategoryObject: ...

        @abstractmethod
        def free_part(self) -> FreeModuleCategoryObject: ...

        @abstractmethod
        def torsion_part(self) -> TorsionModuleCategoryObject: ...

        @abstractmethod
        def dual(self) -> DualModuleCategoryObject:
            r"""
            The ``R``-dual ``Hom_R(M, R)`` as an object of
            ``Modules(R).DualObjects()``.
            """
            ...

        @abstractmethod
        def annihilator(
            self,
            value: ModuleElement | SubmoduleCategoryObject | None = None,
        ) -> IdealSubmodulesCategoryObject:
            r"""
            Annihilator ideal.

            If ``value`` is a module element, return ``{r in R | r·value = 0}``.
            If ``value`` is a subobject, return the ideal annihilating every
            element of that subobject.  If ``value`` is ``None``, return the
            annihilator of the whole module ``self``.
            """
            ...

        @abstractmethod
        def is_free(self) -> bool: ...

        @abstractmethod
        def is_torsion(self) -> bool: ...

        @final
        def is_torsionfree(self) -> bool:
            r"""Over a PID, finitely presented torsion-free modules are free."""
            return self.is_free()

        @abstractmethod
        def free_rank(self) -> Integer: ...

        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @final
        def is_finite(self) -> bool:
            return self.cardinality() != Infinity

        @abstractmethod
        def is_isomorphic_to(self, other: ModulesCategoryObject) -> bool: ...

        @final
        def Hom(self, other: ModulesCategoryObject) -> Homset:
            return Hom(self, other, category=self.category())

        @final
        def End(self) -> EndomorphismAlgebraCategoryObject:
            return self.Hom(self)

        @final
        def Aut(self) -> ModuleAutomorphismGroup:
            return self.End().unit_group()

        @abstractmethod
        def direct_sum(self, *others: ModulesCategoryObject) -> ModulesCategoryObject: ...

        @abstractmethod
        def tensor(self, *others: ModulesCategoryObject) -> ModulesCategoryObject: ...

        @abstractmethod
        def span(
            self,
            elements: Iterable[ModuleElement] | ModuleBaseRingElement,
        ) -> SubmoduleCategoryObject: ...

        @abstractmethod
        def submodule(self, generators: Iterable[ModuleElement]) -> SubmoduleCategoryObject: ...

        @abstractmethod
        def submodules(self) -> Iterable[SubmoduleCategoryObject]: ...

        @abstractmethod
        def is_submodule_of(
            self,
            other: ModulesCategoryObject,
            morphism: ModulesMorphismObject | None = None,
        ) -> bool: ...

        @abstractmethod
        def quotient(self, submodule: SubmoduleCategoryObject) -> QuotientModuleCategoryObject: ...

        @final
        def __truediv__(self, submodule: SubmoduleCategoryObject) -> QuotientModuleCategoryObject:
            return self.quotient(submodule)

        @abstractmethod
        def saturation(self) -> SubmoduleCategoryObject: ...

        @abstractmethod
        def is_primitive(self) -> bool: ...

        @final
        def __add__(self, other: ModulesCategoryObject) -> ModulesCategoryObject:
            return self.direct_sum(other)

        @abstractmethod
        def _mul_(self, other: ModuleBaseRingElement | ModulesCategoryObject) -> ModulesCategoryObject:
            r"""
            Dispatch multiplication by type.

            ``M * N`` is the tensor product of modules.  Scalar
            multiplication is only the Sage left action ``r * M`` and returns
            the subobject ``rM`` via ``_lmul_``.
            """
            ...

        @final
        def __mul__(self, other: ModuleBaseRingElement | ModulesCategoryObject) -> ModulesCategoryObject:
            return self._mul_(other)

        @abstractmethod
        def _lmul_(self, scalar: ModuleBaseRingElement) -> SubmoduleCategoryObject:
            r"""Return the submodule ``scalar · self = {scalar · m | m ∈ self}``."""
            ...

        @final
        def __rmul__(self, scalar: ModuleBaseRingElement) -> SubmoduleCategoryObject:
            return self._lmul_(scalar)

        @abstractmethod
        def __contains__(self, value: Any) -> bool: ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # ElementMethods
    # ------------------------------------------------------------------

    class ElementMethods:

        @abstractmethod
        def parent(self) -> ModulesCategoryObject: ...

        @abstractmethod
        def order(self) -> ElementOrder:
            r"""Additive order in ``ZZ`` or ``Infinity``; never a ring element."""
            ...

        @abstractmethod
        def annihilator(self) -> IdealSubmodulesCategoryObject:
            r"""Annihilator ideal ``{r ∈ R | r·self = 0}``."""
            ...

        @abstractmethod
        def to_vector(self) -> Vector:
            r"""Coordinates with respect to the ordered generator/basis tuple."""
            ...

        @abstractmethod
        def dual(self) -> DualModuleElement:
            r"""
            Return the corresponding element of ``self.parent().dual()``.
            """
            ...

        @final
        def span(self) -> SubmoduleCategoryObject:
            return self.parent().span([self])

        @abstractmethod
        def __add__(self, other: ModuleElement) -> ModuleElement: ...

        @abstractmethod
        def __neg__(self) -> ModuleElement: ...

        @abstractmethod
        def _lmul_(self, scalar: ModuleBaseRingElement) -> ModuleElement: ...

        @final
        def __rmul__(self, scalar: ModuleBaseRingElement) -> ModuleElement:
            return self._lmul_(scalar)

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # MorphismMethods
    # ------------------------------------------------------------------

    class MorphismMethods:

        # @override Morphism.domain
        @abstractmethod
        def domain(self) -> ModulesCategoryObject: ...

        # @override Morphism.codomain
        @abstractmethod
        def codomain(self) -> ModulesCategoryObject: ...

        @abstractmethod
        def __call__(self, value: ModuleElement) -> ModuleElement: ...

        @abstractmethod
        def to_matrix(self) -> Matrix: ...

        @final
        def to_tuple_of_images(self) -> tuple[ModuleElement, ...]:
            return tuple(self(g) for g in self.domain().gens())

        @final
        def to_list_of_images(self) -> list[ModuleElement]:
            return list(self.to_tuple_of_images())

        @final
        def to_dict(self) -> dict[ModuleElement, ModuleElement]:
            return dict(zip(self.domain().gens(), self.to_tuple_of_images(), strict=True))

        @abstractmethod
        def image(self) -> SubmoduleCategoryObject: ...

        @abstractmethod
        def kernel(self) -> SubmoduleCategoryObject: ...

        @abstractmethod
        def cokernel(self) -> QuotientModuleCategoryObject: ...

        @abstractmethod
        def index(self) -> Cardinality:
            r"""Cardinality of ``self.codomain() / self.image()``."""
            ...

        @abstractmethod
        def lift(self, value: ModuleElement) -> ModuleElement: ...

        @abstractmethod
        def lift_generators(self) -> tuple[ModuleElement, ...]:
            r"""
            Lift the generators of ``codomain`` to elements of ``domain``
            along this morphism.
            """
            ...

        @abstractmethod
        def saturation(self) -> SubmoduleCategoryObject: ...

        @abstractmethod
        def invariant_submodule(self) -> SubmoduleCategoryObject:
            r"""
            Subobject of ``domain`` fixed by this endomorphism.

            Undefined unless ``self.is_endomorphism()``.
            """
            ...

        @abstractmethod
        def coinvariant_submodule(self) -> QuotientModuleCategoryObject:
            r"""
            Quotient of ``domain`` by the image of ``(id - self)``.

            Undefined unless ``self.is_endomorphism()``.
            """
            ...

        @abstractmethod
        def is_injective(self) -> bool: ...

        @abstractmethod
        def is_surjective(self) -> bool: ...

        @final
        def is_bijective(self) -> bool:
            return self.is_injective() and self.is_surjective()

        @abstractmethod
        def is_endomorphism(self) -> bool: ...

        @abstractmethod
        def is_isomorphism(self) -> bool: ...

        @abstractmethod
        def is_identity(self) -> bool:
            r"""Whether this endomorphism is the identity on its domain."""
            ...

        @abstractmethod
        def is_primitive(self) -> bool: ...

        @abstractmethod
        def direct_sum(self, other: ModulesMorphismObject) -> ModulesMorphismObject: ...

        @abstractmethod
        def tensor(self, other: ModulesMorphismObject) -> ModulesMorphismObject: ...

        @abstractmethod
        def base_change(
            self, ring: ModuleBaseRingsCategoryObject
        ) -> ModulesMorphismObject: ...

        @abstractmethod
        def __mul__(self, other: ModulesMorphismObject) -> ModulesMorphismObject: ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # Homsets
    # ------------------------------------------------------------------

    class Homsets(HomsetsCategory):

        @final
        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]

        # @overload homset category base ring
        @final
        def base_ring(self) -> ModuleBaseRingsCategoryObject:
            return self.base_category().base_ring()

        @final
        def _repr_object_names(self) -> str:
            return "homsets of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:

            # @override Homset.domain
            @abstractmethod
            def domain(self) -> ModulesCategoryObject: ...

            # @override Homset.codomain
            @abstractmethod
            def codomain(self) -> ModulesCategoryObject: ...

            # @overload homset parent base ring
            @final
            @cached_method
            def base_ring(self) -> ModuleBaseRingsCategoryObject:
                return self.domain().base_ring()

            @abstractmethod
            def from_dict(
                self, mapping: Mapping[ModuleElement, ModuleElement]
            ) -> ModulesMorphismObject: ...

            @abstractmethod
            def from_images(
                self, images: Sequence[ModuleElement]
            ) -> ModulesMorphismObject: ...

            @final
            def from_tuple_of_images(
                self, images: tuple[ModuleElement, ...]
            ) -> ModulesMorphismObject:
                return self.from_images(images)

            @abstractmethod
            def from_matrix(self, matrix_data: Matrix) -> ModulesMorphismObject: ...

            @abstractmethod
            def natural_map(self) -> ModulesMorphismObject: ...

            @abstractmethod
            def __call__(self, data: Any) -> ModulesMorphismObject: ...

            @abstractmethod
            def __contains__(self, value: Any) -> bool: ...

            @abstractmethod
            def _repr_(self) -> str: ...

            @abstractmethod
            def _latex_(self) -> str: ...

        class ElementMethods: ...
        class MorphismMethods: ...

        class Endset(CategoryWithAxiom_over_base_ring):
            r"""
            Endomorphism algebras ``End_R(M)``.

            Sage's category join turns
            ``Modules(R).Homsets().Endset()`` into ``Algebras(R)``: homsets
            supply the ``R``-module structure, generic endsets supply the
            unital associative composition monoid, and ``MagmaticAlgebras(R)``
            supplies bilinearity of multiplication.
            """

            @final
            def extra_super_categories(self):
                return [MagmaticAlgebras(self.base_category().base_ring())]

            @final
            def _repr_object_names(self) -> str:
                return "endomorphism algebras of modules"

            def _latex_(self) -> str: ...

            class ParentMethods:

                @final
                def module(self) -> ModulesCategoryObject:
                    return self.domain()

                @abstractmethod
                def identity(self) -> ModulesMorphismObject: ...

                @final
                def id(self) -> ModulesMorphismObject:
                    return self.identity()

                @final
                def one(self) -> ModulesMorphismObject:
                    return self.identity()

                @abstractmethod
                def zero(self) -> ModulesMorphismObject: ...

                @abstractmethod
                def matrix_algebra_quotient(self) -> Parent:
                    r"""
                    Present ``End_R(M)`` as a quotient of a matrix algebra.

                    For SNF invariants ``(d_1, ..., d_t, 0, ..., 0)``, the
                    presentation records the block equations forcing maps to
                    descend to ``M`` and the reductions modulo torsion
                    invariants.  If ``M`` is free of rank ``n``, this is the
                    literal matrix algebra ``Mat_n(R)``.
                    """
                    ...

                @abstractmethod
                def from_matrix(self, matrix_data: Matrix) -> EndomorphismAlgebraElement: ...

                @abstractmethod
                def Aut(self) -> ModuleAutomorphismGroup: ...

                @final
                def unit_group(self) -> ModuleAutomorphismGroup:
                    return self.Aut()

            class ElementMethods:

                @abstractmethod
                def parent(self) -> EndomorphismAlgebraCategoryObject: ...

                @abstractmethod
                def is_unit(self) -> bool:
                    r"""Whether this endomorphism is an automorphism of its module."""
                    ...

                @abstractmethod
                def inverse(self) -> EndomorphismAlgebraElement:
                    r"""Inverse in ``End_R(M)``; defined exactly for units."""
                    ...

                @final
                def __invert__(self) -> EndomorphismAlgebraElement:
                    return self.inverse()

                @abstractmethod
                def as_automorphism(self) -> ModuleAutomorphism:
                    r"""Return this unit as an element of ``Aut_R(M)``."""
                    ...

            class MorphismMethods: ...

    WithForm = LazyImport('category_specs.modules_with_forms', 'ModulesWithForms')


# Type aliases: use XCategoryObject in annotations instead of X.ParentMethods.
ModulesCategoryObject = Modules.ParentMethods
ModuleElement = Modules.ElementMethods
ModulesMorphismObject = Modules.MorphismMethods
ModuleMorphism = ModulesMorphismObject
FreeModuleCategoryObject = Modules.Free.ParentMethods
TorsionModuleCategoryObject = Modules.Torsion.ParentMethods
IdealSubmodulesCategoryObject = Modules.Ideals.ParentMethods
SubmoduleCategoryObject = Modules.Subobjects.ParentMethods
QuotientModuleCategoryObject = Modules.Quotients.ParentMethods
DualModuleCategoryObject = Modules.DualObjects.ParentMethods
DualModuleElement = Modules.DualObjects.ElementMethods
AutomorphismGroupCategoryObject = Modules.AutomorphismSets.ParentMethods
AutomorphismGroupElement = Modules.AutomorphismSets.ElementMethods
EndomorphismAlgebraCategoryObject = Modules.Homsets.Endset.ParentMethods
EndomorphismAlgebraElement = Modules.Homsets.Endset.ElementMethods
