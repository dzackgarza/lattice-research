r"""Sage-backed module family category."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Integer, Matrix, Polyhedron, RealNumber, RModuleElement

_FreeModulesWithStandardBasis = LazyImport("category_specs.modules.subcategories.free_modules_with_standard_basis", "_FreeModulesWithStandardBasis")
_FreeModulesOverIntegralDomains = LazyImport("category_specs.modules.subcategories.free_modules_over_integral_domains", "_FreeModulesOverIntegralDomains")
_FreeModulesOverPIDs = LazyImport("category_specs.modules.subcategories.free_modules_over_pids", "_FreeModulesOverPIDs")
_VectorSpaces = LazyImport("category_specs.modules.subcategories.vector_spaces", "_VectorSpaces")
_RealDoubleVectorSpaces = LazyImport("category_specs.modules.subcategories.real_double_vector_spaces", "_RealDoubleVectorSpaces")
_ComplexDoubleVectorSpaces = LazyImport("category_specs.modules.subcategories.complex_double_vector_spaces", "_ComplexDoubleVectorSpaces")
_VectorSubspaces = LazyImport("category_specs.modules.subcategories.vector_subspaces", "_VectorSubspaces")
_VectorSubspacesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.vector_subspaces_with_ordered_generating_set", "_VectorSubspacesWithOrderedGeneratingSet")
_VectorSpaceQuotients = LazyImport("category_specs.modules.subcategories.vector_space_quotients", "_VectorSpaceQuotients")
_FreeQuadraticModules = LazyImport("category_specs.modules.subcategories.free_quadratic_modules", "_FreeQuadraticModules")
_FreeModuleSubmodules = LazyImport("category_specs.modules.subcategories.free_module_submodules", "_FreeModuleSubmodules")
_FreeModuleSubmodulesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.free_module_submodules_with_ordered_generating_set", "_FreeModuleSubmodulesWithOrderedGeneratingSet")
_CombinatorialFreeModules = LazyImport("category_specs.modules.subcategories.combinatorial_free_modules", "_CombinatorialFreeModules")
_SubmodulesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.submodules_with_ordered_generating_set", "_SubmodulesWithOrderedGeneratingSet")
_QuotientModulesWithOrderedGeneratingSet = LazyImport("category_specs.modules.subcategories.quotient_modules_with_ordered_generating_set", "_QuotientModulesWithOrderedGeneratingSet")
_FreeModuleQuotients = LazyImport("category_specs.modules.subcategories.free_module_quotients", "_FreeModuleQuotients")
_RepresentationModules = LazyImport("category_specs.modules.subcategories.representation_modules", "_RepresentationModules")
_FiniteRankFreeModules = LazyImport("category_specs.modules.subcategories.finite_rank_free_modules", "_FiniteRankFreeModules")
_FinitelyGeneratedPIDQuotientModules = LazyImport("category_specs.modules.subcategories.finitely_generated_pid_quotient_modules", "_FinitelyGeneratedPIDQuotientModules")
_FreeGradedModules = LazyImport("category_specs.modules.subcategories.free_graded_modules", "_FreeGradedModules")
_FinitelyPresentedGradedModules = LazyImport("category_specs.modules.subcategories.finitely_presented_graded_modules", "_FinitelyPresentedGradedModules")
_OreModules = LazyImport("category_specs.modules.subcategories.ore_modules", "_OreModules")
_IntegerLattices = LazyImport("category_specs.modules.subcategories.integer_lattices", "_IntegerLattices")
_TorsionQuadraticModules = LazyImport("category_specs.modules.subcategories.torsion_quadratic_modules", "_TorsionQuadraticModules")
_RingObjectsAsModules = LazyImport("category_specs.modules.subcategories.ring_objects_as_modules", "_RingObjectsAsModules")


class _IntegerLattices(Category_over_base_ring):
    r"""Sage integer lattices, including LLL/BKZ-backed lattice methods."""

    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).Subobjects(),
            Modules(R).WithOrderedGeneratingSet(),
            Modules(R).OverPID(),
            Modules(R).WithForms().Bilinear(),
        ]

    class ParentMethods:
        @abstract_method
        def gram_matrix(self) -> Matrix: ...

        @abstract_method
        def LLL(
            self,
            delta: RealNumber | None = None,
            eta: RealNumber | None = None,
            algorithm: str = "fpLLL:wrapper",
            fp: str | None = None,
            prec: Integer = 0,
            early_red: bool = False,
            use_givens: bool = False,
            use_siegel: bool = False,
            transformation: bool = False,
        ) -> Matrix: ...

        @abstract_method
        def BKZ(
            self,
            delta: RealNumber | None = None,
            algorithm: str = "fpLLL",
            fp: str | None = None,
            block_size: Integer = 10,
            prune: Integer = 0,
            use_givens: bool = False,
            precision: Integer = 0,
            proof: bool | None = None,
        ) -> Matrix: ...

        @abstract_method
        def shortest_vector(
            self,
            update_reduced_basis: bool = True,
            algorithm: Literal["fplll", "pari"] = "fplll",
        ) -> RModuleElement: ...

        @abstract_method
        def voronoi_cell(self, radius: RealNumber | None = None) -> Polyhedron: ...
