r"""Universal subcategory-method surface for objects of ``Cat()``.

Every ordinary project category is an object of ``Cat()``.  This file is the
single shared source for construction selectors that all such category objects
receive through their ``SubcategoryMethods`` provider.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, cast, final

from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from ..types import (
        Category,
        CategoryObject,
        CategoryOfAutCategories,
        CategoryOfEndCategories,
        CategoryOfHomCategories,
    )


def _cat_cached_method[_SubcategoryMethod: Callable[..., object]](
    method: _SubcategoryMethod,
) -> _SubcategoryMethod:
    return cast(_SubcategoryMethod, cached_method(method))


class UniversalSubcategoryMethods:
    r"""Universal construction selectors for category objects in ``Cat()``.

    Sage mixes ``SubcategoryMethods`` into the dynamic class of category
    instances, not into parents or elements.  Since every ordinary project
    category is an object of ``Cat()``, these methods are the shared categorical
    construction surface for all such objects.

    Individual category classes still declare the construction category class,
    e.g. ``Sets.Subobjects = _Subobjects`` or
    ``Modules.Subobjects = _Subobjects``.  Those classes carry the
    category-specific parent/element/morphism requirements.  The selectors
    here only perform the universal operation already used throughout the
    specs: call ``SomeConstruction.category_of(self)``.
    """

    @final
    def _category_self(self) -> Category:
        return cast("Category", self)

    @_cat_cached_method
    @final
    def Subobjects(self) -> Category:
        r"""Return the subobject construction category of this category."""
        from .base_category_types import SubobjectsCategory

        return SubobjectsCategory.category_of(self._category_self())

    Subsets = Subobjects

    @_cat_cached_method
    @final
    def Quotients(self) -> Category:
        r"""Return the quotient-object construction category of this category."""
        from .base_category_types import QuotientsCategory

        return QuotientsCategory.category_of(self._category_self())

    @_cat_cached_method
    @final
    def Subquotients(self) -> Category:
        r"""Return the subquotient construction category of this category."""
        from .base_category_types import SubquotientsCategory

        return SubquotientsCategory.category_of(self._category_self())

    @_cat_cached_method
    @final
    def ObjectsOver(self, structure_object: CategoryObject) -> Category:
        r"""Return the category of objects over ``structure_object``."""
        from .subcategories.constructions.objects_over import _ObjectsOver

        return _ObjectsOver.category_of(self._category_self(), structure_object)

    @_cat_cached_method
    @final
    def ObjectsUnder(self, structure_object: CategoryObject) -> Category:
        r"""Return the category of objects under ``structure_object``."""
        from .subcategories.constructions.objects_under import _ObjectsUnder

        return _ObjectsUnder.category_of(self._category_self(), structure_object)

    Slice = ObjectsOver
    Coslice = ObjectsUnder

    @_cat_cached_method
    @final
    def CartesianProducts(self) -> Category:
        r"""Return the Cartesian-product construction category of this category."""
        from .base_category_types import CartesianProductsCategory

        return CartesianProductsCategory.category_of(self._category_self())

    @_cat_cached_method
    @final
    def HomCategory(self) -> CategoryOfHomCategories:
        r"""Return the hom-category construction over this category."""
        from ..homsets import HomCategoryConstruction

        return cast(
            "CategoryOfHomCategories",
            HomCategoryConstruction.category_of(self._category_self()),
        )

    @_cat_cached_method
    @final
    def Homsets(self) -> CategoryOfHomCategories:
        r"""Return Sage's homset spelling as an interop alias for ``HomCategory``."""
        return self.HomCategory()

    @_cat_cached_method
    @final
    def EndCategory(self) -> CategoryOfEndCategories:
        r"""Return the endomorphism-category construction over this category."""
        from ..homsets import HomCategory

        category = self._category_self()
        if category.is_subcategory(HomCategory()):
            return cast("CategoryOfEndCategories", category._with_axiom("Endset"))
        return cast(
            "CategoryOfEndCategories",
            category.HomCategory().EndCategory(),
        )

    @_cat_cached_method
    @final
    def Endsets(self) -> CategoryOfEndCategories:
        r"""Return Sage's endset spelling as an interop alias for ``EndCategory``."""
        return self.EndCategory()

    @_cat_cached_method
    @final
    def AutCategory(self) -> CategoryOfAutCategories:
        r"""Return the automorphism-category construction over this category."""
        category = self._category_self()
        if category.is_subcategory(category.EndCategory()):
            return cast("CategoryOfAutCategories", category._with_axiom("Autset"))
        return cast(
            "CategoryOfAutCategories",
            category.EndCategory().AutCategory(),
        )
