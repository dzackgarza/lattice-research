r"""Homsets internal to ``Cat()``.

Morphisms in ``Cat()`` are functors between categories.  Sage already has a
substantial functor and construction-functor implementation; this file only
declares the category-spec surface that will wrap that machinery.
"""

from __future__ import annotations

from typing import Any, final

from sage.categories.functor import Functor
from sage.categories.pushout import ConstructionFunctor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..homsets import HomsetsOf
from . import Category


class _CatHomsetObjectMethods:
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


class CatHomsets(HomsetsOf):
    r"""Homsets of functors between categories."""

    @final
    def __init__(self, base_category: Category) -> None:
        super().__init__(base_category)

    @classmethod
    @final
    def category_of(cls, base_category: Category) -> CatHomsets:
        return cls(base_category)

    @final
    def _repr_object_names(self) -> str:
        return f"functor homsets internal to {self.base_category()}"

    class SubcategoryMethods:
        @cached_method
        @final
        def Endset(self) -> Category:
            return self._with_axiom("Endset")

        @cached_method
        @final
        def Autset(self) -> Category:
            return self.Endset().Autset()

    ParentMethods = _CatHomsetObjectMethods
    ElementMethods = _CatFunctorMethods
    ConstructionFunctorMethods = _CatConstructionFunctorMethods
    Endset = LazyImport("category_specs.cat.endsets", "CatEndsets")


SageFunctor = Functor
SageConstructionFunctor = ConstructionFunctor
