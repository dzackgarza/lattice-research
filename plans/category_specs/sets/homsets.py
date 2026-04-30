r"""Set-specific homset, endset, and autset categories.

Generic Autset construction belongs in the repository-level homset layer. This file
only declares the set-theoretic method surfaces: functions, endomorphisms, and
automorphisms of sets.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutsets, GenericEndsets, Homsets, HomsetsOf

if TYPE_CHECKING:
    from ..types import (
        Set,
        SetAutset,
        SetElement,
        SetEndset,
        Subset,
    )


class _SetHomsetObjects:
    r"""Set-specific homset parent methods; generic homset methods are inherited."""


class _SetMorphisms:
    @abstract_method
    def pre_image(self, y: SetElement) -> Subset: ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    @final
    def is_bijective(self) -> bool:
        return self.is_injective() and self.is_surjective()

    @final
    def is_isomorphism(self) -> bool:
        return self.is_bijective()


class _SetEndomorphisms:
    r"""Set-specific endomorphism methods; generic endomorphism methods are inherited."""


class _SetAutomorphisms:
    r"""Set-specific automorphism methods; generic automorphism methods are inherited."""


class SetHomsets(HomsetsOf):
    r"""Category of homsets between sets."""

    # Category-level Sets.Hom() / Sets().Homsets() construction:
    # objects are set-map parents Hom_Sets(X, Y). Set-map predicates
    # such as is_injective, is_surjective, and is_bijective belong here
    # on ElementMethods, not on the generic category of all morphisms.

    @final
    def extra_super_categories(self) -> list:
        return [Homsets().Of(self.base_category())]

    class SubcategoryMethods:
        @cached_method
        @final
        def Endset(self) -> SetEndset:
            return self._with_axiom("Endset")

        @cached_method
        @final
        def Autset(self) -> SetAutset:
            return self.Endset().Autset()

    ParentMethods = _SetHomsetObjects
    ElementMethods = _SetMorphisms
    Endset = LazyImport(__name__, "_SetEndsets")


class _SetEndsets(GenericEndsets):
    # Category-level Sets.End() / Sets().Homsets().Endset() construction:
    # objects are endomap parents End_Sets(X), not individual endomorphisms.
    _functor_category = "Endset"
    _base_category_class_and_axiom = (SetHomsets, "Endset")
    Autset = LazyImport(__name__, "_SetAutsets")

    class ParentMethods:
        @abstract_method
        def base_set(self) -> Set: ...

    ElementMethods = _SetEndomorphisms


class _SetAutsets(GenericAutsets):
    # Category-level Sets.Aut() / Sets().Homsets().Autset() construction:
    # objects are automorphism parents Aut_Sets(X), with set-map specs
    # inherited from SetHomsets and automorphism specs from GenericAutsets.
    _functor_category = "Autset"
    _base_category_class_and_axiom = (_SetEndsets, "Autset")

    ElementMethods = _SetAutomorphisms
