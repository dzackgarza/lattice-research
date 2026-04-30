r"""The empty category constructor target for ``Cat()``."""

from __future__ import annotations

from typing import Any, final

from .base_category_types import Category, Category_singleton


class EmptyCategory(Category_singleton):
    r"""Bottom category object in the local category-of-categories hierarchy."""

    @final
    def _repr_object_names(self) -> str:
        return "empty category"

    @final
    def super_categories(self) -> list[Category]:
        from . import Cat

        return [Cat()]

    @final
    def additional_structure(self):
        return None

    @final
    def __contains__(self, candidate: Any) -> bool:
        return False

    @final
    def is_subcategory(self, category: Category) -> bool:
        r"""Return whether this bottom object lies under ``category``.

        Sage has joins but no installed bottom category for the empty meet.
        This explicit override is the local mathematical content of
        ``Cat().Constructors().EmptyCategory()``: the empty category is a
        subcategory of every category object that participates in ``Cat()``.
        The special ``category is Cat()`` branch keeps the displayed
        supercategory relation valid even though ``Cat()`` itself is not an
        object of ``Cat()``.
        """
        from . import Cat

        return category is self or category is Cat() or category in Cat()
