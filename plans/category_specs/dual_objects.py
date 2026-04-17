"""Spec class for dual objects in ``ModulesWithForms(R)``."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final

from sage.categories.dual import DualObjectsCategory
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

from .homsets import ModulesWithFormsHomsets

if TYPE_CHECKING:
    from .modules_with_forms import BilinearForm


class ModulesWithFormsDualObjects(DualObjectsCategory):
    r"""
    Dual objects of modules with forms.

    For an object ``(L, b)`` in the base category, the dual object is the
    pair ``(L^*, b^*)`` with ``L^* := Hom_R(L, R)`` regarded as an actual
    homset of ``R``-modules and with ``b`` identified with the tensor
    ``sum_{i,j} b(e_i, e_j) e_i^* \otimes e_j^*`` in ``L^* \otimes_R L^*``
    for the formal dual basis attached to the chosen generators ``e_i`` of
    ``L``.
    """

    # @override DualObjectsCategory.extra_super_categories
    @final
    def extra_super_categories(self):
        from .modules import Modules
        base = self.base_category()
        R = base.base_ring()
        return [base, Modules(R).FinitelyPresented()]

    # @override DualObjectsCategory._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "dual objects of modules with forms"

    # @override DualObjectsCategory._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        # @override DualObjectsCategory.ParentMethods.dual_of
        @abstractmethod
        def dual_of(self) -> Parent:
            ...

        # @override DualObjectsCategory.ParentMethods.natural_pairing
        @abstractmethod
        def natural_pairing(self) -> BilinearForm:
            ...

        @final
        def as_linear_dual(self) -> Homset:
            return self

        @final
        def formal_dual_basis(self) -> tuple[Morphism, ...]:
            return self.gens()

        @abstractmethod
        def source_form_as_dual_tensor(self) -> Element:
            ...

        @abstractmethod
        def _repr_(self) -> str:
            ...

        @abstractmethod
        def _latex_(self) -> str:
            ...

    class ElementMethods(ABC):
        @final
        def as_linear_functional(self) -> Morphism:
            return self

        @final
        def evaluate(self, value: Element) -> RingElement:
            return self(value)

        @abstractmethod
        def __call__(self, value: Element) -> RingElement:
            ...

        @abstractmethod
        def __mul__(self, value: Element | Morphism) -> RingElement:
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
