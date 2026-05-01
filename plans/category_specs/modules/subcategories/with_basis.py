r"""Modules with a specified basis."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction
from .. import Modules

if TYPE_CHECKING:
    from ...types import CategoryElement, ModuleBasis, RingElement, RModuleElement, RModuleMorphism, Set


class _WithBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified basis."""

    _base_category_class_and_axiom = (Modules, "WithBasis")
    WithOrderedBasis = LazyImport(__name__, "_WithOrderedBasis")

    @final
    def extra_super_categories(self):
        return [self.base_category().Free()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_basis()

    class SubcategoryMethods:
        @final
        def WithOrderedBasis(self):
            return self._with_axiom("WithOrderedBasis")

    class ParentMethods:
        @final
        def has_basis(self) -> bool:
            return True

        @abstract_method
        def basis(self) -> ModuleBasis: ...

        @abstract_method
        def basis_index_set(self) -> Set: ...

        @abstract_method
        def monomial(self, i: CategoryElement) -> RModuleElement: ...

        @abstract_method
        def term(self, i: CategoryElement, coefficient: RingElement) -> RModuleElement: ...

        @abstract_method
        def linear_combination_of_basis(self, coeffs: Sequence[RingElement]) -> RModuleElement: ...

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstract_method
            def from_basis_map(self, f: Callable[[CategoryElement], RModuleElement]) -> RModuleMorphism: ...

        class ElementMethods:
            @abstract_method
            def on_basis(self) -> Callable[[CategoryElement], RModuleElement]: ...

        class MorphismMethods: ...

    class ElementMethods:
        @abstract_method
        def coefficient(self, i: CategoryElement) -> RingElement: ...

        @abstract_method
        def support(self) -> tuple[CategoryElement, ...]: ...

        @abstract_method
        def monomial_coefficients(self) -> dict[CategoryElement, RingElement]: ...

    class MorphismMethods: ...


class _WithOrderedBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified ordered basis."""

    _base_category_class_and_axiom = (_WithBasis, "WithOrderedBasis")

    @final
    def extra_super_categories(self):
        return [self.base_category().WithOrderedGeneratingSet()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_basis()

    class ParentMethods:
        @final
        def has_ordered_basis(self) -> bool:
            return True

        @abstract_method
        def basis_order(self) -> Sequence[CategoryElement]: ...

        @abstract_method
        def coordinates(self, v: RModuleElement) -> Sequence[RingElement]: ...

        @abstract_method
        def coordinate_vector(self, v: RModuleElement) -> RModuleElement | Sequence[RingElement]: ...

    class ElementMethods:
        @abstract_method
        def list(self) -> list[RingElement]: ...

        @abstract_method
        def vector(self) -> RModuleElement | Sequence[RingElement]: ...

        @abstract_method
        def ordered_support(self) -> tuple[CategoryElement, ...]: ...

    class MorphismMethods: ...
