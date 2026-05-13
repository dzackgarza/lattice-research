r"""Axiomatic subcategory of graded sets."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, final, overload, override

from sage.categories.sets_with_grading import SetsWithGrading as SageSetsWithGrading

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Set, SetElement, SetGeneratingSeries

    @overload
    def abstractmethod[_MethodT: Callable[..., object]](
        function: _MethodT, /
    ) -> _MethodT: ...

    @overload
    def abstractmethod[_MethodT: Callable[..., object]](
        *, optional: bool = False
    ) -> Callable[[_MethodT], _MethodT]: ...

    def abstractmethod[_MethodT: Callable[..., object]](
        function: _MethodT | None = None, *, optional: bool = False
    ) -> _MethodT | Callable[[_MethodT], _MethodT]: ...
else:
    from abc import abstractmethod

from .. import Sets


class GradedSetsCategory(CategoryWithAxiom):
    r"""Sets equipped with a grading map to a grading set.

    Canonical chain: ``Sets().Graded()``.
    """

    _base_category_class_and_axiom = (Sets, "Graded")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "graded sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets(), SageSetsWithGrading()]

    class ParentMethods:
        @abstractmethod
        def grading_set(self) -> Set:
            r"""Return the set of grades indexing the graded components."""
            ...

        @abstractmethod(optional=True)
        def subset(self, grade: SetElement) -> Set:
            r"""Return the subset of elements with grade ``grade``."""
            del grade
            ...

        @abstractmethod
        def graded_component(self, grade: SetElement) -> Set:
            r"""Return the component of elements of grade ``grade``."""
            del grade
            ...

        @abstractmethod
        def grading(self, elt: SetElement) -> SetElement:
            r"""Return the grade of ``elt``."""
            ...

        @abstractmethod
        def generating_series(self) -> SetGeneratingSeries:
            r"""Return the generating series of graded-component cardinalities."""
            ...

    class ElementMethods: ...

    class MorphismMethods: ...


GradedSetsObject = GradedSetsCategory.ParentMethods
GradedSetsElement = GradedSetsCategory.ElementMethods
GradedSetsMorphism = GradedSetsCategory.MorphismMethods
