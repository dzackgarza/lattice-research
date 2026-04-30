r"""Autset categories and automorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.cachefunc import cached_method
from sage.sets.condition_set import ConditionSet as SageConditionSet

from ..cat import Category, CategoryWithAxiom, CategoryWithAxiom_singleton
from .endsets import Endsets, EndsetsCategory
from .homsets import Homsets

if TYPE_CHECKING:
    from ..types import Automorphism, Autset, CategoryObject, Endomorphism, Endset, Subset


def _autsets_of(category: Category) -> Category:
    if category.is_subcategory(Endsets()):
        endsets = category
    elif category.is_subcategory(Homsets()):
        endsets = category.Endset()
    else:
        endsets = category.Homsets().Endset()
    return endsets.Autset()


def _is_invertible_endomorphism(endomorphism: Endomorphism) -> bool:
    r"""Return whether an endomorphism lies in the corresponding autset."""
    return endomorphism.is_invertible()


class UniversalAutsetObjectMethods:
    r"""Methods on objects ``Aut_C(A)`` of an autset category."""

    def condition_set(self) -> Subset:
        return self

    def endset(self) -> Endset:
        return self.condition_set().ambient()

    def domain(self) -> CategoryObject:
        return self.endset().domain()

    def codomain(self) -> CategoryObject:
        return self.endset().codomain()

    def identity(self) -> Automorphism:
        return self.endset().identity()

    def Aut(self) -> Autset:
        return self


class UniversalAutsetElementMethods:
    r"""Methods on elements of autsets."""

    @final
    def is_invertible(self) -> bool:
        return True

    @final
    def is_isomorphism(self) -> bool:
        return True

    @final
    def is_automorphism(self) -> bool:
        return True


class Autsets(CategoryWithAxiom_singleton):
    r"""Category of all automorphism sets."""

    _base_category_class_and_axiom = (Endsets, "Autset")

    def extra_super_categories(self) -> list:
        return [Endsets()]

    def from_endset(self, endset: Endset) -> Autset:
        return SageConditionSet(endset, _is_invertible_endomorphism, category=self)

    @cached_method
    def Of(self, category: Category) -> Category:
        r"""Return the generic category of autsets internal to ``category``."""
        if category.is_subcategory(Endsets()):
            return category.Autset()
        if category.is_subcategory(Homsets()):
            return category.Endset().Autset()
        return category.Homsets().Endset().Autset()

    ParentMethods = UniversalAutsetObjectMethods
    ElementMethods = UniversalAutsetElementMethods
    class MorphismMethods: ...


class AutsetsCategory(EndsetsCategory):
    r"""Functorial construction category for ``C.Autsets()``."""

    _functor_category = "Autsets"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        if cls is AutsetsOf:
            return Autsets()
        super_categories = category.super_categories()
        if not super_categories:
            return Autsets()
        return Category.join([_autsets_of(super_category) for super_category in super_categories])


class AutsetsOf(CategoryWithAxiom):
    r"""Generic category whose objects are ``Aut_C(A)``."""

    # Category-level construction: Autsets().Of(C) has objects Aut_C(A).
    # Category-object zero-argument C.Aut() selects C.Autsets(); object-level
    # autsets are the invertible endomorphisms inside A.Hom(A), where that
    # parent exists.

    def extra_super_categories(self) -> list:
        return [Autsets()]

    def from_endset(self, endset: Endset) -> Autset:
        return SageConditionSet(endset, _is_invertible_endomorphism, category=self)

    ParentMethods = UniversalAutsetObjectMethods
    ElementMethods = UniversalAutsetElementMethods
    class MorphismMethods: ...


__all__ = [
    "Autsets",
    "AutsetsCategory",
    "AutsetsOf",
    "UniversalAutsetElementMethods",
    "UniversalAutsetObjectMethods",
]
