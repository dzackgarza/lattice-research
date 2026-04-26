"""Static set category surface for the category spec redesign.

This file defines a new ``Sets`` category as a staged replacement for Sage's
set category.  Every named category below is mathematical: it records the
expected Sage-backed method surface.

Naming convention:
    Sets()          -- our category (this file / package)
    SageSets()      -- sage.categories.sets_cat.Sets()

Design:
    ``Sets()`` is a singleton ``Category_singleton`` sitting below Sage's
    ``Sets()`` in the category hierarchy (``super_categories = [SageSets()]``).
    Axiom subcategories are wired via ``_base_category_class_and_axiom``; named
    set constructors are collected under ``Sets().NamedSets()``.

Subcategory lattice (our hierarchy)::

    Sets()
    ├─ .Finite()                  → FiniteSets
    ├─ .Infinite()                → InfiniteSets
    ├─ .Countable()               → CountableSets
    │   ├─ .Finite()              → FiniteCountableSets
    │   └─ .Infinite()            → InfiniteCountableSets
    ├─ .Uncountable()             → UncountableSets
    ├─ .Facade()                  → FacadeSets
    ├─ .Topological()             → TopologicalSets
    │   └─ .Metric()              → MetricSets
    └─ .TotallyOrdered()          → TotallyOrdered
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories import category_with_axiom as _category_with_axiom
from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from .axioms import (
    _CountableSets,
    _FacadeSets,
    _FiniteCountableSets,
    _FiniteSets,
    _InfiniteCountableSets,
    _InfiniteSets,
    _MetricSets,
    _TopologicalSets,
    _TotallyOrdered,
    _UncountableSets,
)
from .specialized import _NamedSets

if TYPE_CHECKING:
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer

    Cardinality = Integer | InfinityElement
    SetElement = Any
    SageSet = Any
    SetMorphism = Any


# ---------------------------------------------------------------------------
# Custom axiom registration
# ---------------------------------------------------------------------------

_CUSTOM_AXIOMS = (
    "WithBooleanOps",
    "TotallyOrdered",
    "Topological",
    "Metric",
)


def _register_custom_axioms() -> None:
    missing = tuple(axiom for axiom in _CUSTOM_AXIOMS if axiom not in _category_with_axiom.all_axioms)
    if missing:
        _category_with_axiom.all_axioms += missing


_register_custom_axioms()


# ---------------------------------------------------------------------------
# Sets parent method surface — abstract interface for all objects in Sets()
# ---------------------------------------------------------------------------


class _SetObjectMethods:
    r"""Abstract parent methods for all objects in ``Sets()``."""

    @abstract_method
    def __contains__(self, x) -> bool:
        r"""Return ``True`` if ``x`` is an element of ``self``."""
        ...

    @abstract_method
    def an_element(self) -> SetElement:
        r"""Return a typical element of ``self`` (cached by callers)."""
        ...

    def some_elements(self) -> list:
        r"""Return a list of elements of ``self``, for testing purposes."""
        try:
            return [self.an_element()]
        except Exception as e:  # grain: narrowed
            raise
            return []

    def is_parent_of(self, element) -> bool:
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

    # ------------------------------------------------------------------
    # Boolean operations (mathematically universal for sets)
    # ------------------------------------------------------------------

    @abstract_method
    def is_subset(self, other) -> bool:
        r"""Return whether ``self`` is a subset of ``other``."""
        ...

    @abstract_method
    def is_superset(self, other) -> bool:
        r"""Return whether ``self`` is a superset of ``other``."""
        ...

    def __le__(self, other) -> bool:
        return self.is_subset(other)

    def __ge__(self, other) -> bool:
        return self.is_superset(other)

    @abstract_method
    def union(self, X) -> SageSet:
        r"""Return the set-theoretic union ``self ∪ X``."""
        ...

    @abstract_method
    def intersection(self, X) -> SageSet:
        r"""Return the set-theoretic intersection ``self ∩ X``."""
        ...

    @abstract_method
    def difference(self, X) -> SageSet:
        r"""Return the set-theoretic difference ``self \ X``."""
        ...

    @abstract_method
    def symmetric_difference(self, X) -> SageSet:
        r"""Return the symmetric difference ``self △ X``."""
        ...

    @abstract_method
    def complement(self) -> SageSet:
        r"""Return the complement of ``self`` in its ambient space.

        Requires the ambient set to be defined by context.
        """
        ...

    def __or__(self, X) -> SageSet:
        return self.union(X)

    def __and__(self, X) -> SageSet:
        return self.intersection(X)

    def __xor__(self, X) -> SageSet:
        return self.symmetric_difference(X)

    def __add__(self, X) -> SageSet:
        return self.union(X)

    def __sub__(self, X) -> SageSet:
        return self.difference(X)

    @abstract_method
    def subsets(self, size=None) -> SageSet:
        r"""Return the :class:`Subsets` object for ``self``."""
        ...

    @abstract_method
    def subsets_lattice(self):
        r"""Return the lattice of subsets ordered by containment (finite only).宣
        ...

    @abstract_method
    def _sympy_(self):
        r"""Return an equivalent SymPy set."""
        ...


# ---------------------------------------------------------------------------
# Set element method surface
# ---------------------------------------------------------------------------


class _SetElementMethods:
    r"""Abstract element methods for elements of sets in ``Sets()``."""

    @abstract_method
    def __eq__(self, other) -> bool:
        r"""Return whether ``self`` equals ``other``."""
        ...

    @abstract_method
    def __hash__(self) -> int:
        r"""Return the hash value of ``self``."""
        ...


# ---------------------------------------------------------------------------
# Set morphism method surface
# ---------------------------------------------------------------------------


class _SetMorphismMethods:
    r"""Abstract morphism methods for maps between sets (set functions)."""

    @abstract_method
    def domain(self) -> SageSet:
        r"""Return the domain set."""
        ...

    @abstract_method
    def codomain(self) -> SageSet:
        r"""Return the codomain set."""
        ...

    @abstract_method
    def image(self, X=None) -> SageSet:
        r"""Return the image of ``X`` (or ``self.domain()`` if ``X`` is ``None``)."""
        ...

    @abstract_method
    def is_injective(self) -> bool:
        r"""Return whether ``self`` is injective (one-to-one)."""
        ...

    @abstract_method
    def is_surjective(self) -> bool:
        r"""Return whether ``self`` is surjective (onto)."""
        ...

    def is_bijective(self) -> bool:
        r"""Return whether ``self`` is bijective (injective and surjective)."""
        return self.is_injective() and self.is_surjective()

    @abstract_method
    def __call__(self, x) -> SetElement:
        r"""Apply the map to ``x``."""
        ...

    @abstract_method
    def pre_image(self, y) -> SageSet:
        r"""Return the pre-image of ``y`` (a subset of the domain)."""
        ...

    @abstract_method
    def pre_compose(self, other) -> SetMorphism:
        r"""Return the composition ``self ∘ other``."""
        ...

    @abstract_method
    def post_compose(self, other) -> SetMorphism:
        r"""Return the composition ``other ∘ self``."""
        ...

    def is_isomorphism(self) -> bool:
        r"""Return whether ``self`` is a bijection (set-theoretic isomorphism)."""
        return self.is_bijective()


# ---------------------------------------------------------------------------
# Sets — the root category
# ---------------------------------------------------------------------------


class Sets(Category_singleton):
    r"""Replacement set category, staged below Sage's existing ``Sets()``.

    This is the base category for all sets in the redesigned category hierarchy.
    All Sage parents that lie in ``SageSets()`` also lie in ``Sets()`` via
    ``__contains__``.

    Axiom subcategories::

        Sets().Finite()          -- finite sets
        Sets().Infinite()        -- infinite sets
        Sets().Countable()       -- countable sets
        Sets().Uncountable()     -- uncountable sets
        Sets().Facade()          -- facade sets (elements live in another parent)
        Sets().Topological()     -- topological sets
        Sets().Topological().Metric()  -- metric sets
        Sets().TotallyOrdered()  -- totally ordered sets

    Named set constructors::

        Sets().NamedSets().Set(X)
        Sets().NamedSets().Primes()
        Sets().NamedSets().IntegerRange(2, 100, 5)
        ... (see :class:`.specialized._NamedSets`)
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

    @cached_method
    def NamedSets(self):
        r"""Return the named Sage set constructor collector."""
        return _NamedSets(self)

    # ------------------------------------------------------------------
    # SubcategoryMethods — available on every subcategory of Sets()
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
        def NamedSets(self):
            return _NamedSets(self)

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
    # Axiomatic subcategories
    # ------------------------------------------------------------------

    Finite = _FiniteSets
    Infinite = _InfiniteSets
    Countable = _CountableSets
    Uncountable = _UncountableSets
    Facade = _FacadeSets
    Topological = _TopologicalSets
    Metric = _MetricSets
    TotallyOrdered = _TotallyOrdered

    # ------------------------------------------------------------------
    # Method providers
    # ------------------------------------------------------------------

    ParentMethods = _SetObjectMethods
    ElementMethods = _SetElementMethods
    MorphismMethods = _SetMorphismMethods


# ---------------------------------------------------------------------------
# Wire _base_category_class_and_axiom for axiom classes rooted at Sets
# ---------------------------------------------------------------------------

_FiniteSets._base_category_class_and_axiom = (Sets, "Finite")
_InfiniteSets._base_category_class_and_axiom = (Sets, "Infinite")
_CountableSets._base_category_class_and_axiom = (Sets, "Countable")
_UncountableSets._base_category_class_and_axiom = (Sets, "Uncountable")
_FacadeSets._base_category_class_and_axiom = (Sets, "Facade")
_TopologicalSets._base_category_class_and_axiom = (Sets, "Topological")
_TotallyOrdered._base_category_class_and_axiom = (Sets, "TotallyOrdered")

# Axiom chains: Countable.Finite, Countable.Infinite
_FiniteCountableSets._base_category_class_and_axiom = (Sets().Countable, "Finite")
_InfiniteCountableSets._base_category_class_and_axiom = (Sets().Countable, "Infinite")

# Axiom chains: TopologicalSets.Metric
_MetricSets._base_category_class_and_axiom = (_TopologicalSets, "Metric")
