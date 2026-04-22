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

from sage.categories import category_with_axiom as _category_with_axiom
from sage.categories.bimodules import Bimodules as SageBimodules
from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory
from sage.categories.filtered_modules import FilteredModulesCategory
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.homsets import HomsetsCategory
from sage.categories.objects import Objects
from sage.categories.quotients import QuotientsCategory
from sage.categories.sets_cat import Sets
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.categories.tensor import TensorProductFunctor, TensorProductsCategory, tensor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..utils import partition_list
from .axioms import (
    _BilinearModules,
    _FinitelyGenerated,
    _FinitelyPresented,
    _Free,
    _FreeFiniteRank,
    _OverCommutativeRing,
    _OverCompleteRing,
    _OverDedekindDomain,
    _OverField,
    _OverIntegralDomain,
    _OverLocalRing,
    _OverPID,
    _Projective,
    _QuadraticModules,
    _RIdeals,
    _Torsion,
    _Torsionfree,
    _WithForms,
    _WithOrderedGeneratingSet,
)
from .homsets import RModuleHomsets, _RModMorphisms

if TYPE_CHECKING:
    from sage.matrix.matrix0 import Matrix
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer

    Cardinality = Integer | InfinityElement
    Ring = Any
    RingElement = Any
    RingEndomorphism = Any
    RModule = Any
    RModuleElement = Any
    RModuleMorphism = Any
    RModuleHomset = Any
    RModuleEndSet = Any
    RModuleAutSet = Any
    DualRModule = Any
    FreeModule = Any
    TorsionModule = Any
    SubModule = Any
    QuotientModule = Any
    Ideal = Any
    RModuleForm = Any
    OrderedSet = Any
    ModuleStructure = Callable[[tuple[RingElement, RModuleElement]], RModuleElement] | Callable[[RingElement], RingEndomorphism]


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

FinSet = Sets().Finite()

_CUSTOM_AXIOMS = (
    "OverIntegralDomain",
    "OverDedekindDomain",
    "OverPID",
    "OverCommutativeRing",
    "OverField",
    "OverLocalRing",
    "OverCompleteRing",
    "Free",
    "FiniteRank",
    "Torsion",
    "Torsionfree",
    "Projective",
    "WithOrderedGeneratingSet",
    "FinitelyGenerated",
    "FinitelyPresented",
    "RIdeals",
    "WithForms",
    "Bilinear",
    "Quadratic",
    "Symmetric",
    "Alternating",
    "Nondegenerate",
    "Integral",
    "Rational",
)


def _register_custom_axioms() -> None:
    missing = tuple(axiom for axiom in _CUSTOM_AXIOMS if axiom not in _category_with_axiom.all_axioms)
    if missing:
        _category_with_axiom.all_axioms += missing


_register_custom_axioms()


# ---------------------------------------------------------------------------
# Categories-of-categories shim
# ---------------------------------------------------------------------------


class Categories(Category_singleton):
    r"""A shim to define an infty-category of (Sage) categories."""

    def super_categories(self):
        return [Objects()]

    def __contains__(self, C: Any) -> bool:
        return isinstance(C, Category)

    @classmethod
    def is_over_a_ring(cls, C: Category) -> bool:
        assert C in Categories(), f"Object is not a category: {C}"
        return any(hasattr(D, "base_ring") for D in C.super_categories())

    @classmethod
    def base_ring(cls, C: Category) -> Ring:
        base_ring_cat = next(
            (D for D in C.super_categories() if hasattr(D, "base_ring")),
            None,
        )
        assert base_ring_cat is not None, f"No super category of {C} is a category over a base ring."
        return base_ring_cat.base_ring()


# ---------------------------------------------------------------------------
# ParentMethods / ElementMethods for Modules(R)
# ---------------------------------------------------------------------------


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

    def quotient(self, N: SubModule) -> QuotientModule:
        return N.inclusion().cokernel()

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
    def Hom(self, N: RModule) -> RModuleHomset: ...

    @abstract_method
    def End(self) -> RModuleEndSet: ...

    @abstract_method
    def Aut(self) -> RModuleAutSet: ...

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

    def inclusion(self) -> RModuleMorphism:
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
# Functorial constructions (Subobjects / Quotients / Tensor / Cartesian / Dual)
# ---------------------------------------------------------------------------


class _DualObjects(DualObjectsCategory):
    r"""Dual modules M^* := Hom_R(M, R) viewed as integral linear forms."""

    def extra_super_categories(self):
        r"""The dual M^* of an R-module is an integral linear form, i.e. an
        object of ``Modules(R).Homsets().Forms().Linear().Integral()``.
        """
        return [self.base_category().Homsets().Forms().Linear().Integral()]


class _Subobjects(SubobjectsCategory):
    r"""Submodule category.  Extends ``RegressiveCovariantConstructionCategory``
    so ``C.Subobjects()`` is always a subcategory of ``C``.

    TODO: enumerate methods already provided by Sage's SubobjectsCategory.
    """

    @abstract_method
    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""Regard M as a submodule of itself via the identity."""
        ...

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule:
            r"""The ambient R-module of which ``self`` is a submodule."""
            ...

        @abstract_method
        def inclusion(self): ...

        @abstract_method
        def intersect(self, N: SubModule) -> SubModule: ...

        def __and__(self, N: SubModule) -> SubModule:
            return self.intersect(N)

        def index(self) -> Cardinality:
            return self.inclusion().index()

        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        def lift(self, m: RModuleElement) -> RModuleElement:
            return self.inclusion()(m)

        @abstract_method
        def saturation(self) -> SubModule: ...

        @abstract_method
        def __le__(self, other: RModule) -> bool: ...

        def quotient_module(self) -> QuotientModule:
            return self.inclusion().cokernel()


class _Quotients(QuotientsCategory):
    r"""Quotient module category.  Extends
    ``RegressiveCovariantConstructionCategory`` so ``C.Quotients()`` is always
    a subcategory of ``C``.

    TODO: enumerate methods already provided by Sage's QuotientsCategory.
    """

    class ParentMethods:
        @abstract_method
        def projection(self): ...

    class ElementMethods:
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products of R-modules.

    TODO: verify
    r * (m_1 \otimes ... \otimes m_n)
        = (r * m_1) \otimes ... \otimes m_n
        = m_1 \otimes ... \otimes (r * m_n)
    holds at the level of the spec.
    """

    @cached_method
    def extra_super_categories(self):
        r"""Declare that M \otimes_R N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def construction(self):
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstract_method
        def tensor_factors(self) -> list[RModule]: ...

        @abstract_method
        def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
            r"""Given an ordered set {m_1, ..., m_n} with m_i in M_i, where
            this module is M = M_1 \otimes_R ... \otimes_R M_n, lift the
            product element (m_1, ..., m_n) to m_1 \otimes ... \otimes m_n.
            """
            ...


class _CartesianProducts(CartesianProductsCategory):
    def extra_super_categories(self):
        r"""Declare that M x N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def __init_extra__(self):
            factors = self._sets
            assert len(factors) > 0, f"No factors found in {self}: {factors}"
            R = factors[0].base_ring()
            assert all(Mi.base_ring() is R for Mi in factors)
            self._base = R

    class ElementMethods:
        def _lmul_(self, x: Any):
            return self.parent()._cartesian_product_of_elements(x * y for y in self.cartesian_factors())


# ---------------------------------------------------------------------------
# The Modules(R) category
# ---------------------------------------------------------------------------


class Modules(Category_module):
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
        # TODO: full ring dispatching.
        # TODO: handle Noetherian non-commutative rings.
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
        if hasattr(M, "elementary_divisors"):
            return self.from_ring_elements(M.elementary_divisors())
        if hasattr(M, "smith_form"):
            D, _, _ = M.smith_form()
            return self.from_ring_elements(D.diagonal())
        raise TypeError(f"Matrix {M} does not appear to support elementary_divisors or smith_form.")

    # ------------------------------------------------------------------
    # SubcategoryMethods — available on every subcategory of Modules(R)
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        def base_ring(self) -> Ring:
            return Categories.base_ring(self)

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

    RIdeals = _RIdeals

    # ------------------------------------------------------------------
    # Axiomatic subcategories — ring properties
    # ------------------------------------------------------------------

    OverIntegralDomain = _OverIntegralDomain
    OverDedekindDomain = _OverDedekindDomain
    OverPID = _OverPID
    OverCommutativeRing = _OverCommutativeRing
    OverField = _OverField
    OverLocalRing = _OverLocalRing
    OverCompleteRing = _OverCompleteRing

    # ------------------------------------------------------------------
    # Axiomatic subcategories — homological
    # ------------------------------------------------------------------

    Free = _Free
    Torsion = _Torsion
    Torsionfree = _Torsionfree
    Projective = _Projective

    # ------------------------------------------------------------------
    # Axiomatic subcategories — generation
    # ------------------------------------------------------------------

    WithOrderedGeneratingSet = _WithOrderedGeneratingSet
    FinitelyGenerated = _FinitelyGenerated
    FinitelyPresented = _FinitelyPresented

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

    WithForms = _WithForms       # Non-full subcategory of pairs (M, f).
    Bilinear = _BilinearModules  # (M, b): b: M \otimes_R M -> S.
    Quadratic = _QuadraticModules  # (M, q): q: M -> S^\sigma.
    # Lattices: (M, b) with M a f.g. torsionfree R-module over a domain and
    # b a symmetric nondegenerate integral bilinear form.


# ---------------------------------------------------------------------------
# Composed surfaces (aspirational; resolved once axiom chains are populated)
# ---------------------------------------------------------------------------
# TODO: immediately restrict to Dedekind domains, then to PIDs.  Bilinear /
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
# TODO: subcategory-specific surface
# ---------------------------------------------------------------------------
# - to_matrix
# - identify when Hom_R(M, N) is a matrix algebra
# - identify when End_R(M) is a matrix algebra
# - identify when Aut_R(M) is a subgroup of (GL_n(R), *)
# - iteration on countable objects
# - __contains__ methods
# - to/from_X for X = dict, images, matrix, function


# ---------------------------------------------------------------------------
# Wire custom axiom classes to their (base category, axiom name) pairs.
# ---------------------------------------------------------------------------

for _axiom, _category_class in (
    ("OverIntegralDomain", _OverIntegralDomain),
    ("OverDedekindDomain", _OverDedekindDomain),
    ("OverPID", _OverPID),
    ("OverCommutativeRing", _OverCommutativeRing),
    ("OverField", _OverField),
    ("OverLocalRing", _OverLocalRing),
    ("OverCompleteRing", _OverCompleteRing),
    ("Free", _Free),
    ("Torsion", _Torsion),
    ("Torsionfree", _Torsionfree),
    ("Projective", _Projective),
    ("WithOrderedGeneratingSet", _WithOrderedGeneratingSet),
    ("FinitelyGenerated", _FinitelyGenerated),
    ("FinitelyPresented", _FinitelyPresented),
    ("RIdeals", _RIdeals),
    ("WithForms", _WithForms),
    ("Bilinear", _BilinearModules),
    ("Quadratic", _QuadraticModules),
):
    _category_class._base_category_class_and_axiom = (Modules, _axiom)

_FreeFiniteRank._base_category_class_and_axiom = (_Free, "FiniteRank")

# The specialized ``FinitelyPresented() ∩ OverPID()`` implementation in
# ``specialized.py`` is intentionally not installed here yet.  Installing
# it as ``_FinitelyPresented.OverPID`` recursively re-enters
# ``FinitelyPresented().OverPID()`` once ``OverPID`` is registered as a real
# axiom.  The generic axiom join composes correctly and keeps the category
# surface usable until the meet class is wired with a non-recursive base.
