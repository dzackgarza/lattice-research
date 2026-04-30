r"""Dual objects of algebras."""

from __future__ import annotations

from ....cat import DualObjectsCategory


class _DualObjects(DualObjectsCategory):
    r"""Dual objects in a category of algebras."""

    def extra_super_categories(self) -> list:
        return []
