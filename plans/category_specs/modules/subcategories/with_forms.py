r"""Modules equipped with forms."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import RModuleMorphism


class _WithForms(CategoryWithAxiom_over_base_ring):
    r"""Non-full category of pairs ``(M, f)`` with a form on ``M``."""

    _base_category_class_and_axiom = (Modules, "WithForms")

    class ParentMethods:
        @abstract_method
        def form(self) -> RModuleMorphism: ...

    class SubcategoryMethods:
        @cached_method
        def Bilinear(self) -> Category:
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self) -> Category:
            return self._with_axiom("Quadratic")

        @cached_method
        def Symmetric(self) -> Category:
            return self._with_axiom("Symmetric")

        @cached_method
        def Alternating(self) -> Category:
            return self._with_axiom("Alternating")

        @cached_method
        def Nondegenerate(self) -> Category:
            return self._with_axiom("Nondegenerate")

        @cached_method
        def Integral(self) -> Category:
            return self._with_axiom("Integral")

        @cached_method
        def Rational(self) -> Category:
            return self._with_axiom("Rational")
