r"""Subobject construction category for categories."""

from __future__ import annotations

from ... import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Subcategories viewed as subobjects in ``Cat()``."""


Subcategories = _Subobjects
