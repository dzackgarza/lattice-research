r"""Aut categories internal to ``Cat()``."""

from __future__ import annotations

from typing import final

from ..homsets import AutCategoryOf
from .endsets import CatEndCategory, _CatEndofunctorMethods


class _CatAutofunctorMethods(_CatEndofunctorMethods):
    @final
    def is_autofunctor(self) -> bool:
        return True


class CatAutCategory(AutCategoryOf):
    r"""Autofunctor category of a category."""

    _base_category_class_and_axiom = (CatEndCategory, "Autset")

    @final
    def _repr_object_names(self) -> str:
        return f"autofunctor categories internal to {self.base_category()}"

    ElementMethods = _CatAutofunctorMethods
    class ParentMethods: ...
    class MorphismMethods: ...
