r"""Hom categories and morphism method surfaces."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, final, overload

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from sage.structure.parent import Parent

from ..cat import Cat, Category, FunctorialConstructionCategory, Homsets as SageHomsetsBase, _SageCategory

if TYPE_CHECKING:
    from ..types import CategoryElement, CategoryObject, Hom, Morphism


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


class HomCategoryConstruction(FunctorialConstructionCategory):
    r"""Functorial construction category for ``C.HomCategory()``.

    This is the project-owned functorial assignment ``Hom_*: Cat -> Cat``,
    sending ``C`` to ``Hom_C``.  Sage's ``HomsetsCategory`` is inventory
    and interop vocabulary here; it is not a source of mathematical method
    inheritance.  The Hom method surface is declared in this file and refined
    by subtree ``homsets.py`` files.
    """

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
        r"""Lift Cat-level supercategories through the hom-category construction."""
        hom_supercategories = [
            super_category.HomCategory()
            for super_category in category.super_categories()
            if super_category in Cat()
        ]
        if not hom_supercategories:
            return HomCategory()
        return Category.join(hom_supercategories)

class HomCategoryOf(HomCategoryConstruction):
    r"""Generic category whose objects are ``Hom_C(A, B)``."""

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport("category_specs.homsets.endsets", "EndCategoryOf")

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
