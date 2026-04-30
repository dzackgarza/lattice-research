r"""Metric spaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import _TopologicalSpaces

if TYPE_CHECKING:
    from ...types import MetricBall, RealNumber, SetElement


class _MetricSpaceObjectMethods:
    r"""Methods on metric spaces."""

    def is_metric(self) -> bool:
        return True

    @abstract_method
    def metric(self, x: SetElement, y: SetElement) -> RealNumber: ...

    @abstract_method
    def ball(self, center: SetElement, radius: RealNumber) -> MetricBall: ...

    @abstract_method
    def dist(self, x: SetElement, y: SetElement) -> RealNumber: ...


class _MetricSpaces(CategoryWithAxiom):
    r"""Category of metric spaces."""

    _base_category_class_and_axiom = (_TopologicalSpaces, "Metric")
    ParentMethods = _MetricSpaceObjectMethods

    def _repr_object_names(self) -> str:
        return "metric spaces"

    def super_categories(self) -> list:
        return [SageSets().Metric(), _TopologicalSpaces()]
