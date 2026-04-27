r"""Homsets internal to ``Cat()``.

Morphisms in ``Cat()`` are functors between categories.  Sage already has a
substantial functor and construction-functor implementation; this file only
declares the category-spec surface that will wrap that machinery.
"""

from __future__ import annotations

from typing import Any

from sage.categories.functor import Functor
from sage.categories.pushout import ConstructionFunctor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from . import Category
from ..homsets import AutsetsOf, EndsetsOf, HomsetsOf


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


class _CatEndofunctorMethods(_CatFunctorMethods):
    def is_endofunctor(self) -> bool:
        return self.domain() == self.codomain()


class _CatAutofunctorMethods(_CatEndofunctorMethods):
    def is_autofunctor(self) -> bool:
        return True


class CatHomsets(HomsetsOf):
    r"""Homsets of functors between categories."""

    def __init__(self, base_category: Category) -> None:
        super().__init__(base_category)

    @classmethod
    def category_of(cls, base_category: Category) -> CatHomsets:
        return cls(base_category)

    def _repr_object_names(self) -> str:
        return f"functor homsets internal to {self.base_category()}"

    @cached_method
    def Endset(self) -> Category:
        return _CatEndsets(self.base_category())

    @cached_method
    def Autset(self) -> Category:
        return _CatAutsets(self.base_category())

    ParentMethods = _CatHomsetObjectMethods
    ElementMethods = _CatFunctorMethods
    ConstructionFunctorMethods = _CatConstructionFunctorMethods


class _CatEndsets(EndsetsOf):
    r"""Endofunctor sets of a category."""

    def _repr_object_names(self) -> str:
        return f"endofunctor sets internal to {self.base_category()}"

    @cached_method
    def Autset(self) -> Category:
        return _CatAutsets(self.base_category())

    ElementMethods = _CatEndofunctorMethods


class _CatAutsets(AutsetsOf):
    r"""Autofunctor sets of a category."""

    def _repr_object_names(self) -> str:
        return f"autofunctor sets internal to {self.base_category()}"

    ElementMethods = _CatAutofunctorMethods


SageFunctor = Functor
SageConstructionFunctor = ConstructionFunctor
