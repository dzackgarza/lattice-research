r"""Autsets internal to ``Cat()``."""

from __future__ import annotations

from typing import final

from ..homsets import AutsetsOf
from .endsets import CatEndsets, _CatEndofunctorMethods


class _CatAutofunctorMethods(_CatEndofunctorMethods):
    @final
    def is_autofunctor(self) -> bool:
        return True


class CatAutsets(AutsetsOf):
    r"""Autofunctor sets of a category."""

    _base_category_class_and_axiom = (CatEndsets, "Autset")

    @final
    def _repr_object_names(self) -> str:
        return f"autofunctor sets internal to {self.base_category()}"

    ElementMethods = _CatAutofunctorMethods


__all__ = ["CatAutsets"]
