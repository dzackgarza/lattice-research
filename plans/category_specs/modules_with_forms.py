"""Spec stub for ``ModulesWithForms(R)``."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import final

from sage.categories.category import Category
from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homset import Hom, Homset
from sage.categories.modules import Modules
from sage.categories.morphism import Morphism
from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.categories.tensor import TensorProductsCategory
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.modules.module import Module
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import Element, InfinityElement, Matrix, RingElement, Vector
from sage.structure.parent import Parent

Cardinality = Integer | InfinityElement


class ModuleForm(Morphism, ABC):
    """Abstract base class for form morphisms."""

    @abstractmethod
    def domain(self) -> Module:
        ...

    @abstractmethod
    def codomain(self) -> Ring:
        ...

    @abstractmethod
    def evaluate(self, value: Element) -> RingElement:
        ...

    @abstractmethod
    def gram_matrix(self) -> Matrix:
        ...

    @abstractmethod
    def _repr_(self) -> str:
        ...

    @abstractmethod
    def _latex_(self) -> str:
        ...


class BilinearForm(ModuleForm):
    """Abstract base class for bilinear forms `L \\otimes_R L -> R`."""

    @abstractmethod
    def underlying_module(self) -> Module:
        ...

    @abstractmethod
    def evaluate(
        self,
        value: Element,
        right: Element | None = None,
    ) -> RingElement:
        ...

    @abstractmethod
    def associated_quadratic_form(self) -> QuadraticForm:
        ...


class QuadraticForm(ModuleForm):
    """Abstract base class for quadratic forms `L -> R`."""

    @abstractmethod
    def associated_bilinear_form(self) -> BilinearForm:
        ...


from .homsets import ModulesWithFormsHomsets


class ModulesWithForms(Category_module):
    r"""
    Spec stub for the category of finitely generated modules with forms.

    An object is a pair ``(M, f)`` with ``M = F ⊕ T`` a finitely generated
    module over a commutative PID ``R`` and ``f`` a primary bilinear or
    quadratic form. Front-door construction is restricted to forms valued in
    ``R`` or its fraction field ``K``. Quotient-valued codomains such as
    ``K / R`` and ``K / 2R`` appear by explicit descent on actual cokernel
    objects.
    """

    Homsets = LazyImport("plans.category_specs.homsets", "ModulesWithFormsHomsets")
    DualObjects = LazyImport("plans.category_specs.dual_objects", "ModulesWithFormsDualObjects")
    Torsion = LazyImport(
        "plans.category_specs.torsion_modules_with_forms",
        "TorsionModulesWithForms",
    )

    BilinearForms = LazyImport("plans.category_specs.bilinear_form", "BilinearForms")

    # @override Category_module.__classcall_private__
    @staticmethod
    @final
    def __classcall_private__(cls, base_ring: Ring):
        if base_ring not in PrincipalIdealDomains():
            raise TypeError("ModulesWithForms is only defined over commutative PIDs")
        return super(ModulesWithForms, cls).__classcall__(cls, base_ring)

    # @override Category_module.super_categories
    @final
    def super_categories(self) -> list[Category]:
        return [Modules(self.base_ring()).WithBasis().FinitelyPresented()]

    # @override Category_module.additional_structure
    @final
    def additional_structure(self) -> Category:
        # Morphisms are required to preserve the attached form.
        return self

    # @override Category_module._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return f"modules with forms over {self.base_ring()}"

    # @override Category_module._latex_
    def _latex_(self) -> str:
        ...

    class SubcategoryMethods:
        # @override Modules.SubcategoryMethods.base_ring
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

        # @override Modules.SubcategoryMethods.DualObjects
        @final
        @cached_method
        def DualObjects(self) -> Category:
            return ModulesWithForms.DualObjects.category_of(self)

        dual = DualObjects

        # @override Modules.SubcategoryMethods.TensorProducts
        @final
        @cached_method
        def TensorProducts(self) -> Category:
            return ModulesWithForms.TensorProducts.category_of(self)

        # @override Modules.SubcategoryMethods.CartesianProducts
        @final
        @cached_method
        def CartesianProducts(self) -> Category:
            return ModulesWithForms.CartesianProducts.category_of(self)

        @final
        @cached_method
        def BilinearForms(self) -> Category:
            return ModulesWithForms.BilinearForms(self.base_ring())

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

        class ParentMethods:
            ...

        class ElementMethods:
            ...

        class MorphismMethods:
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

        class ParentMethods:
            ...

        class ElementMethods:
            ...

        class MorphismMethods:
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

        class ParentMethods:
            ...

        class ElementMethods:
            ...

        class MorphismMethods:
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

        class ParentMethods:
            ...

        class ElementMethods:
            ...

        class MorphismMethods:
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
        r"""External category class for the ``Bilinear`` axiom."""

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
            # @override ModulesWithForms.ParentMethods.form
            # type override only
            @abstractmethod
            def form(self) -> BilinearForm:
                ...

            @abstractmethod
            def associated_quadratic_module(self) -> Parent:
                ...

            # @override ModulesWithForms.ParentMethods.b
            @final
            def b(
                self,
                left: Element,
                right: Element,
            ) -> RingElement:
                return self.form().evaluate(left, right)

            # @override ModulesWithForms.ParentMethods.q
            @final
            def q(self, value: Element) -> RingElement:
                return self.associated_quadratic_module().form().evaluate(value)

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

    class Quadratic(CategoryWithAxiom_over_base_ring):
        r"""External category class for the ``Quadratic`` axiom."""

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
            # @override ModulesWithForms.ParentMethods.form
            # type override only
            @abstractmethod
            def form(self) -> QuadraticForm:
                ...

            @abstractmethod
            def associated_bilinear_module(self) -> Parent:
                ...

            # @override ModulesWithForms.ParentMethods.q
            @final
            def q(self, value: Element) -> RingElement:
                return self.form().evaluate(value)

            # @override ModulesWithForms.ParentMethods.b
            @final
            def b(
                self,
                left: Element,
                right: Element,
            ) -> RingElement:
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

    class FreeBilinearModules(CategoryWithAxiom_over_base_ring):
        r"""Spec class for the meet ``Bilinear ∧ Free``."""

        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring()).Bilinear().Free()]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "free bilinear modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def rank(self) -> Integer:
                ...

            # @override ModulesWithForms.ParentMethods.free_rank
            @final
            def free_rank(self) -> Integer:
                return self.rank()

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
            @abstractmethod
            def divisibility(self) -> RingElement:
                ...

            @abstractmethod
            def is_primitive(self) -> bool:
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

    class Lattices(CategoryWithAxiom_over_base_ring):
        r"""Spec class for the meet ``Bilinear ∧ Free ∧ NonDegenerate ∧ Integral``."""

        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring()).Bilinear().Free().NonDegenerate().Integral()]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "lattices"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def signature_pair(self) -> tuple[Integer, Integer]:
                ...

            @abstractmethod
            def determinant(self) -> RingElement:
                ...

            @final
            def discriminant(self) -> RingElement:
                return abs(self.determinant())

            @abstractmethod
            def is_even(self) -> bool:
                ...

            @final
            def is_odd(self) -> bool:
                return not self.is_even()

            @final
            def is_unimodular(self) -> bool:
                return self.discriminant() == 1

            @abstractmethod
            def nikulin_invariants(self) -> tuple[Integer, ...]:
                ...

            @abstractmethod
            def discriminant_group(self) -> Parent:
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
            def is_locally_isometric_to(
                self, other: Parent, p: RingElement
            ) -> bool:
                ...

            @abstractmethod
            def orthogonal_group(self) -> Parent:
                ...

            @final
            def O(self) -> Parent:
                return self.orthogonal_group()

            @abstractmethod
            def to_quadratic_module(self) -> Parent:
                ...

        class ElementMethods(ABC):
            @abstractmethod
            def norm(self) -> RingElement:
                ...

            @abstractmethod
            def is_root(self) -> bool:
                ...

            @abstractmethod
            def reflection(self) -> Morphism:
                ...

            @abstractmethod
            def perp(self) -> Parent:
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

    class RationalLattices(CategoryWithAxiom_over_base_ring):
        r"""Spec class for the meet ``Bilinear ∧ Free ∧ NonDegenerate ∧ Rational``."""

        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring()).Bilinear().Free().NonDegenerate().Rational()]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "rational lattices"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def signature_pair(self) -> tuple[Integer, Integer]:
                ...

            @abstractmethod
            def orthogonal_complement_of(
                self, submodule: Parent
            ) -> Parent:
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

    class DiscriminantQuadraticForms(CategoryWithAxiom_over_base_ring):
        r"""Spec class for the descended meet ``Quadratic ∧ Torsion ∧ NonDegenerate``."""

        # @override CategoryWithAxiom_over_base_ring.super_categories
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring()).Quadratic().Torsion().NonDegenerate()]

        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "discriminant quadratic forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def associated_discriminant_bilinear_form(self) -> BilinearForm:
                ...

            # @override ModulesWithForms.ParentMethods.form
            # type override only
            @abstractmethod
            def form(self) -> QuadraticForm:
                ...

            # @override ModulesWithForms.ParentMethods.q
            @final
            def q(self, value: Element) -> RingElement:
                return self.form().evaluate(value)

            # @override ModulesWithForms.ParentMethods.b
            @final
            def b(
                self,
                left: Element,
                right: Element,
            ) -> RingElement:
                return self.associated_discriminant_bilinear_form().evaluate(left, right)

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

    class ParentMethods(ABC):
        @abstractmethod
        def underlying_module(self) -> Module:
            ...

        @abstractmethod
        def form(self) -> ModuleForm:
            ...

        @abstractmethod
        def b(
            self,
            left: Element,
            right: Element,
        ) -> RingElement:
            ...

        @abstractmethod
        def q(self, value: Element) -> RingElement:
            ...

        @abstractmethod
        def gens(self) -> tuple[Element, ...]:
            ...

        @final
        def gen(self, index: int) -> Element:
            return self.gens()[index]

        @abstractmethod
        def __iter__(self) -> Iterator[Element]:
            ...

        @abstractmethod
        def zero(self) -> Element:
            ...

        @abstractmethod
        def zero_submodule(self) -> Parent:
            ...

        @abstractmethod
        def base_ring(self) -> Ring:
            ...

        @abstractmethod
        def free_part(self) -> Parent:
            ...

        @abstractmethod
        def torsion_part(self) -> Parent:
            ...

        @abstractmethod
        def dual(self) -> Parent:
            ...

        @abstractmethod
        def is_free(self) -> bool:
            ...

        @abstractmethod
        def is_torsion(self) -> bool:
            ...

        @abstractmethod
        def is_torsionfree(self) -> bool:
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
        def free_rank(self) -> Integer:
            ...

        @abstractmethod
        def cardinality(self) -> Cardinality:
            ...

        @abstractmethod
        def is_finite(self) -> bool:
            ...

        @abstractmethod
        def is_isometric_to(self, other: Parent) -> bool:
            ...

        @final
        def Hom(self, other: Parent) -> Homset:
            return Hom(self, other, category=self.category())

        @final
        def End(self) -> Homset:
            return self.Hom(self)

        @final
        def Aut(self) -> Parent:
            return self.End().Aut()

        @abstractmethod
        def direct_sum(self, *others: Parent) -> Parent:
            ...

        @abstractmethod
        def tensor(self, *others: Parent) -> Parent:
            ...

        @abstractmethod
        def span(self, elements: Iterable[Element]) -> Parent:
            ...

        @abstractmethod
        def random_element(self) -> Element:
            ...

        @abstractmethod
        def _lmul_(self, scalar: RingElement) -> Parent:
            ...

        @abstractmethod
        def base_change(self, ring: Ring) -> Parent:
            ...

        @final
        def __add__(self, other: Parent) -> Parent:
            return self.direct_sum(other)

        @final
        def __mul__(self, other: Parent) -> Parent:
            return self.tensor(other)

        @final
        def __rmul__(self, scalar: RingElement) -> Parent:
            return self._lmul_(scalar)

        @abstractmethod
        def __contains__(self, value: object) -> bool:
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

    class ElementMethods(ABC):
        @abstractmethod
        def parent(self) -> Parent:
            ...

        @final
        def b(self, other: Element) -> RingElement:
            return self.parent().b(self, other)

        @final
        def q(self) -> RingElement:
            return self.parent().q(self)

        @abstractmethod
        def __add__(self, other: Element) -> Element:
            ...

        @abstractmethod
        def __neg__(self) -> Element:
            ...

        @abstractmethod
        def _lmul_(self, scalar: RingElement) -> Element:
            ...

        @final
        def __rmul__(self, scalar: RingElement) -> Element:
            return self._lmul_(scalar)

        @abstractmethod
        def to_vector(self) -> Vector:
            ...

        @final
        def span(self) -> Parent:
            return self.parent().span([self])

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

    class MorphismMethods(ABC):
        @abstractmethod
        def parent(self) -> Homset:
            ...

        @abstractmethod
        def domain(self) -> Parent:
            ...

        @abstractmethod
        def codomain(self) -> Parent:
            ...

        @abstractmethod
        def __call__(self, value: Element) -> Element:
            ...

        @abstractmethod
        def to_matrix(self) -> Matrix:
            ...

        @final
        def to_tuple_of_images(self) -> tuple[Element, ...]:
            return tuple(self(generator) for generator in self.domain().gens())

        @final
        def to_list_of_images(self) -> list[Element]:
            return list(self.to_tuple_of_images())

        @final
        def to_dict(self) -> dict[Element, Element]:
            return {
                generator: image
                for generator, image in zip(
                    self.domain().gens(),
                    self.to_tuple_of_images(),
                    strict=True,
                )
            }

        @abstractmethod
        def kernel(self) -> Parent:
            ...

        @abstractmethod
        def image(self) -> Parent:
            ...

        @abstractmethod
        def cokernel(self) -> Parent:
            ...

        @abstractmethod
        def index(self) -> Cardinality:
            ...

        @abstractmethod
        def lift(self, value: Element) -> Element:
            ...

        @abstractmethod
        def saturation(self) -> Parent:
            ...

        @abstractmethod
        def intersection(self, other: Morphism) -> Parent:
            ...

        @abstractmethod
        def is_injective(self) -> bool:
            ...

        @abstractmethod
        def is_surjective(self) -> bool:
            ...

        @final
        def is_bijective(self) -> bool:
            return self.is_injective() and self.is_surjective()

        @abstractmethod
        def direct_sum(self, other: Morphism) -> Morphism:
            ...

        @abstractmethod
        def tensor(self, other: Morphism) -> Morphism:
            ...

        @abstractmethod
        def base_change(self, ring: Ring) -> Morphism:
            ...

        @abstractmethod
        def __mul__(self, other: Morphism) -> Morphism:
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


def TorsionBilinearModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Torsion().Bilinear()``."""

    return ModulesWithForms(base_ring).Torsion().Bilinear()


def BilinearModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Bilinear()``."""

    return ModulesWithForms(base_ring).Bilinear()


def QuadraticModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Quadratic()``."""

    return ModulesWithForms(base_ring).Quadratic()


def FreeBilinearModules(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Bilinear().Free()``."""

    return ModulesWithForms(base_ring).Bilinear().Free()


def Lattices(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()``."""

    return ModulesWithForms(base_ring).Bilinear().Free().NonDegenerate().Integral()


def RationalLattices(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()``."""

    return ModulesWithForms(base_ring).Bilinear().Free().NonDegenerate().Rational()


def DiscriminantQuadraticForms(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()``."""

    return ModulesWithForms(base_ring).Quadratic().Torsion().NonDegenerate()


def DiscriminantBilinearForms(base_ring: Ring) -> CategoryWithAxiom_over_base_ring:
    r"""Named meet ``ModulesWithForms(R).Bilinear().Torsion().NonDegenerate()``."""

    return ModulesWithForms(base_ring).Bilinear().Torsion().NonDegenerate()
