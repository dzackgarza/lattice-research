"""Centralized type aliases for the category specification hierarchy.

Category modules publish their standard mathematical type packages locally.
This file imports those packages and chooses conventional aliases such as
``Ring = RingsObject`` or ``RModule = ModulesObject``.
"""

from collections.abc import Sequence

from sage.categories.cartesian_product import CartesianProductFunctor as SageCartesianProductFunctor
from sage.categories.homset import Homset as SageHomset
from sage.categories.morphism import Morphism as SageMorphism
from sage.combinat.partition import Partition as SageIntegerPartition
from sage.combinat.posets.posets import FinitePoset as SagePoset
from sage.combinat.set_partition import SetPartition as SageSetPartition
from sage.combinat.set_partition import SetPartitions as SageSetPartitions
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

from .algebras import (
    AlgebrasCategory,
    AlgebrasElement,
    AlgebrasMorphism,
    AlgebrasObject,
)
from .homsets import (
    AutCategoriesCategory,
    AutCategoriesObject,
    EndCategoriesCategory,
    EndCategoriesObject,
    HomCategoriesCategory,
    HomCategoriesObject,
)
from .forms import (
    BilinearModulesAut,
    BilinearModulesAutCategory,
    BilinearModulesAutomorphism,
    BilinearModulesCategory,
    BilinearModulesElement,
    BilinearModulesEnd,
    BilinearModulesEndCategory,
    BilinearModulesEndomorphism,
    BilinearModulesHom,
    BilinearModulesHomCategory,
    BilinearModulesMorphism,
    BilinearModulesObject,
    FormedModulesAut,
    FormedModulesAutCategory,
    FormedModulesAutomorphism,
    FormedModulesCategory,
    FormedModulesElement,
    FormedModulesEnd,
    FormedModulesEndCategory,
    FormedModulesEndomorphism,
    FormedModulesHom,
    FormedModulesHomCategory,
    FormedModulesMorphism,
    FormedModulesObject,
    QuadraticModulesAut,
    QuadraticModulesAutCategory,
    QuadraticModulesAutomorphism,
    QuadraticModulesCategory,
    QuadraticModulesElement,
    QuadraticModulesEnd,
    QuadraticModulesEndCategory,
    QuadraticModulesEndomorphism,
    QuadraticModulesHom,
    QuadraticModulesHomCategory,
    QuadraticModulesMorphism,
    QuadraticModulesObject,
    TorsionQuadraticModulesAut,
    TorsionQuadraticModulesAutCategory,
    TorsionQuadraticModulesAutomorphism,
    TorsionQuadraticModulesCategory,
    TorsionQuadraticModulesElement,
    TorsionQuadraticModulesEnd,
    TorsionQuadraticModulesEndCategory,
    TorsionQuadraticModulesEndomorphism,
    TorsionQuadraticModulesHom,
    TorsionQuadraticModulesHomCategory,
    TorsionQuadraticModulesMorphism,
    TorsionQuadraticModulesObject,
)
from .lattices import (
    LatticesAut,
    LatticesAutCategory,
    LatticesAutomorphism,
    LatticesCategory,
    LatticesElement,
    LatticesEnd,
    LatticesEndCategory,
    LatticesEndomorphism,
    LatticesHom,
    LatticesHomCategory,
    LatticesMorphism,
    LatticesObject,
)
from .lattices.subcategories.constructions.discriminant_groups import (
    LatticeDiscriminantGroupsAut,
    LatticeDiscriminantGroupsAutCategory,
    LatticeDiscriminantGroupsAutomorphism,
    LatticeDiscriminantGroupsCategory,
    LatticeDiscriminantGroupsElement,
    LatticeDiscriminantGroupsEnd,
    LatticeDiscriminantGroupsEndCategory,
    LatticeDiscriminantGroupsEndomorphism,
    LatticeDiscriminantGroupsHom,
    LatticeDiscriminantGroupsHomCategory,
    LatticeDiscriminantGroupsMorphism,
    LatticeDiscriminantGroupsObject,
)
from .modules import (
    ModulesAut,
    ModulesAutomorphism,
    ModulesCategory,
    ModulesElement,
    ModulesEnd,
    ModulesEndomorphism,
    ModulesHom,
    ModulesMorphism,
    ModulesObject,
)
from .posets import (
    PosetsAut,
    PosetsElement,
    PosetsEnd,
    PosetsHom,
    PosetsMorphism,
    PosetsObject,
)
from .posets.subcategories.finite_join_semilattice import _FiniteJoinSemilatticePosets
from .posets.subcategories.finite_lattice import _FiniteLatticePosets
from .posets.subcategories.finite_meet_semilattice import _FiniteMeetSemilatticePosets
from .posets.subcategories.join_semilattice import _JoinSemilatticePosets
from .posets.subcategories.lattice import _LatticePosets
from .posets.subcategories.meet_semilattice import _MeetSemilatticePosets
from .rings import (
    RingsAut,
    RingsAutomorphism,
    RingsElement,
    RingsEnd,
    RingsEndomorphism,
    RingsHom,
    RingsMorphism,
    RingsObject,
    _RingIdeals,
)
from .rings.subcategories.approximate import (
    ApproximateRingsCategory,
    ApproximateRingsElement,
    ApproximateRingsMorphism,
    ApproximateRingsObject,
)
from .rings.subcategories.complete import _CompleteRings
from .rings.subcategories.field import _Fields
from .rings.subcategories.local import _LocalRings
from .tensor_algebra_components import (
    TensorAlgebraComponent,
    TensorAlgebraComponentsObject,
)

# Generic / Support
CategoryObject = SageParent
CategoryElement = SageElement
Matrix = SageMatrix
MatrixSpace = SageMatrixSpace
DiGraph = SageDiGraph
CartesianProductFunctor = SageCartesianProductFunctor
CategoryOfHomCategories = HomCategoriesCategory
CategoryOfEndCategories = EndCategoriesCategory
CategoryOfAutCategories = AutCategoriesCategory
Hom = HomCategoriesObject
End = EndCategoriesObject
Aut = AutCategoriesObject
Morphism = SageMorphism
Endomorphism = SageMorphism
Automorphism = SageMorphism
Ring = RingsObject
Field = _Fields.ParentMethods
RingElement = RingsElement
RingMorphism = RingsMorphism
RingHom = RingsHom
RingEnd = RingsEnd
RingAut = RingsAut
RingEndomorphism = RingsEndomorphism
RingAutomorphism = RingsAutomorphism
ApproximateRing = ApproximateRingsObject
ApproximateRingElement = ApproximateRingsElement
ApproximateRingMorphism = ApproximateRingsMorphism
ApproximateRingCategory = ApproximateRingsCategory
Group = SageGroup
AbelianGroup = AbelianGroup_class
Magma = CategoryObject
Semigroup = CategoryObject
Monoid = Monoid_class
AdditiveSemigroup = CategoryObject
AdditiveMonoid = CategoryObject
AdditiveGroup = CategoryObject
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

RMod = ModulesCategory
RModule = ModulesObject
RModuleElement = ModulesElement
RModMorphism = ModulesMorphism
RModuleMorphism = RModMorphism
FreeModule = ModulesCategory.Free.ParentMethods
TorsionModule = ModulesCategory.Torsion.ParentMethods
ProjectiveModule = ModulesCategory.Projective.ParentMethods
SubModule = ModulesCategory.Subobjects.ParentMethods
Submodule = SubModule
QuotientModule = ModulesCategory.Quotients.ParentMethods
TensorProductRModule = ModulesCategory.TensorProducts.ParentMethods
TensorAlgebraComponent = TensorAlgebraComponentsObject

Ideal = _RingIdeals.ParentMethods
PrimeIdeal = Ideal
MaximalIdeal = PrimeIdeal

RModHom = ModulesHom
RModEnd = ModulesEnd
RModAut = ModulesAut
RModuleEnd = RModEnd
RModuleAut = RModAut
RModEndomorphism = ModulesEndomorphism
RModAutomorphism = ModulesAutomorphism
RModuleEndomorphism = RModEndomorphism
RModuleAutomorphism = RModAutomorphism
DualModule = RModule
RModDualElement = RModuleElement
RModuleForm = RModMorphism
ModuleStructure = RModMorphism
ModuleBasis = AbstractFamily | Sequence[RModuleElement]
Polyhedron = SageParent
FormedModuleCategory = FormedModulesCategory
FormedModule = FormedModulesObject
FormedModuleElement = FormedModulesElement
FormedModuleMorphism = FormedModulesMorphism
FormedModuleHom = FormedModulesHom
FormedModuleEnd = FormedModulesEnd
FormedModuleAut = FormedModulesAut
FormedModuleHomCategory = FormedModulesHomCategory
FormedModuleEndCategory = FormedModulesEndCategory
FormedModuleAutCategory = FormedModulesAutCategory
FormedModuleEndomorphism = FormedModulesEndomorphism
FormedModuleAutomorphism = FormedModulesAutomorphism
BilinearModuleCategory = BilinearModulesCategory
BilinearModule = BilinearModulesObject
BilinearModuleElement = BilinearModulesElement
BilinearModuleMorphism = BilinearModulesMorphism
BilinearModuleHom = BilinearModulesHom
BilinearModuleEnd = BilinearModulesEnd
BilinearModuleAut = BilinearModulesAut
BilinearModuleHomCategory = BilinearModulesHomCategory
BilinearModuleEndCategory = BilinearModulesEndCategory
BilinearModuleAutCategory = BilinearModulesAutCategory
BilinearModuleEndomorphism = BilinearModulesEndomorphism
BilinearModuleAutomorphism = BilinearModulesAutomorphism
QuadraticModuleCategory = QuadraticModulesCategory
QuadraticModule = QuadraticModulesObject
QuadraticModuleElement = QuadraticModulesElement
QuadraticModuleMorphism = QuadraticModulesMorphism
QuadraticModuleHom = QuadraticModulesHom
QuadraticModuleEnd = QuadraticModulesEnd
QuadraticModuleAut = QuadraticModulesAut
QuadraticModuleHomCategory = QuadraticModulesHomCategory
QuadraticModuleEndCategory = QuadraticModulesEndCategory
QuadraticModuleAutCategory = QuadraticModulesAutCategory
QuadraticModuleEndomorphism = QuadraticModulesEndomorphism
QuadraticModuleAutomorphism = QuadraticModulesAutomorphism
TorsionQuadraticModuleCategory = TorsionQuadraticModulesCategory
TorsionQuadraticModule = TorsionQuadraticModulesObject
TorsionQuadraticModuleElement = TorsionQuadraticModulesElement
TorsionQuadraticModuleMorphism = TorsionQuadraticModulesMorphism
TorsionQuadraticModuleHom = TorsionQuadraticModulesHom
TorsionQuadraticModuleEnd = TorsionQuadraticModulesEnd
TorsionQuadraticModuleAut = TorsionQuadraticModulesAut
TorsionQuadraticModuleHomCategory = TorsionQuadraticModulesHomCategory
TorsionQuadraticModuleEndCategory = TorsionQuadraticModulesEndCategory
TorsionQuadraticModuleAutCategory = TorsionQuadraticModulesAutCategory
TorsionQuadraticModuleEndomorphism = TorsionQuadraticModulesEndomorphism
TorsionQuadraticModuleAutomorphism = TorsionQuadraticModulesAutomorphism
BilinearFormsModule = SageHomset
BilinearForm = SageMorphism
QuadraticFormsModule = SageHomset
QuadraticForm = SageMorphism

RAlgebra = AlgebrasCategory
Algebra = AlgebrasObject
AlgebraElement = AlgebrasElement
AlgebraMorphism = AlgebrasMorphism
AlgebraBasis = AbstractFamily
HochschildChainComplex = HochschildComplex

# Sets
from .sets import (
    SetsAut,
    SetsAutomorphism,
    SetsCategory,
    SetsElement,
    SetsEnd,
    SetsEndomorphism,
    SetsHom,
    SetsMorphism,
    SetsObject,
)
from .sets.subcategories.constructions.isomorphic_objects import _IsomorphicObjects as SetIsomorphicObjects
from .sets.subcategories.constructions.quotients import _Quotients as SetQuotients
from .sets.subcategories.constructions.realizations import _Realizations as SetRealizations
from .sets.subcategories.constructions.subobjects import _Subobjects as SetSubobjects
from .sets.subcategories.constructions.subquotients import _Subquotients as SetSubquotients
from .sets.subcategories.constructions.with_realizations import _WithRealizations as SetWithRealizationsCategory
from .sets.subcategories.graded import _GradedSets
from .sets.subcategories.group_actions import _GSets
from .sets.subcategories.partitioned import (
    PartitionedSetsAut,
    PartitionedSetsAutCategory,
    PartitionedSetsAutomorphism,
    PartitionedSetsCategory,
    PartitionedSetsElement,
    PartitionedSetsEnd,
    PartitionedSetsEndCategory,
    PartitionedSetsEndomorphism,
    PartitionedSetsHom,
    PartitionedSetsHomCategory,
    PartitionedSetsMorphism,
    PartitionedSetsObject,
)
from .topological_spaces import (
    MetricSpacesObject,
    TopologicalSpacesMorphism,
    TopologicalSpacesObject,
)

Set = SetsObject
FiniteSet = SetsCategory.Finite.ParentMethods
CountableSet = SetsCategory.Countable.ParentMethods
InfiniteSet = SetsCategory.Infinite.ParentMethods
UncountableSet = SetsCategory.Uncountable.ParentMethods
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
SetElement = SetsElement
SetMorphism = SetsMorphism
SetHom = SetsHom
SetEnd = SetsEnd
SetAut = SetsAut
SetEndomorphism = SetsEndomorphism
SetAutomorphism = SetsAutomorphism
FiniteSetMap = FiniteSetMap_MN
SetFamily = AbstractFamily
SetGeneratingSeries = SageParent
IntegerPartition = SageIntegerPartition
SetPartition = SageSetPartition
SetPartitionsParent = SageSetPartitions
PartitionedSet = PartitionedSetsObject
PartitionedSetElement = PartitionedSetsElement
PartitionedSetMorphism = PartitionedSetsMorphism
PartitionedSetHom = PartitionedSetsHom
PartitionedSetEnd = PartitionedSetsEnd
PartitionedSetAut = PartitionedSetsAut
PartitionedSetEndomorphism = PartitionedSetsEndomorphism
PartitionedSetAutomorphism = PartitionedSetsAutomorphism
PartitionedSetHomCategory = PartitionedSetsHomCategory
PartitionedSetEndCategory = PartitionedSetsEndCategory
PartitionedSetAutCategory = PartitionedSetsAutCategory
PartitionedSetCategory = PartitionedSetsCategory
SetPartitionSet = PartitionedSet
EquivalenceRelation = SetPartition
GroupElement = SageElement
GroupAction = SageMorphism

RealNumber = SageRealNumber
TopologicalSpace = TopologicalSpacesObject
MetricSpace = MetricSpacesObject
TopologicalSpaceMorphism = TopologicalSpacesMorphism
RealSubset = Subset
RealOpenSet = OpenSubset
RealInterval = InternalRealInterval
MetricBall = OpenSubset
PrimeSubset = Subset
PrimesInArithmeticProgressions = PrimeSubset
SympySet = SageSympySet
Poset = PosetsObject
PosetElement = PosetsElement
PosetMorphism = PosetsMorphism
PosetHom = PosetsHom
PosetEnd = PosetsEnd
PosetAut = PosetsAut
PosetSubset = Subset
MeetSemilatticePoset = _MeetSemilatticePosets.ParentMethods
JoinSemilatticePoset = _JoinSemilatticePosets.ParentMethods
LatticePoset = _LatticePosets.ParentMethods
FiniteMeetSemilatticePoset = _FiniteMeetSemilatticePosets.ParentMethods
FiniteJoinSemilatticePoset = _FiniteJoinSemilatticePosets.ParentMethods
FiniteLatticePoset = _FiniteLatticePosets.ParentMethods
SageFinitePoset = SagePoset
LatticeCategory = LatticesCategory
Lattice = LatticesObject
LatticeElement = LatticesElement
LatticeMorphism = LatticesMorphism
LatticeHom = LatticesHom
LatticeEnd = LatticesEnd
LatticeAut = LatticesAut
LatticeHomCategory = LatticesHomCategory
LatticeEndCategory = LatticesEndCategory
LatticeAutCategory = LatticesAutCategory
LatticeEndomorphism = LatticesEndomorphism
LatticeAutomorphism = LatticesAutomorphism
DiscriminantGroupCategory = LatticeDiscriminantGroupsCategory
DiscriminantGroup = LatticeDiscriminantGroupsObject
DiscriminantGroupElement = LatticeDiscriminantGroupsElement
DiscriminantGroupMorphism = LatticeDiscriminantGroupsMorphism
DiscriminantGroupHom = LatticeDiscriminantGroupsHom
DiscriminantGroupEnd = LatticeDiscriminantGroupsEnd
DiscriminantGroupAut = LatticeDiscriminantGroupsAut
DiscriminantGroupHomCategory = LatticeDiscriminantGroupsHomCategory
DiscriminantGroupEndCategory = LatticeDiscriminantGroupsEndCategory
DiscriminantGroupAutCategory = LatticeDiscriminantGroupsAutCategory
DiscriminantGroupEndomorphism = LatticeDiscriminantGroupsEndomorphism
DiscriminantGroupAutomorphism = LatticeDiscriminantGroupsAutomorphism
OrthogonalGroup = RModAut
OrthogonalAutomorphism = RModAutomorphism
LatticeOrthogonalGroup = LatticeAut
LatticeIsometry = LatticeAutomorphism
SignaturePair = tuple[Integer, Integer]
IntegralRescaling = tuple[Integer, Lattice]
