r"""Hom, end, and aut categories for topological spaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import MetricSpace, TopologicalSpace


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


class _ShortMaps(_ContinuousMaps):
    @final
    def is_short(self) -> bool:
        return True


class _Isometries:
    @final
    def is_isometry(self) -> bool:
        return True


class TopologicalSpaceHomCategory(HomCategoryOf):
    r"""Category of homs whose elements are continuous maps.

    Canonical chain: ``TopologicalSpaces().HomCategory()``.
    """

    @final
    def extra_super_categories(self):
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _TopologicalHomCategoryObjectMethods
    ElementMethods = _ContinuousMaps
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "TopologicalSpaceEndCategory")


class TopologicalSpaceEndCategory(GenericEndCategory):
    r"""Canonical chain: ``TopologicalSpaces().EndCategory()``."""
    _base_category_class_and_axiom = (TopologicalSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "TopologicalSpaceAutCategory")

    class ParentMethods:
        @abstract_method
        def base_space(self) -> TopologicalSpace: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class TopologicalSpaceAutCategory(GenericAutCategory):
    r"""Canonical chain: ``TopologicalSpaces().AutCategory()``."""
    _base_category_class_and_axiom = (TopologicalSpaceEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _Homeomorphisms
    class MorphismMethods: ...


class MetricSpaceHomCategory(TopologicalSpaceHomCategory):
    r"""Category of homs whose elements are short maps of metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric().HomCategory()``.
    """

    @final
    def extra_super_categories(self):
        return [TopologicalSpaceHomCategory(self.base_category())]

    ElementMethods = _ShortMaps

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "MetricSpaceEndCategory")


class MetricSpaceEndCategory(GenericEndCategory):
    r"""Canonical chain: ``TopologicalSpaces().Metric().EndCategory()``."""
    _base_category_class_and_axiom = (MetricSpaceHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "MetricSpaceAutCategory")

    class ParentMethods:
        @abstract_method
        def base_space(self) -> MetricSpace: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class MetricSpaceAutCategory(GenericAutCategory):
    r"""Canonical chain: ``TopologicalSpaces().Metric().AutCategory()``."""
    _base_category_class_and_axiom = (MetricSpaceEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _Isometries
    class MorphismMethods: ...
