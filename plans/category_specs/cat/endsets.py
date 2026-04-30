r"""Endsets internal to ``Cat()``."""

from __future__ import annotations

from typing import final

from sage.misc.lazy_import import LazyImport

from ..homsets import EndsetsOf
from .homsets import CatHomsets, _CatFunctorMethods


class _CatEndofunctorMethods(_CatFunctorMethods):
    @final
    def is_endofunctor(self) -> bool:
        return self.domain() == self.codomain()


class CatEndsets(EndsetsOf):
    r"""Endofunctor sets of a category."""

    _base_category_class_and_axiom = (CatHomsets, "Endset")

    @final
    def _repr_object_names(self) -> str:
        return f"endofunctor sets internal to {self.base_category()}"

    ElementMethods = _CatEndofunctorMethods
    Autset = LazyImport("category_specs.cat.autsets", "CatAutsets")


__all__ = ["CatEndsets"]
