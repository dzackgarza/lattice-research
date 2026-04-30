r"""Homset, endset, and autset categories for algebras."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutsets, GenericEndsets, Homsets, HomsetsOf

if TYPE_CHECKING:
    from ..types import Algebra


class _AlgebraHomsetObjects:
    r"""Algebra-specific homset parent methods; generic homset methods are inherited."""


class _AlgebraHomomorphisms:
    @abstract_method
    def kernel(self) -> Algebra: ...


class AlgebraHomsets(HomsetsOf):
    r"""Category of algebra homsets."""

    @final
    def extra_super_categories(self):
        return [Homsets().Of(self.base_category())]

    ParentMethods = _AlgebraHomsetObjects
    ElementMethods = _AlgebraHomomorphisms
    class MorphismMethods: ...

    Endset = LazyImport(__name__, "_AlgebraEndsets")


class _AlgebraEndsets(GenericEndsets):
    _functor_category = "Endset"
    _base_category_class_and_axiom = (AlgebraHomsets, "Endset")
    Autset = LazyImport(__name__, "_AlgebraAutsets")

    class ParentMethods:
        @abstract_method
        def base_algebra(self) -> Algebra: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class _AlgebraAutsets(GenericAutsets):
    _functor_category = "Autset"
    _base_category_class_and_axiom = (_AlgebraEndsets, "Autset")

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
