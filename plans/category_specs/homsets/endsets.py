r"""Endset categories and endomorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category, CategoryWithAxiom, CategoryWithAxiom_singleton
from .homsets import Homsets, HomsetsCategory

if TYPE_CHECKING:
    from ..types import Autset, Endomorphism


def _endsets_of(category: Category) -> Category:
    if category.is_subcategory(Homsets()):
        return category.Endset()
    return category.Homsets().Endset()


class UniversalEndsetObjectMethods:
    r"""Methods on objects ``End_C(A)`` of an endset category."""

    @final
    def is_endomorphism_set(self) -> bool:
        return True

    @abstract_method
    def identity(self) -> Endomorphism: ...

    def Aut(self) -> Autset:
        return self.category().Autset().from_endset(self)


class UniversalEndsetElementMethods:
    r"""Methods on elements of endsets."""

    @final
    def is_endomorphism(self) -> bool:
        return True


class Endsets(CategoryWithAxiom_singleton):
    r"""Category of all endomorphism sets."""

    _base_category_class_and_axiom = (Homsets, "Endset")

    def extra_super_categories(self) -> list:
        from sage.categories.homsets import Homsets as SageHomsets

        return [SageHomsets().Endset()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Autset(self) -> Category:
            return self._with_axiom("Autset")


    @cached_method
    def Of(self, category: Category) -> Category:
        r"""Return the generic category of endsets internal to ``category``."""
        if category.is_subcategory(Homsets()):
            return category.Endset()
        return category.Homsets().Endset()

    ParentMethods = UniversalEndsetObjectMethods
    ElementMethods = UniversalEndsetElementMethods
    Autset = LazyImport("category_specs.homsets.autsets", "Autsets")


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


class EndsetsOf(CategoryWithAxiom):
    r"""Generic category whose objects are ``End_C(A)``."""

    # Category-level construction: Endsets().Of(C) has objects End_C(A).
    # It is distinct from the object-level parent A.End() = End_C(A).

    def extra_super_categories(self) -> list:
        return [Endsets()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Autset(self) -> Category:
            return self._with_axiom("Autset")

    ParentMethods = UniversalEndsetObjectMethods
    ElementMethods = UniversalEndsetElementMethods


__all__ = [
    "Endsets",
    "EndsetsCategory",
    "EndsetsOf",
    "UniversalEndsetElementMethods",
    "UniversalEndsetObjectMethods",
]
