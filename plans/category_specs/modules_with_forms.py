"""Spec stub for ``Modules(R).WithForm()`` a.k.a. ``ModulesWithForms(R)``."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import final

from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.morphism import Morphism
from sage.categories.tensor import TensorProductsCategory
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.modules.module import Module
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import Element, Matrix
from sage.structure.parent import Parent

from .homsets import ModulesWithFormsHomsets
from .modules import Modules


class ModuleForm(ABC):
    r"""
    Abstract base class for tensor-degree semilinear data on an ``R``-module.

    The datum attached to a pair ``(L, f)`` is a map with domain some graded
    piece or quotient of the tensor algebra of ``L`` and codomain an
    ``R``-module ``S``. The current workflow specializes this general layer to
    symmetric bilinear forms and quadratic forms.
    """

    @abstractmethod
    def base_ring(self) -> Ring:
        ...

    @abstractmethod
    def ambient_module(self) -> Parent:
        ...

    @abstractmethod
    def domain(self) -> Parent:
        ...

    @abstractmethod
    def codomain(self) -> Parent:
        ...

    @abstractmethod
    def tensor_degree(self) -> Integer:
        ...

    @abstractmethod
    def scalar_action_endomorphism(self) -> Morphism:
        ...

    @abstractmethod
    def gram_matrix(self) -> Matrix:
        ...

    @abstractmethod
    def evaluate(self, value: Element) -> Element:
        ...

    @abstractmethod
    def _repr_(self) -> str:
        ...

    @abstractmethod
    def _latex_(self) -> str:
        ...


class BilinearForm(ModuleForm, Morphism, ABC):
    r"""
    Abstract base class for symmetric bilinear data of degree ``2``.

    Concretely, this is the bilinear branch of the pair category, with actual
    source a degree-two tensor construction on ``L`` such as ``L \otimes_R L``
    or ``Sym^2_R(L)`` and scalar action twisted by ``id_R``.
    """

    @final
    def tensor_degree(self) -> Integer:
        return Integer(2)

    @abstractmethod
    def evaluate(self, value: Element, right: Element | None = None) -> Element:
        ...

    @abstractmethod
    def associated_quadratic_form(self) -> QuadraticForm:
        ...


class QuadraticForm(ModuleForm):
    r"""
    Abstract base class for quadratic data of degree ``1``.

    These maps are semilinear rather than linear: ``q(r * v) = sigma(r) q(v)``
    for a chosen endomorphism ``sigma`` of the base ring. In the current
    lattice workflow, ``sigma(r) = r^2``.
    """

    @final
    def tensor_degree(self) -> Integer:
        return Integer(1)

    @abstractmethod
    def associated_bilinear_form(self) -> BilinearForm:
        ...


class ModulesWithForms(CategoryWithAxiom_over_base_ring):
    r"""
    Category of pairs ``(L, f)`` with ``L`` a finitely presented ``R``-module
    and ``f`` semilinear tensor-degree data with values in an ``R``-module.

    Accessible as ``Modules(R).WithForm()``.
    """

    Homsets = LazyImport("category_specs.homsets", "ModulesWithFormsHomsets")
    DualObjects = LazyImport("category_specs.dual_objects", "ModulesWithFormsDualObjects")
    BilinearForms = LazyImport("category_specs.bilinear_form", "BilinearForms")

    # @override CategoryWithAxiom_over_base_ring.super_categories
    @final
    def super_categories(self) -> list[Category]:
        return [Modules(self.base_ring())]

    # @override CategoryWithAxiom_over_base_ring.additional_structure
    @final
    def additional_structure(self):
        return self

    # @override CategoryWithAxiom_over_base_ring._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return f"modules with forms over {self.base_ring()}"

    # @override CategoryWithAxiom_over_base_ring._latex_
    def _latex_(self) -> str:
        ...

    class SubcategoryMethods:
        @final
        @cached_method
        def base_ring(self) -> Ring:
            for category in self.super_categories():
                if hasattr(category, "base_ring"):
                    return category.base_ring()
            assert False, (
                f"some super category of {self} should be a category over a base ring"
            )

        @final
        @cached_method
        def Bilinear(self) -> Category:
            return self._with_axiom("Bilinear")

        @final
        @cached_method
        def Quadratic(self) -> Category:
            return self._with_axiom("Quadratic")

        @final
        @cached_method
        def Free(self) -> Category:
            return self._with_axiom("Free")

        @final
        @cached_method
        def Torsion(self) -> Category:
            return self._with_axiom("Torsion")

        @final
        @cached_method
        def NonDegenerate(self) -> Category:
            return self._with_axiom("NonDegenerate")

        @final
        @cached_method
        def Integral(self) -> Category:
            return self._with_axiom("Integral")

        @final
        @cached_method
        def Rational(self) -> Category:
            return self._with_axiom("Rational")

        @final
        @cached_method
        def DualObjects(self) -> Category:
            return ModulesWithForms.DualObjects.category_of(self)

        dual = DualObjects

        @final
        @cached_method
        def TensorProducts(self) -> Category:
            return ModulesWithForms.TensorProducts.category_of(self)

        @final
        @cached_method
        def CartesianProducts(self) -> Category:
            return ModulesWithForms.CartesianProducts.category_of(self)

        @final
        @cached_method
        def BilinearForms(self) -> Category:
            return ModulesWithForms.BilinearForms(self.base_ring())

        @abstractmethod
        def zero_module(self) -> Parent:
            ...

        @final
        def base_change(self, ring: Ring) -> ModulesWithForms | CategoryWithAxiom_over_base_ring:
            category = ModulesWithForms(ring)
            for axiom in self.axioms():
                category = category._with_axiom(axiom)
            return category

    class TensorProducts(TensorProductsCategory):
        # @override TensorProductsCategory.extra_super_categories
        @final
        def extra_super_categories(self):
            return [self.base_category()]

        # @override TensorProductsCategory._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "tensor products of modules with forms"

        # @override TensorProductsCategory._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def tensor_factors(self) -> tuple[Parent, ...]:
                ...

            @abstractmethod
            def _repr_(self) -> str:
                ...

            @abstractmethod
            def _latex_(self) -> str:
                ...

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class CartesianProducts(CartesianProductsCategory):
        # @override CartesianProductsCategory.extra_super_categories
        @final
        def extra_super_categories(self):
            return [self.base_category()]

        # @override CartesianProductsCategory._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "cartesian products of modules with forms"

        # @override CartesianProductsCategory._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def summands(self) -> tuple[Parent, ...]:
                ...

            @abstractmethod
            def _repr_(self) -> str:
                ...

            @abstractmethod
            def _latex_(self) -> str:
                ...

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class Torsion(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "torsion modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            ...

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class Free(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "free modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            ...

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class NonDegenerate(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "nondegenerate modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def signature_pair(self) -> tuple[Integer, Integer]:
                ...

            @abstractmethod
            def determinant(self) -> Element:
                ...

            @abstractmethod
            def discriminant(self) -> Element:
                ...

            @abstractmethod
            def rational_span(self) -> Parent:
                ...

            @abstractmethod
            def is_isometric_to(
                self,
                other: Parent,
                witness: bool = False,
            ) -> bool | tuple[bool, Morphism]:
                ...

            @abstractmethod
            def is_rationally_isometric_to(self, other: Parent) -> bool:
                ...

            @abstractmethod
            def is_locally_isometric_to(self, other: Parent, p: Element) -> bool:
                ...

            @abstractmethod
            def orthogonal_group(self) -> Parent:
                ...

            @final
            def O(self) -> Parent:
                return self.orthogonal_group()

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class Integral(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "integral modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def is_even(self) -> bool:
                ...

            @final
            def is_odd(self) -> bool:
                return not self.is_even()

            @abstractmethod
            def is_unimodular(self) -> bool:
                ...

            @abstractmethod
            def nikulin_invariants(self) -> tuple[Integer, ...]:
                ...

            @abstractmethod
            def discriminant_group(self) -> Parent:
                ...

            @abstractmethod
            def to_quadratic_module(self) -> Parent:
                ...

        class ElementMethods(ABC):
            @abstractmethod
            def is_root(self) -> bool:
                ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class Rational(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "rational modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def orthogonal_complement_of(self, submodule: Parent) -> Parent:
                ...

        class ElementMethods(ABC):
            @abstractmethod
            def is_integral(self) -> bool:
                ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class Bilinear(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "bilinear modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def form(self) -> BilinearForm:
                ...

            @abstractmethod
            def associated_quadratic_module(self) -> Parent:
                ...

            @final
            def b(self, left: Element, right: Element) -> Element:
                return self.form().evaluate(left, right)

            @final
            def q(self, value: Element) -> Element:
                return self.associated_quadratic_module().form().evaluate(value)

            @abstractmethod
            def is_positive_definite(self) -> bool:
                ...

            @abstractmethod
            def is_negative_definite(self) -> bool:
                ...

            @final
            def is_definite(self) -> bool:
                return self.is_positive_definite() or self.is_negative_definite()

            @final
            def is_indefinite(self) -> bool:
                return not self.is_definite()

        class ElementMethods(ABC):
            @final
            def norm(self) -> Element:
                return self.q()

            @final
            def is_isotropic(self) -> bool:
                return self.q() == 0

            @abstractmethod
            def reflection(self) -> Morphism:
                ...

            @abstractmethod
            def perp(self) -> Parent:
                ...

        class MorphismMethods(ABC):
            @final
            def is_isometry(self) -> bool:
                return self.is_form_preserving()

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class Quadratic(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "quadratic modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def form(self) -> QuadraticForm:
                ...

            @abstractmethod
            def associated_bilinear_module(self) -> Parent:
                ...

            @final
            def q(self, value: Element) -> Element:
                return self.form().evaluate(value)

            @final
            def b(self, left: Element, right: Element) -> Element:
                return self.associated_bilinear_module().form().evaluate(left, right)

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...

        class Homsets(ModulesWithFormsHomsets):
            class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
                ...

            class Endset(ModulesWithFormsHomsets.Endset):
                class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                    ...

                class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                    ...

                class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                    ...

    class ParentMethods(Modules.ParentMethods, ABC):
        @abstractmethod
        def underlying_module(self) -> Module:
            ...

        @abstractmethod
        def form(self) -> ModuleForm:
            ...

        @final
        def form_codomain(self) -> Parent:
            return self.form().codomain()

        @final
        def form_domain(self) -> Parent:
            return self.form().domain()

        @final
        def tensor_degree(self) -> Integer:
            return self.form().tensor_degree()

        @final
        def scalar_action_endomorphism(self) -> Morphism:
            return self.form().scalar_action_endomorphism()

        @abstractmethod
        def b(self, left: Element, right: Element) -> Element:
            ...

        @abstractmethod
        def q(self, value: Element) -> Element:
            ...

        @abstractmethod
        def is_bilinear(self) -> bool:
            ...

        @abstractmethod
        def is_quadratic(self) -> bool:
            ...

        @abstractmethod
        def is_integral(self) -> bool:
            ...

        @abstractmethod
        def is_rational(self) -> bool:
            ...

        @abstractmethod
        def is_nondegenerate(self) -> bool:
            ...

        @abstractmethod
        def is_isometric_to(
            self,
            other: Parent,
            witness: bool = False,
        ) -> bool | tuple[bool, Morphism]:
            ...

        @abstractmethod
        def zero_submodule(self) -> Parent:
            ...

        @abstractmethod
        def base_change(self, ring: Ring) -> Parent:
            ...

        @abstractmethod
        def __eq__(self, other: object) -> bool:
            ...

        @abstractmethod
        def __hash__(self) -> int:
            ...

        @abstractmethod
        def _repr_(self) -> str:
            ...

        @abstractmethod
        def _latex_(self) -> str:
            ...

    class ElementMethods(Modules.ElementMethods, ABC):
        @final
        def b(self, other: Element) -> Element:
            return self.parent().b(self, other)

        @final
        def q(self) -> Element:
            return self.parent().q(self)

    class MorphismMethods(Modules.MorphismMethods, ABC):
        @abstractmethod
        def is_form_preserving(self) -> bool:
            """Whether this morphism preserves the form data."""
            ...

        @abstractmethod
        def is_isometry(self) -> bool:
            ...

        @abstractmethod
        def adjoint(self) -> Morphism:
            ...


def BilinearModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Bilinear()


def QuadraticModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Quadratic()


def FreeBilinearModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Bilinear().Free()


def TorsionBilinearModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Torsion().Bilinear()


def Lattices(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Bilinear().Free().NonDegenerate().Integral()


def RationalLattices(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Bilinear().Free().NonDegenerate().Rational()


def DiscriminantQuadraticForms(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Quadratic().Torsion().NonDegenerate()


def DiscriminantBilinearForms(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    return ModulesWithForms(base_ring).Bilinear().Torsion().NonDegenerate()
