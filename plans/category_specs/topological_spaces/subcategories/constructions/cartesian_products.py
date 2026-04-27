r"""Cartesian-product construction category for topological spaces."""

from __future__ import annotations

from sage.categories.cartesian_product import CartesianProductsCategory


class _CartesianProducts(CartesianProductsCategory):
    r"""Cartesian products equipped with the product topology."""
