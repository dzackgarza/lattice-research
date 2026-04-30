r"""Hom categories and morphism method surfaces."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, final, overload

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.structure.dynamic_class import DynamicMetaclass

from sage.structure.parent import Parent

from ..cat import Cat, Category, CategoryWithParameters, FunctorialConstructionCategory, Homsets as SageHomsetsBase, _SageCategory

if TYPE_CHECKING:
    from ..types import CategoryElement, CategoryObject, Hom, Morphism


def _base_class(cls: type) -> type:
    if isinstance(cls, DynamicMetaclass):
        return cls.__base__
    return cls


class UniversalHomObjectMethods:
    r"""Methods on objects ``Hom_C(A, B)`` of a hom category."""

    @abstract_method
    def domain(self) -> CategoryObject: ...

    @abstract_method
    def codomain(self) -> CategoryObject: ...

    @final
    def is_endomorphism_set(self) -> bool:
        return self.domain() == self.codomain()

    @overload
    def __call__(self, morphism: Morphism) -> Morphism: ...

    @overload
    def __call__(self, function: Callable[[CategoryElement], CategoryElement]) -> Morphism: ...

    @abstract_method
    def __call__(self, data: Morphism | Callable[[CategoryElement], CategoryElement]) -> Morphism: ...


class UniversalHomElementMethods:
    r"""Methods on elements ``f`` of hom categories."""

    @final
    def domain(self) -> CategoryObject:
        return self.parent().domain()

    @final
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

    @final
    def is_endomorphism(self) -> bool:
        return self.domain() == self.codomain()

    @final
    def is_identity(self) -> bool:
        return self.is_endomorphism() and self == self.parent().identity()

    @abstract_method
    def is_invertible(self) -> bool: ...

    @abstract_method
    def is_isomorphism(self) -> bool:
        ...

    @final
    def is_automorphism(self) -> bool:
        return self.is_endomorphism() and self.is_invertible()


class HomCategory(SageHomsetsBase):
    r"""Category of all hom categories."""

    def super_categories(self) -> list[Category]:
        return super().super_categories()

    class SubcategoryMethods:
        @cached_method
        @final
        def EndCategory(self) -> Category:
            return self._with_axiom("Endset")

        @cached_method
        @final
        def AutCategory(self) -> Category:
            return self.EndCategory().AutCategory()

    ParentMethods = UniversalHomObjectMethods
    ElementMethods = UniversalHomElementMethods
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport("category_specs.homsets.endsets", "EndCategory")


class HomCategoryConstruction(FunctorialConstructionCategory, CategoryWithParameters):
    r"""Functorial construction category for ``C.HomCategory()``."""

    _functor_category = "HomCategory"
    _base_category_class = (_SageCategory,)

    class SubcategoryMethods:
        @cached_method
        @final
        def EndCategory(self) -> Category:
            return self._with_axiom("Endset")

        @cached_method
        @final
        def AutCategory(self) -> Category:
            return self.EndCategory().AutCategory()

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

    @final
    def Of(self, domain: CategoryObject, codomain: CategoryObject) -> Hom:
        r"""Return ``Hom_C(domain, codomain)`` for ``C = self.base_category()``."""
        category = self.base_category()
        assert domain in category, "domain must be an object of the base category"
        assert codomain in category, "codomain must be an object of the base category"
        return Parent.Hom(domain, codomain, category=category)

    @classmethod
    @final
    def default_super_categories(cls, category: Category) -> Category:
        r"""Return hom-category supercategories without repeating one construction.

        Sage's hom construction is deliberately not handled like an
        ordinary covariant functor: its own
        ``HomsetsCategory.default_super_categories`` first looks at full
        supercategories, and otherwise falls back to the generic
        ``HomCategoryOf`` stub.  That distinction matters here because the Cat
        wrapper layer makes ``HomCategory`` a universal construction method on
        every project category object.  If we naively recurse through every
        supercategory after that rewrite, a chain such as
        ``Modules(R).OverPID() -> OverDedekind() -> OverIntegralDomain() ->
        Modules(R)`` contributes four different dynamic
        ``RModuleHomCategory.parent_class`` and ``RModuleHomCategory.element_class``
        providers.  Each provider declares the same abstract module-hom
        requirements, so the resulting mixed classes re-declare the same spec
        surface several times.

        The mathematical relation we need is weaker and cleaner: keep hom-category
        supercategories that use a genuinely different construction class
        (for example ``Sets().HomCategory()`` under module hom categories), but collapse
        intermediate supercategories whose hom categories are again the same local
        construction.  The base category itself can still appear through
        ``extra_super_categories`` where a concrete hom category, such as
        ``RModuleHomCategory``, declares that its objects are also modules.
        """
        construction_class = _base_class(cls)
        if construction_class is HomCategoryOf:
            return HomCategory()

        hom_supercategories = []
        hom_supercategory_ids = set()
        seen_category_ids = set()

        def collect_supercategory_hom_categories(base_category: Category) -> None:
            for super_category in base_category.super_categories():
                if id(super_category) in seen_category_ids:
                    continue
                seen_category_ids.add(id(super_category))
                hom_category = super_category.HomCategory()
                if _base_class(hom_category.__class__) is construction_class:
                    collect_supercategory_hom_categories(super_category)
                    continue
                if id(hom_category) in hom_supercategory_ids:
                    continue
                hom_supercategories.append(hom_category)
                hom_supercategory_ids.add(id(hom_category))

        collect_supercategory_hom_categories(category)
        if not hom_supercategories:
            return HomCategory()
        return Category.join(hom_supercategories)

    def _make_named_class_key(self, name: str):
        return getattr(self.base_category(), name)


class HomCategoryOf(HomCategoryConstruction):
    r"""Generic category whose objects are ``Hom_C(A, B)``."""

    # This is the category-level construction for a category C:
    # C.HomCategory() is the category whose objects are Hom_C(A, B).
    # Its Of(A, B) constructor evaluates the construction at objects A, B.
    # It does not define
    # set-map-only predicates such as injectivity.

    def _repr_object_names(self) -> str:
        base_category = self.base_category()
        if base_category in Cat().JoinCategories():
            object_names = " and ".join(category._repr_object_names() for category in base_category.super_categories())
        else:
            object_names = base_category._repr_object_names()
        return f"hom categories of {object_names}"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
