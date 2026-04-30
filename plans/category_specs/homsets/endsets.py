r"""End categories and endomorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category, CategoryWithAxiom, CategoryWithAxiom_singleton
from .homsets import HomCategory, HomCategoryConstruction

if TYPE_CHECKING:
    from ..types import CategoryObject, End, Endomorphism


def _end_categories_of(category: Category) -> Category:
    if category.is_subcategory(HomCategory()):
        return category.EndCategory()
    return category.HomCategory().EndCategory()


class UniversalEndObjectMethods:
    r"""Methods on objects ``End_C(A)`` of an end category."""

    @final
    def is_endomorphism_set(self) -> bool:
        return True

    @abstract_method
    def identity(self) -> Endomorphism: ...


class UniversalEndElementMethods:
    r"""Methods on elements of end categories."""

    @final
    def is_endomorphism(self) -> bool:
        return True


class EndCategory(CategoryWithAxiom_singleton):
    r"""Category of all endomorphism categories."""

    _base_category_class_and_axiom = (HomCategory, "Endset")

    def extra_super_categories(self) -> list[Category]:
        from sage.categories.homsets import Homsets as SageHomsets

        return [SageHomsets().Endset()]

    class SubcategoryMethods:
        @cached_method
        @final
        def AutCategory(self) -> Category:
            return self._with_axiom("Autset")

    ParentMethods = UniversalEndObjectMethods
    ElementMethods = UniversalEndElementMethods
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport("category_specs.homsets.autsets", "AutCategory")


class EndCategoryConstruction(HomCategoryConstruction):
    r"""Functorial construction category for ``C.EndCategory()``."""

    _functor_category = "EndCategory"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

    @final
    def Of(self, domain: CategoryObject) -> End:
        r"""Return ``End_C(domain)`` for ``C = self.base_category()``."""
        return self.base_category().HomCategory().Of(domain, domain)

    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        if cls is EndCategoryOf:
            return EndCategory()
        super_categories = category.super_categories()
        if not super_categories:
            return EndCategory()
        return Category.join([_end_categories_of(super_category) for super_category in super_categories])


class EndCategoryOf(CategoryWithAxiom):
    r"""Generic category whose objects are ``End_C(A)``."""

    # Category-level construction: C.EndCategory() has objects End_C(A).
    # Its Of(A) constructor evaluates the construction at A.

    def extra_super_categories(self) -> list[Category]:
        return [EndCategory()]

    @final
    def Of(self, domain: CategoryObject) -> End:
        r"""Return ``End_C(domain)`` for ``C = self.base_category()``."""
        return self.base_category().Of(domain, domain)

    class SubcategoryMethods:
        @cached_method
        @final
        def AutCategory(self) -> Category:
            return self._with_axiom("Autset")

    ParentMethods = UniversalEndObjectMethods
    ElementMethods = UniversalEndElementMethods
    class MorphismMethods: ...
