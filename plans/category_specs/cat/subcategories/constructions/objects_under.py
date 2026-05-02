r"""Coslice construction category for categories under a fixed category."""

from __future__ import annotations

from typing import override

from sage.categories.functor import Functor
from sage.misc.abstract_method import abstract_method

from ... import Category, Category_over_base, RegressiveCovariantConstructionCategory


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Categories ``D`` equipped with a functor ``C -> D``.

    Canonical chain: ``Cat().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    def _repr_object_names(self) -> str:
        return f"categories under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_category(self) -> Category:
            r"""Return the base category ``C`` of this coslice object."""
            ...

        @abstract_method
        def structure_functor(self) -> Functor:
            r"""Return the structure functor from ``C`` to this category."""
            ...

        def structure_domain(self) -> Category:
            r"""Return the domain category of the structure functor."""
            return self.structure_category()

        def structure_codomain(self) -> Category:
            r"""Return the codomain category of the structure functor."""
            return self

    class ElementMethods: ...
    class MorphismMethods: ...


CosliceCategories = _ObjectsUnder
