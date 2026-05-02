r"""Hom categories internal to ``Cat()``.

Morphisms in ``Cat()`` are functors between categories.  Sage already has a
substantial functor and construction-functor implementation; this file only
declares the category-spec surface that will wrap that machinery.
"""

from __future__ import annotations

from typing import Any, final

from sage.categories.functor import Functor
from sage.categories.pushout import ConstructionFunctor
from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import HomCategoryOf
from . import Category


class _CatHomCategoryObjectMethods:
    @abstract_method
    def __call__(self, functor: Functor) -> Functor: ...

    @abstract_method
    def __contains__(self, functor: Any) -> bool: ...


class _CatFunctorMethods:
    @abstract_method
    def __call__(self, category: Category) -> Category: ...

    @abstract_method
    def _coerce_into_domain(self, category: Category) -> Category: ...

    @abstract_method
    def _apply_functor(self, category: Category) -> Category: ...

    @abstract_method
    def _apply_functor_to_morphism(self, functor: Functor) -> Functor: ...


class _CatConstructionFunctorMethods(_CatFunctorMethods):
    r"""Sage ``ConstructionFunctor`` surface for actual functors.

    These methods come from ``sage.categories.pushout.ConstructionFunctor``.
    They are not methods on Sage ``FunctorialConstructionCategory`` objects
    such as ``C.Subobjects()``; those are category objects, not callable
    functors between category objects.
    """

    coercion_reversed: bool = False

    @abstract_method
    def pushout(self, other: ConstructionFunctor) -> ConstructionFunctor: ...

    @abstract_method
    def merge(self, other: ConstructionFunctor) -> ConstructionFunctor | None: ...

    @abstract_method
    def commutes(self, other: ConstructionFunctor) -> bool: ...

    @abstract_method
    def expand(self) -> list[ConstructionFunctor]: ...

    @abstract_method
    def common_base(self, other_functor: ConstructionFunctor, self_bases, other_bases): ...


class CatHomCategory(HomCategoryOf):
    r"""Hom category of functors between categories.

    Canonical chain: ``Cat().HomCategory()``.
    """

    @final
    def __init__(self, base_category: Category) -> None:
        super().__init__(base_category)

    @classmethod
    @final
    def category_of(cls, base_category: Category) -> CatHomCategory:
        return cls(base_category)

    @final
    def _repr_object_names(self) -> str:
        return f"functor hom categories internal to {self.base_category()}"

    @final
    def extra_super_categories(self) -> list[Category]:
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _CatHomCategoryObjectMethods
    ElementMethods = _CatFunctorMethods
    class MorphismMethods: ...

    ConstructionFunctorMethods = _CatConstructionFunctorMethods
    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport("category_specs.cat.endsets", "CatEndCategory")


SageFunctor = Functor
SageConstructionFunctor = ConstructionFunctor
