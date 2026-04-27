"""Homset/endset/autset layer for ``Rings()``."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.groups import Groups as SageGroups
from sage.categories.homsets import HomsetsCategory
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..homsets.utils import refine_automorphism_set_from_endset
from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import Ideal, Ring, RingAutset, RingEndset, RingMorphism


class _RingHomsetObjects:
    @abstract_method
    def domain(self) -> Ring: ...

    @abstract_method
    def codomain(self) -> Ring: ...

    @abstract_method
    def __call__(self, *args, **kwds) -> RingMorphism: ...

    @abstract_method
    def __contains__(self, obj: RingMorphism) -> bool: ...


class _RingHomomorphisms:
    @abstract_method
    def domain(self) -> Ring: ...

    @abstract_method
    def codomain(self) -> Ring: ...

    @abstract_method
    def image(self, I: Ideal | None = None) -> Ideal: ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    @abstract_method
    def is_endomorphism(self) -> bool: ...

    @abstract_method
    def is_identity(self) -> bool: ...

    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def kernel(self) -> Ideal: ...

    @abstract_method
    def section(self) -> RingMorphism: ...

    @abstract_method
    def pre_compose(self, other: RingMorphism) -> RingMorphism: ...

    @abstract_method
    def post_compose(self, other: RingMorphism) -> RingMorphism: ...


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
    ElementMethods = _RingHomomorphisms
    Endset = LazyImport(__name__, "_Endsets")
    Autset = LazyImport(__name__, "_Autsets")


class _Endsets(CategoryWithAxiom):
    _base_category_class_and_axiom = (RingHomsets, "Endset")
    Autset = LazyImport(__name__, "_Autsets")

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
    _base_category_class_and_axiom = (RingHomsets, "Autset")

    def extra_super_categories(self):
        return [self.base_category().Endset(), SageGroups(), SageSets()]

    @classmethod
    def from_endset(cls, endset: RingEndset) -> RingAutset:
        return refine_automorphism_set_from_endset(endset, cls())

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
