"""Centralized type aliases for the module hierarchy.

Only aliases backed by files that exist in this tree are exposed.  The
``ModulesWithForms`` / ``TwistedForms`` aliases from earlier drafts are
dropped until those spec files land.
"""

from collections.abc import Sequence

from sage.categories.cartesian_product import CartesianProductFunctor as SageCartesianProductFunctor
from sage.categories.homset import Homset as SageHomset
from sage.categories.morphism import Morphism as SageMorphism
from sage.combinat.posets.posets import FinitePoset as SagePoset
from sage.graphs.digraph import DiGraph as SageDiGraph
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.group import Group as SageGroup
from sage.homology.free_resolution import FreeResolution as SageFreeResolution
from sage.homology.hochschild_complex import HochschildComplex
from sage.matrix.matrix2 import Matrix as SageMatrix
from sage.matrix.matrix_space import MatrixSpace as SageMatrixSpace
from sage.monoids.monoid import Monoid_class
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.infinity import InfinityElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial as SagePolynomial
from sage.rings.polynomial.term_order import TermOrder as SageTermOrder
from sage.rings.qqbar import AlgebraicPolynomialTracker
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.real_mpfr import RealNumber as SageRealNumber
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.sets.family import AbstractFamily
from sage.sets.finite_set_map_cy import FiniteSetMap_MN
from sage.sets.real_set import InternalRealInterval
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent as SageParent
from sympy.sets.sets import Set as SageSympySet

from .algebras import Algebras
from .homsets import Autsets, Endsets, Homsets
from .modules import Modules
from .modules.homsets import RModuleHomsets
from .posets import Posets
from .posets.subcategories.finite_lattice import _FiniteLatticePosets
from .posets.subcategories.lattice import _LatticePosets
from .rings import Rings, _RingIdeals
from .rings.homsets import RingHomsets
from .rings.subcategories.complete import _CompleteRings
from .rings.subcategories.field import _Fields
from .rings.subcategories.local import _LocalRings

# Generic / Support
CategoryObject = SageParent
CategoryElement = SageElement
Matrix = SageMatrix
MatrixSpace = SageMatrixSpace
DiGraph = SageDiGraph
CartesianProductFunctor = SageCartesianProductFunctor
CategoryOfHomsets = Homsets
CategoryOfEndsets = Endsets
CategoryOfAutsets = Autsets
Homset = Homsets.ParentMethods
Endset = Endsets.ParentMethods
Autset = Autsets.ParentMethods
Morphism = SageMorphism
Endomorphism = SageMorphism
Automorphism = SageMorphism
Ring = Rings.ParentMethods
Field = _Fields.ParentMethods
RingElement = Rings.ElementMethods
RingMorphism = Rings.MorphismMethods
RingHomset = RingHomsets.ParentMethods
RingEndset = RingHomsets.Endset.ParentMethods
RingAutset = RingHomsets.Endset.Autset.ParentMethods
RingEndomorphism = RingHomsets.Endset.ElementMethods
RingAutomorphism = RingHomsets.Endset.Autset.ElementMethods
Group = SageGroup
AbelianGroup = AbelianGroup_class
Monoid = Monoid_class
Polynomial = SagePolynomial
AlgebraicPolynomial = AlgebraicPolynomialTracker
TermOrder = SageTermOrder
RealNumberInterval = RealIntervalFieldElement
ComplexInterval = ComplexIntervalFieldElement
Valuation = DiscretePseudoValuation

LocalRing = _LocalRings.ParentMethods
CompleteRing = _CompleteRings.ParentMethods

Cardinality = Integer | InfinityElement
FreeResolution = SageFreeResolution

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

RModHomset = RModuleHomsets.ParentMethods
RModEndset = RModuleHomsets.Endset.ParentMethods
RModAutset = RModuleHomsets.Endset.Autset.ParentMethods
RModuleEndSet = RModEndset
RModuleAutSet = RModAutset
RModEndomorphism = RModuleHomsets.Endset.ElementMethods
RModAutomorphism = RModuleHomsets.Endset.Autset.ElementMethods
RModuleEndomorphism = RModEndomorphism
RModAutSet = RModAutset
DualModule = RModule
RModDualElement = RModuleElement
RModuleForm = RModMorphism
ModuleStructure = RModMorphism
ModuleBasis = AbstractFamily | Sequence[RModuleElement]
Polyhedron = SageParent
BilinearFormsModule = SageHomset
BilinearForm = SageMorphism
QuadraticFormsModule = SageHomset
QuadraticForm = SageMorphism

RAlgebra = Algebras
Algebra = Algebras.ParentMethods
AlgebraElement = Algebras.ElementMethods
AlgebraMorphism = Algebras.MorphismMethods
AlgebraBasis = AbstractFamily
HochschildChainComplex = HochschildComplex

# Sets
from .posets.homsets import PosetHomsets
from .sets import Sets
from .sets.homsets import SetHomsets
from .sets.subcategories.constructions.isomorphic_objects import _IsomorphicObjects as SetIsomorphicObjects
from .sets.subcategories.constructions.quotients import _Quotients as SetQuotients
from .sets.subcategories.constructions.realizations import _Realizations as SetRealizations
from .sets.subcategories.constructions.subobjects import _Subobjects as SetSubobjects
from .sets.subcategories.constructions.subquotients import _Subquotients as SetSubquotients
from .sets.subcategories.constructions.with_realizations import _WithRealizations as SetWithRealizationsCategory
from .sets.subcategories.graded import _GradedSets
from .sets.subcategories.group_actions import _GSets
from .topological_spaces import _MetricSpaces, _TopologicalSpaces

Set = Sets.ParentMethods
FiniteSet = Sets.Finite.ParentMethods
CountableSet = Sets.Countable.ParentMethods
InfiniteSet = Sets.Infinite.ParentMethods
UncountableSet = Sets.Uncountable.ParentMethods
GradedSet = _GradedSets.ParentMethods
GSet = _GSets.ParentMethods
Subset = SetSubobjects.ParentMethods
OpenSubset = Subset
ClosedSubset = Subset
SetSubquotient = SetSubquotients.ParentMethods
QuotientSet = SetQuotients.ParentMethods
IsomorphicSetObject = SetIsomorphicObjects.ParentMethods
SetWithRealizations = SetWithRealizationsCategory.ParentMethods
SetRealization = SetRealizations.ParentMethods
SetElement = Sets.ElementMethods
SetMorphism = Sets.MorphismMethods
SetHomset = SetHomsets.ParentMethods
SetEndset = SetHomsets.Endset.ParentMethods
SetAutset = SetHomsets.Endset.Autset.ParentMethods
SetEndomorphism = SetHomsets.Endset.ElementMethods
SetAutomorphism = SetHomsets.Endset.Autset.ElementMethods
FiniteSetMap = FiniteSetMap_MN
SetFamily = AbstractFamily
SetGeneratingSeries = SageParent
GroupElement = SageElement
GroupAction = SageMorphism

RealNumber = SageRealNumber
TopologicalSpace = _TopologicalSpaces.ParentMethods
MetricSpace = _MetricSpaces.ParentMethods
TopologicalSpaceMorphism = SageMorphism
RealSubset = Subset
RealOpenSet = OpenSubset
RealInterval = InternalRealInterval
MetricBall = OpenSubset
PrimeSubset = Subset
PrimesInArithmeticProgressions = PrimeSubset
SympySet = SageSympySet
Poset = Posets.ParentMethods
PosetElement = Posets.ElementMethods
PosetMorphism = Posets.MorphismMethods
PosetHomset = PosetHomsets.ParentMethods
PosetEndset = PosetHomsets.Endset.ParentMethods
PosetAutset = PosetHomsets.Endset.Autset.ParentMethods
PosetSubset = Subset
LatticePoset = _LatticePosets.ParentMethods
FiniteLatticePoset = _FiniteLatticePosets.ParentMethods
SageFinitePoset = SagePoset
Lattice = SageParent
DiscriminantGroup = SageParent
OrthogonalGroup = SageGroup
SignaturePair = tuple[Integer, Integer]
IntegralRescaling = tuple[Integer, Lattice]
