r"""Set category surface for the category spec redesign.

This file defines ``Sets()`` as a staged non-destructive replacement for
Sage's ``Sets()``. Reading this file is sufficient to understand the full
public surface of the category.

Naming convention:
    Sets()      -- our category (this file / package)
    SageSets()  -- sage.categories.sets_cat.Sets()

Subcategory lattice::

    Sets()
    |- .Finite()                  -> FiniteSets
    |- .Infinite()                -> InfiniteSets
    |- .Countable()               -> CountableSets
    |   |- .Finite()              -> FiniteCountableSets
    |   `- .Infinite()            -> InfiniteCountableSets
    |- .Uncountable()             -> UncountableSets
    |- .Facade()                  -> FacadeSets
    |- .Topological()             -> TopologicalSets
    |   `- .Metric()              -> MetricSets
    |- .TotallyOrdered()          -> TotallyOrderedSets
    `- .WithBooleanOps()          -> WithBooleanOpsSets

Named set constructors (via ``Sets().Constructors()``)::

    Sets().Constructors().Set(X)
    Sets().Constructors().Primes()
    Sets().Constructors().IntegerRange(2, 100, 5)
    Sets().Constructors().NonNegativeIntegers()
    Sets().Constructors().PositiveIntegers()
    Sets().Constructors().RealSet((0, 1))
    Sets().Constructors().FiniteEnumeratedSet([1, 2, 3])
    Sets().Constructors().RecursivelyEnumeratedSet([0], lambda n: [n + 1])
    Sets().Constructors().DisjointUnionEnumeratedSets(family)
    Sets().Constructors().CartesianProduct([A, B])
    Sets().Constructors().cartesian_product(A, B)
    Sets().Constructors().ConditionSet(ZZ, predicate)
    Sets().Constructors().ImageSubobject(f, X)
    Sets().Constructors().TotallyOrderedFiniteSet(['a', 'b', 'c'])
    Sets().Constructors().FiniteSetMaps(domain, codomain)
    Sets().Constructors().Family(indices, function)
    Sets().Constructors().EnumeratedSetFromIterator(callable)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import (
        Cardinality,
        RealNumber,
        Set,
        SetElement,
        SetMorphism,
        SympySet,
    )


# ---------------------------------------------------------------------------
# Sets -- the root category
# ---------------------------------------------------------------------------


class Sets(Category_singleton):
    r"""Replacement set category, staged below Sage's existing ``Sets()``.

    Objects in ``Sets()`` are any Sage parents that lie in ``SageSets()``.

    Axiom subcategories::

        Sets().Finite()          -- finite sets
        Sets().Infinite()        -- infinite sets
        Sets().Countable()       -- countable (enumerable) sets
        Sets().Uncountable()     -- uncountable sets
        Sets().Facade()          -- facade sets
        Sets().Topological()     -- topological sets
        Sets().Topological().Metric()  -- metric sets
        Sets().TotallyOrdered()  -- totally ordered sets
        Sets().WithBooleanOps()  -- sets with boolean operations

    Named constructors::

        Sets().Constructors().Primes()
        Sets().Constructors().IntegerRange(n)
        ...
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
        def WithBooleanOps(self):
            return self._with_axiom("WithBooleanOps")

        @cached_method
        def CartesianProducts(self):
            from sage.categories.cartesian_product import CartesianProductsCategory
            return CartesianProductsCategory.category_of(self)

        @cached_method
        def Subquotients(self):
            from sage.categories.subquotients import SubquotientsCategory
            return SubquotientsCategory.category_of(self)

        @cached_method
        def Quotients(self):
            from sage.categories.quotients import QuotientsCategory
            return QuotientsCategory.category_of(self)

        @cached_method
        def Subobjects(self):
            from sage.categories.subobjects import SubobjectsCategory
            return SubobjectsCategory.category_of(self)

        @cached_method
        def IsomorphicObjects(self):
            from sage.categories.isomorphic_objects import IsomorphicObjectsCategory
            return IsomorphicObjectsCategory.category_of(self)

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
            from .subcategories.finite_named import _FiniteEnumeratedSetObjects

            return refine_category(SageFES(elements), [Sets(), _FiniteEnumeratedSetObjects()])

        def IntegerRange(self, *args, **kwds):
            r"""Return an ``IntegerRange``, refined into its subcategory."""
            from sage.sets.integer_range import IntegerRange as SageIR
            from .subcategories.numbers import _IntegerRangeSets

            return refine_category(SageIR(*args, **kwds), [Sets(), _IntegerRangeSets()])

        def NonNegativeIntegers(self):
            r"""Return ``NonNegativeIntegers()``, refined into its subcategory."""
            from sage.sets.non_negative_integers import NonNegativeIntegers as SageNN
            from .subcategories.numbers import _NonNegativeIntegersSets

            return refine_category(SageNN(), [Sets(), _NonNegativeIntegersSets()])

        def PositiveIntegers(self):
            r"""Return ``PositiveIntegers()``, refined into its subcategory."""
            from sage.sets.positive_integers import PositiveIntegers as SagePP
            from .subcategories.numbers import _PositiveIntegersSets

            return refine_category(SagePP(), [Sets(), _PositiveIntegersSets()])

        def Primes(self, *args, **kwds):
            r"""Return ``Primes(*args, **kwds)``, refined into its subcategory."""
            from sage.sets.primes import Primes as SagePrimes
            from .subcategories.numbers import _PrimesSets

            return refine_category(SagePrimes(*args, **kwds), [Sets(), _PrimesSets()])

        def RealSet(self, *args, **kwds):
            r"""Return a ``RealSet``, refined into its subcategory."""
            from sage.sets.real_set import RealSet as SageRealSet
            from .subcategories.real_intervals import _RealSets

            return refine_category(SageRealSet(*args, **kwds), [Sets(), _RealSets()])

        def RecursivelyEnumeratedSet(self, seeds, successors, *args, **kwds):
            r"""Return a ``RecursivelyEnumeratedSet``, refined into its subcategory."""
            from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as SageRES
            from .subcategories.enumerated_constructions import _RecursivelyEnumeratedSets

            S = SageRES(seeds, successors, *args, **kwds)
            return refine_category(S, [Sets(), _RecursivelyEnumeratedSets()])

        def DisjointUnionEnumeratedSets(self, family, **kwds):
            r"""Return a ``DisjointUnionEnumeratedSets``, refined into its subcategory."""
            from sage.sets.disjoint_union_enumerated_sets import (
                DisjointUnionEnumeratedSets as SageDUES,
            )
            from .subcategories.enumerated_constructions import _DisjointUnionEnumeratedSets

            S = SageDUES(family, **kwds)
            return refine_category(S, [Sets(), _DisjointUnionEnumeratedSets()])

        def CartesianProduct(self, sets, **kwds):
            r"""Return a ``CartesianProduct``, refined into its subcategory."""
            from sage.sets.cartesian_product import CartesianProduct as SageCP
            from .subcategories.enumerated_constructions import _CartesianProductSets

            category = kwds.pop("category", Sets().CartesianProducts())
            S = SageCP(tuple(sets), category=category, **kwds)
            return refine_category(S, [Sets(), _CartesianProductSets()])

        def ConditionSet(self, universe, *predicates, **kwds):
            r"""Return a ``ConditionSet``, refined into its subcategory."""
            from sage.sets.condition_set import ConditionSet as SageCS
            from .subcategories.condition import _ConditionSets

            return refine_category(SageCS(universe, *predicates, **kwds), [Sets(), _ConditionSets()])

        def ImageSubobject(self, f, domain_subset, **kwds):
            r"""Return ``ImageSubobject(f, domain_subset)``, refined into its subcategory."""
            from sage.sets.image_set import ImageSubobject as SageIS
            from .subcategories.enumerated_constructions import _ImageSets

            return refine_category(SageIS(f, domain_subset, **kwds), [Sets(), _ImageSets()])

        def TotallyOrderedFiniteSet(self, elements, **kwds):
            r"""Return a ``TotallyOrderedFiniteSet``, refined into its subcategory."""
            from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet as SageTOFS
            from .subcategories.finite_named import _TotallyOrderedFiniteSets

            S = SageTOFS(elements, **kwds)
            return refine_category(S, [Sets(), _TotallyOrderedFiniteSets()])

        def FiniteSetMaps(self, domain, codomain=None, **kwds):
            r"""Return a ``FiniteSetMaps`` object, refined into its subcategory."""
            from sage.sets.finite_set_maps import FiniteSetMaps as SageFSM
            from .subcategories.finite_named import _FiniteSetMapsSets

            S = SageFSM(domain, **kwds) if codomain is None else SageFSM(domain, codomain, **kwds)
            return refine_category(S, [Sets(), _FiniteSetMapsSets()])

        def Family(self, indices, function=None, **kwds):
            r"""Return a ``Family``, refined into its subcategory."""
            from sage.sets.family import Family as SageFamily
            from .subcategories.enumerated_constructions import _FamilySets

            S = SageFamily(indices, **kwds) if function is None else SageFamily(indices, function, **kwds)
            return refine_category(S, [Sets(), _FamilySets()])

        def EnumeratedSetFromIterator(self, f, args=(), **kwds):
            r"""Return an ``EnumeratedSetFromIterator``, refined into its subcategory."""
            from sage.sets.set_from_iterator import EnumeratedSetFromIterator as SageESFI
            from .subcategories.enumerated_constructions import _EnumeratedSetsFromIterator

            return refine_category(SageESFI(f, args, **kwds), [Sets(), _EnumeratedSetsFromIterator()])

        def cartesian_product(self, *factors):
            r"""Return ``cartesian_product(factors)``, refined into its subcategory."""
            from sage.categories.cartesian_product import cartesian_product
            from .subcategories.enumerated_constructions import _CartesianProductSets

            return refine_category(cartesian_product(list(factors)), [Sets(), _CartesianProductSets()])

    @cached_method
    def Constructors(self):
        r"""Return the named Sage set constructor collector."""
        return self.__class__.Constructors(self)

    # ------------------------------------------------------------------
    # ParentMethods -- abstract interface for all objects in Sets()
    # ------------------------------------------------------------------

    class ParentMethods:
        r"""Abstract parent methods for all objects in ``Sets()``."""

        @abstract_method
        def __contains__(self, x: Any) -> bool:
            r"""Return ``True`` if ``x`` is an element of ``self``."""
            ...

        @abstract_method
        def an_element(self) -> SetElement:
            r"""Return a typical element of ``self``."""
            ...

        def some_elements(self) -> list:
            r"""Return a list of elements of ``self``, for testing purposes."""
            return [self.an_element()]

        def is_parent_of(self, element: SetElement) -> bool:
            r"""Return whether ``self`` is the parent of ``element`` (no coercion)."""
            from sage.structure.element import parent
            return parent(element) == self

        @abstract_method
        def cardinality(self) -> Cardinality:
            r"""Return the number of elements (a Sage Integer or ``infinity``)."""
            ...

        @abstract_method
        def is_empty(self) -> bool:
            r"""Return whether ``self`` contains no elements."""
            ...

        @abstract_method
        def is_finite(self) -> bool:
            r"""Return whether ``self`` is a finite set."""
            ...

        def is_enumerated(self) -> bool:
            r"""Return whether ``self`` is an enumerated set."""
            return False

        def is_facade(self) -> bool:
            r"""Return whether ``self`` is a facade set."""
            return False

        def is_topological(self) -> bool:
            r"""Return whether ``self`` is a topological set."""
            return False

        def is_metric(self) -> bool:
            r"""Return whether ``self`` is a metric set."""
            return False

        def is_totally_ordered(self) -> bool:
            r"""Return whether ``self`` is a totally ordered set."""
            return False

        @abstract_method
        def is_subset(self, other: Set) -> bool:
            r"""Return whether ``self`` is a subset of ``other``."""
            ...

        @abstract_method
        def is_superset(self, other: Set) -> bool:
            r"""Return whether ``self`` is a superset of ``other``."""
            ...

        def __le__(self, other: Set) -> bool:
            return self.is_subset(other)

        def __ge__(self, other: Set) -> bool:
            return self.is_superset(other)

        @abstract_method
        def union(self, X: Set) -> Set: ...

        @abstract_method
        def intersection(self, X: Set) -> Set: ...

        @abstract_method
        def difference(self, X: Set) -> Set: ...

        @abstract_method
        def symmetric_difference(self, X: Set) -> Set: ...

        @abstract_method
        def complement(self) -> Set:
            r"""Return the complement of ``self`` in its ambient space."""
            ...

        def __or__(self, X: Set) -> Set:
            return self.union(X)

        def __and__(self, X: Set) -> Set:
            return self.intersection(X)

        def __xor__(self, X: Set) -> Set:
            return self.symmetric_difference(X)

        def __add__(self, X: Set) -> Set:
            return self.union(X)

        def __sub__(self, X: Set) -> Set:
            return self.difference(X)

        @abstract_method
        def subsets(self, size=None) -> Set:
            r"""Return the ``Subsets`` object for ``self``."""
            ...

        @abstract_method
        def subsets_lattice(self) -> Set:
            r"""Return the lattice of subsets ordered by containment (finite only)."""
            ...

        @abstract_method
        def _sympy_(self) -> SympySet:
            r"""Return an equivalent SymPy set."""
            ...

    # ------------------------------------------------------------------
    # ElementMethods
    # ------------------------------------------------------------------

    class ElementMethods:
        r"""Abstract element methods for elements of sets in ``Sets()``."""

        @abstract_method
        def __eq__(self, other: SetElement) -> bool: ...

        @abstract_method
        def __hash__(self) -> int: ...

    # ------------------------------------------------------------------
    # MorphismMethods
    # ------------------------------------------------------------------

    class MorphismMethods:
        r"""Abstract morphism methods for maps between sets."""

        @abstract_method
        def domain(self) -> Set: ...

        @abstract_method
        def codomain(self) -> Set: ...

        @abstract_method
        def image(self, X: Set = None) -> Set:
            r"""Return the image of ``X`` (or ``self.domain()`` if ``X`` is ``None``)."""
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

    # ------------------------------------------------------------------
    # Axiomatic subcategory class slots -- wired after subcategory imports
    # ------------------------------------------------------------------

    Finite: type
    Infinite: type
    Countable: type
    Uncountable: type
    Facade: type
    Topological: type
    TotallyOrdered: type
    WithBooleanOps: type


# ---------------------------------------------------------------------------
# Import and wire axiomatic subcategories
# ---------------------------------------------------------------------------

from .subcategories.finite import _FiniteSets
from .subcategories.countable import _CountableSets, _FiniteCountableSets, _InfiniteCountableSets
from .subcategories.infinite import _InfiniteSets
from .subcategories.uncountable import _UncountableSets
from .subcategories.facade import _FacadeSets
from .subcategories.topological import _MetricSets, _TopologicalSets
from .subcategories.totally_ordered import _TotallyOrdered
from .subcategories.boolean_ops import _WithBooleanOpsSets

Sets.Finite = _FiniteSets
Sets.Infinite = _InfiniteSets
Sets.Countable = _CountableSets
Sets.Uncountable = _UncountableSets
Sets.Facade = _FacadeSets
Sets.Topological = _TopologicalSets
Sets.TotallyOrdered = _TotallyOrdered
Sets.WithBooleanOps = _WithBooleanOpsSets
