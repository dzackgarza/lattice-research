r"""Homset, endset, and autset categories for posets."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutsets, GenericEndsets, Homsets, HomsetsOf

if TYPE_CHECKING:
    from ..types import Poset


class _PosetHomsetObjects:
    r"""Poset-specific homset parent methods; generic homset methods are inherited."""


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


class PosetHomsets(HomsetsOf):
    r"""Category of homsets whose elements are order-preserving maps."""

    @final
    def extra_super_categories(self) -> list:
        return [Homsets().Of(self.base_category())]

    ParentMethods = _PosetHomsetObjects
    ElementMethods = _OrderPreservingMaps
    class MorphismMethods: ...

    Endset = LazyImport(__name__, "_PosetEndsets")


class _PosetEndsets(GenericEndsets):
    _functor_category = "Endset"
    _base_category_class_and_axiom = (PosetHomsets, "Endset")
    Autset = LazyImport(__name__, "_PosetAutsets")

    class ParentMethods:
        @abstract_method
        def base_poset(self) -> Poset: ...

    ElementMethods = _PosetEndomorphisms
    class MorphismMethods: ...


class _PosetAutsets(GenericAutsets):
    _functor_category = "Autset"
    _base_category_class_and_axiom = (_PosetEndsets, "Autset")

    class ParentMethods: ...
    ElementMethods = _PosetAutomorphisms
    class MorphismMethods: ...
