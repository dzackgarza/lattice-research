r"""Ring subobjects."""

from __future__ import annotations

from sage.categories.subobjects import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Ring subobjects: subrings in the current ring category."""

    def _repr_object_names(self):
        return f"subobjects of {self.base_category()._repr_object_names()}"
