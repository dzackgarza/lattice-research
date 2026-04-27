r"""Topological-space category surface.

Topological spaces are sets with a topology. This subtree owns the category
``TopologicalSpaces()`` and its metric-space subcategory. The set category exposes
``Sets().Topological()`` and ``Sets().Metric()`` as navigation to these same
mathematical categories.

Subcategory hierarchy::

    TopologicalSpaces() / Sets().Topological()
    `-- Metric() / Sets().Metric()

Constructor entry points live under ``TopologicalSpaces().Constructors()`` once Sage
topological-space constructors are inventoried.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..sets import Sets

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

    def _repr_object_names(self) -> str:
        return "topological spaces"

    def super_categories(self) -> list[Category]:
        return [SageSets().Topological(), Sets()]

    class SubcategoryMethods:
        @cached_method
        def Metric(self):
            return self._with_axiom("Metric")


class TopologicalSpaces(Category_singleton):
    r"""Public category object for topological spaces."""

    ParentMethods = _TopologicalSpaceObjectMethods

    def __contains__(self, X: Any) -> bool:
        match X:
            case _ if isinstance(X, Category) and X.is_subcategory(Sets().Topological()):
                return True
            case _ if X in SageSets().Topological():
                return True
            case _:
                return False

    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Topological()]

    @cached_method
    def Metric(self):
        return _MetricSpaces()

    class Constructors:
        r"""Topological-space constructors.

        No standalone Sage topological-space constructor has been admitted yet.
        """

    _Constructors = Constructors

    @cached_method
    def Constructors(self):
        return self.__class__._Constructors()


TopologicalSpace = _TopologicalSpaces


from .subcategories.metric import _MetricSpaces

MetricSpace = _MetricSpaces
