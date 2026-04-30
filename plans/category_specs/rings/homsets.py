"""Homset/endset/autset layer for ``Rings()``."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category
from ..homsets import GenericAutsets, GenericEndsets, Homsets, HomsetsOf
from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import Ideal, Ring, RingAutset, RingEndset, RingHomset, RingMorphism


class _RingHomsetObjects:
    r"""Ring-specific homset parent methods; generic homset methods are inherited."""


class _RingHomomorphisms:
    @abstract_method
    def is_zero(self) -> bool: ...

    @abstract_method
    def kernel(self) -> Ideal: ...

    @abstract_method
    def section(self) -> RingMorphism: ...


class _RingEndomorphisms:
    r"""Ring-specific endomorphism methods; generic endomorphism methods are inherited."""


class _RingAutomorphisms:
    r"""Ring-specific automorphism methods; generic automorphism methods are inherited."""


class RingHomsets(HomsetsOf):
    @classmethod
    @final
    def from_sage_homset(cls, homset: RingHomset) -> RingHomset:
        from . import Rings

        return refine_category(homset, Rings().Homsets())

    @final
    def extra_super_categories(self):
        return [Homsets().Of(self.base_category())]

    class SubcategoryMethods:
        @cached_method
        @final
        def Endset(self) -> Category:
            return self._with_axiom("Endset")

        @cached_method
        @final
        def Autset(self) -> Category:
            return self.Endset().Autset()

    ParentMethods = _RingHomsetObjects
    ElementMethods = _RingHomomorphisms
    Endset = LazyImport(__name__, "_Endsets")


class _Endsets(GenericEndsets):
    _functor_category = "Endset"
    _base_category_class_and_axiom = (RingHomsets, "Endset")
    Autset = LazyImport(__name__, "_Autsets")

    @classmethod
    @final
    def from_sage_endset(cls, endset: RingEndset) -> RingEndset:
        from . import Rings

        return refine_category(endset, Rings().Homsets().Endset())

    class ParentMethods:
        @abstract_method
        def base_ring(self) -> Ring:
            """If this is End(R), return R."""
            ...

        @final
        def unit_group(self) -> RingAutset:
            return self.Aut()

    ElementMethods = _RingEndomorphisms


class _Autsets(GenericAutsets):
    _functor_category = "Autset"
    _base_category_class_and_axiom = (_Endsets, "Autset")

    class ParentMethods:
        @final
        def base_ring(self) -> Ring:
            return self.endset().base_ring()

        @final
        def unit_group(self) -> RingAutset:
            return self

    ElementMethods = _RingAutomorphisms
