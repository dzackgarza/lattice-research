r"""Universal subcategory-method surface for objects of ``Cat()``.

Every ordinary project category is an object of ``Cat()``.  This file is the
single shared source for construction selectors that all such category objects
receive through their ``SubcategoryMethods`` provider.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from ..types import Category, CategoryObject, CategoryOfAutsets, CategoryOfEndsets, CategoryOfHomsets


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

    @cached_method
    @final
    def Subobjects(self) -> Category:
        from .base_category_types import SubobjectsCategory

        return SubobjectsCategory.category_of(self)

    Subsets = Subobjects

    @cached_method
    @final
    def Quotients(self) -> Category:
        from .base_category_types import QuotientsCategory

        return QuotientsCategory.category_of(self)

    @cached_method
    @final
    def Subquotients(self) -> Category:
        from .base_category_types import SubquotientsCategory

        return SubquotientsCategory.category_of(self)

    @cached_method
    @final
    def ObjectsOver(self, structure_object: CategoryObject) -> Category:
        from .subcategories.constructions.objects_over import _ObjectsOver

        return _ObjectsOver.category_of(self, structure_object)

    @cached_method
    @final
    def ObjectsUnder(self, structure_object: CategoryObject) -> Category:
        from .subcategories.constructions.objects_under import _ObjectsUnder

        return _ObjectsUnder.category_of(self, structure_object)

    Slice = ObjectsOver
    Coslice = ObjectsUnder

    @cached_method
    @final
    def CartesianProducts(self) -> Category:
        from .base_category_types import CartesianProductsCategory

        return CartesianProductsCategory.category_of(self)

    @cached_method
    @final
    def Homsets(self) -> CategoryOfHomsets:
        from .base_category_types import HomsetsCategory

        return HomsetsCategory.category_of(self)

    @cached_method
    @final
    def Endsets(self) -> CategoryOfEndsets:
        return self.Homsets().Endset()

    @cached_method
    @final
    def Autsets(self) -> CategoryOfAutsets:
        return self.Endsets().Autset()

    @cached_method
    @final
    def Hom(self) -> CategoryOfHomsets:
        return self.Homsets()

    @cached_method
    @final
    def End(self) -> CategoryOfEndsets:
        return self.Endsets()

    @cached_method
    @final
    def Aut(self) -> CategoryOfAutsets:
        return self.Autsets()


__all__ = ["UniversalSubcategoryMethods"]
