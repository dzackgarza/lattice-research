r"""Homset categories and morphism method surfaces."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, overload

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..cat import Category
from ..cat import Homsets as BaseHomsets
from ..cat import HomsetsCategory as BaseHomsetsCategory
from ..cat import _SageCategory

if TYPE_CHECKING:
    from ..types import CategoryElement, CategoryObject, Morphism


class _HomsetParentMethods:
    r"""Methods on objects ``Hom_C(A, B)`` of a homset category."""

    @abstract_method
    def domain(self) -> CategoryObject: ...

    @abstract_method
    def codomain(self) -> CategoryObject: ...

    def is_endomorphism_set(self) -> bool:
        return self.domain() is self.codomain()

    @overload
    def __call__(self, morphism: Morphism) -> Morphism: ...

    @overload
    def __call__(self, function: Callable[[CategoryElement], CategoryElement]) -> Morphism: ...

    @abstract_method
    def __call__(self, data: Morphism | Callable[[CategoryElement], CategoryElement]) -> Morphism: ...


class _MorphismMethods:
    r"""Methods on elements ``f`` of homsets."""

    def domain(self) -> CategoryObject:
        return self.parent().domain()

    def codomain(self) -> CategoryObject:
        return self.parent().codomain()

    @abstract_method
    def __call__(self, x: CategoryElement) -> CategoryElement: ...

    @abstract_method
    def image(self, domain_subset: CategoryObject | None = None) -> CategoryObject: ...

    @abstract_method
    def pre_compose(self, other: Morphism) -> Morphism: ...

    @abstract_method
    def post_compose(self, other: Morphism) -> Morphism: ...

    def is_endomorphism(self) -> bool:
        return self.domain() is self.codomain()

    def is_identity(self) -> bool:
        return self.is_endomorphism() and self == self.parent().identity()

    @abstract_method
    def is_invertible(self) -> bool: ...

    @abstract_method
    def is_isomorphism(self) -> bool:
        ...

    def is_automorphism(self) -> bool:
        return self.is_endomorphism() and self.is_invertible()


class Homsets(BaseHomsets):
    r"""Category of all homsets."""

    def super_categories(self) -> list[Category]:
        return [BaseHomsets()]

    @cached_method
    def Endset(self) -> Category:
        from .endsets import Endsets

        return Endsets()

    @cached_method
    def Autset(self) -> Category:
        from .autsets import Autsets

        return Autsets()

    @cached_method
    def Of(self, category: Category) -> Category:
        r"""Return the generic category of homsets internal to ``category``."""
        return HomsetsOf(category)

    ParentMethods = _HomsetParentMethods
    ElementMethods = _MorphismMethods


class HomsetsCategory(BaseHomsetsCategory):
    r"""Functorial construction category for ``C.Homsets()``."""

    _functor_category = "Homsets"
    _base_category_class = (_SageCategory,)

    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        if cls is HomsetsOf:
            return Homsets()
        super_categories = category.super_categories()
        if not super_categories:
            return Homsets()
        return Category.join([super_category.Homsets() for super_category in super_categories])

    def _make_named_class_key(self, name: str):
        return getattr(self.base_category(), name)


class HomsetsOf(HomsetsCategory):
    r"""Generic category whose objects are ``Hom_C(A, B)``."""

    # This is the category-level construction for a category C:
    # Homsets().Of(C) is the category whose objects are the parents Hom_C(A, B).
    # It is not an object-level Hom_C(A, B) parent and it does not define
    # set-map-only predicates such as injectivity.

    def _repr_object_names(self) -> str:
        base_category = self.base_category()
        try:
            object_names = base_category._repr_object_names()
        except ValueError:
            object_names = " and ".join(category._repr_object_names() for category in base_category.super_categories())
        return f"homsets of {object_names}"

    @cached_method
    def Endset(self) -> Category:
        from .endsets import Endsets

        return Endsets().Of(self.base_category())

    @cached_method
    def Autset(self) -> Category:
        from .autsets import Autsets

        return Autsets().Of(self.base_category())


__all__ = [
    "Homsets",
    "HomsetsCategory",
    "HomsetsOf",
]
