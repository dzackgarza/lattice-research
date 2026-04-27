r"""Set-specific homset, endset, and autset categories.

Generic Autset construction belongs in the repository-level homset layer. This file
only declares the set-theoretic method surfaces: functions, endomorphisms, and
automorphisms of sets.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.groups import Groups as SageGroups
from sage.categories.homsets import HomsetsCategory
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..homsets.utils import refine_automorphism_set_from_endset

if TYPE_CHECKING:
    from ..types import Cardinality, Set, SetAutset, SetElement, SetEndset, SetMorphism, Subset


class _SetHomsetObjects:
    @abstract_method
    def domain(self) -> Set: ...

    @abstract_method
    def codomain(self) -> Set: ...

    @abstract_method
    def __call__(self, *args: object, **kwds: object) -> SetMorphism: ...

    @abstract_method
    def __contains__(self, obj: Any) -> bool: ...


class _SetMorphisms:
    @abstract_method
    def domain(self) -> Set: ...

    @abstract_method
    def codomain(self) -> Set: ...

    @abstract_method
    def __call__(self, x: SetElement) -> SetElement: ...

    @abstract_method
    def image(self, domain_subset: Subset | None = None) -> Subset: ...

    @abstract_method
    def pre_image(self, y: SetElement) -> Subset: ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    def is_bijective(self) -> bool:
        return self.is_injective() and self.is_surjective()

    def is_isomorphism(self) -> bool:
        return self.is_bijective()


class _SetEndomorphisms:
    @abstract_method
    def is_invertible(self) -> bool: ...

    @abstract_method
    def inverse(self) -> SetMorphism: ...

    @abstract_method
    def order(self) -> Cardinality: ...


class _SetAutomorphisms:
    def is_invertible(self) -> bool:
        return True

    def is_injective(self) -> bool:
        return True

    def is_surjective(self) -> bool:
        return True

    def is_bijective(self) -> bool:
        return True

    def is_isomorphism(self) -> bool:
        return True

    @abstract_method
    def inverse(self) -> SetMorphism: ...

    @abstract_method
    def order(self) -> Cardinality: ...


class SetHomsets(HomsetsCategory):
    r"""Category of homsets between sets."""

    def extra_super_categories(self) -> list:
        return [SageSets()]

    class SubcategoryMethods:
        @cached_method
        def Endset(self) -> SetEndset:
            return self._with_axiom("Endset")

        @cached_method
        def Autset(self) -> SetAutset:
            return self._with_axiom("Autset")

    ParentMethods = _SetHomsetObjects
    ElementMethods = _SetMorphisms
    Endset = LazyImport(__name__, "_SetEndsets")
    Autset = LazyImport(__name__, "_SetAutsets")


class _SetEndsets(CategoryWithAxiom):
    _base_category_class_and_axiom = (SetHomsets, "Endset")
    Autset = LazyImport(__name__, "_SetAutsets")

    def extra_super_categories(self) -> list:
        return [SageSets()]

    class ParentMethods:
        @abstract_method
        def base_set(self) -> Set: ...

        @abstract_method
        def domain(self) -> Set: ...

        @abstract_method
        def codomain(self) -> Set: ...

        @abstract_method
        def identity(self) -> SetMorphism: ...

        @abstract_method
        def Aut(self) -> SetAutset: ...

    ElementMethods = _SetEndomorphisms


class _SetAutsets(CategoryWithAxiom):
    _base_category_class_and_axiom = (SetHomsets, "Autset")

    def extra_super_categories(self) -> list:
        return [self.base_category().Endset(), SageGroups(), SageSets()]

    def from_endset(self, endset: SetEndset) -> SetAutset:
        r"""Refine the generic Autset over ``endset``.

        The repository-level homset layer owns ConditionSet-based Autset construction.
        """
        return refine_automorphism_set_from_endset(endset, self)

    class ParentMethods:
        @abstract_method
        def endset(self) -> SetEndset: ...

        def domain(self) -> Set:
            return self.endset().domain()

        def codomain(self) -> Set:
            return self.endset().codomain()

        @abstract_method
        def identity(self) -> SetMorphism: ...

    ElementMethods = _SetAutomorphisms
