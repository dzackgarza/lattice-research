"""Ring and ideal categories used by the module redesign.

The module surface refines a fixed collection of Sage ring parents into
``ModuleBaseRings``.  Ideals of those rings are still Sage ideals first:
``Ideal_generic.category()`` returns Sage's ``Ideals(R)`` hierarchy.  The
redesign adds ``ModuleBaseIdeals(R)`` as the ring-ideal refinement layer, and
``Modules(R).Ideals()`` supplies the module-subobject view.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_ideal
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.rings import Rings as SageRings
from sage.rings.integer import Integer

from .modules import Modules

if TYPE_CHECKING:
    from .types import (
        CompleteRing,
        FreeModule,
        Ideal,
        LocalRing,
        Ring,
        RingElement,
        RModule,
    )

Names = str | tuple[str, ...] | None


class ModuleBaseIdeals(Category_ideal):
    r"""
    Sage ideals of a refined module base ring.

    Objects are existing ``Ideal_generic`` / ``Ideal_pid`` instances whose
    categories have been refined into this category.
    
    This category represents ideals as submodules of the free rank-1 module
    ``R^1``. Its super-categories include ``Modules(R).Free().Subobjects()``.
    """

    def super_categories(self) -> list[Category]:
        from sage.categories.commutative_ring_ideals import CommutativeRingIdeals
        R = self.ring()
        return [
            CommutativeRingIdeals(R),
            Modules(R).Free().Subobjects(),
        ]

    @classmethod
    def from_ideal(cls, sage_ideal) -> Ideal:
        r"""
        Return the subobject corresponding to the given Sage ideal.
        """
        # Implementation will refine the sage_ideal into this category
        return sage_ideal

    def _repr_object_names(self) -> str:
        return "module-base ideals"

    def _latex_(self) -> str: ...

    class ParentMethods:
        @final
        def ideal(self):
            r"""Return the underlying Sage ideal."""
            return self

    class ElementMethods: ...
    class MorphismMethods: ...


class ModuleBaseRings(Category_singleton):
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
            def maximal_ideal(self) -> Ideal: ...

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
        def unit_ideal(self) -> Ideal: ...

        # @override CommutativeRings.nilradical
        @abstractmethod
        def nilradical(self) -> Ideal: ...

        # @override CommutativeRings.ideal
        @abstractmethod
        def ideal(self, generator: RingElement, **kwds) -> Ideal:
            r"""
            Calls ``super().ideal(generator)``, then refines the result into
            ``ModuleBaseIdeals(self)`` and ``Modules(self).Ideals()``.
            """
            ...

        # @override Ring.__mul__
        @abstractmethod
        def __mul__(self, generator: RingElement) -> Ideal:
            r"""Delegates to ``self.ideal(generator)``."""
            ...

        # @override Ring.__rmul__
        @abstractmethod
        def __rmul__(self, generator: RingElement) -> Ideal: ...

        # @override CommutativeRings.quotient
        @abstractmethod
        def quotient(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule:
            r"""
            Calls ``super().quotient(modulus)``, then refines the result into
            ``Modules(self)``.
            """
            ...

        # @override CommutativeRings.quo
        @abstractmethod
        def quo(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule: ...

        @final
        def quotient_ring(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule:
            return self.quotient(modulus, names=names, **kwds)

        @final
        def __truediv__(
            self,
            modulus: RingElement | Ideal,
        ) -> RModule:
            return self.quotient(modulus)

        # @override Ring.__pow__
        @abstractmethod
        def __pow__(self, n: Integer) -> FreeModule:
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
        ) -> RModule:
            r"""
            Calls ``super().derivation_module(...)``, then refines the result
            into ``Modules(self)``.
            """
            ...

        # @override Ring.localization
        @abstractmethod
        def localization(
            self, *extra_units: RingElement, **kwds
        ) -> LocalRing:
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
        ) -> CompleteRing:
            r"""
            Calls ``super().completion(place, prec)``, then refines the
            returned ring via
            ``result._refine_category_(ModuleBaseRings().Complete())``.
            """
            ...

        # @override Ring.fraction_field
        @abstractmethod
        def fraction_field(self) -> Ring:
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
        def parent(self) -> Ring: ...

        @abstractmethod
        def principal_ideal(self) -> Ideal:
            """Sugar for ``self.parent().ideal(self)``."""
            ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    class MorphismMethods: ...


from .modules import Modules # noqa


# --- Module-level category refinement ----------------------------------------
# Runs at import time.  Idempotent: checks ring.category() before refining.

def _refine_target_rings() -> None:
    from sage.rings.complex_mpfr import CC
    from sage.rings.integer_ring import ZZ
    from sage.rings.qqbar import QQbar
    from sage.rings.rational_field import QQ
    from sage.rings.real_mpfr import RR
    _cat = ModuleBaseRings()
    for ring in (ZZ, QQ, RR, CC, QQbar):
        if _cat not in ring.category().super_categories():
            ring._refine_category_(_cat)


_refine_target_rings()
