r"""Tensor products of modules."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories.tensor import TensorProductFunctor, TensorProductsCategory
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from ....types import RModule, RModuleElement


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products of R-modules."""

    @cached_method
    def extra_super_categories(self):
        r"""Declare that M tensor_R N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def construction(self):
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstract_method
        def tensor_factors(self) -> list[RModule]: ...

        @abstract_method
        def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
            r"""Lift a product element to the tensor product."""
            ...
