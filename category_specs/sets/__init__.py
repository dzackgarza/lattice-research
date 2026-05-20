r"""Set category surface for the category spec redesign.

This module defines ``Sets()`` as a staged, non-destructive replacement for
Sage's ``Sets()``. It is the public API document for the set subtree: category
navigation, method surfaces, constructions, and constructor entry points live here.

Naming convention:
    Sets()      -- project category
    SageSets()  -- sage.categories.sets_cat.Sets()

Subcategory hierarchy::

    Sets()
    |-- Finite()
    |-- Infinite()
    |-- Countable()
    |   |-- Finite()
    |   `-- Infinite()
    |-- Uncountable()
    |-- Facade()
    |-- Topological()
    |   `-- Metric()
    |-- TotallyOrdered()
    |-- Graded()
    |-- Partitioned()
    |-- GSets(G)
    |-- CartesianProducts()
    |-- Subquotients()
    |-- Subobjects() / Subsets()
    |-- Quotients()
    |-- IsomorphicObjects()
    |-- WithRealizations()
    |-- Realizations()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()

One-object constructor refinements::

    FiniteEnumeratedSetObjects
    IntegerRangeSets
    NonNegativeIntegersSets
    PositiveIntegersSets
    PrimesSets
    RealSets
    RecursivelyEnumeratedSets
    DisjointUnionEnumeratedSets
    CartesianProductSets
    ImageSets
    TotallyOrderedFiniteSets
    FiniteSetMapsSets
    FamilySets
    EnumeratedSetsFromIterator

Constructor entry points live under ``Sets().Constructors()`` and call Sage's
canonical constructors before refining the result into this hierarchy. Named
finite-set entry points such as ``SingletonSet`` route through those canonical
finite-enumerated set objects.
"""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Iterable, Iterator, Sequence
from types import MethodType
from typing import (
    TYPE_CHECKING,
    Any,
    Protocol,
    TypeAlias,
    cast,
    final,
    overload,
    override,
)

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.lazy_import import LazyImport
from sage.rings.infinity import infinity, minus_infinity
from sage.structure.richcmp import op_EQ, op_GE, op_GT, op_LE, op_LT, op_NE

from ..cat import Category, Category_singleton
from ..utils import refine_category, with_axiom
from .homsets import (
    SetAutCategory,
    SetEndCategory,
    SetHomCategory,
    _SetAutomorphisms,
    _SetEndomorphisms,
    _SetHomCategoryObjectMethods,
    _SetMorphisms,
)

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
    from ..types import (
        Algebra,
        Cardinality,
        CountableSet,
        FiniteSet,
        Group,
        InfinityElement,
        Integer,
        IntegerPartition,
        RealInterval,
        RealNumber,
        RealOpenSet,
        RealSubset,
        Ring,
        RModule,
        Set,
        SetElement,
        SetFamily,
        SetMorphism,
        SetPartition,
        SetPartitionSet,
        Subset,
        SympySet,
    )

    SetPartitionType: TypeAlias = SetPartition

    class _SubsetLatticeSource(Protocol):
        def lattice(self) -> Set: ...

if TYPE_CHECKING:
    def cached_method[MethodT: Callable[..., object]](method: MethodT) -> MethodT: ...
else:
    from sage.misc.cachefunc import cached_method


# ---------------------------------------------------------------------------
# Method surfaces for the root category
# ---------------------------------------------------------------------------


class _SetObjectMethods:
    r"""Methods on objects of the root category ``Sets()``."""

    @abstractmethod
    def __contains__(self, x: Any) -> bool:
        r"""Return ``True`` if ``x`` is an element of ``self``."""
        ...

    @final
    def _element_constructor_(self, x: SetElement) -> SetElement:
        if hasattr(self, "element_class"):
            return cast("SetElement", self.element_class(self, x))
        raise NotImplementedError(
            "generic set element construction requires an element class"
        )

    @abstractmethod
    def __call__(self, x: SetElement) -> SetElement:
        r"""Construct the corresponding element of this set."""
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[SetElement]: ...

    @abstractmethod
    def has_coerce_map_from(self, source: Set) -> bool: ...

    @final
    def is_parent_of(self, element: Any) -> bool:
        r"""Return whether this set is the parent of ``element``."""
        from sage.structure.element import parent

        return cast(bool, parent(element) == self)

    @abstractmethod
    def an_element(self) -> SetElement:
        r"""Return a distinguished element of this set."""
        ...

    @final
    def some_elements(self) -> list[SetElement]:
        r"""Return sample elements of this set."""
        from sage.categories.sets_cat import Sets as SageSets

        return cast("list[SetElement]", SageSets.ParentMethods.some_elements(self))

    @abstractmethod
    def cardinality(self) -> Cardinality:
        r"""Return the cardinality of this set."""
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        r"""Return whether this set has no elements."""
        ...

    @abstractmethod
    def is_finite(self) -> bool:
        r"""Return whether this set has finite cardinality."""
        ...

    @final
    def construction(self) -> None:
        r"""Return Sage construction data for this set, when it has one."""
        return None

    @final
    def cartesian_product(
        self,
        other: Set,
        *,
        category: Category | None = None,
        extra_category: Category | None = None,
        flatten: bool = False,
    ) -> Set:
        r"""Return the binary Cartesian product of this set with ``other``."""
        return (
            Sets()
            .Constructors()
            .CartesianProductFromFactors(
                (self, other),
                category=category,
                extra_category=extra_category,
                flatten=flatten,
            )
        )

    @final
    def union(self, other: Set) -> Set:
        r"""Return the set-theoretic union of ``self`` and ``other``."""
        from sage.sets.set import Set as SageSet

        return cast("Set", SageSet(self).union(SageSet(other)))

    @final
    def __or__(self, other: Set) -> Set:
        return self.union(other)

    @final
    def __add__(self, other: Set) -> Set:
        return self.union(other)

    @final
    def is_subset(self, other: Set) -> bool:
        r"""Return whether ``self`` is a subset of ``other``."""
        if self is other:
            return True
        if self.is_finite():
            return all(element in other for element in self)
        raise NotImplementedError(
            "generic subset testing requires a finite enumerable set"
        )

    @final
    def is_proper_subset(self, other: Set) -> bool:
        r"""Return whether ``self`` is a proper subset of ``other``."""
        return self.is_subset(other) and not other.is_subset(self)

    @final
    def is_superset(self, other: Set) -> bool:
        r"""Return whether ``self`` contains ``other`` as a subset."""
        return other.is_subset(self)

    @final
    def is_proper_superset(self, other: Set) -> bool:
        r"""Return whether ``self`` properly contains ``other``."""
        return other.is_proper_subset(self)

    @final
    def __richcmp__(self, other: Set, op: Integer) -> bool:
        r"""Compare sets using equality and subset/proper-subset relations."""
        if op == op_LE:
            return self.is_subset(other)
        if op == op_LT:
            return self.is_proper_subset(other)
        if op == op_GE:
            return self.is_superset(other)
        if op == op_GT:
            return self.is_proper_superset(other)
        if op == op_EQ:
            return self.is_subset(other) and other.is_subset(self)
        if op == op_NE:
            return not (self.is_subset(other) and other.is_subset(self))
        raise ValueError(f"unknown rich comparison operation: {op}")

    @final
    def __le__(self, other: Set) -> bool:
        return self.is_subset(other)

    @final
    def __lt__(self, other: Set) -> bool:
        return self.is_proper_subset(other)

    @final
    def __ge__(self, other: Set) -> bool:
        return self.is_superset(other)

    @final
    def __gt__(self, other: Set) -> bool:
        return self.is_proper_superset(other)

    @final
    def subsets(self, size: Integer | None = None) -> Set:
        r"""Return the set of subsets, optionally with fixed cardinality ``size``."""
        from sage.combinat.subset import Subsets

        if size is None:
            return cast("Set", Subsets(self))
        return cast("Set", Subsets(self, size))

    @final
    def subsets_lattice(self) -> Set:
        r"""Return the lattice of subsets ordered by inclusion."""
        return cast("_SubsetLatticeSource", self.subsets()).lattice()

    @final
    def free_module(self, base_ring: Ring) -> RModule:
        r"""Return the free ``base_ring``-module with basis indexed by this set."""
        from ..modules import Modules

        return (
            Modules(base_ring).Constructors().CombinatorialFreeModule(basis_keys=self)
        )

    @final
    def free_algebra(self, base_ring: Ring) -> Algebra:
        r"""Return the free ``base_ring``-algebra on this set of generators."""
        from ..algebras import Algebras

        return Algebras(base_ring).Constructors().free_algebra_from_set(self)

    @final
    def _sympy_(self) -> SympySet:
        from sage.interfaces.sympy import sympy_init
        from sage.interfaces.sympy_wrapper import SageSet

        sympy_init()
        return SageSet(self)


class _SetElementMethods:
    r"""Methods on elements of objects in ``Sets()``."""

    @abstractmethod
    def __eq__(self, other: object) -> bool: ...

    @abstractmethod
    def __hash__(self) -> Integer: ...

    @abstractmethod
    def cartesian_product(self, elements: Sequence[SetElement]) -> SetElement:
        r"""Return the Cartesian product element with these coordinates."""
        ...


# ---------------------------------------------------------------------------
# Sets -- the root category
# ---------------------------------------------------------------------------


class Sets(Category_singleton):
    r"""Replacement set category, staged below Sage's existing ``Sets()``.

    Canonical chain: ``Sets()``.

    Objects in ``Sets()`` are any Sage parents that lie in ``SageSets()``.
    The module docstring records the full public category hierarchy and constructor
    refinement map.
    """

    @override
    @final
    def __contains__(self, candidate: Any) -> bool:
        r"""Return whether ``candidate`` is a Sage/project set parent."""
        from sage.structure.parent import Parent

        return isinstance(candidate, Parent) and candidate.category().is_subcategory(
            SageSets()
        )

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageSets(),)

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage's set category refined by this spec."""
        return [SageSets()]

    @override
    @final
    def additional_structure(self) -> Category | None:
        r"""Return Sage's additional-structure marker for plain sets."""
        return None

    # ------------------------------------------------------------------
    # SubcategoryMethods -- available on every subcategory of Sets()
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        @final
        def Finite(self) -> Category:
            r"""Return the finite-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Finite"))

        @cached_method
        @final
        def Infinite(self) -> Category:
            r"""Return the infinite-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Infinite"))

        @cached_method
        @final
        def Countable(self) -> Category:
            r"""Return the countable-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Countable"))

        @cached_method
        @final
        def Uncountable(self) -> Category:
            r"""Return the uncountable-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Uncountable"))

        @cached_method
        @final
        def Facade(self) -> Category:
            r"""Return the facade-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Facade"))

        @cached_method
        @final
        def Topological(self) -> Category:
            r"""Return the topological-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Topological"))

        @cached_method
        @final
        def Metric(self) -> Category:
            r"""Return the metric-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Metric"))

        @cached_method
        @final
        def TotallyOrdered(self) -> Category:
            r"""Return the totally ordered set subcategory of this set category."""
            return cast(Category, with_axiom(self, "TotallyOrdered"))

        @cached_method
        @final
        def Graded(self) -> Category:
            r"""Return the graded-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Graded"))

        @cached_method
        @final
        def Partitioned(self) -> Category:
            r"""Return the partitioned-set subcategory of this set category."""
            return cast(Category, with_axiom(self, "Partitioned"))

        @cached_method
        @final
        def GSets(self, acting_group: Group) -> Category:
            r"""Return the category of sets with an action by ``acting_group``."""
            from .subcategories.group_actions import _GSets

            return _GSets(acting_group, self)

        @cached_method
        @final
        def IsomorphicObjects(self) -> Category:
            r"""Return the category of set objects presented by isomorphic models."""
            from .subcategories.constructions.isomorphic_objects import (
                _IsomorphicObjects,
            )

            return cast(Category, _IsomorphicObjects.category_of(self))

        @cached_method
        @final
        def WithRealizations(self) -> Category:
            r"""Return the category of sets equipped with named realizations."""
            from .subcategories.constructions.with_realizations import (
                SetsWithRealizations,
            )

            return cast(Category, SetsWithRealizations.category_of(self))

        @cached_method
        @final
        def Realizations(self) -> Category:
            r"""Return the category of realizations of objects in this set category."""
            from .subcategories.constructions.realizations import _Realizations

            return cast(Category, _Realizations.category_of(self))

    # ------------------------------------------------------------------
    # Constructors -- named Sage set entry points
    # ------------------------------------------------------------------

    class _Constructors:
        r"""Named Sage set constructor entry points.

        Every method calls the canonical Sage constructor, then refines
        the resulting parent into ``Sets()`` and the most specific
        one-object subcategory.

        Usage::

            Sets().Constructors().Primes()
            Sets().Constructors().FiniteEnumeratedSet([1, 2, 3])
            Sets().Constructors().IntegerRange(2, 100, 5)
        """

        @final
        def __init__(self, category: Sets) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return "Sets constructors"

        @final
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for set constructors."""
            from category_specs.spec_core import constructor_registry_for_category

            return constructor_registry_for_category(
                self._category, owner_category="Sets()", id_prefix="sets"
            )

        @staticmethod
        def _set_partitions_categories() -> list[Category]:
            r"""Return project categories for fixed-base set-partition parents."""
            from .subcategories.partitioned import (
                PartitionedSetsCategory,
                PartitionsCategory,
            )

            return [Sets(), PartitionsCategory(), PartitionedSetsCategory()]

        @final
        def _set_partitions_base(
            self,
            base_set: Set | Iterable[SetElement] | Integer,
        ) -> tuple[Set | tuple[SetElement, ...] | Integer, list[Category]]:
            r"""Normalize one admitted fixed-base set-partition input shape."""
            from sage.rings.integer import Integer as SageInteger
            from sage.structure.category_object import CategoryObject

            if isinstance(base_set, SageInteger):
                return base_set, self._set_partitions_categories()
            if isinstance(base_set, CategoryObject) and base_set in Sets():
                return base_set, self._set_partitions_categories()
            if isinstance(base_set, Iterable):
                return tuple(base_set), self._set_partitions_categories()
            raise TypeError(
                "set-partition constructors require a set object, "
                "a finite iterable of elements, or a Sage Integer cardinality"
            )

        @final
        def from_iterable(self, elements: Iterable[SetElement]) -> FiniteSet:
            r"""Return the finite enumerated set read from ``elements``."""
            return self.FiniteEnumeratedSet(elements)

        @final
        def FiniteEnumeratedSet(self, elements: Iterable[SetElement]) -> FiniteSet:
            r"""Return ``FiniteEnumeratedSet(elements)``, refined."""
            from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as SageFES

            from .subcategories.finite_enumerated_set import _FiniteEnumeratedSetObjects

            return cast(
                "FiniteSet",
                refine_category(
                    SageFES(elements), [Sets(), _FiniteEnumeratedSetObjects()]
                ),
            )

        @final
        def SingletonSet(self, element: SetElement) -> FiniteSet:
            r"""Return the singleton finite set ``{element}``."""
            return self.FiniteEnumeratedSet((element,))

        @final
        def IntegerRange(
            self,
            begin: Integer | InfinityElement,
            end: Integer | InfinityElement | None = None,
            step: Integer = 1,
            middle_point: Integer | None = None,
        ) -> CountableSet:
            r"""Return the integer arithmetic progression determined by the bounds."""
            from sage.sets.integer_range import IntegerRange as SageIR

            from .subcategories.integer_range import _IntegerRangeSets

            return cast(
                "CountableSet",
                refine_category(
                    SageIR(begin, end, step, middle_point),
                    [Sets(), _IntegerRangeSets()],
                ),
            )

        @final
        def NonNegativeIntegers(self) -> CountableSet:
            r"""Return ``NonNegativeIntegers()``, refined into its subcategory."""
            from sage.sets.non_negative_integers import NonNegativeIntegers as SageNN

            from .subcategories.non_negative_integers import _NonNegativeIntegersSets

            return cast(
                "CountableSet",
                refine_category(SageNN(), [Sets(), _NonNegativeIntegersSets()]),
            )

        @final
        def PositiveIntegers(self) -> CountableSet:
            r"""Return ``PositiveIntegers()``, refined into its subcategory."""
            from sage.sets.positive_integers import PositiveIntegers as SagePP

            from .subcategories.positive_integers import _PositiveIntegersSets

            return cast(
                "CountableSet",
                refine_category(SagePP(), [Sets(), _PositiveIntegersSets()]),
            )

        @final
        def Primes(self, proof: bool = True) -> CountableSet:
            r"""Return the full Sage set of prime integers."""
            from sage.sets.primes import Primes as SagePrimes

            from .subcategories.primes import _PrimesSets

            return cast(
                "CountableSet",
                refine_category(SagePrimes(proof), [Sets(), _PrimesSets()]),
            )

        @final
        def _real_subset_categories(self, real_set: RealSubset) -> list[Category]:
            r"""Return the project categories satisfied by a Sage real subset."""
            from sage.categories.topological_spaces import (
                TopologicalSpaces as SageTopologicalSpaces,
            )

            from ..topological_spaces import TopologicalSpaces
            from .subcategories.real_set import _RealSets

            topological_spaces = TopologicalSpaces()
            categories = [
                Sets(),
                Sets().Subobjects(),
                Sets().Topological(),
                _RealSets(),
                topological_spaces.Subobjects(),
            ]
            if real_set.is_connected():
                connected_spaces = topological_spaces.Connected()
                categories.extend([connected_spaces, connected_spaces.Subobjects()])
            is_compact = real_set.category().is_subcategory(
                SageTopologicalSpaces().Compact()
            ) or (
                real_set.is_empty()
                or (
                    real_set.is_closed()
                    and real_set.inf() is not minus_infinity
                    and real_set.sup() is not infinity
                )
            )
            if is_compact:
                compact_spaces = topological_spaces.Compact()
                categories.extend([compact_spaces, compact_spaces.Subobjects()])
                if real_set.is_connected():
                    categories.append(compact_spaces.Connected().Subobjects())
            return categories

        @final
        def _refine_real_subset(self, real_set: RealSubset) -> RealSubset:
            r"""Refine a Sage real subset into the local set/topological hierarchy."""
            return self._install_real_subset_ambient_adapter(
                refine_category(real_set, self._real_subset_categories(real_set))
            )

        @final
        def _install_real_subset_ambient_adapter(
            self, real_set: RealSubset
        ) -> RealSubset:
            r"""Install the ambient-relative route on a real subset."""
            sage_is_open = real_set.is_open
            sage_is_closed = real_set.is_closed
            sage_ambient = real_set.ambient
            sage_closure = real_set.closure
            sage_interior = real_set.interior
            sage_boundary = real_set.boundary

            def is_real_line(X: RealSubset) -> bool:
                if X.n_components() != 1:
                    return False
                interval = X.get_interval(0)
                return (
                    interval.lower() is minus_infinity and interval.upper() is infinity
                )

            def ambient(U: RealSubset) -> RealSubset:
                return (
                    U if is_real_line(U) else self._refine_real_subset(sage_ambient())
                )

            def is_open(X: RealSubset, U: RealSubset | None = None) -> bool:
                if U is None:
                    return sage_is_open()
                return U.is_subset(X) and U.is_open()

            def is_closed(X: RealSubset, U: RealSubset | None = None) -> bool:
                if U is None:
                    return sage_is_closed()
                return U.is_subset(X) and U.is_closed()

            def closure(X: RealSubset, U: RealSubset | None = None) -> RealSubset:
                if U is None:
                    return self._refine_real_subset(sage_closure())
                if not U.is_subset(X):
                    raise ValueError("closure subset must lie in its ambient real set")
                return self._refine_real_subset(U.closure())

            def interior(X: RealSubset, U: RealSubset | None = None) -> RealSubset:
                if U is None:
                    return self._refine_real_subset(sage_interior())
                if not U.is_subset(X):
                    raise ValueError("interior subset must lie in its ambient real set")
                return self._refine_real_subset(U.interior())

            def boundary(X: RealSubset, U: RealSubset | None = None) -> RealSubset:
                if U is None:
                    return self._refine_real_subset(sage_boundary())
                if not U.is_subset(X):
                    raise ValueError("boundary subset must lie in its ambient real set")
                return self._refine_real_subset(U.boundary())

            setattr(real_set, "ambient", MethodType(ambient, real_set))
            setattr(real_set, "is_open", MethodType(is_open, real_set))
            setattr(real_set, "is_closed", MethodType(is_closed, real_set))
            setattr(real_set, "closure", MethodType(closure, real_set))
            setattr(real_set, "interior", MethodType(interior, real_set))
            setattr(real_set, "boundary", MethodType(boundary, real_set))
            return real_set

        @final
        def RR(self) -> Set:
            r"""Return Sage ``RR`` refined as a topological set object."""
            from sage.rings.real_mpfr import RealField

            return cast(
                "Set",
                refine_category(RealField(), [Sets(), Sets().Topological()]),
            )

        @final
        def RealSetFromIntervals(self, intervals: Sequence[RealInterval]) -> RealSubset:
            r"""Return a real subset from a finite sequence of real intervals."""
            from sage.sets.real_set import RealSet as SageRealSet

            return self._refine_real_subset(SageRealSet(*tuple(intervals)))

        @final
        def RealSetInterval(
            self,
            lower: RealNumber | InfinityElement,
            upper: RealNumber | InfinityElement,
            *,
            lower_closed: bool,
            upper_closed: bool,
        ) -> RealSubset:
            r"""Return ``RealSet.interval(lower, upper, ...)``."""
            from sage.sets.real_set import RealSet as SageRealSet

            S = SageRealSet.interval(
                lower,
                upper,
                lower_closed=lower_closed,
                upper_closed=upper_closed,
            )
            return self._refine_real_subset(S)

        @final
        def OpenRealInterval(self, lower: RealNumber, upper: RealNumber) -> RealOpenSet:
            r"""Return ``RealSet.open(lower, upper)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=False,
                upper_closed=False,
            )

        @final
        def ClosedRealInterval(
            self, lower: RealNumber, upper: RealNumber
        ) -> RealSubset:
            r"""Return ``RealSet.closed(lower, upper)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=True,
                upper_closed=True,
            )

        @final
        def RealPoint(self, point: RealNumber) -> RealSubset:
            r"""Return ``RealSet.point(point)``, refined into ``RealSets``."""
            return self.RealSetInterval(
                point,
                point,
                lower_closed=True,
                upper_closed=True,
            )

        @final
        def OpenClosedRealInterval(
            self,
            lower: RealNumber,
            upper: RealNumber,
        ) -> RealSubset:
            r"""Return ``RealSet.open_closed(lower, upper)``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=False,
                upper_closed=True,
            )

        @final
        def ClosedOpenRealInterval(
            self,
            lower: RealNumber,
            upper: RealNumber,
        ) -> RealSubset:
            r"""Return ``RealSet.closed_open(lower, upper)``."""
            return self.RealSetInterval(
                lower,
                upper,
                lower_closed=True,
                upper_closed=False,
            )

        @final
        def UnboundedBelowClosedRealInterval(self, bound: RealNumber) -> RealSubset:
            r"""Return ``RealSet.unbounded_below_closed(bound)``."""
            return self.RealSetInterval(
                -infinity,
                bound,
                lower_closed=False,
                upper_closed=True,
            )

        @final
        def UnboundedBelowOpenRealInterval(self, bound: RealNumber) -> RealOpenSet:
            r"""Return ``RealSet.unbounded_below_open(bound)``."""
            return self.RealSetInterval(
                -infinity,
                bound,
                lower_closed=False,
                upper_closed=False,
            )

        @final
        def UnboundedAboveClosedRealInterval(self, bound: RealNumber) -> RealSubset:
            r"""Return ``RealSet.unbounded_above_closed(bound)``."""
            return self.RealSetInterval(
                bound,
                infinity,
                lower_closed=True,
                upper_closed=False,
            )

        @final
        def UnboundedAboveOpenRealInterval(self, bound: RealNumber) -> RealOpenSet:
            r"""Return ``RealSet.unbounded_above_open(bound)``."""
            return self.RealSetInterval(
                bound,
                infinity,
                lower_closed=False,
                upper_closed=False,
            )

        @final
        def RealLine(self) -> RealSubset:
            r"""Return ``RealSet.real_line()``, refined into ``RealSets``."""
            return self.RealSetInterval(
                -infinity,
                infinity,
                lower_closed=False,
                upper_closed=False,
            )

        @final
        def RecursivelyEnumeratedSet(
            self,
            seeds: Iterable[SetElement],
            successors: Callable[[SetElement], Iterable[SetElement]],
            *,
            enumeration: str = "depth",
            max_depth: Integer | InfinityElement = infinity,
            post_process: Callable[[SetElement], SetElement] | None = None,
            facade: bool | None = None,
            category: Category | None = None,
        ) -> CountableSet:
            r"""Return a ``RecursivelyEnumeratedSet``, refined into its subcategory."""
            from sage.sets.recursively_enumerated_set import (
                RecursivelyEnumeratedSet as SageRES,
            )

            from .subcategories.recursively_enumerated import _RecursivelyEnumeratedSets

            S = SageRES(
                seeds,
                successors,
                enumeration=enumeration,
                max_depth=max_depth,
                post_process=post_process,
                facade=facade,
                category=category,
            )
            return cast(
                "CountableSet",
                refine_category(S, [Sets(), _RecursivelyEnumeratedSets()]),
            )

        @final
        def DisjointUnionEnumeratedSets(
            self,
            family: SetFamily | Iterable[Set],
            *,
            facade: bool = True,
            keepkey: bool = False,
            category: Category | None = None,
        ) -> CountableSet:
            r"""Return a refined ``DisjointUnionEnumeratedSets``."""
            from sage.sets.disjoint_union_enumerated_sets import (
                DisjointUnionEnumeratedSets as SageDUES,
            )

            from .subcategories.disjoint_union import _DisjointUnionEnumeratedSets

            S = SageDUES(family, facade=facade, keepkey=keepkey, category=category)
            return cast(
                "CountableSet",
                refine_category(S, [Sets(), _DisjointUnionEnumeratedSets()]),
            )

        @final
        def CartesianProduct(
            self,
            left: Set,
            right: Set,
            *,
            category: Category | None = None,
            flatten: bool = False,
        ) -> Set:
            r"""Return the binary Cartesian product of ``left`` and ``right``."""
            return self.CartesianProductFromFactors(
                (left, right), category=category, flatten=flatten
            )

        @final
        def CartesianProductFromFactors(
            self,
            factors: Sequence[Set],
            *,
            category: Category | None = None,
            extra_category: Category | None = None,
            flatten: bool = False,
        ) -> Set:
            r"""Return the Cartesian product of finite ordered set parents."""
            from sage.categories.cartesian_product import cartesian_product
            from sage.sets.cartesian_product import CartesianProduct as SageCP

            from .subcategories.cartesian_product import _CartesianProductSets

            parents = tuple(factors)
            product_category = category or cartesian_product.category_from_parents(
                parents
            )
            if extra_category is not None:
                if isinstance(product_category, (list, tuple)):
                    product_category = tuple(product_category) + (extra_category,)
                else:
                    product_category = product_category & extra_category
            S = SageCP(parents, category=product_category, flatten=flatten)
            return cast("Set", refine_category(S, [Sets(), _CartesianProductSets()]))

        @final
        def ImageSubobject(
            self,
            f: SetMorphism,
            domain_subset: Subset,
        ) -> Subset:
            r"""Return ``ImageSubobject(f, domain_subset)``."""
            from .subcategories.image import ImageSubobject as ProjectImageSubobject
            from .subcategories.image import _ImageSets

            return cast(
                "Subset",
                refine_category(
                    ProjectImageSubobject(f, domain_subset),
                    [Sets(), _ImageSets()],
                ),
            )

        @final
        def TotallyOrderedFiniteSet(
            self, elements: Iterable[SetElement], *, facade: bool = True
        ) -> FiniteSet:
            r"""Return a ``TotallyOrderedFiniteSet``, refined into its subcategory."""
            from sage.sets.totally_ordered_finite_set import (
                TotallyOrderedFiniteSet as SageTOFS,
            )

            from .subcategories.totally_ordered_finite import _TotallyOrderedFiniteSets

            S = SageTOFS(elements, facade=facade)
            return cast(
                "FiniteSet",
                refine_category(S, [Sets(), _TotallyOrderedFiniteSets()]),
            )

        @final
        def FiniteSetMaps(
            self,
            domain: FiniteSet | Integer,
            codomain: FiniteSet | Integer | None = None,
            *,
            action: str = "left",
            category: Category | None = None,
        ) -> FiniteSet:
            r"""Return the finite set of all functions ``domain -> codomain``.

            With only ``domain`` specified, Sage constructs the endomap set
            ``Map(domain, domain)``, whose elements form a finite monoid under
            composition.
            """
            from sage.sets.finite_set_maps import FiniteSetMaps as SageFSM

            from .subcategories.finite_set_maps import _FiniteSetMapsSets

            if codomain is None:
                S = SageFSM(domain, action=action, category=category)
            else:
                S = SageFSM(domain, codomain, action=action, category=category)
            return cast("FiniteSet", refine_category(S, [Sets(), _FiniteSetMapsSets()]))

        @final
        def Family(
            self,
            indices: Iterable[SetElement] | Set,
            function: Callable[[SetElement], SetElement] | None = None,
            *,
            hidden_keys: Sequence[SetElement] = (),
            hidden_function: Callable[[SetElement], SetElement] | None = None,
            lazy: bool = False,
            name: str | None = None,
        ) -> SetFamily:
            r"""Return a ``Family``, refined into its subcategory."""
            from sage.sets.family import Family as SageFamily

            from .subcategories.family import _FamilySets

            S = SageFamily(
                indices,
                function,
                hidden_keys=list(hidden_keys),
                hidden_function=hidden_function,
                lazy=lazy,
                name=name,
            )
            return cast("SetFamily", refine_category(S, [Sets(), _FamilySets()]))

        @final
        def EnumeratedSetFromIterator(
            self,
            iterator_factory: Callable[[], Iterable[SetElement]],
            *,
            name: str | None = None,
            category: Category | None = None,
            cache: bool = False,
        ) -> CountableSet:
            r"""Return a callable-backed set from a nullary iterator factory."""
            from sage.sets.set_from_iterator import (
                EnumeratedSetFromIterator as SageESFI,
            )

            from .subcategories.enumerated_from_iterator import (
                _EnumeratedSetsFromIterator,
            )

            return cast(
                "CountableSet",
                refine_category(
                    SageESFI(
                        iterator_factory,
                        name=name,
                        category=category,
                        cache=cache,
                    ),
                    [Sets(), _EnumeratedSetsFromIterator()],
                ),
            )

        @final
        def AllSetPartitions(self) -> CountableSet:
            r"""Return Sage's countable set of all finite set partitions."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "CountableSet",
                refine_category(SageSetPartitions(), [Sets(), Sets().Countable()]),
            )

        @overload
        def SetPartitions(self, base_set: Set) -> SetPartitionSet: ...

        @overload
        def SetPartitions(self, base_set: Iterable[SetElement]) -> SetPartitionSet: ...

        @overload
        def SetPartitions(self, base_set: Integer) -> SetPartitionSet: ...

        @final
        def SetPartitions(
            self, base_set: Set | Iterable[SetElement] | Integer
        ) -> SetPartitionSet:
            r"""Return the set of all partitions of ``base_set``."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            normalized_base, categories = self._set_partitions_base(base_set)
            return cast(
                "SetPartitionSet",
                refine_category(SageSetPartitions(normalized_base), categories),
            )

        @overload
        def SetPartitionsWithBlockCount(
            self,
            base_set: Set,
            block_count: Integer,
        ) -> SetPartitionSet: ...

        @overload
        def SetPartitionsWithBlockCount(
            self,
            base_set: Iterable[SetElement],
            block_count: Integer,
        ) -> SetPartitionSet: ...

        @overload
        def SetPartitionsWithBlockCount(
            self,
            base_set: Integer,
            block_count: Integer,
        ) -> SetPartitionSet: ...

        @final
        def SetPartitionsWithBlockCount(
            self,
            base_set: Set | Iterable[SetElement] | Integer,
            block_count: Integer,
        ) -> SetPartitionSet:
            r"""Return partitions of ``base_set`` into ``block_count`` blocks."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            normalized_base, categories = self._set_partitions_base(base_set)
            return cast(
                "SetPartitionSet",
                refine_category(
                    SageSetPartitions(normalized_base, block_count), categories
                ),
            )

        @overload
        def SetPartitionsWithBlockSizes(
            self,
            base_set: Set,
            block_sizes: IntegerPartition | Sequence[Integer],
        ) -> SetPartitionSet: ...

        @overload
        def SetPartitionsWithBlockSizes(
            self,
            base_set: Iterable[SetElement],
            block_sizes: IntegerPartition | Sequence[Integer],
        ) -> SetPartitionSet: ...

        @overload
        def SetPartitionsWithBlockSizes(
            self,
            base_set: Integer,
            block_sizes: IntegerPartition | Sequence[Integer],
        ) -> SetPartitionSet: ...

        @final
        def SetPartitionsWithBlockSizes(
            self,
            base_set: Set | Iterable[SetElement] | Integer,
            block_sizes: IntegerPartition | Sequence[Integer],
        ) -> SetPartitionSet:
            r"""Return partitions of ``base_set`` with block sizes."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            normalized_base, categories = self._set_partitions_base(base_set)
            return cast(
                "SetPartitionSet",
                refine_category(
                    SageSetPartitions(normalized_base, block_sizes), categories
                ),
            )

        @final
        def SetPartition(
            self,
            blocks: Iterable[Iterable[SetElement]],
            *,
            check: bool = True,
        ) -> SetPartition:
            r"""Return the partition whose blocks are ``blocks``."""
            from sage.combinat.set_partition import SetPartition as SageSetPartition

            return cast("SetPartition", SageSetPartition(blocks, check=check))

        @final
        def SetPartitionFromRestrictedGrowthWordBlocks(
            self, word: Sequence[Integer]
        ) -> SetPartitionType:
            r"""Return the set partition encoded by block-convention ``word``."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_restricted_growth_word_blocks(word),
            )

        @final
        def SetPartitionFromRestrictedGrowthWordIntertwining(
            self, word: Sequence[Integer]
        ) -> SetPartitionType:
            r"""Return the set partition encoded by intertwining ``word``."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_restricted_growth_word_intertwining(word),
            )

        @final
        def SetPartitionFromArcs(
            self,
            arcs: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartitionType:
            r"""Return the coarsest partition of ``{1, ..., n}`` containing ``arcs``."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_arcs(arcs, base_set_cardinality),
            )

        @final
        def SetPartitionFromRookPlacementArcs(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer | None = None,
        ) -> SetPartitionType:
            r"""Return the set partition encoded by a rook placement through arcs."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_rook_placement(
                    rooks, "arcs", base_set_cardinality
                ),
            )

        @final
        def SetPartitionFromRookPlacementGamma(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartitionType:
            r"""Return the set partition encoded by the Wachs-White gamma bijection."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_rook_placement_gamma(
                    rooks, base_set_cardinality
                ),
            )

        @final
        def SetPartitionFromRookPlacementRho(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartitionType:
            r"""Return the set partition encoded by the Wachs-White rho bijection."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_rook_placement_rho(
                    rooks, base_set_cardinality
                ),
            )

        @final
        def SetPartitionFromRookPlacementPsi(
            self,
            rooks: Sequence[tuple[Integer, Integer]],
            base_set_cardinality: Integer,
        ) -> SetPartitionType:
            r"""Return the set partition encoded by Yip's psi bijection."""
            from sage.combinat.set_partition import SetPartitions as SageSetPartitions

            return cast(
                "SetPartitionType",
                SageSetPartitions().from_rook_placement_psi(
                    rooks, base_set_cardinality
                ),
            )

        @final
        def cartesian_product(self, factors: Sequence[Set]) -> Set:
            r"""Return Sage's sequence-style Cartesian product."""
            return self.CartesianProductFromFactors(factors)

    @cached_method
    @final
    def Constructors(self) -> Sets._Constructors:
        r"""Return the named Sage set constructor collector."""
        return self.__class__._Constructors(self)

    HomCategory = SetHomCategory

    # ------------------------------------------------------------------
    # Axiomatic subcategories and construction categories
    # ------------------------------------------------------------------

    Finite = LazyImport("category_specs.sets.subcategories.finite", "_FiniteSets")
    Infinite = LazyImport("category_specs.sets.subcategories.infinite", "_InfiniteSets")
    Countable = LazyImport(
        "category_specs.sets.subcategories.countable", "_CountableSets"
    )
    Uncountable = LazyImport(
        "category_specs.sets.subcategories.uncountable", "_UncountableSets"
    )
    Facade = LazyImport("category_specs.sets.subcategories.facade", "_FacadeSets")
    Topological = LazyImport("category_specs.topological_spaces", "TopologicalSpaces")
    TotallyOrdered = LazyImport(
        "category_specs.sets.subcategories.totally_ordered", "_TotallyOrdered"
    )
    Graded = LazyImport(
        "category_specs.sets.subcategories.graded", "GradedSetsCategory"
    )
    Partitioned = LazyImport(
        "category_specs.sets.subcategories.partitioned", "PartitionedSetsCategory"
    )
    Metric = LazyImport("category_specs.topological_spaces", "MetricSpacesCategory")
    Subquotients = LazyImport(
        "category_specs.sets.subcategories.constructions.subquotients", "_Subquotients"
    )
    Subobjects = LazyImport(
        "category_specs.sets.subcategories.constructions.subobjects", "Subsets"
    )
    ObjectsOver = LazyImport(
        "category_specs.sets.subcategories.constructions.objects_over", "_ObjectsOver"
    )
    ObjectsUnder = LazyImport(
        "category_specs.sets.subcategories.constructions.objects_under", "_ObjectsUnder"
    )
    CartesianProducts = LazyImport(
        "category_specs.sets.subcategories.constructions.cartesian_products",
        "_CartesianProducts",
    )
    Subsets = Subobjects
    Quotients = LazyImport(
        "category_specs.sets.subcategories.constructions.quotients", "_Quotients"
    )
    IsomorphicObjects = LazyImport(
        "category_specs.sets.subcategories.constructions.isomorphic_objects",
        "_IsomorphicObjects",
    )
    WithRealizations = LazyImport(
        "category_specs.sets.subcategories.constructions.with_realizations",
        "SetsWithRealizations",
    )
    Realizations = LazyImport(
        "category_specs.sets.subcategories.constructions.realizations",
        "_Realizations",
    )

    ParentMethods = _SetObjectMethods
    ElementMethods = _SetElementMethods


SetsCategory = Sets
SetsObject = _SetObjectMethods
SetsElement = _SetElementMethods
SetsMorphism = _SetMorphisms
SetsHomCategory = SetHomCategory
SetsEndCategory = SetEndCategory
SetsAutCategory = SetAutCategory
SetsHom = _SetHomCategoryObjectMethods
SetsEnd = SetEndCategory.ParentMethods
SetsAut = SetAutCategory.ParentMethods
SetsEndomorphism = _SetEndomorphisms
SetsAutomorphism = _SetAutomorphisms
