"""Centralized type aliases for the category specification hierarchy.

Category modules publish their standard mathematical type packages locally.
This file imports those packages and chooses conventional aliases such as
``Ring = RingsObject`` or ``RModule = ModulesObject``.
"""

from collections.abc import Sequence

from sage.categories.cartesian_product import (
    CartesianProductFunctor as SageCartesianProductFunctor,
)
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
    AlgebrasAut,
    AlgebrasAutCategory,
    AlgebrasAutomorphism,
    AlgebrasCategory,
    AlgebrasElement,
    AlgebrasEnd,
    AlgebrasEndCategory,
    AlgebrasEndomorphism,
    AlgebrasHom,
    AlgebrasHomCategory,
    AlgebrasMorphism,
    AlgebrasObject,
    AssociativeAlgebrasCategory,
    AssociativeAlgebrasElement,
    AssociativeAlgebrasMorphism,
    AssociativeAlgebrasObject,
    MagmaticAlgebrasCategory,
    MagmaticAlgebrasElement,
    MagmaticAlgebrasMorphism,
    MagmaticAlgebrasObject,
)
from .algebras.subcategories.constructions.ideals import AlgebraIdealsObject
from .cat import (
    CatAut,
    CatAutCategory,
    CatAutomorphism,
    CatCategory,
    CatElement,
    CatEnd,
    CatEndCategory,
    CatEndomorphism,
    CatHom,
    CatHomCategory,
    CatMorphism,
    CatObject,
)
from .cat import (
    Category as CatBaseCategory,
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
from .homsets import (
    AutCategoriesCategory,
    AutCategoriesElement,
    AutCategoriesMorphism,
    AutCategoriesObject,
    EndCategoriesCategory,
    EndCategoriesElement,
    EndCategoriesMorphism,
    EndCategoriesObject,
    HomCategoriesCategory,
    HomCategoriesElement,
    HomCategoriesMorphism,
    HomCategoriesObject,
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
    ModulesAutCategory,
    ModulesAutomorphism,
    ModulesCategory,
    ModulesElement,
    ModulesEnd,
    ModulesEndCategory,
    ModulesEndomorphism,
    ModulesHom,
    ModulesHomCategory,
    ModulesMorphism,
    ModulesObject,
)
from .modules.subcategories.constructions.dual_objects import (
    _DualObjects as ModuleDualObjects,
)
from .posets import (
    PosetsAut,
    PosetsAutCategory,
    PosetsAutomorphism,
    PosetsCategory,
    PosetsElement,
    PosetsEnd,
    PosetsEndCategory,
    PosetsEndomorphism,
    PosetsHom,
    PosetsHomCategory,
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
    RingsAutCategory,
    RingsAutomorphism,
    RingsCategory,
    RingsElement,
    RingsEnd,
    RingsEndCategory,
    RingsEndomorphism,
    RingsHom,
    RingsHomCategory,
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
from .sets import (
    SetsAut,
    SetsAutCategory,
    SetsAutomorphism,
    SetsCategory,
    SetsElement,
    SetsEnd,
    SetsEndCategory,
    SetsEndomorphism,
    SetsHom,
    SetsHomCategory,
    SetsMorphism,
    SetsObject,
)
from .sets.subcategories.constructions.isomorphic_objects import (
    _IsomorphicObjects as SetIsomorphicObjects,
)
from .sets.subcategories.constructions.quotients import _Quotients as SetQuotients
from .sets.subcategories.constructions.realizations import (
    _Realizations as SetRealizations,
)
from .sets.subcategories.constructions.subobjects import Subsets as SetSubobjects
from .sets.subcategories.constructions.subquotients import (
    _Subquotients as SetSubquotients,
)
from .sets.subcategories.constructions.with_realizations import (
    SetsWithRealizations as SetWithRealizationsCategory,
)
from .sets.subcategories.graded import GradedSetsCategory
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
from .tensor_algebra_components import (
    TensorAlgebraComponentsAut,
    TensorAlgebraComponentsAutCategory,
    TensorAlgebraComponentsAutomorphism,
    TensorAlgebraComponentsCategory,
    TensorAlgebraComponentsElement,
    TensorAlgebraComponentsEnd,
    TensorAlgebraComponentsEndCategory,
    TensorAlgebraComponentsEndomorphism,
    TensorAlgebraComponentsHom,
    TensorAlgebraComponentsHomCategory,
    TensorAlgebraComponentsMorphism,
    TensorAlgebraComponentsObject,
)
from .topological_spaces import (
    MetricSpacesAut,
    MetricSpacesAutCategory,
    MetricSpacesAutomorphism,
    MetricSpacesCategory,
    MetricSpacesElement,
    MetricSpacesEnd,
    MetricSpacesEndCategory,
    MetricSpacesEndomorphism,
    MetricSpacesHom,
    MetricSpacesHomCategory,
    MetricSpacesMorphism,
    MetricSpacesObject,
    TopologicalSpacesAut,
    TopologicalSpacesAutCategory,
    TopologicalSpacesAutomorphism,
    TopologicalSpacesCategory,
    TopologicalSpacesElement,
    TopologicalSpacesEnd,
    TopologicalSpacesEndCategory,
    TopologicalSpacesEndomorphism,
    TopologicalSpacesHom,
    TopologicalSpacesHomCategory,
    TopologicalSpacesMorphism,
    TopologicalSpacesObject,
)

# Generic / Support
type Category = CatBaseCategory
type CategoryObject = SageParent
type CategoryElement = SageElement
type Matrix = SageMatrix
type MatrixSpace = SageMatrixSpace
type DiGraph = SageDiGraph
type CartesianProductFunctor = SageCartesianProductFunctor
type CategoryOfHomCategories = HomCategoriesCategory
type CategoryOfEndCategories = EndCategoriesCategory
type CategoryOfAutCategories = AutCategoriesCategory
type Hom = HomCategoriesObject
type End = EndCategoriesObject
type Aut = AutCategoriesObject
type Morphism = SageMorphism
type Endomorphism = SageMorphism
type Automorphism = SageMorphism
type Ring = RingsObject
type Field = _Fields.ParentMethods
type RingElement = RingsElement
type RingMorphism = RingsMorphism
type RingHom = RingsHom
type RingEnd = RingsEnd
type RingAut = RingsAut
type RingEndomorphism = RingsEndomorphism
type RingAutomorphism = RingsAutomorphism
type ApproximateRing = ApproximateRingsObject
type ApproximateRingElement = ApproximateRingsElement
type ApproximateRingMorphism = ApproximateRingsMorphism
type ApproximateRingCategory = ApproximateRingsCategory
type Group = SageGroup
type AbelianGroup = AbelianGroup_class
type Magma = CategoryObject
type Semigroup = CategoryObject
type Monoid = Monoid_class
type AdditiveSemigroup = CategoryObject
type AdditiveMonoid = CategoryObject
type AdditiveGroup = CategoryObject
type Polynomial = SagePolynomial
type AlgebraicPolynomial = AlgebraicPolynomialTracker
type TermOrder = SageTermOrder
type RealNumberInterval = RealIntervalFieldElement
type ComplexInterval = ComplexIntervalFieldElement
type Valuation = DiscretePseudoValuation

type LocalRing = _LocalRings.ParentMethods
type CompleteRing = _CompleteRings.ParentMethods

type Cardinality = Integer | InfinityElement
type FreeResolution = SageFreeResolution

type RMod = ModulesCategory
type RModule = ModulesObject
type RModuleElement = ModulesElement
type RModMorphism = ModulesMorphism
type RModuleMorphism = RModMorphism
type FreeModule = ModulesCategory.Free.ParentMethods
type TorsionModule = ModulesCategory.Torsion.ParentMethods
type ProjectiveModule = ModulesCategory.Projective.ParentMethods
type SubModule = ModulesCategory.Subobjects.ParentMethods
type Submodule = SubModule
type QuotientModule = ModulesCategory.Quotients.ParentMethods
type TensorProductRModule = ModulesCategory.TensorProducts.ParentMethods
type TensorAlgebraComponent = TensorAlgebraComponentsObject
type Tensor = TensorAlgebraComponentsElement

type Ideal = _RingIdeals.ParentMethods
type PrimeIdeal = Ideal
type MaximalIdeal = PrimeIdeal

type RModHom = ModulesHom
type RModEnd = ModulesEnd
type RModAut = ModulesAut
type RModuleEnd = RModEnd
type RModuleAut = RModAut
type RModEndomorphism = ModulesEndomorphism
type RModAutomorphism = ModulesAutomorphism
type RModuleEndomorphism = RModEndomorphism
type RModuleAutomorphism = RModAutomorphism
type DualModule = ModuleDualObjects.ParentMethods
type DualModuleElement = ModuleDualObjects.ElementMethods
type DualModuleMorphism = ModuleDualObjects.MorphismMethods
type RModDual = DualModule
type RModuleDual = DualModule
type RModDualElement = DualModuleElement
type RModuleDualElement = DualModuleElement
type RModDualMorphism = DualModuleMorphism
type RModuleDualMorphism = DualModuleMorphism
type RModuleForm = RModMorphism
type ModuleStructure = RModMorphism
type ModuleBasis = AbstractFamily | Sequence[RModuleElement]
type Polyhedron = SageParent
type FormedModuleCategory = FormedModulesCategory
type FormedModule = FormedModulesObject
type FormedModuleElement = FormedModulesElement
type FormedModuleMorphism = FormedModulesMorphism
type FormedModuleHom = FormedModulesHom
type FormedModuleEnd = FormedModulesEnd
type FormedModuleAut = FormedModulesAut
type FormedModuleHomCategory = FormedModulesHomCategory
type FormedModuleEndCategory = FormedModulesEndCategory
type FormedModuleAutCategory = FormedModulesAutCategory
type FormedModuleEndomorphism = FormedModulesEndomorphism
type FormedModuleAutomorphism = FormedModulesAutomorphism
type BilinearModuleCategory = BilinearModulesCategory
type BilinearModule = BilinearModulesObject
type BilinearModuleElement = BilinearModulesElement
type BilinearModuleMorphism = BilinearModulesMorphism
type BilinearModuleHom = BilinearModulesHom
type BilinearModuleEnd = BilinearModulesEnd
type BilinearModuleAut = BilinearModulesAut
type BilinearModuleHomCategory = BilinearModulesHomCategory
type BilinearModuleEndCategory = BilinearModulesEndCategory
type BilinearModuleAutCategory = BilinearModulesAutCategory
type BilinearModuleEndomorphism = BilinearModulesEndomorphism
type BilinearModuleAutomorphism = BilinearModulesAutomorphism
type QuadraticModuleCategory = QuadraticModulesCategory
type QuadraticModule = QuadraticModulesObject
type QuadraticModuleElement = QuadraticModulesElement
type QuadraticModuleMorphism = QuadraticModulesMorphism
type QuadraticModuleHom = QuadraticModulesHom
type QuadraticModuleEnd = QuadraticModulesEnd
type QuadraticModuleAut = QuadraticModulesAut
type QuadraticModuleHomCategory = QuadraticModulesHomCategory
type QuadraticModuleEndCategory = QuadraticModulesEndCategory
type QuadraticModuleAutCategory = QuadraticModulesAutCategory
type QuadraticModuleEndomorphism = QuadraticModulesEndomorphism
type QuadraticModuleAutomorphism = QuadraticModulesAutomorphism
type TorsionQuadraticModuleCategory = TorsionQuadraticModulesCategory
type TorsionQuadraticModule = TorsionQuadraticModulesObject
type TorsionQuadraticModuleElement = TorsionQuadraticModulesElement
type TorsionQuadraticModuleMorphism = TorsionQuadraticModulesMorphism
type TorsionQuadraticModuleHom = TorsionQuadraticModulesHom
type TorsionQuadraticModuleEnd = TorsionQuadraticModulesEnd
type TorsionQuadraticModuleAut = TorsionQuadraticModulesAut
type TorsionQuadraticModuleHomCategory = TorsionQuadraticModulesHomCategory
type TorsionQuadraticModuleEndCategory = TorsionQuadraticModulesEndCategory
type TorsionQuadraticModuleAutCategory = TorsionQuadraticModulesAutCategory
type TorsionQuadraticModuleEndomorphism = TorsionQuadraticModulesEndomorphism
type TorsionQuadraticModuleAutomorphism = TorsionQuadraticModulesAutomorphism
type BilinearFormsModule = SageHomset
type BilinearForm = SageMorphism
type QuadraticFormsModule = SageHomset
type QuadraticForm = SageMorphism

type RAlgebra = AlgebrasCategory
type Algebra = AlgebrasObject
type AlgebraElement = AlgebrasElement
type AlgebraMorphism = AlgebrasMorphism
type MagmaticAlgebraCategory = MagmaticAlgebrasCategory
type MagmaticAlgebra = MagmaticAlgebrasObject
type MagmaticAlgebraElement = MagmaticAlgebrasElement
type MagmaticAlgebraMorphism = MagmaticAlgebrasMorphism
type AssociativeAlgebraCategory = AssociativeAlgebrasCategory
type AssociativeAlgebra = AssociativeAlgebrasObject
type AssociativeAlgebraElement = AssociativeAlgebrasElement
type AssociativeAlgebraMorphism = AssociativeAlgebrasMorphism
type AlgebraBasis = AbstractFamily
type AlgebraIdeal = AlgebraIdealsObject
type HochschildChainComplex = HochschildComplex

# Sets

type Set = SetsObject
type FiniteSet = SetsCategory.Finite.ParentMethods
type CountableSet = SetsCategory.Countable.ParentMethods
type InfiniteSet = SetsCategory.Infinite.ParentMethods
type UncountableSet = SetsCategory.Uncountable.ParentMethods
type GradedSet = GradedSetsCategory.ParentMethods
type GSet = _GSets.ParentMethods
type Subset = SetSubobjects.ParentMethods
type OpenSubset = Subset
type ClosedSubset = Subset
type SetSubquotient = SetSubquotients.ParentMethods
type QuotientSet = SetQuotients.ParentMethods
type IsomorphicSetObject = SetIsomorphicObjects.ParentMethods
type SetWithRealizations = SetWithRealizationsCategory.ParentMethods
type SetRealization = SetRealizations.ParentMethods
type SetElement = SetsElement
type SetMorphism = SetsMorphism
type SetHom = SetsHom
type SetEnd = SetsEnd
type SetAut = SetsAut
type SetEndomorphism = SetsEndomorphism
type SetAutomorphism = SetsAutomorphism
type FiniteSetMap = FiniteSetMap_MN
type SetFamily = AbstractFamily
type SetGeneratingSeries = SageParent
type IntegerPartition = SageIntegerPartition
type SetPartition = SageSetPartition
type SetPartitionsParent = SageSetPartitions
type PartitionedSet = PartitionedSetsObject
type PartitionedSetElement = PartitionedSetsElement
type PartitionedSetMorphism = PartitionedSetsMorphism
type PartitionedSetHom = PartitionedSetsHom
type PartitionedSetEnd = PartitionedSetsEnd
type PartitionedSetAut = PartitionedSetsAut
type PartitionedSetEndomorphism = PartitionedSetsEndomorphism
type PartitionedSetAutomorphism = PartitionedSetsAutomorphism
type PartitionedSetHomCategory = PartitionedSetsHomCategory
type PartitionedSetEndCategory = PartitionedSetsEndCategory
type PartitionedSetAutCategory = PartitionedSetsAutCategory
type PartitionedSetCategory = PartitionedSetsCategory
type SetPartitionSet = PartitionedSet
type EquivalenceRelation = SetPartition
type GroupElement = SageElement
type GroupAction = SageMorphism

type RealNumber = SageRealNumber
type TopologicalSpace = TopologicalSpacesObject
type MetricSpace = MetricSpacesObject
type TopologicalSpaceMorphism = TopologicalSpacesMorphism
type RealSubset = Subset
type RealOpenSet = OpenSubset
type RealInterval = InternalRealInterval
type MetricBall = OpenSubset
type PrimeSubset = Subset
type PrimesInArithmeticProgressions = PrimeSubset
type SympySet = SageSympySet
type Poset = PosetsObject
type PosetElement = PosetsElement
type PosetMorphism = PosetsMorphism
type PosetHom = PosetsHom
type PosetEnd = PosetsEnd
type PosetAut = PosetsAut
type PosetSubset = Subset
type MeetSemilatticePoset = _MeetSemilatticePosets.ParentMethods
type JoinSemilatticePoset = _JoinSemilatticePosets.ParentMethods
type LatticePoset = _LatticePosets.ParentMethods
type FiniteMeetSemilatticePoset = _FiniteMeetSemilatticePosets.ParentMethods
type FiniteJoinSemilatticePoset = _FiniteJoinSemilatticePosets.ParentMethods
type FiniteLatticePoset = _FiniteLatticePosets.ParentMethods
type SageFinitePoset = SagePoset
type LatticeCategory = LatticesCategory
type Lattice = LatticesObject
type LatticeElement = LatticesElement
type LatticeMorphism = LatticesMorphism
type LatticeHom = LatticesHom
type LatticeEnd = LatticesEnd
type LatticeAut = LatticesAut
type LatticeHomCategory = LatticesHomCategory
type LatticeEndCategory = LatticesEndCategory
type LatticeAutCategory = LatticesAutCategory
type LatticeEndomorphism = LatticesEndomorphism
type LatticeAutomorphism = LatticesAutomorphism
type DiscriminantGroupCategory = LatticeDiscriminantGroupsCategory
type DiscriminantGroup = LatticeDiscriminantGroupsObject
type DiscriminantGroupElement = LatticeDiscriminantGroupsElement
type DiscriminantGroupMorphism = LatticeDiscriminantGroupsMorphism
type DiscriminantGroupHom = LatticeDiscriminantGroupsHom
type DiscriminantGroupEnd = LatticeDiscriminantGroupsEnd
type DiscriminantGroupAut = LatticeDiscriminantGroupsAut
type DiscriminantGroupHomCategory = LatticeDiscriminantGroupsHomCategory
type DiscriminantGroupEndCategory = LatticeDiscriminantGroupsEndCategory
type DiscriminantGroupAutCategory = LatticeDiscriminantGroupsAutCategory
type DiscriminantGroupEndomorphism = LatticeDiscriminantGroupsEndomorphism
type DiscriminantGroupAutomorphism = LatticeDiscriminantGroupsAutomorphism
type OrthogonalGroup = RModAut
type OrthogonalAutomorphism = RModAutomorphism
type LatticeOrthogonalGroup = LatticeAut
type LatticeIsometry = LatticeAutomorphism
type SignaturePair = tuple[Integer, Integer]
type IntegralRescaling = tuple[Integer, Lattice]


class CatTypes:
    Category = CatCategory
    Object = CatObject
    Element = CatElement
    Morphism = CatMorphism
    HomCategory = CatHomCategory
    EndCategory = CatEndCategory
    AutCategory = CatAutCategory
    Hom = CatHom
    End = CatEnd
    Aut = CatAut
    Endomorphism = CatEndomorphism
    Automorphism = CatAutomorphism


class HomCategoryTypes:
    Category = HomCategoriesCategory
    Object = HomCategoriesObject
    Element = HomCategoriesElement
    Morphism = HomCategoriesMorphism


class EndCategoryTypes:
    Category = EndCategoriesCategory
    Object = EndCategoriesObject
    Element = EndCategoriesElement
    Morphism = EndCategoriesMorphism


class AutCategoryTypes:
    Category = AutCategoriesCategory
    Object = AutCategoriesObject
    Element = AutCategoriesElement
    Morphism = AutCategoriesMorphism


class SetTypes:
    Category = SetsCategory
    Object = SetsObject
    Element = SetsElement
    Morphism = SetsMorphism
    HomCategory = SetsHomCategory
    EndCategory = SetsEndCategory
    AutCategory = SetsAutCategory
    Hom = SetsHom
    End = SetsEnd
    Aut = SetsAut
    Endomorphism = SetsEndomorphism
    Automorphism = SetsAutomorphism


class RingTypes:
    Category = RingsCategory
    Object = RingsObject
    Element = RingsElement
    Morphism = RingsMorphism
    HomCategory = RingsHomCategory
    EndCategory = RingsEndCategory
    AutCategory = RingsAutCategory
    Hom = RingsHom
    End = RingsEnd
    Aut = RingsAut
    Endomorphism = RingsEndomorphism
    Automorphism = RingsAutomorphism


class RModuleTypes:
    Category = ModulesCategory
    Object = ModulesObject
    Element = ModulesElement
    Morphism = ModulesMorphism
    HomCategory = ModulesHomCategory
    EndCategory = ModulesEndCategory
    AutCategory = ModulesAutCategory
    Hom = ModulesHom
    End = ModulesEnd
    Aut = ModulesAut
    Endomorphism = ModulesEndomorphism
    Automorphism = ModulesAutomorphism


class FormedModuleTypes:
    Category = FormedModulesCategory
    Object = FormedModulesObject
    Element = FormedModulesElement
    Morphism = FormedModulesMorphism
    HomCategory = FormedModulesHomCategory
    EndCategory = FormedModulesEndCategory
    AutCategory = FormedModulesAutCategory
    Hom = FormedModulesHom
    End = FormedModulesEnd
    Aut = FormedModulesAut
    Endomorphism = FormedModulesEndomorphism
    Automorphism = FormedModulesAutomorphism


class BilinearModuleTypes:
    Category = BilinearModulesCategory
    Object = BilinearModulesObject
    Element = BilinearModulesElement
    Morphism = BilinearModulesMorphism
    HomCategory = BilinearModulesHomCategory
    EndCategory = BilinearModulesEndCategory
    AutCategory = BilinearModulesAutCategory
    Hom = BilinearModulesHom
    End = BilinearModulesEnd
    Aut = BilinearModulesAut
    Endomorphism = BilinearModulesEndomorphism
    Automorphism = BilinearModulesAutomorphism


class QuadraticModuleTypes:
    Category = QuadraticModulesCategory
    Object = QuadraticModulesObject
    Element = QuadraticModulesElement
    Morphism = QuadraticModulesMorphism
    HomCategory = QuadraticModulesHomCategory
    EndCategory = QuadraticModulesEndCategory
    AutCategory = QuadraticModulesAutCategory
    Hom = QuadraticModulesHom
    End = QuadraticModulesEnd
    Aut = QuadraticModulesAut
    Endomorphism = QuadraticModulesEndomorphism
    Automorphism = QuadraticModulesAutomorphism


class TorsionQuadraticModuleTypes:
    Category = TorsionQuadraticModulesCategory
    Object = TorsionQuadraticModulesObject
    Element = TorsionQuadraticModulesElement
    Morphism = TorsionQuadraticModulesMorphism
    HomCategory = TorsionQuadraticModulesHomCategory
    EndCategory = TorsionQuadraticModulesEndCategory
    AutCategory = TorsionQuadraticModulesAutCategory
    Hom = TorsionQuadraticModulesHom
    End = TorsionQuadraticModulesEnd
    Aut = TorsionQuadraticModulesAut
    Endomorphism = TorsionQuadraticModulesEndomorphism
    Automorphism = TorsionQuadraticModulesAutomorphism


class AlgebraTypes:
    Category = AlgebrasCategory
    Object = AlgebrasObject
    Element = AlgebrasElement
    Morphism = AlgebrasMorphism
    HomCategory = AlgebrasHomCategory
    EndCategory = AlgebrasEndCategory
    AutCategory = AlgebrasAutCategory
    Hom = AlgebrasHom
    End = AlgebrasEnd
    Aut = AlgebrasAut
    Endomorphism = AlgebrasEndomorphism
    Automorphism = AlgebrasAutomorphism


class MagmaticAlgebraTypes:
    Category = MagmaticAlgebrasCategory
    Object = MagmaticAlgebrasObject
    Element = MagmaticAlgebrasElement
    Morphism = MagmaticAlgebrasMorphism


class AssociativeAlgebraTypes:
    Category = AssociativeAlgebrasCategory
    Object = AssociativeAlgebrasObject
    Element = AssociativeAlgebrasElement
    Morphism = AssociativeAlgebrasMorphism


class PosetTypes:
    Category = PosetsCategory
    Object = PosetsObject
    Element = PosetsElement
    Morphism = PosetsMorphism
    HomCategory = PosetsHomCategory
    EndCategory = PosetsEndCategory
    AutCategory = PosetsAutCategory
    Hom = PosetsHom
    End = PosetsEnd
    Aut = PosetsAut
    Endomorphism = PosetsEndomorphism
    Automorphism = PosetsAutomorphism


class TopologicalSpaceTypes:
    Category = TopologicalSpacesCategory
    Object = TopologicalSpacesObject
    Element = TopologicalSpacesElement
    Morphism = TopologicalSpacesMorphism
    HomCategory = TopologicalSpacesHomCategory
    EndCategory = TopologicalSpacesEndCategory
    AutCategory = TopologicalSpacesAutCategory
    Hom = TopologicalSpacesHom
    End = TopologicalSpacesEnd
    Aut = TopologicalSpacesAut
    Endomorphism = TopologicalSpacesEndomorphism
    Automorphism = TopologicalSpacesAutomorphism


class MetricSpaceTypes:
    Category = MetricSpacesCategory
    Object = MetricSpacesObject
    Element = MetricSpacesElement
    Morphism = MetricSpacesMorphism
    HomCategory = MetricSpacesHomCategory
    EndCategory = MetricSpacesEndCategory
    AutCategory = MetricSpacesAutCategory
    Hom = MetricSpacesHom
    End = MetricSpacesEnd
    Aut = MetricSpacesAut
    Endomorphism = MetricSpacesEndomorphism
    Automorphism = MetricSpacesAutomorphism


class TensorAlgebraComponentTypes:
    Category = TensorAlgebraComponentsCategory
    Object = TensorAlgebraComponentsObject
    Element = TensorAlgebraComponentsElement
    Morphism = TensorAlgebraComponentsMorphism
    HomCategory = TensorAlgebraComponentsHomCategory
    EndCategory = TensorAlgebraComponentsEndCategory
    AutCategory = TensorAlgebraComponentsAutCategory
    Hom = TensorAlgebraComponentsHom
    End = TensorAlgebraComponentsEnd
    Aut = TensorAlgebraComponentsAut
    Endomorphism = TensorAlgebraComponentsEndomorphism
    Automorphism = TensorAlgebraComponentsAutomorphism


class LatticeTypes:
    Category = LatticesCategory
    Object = LatticesObject
    Element = LatticesElement
    Morphism = LatticesMorphism
    HomCategory = LatticesHomCategory
    EndCategory = LatticesEndCategory
    AutCategory = LatticesAutCategory
    Hom = LatticesHom
    End = LatticesEnd
    Aut = LatticesAut
    Endomorphism = LatticesEndomorphism
    Automorphism = LatticesAutomorphism


class DiscriminantGroupTypes:
    Category = LatticeDiscriminantGroupsCategory
    Object = LatticeDiscriminantGroupsObject
    Element = LatticeDiscriminantGroupsElement
    Morphism = LatticeDiscriminantGroupsMorphism
    HomCategory = LatticeDiscriminantGroupsHomCategory
    EndCategory = LatticeDiscriminantGroupsEndCategory
    AutCategory = LatticeDiscriminantGroupsAutCategory
    Hom = LatticeDiscriminantGroupsHom
    End = LatticeDiscriminantGroupsEnd
    Aut = LatticeDiscriminantGroupsAut
    Endomorphism = LatticeDiscriminantGroupsEndomorphism
    Automorphism = LatticeDiscriminantGroupsAutomorphism
