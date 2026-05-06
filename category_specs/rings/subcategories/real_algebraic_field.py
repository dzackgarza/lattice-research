r"""AA ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, final, overload, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton

from ._lazy_subcategories import _AlgebraicFields


if TYPE_CHECKING:
    from ...types import (
        Polynomial,
        RealInterval,
        RingElement,
    )


class _AA(Category_singleton):
    r"""Sage's field of real algebraic numbers.

    Constructor target: ``Rings().Constructors().AA()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "algebraic real field"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_AlgebraicFields()]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import AA

        return x is AA

    @final
    def object(self):
        from sage.all import AA

        return AA

    class ParentMethods:
        @override
        def polynomial_root(self, poly: Polynomial, interval: RealInterval, multiplicity: Integer = 1) -> RingElement: ...

    class ElementMethods:
        @overload
        def nth_root(self, n: Integer, all: Literal[False] = False) -> RingElement: ...

        @overload
        def nth_root(self, n: Integer, all: Literal[True] = True) -> list[RingElement]: ...

        @overload
        def nth_root(self, n: Integer, all: bool = False) -> RingElement | list[RingElement]: ...

        @override
        def nth_root(self, n: Integer, all: bool = False) -> RingElement | list[RingElement]: ...

    class MorphismMethods: ...
