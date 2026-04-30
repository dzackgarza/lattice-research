r"""Ring quotients."""

from __future__ import annotations

from typing import final
from ....cat import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Ring quotients in the current ring category."""

    @final
    def _repr_object_names(self):
        return f"quotients of {self.base_category()._repr_object_names()}"
