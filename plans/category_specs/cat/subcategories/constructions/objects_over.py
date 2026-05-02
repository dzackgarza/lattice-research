r"""Slice construction category for categories over a fixed category."""

from __future__ import annotations

from typing import override

from sage.categories.functor import Functor
from sage.misc.abstract_method import abstract_method

from ... import Category, Category_over_base, RegressiveCovariantConstructionCategory


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Categories ``D`` equipped with a functor ``D -> C``.

    Canonical chain: ``Cat().ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    def _repr_object_names(self) -> str:
        return f"categories over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_category(self) -> Category:
            r"""Return the base category ``C`` of this slice object."""
            ...

        @abstract_method
        def structure_functor(self) -> Functor:
            r"""Return the structure functor from this category to ``C``."""
            ...

        def structure_domain(self) -> Category:
            r"""Return the domain category of the structure functor."""
            return self

        def structure_codomain(self) -> Category:
            r"""Return the codomain category of the structure functor."""
            return self.structure_category()

    class ElementMethods: ...
    class MorphismMethods: ...


SliceCategories = _ObjectsOver
