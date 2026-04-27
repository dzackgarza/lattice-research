r"""Autset categories and automorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.cachefunc import cached_method
from sage.sets.condition_set import ConditionSet as SageConditionSet

from ..cat import Category
from .endsets import Endsets, EndsetsCategory
from .homsets import Homsets

if TYPE_CHECKING:
    from ..types import Automorphism, Autset, CategoryObject, Endomorphism, Endset, Subset


def _autsets_of(category: Category) -> Category:
    homsets = category if category.is_subcategory(Homsets()) else category.Homsets()
    autset = getattr(homsets, "Autset", None)
    if autset is None:
        return Autsets().Of(homsets)
    return autset()


def _is_invertible_endomorphism(endomorphism: Endomorphism) -> bool:
    r"""Return whether an endomorphism lies in the corresponding autset."""
    return endomorphism.is_invertible()


class _AutsetParentMethods:
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


class _AutomorphismMethods:
    r"""Methods on elements of autsets."""

    def is_invertible(self) -> bool:
        return True

    def is_isomorphism(self) -> bool:
        return True

    def is_automorphism(self) -> bool:
        return True


class Autsets(Category):
    r"""Category of all automorphism sets."""

    def super_categories(self) -> list[Category]:
        return [Endsets()]

    def from_endset(self, endset: Endset) -> Autset:
        return SageConditionSet(endset, _is_invertible_endomorphism, category=self)

    @cached_method
    def Of(self, category: Category) -> Category:
        r"""Return the generic category of autsets internal to ``category``."""
        return AutsetsOf(category)

    ParentMethods = _AutsetParentMethods
    ElementMethods = _AutomorphismMethods


class AutsetsCategory(EndsetsCategory):
    r"""Functorial construction category for ``C.Autsets()``."""

    _functor_category = "Autsets"

    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        if cls is AutsetsOf:
            return Autsets()
        super_categories = category.super_categories()
        if not super_categories:
            return Autsets()
        return Category.join([_autsets_of(super_category) for super_category in super_categories])


class AutsetsOf(AutsetsCategory):
    r"""Generic category whose objects are ``Aut_C(A)``."""

    # Category-level construction: Autsets().Of(C) has objects Aut_C(A).
    # It is distinct from the object-level parent A.Aut() = Aut_C(A).

    def extra_super_categories(self) -> list[Category]:
        base_category = self.base_category()
        if base_category.is_subcategory(Homsets()):
            return [Autsets(), base_category.Endset()]
        endsets = getattr(base_category, "Endsets", None)
        if endsets is not None:
            return [Autsets(), endsets()]
        return [Autsets(), base_category.Homsets().Endset()]

    def from_endset(self, endset: Endset) -> Autset:
        return SageConditionSet(endset, _is_invertible_endomorphism, category=self)


__all__ = [
    "Autsets",
    "AutsetsCategory",
    "AutsetsOf",
]
