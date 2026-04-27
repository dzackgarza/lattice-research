r"""Quotient construction category for topological spaces."""

from __future__ import annotations

from sage.categories.quotients import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Topological quotient spaces with the quotient topology."""
