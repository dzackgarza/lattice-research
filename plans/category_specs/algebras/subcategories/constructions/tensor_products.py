r"""Tensor products of algebras."""

from __future__ import annotations

from ....cat import TensorProductsCategory


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products in a category of algebras."""

    def extra_super_categories(self) -> list:
        return [self.base_category()]
