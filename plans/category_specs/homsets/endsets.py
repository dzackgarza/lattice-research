r"""Endset categories and endomorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..cat import Category
from ..cat import Homsets as BaseHomsets
from .homsets import Homsets, HomsetsCategory

if TYPE_CHECKING:
    from ..types import Autset, Endomorphism


def _endsets_of(category: Category) -> Category:
    if category.is_subcategory(Homsets()):
        return category.Endset()
    return category.Homsets().Endset()


class _EndsetParentMethods:
    r"""Methods on objects ``End_C(A)`` of an endset category."""

    def is_endomorphism_set(self) -> bool:
        return True

    @abstract_method
    def identity(self) -> Endomorphism: ...

    def Aut(self) -> Autset:
        return self.category().Autset().from_endset(self)


class _EndomorphismMethods:
    r"""Methods on elements of endsets."""

    def is_endomorphism(self) -> bool:
        return True


class Endsets(Category):
    r"""Category of all endomorphism sets."""

    def super_categories(self) -> list[Category]:
        return [BaseHomsets().Endset()]

    @cached_method
    def Autset(self) -> Category:
        from .autsets import Autsets

        return Autsets()

    @cached_method
    def Of(self, category: Category) -> Category:
        r"""Return the generic category of endsets internal to ``category``."""
        return EndsetsOf(category)

    ParentMethods = _EndsetParentMethods
    ElementMethods = _EndomorphismMethods


class EndsetsCategory(HomsetsCategory):
    r"""Functorial construction category for ``C.Endsets()``."""

    _functor_category = "Endsets"

    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        if cls is EndsetsOf:
            return Endsets()
        super_categories = category.super_categories()
        if not super_categories:
            return Endsets()
        return Category.join([_endsets_of(super_category) for super_category in super_categories])


class EndsetsOf(EndsetsCategory):
    r"""Generic category whose objects are ``End_C(A)``."""

    # Category-level construction: Endsets().Of(C) has objects End_C(A).
    # It is distinct from the object-level parent A.End() = End_C(A).

    def extra_super_categories(self) -> list[Category]:
        base_category = self.base_category()
        if base_category.is_subcategory(Homsets()):
            return [Endsets(), base_category]
        return [Endsets(), base_category.Homsets()]

    @cached_method
    def Autset(self) -> Category:
        from .autsets import Autsets

        return Autsets().Of(self.base_category())


__all__ = [
    "Endsets",
    "EndsetsCategory",
    "EndsetsOf",
]
