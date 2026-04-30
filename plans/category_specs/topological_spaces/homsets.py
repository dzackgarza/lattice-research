r"""Hom, end, and aut categories for topological spaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import TopologicalSpace


class _TopologicalHomCategoryObjectMethods:
    r"""Topological hom parent methods; generic hom methods are inherited."""


class _ContinuousMaps:
    @abstract_method
    def is_continuous(self) -> bool: ...

    @abstract_method
    def preimage(self, subset: TopologicalSpace) -> TopologicalSpace: ...


class _Homeomorphisms:
    @final
    def is_homeomorphism(self) -> bool:
        return True


class TopologicalSpaceHomCategory(HomCategoryOf):
    r"""Category of homs whose elements are continuous maps."""

    @final
    def extra_super_categories(self):
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _TopologicalHomCategoryObjectMethods
    ElementMethods = _ContinuousMaps
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "TopologicalSpaceEndCategory")


class TopologicalSpaceEndCategory(GenericEndCategory):
    _base_category_class_and_axiom = (TopologicalSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "TopologicalSpaceAutCategory")

    class ParentMethods:
        @abstract_method
        def base_space(self) -> TopologicalSpace: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class TopologicalSpaceAutCategory(GenericAutCategory):
    _base_category_class_and_axiom = (TopologicalSpaceEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _Homeomorphisms
    class MorphismMethods: ...
