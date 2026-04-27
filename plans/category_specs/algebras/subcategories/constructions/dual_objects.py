r"""Dual objects of algebras."""

from __future__ import annotations

from sage.categories.dual import DualObjectsCategory


class _DualObjects(DualObjectsCategory):
    r"""Dual objects in a category of algebras."""

    def extra_super_categories(self) -> list:
        return []
