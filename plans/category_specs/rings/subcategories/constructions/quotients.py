r"""Ring quotients."""

from __future__ import annotations

from sage.categories.quotients import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Ring quotients in the current ring category."""

    def _repr_object_names(self):
        return f"quotients of {self.base_category()._repr_object_names()}"
