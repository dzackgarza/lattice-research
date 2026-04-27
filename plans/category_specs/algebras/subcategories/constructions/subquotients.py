r"""Subquotient construction category for algebras."""

from __future__ import annotations

from sage.categories.subquotients import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Algebra objects obtained as subobjects of quotients or quotients of subobjects."""
