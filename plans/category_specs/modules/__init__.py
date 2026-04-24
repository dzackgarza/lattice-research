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

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories import category_with_axiom as _category_with_axiom
from sage.categories.bimodules import Bimodules as SageBimodules
from sage.categories.category_types import Category_module
from sage.categories.dual import DualObjectsCategory
from sage.categories.filtered_modules import FilteredModulesCategory
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.quotients import QuotientsCategory
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.categories.tensor import TensorProductsCategory
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
from .constructions import (
    _CartesianProducts,
    _DualObjects,
    _Quotients,
    _Subobjects,
    _TensorProducts,
)
from .homsets import RModuleHomsets, _RModMorphisms
from .methods import _RModElements, _RModObjects
from .named import _NamedModules
from .support import Categories
from .support import FinSet as FinSet

if TYPE_CHECKING:
    from typing import Protocol

    from sage.categories.homset import Homset
    from sage.categories.morphism import Morphism
    from sage.matrix.matrix0 import Matrix
    from sage.rings.ideal import Ideal_generic
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    Cardinality = Integer | InfinityElement
    Ring = Parent
    RingElement = Element
    RModule = Parent
    RModuleElement = Element
    RModuleMorphism = Morphism
    RModuleHomset = Homset
    RModuleEndSet = Homset
    RModuleAutSet = Homset
    DualRModule = Parent
    FreeModule = Parent
    TorsionModule = Parent
    SubModule = Parent
    QuotientModule = Parent
    Ideal = Ideal_generic
    RModuleForm = Morphism

    class OrderedSet(Protocol):
        def cardinality(self) -> Cardinality: ...

        def __getitem__(self, key: object) -> RModuleElement: ...

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

    @cached_method
    def NamedModules(self):
        r"""Return the named Sage module constructor collector over ``self.base_ring()``."""
        return _NamedModules(self)

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

        ## Named Sage-backed constructors

        @cached_method
        def NamedModules(self):
            r"""Return the named Sage module constructor collector over this base ring."""
            return _NamedModules(self)

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

    WithForms = _WithForms  # Non-full subcategory of pairs (M, f).
    Bilinear = _BilinearModules  # (M, b): b: M \otimes_R M -> S.
    Quadratic = _QuadraticModules  # (M, q): q: M -> S^\sigma.
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
