r"""Registered re-exports of Sage category base classes.

This file is the single Sage-category touch point for the category-spec tree.
Other subtrees inherit these classes instead of inheriting directly from
``sage.categories.*`` base classes.
"""

from __future__ import annotations

import sys

from sage.cpython.getattr import dir_with_other_class
from sage.cpython.getattr import getattr_from_other_class
from sage.categories.category import Category as SageCategory
from sage.categories.category import CategoryWithParameters as SageCategoryWithParameters
from sage.categories.category_singleton import Category_singleton as SageCategorySingleton
from sage.categories.category_types import Category_ideal as SageCategoryIdeal
from sage.categories.category_types import Category_module as SageCategoryModule
from sage.categories.category_types import Category_over_base as SageCategoryOverBase
from sage.categories.category_types import Category_over_base_ring as SageCategoryOverBaseRing
from sage.categories.category_with_axiom import CategoryWithAxiom as SageCategoryWithAxiom
from sage.categories.category_with_axiom import (
    CategoryWithAxiom_over_base_ring as SageCategoryWithAxiomOverBaseRing,
)
from sage.categories.category_with_axiom import CategoryWithAxiom_singleton as SageCategoryWithAxiomSingleton
from sage.categories.homsets import Homsets as SageHomsets
from sage.categories.homsets import HomsetsCategory as SageHomsetsCategory
from sage.categories.homsets import HomsetsOf as SageHomsetsOf
from sage.misc.cachefunc import cached_method
from sage.misc.constant_function import ConstantFunction
from sage.structure.dynamic_class import DynamicMetaclass

_SageCategory = SageCategory
_SageCategoryWithParameters = SageCategoryWithParameters
_SageCategorySingleton = SageCategorySingleton
_SageCategoryIdeal = SageCategoryIdeal
_SageCategoryModule = SageCategoryModule
_SageCategoryOverBase = SageCategoryOverBase
_SageCategoryOverBaseRing = SageCategoryOverBaseRing
_SageCategoryWithAxiom = SageCategoryWithAxiom
_SageCategoryWithAxiomOverBaseRing = SageCategoryWithAxiomOverBaseRing
_SageCategoryWithAxiomSingleton = SageCategoryWithAxiomSingleton
_SageHomsets = SageHomsets
_SageHomsetsCategory = SageHomsetsCategory
_SageHomsetsOf = SageHomsetsOf


def _undynamic_category_class(category_cls: type) -> type:
    if isinstance(category_cls, DynamicMetaclass):
        return category_cls.__base__
    return category_cls


def _register_category_class_from_classcall(category_cls: type[SageCategory]) -> type[SageCategory]:
    category_cls = _undynamic_category_class(category_cls)
    cat_module = sys.modules.get(__package__)
    cat_cls = getattr(cat_module, "Cat", None)
    if cat_cls is not None and issubclass(category_cls, SageCategory):
        cat_cls.register_category(category_cls)
    return category_cls


class _RegisteredCategoryObjectMixin:
    r"""Mixin making wrapped category instances objects of ``Cat()``."""

    def category(self):
        cat_module = sys.modules.get(__package__)
        cat_cls = getattr(cat_module, "Cat", None)
        if cat_cls is not None and cat_cls._is_registered_category_object(self):
            return cat_cls()
        return SageCategory.category(self)

    def __getattr__(self, name: str):
        try:
            return getattr_from_other_class(self, self.category().parent_class, name)
        except AttributeError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'") from None

    def __dir__(self):
        return dir_with_other_class(self, self.category().parent_class)


class _Category(_RegisteredCategoryObjectMixin, SageCategory):
    r"""Registered re-export of Sage's ``Category`` base class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategory.__classcall__(cls, *args, **options)


class _CategoryWithParameters(_RegisteredCategoryObjectMixin, SageCategoryWithParameters):
    r"""Registered re-export of Sage's ``CategoryWithParameters`` base class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryWithParameters.__classcall__(cls, *args, **options)


class _CategoryWithAxiom(_RegisteredCategoryObjectMixin, SageCategoryWithAxiom):
    r"""Registered re-export of Sage's ``CategoryWithAxiom`` base class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryWithAxiom.__classcall__(cls, *args, **options)

    def __init__(self, base_category) -> None:
        if isinstance(base_category, SageCategorySingleton) and not isinstance(self, CategoryWithAxiom_singleton):
            cls = self.__class__
            assert cls.__base__ in (CategoryWithAxiom, SageCategoryWithAxiom)
            cls.__bases__ = (CategoryWithAxiom_singleton,) + cls.__bases__[1:]
        self._base_category = base_category
        SageCategory.__init__(self)


class _CategoryWithAxiom_over_base_ring(_RegisteredCategoryObjectMixin, SageCategoryWithAxiomOverBaseRing):
    r"""Registered re-export of Sage's base-ring axiom category class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryWithAxiomOverBaseRing.__classcall__(cls, *args, **options)


class _Category_over_base(_RegisteredCategoryObjectMixin, SageCategoryOverBase):
    r"""Registered re-export of Sage's ``Category_over_base`` class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryOverBase.__classcall__(cls, *args, **options)


class _Category_over_base_ring(_RegisteredCategoryObjectMixin, SageCategoryOverBaseRing):
    r"""Registered re-export of Sage's ``Category_over_base_ring`` class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryOverBaseRing.__classcall__(cls, *args, **options)


class _Category_module(_RegisteredCategoryObjectMixin, SageCategoryModule):
    r"""Registered re-export of Sage's module category base class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryModule.__classcall__(cls, *args, **options)


class _Category_ideal(_RegisteredCategoryObjectMixin, SageCategoryIdeal):
    r"""Registered re-export of Sage's ideal category base class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageCategoryIdeal.__classcall__(cls, *args, **options)


class _HomsetsCategory(_RegisteredCategoryObjectMixin, SageHomsetsCategory):
    r"""Registered re-export of Sage's homsets functorial category class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageHomsetsCategory.__classcall__(cls, *args, **options)


class _HomsetsOf(_RegisteredCategoryObjectMixin, SageHomsetsOf):
    r"""Registered re-export of Sage's ``HomsetsOf`` category class."""

    @staticmethod
    def __classcall__(cls, *args, **options):
        cls = _register_category_class_from_classcall(cls)
        return SageHomsetsOf.__classcall__(cls, *args, **options)


class _Homsets(_RegisteredCategoryObjectMixin, SageHomsets):
    r"""Registered re-export of Sage's singleton ``Homsets`` category."""

    @staticmethod
    def __classcall__(cls, *args):
        cls = _register_category_class_from_classcall(cls)
        assert (
            cls is Homsets
            or cls.__mro__[1] is Homsets
            or cls.__mro__[1] is CategoryWithAxiom_singleton
            or cls.__mro__[1] is SageHomsets
            or cls.__mro__[1] is SageCategoryWithAxiomSingleton
        ), f"{cls} is not a direct subclass of {Homsets}"
        obj = super(SageCategorySingleton, cls).__classcall__(cls, *args)
        cls._set_classcall(ConstantFunction(obj))
        obj.__class__._set_classcall(ConstantFunction(obj))
        return obj

    @cached_method
    def Endset(self):
        r"""Return Sage's existing root category of endomorphism sets."""
        return SageHomsets().Endset()


class _Category_singleton(_RegisteredCategoryObjectMixin, SageCategorySingleton):
    r"""Registered re-export of Sage's singleton category base class."""

    @staticmethod
    def __classcall__(cls, *args):
        cls = _register_category_class_from_classcall(cls)
        assert (
            cls is Category_singleton
            or cls.__mro__[1] is Category_singleton
            or cls.__mro__[1] is CategoryWithAxiom_singleton
            or cls.__mro__[1] is SageCategoryWithAxiomSingleton
        ), f"{cls} is not a direct subclass of {Category_singleton}"
        obj = super(SageCategorySingleton, cls).__classcall__(cls, *args)
        cls._set_classcall(ConstantFunction(obj))
        obj.__class__._set_classcall(ConstantFunction(obj))
        return obj


class _CategoryWithAxiom_singleton(_Category_singleton, _CategoryWithAxiom):
    r"""Registered re-export of Sage's singleton category-with-axiom base."""


Category = _Category
CategoryWithParameters = _CategoryWithParameters
CategoryWithAxiom = _CategoryWithAxiom
CategoryWithAxiom_singleton = _CategoryWithAxiom_singleton
CategoryWithAxiom_over_base_ring = _CategoryWithAxiom_over_base_ring
Category_over_base = _Category_over_base
Category_over_base_ring = _Category_over_base_ring
Category_module = _Category_module
Category_ideal = _Category_ideal
HomsetsCategory = _HomsetsCategory
HomsetsOf = _HomsetsOf
Homsets = _Homsets
Category_singleton = _Category_singleton


__all__ = [
    "Category",
    "CategoryWithAxiom",
    "CategoryWithAxiom_singleton",
    "CategoryWithAxiom_over_base_ring",
    "CategoryWithParameters",
    "Category_ideal",
    "Category_module",
    "Category_over_base",
    "Category_over_base_ring",
    "Category_singleton",
    "Homsets",
    "HomsetsCategory",
    "HomsetsOf",
]
