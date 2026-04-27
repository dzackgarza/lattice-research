"""Centralized type aliases for the module hierarchy.

Only aliases backed by files that exist in this tree are exposed.  The
``ModulesWithForms`` / ``TwistedForms`` aliases from earlier drafts are
dropped until those spec files land.
"""

from collections.abc import Sequence

from sage.categories.homset import Homset as SageHomset
from sage.categories.morphism import Morphism as SageMorphism
from sage.combinat.posets.posets import FinitePoset as SagePoset
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.group import Group as SageGroup
from sage.matrix.matrix0 import Matrix
from sage.monoids.monoid import Monoid_class
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.infinity import InfinityElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial as SagePolynomial
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.real_mpfr import RealNumber as SageRealNumber
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.sets.family import AbstractFamily
from sage.sets.finite_set_map_cy import FiniteSetMap_MN
from sage.sets.real_set import InternalRealInterval
from sage.structure.parent import Parent as SageParent
from sympy.sets.sets import Set as SageSympySet

from .algebras import Algebras
from .homsets import Homsets
from .modules import Modules
from .rings import Rings, _RingIdeals
from .rings.subcategories.complete import _CompleteRings
from .rings.subcategories.field import _Fields
from .rings.subcategories.local import _LocalRings

# Generic / Support
HomsetObject = Homsets.ParentMethods
HomsetElement = Homsets.ElementMethods
Endset = Homsets.Endset.ParentMethods
EndsetElement = Homsets.Endset.ElementMethods
Autset = Homsets.Autset.ParentMethods
AutsetElement = Homsets.Autset.ElementMethods
Ring = Rings.ParentMethods
Field = _Fields.ParentMethods
RingElement = Rings.ElementMethods
RingMorphism = Rings.MorphismMethods
RingHomset = Rings.Homsets.ParentMethods
RingHomsetElement = Rings.MorphismMethods
RingEndset = Rings.Homsets.Endset.ParentMethods
RingEndsetElement = Rings.Homsets.Endset.ElementMethods
RingAutset = Rings.Homsets.Endset.Autset.ParentMethods
RingAutsetElement = Rings.Homsets.Endset.Autset.ElementMethods
Group = SageGroup
AbelianGroup = AbelianGroup_class
Monoid = Monoid_class
Polynomial = SagePolynomial
RealNumberInterval = RealIntervalFieldElement
ComplexInterval = ComplexIntervalFieldElement
Interval = RealNumberInterval | ComplexInterval
Valuation = DiscretePseudoValuation

LocalRing = _LocalRings.ParentMethods
CompleteRing = _CompleteRings.ParentMethods

MatrixEntryOrder = Sequence[tuple[int, int]] | None
Cardinality = Integer | InfinityElement

RMod = Modules
RModule = Modules.ParentMethods
RModuleElement = Modules.ElementMethods
RModMorphism = Modules.MorphismMethods
RModuleMorphism = RModMorphism
FreeModule = Modules.Free.ParentMethods
TorsionModule = Modules.Torsion.ParentMethods
ProjectiveModule = Modules.Projective.ParentMethods
SubModule = Modules.Subobjects.ParentMethods
Submodule = SubModule
QuotientModule = Modules.Quotients.ParentMethods
TensorProductRModule = Modules.TensorProducts.ParentMethods

Ideal = _RingIdeals.ParentMethods
PrimeIdeal = Ideal
MaximalIdeal = PrimeIdeal

RModHomset = Modules.Homsets.ParentMethods
RModHomsetElement = Modules.Homsets.ElementMethods
RModEndset = Modules.Homsets.Endset.ParentMethods
RModEndsetElement = Modules.Homsets.Endset.ElementMethods
RModAutset = Modules.Homsets.Endset.Autset.ParentMethods
RModAutsetElement = Modules.Homsets.Endset.Autset.ElementMethods
RModuleEndSet = RModEndset
RModuleAutSet = RModAutset
RModEndomorphism = RModEndsetElement
RModAutomorphism = RModAutsetElement
RModuleEndomorphism = RModEndomorphism
RModuleHomsetElement = RModMorphism
RModAutSet = RModAutset
DualModule = Modules.DualObjects.ParentMethods
RModDualElement = Modules.DualObjects.ElementMethods
RModuleForm = RModMorphism
BilinearFormsModule = SageHomset
BilinearForm = SageMorphism
QuadraticFormsModule = SageHomset
QuadraticForm = SageMorphism

RAlgebra = Algebras
Algebra = Algebras.ParentMethods
AlgebraElement = Algebras.ElementMethods
AlgebraMorphism = Algebras.MorphismMethods

# Sets
from .sets import Sets
from .sets.homsets import SetHomsets
from .sets.subcategories.constructions.quotients import _Quotients as SetQuotients
from .sets.subcategories.constructions.subobjects import _Subobjects as SetSubobjects
from .topological_spaces import _MetricSpaces, _TopologicalSpaces

Set = Sets.ParentMethods
FiniteSet = Sets.Finite.ParentMethods
CountableSet = Sets.Countable.ParentMethods
InfiniteSet = Sets.Infinite.ParentMethods
UncountableSet = Sets.Uncountable.ParentMethods
Subset = SetSubobjects.ParentMethods
QuotientSet = SetQuotients.ParentMethods
SetElement = Sets.ElementMethods
SetMorphism = Sets.MorphismMethods
SetHomset = SetHomsets.ParentMethods
SetHomsetElement = SetHomsets.ElementMethods
SetEndset = SetHomsets.Endset.ParentMethods
SetEndsetElement = SetHomsets.Endset.ElementMethods
SetAutset = SetHomsets.Autset.ParentMethods
SetAutsetElement = SetHomsets.Autset.ElementMethods
Morphism = SageMorphism
Endomorphism = SageMorphism
Automorphism = SageMorphism
FiniteSetMap = FiniteSetMap_MN
SetFamily = AbstractFamily

RealNumber = SageRealNumber
TopologicalSpace = _TopologicalSpaces.ParentMethods
MetricSpace = _MetricSpaces.ParentMethods
RealSubset = Subset
RealOpenSet = Subset
RealInterval = InternalRealInterval
RealIntervalComponent = RealInterval
PrimeSubset = Subset
PrimesInArithmeticProgressions = PrimeSubset
SympySet = SageSympySet
Poset = SagePoset
Lattice = SageParent
DiscriminantGroup = SageParent
OrthogonalGroup = SageGroup
