r"""Tensor products of algebras."""

from __future__ import annotations

from typing import final
from ....cat import TensorProductsCategory


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products in a category of algebras."""

    @final
    def extra_super_categories(self) -> list:
        return [self.base_category()]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
