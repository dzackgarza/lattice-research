r"""Modules equipped with bilinear forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import _WithForms

if TYPE_CHECKING:
    from ...types import Matrix, RingElement, RModuleElement


class _BilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, b)`` with ``b`` bilinear on ``M``."""

    _base_category_class_and_axiom = (_WithForms, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    class ParentMethods:
        @final
        def is_bilinear(self) -> bool:
            return True

        @abstract_method
        def is_symmetric(self) -> bool: ...

        @abstract_method
        def is_alternating(self) -> bool: ...

        @abstract_method
        def is_nondegenerate(self) -> bool: ...

        @abstract_method
        def is_integral(self) -> bool: ...

        @abstract_method
        def is_rational(self) -> bool: ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)

        @abstract_method
        def inner_product_matrix(self) -> Matrix: ...

        @abstract_method
        def gram_matrix(self) -> Matrix: ...

        @abstract_method
        def uses_ambient_inner_product(self) -> bool: ...

    class ElementMethods:
        @abstract_method
        def inner_product(self, other: RModuleElement) -> RingElement: ...

        @abstract_method
        def dot_product(self, other: RModuleElement) -> RingElement: ...

    class MorphismMethods: ...

    Symmetric = LazyImport("category_specs.lattices.subcategories.symmetric", "_SymmetricBilinearModules")
    Alternating = LazyImport("category_specs.lattices.subcategories.alternating", "_AlternatingBilinearModules")
    Nondegenerate = LazyImport("category_specs.lattices.subcategories.nondegenerate", "_NondegenerateBilinearModules")
    Integral = LazyImport("category_specs.lattices.subcategories.integral", "_IntegralBilinearModules")
    Rational = LazyImport("category_specs.lattices.subcategories.rational", "_RationalBilinearModules")
