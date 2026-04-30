r"""Hom, end, and aut categories for algebras."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from ..types import Algebra


class _AlgebraHomCategoryObjectMethods:
    r"""Algebra-specific hom parent methods; generic hom methods are inherited."""


class _AlgebraHomomorphisms:
    @abstract_method
    def kernel(self) -> Algebra: ...


class AlgebraHomCategory(HomCategoryOf):
    r"""Category of algebra homs."""

    @final
    def extra_super_categories(self):
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _AlgebraHomCategoryObjectMethods
    ElementMethods = _AlgebraHomomorphisms
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "AlgebraEndCategory")


class AlgebraEndCategory(GenericEndCategory):
    _base_category_class_and_axiom = (AlgebraHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "AlgebraAutCategory")

    class ParentMethods:
        @abstract_method
        def base_algebra(self) -> Algebra: ...

    class ElementMethods: ...
    class MorphismMethods: ...


class AlgebraAutCategory(GenericAutCategory):
    _base_category_class_and_axiom = (AlgebraEndCategory, "Autset")

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
