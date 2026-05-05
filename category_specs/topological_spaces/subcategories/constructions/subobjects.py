r"""Subobject construction category for topological spaces."""

from __future__ import annotations

from typing import final, override

from ....cat import Category, SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Topological subspaces with the induced topology.

    Canonical chain: ``TopologicalSpaces().Subobjects()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return project subobject categories without Sage axiom reapplication."""
        from ....sets import Sets

        return [self.base_category(), Sets().Subobjects()]

    class ParentMethods: ...

    class ElementMethods: ...

    class MorphismMethods: ...
