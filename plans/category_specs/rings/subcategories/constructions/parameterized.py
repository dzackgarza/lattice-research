r"""Parameterized ring construction category helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category import Category, CategoryWithParameters
from sage.rings.integer import Integer

if TYPE_CHECKING:
    from ....types import Ring


class _Category_over_base_integer(CategoryWithParameters):
    r"""Base class for categories indexed by an integer and a base category."""

    parameter_name = "integer"

    @staticmethod
    def __classcall_private__(cls, category, base_integer):
        return super().__classcall__(cls, category, Integer(base_integer))

    def __init__(self, category, base_integer):
        self._base_category = category
        self._base_integer = Integer(base_integer)
        Category.__init__(self)

    def base_category(self) -> Category:
        return self._base_category

    def base_integer(self) -> Integer:
        return self._base_integer

    def super_categories(self) -> list[Category]:
        return [self.base_category()]

    def _make_named_class_key(self, name):
        return (self.base_category(), self.base_integer())


class _Category_over_base_integer_pair(CategoryWithParameters):
    r"""Base class for categories indexed by a base ring and two integers."""

    parameter_name = "integer_pair"

    @staticmethod
    def __classcall_private__(cls, base_ring, n: int, m: int | None = None):
        if m is None:
            m = n
        return super().__classcall__(cls, base_ring, Integer(n), Integer(m))

    def __init__(self, base_ring: Ring, n: Integer, m: Integer):
        self._base_ring = base_ring
        self._n = Integer(n)
        self._m = Integer(m)
        Category.__init__(self)

    def base_ring(self) -> Ring:
        return self._base_ring

    def nrows(self) -> Integer:
        return self._n

    def ncols(self) -> Integer:
        return self._m

    def _make_named_class_key(self, name: str):
        return (self._base_ring, self._n, self._m)

    def super_categories(self) -> list[Category]:
        from ... import Rings

        return [Rings()]
