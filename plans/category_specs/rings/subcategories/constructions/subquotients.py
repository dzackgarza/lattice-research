r"""Ring subquotients."""

from __future__ import annotations

from sage.categories.subquotients import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Ring subquotients in the current ring category."""

    def _repr_object_names(self):
        return f"subquotients of {self.base_category()._repr_object_names()}"
