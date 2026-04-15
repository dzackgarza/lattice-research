"""Spec class for the bilinear-form stratum."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.modules.module import Module
from sage.rings.ring import Ring
from sage.structure.element import Element, Matrix, RingElement

from .homsets import ModulesWithFormsHomsets

if TYPE_CHECKING:
    from .modules_with_forms import QuadraticForm


class BilinearForms(CategoryWithAxiom_over_base_ring):
    r"""Spec class for bilinear form objects associated to modules with forms."""

    # @override CategoryWithAxiom_over_base_ring.super_categories
    @final
    def super_categories(self):
        from .modules_with_forms import ModulesWithForms

        return [ModulesWithForms(self.base_ring()).Bilinear()]

    # @override CategoryWithAxiom_over_base_ring._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "bilinear forms"

    # @override CategoryWithAxiom_over_base_ring._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        @abstractmethod
        def domain(self) -> Module:
            ...

        @abstractmethod
        def codomain(self) -> Ring:
            ...

        @final
        def arity(self) -> int:
            return 2

        @abstractmethod
        def gram_matrix(self) -> Matrix:
            ...

        @abstractmethod
        def evaluate(self, left: Element, right: Element) -> RingElement:
            ...

        @abstractmethod
        def associated_quadratic_form(self) -> QuadraticForm:
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
