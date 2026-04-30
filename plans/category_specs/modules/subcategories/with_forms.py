r"""Modules equipped with forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import RModuleMorphism


class _WithForms(CategoryWithAxiom_over_base_ring):
    r"""Non-full category of pairs ``(M, f)`` with a form on ``M``."""

    _base_category_class_and_axiom = (Modules, "WithForms")
    _defining_predicates = ("has_form",)

    class ParentMethods:
        @final
        def has_form(self) -> bool:
            return True

        @abstract_method
        def is_bilinear(self) -> bool: ...

        @abstract_method
        def is_quadratic(self) -> bool: ...

        @abstract_method
        def form(self) -> RModuleMorphism: ...

    class SubcategoryMethods:
        @cached_method
        @final
        def Bilinear(self) -> Category:
            return self._with_axiom("Bilinear")

        @cached_method
        @final
        def Quadratic(self) -> Category:
            return self._with_axiom("Quadratic")

        @cached_method
        @final
        def Symmetric(self) -> Category:
            return self._with_axiom("Symmetric")

        @cached_method
        @final
        def Alternating(self) -> Category:
            return self._with_axiom("Alternating")

        @cached_method
        @final
        def Nondegenerate(self) -> Category:
            return self._with_axiom("Nondegenerate")

        @cached_method
        @final
        def Integral(self) -> Category:
            return self._with_axiom("Integral")

        @cached_method
        @final
        def Rational(self) -> Category:
            return self._with_axiom("Rational")

    class ElementMethods: ...
    class MorphismMethods: ...

    Bilinear = LazyImport("category_specs.modules.subcategories.bilinear", "_BilinearModules")
    Quadratic = LazyImport("category_specs.modules.subcategories.quadratic", "_QuadraticModules")
