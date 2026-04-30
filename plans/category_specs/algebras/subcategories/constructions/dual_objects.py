r"""Dual objects of algebras."""

from __future__ import annotations

from typing import final
from ....cat import DualObjectsCategory


class _DualObjects(DualObjectsCategory):
    r"""Dual objects in a category of algebras."""

    @final
    def extra_super_categories(self) -> list:
        return []

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
