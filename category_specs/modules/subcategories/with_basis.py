r"""Modules with a specified basis."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category import Category
from sage.sets.family import AbstractFamily

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction
from .. import Modules

if TYPE_CHECKING:
    from ...types import (
        CategoryElement,
        Integer,
        Matrix,
        ModuleBasis,
        Ring,
        RingElement,
        RModule,
        RModuleElement,
        RModuleMorphism,
    )


class _WithBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified basis.

    Canonical chain: ``Modules(R).WithBasis()``.
    """

    _base_category_class_and_axiom = (Modules, "WithBasis")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().Free()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_basis()

    class SubcategoryMethods:
        @final
        def WithOrderedBasis(self) -> Category:
            return self.base_category().WithOrderedBasis()

    class ParentMethods:
        @override
        @final
        def has_basis(self) -> bool:
            return True

        @abstractmethod
        def basis(self) -> ModuleBasis: ...

        @final
        def basis_index_set(self) -> Sequence[CategoryElement]:
            basis = self.basis()
            if isinstance(basis, AbstractFamily):
                return tuple(basis.keys())
            if isinstance(basis, Mapping):
                return tuple(basis.keys())
            return tuple(range(len(basis)))

        @abstractmethod
        def monomial(self, index: CategoryElement) -> RModuleElement:
            r"""Return the basis element indexed by ``index``."""
            ...

        @abstractmethod
        def term(
            self, index: CategoryElement, coeff: RingElement | None = None
        ) -> RModuleElement:
            r"""Return ``coeff`` times the basis element indexed by ``index``."""
            ...

        @abstractmethod
        def linear_combination_of_basis(
            self,
            terms: dict[CategoryElement, RingElement]
            | Sequence[tuple[CategoryElement, RingElement]],
        ) -> RModuleElement:
            r"""Return the finite linear combination of basis terms."""
            ...

        @abstractmethod
        def echelon_form(
            self,
            elements: Sequence[RModuleElement],
            row_reduced: bool = False,
            order: Sequence[CategoryElement]
            | Callable[[CategoryElement], Integer | str]
            | None = None,
        ) -> list[RModuleElement]:
            ...

        @abstractmethod
        def reduce(self, x: RModuleElement) -> RModuleElement: ...

    class ElementMethods:
        @abstractmethod
        def monomial_coefficients(
            self, copy: bool = True
        ) -> dict[CategoryElement, RingElement]:
            r"""Return the finite coefficient map in the parent's basis."""
            ...

        @abstractmethod
        def coefficient(self, index: CategoryElement) -> RingElement:
            r"""Return the coefficient of the basis element indexed by ``index``."""
            ...

        @abstractmethod
        def support(self) -> list[CategoryElement]:
            r"""Return the finite basis support of this element."""
            ...

        @abstractmethod
        def monomials(self) -> list[RModuleElement]:
            r"""Return the basis monomials appearing with nonzero coefficient."""
            ...

        @abstractmethod
        def terms(self) -> list[RModuleElement]:
            r"""Return the nonzero scalar basis terms of this element."""
            ...

        @abstractmethod
        def coefficients(self) -> list[RingElement]:
            r"""Return the nonzero coefficients in the basis expansion."""
            ...

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstractmethod
            def from_basis_map(
                self, f: Callable[[CategoryElement], RModuleElement]
            ) -> RModuleMorphism:
                r"""Return the module morphism determined by a map on basis indices."""
                ...

        class ElementMethods:
            @abstractmethod
            def on_basis(self) -> Callable[[CategoryElement], RModuleElement]:
                r"""Return the basis-index map determining this morphism."""
                ...




class _WithOrderedBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified ordered basis.

    Canonical chain: ``Modules(R).WithOrderedBasis()``.
    """

    _base_category_class_and_axiom = (Modules, "WithOrderedBasis")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [
            self.base_category().WithBasis(),
            self.base_category().WithOrderedGeneratingSet(),
        ]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_basis()

    class ParentMethods:
        @override
        @final
        def has_ordered_basis(self) -> bool:
            return True

        @final
        def basis_order(self) -> tuple[CategoryElement, ...]:
            return tuple(self.basis_index_set())

        @final
        def user_basis(self) -> ModuleBasis:
            return self.basis()

        @abstractmethod
        def basis_matrix(self, ring: Ring | None = None) -> Matrix: ...

        @abstractmethod
        def echelonized_basis(self) -> ModuleBasis: ...

        @abstractmethod
        def echelonized_basis_matrix(self) -> Matrix: ...

        @abstractmethod
        def coordinate_vector(
            self,
            v: RModuleElement | Sequence[RingElement],
            check: bool = True,
        ) -> RModuleElement | Sequence[RingElement]: ...

        @abstractmethod
        def coordinates(
            self, v: RModuleElement | Sequence[RingElement]
        ) -> RModuleElement | Sequence[RingElement]: ...

        @abstractmethod
        def from_vector(
            self,
            vector: RModuleElement | Sequence[RingElement],
            order: Sequence[CategoryElement] | None = None,
            coerce: bool = True,
        ) -> RModuleElement:
            ...

        @abstractmethod
        def coordinate_module(self, V: RModule) -> RModule: ...

        @abstractmethod
        def matrix(self) -> Matrix: ...

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstractmethod
            def from_matrix(self, M: Matrix) -> RModuleMorphism:
                r"""Return the morphism represented by ``M`` in the ordered bases."""
                ...

        class ElementMethods:
            @abstractmethod
            def to_matrix(self) -> Matrix:
                r"""Return the matrix representing this morphism in ordered bases."""
                ...

    class ElementMethods:
        @abstractmethod
        def list(self) -> list[RingElement]: ...

        @abstractmethod
        def vector(self) -> RModuleElement | Sequence[RingElement]: ...

        @abstractmethod
        def degree(self) -> Integer: ...
