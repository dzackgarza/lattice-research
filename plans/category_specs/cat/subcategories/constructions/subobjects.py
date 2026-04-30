r"""Subobject construction category for categories."""

from __future__ import annotations

from ... import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Subcategories viewed as subobjects in ``Cat()``."""

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...


Subcategories = _Subobjects
