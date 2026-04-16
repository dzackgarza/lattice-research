"""Ring and ideal categories used by the module redesign.

The module surface refines a fixed collection of Sage ring parents into
``ModuleBaseRings``.  Ideals of those rings are still Sage ideals first:
``Ideal_generic.category()`` returns Sage's ``Ideals(R)`` hierarchy.  The
redesign adds ``ModuleBaseIdeals(R)`` as the ring-ideal refinement layer, and
``Modules(R).Ideals()`` supplies the module-subobject view.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.categories.category_types import Category_ideal
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.commutative_ring_ideals import CommutativeRingIdeals
from sage.categories.rings import Rings as SageRings
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import RingElement as SageRingElement

if TYPE_CHECKING:
    from .modules import (
        FreeModuleCategoryObject,
        IdealSubmodulesCategoryObject,
        ModulesCategoryObject,
        TorsionModuleCategoryObject,
    )

Names = str | tuple[str, ...] | None


class ModuleBaseIdeals(Category_ideal):
    r"""
    Sage ideals of a refined module base ring.

    Objects are existing ``Ideal_generic`` / ``Ideal_pid`` instances whose
    categories have been refined into this category.  This is not a ring
    category: an ideal such as ``2*ZZ`` is an ideal object, and the
    module-facing subobject interpretation is supplied separately by
    ``Modules(ZZ).Ideals()``.
    """

    def __init__(self, ring: ModuleBaseRingsCategoryObject):
        if ring not in ModuleBaseRings():
            raise TypeError(f"ring must be refined into ModuleBaseRings(); got {ring!r}")
        Category_ideal.__init__(self, ring)

    def super_categories(self) -> list[Category]:
        return [CommutativeRingIdeals(self.ring())]

    def _repr_object_names(self) -> str:
        return "module-base ideals"

    def _latex_(self) -> str: ...

    class ParentMethods:

        # @override Ideal_generic.ring
        def ring(self) -> ModuleBaseRingsCategoryObject: ...

        # @override Ideal_generic.base_ring
        # @overload ideal parent base ring
        def base_ring(self) -> ModuleBaseRingsCategoryObject: ...

        # @override Ideal_generic.gens
        def gens(self) -> tuple[ModuleBaseRingElement, ...]: ...

        # @override Ideal_generic.gen
        def gen(self, index: int = 0) -> ModuleBaseRingElement: ...

        # @override Ideal_generic.random_element
        def random_element(self, *args, **kwds) -> ModuleBaseRingElement: ...

        # @override Ideal_generic.reduce
        def reduce(self, value: ModuleBaseRingElement) -> ModuleBaseRingElement: ...

        # @override Ideal_pid.gcd
        def gcd(self, other: ModuleBaseIdealCategoryObject) -> ModuleBaseIdealCategoryObject: ...

        # @override Ideal_pid.lcm
        def lcm(self, other: ModuleBaseIdealCategoryObject) -> ModuleBaseIdealCategoryObject: ...

    class ElementMethods:
        ...

    class MorphismMethods:
        ...


class ModuleBaseRings(CategoryWithAxiom):
    r"""
    Subcategory of ``Rings().PrincipalIdealDomains().Commutative()`` whose
    ring parents produce objects in the redesigned module surface.

    Existing ring parents join this category via
    ``ring._refine_category_(ModuleBaseRings())``.  Sage's dynamic dispatch
    then serves ``ParentMethods`` below without creating new ring classes.
    """

    @final
    def super_categories(self) -> list[Category]:
        return [SageRings().PrincipalIdealDomains().Commutative()]

    @final
    def additional_structure(self):
        return None

    @final
    def _repr_object_names(self) -> str:
        return "commutative PID base rings for finitely presented modules"

    def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # Subcategories
    # ------------------------------------------------------------------

    class Local(CategoryWithAxiom):
        r"""Local rings in the module surface (e.g. ``Zp(p)``)."""

        @final
        def super_categories(self) -> list[Category]:
            from sage.categories.local_rings import LocalRings as SageLocalRings
            return [ModuleBaseRings(), SageLocalRings()]

        @final
        def _repr_object_names(self) -> str:
            return "local rings for finitely presented modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def maximal_ideal(self) -> IdealSubmodulesCategoryObject: ...

        class ElementMethods:
            ...
        class MorphismMethods: ...

    class Complete(CategoryWithAxiom):
        r"""Complete rings in the module surface (e.g. ``Zp(p)``)."""

        @final
        def super_categories(self) -> list[Category]:
            # Intersect with Sage's complete ring category when available.
            return [ModuleBaseRings()]

        @final
        def _repr_object_names(self) -> str:
            return "complete rings for finitely presented modules"

        def _latex_(self) -> str: ...

        class ParentMethods: ...
        class ElementMethods:
            ...
        class MorphismMethods: ...

    # Field() is inherited from Rings().PrincipalIdealDomains().Commutative()
    # via the axiom system.  No explicit subcategory needed here.

    # ------------------------------------------------------------------
    # ParentMethods
    # ------------------------------------------------------------------

    class ParentMethods:

        # @override CommutativeRings.unit_ideal
        @abstractmethod
        def unit_ideal(self) -> IdealSubmodulesCategoryObject: ...

        # @override CommutativeRings.nilradical
        @abstractmethod
        def nilradical(self) -> IdealSubmodulesCategoryObject: ...

        # @override CommutativeRings.ideal
        @abstractmethod
        def ideal(self, generator: RingElement, **kwds) -> IdealSubmodulesCategoryObject:
            r"""
            Calls ``super().ideal(generator)``, then refines the result into
            ``ModuleBaseIdeals(self)`` and ``Modules(self).Ideals()``.
            """
            ...

        # @override Ring.__mul__
        @abstractmethod
        def __mul__(self, generator: RingElement) -> IdealSubmodulesCategoryObject:
            r"""Delegates to ``self.ideal(generator)``."""
            ...

        # @override Ring.__rmul__
        @abstractmethod
        def __rmul__(self, generator: RingElement) -> IdealSubmodulesCategoryObject: ...

        # @override CommutativeRings.quotient
        @abstractmethod
        def quotient(
            self,
            modulus: RingElement | IdealSubmodulesCategoryObject,
            names: Names = None,
            **kwds,
        ) -> TorsionModuleCategoryObject:
            r"""
            Calls ``super().quotient(modulus)``, then refines the result via
            ``result._refine_category_(Modules(self).Torsion())``.
            """
            ...

        # @override CommutativeRings.quo
        @abstractmethod
        def quo(
            self,
            modulus: RingElement | IdealSubmodulesCategoryObject,
            names: Names = None,
            **kwds,
        ) -> TorsionModuleCategoryObject: ...

        @final
        def quotient_ring(
            self,
            modulus: RingElement | IdealSubmodulesCategoryObject,
            names: Names = None,
            **kwds,
        ) -> TorsionModuleCategoryObject:
            return self.quotient(modulus, names=names, **kwds)

        @final
        def __truediv__(
            self,
            modulus: RingElement | IdealSubmodulesCategoryObject,
        ) -> TorsionModuleCategoryObject:
            return self.quotient(modulus)

        # @override Ring.__pow__
        @abstractmethod
        def __pow__(self, n: Integer) -> FreeModuleCategoryObject:
            r"""
            Calls Sage's native ``__pow__`` via ``super()``, then refines
            the result via ``result._refine_category_(Modules(self).Free())``.
            """
            ...

        # @override Ring.free_module — deprecated
        @final
        def free_module(self, base=None, basis=None, map=True):
            r"""
            Deprecated in the module surface.  Use ``R ** 1`` instead.

            ``Ring.free_module()`` regards ``R`` as a free rank-1 module over
            itself; in the redesign surface that is simply ``R^1``.
            """
            import warnings
            warnings.warn(
                "Ring.free_module() is deprecated; use R ** 1 instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            return self.__pow__(1)

        # @override CommutativeRings.derivation_module
        @abstractmethod
        def derivation_module(
            self, codomain=None, twist=None
        ) -> ModulesCategoryObject:
            r"""
            Calls ``super().derivation_module(...)``, then refines the result
            into ``Modules(self)``.
            """
            ...

        # @override Ring.localization
        @abstractmethod
        def localization(
            self, *extra_units: RingElement, **kwds
        ) -> LocalRingCategoryObject:
            r"""
            Calls ``super().localization(*extra_units)``, then refines the
            returned ring via
            ``result._refine_category_(ModuleBaseRings().Local())``.
            """
            ...

        # @override Ring.completion
        @abstractmethod
        def completion(
            self,
            place: RingElement,
            prec: Integer | None = None,
            extras: dict | None = None,
        ) -> CompleteRingCategoryObject:
            r"""
            Calls ``super().completion(place, prec)``, then refines the
            returned ring via
            ``result._refine_category_(ModuleBaseRings().Complete())``.
            """
            ...

        # @override Ring.fraction_field
        @abstractmethod
        def fraction_field(self) -> ModuleBaseRingsCategoryObject:
            r"""
            Calls ``super().fraction_field()``, then refines the returned
            field via ``result._refine_category_(ModuleBaseRings())``.
            The result also satisfies ``Fields()`` via the axiom system.
            """
            ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    class ElementMethods:

        @abstractmethod
        def parent(self) -> ModuleBaseRingsCategoryObject: ...

        @abstractmethod
        def principal_ideal(self) -> IdealSubmodulesCategoryObject:
            """Sugar for ``self.parent().ideal(self)``."""
            ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    class MorphismMethods: ...


# Type aliases: use XCategoryObject in annotations instead of X.ParentMethods.
ModuleBaseRingsCategoryObject = ModuleBaseRings.ParentMethods
ModuleBaseRingElement = ModuleBaseRings.ElementMethods
RingElement = ModuleBaseRingElement
SageRawRingElement = SageRingElement
ModuleBaseRingsMorphismObject = ModuleBaseRings.MorphismMethods
RingMorphism = ModuleBaseRingsMorphismObject
ModuleBaseIdealCategoryObject = ModuleBaseIdeals.ParentMethods
LocalRingCategoryObject = ModuleBaseRings.Local.ParentMethods
CompleteRingCategoryObject = ModuleBaseRings.Complete.ParentMethods


# --- Module-level category refinement ----------------------------------------
# Runs at import time.  Idempotent: checks ring.category() before refining.

def _refine_target_rings() -> None:
    from sage.rings.integer_ring import ZZ
    from sage.rings.rational_field import QQ
    from sage.rings.real_mpfr import RR
    from sage.rings.complex_mpfr import CC
    from sage.rings.qqbar import QQbar
    _cat = ModuleBaseRings()
    for ring in (ZZ, QQ, RR, CC, QQbar):
        if _cat not in ring.category().super_categories():
            ring._refine_category_(_cat)


_refine_target_rings()
