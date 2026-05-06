r"""Free modules."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.modules.free_module import FreeModule as SageFreeModule
from sage.modules.free_module import FreeModule_generic as SageFreeModuleGeneric
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule as SageFiniteRankFreeModule

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Algebra, Cardinality, Integer, ModuleBasis, RingMorphism, RModMorphism, RModule


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free modules over the base ring.

    Canonical chain: ``Modules(R).Free()``.
    """

    _base_category_class_and_axiom = (Modules, "Free")
    FiniteRank = LazyImport(__name__, "_FreeFiniteRank")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().Projective()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @cached_method
        @final
        def FiniteRank(self) -> Category:
            return self._with_axiom("FiniteRank")

    class ParentMethods:
        @override
        @final
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Cardinality:
            r"""Return the cardinality of a basis."""
            ...

    class ElementMethods: ...

    class MorphismMethods: ...


class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules.

    Canonical chain: ``Modules(R).Free().FiniteRank()``.
    """

    _base_category_class_and_axiom = (_Free, "FiniteRank")
    WithForms = LazyImport("category_specs.forms.chain", "FiniteRankFreeFormedModulesCategory")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods:
        @abstract_method
        def basis(self) -> ModuleBasis: ...

        @override
        @final
        def bases(self) -> list[ModuleBasis]:
            if isinstance(self, SageFiniteRankFreeModule):
                return SageFiniteRankFreeModule.bases(self)
            assert isinstance(self, SageFreeModuleGeneric)
            return [self.basis()]

        @override
        @final
        def default_basis(self) -> ModuleBasis:
            if isinstance(self, SageFiniteRankFreeModule):
                return SageFiniteRankFreeModule.default_basis(self)
            assert isinstance(self, SageFreeModuleGeneric)
            return self.basis()

        @override
        @final
        def set_default_basis(self, basis: ModuleBasis) -> None:
            if isinstance(self, SageFiniteRankFreeModule):
                return SageFiniteRankFreeModule.set_default_basis(self, basis)
            assert isinstance(self, SageFreeModuleGeneric)
            if basis != self.basis():
                raise NotImplementedError("ambient Sage free modules have a fixed canonical basis")
            return None

        @abstract_method
        def dimension(self) -> Cardinality: ...

        @final
        def degree(self) -> Cardinality:
            return self.dimension()

        @override
        @final
        def symmetric_algebra(self) -> Algebra:
            from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

            return PolynomialRing(self.base_ring(), names=tuple(f"x{i}" for i in range(self.rank())))

        @override
        @final
        def alternating_algebra(self) -> Algebra:
            from sage.algebras.clifford_algebra import ExteriorAlgebra

            return ExteriorAlgebra(self, names=tuple(f"e{i}" for i in range(self.rank())))

        @override
        @final
        def determinant_module(self) -> RModule:
            return self.exterior_power(self.rank())

        @override
        @final
        def dual(self) -> RModule:
            if isinstance(self, SageFiniteRankFreeModule):
                return SageFiniteRankFreeModule.dual(self)

            assert isinstance(self, SageFreeModuleGeneric)
            return self.Hom(SageFreeModule(self.base_ring(), 1))

        @override
        @final
        def is_isomorphic_to(self, other: RModule) -> bool:
            if isinstance(other, (SageFiniteRankFreeModule, SageFreeModuleGeneric)):
                return self.base_ring() == other.base_ring() and self.rank() == other.rank()
            return False

        @override
        @abstract_method
        def tensor_module(
            self,
            k: Integer,
            l: Integer,
            *,
            sym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
            antisym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
        ) -> RModule: ...

        @override
        @final
        def exterior_power(self, p: Integer) -> RModule:
            if isinstance(self, SageFiniteRankFreeModule):
                return SageFiniteRankFreeModule.exterior_power(self, p)

            from sage.algebras.clifford_algebra import ExteriorAlgebra

            assert isinstance(self, SageFreeModuleGeneric)
            exterior_algebra = ExteriorAlgebra(self, names=tuple(f"e{i}" for i in range(self.rank())))
            return exterior_algebra.homogeneous_component(p)

        @override
        @final
        def alternating_form(
            self,
            degree: Integer,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> RModMorphism:
            return SageFiniteRankFreeModule.alternating_form(
                self, degree, name=name, latex_name=latex_name
            )

        @override
        @final
        def base_change(self, morphism: RingMorphism) -> RModule:
            assert morphism.domain() == self.base_ring()
            return self.change_ring(morphism.codomain())

    class ElementMethods: ...

    class MorphismMethods: ...
