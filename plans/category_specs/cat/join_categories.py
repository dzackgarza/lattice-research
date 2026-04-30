r"""Join-category predicate surface for ``Cat()``."""

from __future__ import annotations

from typing import Any, final

from sage.categories.category import JoinCategory as SageJoinCategory

from .base_category_types import Category, Category_singleton


@final
def is_join_category(candidate: Any) -> bool:
    r"""Return whether ``candidate`` is Sage's category-lattice join object."""
    return isinstance(candidate, SageJoinCategory)


class JoinCategories(Category_singleton):
    r"""Subcategory of ``Cat()`` whose objects are Sage join categories."""

    @final
    def _repr_object_names(self) -> str:
        return "join categories"

    @final
    def super_categories(self) -> list[Category]:
        from . import Cat

        return [Cat()]

    @final
    def additional_structure(self):
        return None

    @final
    def __contains__(self, candidate: Any) -> bool:
        return is_join_category(candidate)
