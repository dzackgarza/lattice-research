r"""QQbar ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, final, overload, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _AlgebraicFields

if TYPE_CHECKING:
    from ...types import (
        ComplexInterval,
        Polynomial,
        RealInterval,
        RingElement,
    )


class _QQbar(Category_singleton):
    r"""Sage's algebraic closure of the rational field.

    Constructor target: ``Rings().Constructors().QQbar()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "algebraic field"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_AlgebraicFields()]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import QQbar

        return x is QQbar

    @final
    def object(self):
        from sage.all import QQbar

        return QQbar

    class ParentMethods:
        @override
        def polynomial_root(
            self,
            poly: Polynomial,
            interval: RealInterval | ComplexInterval,
            multiplicity: Integer = 1,
        ) -> RingElement: ...

    class ElementMethods:
        @overload
        def nth_root(self, n: Integer, all: Literal[False] = False) -> RingElement: ...

        @overload
        def nth_root(
            self, n: Integer, all: Literal[True] = True
        ) -> list[RingElement]: ...

        @overload
        def nth_root(
            self, n: Integer, all: bool = False
        ) -> RingElement | list[RingElement]: ...

        @override
        def nth_root(
            self, n: Integer, all: bool = False
        ) -> RingElement | list[RingElement]: ...

    class MorphismMethods: ...
