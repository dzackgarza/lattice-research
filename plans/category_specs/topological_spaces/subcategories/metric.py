r"""Metric spaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import _TopologicalSpaces
from ..homsets import MetricSpaceHomCategory

if TYPE_CHECKING:
    from ...types import MetricBall, RealNumber, SetElement, SetMorphism


class _MetricSpaceObjectMethods:
    r"""Methods on metric spaces."""

    @final
    def is_metric(self) -> bool:
        return True

    @abstract_method
    def metric(self) -> SetMorphism:
        r"""Return the metric map ``d: X x X -> RR``."""
        ...

    @abstract_method
    def ball(self, center: SetElement, radius: RealNumber) -> MetricBall: ...

    @abstract_method
    def dist(self, x: SetElement, y: SetElement) -> RealNumber: ...


class _MetricSpaceElementMethods:
    r"""Methods on points of metric spaces."""

    @final
    def dist(self, other: SetElement) -> RealNumber:
        return self.parent().dist(self, other)


class _MetricSpaces(CategoryWithAxiom):
    r"""Category of metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric()``.
    """

    _base_category_class_and_axiom = (_TopologicalSpaces, "Metric")
    ParentMethods = _MetricSpaceObjectMethods
    ElementMethods = _MetricSpaceElementMethods
    HomCategory = MetricSpaceHomCategory
    Complete = LazyImport("category_specs.topological_spaces.subcategories.complete", "_CompleteMetricSpaces")

    @final
    def _repr_object_names(self) -> str:
        return "metric spaces"

    @final
    def super_categories(self) -> list[Category]:
        return [SageSets().Metric(), _TopologicalSpaces()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Complete(self) -> Category:
            return self._with_axiom("Complete")

    class MorphismMethods: ...
