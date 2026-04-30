r"""Homset, endset, and autset categories for topological spaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutsets, GenericEndsets, Homsets, HomsetsOf

if TYPE_CHECKING:
    from ..types import TopologicalSpace


class _TopologicalHomsetObjects:
    r"""Topological homset parent methods; generic homset methods are inherited."""


class _ContinuousMaps:
    @abstract_method
    def is_continuous(self) -> bool: ...

    @abstract_method
    def preimage(self, subset: TopologicalSpace) -> TopologicalSpace: ...


class _Homeomorphisms:
    @final
    def is_homeomorphism(self) -> bool:
        return True


class TopologicalSpaceHomsets(HomsetsOf):
    r"""Category of homsets whose elements are continuous maps."""

    @final
    def extra_super_categories(self):
        return [Homsets().Of(self.base_category())]

    ParentMethods = _TopologicalHomsetObjects
    ElementMethods = _ContinuousMaps
    class MorphismMethods: ...

    Endset = LazyImport(__name__, "_TopologicalEndsets")


class _TopologicalEndsets(GenericEndsets):
    _functor_category = "Endset"
    _base_category_class_and_axiom = (TopologicalSpaceHomsets, "Endset")
    Autset = LazyImport(__name__, "_TopologicalAutsets")

    class ParentMethods:
        @abstract_method
        def base_space(self) -> TopologicalSpace: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class _TopologicalAutsets(GenericAutsets):
    _functor_category = "Autset"
    _base_category_class_and_axiom = (_TopologicalEndsets, "Autset")

    class ParentMethods: ...
    ElementMethods = _Homeomorphisms
    class MorphismMethods: ...
