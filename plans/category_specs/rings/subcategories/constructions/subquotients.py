r"""Ring subquotients."""

from __future__ import annotations

from typing import final

from ....cat import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Ring subquotients in the current ring category."""

    @final
    def _repr_object_names(self):
        return f"subquotients of {self.base_category()._repr_object_names()}"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
