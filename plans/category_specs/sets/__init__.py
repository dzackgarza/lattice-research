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
    |-- GSets(G)
    |-- CartesianProducts()
    |-- Subquotients()
    |-- Subobjects() / Subsets()
    |-- Quotients()
    |-- IsomorphicObjects()
    |-- WithRealizations()
    |-- Realizations()
    `-- Homsets()
        |-- Endset()
        `-- Autset()

One-object constructor refinements::

    SetObjects, SetObjectsEnumerated
    FiniteEnumeratedSetObjects
    IntegerRangeSets
    NonNegativeIntegersSets
    PositiveIntegersSets
    PrimesSets
    RealSets
    RecursivelyEnumeratedSets
    DisjointUnionEnumeratedSets
    CartesianProductSets
    ConditionSets
    ImageSets
    TotallyOrderedFiniteSets
    FiniteSetMapsSets
    FamilySets
    EnumeratedSetsFromIterator

Constructor entry points live under ``Sets().Constructors()`` and call Sage's
canonical constructors before refining the result into this hierarchy.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..utils import refine_category
from .homsets import SetHomsets

if TYPE_CHECKING:
    from ..types import (
        FiniteSet,
        Group,
        RealNumber,
        RealOpenSet,
        RealSubset,
        Set,
        SetAutset,
        SetElement,
        SetEndset,
        SetHomset,
        SetMorphism,
        SympySet,
    )


# ---------------------------------------------------------------------------
# Method surfaces for the root category
# ---------------------------------------------------------------------------


class _SetObjectMethods:
    r"""Methods on objects of the root category ``Sets()``."""

    @abstract_method
    def __contains__(self, x: Any) -> bool:
        r"""Return ``True`` if ``x`` is an element of ``self``."""
        ...

    @abstract_method
    def _element_constructor_(self, x: SetElement) -> SetElement: ...

    @abstract_method
    def _element_constructor_from_element_class(self, *args, **keywords) -> SetElement: ...

    @abstract_method
    def is_parent_of(self, element: SetElement) -> bool: ...

    @abstract_method
    def an_element(self) -> SetElement: ...

    @abstract_method
    def some_elements(self) -> list[SetElement]: ...

    @abstract_method
    def construction(self): ...

    @abstract_method
    def cartesian_product(self, factors: Sequence[Set], **kwargs: Any) -> Set:
        r"""Return the Cartesian product of ``self`` with the parent sets in ``factors``."""
        ...

    @abstract_method
    def union(self, other: Set) -> Set:
        r"""Return the set-theoretic union of ``self`` and ``other``."""
        ...

    def __or__(self, other: Set) -> Set:
        return self.union(other)

    def __add__(self, other: Set) -> Set:
        return self.union(other)

    @abstract_method
    def algebra(self, base_ring, category=None, **kwds):
        r"""Return the algebra of this set over ``base_ring``."""
        ...

    @abstract_method
    def _sympy_(self) -> SympySet: ...

    @abstract_method
    def Hom(self, codomain: Set) -> SetHomset: ...

    @abstract_method
    def End(self) -> SetEndset: ...

    @abstract_method
    def Aut(self) -> SetAutset: ...


class _SetElementMethods:
    r"""Methods on elements of objects in ``Sets()``."""

    @abstract_method
    def __eq__(self, other: SetElement) -> bool: ...

    @abstract_method
    def __hash__(self) -> int: ...

    @abstract_method
    def cartesian_product(self, *elements: SetElement) -> SetElement: ...


class _SetMorphismMethods:
    r"""Methods on morphisms between sets."""

    @abstract_method
    def domain(self) -> Set: ...

    @abstract_method
    def codomain(self) -> Set: ...

    @abstract_method
    def image(self, domain_subset: Set | None = None) -> Set:
        r"""Return the image of ``domain_subset`` or of the full domain."""
        ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    def is_bijective(self) -> bool:
        return self.is_injective() and self.is_surjective()

    @abstract_method
    def __call__(self, x: SetElement) -> SetElement: ...

    @abstract_method
    def pre_image(self, y: SetElement) -> Set: ...

    @abstract_method
    def pre_compose(self, other: SetMorphism) -> SetMorphism:
        r"""Return the composition ``self`` after ``other``."""
        ...

    @abstract_method
    def post_compose(self, other: SetMorphism) -> SetMorphism:
        r"""Return the composition ``other`` after ``self``."""
        ...

    def is_isomorphism(self) -> bool:
        return self.is_bijective()


# ---------------------------------------------------------------------------
# Sets -- the root category
# ---------------------------------------------------------------------------


class Sets(Category_singleton):
    r"""Replacement set category, staged below Sage's existing ``Sets()``.

    Objects in ``Sets()`` are any Sage parents that lie in ``SageSets()``.
    The module docstring records the full public category hierarchy and constructor
    refinement map.
    """

    def __contains__(self, S: Any) -> bool:
        match S:
            case _ if isinstance(S, Category) and S.is_subcategory(self):
                return True
            case _ if S in SageSets():
                return True
            case _:
                return False

    @final
    def super_categories(self) -> list[Category]:
        return [SageSets()]

    @final
    def additional_structure(self):
        return None

    # ------------------------------------------------------------------
    # SubcategoryMethods -- available on every subcategory of Sets()
    # ------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        def Finite(self):
            return self._with_axiom("Finite")

        @cached_method
        def Infinite(self):
            return self._with_axiom("Infinite")

        @cached_method
        def Countable(self):
            return self._with_axiom("Countable")

        @cached_method
        def Uncountable(self):
            return self._with_axiom("Uncountable")

        @cached_method
        def Facade(self):
            return self._with_axiom("Facade")

        @cached_method
        def Topological(self):
            return self._with_axiom("Topological")

        @cached_method
        def Metric(self):
            return self._with_axiom("Metric")

        @cached_method
        def TotallyOrdered(self):
            return self._with_axiom("TotallyOrdered")

        @cached_method
        def Graded(self):
            return self._with_axiom("Graded")

        @cached_method
        def GSets(self, acting_group: Group):
            from .subcategories.group_actions import _GSets

            return _GSets(acting_group, self)

        @cached_method
        def CartesianProducts(self):
            from sage.categories.cartesian_product import CartesianProductsCategory
            return CartesianProductsCategory.category_of(self)

        @cached_method
        def Subquotients(self):
            from .subcategories.constructions.subquotients import _Subquotients

            return _Subquotients.category_of(self)

        @cached_method
        def Quotients(self):
            from .subcategories.constructions.quotients import _Quotients
            return _Quotients.category_of(self)

        @cached_method
        def Subobjects(self):
            from .subcategories.constructions.subobjects import _Subobjects
            return _Subobjects.category_of(self)

        @cached_method
        def Subsets(self):
            return self.Subobjects()

        @cached_method
        def IsomorphicObjects(self):
            from .subcategories.constructions.isomorphic_objects import _IsomorphicObjects

            return _IsomorphicObjects.category_of(self)

        @cached_method
        def WithRealizations(self):
            from .subcategories.constructions.with_realizations import _WithRealizations

            return _WithRealizations.category_of(self)

        @cached_method
        def Realizations(self):
            from .subcategories.constructions.realizations import _Realizations

            return _Realizations.category_of(self)

        @cached_method
        def Homsets(self):
            return SetHomsets()

        @cached_method
        def Endsets(self):
            return self.Homsets().Endset()

        @cached_method
        def Autsets(self):
            return self.Homsets().Autset()

    # ------------------------------------------------------------------
    # Constructors -- named Sage set entry points
    # ------------------------------------------------------------------

    class Constructors:
        r"""Named Sage set constructor entry points.

        Every method calls the canonical Sage constructor, then refines
        the resulting parent into ``Sets()`` and the most specific
        one-object subcategory.

        Usage::

            Sets().Constructors().Primes()
            Sets().Constructors().Set(ZZ)
            Sets().Constructors().IntegerRange(2, 100, 5)
        """

        def __init__(self, category):
            self._category = category

        def __repr__(self) -> str:
            return "Sets constructors"

        def Set(self, X=None):
            r"""Return ``Set(X)``, refined into its one-object subcategory."""
            from sage.sets.set import Set as SageSet

            from .subcategories.set_objects import _SetObjects, _SetObjectsEnumerated

            S = SageSet() if X is None else SageSet(X)
            extra = _SetObjectsEnumerated() if S.is_finite() else _SetObjects()
            return refine_category(S, [Sets(), extra])

        def FiniteEnumeratedSet(self, elements):
            r"""Return ``FiniteEnumeratedSet(elements)``, refined into its subcategory."""
            from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as SageFES

            from .subcategories.finite_enumerated_set import _FiniteEnumeratedSetObjects

            return refine_category(SageFES(elements), [Sets(), _FiniteEnumeratedSetObjects()])

        def IntegerRange(self, *args, **kwds):
            r"""Return an ``IntegerRange``, refined into its subcategory."""
            from sage.sets.integer_range import IntegerRange as SageIR

            from .subcategories.integer_range import _IntegerRangeSets

            return refine_category(SageIR(*args, **kwds), [Sets(), _IntegerRangeSets()])

        def NonNegativeIntegers(self):
            r"""Return ``NonNegativeIntegers()``, refined into its subcategory."""
            from sage.sets.non_negative_integers import NonNegativeIntegers as SageNN

            from .subcategories.non_negative_integers import _NonNegativeIntegersSets

            return refine_category(SageNN(), [Sets(), _NonNegativeIntegersSets()])

        def PositiveIntegers(self):
            r"""Return ``PositiveIntegers()``, refined into its subcategory."""
            from sage.sets.positive_integers import PositiveIntegers as SagePP

            from .subcategories.positive_integers import _PositiveIntegersSets

            return refine_category(SagePP(), [Sets(), _PositiveIntegersSets()])

        def Primes(self, *args, **kwds):
            r"""Return ``Primes(*args, **kwds)``, refined into its subcategory."""
            from sage.sets.primes import Primes as SagePrimes

            from .subcategories.primes import _PrimesSets

            return refine_category(SagePrimes(*args, **kwds), [Sets(), _PrimesSets()])

        def RealSet(self, *args, **kwds) -> RealSubset:
            r"""Return a ``RealSet``, refined into its subcategory."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet(*args, **kwds), [Sets(), _RealSets()])

        def RealSetInterval(
            self,
            lower: RealNumber,
            upper: RealNumber,
            *,
            lower_closed: bool | None = None,
            upper_closed: bool | None = None,
            **kwds: object,
        ) -> RealSubset:
            r"""Return ``RealSet.interval(lower, upper, ...)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            S = SageRealSet.interval(
                lower,
                upper,
                lower_closed=lower_closed,
                upper_closed=upper_closed,
                **kwds,
            )
            return refine_category(S, [Sets(), _RealSets()])

        def OpenRealInterval(self, lower: RealNumber, upper: RealNumber, **kwds: object) -> RealOpenSet:
            r"""Return ``RealSet.open(lower, upper)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.open(lower, upper, **kwds), [Sets(), _RealSets()])

        def ClosedRealInterval(self, lower: RealNumber, upper: RealNumber, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.closed(lower, upper)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.closed(lower, upper, **kwds), [Sets(), _RealSets()])

        def RealPoint(self, point: RealNumber, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.point(point)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.point(point, **kwds), [Sets(), _RealSets()])

        def OpenClosedRealInterval(self, lower: RealNumber, upper: RealNumber, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.open_closed(lower, upper)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.open_closed(lower, upper, **kwds), [Sets(), _RealSets()])

        def ClosedOpenRealInterval(self, lower: RealNumber, upper: RealNumber, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.closed_open(lower, upper)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.closed_open(lower, upper, **kwds), [Sets(), _RealSets()])

        def UnboundedBelowClosedRealInterval(self, bound: RealNumber, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.unbounded_below_closed(bound)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.unbounded_below_closed(bound, **kwds), [Sets(), _RealSets()])

        def UnboundedBelowOpenRealInterval(self, bound: RealNumber, **kwds: object) -> RealOpenSet:
            r"""Return ``RealSet.unbounded_below_open(bound)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.unbounded_below_open(bound, **kwds), [Sets(), _RealSets()])

        def UnboundedAboveClosedRealInterval(self, bound: RealNumber, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.unbounded_above_closed(bound)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.unbounded_above_closed(bound, **kwds), [Sets(), _RealSets()])

        def UnboundedAboveOpenRealInterval(self, bound: RealNumber, **kwds: object) -> RealOpenSet:
            r"""Return ``RealSet.unbounded_above_open(bound)``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.unbounded_above_open(bound, **kwds), [Sets(), _RealSets()])

        def RealLine(self, **kwds: object) -> RealSubset:
            r"""Return ``RealSet.real_line()``, refined into ``RealSets``."""
            from sage.sets.real_set import RealSet as SageRealSet

            from .subcategories.real_set import _RealSets

            return refine_category(SageRealSet.real_line(**kwds), [Sets(), _RealSets()])

        def RecursivelyEnumeratedSet(self, seeds, successors, *args, **kwds):
            r"""Return a ``RecursivelyEnumeratedSet``, refined into its subcategory."""
            from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as SageRES

            from .subcategories.recursively_enumerated import _RecursivelyEnumeratedSets

            S = SageRES(seeds, successors, *args, **kwds)
            return refine_category(S, [Sets(), _RecursivelyEnumeratedSets()])

        def DisjointUnionEnumeratedSets(self, family, **kwds):
            r"""Return a ``DisjointUnionEnumeratedSets``, refined into its subcategory."""
            from sage.sets.disjoint_union_enumerated_sets import (
                DisjointUnionEnumeratedSets as SageDUES,
            )

            from .subcategories.disjoint_union import _DisjointUnionEnumeratedSets

            S = SageDUES(family, **kwds)
            return refine_category(S, [Sets(), _DisjointUnionEnumeratedSets()])

        def CartesianProduct(self, factors: Sequence[Set], **kwds: Any) -> Set:
            r"""Return the Cartesian product of a sequence of set parents."""
            from sage.sets.cartesian_product import CartesianProduct as SageCP

            from .subcategories.cartesian_product import _CartesianProductSets

            category = kwds.pop("category", Sets().CartesianProducts())
            S = SageCP(tuple(factors), category=category, **kwds)
            return refine_category(S, [Sets(), _CartesianProductSets()])

        def ConditionSet(self, universe, *predicates, **kwds):
            r"""Return a ``ConditionSet``, refined into its subcategory."""
            from sage.sets.condition_set import ConditionSet as SageCS

            from .subcategories.condition import _ConditionSets

            return refine_category(SageCS(universe, *predicates, **kwds), [Sets(), _ConditionSets()])

        def ImageSubobject(self, f, domain_subset, **kwds):
            r"""Return ``ImageSubobject(f, domain_subset)``, refined into its subcategory."""
            from sage.sets.image_set import ImageSubobject as SageIS

            from .subcategories.image import _ImageSets

            return refine_category(SageIS(f, domain_subset, **kwds), [Sets(), _ImageSets()])

        def TotallyOrderedFiniteSet(self, elements, **kwds):
            r"""Return a ``TotallyOrderedFiniteSet``, refined into its subcategory."""
            from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet as SageTOFS

            from .subcategories.totally_ordered_finite import _TotallyOrderedFiniteSets

            S = SageTOFS(elements, **kwds)
            return refine_category(S, [Sets(), _TotallyOrderedFiniteSets()])

        def FiniteSetMaps(
            self,
            domain: FiniteSet | int,
            codomain: FiniteSet | int | None = None,
            **kwds: Any,
        ) -> FiniteSet:
            r"""Return the finite set of all functions ``domain -> codomain``.

            With only ``domain`` specified, Sage constructs the endomap set
            ``Map(domain, domain)``, whose elements form a finite monoid under
            composition.
            """
            from sage.sets.finite_set_maps import FiniteSetMaps as SageFSM

            from .subcategories.finite_set_maps import _FiniteSetMapsSets

            S = SageFSM(domain, **kwds) if codomain is None else SageFSM(domain, codomain, **kwds)
            return refine_category(S, [Sets(), _FiniteSetMapsSets()])

        def Family(self, indices, function=None, **kwds):
            r"""Return a ``Family``, refined into its subcategory."""
            from sage.sets.family import Family as SageFamily

            from .subcategories.family import _FamilySets

            S = SageFamily(indices, **kwds) if function is None else SageFamily(indices, function, **kwds)
            return refine_category(S, [Sets(), _FamilySets()])

        def EnumeratedSetFromIterator(self, f, args=(), **kwds):
            r"""Return an ``EnumeratedSetFromIterator``, refined into its subcategory."""
            from sage.sets.set_from_iterator import EnumeratedSetFromIterator as SageESFI

            from .subcategories.enumerated_from_iterator import _EnumeratedSetsFromIterator

            return refine_category(SageESFI(f, args, **kwds), [Sets(), _EnumeratedSetsFromIterator()])

        def cartesian_product(self, factors: Sequence[Set]) -> Set:
            r"""Return Sage's categorical Cartesian product of ``factors``."""
            from sage.categories.cartesian_product import cartesian_product

            from .subcategories.cartesian_product import _CartesianProductSets

            return refine_category(cartesian_product(list(factors)), [Sets(), _CartesianProductSets()])

    _Constructors = Constructors

    @cached_method
    def Constructors(self):
        r"""Return the named Sage set constructor collector."""
        return self.__class__._Constructors(self)

    @cached_method
    def Homsets(self):
        r"""Return the category of set homsets."""
        return SetHomsets()

    @cached_method
    def Endsets(self):
        r"""Return the category of set endsets."""
        return self.Homsets().Endset()

    @cached_method
    def Autsets(self):
        r"""Return the category of set autsets."""
        return self.Homsets().Autset()

    # ------------------------------------------------------------------
    # Axiomatic subcategories and construction categories
    # ------------------------------------------------------------------

    Finite = LazyImport("category_specs.sets.subcategories.finite", "_FiniteSets")
    Infinite = LazyImport("category_specs.sets.subcategories.infinite", "_InfiniteSets")
    Countable = LazyImport("category_specs.sets.subcategories.countable", "_CountableSets")
    Uncountable = LazyImport("category_specs.sets.subcategories.uncountable", "_UncountableSets")
    Facade = LazyImport("category_specs.sets.subcategories.facade", "_FacadeSets")
    Topological = LazyImport("category_specs.topological_spaces", "_TopologicalSpaces")
    TotallyOrdered = LazyImport("category_specs.sets.subcategories.totally_ordered", "_TotallyOrdered")
    Graded = LazyImport("category_specs.sets.subcategories.graded", "_GradedSets")
    Metric = LazyImport("category_specs.topological_spaces", "_MetricSpaces")
    Subquotients = LazyImport("category_specs.sets.subcategories.constructions.subquotients", "_Subquotients")
    Subobjects = LazyImport("category_specs.sets.subcategories.constructions.subobjects", "_Subobjects")
    Subsets = Subobjects
    Quotients = LazyImport("category_specs.sets.subcategories.constructions.quotients", "_Quotients")
    IsomorphicObjects = LazyImport(
        "category_specs.sets.subcategories.constructions.isomorphic_objects",
        "_IsomorphicObjects",
    )
    WithRealizations = LazyImport(
        "category_specs.sets.subcategories.constructions.with_realizations",
        "_WithRealizations",
    )
    Realizations = LazyImport(
        "category_specs.sets.subcategories.constructions.realizations",
        "_Realizations",
    )

    ParentMethods = _SetObjectMethods
    ElementMethods = _SetElementMethods
    MorphismMethods = _SetMorphismMethods
