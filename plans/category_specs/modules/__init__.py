r"""Spec for the (R,R)-bimodule category ``Modules(R)``.

Naming convention — Sage vs. ours:
    Modules(R)          -- our category of R-modules (this file)
    SageModules(R)      -- sage.categories.modules.Modules(R)
    CommutativeRings()  -- our Rings().Commutative()
    SageCommutativeRings -- sage.categories.commutative_rings.CommutativeRings
    (similarly for Fields, IntegralDomains, PrincipalIdealDomains, etc.)

Canonical type aliases used throughout this package:
    Matrix, vector            -- Sage primitives
    Category                  -- a Sage category
    RMod                      -- the Modules(R) category itself
    RModule                   -- an object M in RMod
    RModuleElement            -- an element in some M
    RModHomset                -- Hom_R(M, N) for some M, N in RMod
    RModMorphism              -- an element in some Hom_R(M, N)
    RModEndset                -- End_R(M) for some M in RMod
    RModEndomorphism          -- an element in some End_R(M)
    RModAutset                -- Aut_R(M) for some M in RMod
    RModAutomorphism          -- an element in some Aut_R(M)
    SubModule                 -- an element in RMod.Subobjects()
    QuotientModule            -- an element in RMod.Quotients()
    RModDual                  -- the Modules dual category (= linear twisted forms)
    DualRModule               -- M^* for some RModule M; an object in RModDual
    Rings                     -- our promoted category of rings
    Ring                      -- an object in Rings
    Ideals                    -- our promoted category of ideals of R as a
                                 subcategory of Modules(R).Subobjects()
    Ideal                     -- an object in Ideals
    RingMorphism              -- a morphism in Rings
    RingEndomorphism          -- an endomorphism in Rings
    RingAutomorphism          -- an automorphism in Rings
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any

from sage.categories.bimodules import Bimodules as SageBimodules
from sage.categories.category import Category
from sage.categories.category_types import Category_module
from sage.categories.dual import DualObjectsCategory
from sage.categories.filtered_modules import FilteredModulesCategory
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.quotients import QuotientsCategory
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.categories.tensor import TensorProductsCategory, tensor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..utils import partition_list, refine_category
from .homsets import RModuleHomsets, _RModMorphisms
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.tensor_products import _TensorProducts

_FreeModulesWithStandardBasis = LazyImport(
    "category_specs.modules.subcategories.free_modules_with_standard_basis", "_FreeModulesWithStandardBasis"
)
_FreeModulesOverIntegralDomains = LazyImport(
    "category_specs.modules.subcategories.free_modules_over_integral_domains", "_FreeModulesOverIntegralDomains"
)
_FreeModulesOverPIDs = LazyImport("category_specs.modules.subcategories.free_modules_over_pids", "_FreeModulesOverPIDs")
_VectorSpaces = LazyImport("category_specs.modules.subcategories.vector_spaces", "_VectorSpaces")
_RealDoubleVectorSpaces = LazyImport(
    "category_specs.modules.subcategories.real_double_vector_spaces", "_RealDoubleVectorSpaces"
)
_ComplexDoubleVectorSpaces = LazyImport(
    "category_specs.modules.subcategories.complex_double_vector_spaces", "_ComplexDoubleVectorSpaces"
)
_VectorSubspaces = LazyImport("category_specs.modules.subcategories.vector_subspaces", "_VectorSubspaces")
_VectorSubspacesWithOrderedGeneratingSet = LazyImport(
    "category_specs.modules.subcategories.vector_subspaces_with_ordered_generating_set",
    "_VectorSubspacesWithOrderedGeneratingSet",
)
_VectorSpaceQuotients = LazyImport("category_specs.modules.subcategories.vector_space_quotients", "_VectorSpaceQuotients")
_FreeQuadraticModules = LazyImport("category_specs.modules.subcategories.free_quadratic_modules", "_FreeQuadraticModules")
_FreeModuleSubmodules = LazyImport("category_specs.modules.subcategories.free_module_submodules", "_FreeModuleSubmodules")
_FreeModuleSubmodulesWithOrderedGeneratingSet = LazyImport(
    "category_specs.modules.subcategories.free_module_submodules_with_ordered_generating_set",
    "_FreeModuleSubmodulesWithOrderedGeneratingSet",
)
_CombinatorialFreeModules = LazyImport(
    "category_specs.modules.subcategories.combinatorial_free_modules", "_CombinatorialFreeModules"
)
_SubmodulesWithOrderedGeneratingSet = LazyImport(
    "category_specs.modules.subcategories.submodules_with_ordered_generating_set",
    "_SubmodulesWithOrderedGeneratingSet",
)
_QuotientModulesWithOrderedGeneratingSet = LazyImport(
    "category_specs.modules.subcategories.quotient_modules_with_ordered_generating_set",
    "_QuotientModulesWithOrderedGeneratingSet",
)
_FreeModuleQuotients = LazyImport("category_specs.modules.subcategories.free_module_quotients", "_FreeModuleQuotients")
_RepresentationModules = LazyImport("category_specs.modules.subcategories.representation_modules", "_RepresentationModules")
_FiniteRankFreeModules = LazyImport("category_specs.modules.subcategories.finite_rank_free_modules", "_FiniteRankFreeModules")
_FinitelyGeneratedPIDQuotientModules = LazyImport(
    "category_specs.modules.subcategories.finitely_generated_pid_quotient_modules",
    "_FinitelyGeneratedPIDQuotientModules",
)
_FreeGradedModules = LazyImport("category_specs.modules.subcategories.free_graded_modules", "_FreeGradedModules")
_FinitelyPresentedGradedModules = LazyImport(
    "category_specs.modules.subcategories.finitely_presented_graded_modules", "_FinitelyPresentedGradedModules"
)
_OreModules = LazyImport("category_specs.modules.subcategories.ore_modules", "_OreModules")
_IntegerLattices = LazyImport("category_specs.modules.subcategories.integer_lattices", "_IntegerLattices")
_TorsionQuadraticModules = LazyImport(
    "category_specs.modules.subcategories.torsion_quadratic_modules", "_TorsionQuadraticModules"
)
_RingObjectsAsModules = LazyImport("category_specs.modules.subcategories.ring_objects_as_modules", "_RingObjectsAsModules")

if TYPE_CHECKING:
    from ..types import (
        Algebra,
        AlgebraElement,
        Cardinality,
        DualRModule,
        FreeModule,
        Ideal,
        Integer,
        Matrix,
        ModuleBasisKeys,
        ModuleStructure,
        PolynomialRingConstructorData,
        ProjectiveModule,
        QuotientModule,
        Ring,
        RingElement,
        RMod,
        RModAutset,
        RModEndset,
        RModHomset,
        RModMorphism,
        RModule,
        RModuleElement,
        RModuleElementClass,
        RModuleForm,
        SubModule,
        TorsionModule,
    )


class _RModObjects:
    r"""ParentMethods for ``Modules(R)``.

    ``linear_combination(...)`` is intentionally not provided here: when
    elements are implemented properly the parent does not need it.
    """

    def is_over_integral_domain(self) -> bool:
        return False

    def is_over_dedekind_domain(self) -> bool:
        return False

    def is_over_pid(self) -> bool:
        return False

    def is_over_commutative_ring(self) -> bool:
        return False

    def is_over_field(self) -> bool:
        return False

    def is_over_local_ring(self) -> bool:
        return False

    def is_over_complete_ring(self) -> bool:
        return False

    def is_free(self) -> bool:
        return False

    def is_torsion(self) -> bool:
        return False

    def is_torsionfree(self) -> bool:
        return False

    def is_projective(self) -> bool:
        return False

    def is_finite(self) -> bool:
        return False

    def has_ordered_generating_set(self) -> bool:
        return False

    def is_finitely_generated(self) -> bool:
        return False

    def is_finitely_presented(self) -> bool:
        return False

    def is_ideal(self) -> bool:
        return False

    @cached_method
    def tensor_square(self):
        return self.tensor_power(2)

    def tensor_power(self, n: int):
        match n:
            case 0:
                return self.base_ring()
            case _ if n >= 1:
                return tensor(n * [self])
            case _ if n <= -1:
                return tensor((-n) * [self.dual()])
            case _:
                raise ValueError(f"Unsupported tensor power: {n}")

    def tensor_module(self, p: int, q: int):
        assert p >= 0 and q >= 0, "T_R(M) is NN^2-graded."
        return tensor([self.tensor_power(p), self.dual().tensor_power(q)])

    @abstract_method
    def annihilator(self) -> Ideal: ...

    def __truediv__(self, N: SubModule) -> QuotientModule:
        return self.quotient(N)

    @abstract_method
    def torsion_submodule(self) -> SubModule:
        r"""M_tors := <{m in M | r*m = 0 for some r in R}>
        = <{m in M | Ann_R(m) != 0}>.
        """
        ...

    @abstract_method
    def tensor_algebra(self) -> RModule:
        r"""Return T_R(M) := \bigoplus_n \bigoplus_{p+q=n} T_R(M)[p,q]."""
        ...

    @abstract_method
    def base_change(self, S: Ring) -> RModule:
        r"""Return a representation of M_S := M \otimes_R S in S-Mod."""
        ...

    @abstract_method
    def module_structure(self) -> ModuleStructure:
        r"""The map sigma: R x M -> M such that r.m := sigma(r, m).

        May equivalently be interpreted as a ring morphism
        sigma: R -> End_R(M), where r.m := sigma(r)(m).  Made explicit so
        that M can be twisted by composing with a ring endomorphism.
        """
        ...

    @abstract_method
    def modify_module_structure(self, sigma: ModuleStructure):
        r"""Define a new module structure sigma': R -> End_R(M) so that
        r.m = sigma'(r)(m), replacing the existing sigma.
        """
        ...

    @abstract_method
    def symmetric_algebra(self) -> RModule: ...

    @abstract_method
    def alternating_algebra(self) -> RModule: ...

    @abstract_method
    def dual(self) -> DualRModule: ...

    @abstract_method
    def Hom(self, N: RModule) -> RModHomset: ...

    @abstract_method
    def End(self) -> RModEndset: ...

    @abstract_method
    def Aut(self) -> RModAutset: ...

    @abstract_method
    def determinant_module(self) -> RModule:
        r"""Return \Lambda^n_R(M), the top exterior power of M."""
        ...

    @abstract_method
    def __contains__(self, data: RModuleElement | SubModule) -> bool:
        r"""Concrete impls dispatch on RModuleElement vs SubModule."""
        ...

    @abstract_method
    def cardinality(self) -> Cardinality: ...

    @abstract_method
    def is_isomorphic_to(self, other: RModule) -> bool: ...

    @abstract_method
    def is_submodule_of(self, other: RModule) -> bool: ...

    @abstract_method
    def direct_sum(self, other: RModule | Sequence[RModule]) -> RModule: ...

    @abstract_method
    def tensor(self, other: RModule | Sequence[RModule]) -> RModule: ...

    def submodule(self, elts: RModuleElement | Sequence[RModuleElement], *args, **kwds) -> SubModule:
        return self.span(elts)

    @abstract_method
    def intersection(self, other: SubModule) -> SubModule: ...

    @abstract_method
    def span(self, elts: RModuleElement | Sequence[RModuleElement]) -> SubModule: ...

    def __add__(self, other: RModule) -> RModule:
        return self.direct_sum(other)

    @abstract_method
    def __mul__(self, other: RingElement | RModule) -> RModule:
        r"""``r * M`` = submodule spanned by ``{r*m | m in M}``;
        ``N * M`` = the tensor product ``M \otimes_R N``.
        """
        ...

    # Do not define: submodule(), _mul_, _rmul_, _lmul_

    @abstract_method
    def natural_pairing(self) -> RModuleForm:
        r"""The (1,1) form b: M \otimes_R M^* -> R defined by b(v, w^*) := w^*(v)."""
        ...


class _RModElements:
    def span(self) -> SubModule:
        return self.parent().span([self])

    def inclusion(self) -> RModMorphism:
        Rm = self.span()
        f = Rm.inclusion()
        assert f in Rm.Hom(self.parent())
        return f

    def annihilator(self) -> Ideal:
        return self.span().annihilator()

    @abstract_method
    def cyclic_submodule(self) -> SubModule: ...

    def is_primitive(self) -> bool:
        return self.span().inclusion().is_primitive()

    @abstract_method
    def __add__(self, m: RModuleElement) -> RModuleElement: ...

    @abstract_method
    def __mul__(self, r: RingElement) -> RModuleElement: ...

    def __neg__(self) -> RModuleElement:
        R = self.base_ring()
        return R(-1) * self

    @abstract_method
    def _lmul_(self, r: RingElement) -> RModuleElement: ...

    @abstract_method
    def _rmul_(self, r: RingElement) -> RModuleElement: ...

    # TODO: define R*m := m.span() when R == m.base_ring(), or base-change.

# ---------------------------------------------------------------------------
# The Modules(R) category
# ---------------------------------------------------------------------------


class Modules(Category_module):
    def __contains__(self, M: Any) -> bool:
        match M:
            case _ if isinstance(M, Category) and M.is_subcategory(self):
                return True
            case _ if hasattr(M, "category") and M.category().is_subcategory(self):
                return True
            case _ if M in SageBimodules(self.base_ring(), self.base_ring()):
                return True
            case _:
                return False

    @staticmethod
    def __classcall_private__(cls, base_ring, dispatch=True):
        from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
        from sage.categories.dedekind_domains import DedekindDomains as SageDedekindDomains
        from sage.categories.fields import Fields as SageFields
        from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
        from sage.categories.principal_ideal_domains import PrincipalIdealDomains as SagePrincipalIdealDomains

        result = super().__classcall__(cls, base_ring)
        if not dispatch:
            return result
        # Cascade from most structure to least.
        if base_ring in SageFields():
            return result._with_axiom("OverField")
        if base_ring in SagePrincipalIdealDomains():
            return result._with_axiom("OverPID")
        if base_ring in SageDedekindDomains():
            return result._with_axiom("OverDedekindDomain")
        if base_ring in SageIntegralDomains():
            return result._with_axiom("OverIntegralDomain")
        if base_ring in SageCommutativeRings():
            return result._with_axiom("OverCommutativeRing")
        # TODO: full ring dispatching. -- [needs approach]
        # TODO: handle Noetherian non-commutative rings. -- [needs approach]
        return result

    def super_categories(self):
        R = self.base_ring()
        return [SageBimodules(R, R)]

    def additional_structure(self):
        r"""Return ``None`` because R-Mod morphisms are exactly (R,R)-biMod morphisms."""
        return None

    # ------------------------------------------------------------------
    # Constructors
    # ------------------------------------------------------------------

    class Constructors:
        r"""Sage module constructor entry points over ``self.base_ring()``."""

        def __init__(self, category: RMod) -> None:
            self._category = category

        def __repr__(self) -> str:
            return f"Sage module constructors over {self.base_ring()}"

        def category(self) -> RMod:
            return self._category

        def base_ring(self) -> Ring:
            return self.category().base_ring()

        def _refine_constructed_module(self, M: RModule, *categories: Category) -> RModule:
            return refine_category(M, [Modules(M.base_ring()), *categories])

        def FreeModulesWithStandardBasis(self) -> Category:
            return _FreeModulesWithStandardBasis(self.base_ring())

        def FreeModulesOverIntegralDomains(self) -> Category:
            return _FreeModulesOverIntegralDomains(self.base_ring())

        def FreeModulesOverPIDs(self) -> Category:
            return _FreeModulesOverPIDs(self.base_ring())

        def VectorSpaces(self) -> Category:
            return _VectorSpaces(self.base_ring())

        def RealDoubleVectorSpaces(self) -> Category:
            return _RealDoubleVectorSpaces(self.base_ring())

        def ComplexDoubleVectorSpaces(self) -> Category:
            return _ComplexDoubleVectorSpaces(self.base_ring())

        def VectorSubspaces(self) -> Category:
            return _VectorSubspaces(self.base_ring())

        def VectorSubspacesWithOrderedGeneratingSet(self) -> Category:
            return _VectorSubspacesWithOrderedGeneratingSet(self.base_ring())

        def VectorSpaceQuotients(self) -> Category:
            return _VectorSpaceQuotients(self.base_ring())

        def FreeQuadraticModules(self) -> Category:
            return _FreeQuadraticModules(self.base_ring())

        def CombinatorialFreeModules(self) -> Category:
            return _CombinatorialFreeModules(self.base_ring())

        def FiniteRankFreeModules(self) -> Category:
            return _FiniteRankFreeModules(self.base_ring())

        def FreeModuleSubmodules(self) -> Category:
            return _FreeModuleSubmodules(self.base_ring())

        def FreeModuleSubmodulesWithOrderedGeneratingSet(self) -> Category:
            return _FreeModuleSubmodulesWithOrderedGeneratingSet(self.base_ring())

        def SubmodulesWithOrderedGeneratingSet(self) -> Category:
            return _SubmodulesWithOrderedGeneratingSet(self.base_ring())

        def QuotientModulesWithOrderedGeneratingSet(self) -> Category:
            return _QuotientModulesWithOrderedGeneratingSet(self.base_ring())

        def FreeModuleQuotients(self) -> Category:
            return _FreeModuleQuotients(self.base_ring())

        def RepresentationModules(self) -> Category:
            return _RepresentationModules(self.base_ring())

        def FinitelyGeneratedPIDQuotientModules(self) -> Category:
            return _FinitelyGeneratedPIDQuotientModules(self.base_ring())

        def FreeGradedModules(self) -> Category:
            return _FreeGradedModules(self.base_ring())

        def FinitelyPresentedGradedModules(self) -> Category:
            return _FinitelyPresentedGradedModules(self.base_ring())

        def OreModules(self) -> Category:
            return _OreModules(self.base_ring())

        def IntegerLattices(self) -> Category:
            return _IntegerLattices(self.base_ring())

        def TorsionQuadraticModules(self) -> Category:
            return _TorsionQuadraticModules(self.base_ring())

        def RingObjectsAsModules(self) -> Category:
            return _RingObjectsAsModules(self.base_ring())

        def _category_for_free_module(self, M: RModule) -> Category:
            if M in self.FreeQuadraticModules():
                return self.FreeQuadraticModules()
            if M in self.VectorSpaceQuotients():
                return self.VectorSpaceQuotients()
            if M in self.VectorSubspacesWithOrderedGeneratingSet():
                return self.VectorSubspacesWithOrderedGeneratingSet()
            if M in self.VectorSubspaces():
                return self.VectorSubspaces()
            if M in self.RealDoubleVectorSpaces():
                return self.RealDoubleVectorSpaces()
            if M in self.ComplexDoubleVectorSpaces():
                return self.ComplexDoubleVectorSpaces()
            if M in self.FreeModuleSubmodulesWithOrderedGeneratingSet():
                return self.FreeModuleSubmodulesWithOrderedGeneratingSet()
            if M in self.FreeModuleSubmodules():
                return self.FreeModuleSubmodules()
            if M in self.VectorSpaces():
                return self.VectorSpaces()
            from sage.categories.integral_domains import IntegralDomains
            from sage.categories.principal_ideal_domains import PrincipalIdealDomains

            R = self.base_ring()
            if R in PrincipalIdealDomains():
                return self.FreeModulesOverPIDs()
            if R in IntegralDomains():
                return self.FreeModulesOverIntegralDomains()
            return self.FreeModulesWithStandardBasis()

        def _category_for_quotient_module(self, M: RModule) -> Category:
            if M in self.VectorSpaceQuotients():
                return self.VectorSpaceQuotients()
            if M in self.FreeModuleQuotients():
                return self.FreeModuleQuotients()
            if M in self.FinitelyGeneratedPIDQuotientModules():
                return self.FinitelyGeneratedPIDQuotientModules()
            return self._category_for_free_module(M)

        def FreeModule(
            self,
            rank_or_basis_keys: int | Integer | ModuleBasisKeys | None = None,
            sparse: bool = False,
            inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] | Sequence[RingElement] | None = None,
            *,
            with_basis: str | None = "standard",
            rank: int | Integer | None = None,
            basis_keys: ModuleBasisKeys | None = None,
        ) -> RModule:
            from sage.modules.free_module import FreeModule as SageFreeModule

            M = SageFreeModule(
                self.base_ring(),
                rank_or_basis_keys,
                sparse,
                inner_product_matrix,
                with_basis=with_basis,
                rank=rank,
                basis_keys=basis_keys,
            )
            if M in self.CombinatorialFreeModules():
                category = self.CombinatorialFreeModules()
            elif M in self.FiniteRankFreeModules():
                category = self.FiniteRankFreeModules()
            else:
                category = self._category_for_free_module(M)
            return self._refine_constructed_module(M, category)

        def VectorSpace(
            self,
            dimension_or_basis_keys: int | Integer | ModuleBasisKeys | None = None,
            sparse: bool = False,
            inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] | Sequence[RingElement] | None = None,
            *,
            with_basis: str | None = "standard",
            dimension: int | Integer | None = None,
            basis_keys: ModuleBasisKeys | None = None,
        ) -> RModule:
            from sage.modules.free_module import VectorSpace as SageVectorSpace

            M = SageVectorSpace(
                self.base_ring(),
                dimension_or_basis_keys,
                sparse,
                inner_product_matrix,
                with_basis=with_basis,
                dimension=dimension,
                basis_keys=basis_keys,
            )
            return self._refine_constructed_module(M, self._category_for_free_module(M))

        def FreeQuadraticModule(
            self,
            rank: int | Integer,
            inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] | Sequence[RingElement],
            sparse: bool = False,
            inner_product_ring: Ring | None = None,
        ) -> RModule:
            from sage.modules.free_quadratic_module import FreeQuadraticModule

            M = FreeQuadraticModule(
                self.base_ring(),
                rank,
                inner_product_matrix,
                sparse=sparse,
                inner_product_ring=inner_product_ring,
            )
            return self._refine_constructed_module(M, self.FreeQuadraticModules())

        def span(
            self,
            gens: Sequence[RModuleElement] | Matrix,
            check: bool = True,
            already_echelonized: bool = False,
        ) -> SubModule:
            from sage.modules.free_module import span as sage_span

            M = sage_span(gens, self.base_ring(), check=check, already_echelonized=already_echelonized)
            return self._refine_constructed_module(M, self._category_for_free_module(M))

        def CombinatorialFreeModule(
            self,
            basis_keys: ModuleBasisKeys,
            element_class: RModuleElementClass | None = None,
            category: Category | tuple[Category, ...] | None = None,
            prefix: str | None = None,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.combinat.free_module import CombinatorialFreeModule

            M = CombinatorialFreeModule(
                self.base_ring(),
                basis_keys,
                element_class=element_class,
                category=category,
                prefix=prefix,
                names=names,
            )
            return self._refine_constructed_module(M, self.CombinatorialFreeModules())

        def FiniteRankFreeModule(
            self,
            rank: int | Integer,
            name: str | None = None,
            latex_name: str | None = None,
            start_index: int | Integer = 0,
            output_formatter: Callable[[RingElement], str] | Callable[[RingElement, str], str] | None = None,
        ) -> FreeModule:
            from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule

            M = FiniteRankFreeModule(
                self.base_ring(),
                rank,
                name=name,
                latex_name=latex_name,
                start_index=start_index,
                output_formatter=output_formatter,
            )
            return self._refine_constructed_module(M, self.FiniteRankFreeModules())

        def quotient_of_free_modules(self, V: FreeModule, W: SubModule) -> QuotientModule:
            M = V / W
            return self._refine_constructed_module(M, self._category_for_quotient_module(M))

        def quotient_module(self, module: RModule, submodule: SubModule, check: bool = True) -> QuotientModule:
            M = module.quotient_module(submodule, check=check)
            return self._refine_constructed_module(M, self._category_for_quotient_module(M))

        def FPModule(
            self,
            arg0: Algebra | RModule | RModMorphism,
            generator_degrees: Sequence[int | Integer] | None = None,
            relations: Sequence[Sequence[AlgebraElement]] = (),
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.module import FPModule

            M = FPModule(arg0, generator_degrees=generator_degrees, relations=relations, names=names)
            return self._refine_constructed_module(M, self.FinitelyPresentedGradedModules())

        def FreeGradedModule(
            self,
            algebra: Algebra,
            generator_degrees: Sequence[int | Integer],
            category: Category | None = None,
            names: str | tuple[str, ...] | None = None,
        ) -> RModule:
            from sage.modules.fp_graded.free_module import FreeGradedModule

            M = FreeGradedModule(algebra, generator_degrees, category=category, names=names)
            return self._refine_constructed_module(M, self.FreeGradedModules())

        def OreQuotientModule(self, ore_polynomial_ring: Ring, polynomial: RingElement) -> RModule:
            M = ore_polynomial_ring.quotient_module(polynomial)
            return self._refine_constructed_module(M, self.OreModules())

        def IntegerLattice(
            self,
            basis: Matrix | Sequence[Sequence[RingElement]],
            lll_reduce: bool = True,
        ) -> RModule:
            from sage.modules.free_module_integer import IntegerLattice

            M = IntegerLattice(basis, lll_reduce=lll_reduce)
            return self._refine_constructed_module(M, self.IntegerLattices())

        def TorsionQuadraticForm(self, q: Matrix | Sequence[Sequence[RingElement]]) -> RModule:
            from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

            M = TorsionQuadraticForm(q)
            return self._refine_constructed_module(M, self.TorsionQuadraticModules())

        def ring_as_rank_one_module(self, ring: Ring | None = None) -> FreeModule:
            R = self.base_ring() if ring is None else ring
            M = Modules(R).Constructors().FreeModule(1)
            return self._refine_constructed_module(M, self.FreeModulesWithStandardBasis())

        def ideal_as_submodule(self, ideal: Ideal) -> SubModule:
            return self._refine_constructed_module(ideal, Modules(ideal.ring()).RIdeals())

        def invertible_ideal_as_projective_submodule(self, ideal: Ideal) -> ProjectiveModule:
            R = ideal.ring()
            return self._refine_constructed_module(ideal, Modules(R).RIdeals(), Modules(R).Projective())

        def polynomial_ring_as_module(
            self,
            *args: PolynomialRingConstructorData,
            **kwds: PolynomialRingConstructorData,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PolynomialRing(self.base_ring(), *args, **kwds)
            return self._refine_constructed_module(S, self.RingObjectsAsModules())

        def power_series_ring_as_module(
            self,
            name: str | None = None,
            arg2: int | Integer | str | None = None,
            names: str | Sequence[str] | None = None,
            sparse: bool = False,
            default_prec: int | Integer | None = None,
            order: str = "negdeglex",
            num_gens: int | Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PowerSeriesRing(
                self.base_ring(),
                name=name,
                arg2=arg2,
                names=names,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
                num_gens=num_gens,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, self.RingObjectsAsModules())

        def laurent_series_ring_as_module(
            self,
            name: str | None = None,
            arg2: int | Integer | str | None = None,
            names: str | Sequence[str] | None = None,
            sparse: bool = False,
            default_prec: int | Integer | None = None,
            order: str = "negdeglex",
            num_gens: int | Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().LaurentSeriesRing(
                self.base_ring(),
                name=name,
                arg2=arg2,
                names=names,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
                num_gens=num_gens,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, self.RingObjectsAsModules())

        def puiseux_series_ring_as_module(
            self,
            name: str | None = None,
            arg2: int | Integer | str | None = None,
            names: str | Sequence[str] | None = None,
            sparse: bool = False,
            default_prec: int | Integer | None = None,
            order: str = "negdeglex",
            num_gens: int | Integer | None = None,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().PuiseuxSeriesRing(
                self.base_ring(),
                name=name,
                arg2=arg2,
                names=names,
                sparse=sparse,
                default_prec=default_prec,
                order=order,
                num_gens=num_gens,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, self.RingObjectsAsModules())

        def matrix_ring_as_module(
            self,
            n: int | Integer,
            sparse: bool = False,
            implementation: str | None = None,
        ) -> RModule:
            from ..rings import Rings

            S = Rings().Constructors().MatrixRing(
                self.base_ring(),
                n,
                sparse=sparse,
                implementation=implementation,
            )
            return self._refine_constructed_module(S, self.RingObjectsAsModules())

    _Constructors = Constructors

    @cached_method
    def Constructors(self):
        r"""Return the Sage module constructor collector over ``self.base_ring()``."""
        return self.__class__._Constructors(self)

    def zero_module(self) -> RModule: ...

    def R(self) -> FreeModule:
        r"""Return R as a rank 1 free R-module."""
        ...

    def torsion_module(self, r: RingElement) -> TorsionModule:
        r"""Return R/r.  Asserts R != 0."""
        ...

    def free_module(self, n: int) -> FreeModule:
        from sage.rings.semirings.non_negative_integer_semiring import NN

        assert n in NN, f"Negative integers are not well-defined ranks: {n}"
        if n == 0:
            return self.zero_module()
        return sum(n * [self.R()])

    def from_ring_elements(self, elts: Sequence[RingElement]) -> RModule:
        r"""Given an ordered subset {r_1, ..., r_n} of R, return
        ``M := R/r_1 \oplus ... \oplus R/r_n``, where R/0 := R.
        """
        from sage.categories.rings import Rings as SageRings

        if not elts:
            return self.zero_module()
        assert all(r.parent() in SageRings() for r in elts), f"All element parents must be rings: {elts}"
        R = elts[0].parent()
        assert all(r.parent() is R for r in elts), f"Elements must share a common ring: {[r.parent() for r in elts]}"
        zs, rs = partition_list(elts, lambda x: x.is_zero())
        F = self.free_module(len(zs))
        T = sum(self.torsion_module(r) for r in rs)
        return F + T

    def from_invariant_factors(self, elts: Sequence[RingElement]) -> RModule:
        return self.from_ring_elements(elts)

    def from_matrix(self, M: Matrix) -> RModule:
        r"""Interpret a matrix as a representation of a morphism
        f: R^m -> R^n and return ``coker(f)``.
        """
        from .subcategories.finitely_presented_over_pid import FinitelyPresentedModulesOverPID

        return FinitelyPresentedModulesOverPID.from_matrix(self, M)

    # ------------------------------------------------------------------
    # SubcategoryMethods — available on every subcategory of Modules(R)
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        def base_ring(self) -> Ring:
            return self.base_category().base_ring()

        ## Ring properties

        @cached_method
        def OverIntegralDomain(self):
            return self._with_axiom("OverIntegralDomain")

        @cached_method
        def OverDedekindDomain(self):
            return self._with_axiom("OverDedekindDomain")

        @cached_method
        def OverPID(self):
            return self._with_axiom("OverPID")

        @cached_method
        def OverCommutativeRing(self):
            return self._with_axiom("OverCommutativeRing")

        @cached_method
        def OverField(self):
            return self._with_axiom("OverField")

        @cached_method
        def OverLocalRing(self):
            return self._with_axiom("OverLocalRing")

        @cached_method
        def OverCompleteRing(self):
            return self._with_axiom("OverCompleteRing")

        ## Homological properties

        @cached_method
        def Free(self):
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
            return self._with_axiom("Torsion")

        @cached_method
        def Torsionfree(self):
            return self._with_axiom("Torsionfree")

        @cached_method
        def Projective(self):
            return self._with_axiom("Projective")

        ## Generation properties

        @cached_method
        def WithOrderedGeneratingSet(self):
            return self._with_axiom("WithOrderedGeneratingSet")

        @cached_method
        def FinitelyGenerated(self):
            return self._with_axiom("FinitelyGenerated")

        @cached_method
        def FinitelyPresented(self):
            return self._with_axiom("FinitelyPresented")

        ## Sage-backed constructors

        @cached_method
        def Constructors(self):
            r"""Return the Sage module constructor collector over this base ring."""
            return Modules._Constructors(self)

        ## Functorial constructions

        @cached_method
        def Subobjects(self):
            return SubobjectsCategory.category_of(self)

        @cached_method
        def Quotients(self):
            return QuotientsCategory.category_of(self)

        @cached_method
        def TensorProducts(self):
            return TensorProductsCategory.category_of(self)

        @cached_method
        def DualObjects(self):
            return DualObjectsCategory.category_of(self)

        dual = DualObjects

        ## Extra structure

        @cached_method
        def Filtered(self):
            return FilteredModulesCategory.category_of(self)

        @cached_method
        def Graded(self):
            return GradedModulesCategory.category_of(self)

        @cached_method
        def Super(self):
            return SuperModulesCategory.category_of(self)

        ## Forms

        @cached_method
        def WithForms(self):
            return self._with_axiom("WithForms")

        @cached_method
        def RIdeals(self):
            return self._with_axiom("RIdeals")

    # ------------------------------------------------------------------
    # Method providers
    # ------------------------------------------------------------------

    ParentMethods = _RModObjects
    ElementMethods = _RModElements
    MorphismMethods = _RModMorphisms
    Homsets = RModuleHomsets

    # ------------------------------------------------------------------
    # Named subcategories
    # ------------------------------------------------------------------

    RIdeals = LazyImport("category_specs.modules.subcategories.r_ideals", "_RIdeals")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — ring properties
    # ------------------------------------------------------------------

    OverIntegralDomain = LazyImport("category_specs.modules.subcategories.over_integral_domain", "_OverIntegralDomain")
    OverDedekindDomain = LazyImport("category_specs.modules.subcategories.over_dedekind_domain", "_OverDedekindDomain")
    OverPID = LazyImport("category_specs.modules.subcategories.over_pid", "_OverPID")
    OverCommutativeRing = LazyImport("category_specs.modules.subcategories.over_commutative_ring", "_OverCommutativeRing")
    OverField = LazyImport("category_specs.modules.subcategories.over_field", "_OverField")
    OverLocalRing = LazyImport("category_specs.modules.subcategories.over_local_ring", "_OverLocalRing")
    OverCompleteRing = LazyImport("category_specs.modules.subcategories.over_complete_ring", "_OverCompleteRing")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — homological
    # ------------------------------------------------------------------

    Free = LazyImport("category_specs.modules.subcategories.free", "_Free")
    Torsion = LazyImport("category_specs.modules.subcategories.torsion", "_Torsion")
    Torsionfree = LazyImport("category_specs.modules.subcategories.torsionfree", "_Torsionfree")
    Projective = LazyImport("category_specs.modules.subcategories.projective", "_Projective")

    # ------------------------------------------------------------------
    # Axiomatic subcategories — generation
    # ------------------------------------------------------------------

    WithOrderedGeneratingSet = LazyImport(
        "category_specs.modules.subcategories.with_ordered_generating_set", "_WithOrderedGeneratingSet"
    )
    FinitelyGenerated = LazyImport("category_specs.modules.subcategories.finitely_generated", "_FinitelyGenerated")
    FinitelyPresented = LazyImport("category_specs.modules.subcategories.finitely_presented", "_FinitelyPresented")

    # ------------------------------------------------------------------
    # Functorial constructions
    # ------------------------------------------------------------------

    Subobjects = _Subobjects
    SubModules = Subobjects
    Quotients = _Quotients
    TensorProducts = _TensorProducts
    CartesianProducts = _CartesianProducts
    DualObjects = _DualObjects

    Filtered = LazyImport("sage.categories.filtered_modules", "FilteredModules")
    Graded = LazyImport("sage.categories.graded_modules", "GradedModules")
    Super = LazyImport("sage.categories.super_modules", "SuperModules")

    # ------------------------------------------------------------------
    # Forms / lattice surface
    # ------------------------------------------------------------------

    WithForms = LazyImport("category_specs.modules.subcategories.with_forms", "_WithForms")
    Bilinear = LazyImport("category_specs.modules.subcategories.bilinear", "_BilinearModules")
    Quadratic = LazyImport("category_specs.modules.subcategories.quadratic", "_QuadraticModules")
    # Lattices: (M, b) with M a f.g. torsionfree R-module over a domain and
    # b a symmetric nondegenerate integral bilinear form.


# ---------------------------------------------------------------------------
# Composed surfaces (aspirational; resolved once axiom chains are populated)
# ---------------------------------------------------------------------------
# TODO: immediately restrict to Dedekind domains, then to PIDs.  Bilinear / -- [needs approach]
# quadratic modules and (rational) lattices are wanted over PIDs (so they
# are free of finite rank).
#
# Lattices = (
#     Modules(IntegralDomains())
#         .FinitelyGenerated()
#         .Torsionfree()
#         .WithForms()
#         .Bilinear()
#         .Symmetric()
#         .Nondegenerate()
#         .Integral()
# )
# RationalLattices = (
#     Modules(IntegralDomains())
#         .FinitelyGenerated()
#         .Torsionfree()
#         .OverIntegralDomain()
#         .WithForms()
#         .Bilinear()
#         .Symmetric()
#         .Nondegenerate()
#         .Rational()
# )


# ---------------------------------------------------------------------------
# TODO: subcategory-specific surface -- [needs approach]
# ---------------------------------------------------------------------------
# - to_matrix
# - identify when Hom_R(M, N) is a matrix algebra
# - identify when End_R(M) is a matrix algebra
# - identify when Aut_R(M) is a subgroup of (GL_n(R), *)
# - iteration on countable objects
# - __contains__ methods
# - to/from_X for X = dict, images, matrix, function


# The specialized ``FinitelyPresented() ∩ OverPID()`` implementation in
# ``subcategories/finitely_presented_over_pid.py`` is intentionally not installed here
# yet. Installing it as ``_FinitelyPresented.OverPID`` recursively re-enters
# ``FinitelyPresented().OverPID()`` once ``OverPID`` is registered as a real
# axiom.  The generic axiom join composes correctly and keeps the category
# surface usable until the meet class is wired with a non-recursive base.
