r"""Homset categories and morphism method surfaces."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, final, overload

from sage.categories.homsets import Homsets as SageHomsets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.structure.dynamic_class import DynamicMetaclass

from ..cat import Cat, Category, Category_singleton, CategoryWithParameters, FunctorialConstructionCategory, _SageCategory

if TYPE_CHECKING:
    from ..types import CategoryElement, CategoryObject, Morphism


def _base_class(cls: type) -> type:
    if isinstance(cls, DynamicMetaclass):
        return cls.__base__
    return cls


class UniversalHomsetObjectMethods:
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


class UniversalHomsetElementMethods:
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


class Homsets(Category_singleton):
    r"""Category of all homsets."""

    def super_categories(self) -> list:
        return [SageHomsets()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Endset(self) -> Category:
            return self._with_axiom("Endset")

        @cached_method
        @final
        def Autset(self) -> Category:
            return self.Endset().Autset()

    @cached_method
    def Of(self, category: Category) -> Category:
        r"""Return the generic category of homsets internal to ``category``."""
        return HomsetsOf(category)

    ParentMethods = UniversalHomsetObjectMethods
    ElementMethods = UniversalHomsetElementMethods
    Endset = LazyImport("category_specs.homsets.endsets", "Endsets")


class HomsetsCategory(FunctorialConstructionCategory, CategoryWithParameters):
    r"""Functorial construction category for ``C.Homsets()``."""

    _functor_category = "Homsets"
    _base_category_class = (_SageCategory,)

    @classmethod
    @final
    def default_super_categories(cls, category: Category) -> Category:
        r"""Return homset supercategories without repeating one construction.

        Sage's homset construction is deliberately not handled like an
        ordinary covariant functor: its own
        ``HomsetsCategory.default_super_categories`` first looks at full
        supercategories, and otherwise falls back to the generic
        ``HomsetsOf`` stub.  That distinction matters here because the Cat
        wrapper layer makes ``Homsets`` a universal construction method on
        every project category object.  If we naively recurse through every
        supercategory after that rewrite, a chain such as
        ``Modules(R).OverPID() -> OverDedekind() -> OverIntegralDomain() ->
        Modules(R)`` contributes four different dynamic
        ``RModuleHomsets.parent_class`` and ``RModuleHomsets.element_class``
        providers.  Each provider declares the same abstract module-homset
        requirements, so the resulting mixed classes re-declare the same spec
        surface several times.

        The mathematical relation we need is weaker and cleaner: keep homset
        supercategories that use a genuinely different construction class
        (for example ``Sets().Homsets()`` under module homsets), but collapse
        intermediate supercategories whose homsets are again the same local
        construction.  The base category itself can still appear through
        ``extra_super_categories`` where a concrete homset category, such as
        ``RModuleHomsets``, declares that its objects are also modules.
        """
        construction_class = _base_class(cls)
        if construction_class is HomsetsOf:
            return Homsets()

        homset_supercategories = []
        homset_supercategory_ids = set()
        seen_category_ids = set()

        def collect_supercategory_homsets(base_category: Category) -> None:
            for super_category in base_category.super_categories():
                if id(super_category) in seen_category_ids:
                    continue
                seen_category_ids.add(id(super_category))
                homsets = super_category.Homsets()
                if _base_class(homsets.__class__) is construction_class:
                    collect_supercategory_homsets(super_category)
                    continue
                if id(homsets) in homset_supercategory_ids:
                    continue
                homset_supercategories.append(homsets)
                homset_supercategory_ids.add(id(homsets))

        collect_supercategory_homsets(category)
        if not homset_supercategories:
            return Homsets()
        return Category.join(homset_supercategories)

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
        if base_category in Cat().JoinCategories():
            object_names = " and ".join(category._repr_object_names() for category in base_category.super_categories())
        else:
            object_names = base_category._repr_object_names()
        return f"homsets of {object_names}"


__all__ = [
    "Homsets",
    "HomsetsCategory",
    "HomsetsOf",
    "UniversalHomsetElementMethods",
    "UniversalHomsetObjectMethods",
]
