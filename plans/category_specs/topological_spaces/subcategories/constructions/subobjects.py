r"""Subobject construction category for topological spaces."""

from __future__ import annotations

from sage.categories.subobjects import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Topological subspaces with the induced topology."""
