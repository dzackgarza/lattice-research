r"""Hom, end, and aut categories for posets."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import Poset


class _PosetHomCategoryObjectMethods:
    r"""Poset-specific hom parent methods; generic hom methods are inherited."""


class _OrderPreservingMaps:
    @abstract_method
    def is_order_preserving(self) -> bool: ...

    @abstract_method
    def is_order_embedding(self) -> bool: ...


class _PosetEndomorphisms:
    r"""Endomorphisms of posets; generic endomorphism methods are inherited."""


class _PosetAutomorphisms:
    @final
    def is_order_automorphism(self) -> bool:
        return True


class PosetHomCategory(HomCategoryOf):
    r"""Category of homs whose elements are order-preserving maps."""

    @final
    def extra_super_categories(self) -> list:
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _PosetHomCategoryObjectMethods
    ElementMethods = _OrderPreservingMaps
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "PosetEndCategory")


class PosetEndCategory(GenericEndCategory):
    _base_category_class_and_axiom = (PosetHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "PosetAutCategory")

    class ParentMethods:
        @abstract_method
        def base_poset(self) -> Poset: ...

    ElementMethods = _PosetEndomorphisms
    class MorphismMethods: ...


class PosetAutCategory(GenericAutCategory):
    _base_category_class_and_axiom = (PosetEndCategory, "Autset")

    class ParentMethods: ...
    ElementMethods = _PosetAutomorphisms
    class MorphismMethods: ...
