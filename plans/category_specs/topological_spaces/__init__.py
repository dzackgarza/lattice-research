r"""Topological-space category surface.

Topological spaces are sets with a topology. This subtree owns the category
``TopologicalSpaces()`` and its metric-space subcategory. The set category exposes
``Sets().Topological()`` and ``Sets().Metric()`` as the same mathematical
categories, not as set-local duplicates.

Subcategory hierarchy::

    TopologicalSpaces() = Sets().Topological()
    |-- Metric() = Sets().Metric()
    |-- Subobjects()
    |-- Quotients()
    |-- Subquotients()
    |-- ObjectsOver()
    |-- ObjectsUnder()
    |-- CartesianProducts()
    `-- Homsets()
        |-- Endset()
        `-- Autset()

Constructor entry points live under ``TopologicalSpaces().Constructors()`` once Sage
topological-space constructors are inventoried.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category, CategoryWithAxiom
from ..sets import Sets
from .homsets import TopologicalSpaceHomsets
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

if TYPE_CHECKING:
    from ..types import TopologicalSpace


class _TopologicalSpaceObjectMethods:
    r"""Methods on objects in the category of topological spaces."""

    def is_topological(self) -> bool:
        return True

    @abstract_method
    def is_connected(self) -> bool: ...

    @abstract_method
    def closure(self) -> TopologicalSpace: ...

    @abstract_method
    def interior(self) -> TopologicalSpace: ...

    @abstract_method
    def boundary(self) -> TopologicalSpace: ...

    @abstract_method
    def is_open(self) -> bool: ...

    @abstract_method
    def is_closed(self) -> bool: ...

    @abstract_method
    def is_compact(self) -> bool: ...


class _TopologicalSpaces(CategoryWithAxiom):
    r"""Category of topological spaces."""

    _base_category_class_and_axiom = (Sets, "Topological")
    ParentMethods = _TopologicalSpaceObjectMethods
    Homsets = TopologicalSpaceHomsets
    Metric = LazyImport("category_specs.topological_spaces.subcategories.metric", "_MetricSpaces")

    def _repr_object_names(self) -> str:
        return "topological spaces"

    def super_categories(self) -> list[Category]:
        return [SageSets().Topological(), Sets()]

    class Constructors:
        r"""Topological-space constructors.

        No standalone Sage topological-space constructor has been admitted yet.
        """

    _Constructors = Constructors

    @cached_method
    def Constructors(self):
        return self.__class__._Constructors()

    class SubcategoryMethods:
        @cached_method
        def Metric(self) -> Category:
            return self._with_axiom("Metric")

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts


TopologicalSpaces = _TopologicalSpaces
TopologicalSpace = _TopologicalSpaces


from .subcategories.metric import _MetricSpaces

MetricSpace = _MetricSpaces
