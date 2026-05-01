r"""Complete metric spaces."""

from __future__ import annotations

from typing import final

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category, CategoryWithAxiom_singleton as CategoryWithAxiom
from .metric import _MetricSpaces


class _CompleteMetricSpaces(CategoryWithAxiom):
    r"""Category of complete metric spaces."""

    _base_category_class_and_axiom = (_MetricSpaces, "Complete")

    @final
    def _repr_object_names(self) -> str:
        return "complete metric spaces"

    @final
    def super_categories(self) -> list[Category]:
        return [SageSets().Metric().Complete(), _MetricSpaces()]

    class ParentMethods:
        @final
        def is_complete(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
