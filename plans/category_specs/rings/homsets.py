"""Homset/endset/autset layer for ``Rings()``."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.groups import Groups as SageGroups
from sage.categories.homsets import HomsetsCategory
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import Ring, RingAutset, RingEndset, RingMorphism


class _RingHomsetObjects:
    @abstract_method
    def domain(self) -> Ring: ...

    @abstract_method
    def codomain(self) -> Ring: ...

    @abstract_method
    def __call__(self, *args, **kwds) -> RingMorphism: ...

    @abstract_method
    def __contains__(self, obj: RingMorphism) -> bool: ...


class _RingEndomorphisms:
    @abstract_method
    def is_invertible(self) -> bool: ...

    @abstract_method
    def inverse(self) -> RingMorphism: ...


class _RingAutomorphisms:
    def is_invertible(self) -> bool:
        return True

    @abstract_method
    def inverse(self) -> RingMorphism: ...


class _Endsets(CategoryWithAxiom):
    def extra_super_categories(self):
        from . import Rings

        return [SageSets(), Rings()]

    @classmethod
    def from_sage_endset(cls, endset: RingEndset) -> RingEndset:
        from . import Rings

        return refine_category(endset, Rings().Homsets().Endset())

    class ParentMethods:
        @abstract_method
        def base_ring(self) -> Ring:
            """If this is End(R), return R."""
            ...

        def Aut(self) -> RingAutset:
            from . import Rings

            return Rings().Autsets().from_endset(self)

        def unit_group(self) -> RingAutset:
            return self.Aut()

        @abstract_method
        def identity(self) -> RingMorphism: ...

    ElementMethods = _RingEndomorphisms


class _Autsets(CategoryWithAxiom):
    def extra_super_categories(self):
        return [self.base_category().Endset(), SageGroups(), SageSets()]

    @classmethod
    def from_endset(cls, endset: RingEndset) -> RingAutset:
        from sage.sets.condition_set import ConditionSet as SageConditionSet

        autset = SageConditionSet(endset, lambda f: f.is_invertible())
        return refine_category(autset, cls())

    class ParentMethods:
        def base_ring(self) -> Ring:
            return self.endset().base_ring()

        def domain(self) -> Ring:
            return self.endset().domain()

        def codomain(self) -> Ring:
            return self.endset().codomain()

        def __call__(self, *args, **kwds) -> RingMorphism:
            return self.endset()(*args, **kwds)

        def __contains__(self, f: RingMorphism) -> bool:
            return f in self.endset() and f.is_invertible()

        def endset(self) -> RingEndset:
            if hasattr(self, "universe"):
                return self.universe()
            return self._universe

        def identity(self) -> RingMorphism:
            return self.endset().identity()

        def Aut(self) -> RingAutset:
            return self

        def unit_group(self) -> RingAutset:
            return self

    ElementMethods = _RingAutomorphisms


_Endsets.Autset = _Autsets


class RingHomsets(HomsetsCategory):
    @classmethod
    def from_sage_homset(cls, homset):
        from . import Rings

        return refine_category(homset, Rings().Homsets())

    def extra_super_categories(self):
        return [SageSets()]

    class SubcategoryMethods:
        @cached_method
        def Endset(self):
            return self._with_axiom("Endset")

        @cached_method
        def Autset(self):
            return self._with_axiom("Autset")

    ParentMethods = _RingHomsetObjects
    Endset = _Endsets
    Autset = _Autsets


_Endsets._base_category_class_and_axiom = (RingHomsets, "Endset")
_Autsets._base_category_class_and_axiom = (RingHomsets, "Autset")
