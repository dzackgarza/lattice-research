r"""Subquotient construction category for categories."""

from __future__ import annotations

from sage.categories.subquotients import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Categories obtained as subcategories of quotients or quotients of subcategories."""
