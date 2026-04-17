"""Spec class for the TwistedForms category."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final
import sage.categories.category_with_axiom as _cwa
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.rings.integer import Integer
from sage.structure.element import Matrix
from sage.structure.parent import Parent

from .types import (
    BilinearForm,
    BilinearFormSpace,
    QuadraticForm,
    QuadraticFormSpace,
    RingMorphism,
    RModule,
    RModuleElement,
    TensorProductRModule,
)

_cwa.all_axioms += ("Bilinear", "Quadratic")


class TwistedForms(Category_over_base_ring):
    r"""
    The category of twisted form spaces over a base ring ``R``.

    Objects in this category are Hom-spaces ``Hom_R(T_R(M)[k], S)^\sigma``. Here:
    - ``T_R(M)`` is the tensor algebra of an ``R``-module ``M``,
    - ``[k]`` is the ``k``-th graded piece,
    - ``S`` is an ``R``-module (typically ``R`` or a quotient ``K/R``),
    - ``\sigma \in Aut(R)`` is the twist.

    These forms satisfy the semilinearity condition:
    ``f(r \cdot m) = \sigma(r) \cdot f(m)``.
    """

    @final
    def super_categories(self) -> list[Category]:
        from .modules import Modules
        return [Modules(self.base_ring()).TensorProducts().Homsets()]

    @final
    def _repr_object_names(self) -> str:
        return "twisted form spaces"

    def _latex_(self) -> str:
        ...

    class SubcategoryMethods:
        @final
        def Bilinear(self):
            return self._with_axiom("Bilinear")

        @final
        def Quadratic(self):
            return self._with_axiom("Quadratic")

    class ParentMethods(ABC):
        @abstractmethod
        def base_module(self) -> RModule | TensorProductRModule:
            r"""The underlying module ``M``."""
            ...

        @abstractmethod
        def tensor_degree(self) -> Integer:
            r"""The degree ``k`` of the graded piece."""
            ...

        @abstractmethod
        def twist_endomorphism(self) -> RingMorphism:
            r"""The twist automorphism ``\sigma \in Aut(R)``."""
            ...

    class ElementMethods(ABC):
        @final
        def tensor_degree(self) -> Integer:
            return self.parent().tensor_degree()

        @final
        def twist_endomorphism(self) -> RingMorphism:
            return self.parent().twist_endomorphism()

        @final
        def base_module(self) -> RModule | TensorProductRModule:
            return self.parent().base_module()

    class MorphismMethods(ABC):
        ...

    class Bilinear(CategoryWithAxiom_over_base_ring):
        r"""
        Symmetric bilinear form spaces.

        Degree ``k=2`` with ``\sigma = id_R``.
        """
        @final
        def _repr_object_names(self) -> str:
            return "bilinear twisted form spaces"

        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @final
            def tensor_degree(self) -> Integer:
                return Integer(2)

            @abstractmethod
            def associated_quadratic_form_space(self) -> QuadraticFormSpace:
                ...

        class ElementMethods(ABC):
            @abstractmethod
            def gram_matrix(self) -> Matrix:
                ...

            @abstractmethod
            def associated_quadratic_form(self) -> QuadraticForm:
                ...

    class Quadratic(CategoryWithAxiom_over_base_ring):
        r"""
        Quadratic form spaces.

        Degree ``k=1`` with semilinearity twist ``\sigma(r) = r^2``.
        """
        @final
        def _repr_object_names(self) -> str:
            return "quadratic twisted form spaces"

        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @final
            def tensor_degree(self) -> Integer:
                return Integer(1)

            @abstractmethod
            def associated_bilinear_form_space(self) -> BilinearFormSpace:
                ...

        class ElementMethods(ABC):
            @abstractmethod
            def associated_bilinear_form(self) -> BilinearForm:
                ...
