"""Spec class for homsets in ``ModulesWithForms(R)``."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from typing import final

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homsets import HomsetsCategory
from sage.misc.cachefunc import cached_method
from sage.categories.morphism import Morphism
from sage.rings.ring import Ring
from sage.structure.element import Element, Matrix
from sage.structure.parent import Parent


class ModulesWithFormsHomsets(HomsetsCategory):
    r"""Homset category for modules with forms."""

    # @override HomsetsCategory.extra_super_categories
    @final
    def extra_super_categories(self):
        return []

    # @override HomsetsCategory.base_ring
    @final
    def base_ring(self) -> Ring:
        return self.base_category().base_ring()

    # @override HomsetsCategory._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "homsets of modules with forms"

    # @override HomsetsCategory._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        @abstractmethod
        def domain(self) -> Parent:
            ...

        @abstractmethod
        def codomain(self) -> Parent:
            ...

        @final
        @cached_method
        def base_ring(self) -> Ring:
            return self.domain().base_ring()

        @abstractmethod
        def element_from_dict(self, mapping: Mapping[Element, Element]) -> Morphism:
            ...

        @abstractmethod
        def element_from_images(self, images: Sequence[Element]) -> Morphism:
            ...

        @abstractmethod
        def element_from_matrix(self, matrix_data: Matrix) -> Morphism:
            ...

        @abstractmethod
        def __contains__(self, value: object) -> bool:
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

    class Endset(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "endomorphism sets of modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @abstractmethod
            def identity(self) -> Morphism:
                ...

            @abstractmethod
            def Aut(self) -> Parent:
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
