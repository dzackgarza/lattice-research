r"""Category of categories.

This subtree introduces ``Cat()`` as the singleton category whose objects are
ordinary 1-categories.  It is deliberately small: the immediate goal is to
standardize category-object vocabulary and common boilerplate, not to build a
full subcategory hierarchy for categories.

``Cat()`` is the ambient category at this level.  It is not an object of
itself, and expressions such as ``Cat().Hom(Cat())`` are intentionally outside
this spec: those would be higher-categorical functors.  The Cat-backed wrapper
layer in ``base_category_types.py`` starts one level below this root, for
category objects such as ``Sets()``, ``Rings()``, and their subcategories.

Public surface:

```
Cat()
|-- join(...)
|-- meet(...)
|-- Constructors()
|   `-- EmptyCategory()
|-- Subobjects()
|-- Quotients()
|-- Subquotients()
|-- ObjectsOver()
|-- ObjectsUnder()
|-- CartesianProducts()
|-- JoinCategories()
`-- Homsets()
    |-- Endset()
    `-- Autset()
```
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, final

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.structure.category_object import CategoryObject as SageCategoryObject

from .base_category_types import (
    AlgebrasCategory,
    CartesianProductsCategory,
    Category,
    Category_ideal,
    Category_module,
    Category_over_base,
    Category_over_base_ring,
    Category_singleton,
    CategoryWithAxiom,
    CategoryWithAxiom_over_base_ring,
    CategoryWithAxiom_singleton,
    CategoryWithParameters,
    CovariantConstructionCategory,
    DualObjectsCategory,
    FilteredModulesCategory,
    FunctorialConstructionCategory,
    GradedModulesCategory,
    Homsets,
    HomsetsCategory,
    HomsetsOf,
    IsomorphicObjectsCategory,
    QuotientsCategory,
    RealizationsCategory,
    RegressiveCovariantConstructionCategory,
    SubobjectsCategory,
    SubquotientsCategory,
    SuperModulesCategory,
    TensorProductsCategory,
    WithRealizationsCategory,
    _make_named_class_with_cat_subcategory_methods,
    _SageCategory,
    _SageCategorySingleton,
)

if TYPE_CHECKING:
    from ..types import Autset, CategoryOfAutsets, CategoryOfEndsets, CategoryOfHomsets, Endset, Homset

class _CatObjectMethods:
    r"""Methods on objects of ``Cat()``, i.e. category objects."""

    # Object-level hom/end/aut selectors:
    # for a category object X in Cat(), X.Hom(Y), X.End(), and X.Aut()
    # are the parents Hom_Cat(X, Y), End_Cat(X), and Aut_Cat(X).

    @abstract_method
    def Hom(self, codomain: Category) -> Homset: ...

    @final
    def End(self) -> Endset:
        return self.Hom(self)

    @final
    def Aut(self) -> Autset:
        return self.End().Aut()

    @final
    def is_join_category(self) -> bool:
        from .join_categories import is_join_category

        return is_join_category(self)

    @final
    def leq(self, other: Category) -> bool:
        r"""Return whether ``self`` is a subcategory of ``other``."""
        return self.is_subcategory(other)

    @final
    def geq(self, other: Category) -> bool:
        r"""Return whether ``self`` contains ``other`` as a subcategory."""
        return other.is_subcategory(self)

    __le__ = leq
    __ge__ = geq


class _CategoryElementMethods:
    r"""Baseline element methods for objects internal to a category object."""


class Cat(_SageCategorySingleton):
    r"""Root category whose objects are project category objects.

    ``Cat`` deliberately does not use the Cat-backed wrapper bases.  The wrapper
    layer makes ordinary categories into objects of ``Cat()``; applying it to
    ``Cat`` itself would assert a self-membership statement and would turn
    ``Cat().Hom(Cat())`` into an apparent 1-categorical construction.  This spec
    does not model that higher level.

    For the same reason, ``Cat`` does not re-export the object-level
    ``leq``/``geq`` aliases from ``Cat.ParentMethods``.  Ordinary category
    objects may compare as Sage subcategories; the root ``Cat()`` object is not
    specified as an object comparable inside a larger modeled category.
    """

    @final
    def _make_named_class(self, name, method_provider, cache=False, picklable: bool = True):
        r"""Use the wrapper-layer universal subcategory-method injection.

        ``Cat`` cannot inherit from the Cat-backed wrapper bases because it is
        not an object of itself.  This override is therefore only a local opt-in
        to the same base-layer Sage integration used by ordinary wrapped
        categories.
        """
        return _make_named_class_with_cat_subcategory_methods(
            self,
            super()._make_named_class,
            name,
            method_provider,
            cache=cache,
            picklable=picklable,
        )

    @final
    def __contains__(self, candidate: Any) -> bool:
        from .join_categories import is_join_category

        if candidate is self:
            return False
        if is_join_category(candidate):
            return True
        if isinstance(candidate, SageCategoryObject):
            return candidate.category().is_subcategory(self)
        return False

    @final
    def join(self, categories: Iterable[Category]) -> Category:
        r"""Return Sage's category-lattice join of ``categories``."""
        return _SageCategory.join(categories)

    @final
    def meet(self, categories: Iterable[Category]) -> Category:
        r"""Return Sage's category-lattice meet of ``categories``.

        Sage intentionally leaves the empty meet unimplemented.  The Cat
        subtree has an explicit bottom object, so the empty meet is the local
        ``EmptyCategory()``.
        """
        categories = tuple(categories)
        if not categories:
            return self.Constructors().EmptyCategory()
        return _SageCategory.meet(categories)

    @final
    def super_categories(self) -> list:
        return []

    @final
    def additional_structure(self):
        return None

    class SubcategoryMethods:
        r"""Category-level construction methods supplied by Sage's machinery."""

        @cached_method
        @final
        def JoinCategories(self) -> Category:
            from .join_categories import JoinCategories

            return JoinCategories()

    ParentMethods = _CatObjectMethods
    ElementMethods = _CategoryElementMethods
    Subobjects = LazyImport("category_specs.cat.subcategories.constructions.subobjects", "_Subobjects")
    Quotients = LazyImport("category_specs.cat.subcategories.constructions.quotients", "_Quotients")
    Subquotients = LazyImport("category_specs.cat.subcategories.constructions.subquotients", "_Subquotients")
    ObjectsOver = LazyImport("category_specs.cat.subcategories.constructions.objects_over", "_ObjectsOver")
    ObjectsUnder = LazyImport("category_specs.cat.subcategories.constructions.objects_under", "_ObjectsUnder")
    CartesianProducts = LazyImport(
        "category_specs.cat.subcategories.constructions.cartesian_products",
        "_CartesianProducts",
    )
    Homsets = LazyImport("category_specs.cat.homsets", "CatHomsets")
    JoinCategories = LazyImport("category_specs.cat.join_categories", "JoinCategories")
    EmptyCategory = LazyImport("category_specs.cat.empty_category", "EmptyCategory")

    class Constructors:
        r"""Category-object constructor entry points."""

        @final
        def __repr__(self) -> str:
            return "Cat constructors"

        @final
        def EmptyCategory(self) -> Category:
            r"""Return the bottom category object for the local ``Cat()`` hierarchy."""
            from .empty_category import EmptyCategory

            return EmptyCategory()


Categories = Cat
