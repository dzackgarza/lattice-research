r"""Rings of fixed characteristic."""

from __future__ import annotations

from typing import Any

from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from .parameterized import _Category_over_base_integer


class _CharacteristicRings(_Category_over_base_integer):
    parameter_name = "characteristic"

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.characteristic() == self.characteristic()

    def characteristic(self) -> Integer:
        return self.base_integer()

    def _repr_object_names(self):
        return f"{self.base_category()._repr_object_names()} of characteristic {self.characteristic()}"

    class ParentMethods:
        @abstract_method
        def characteristic(self) -> Integer: ...
