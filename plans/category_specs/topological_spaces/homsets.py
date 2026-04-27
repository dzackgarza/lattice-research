r"""Homset, endset, and autset categories for topological spaces."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, overload

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category
from ..homsets import GenericAutsets, GenericEndsets, Homsets, HomsetsOf

if TYPE_CHECKING:
    from ..types import CategoryElement, TopologicalSpace, TopologicalSpaceMorphism


class _TopologicalHomsetObjects:
    r"""Topological homset parent methods; generic homset methods are inherited."""


class _ContinuousMaps:
    @abstract_method
    def is_continuous(self) -> bool: ...

    @abstract_method
    def preimage(self, subset: TopologicalSpace) -> TopologicalSpace: ...


class _Homeomorphisms:
    def is_homeomorphism(self) -> bool:
        return True


class TopologicalSpaceHomsets(HomsetsOf):
    r"""Category of homsets whose elements are continuous maps."""

    def extra_super_categories(self):
        return [Homsets().Of(self.base_category())]

    class SubcategoryMethods:
        @cached_method
        def Endset(self) -> Category:
            return self._with_axiom("Endset")

        @cached_method
        def Autset(self) -> Category:
            return self._with_axiom("Autset")

    ParentMethods = _TopologicalHomsetObjects
    ElementMethods = _ContinuousMaps
    Endset = LazyImport(__name__, "_TopologicalEndsets")
    Autset = LazyImport(__name__, "_TopologicalAutsets")


class _TopologicalEndsets(GenericEndsets):
    _functor_category = "Endset"
    _base_category_class_and_axiom = (TopologicalSpaceHomsets, "Endset")
    Autset = LazyImport(__name__, "_TopologicalAutsets")

    class ParentMethods:
        @abstract_method
        def base_space(self) -> TopologicalSpace: ...


class _TopologicalAutsets(GenericAutsets):
    _functor_category = "Autset"
    _base_category_class_and_axiom = (TopologicalSpaceHomsets, "Autset")

    ElementMethods = _Homeomorphisms
