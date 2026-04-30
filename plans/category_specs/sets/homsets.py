r"""Set-specific hom, end, and aut categories.

Generic aut construction belongs in the repository-level hom layer. This file
only declares the set-theoretic method surfaces: functions, endomorphisms, and
automorphisms of sets.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import (
        Set,
        SetElement,
        Subset,
    )


class _SetHomCategoryObjectMethods:
    r"""Set-specific hom parent methods; generic hom methods are inherited."""


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


class SetHomCategory(HomCategoryOf):
    r"""Category of homs between sets."""

    # Category-level Sets().HomCategory() construction:
    # objects are set-map parents Hom_Sets(X, Y). Set-map predicates
    # such as is_injective, is_surjective, and is_bijective belong here
    # on ElementMethods, not on the generic category of all morphisms.

    @final
    def extra_super_categories(self) -> list:
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _SetHomCategoryObjectMethods
    ElementMethods = _SetMorphisms
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "SetEndCategory")


class SetEndCategory(GenericEndCategory):
    # Category-level Sets().EndCategory() construction:
    # objects are endomap parents End_Sets(X), not individual endomorphisms.
    _base_category_class_and_axiom = (SetHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "SetAutCategory")

    class ParentMethods:
        @abstract_method
        def base_set(self) -> Set: ...

    ElementMethods = _SetEndomorphisms
    class MorphismMethods: ...


class SetAutCategory(GenericAutCategory):
    # Category-level Sets().AutCategory() construction:
    # objects are automorphism parents Aut_Sets(X), with set-map specs
    # inherited from SetHomCategory and automorphism specs from GenericAutCategory.
    _base_category_class_and_axiom = (SetEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _SetAutomorphisms
    class MorphismMethods: ...
