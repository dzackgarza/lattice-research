r"""One-object subcategories for images of sets under maps."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, Set, SetElement, SympySet


from ...cat import Category
from .. import Sets


class _ImageSets(Category_singleton):
    r"""Image subobjects ``{f(x) | x in X}`` under a set map.

    Constructor target:
    ``Sets().Constructors().ImageSubobject(f, domain_subset)`` refines here as
    a constructive set subobject/subquotient.  The ambient set is the codomain
    of ``f``; ``lift`` and ``retract`` express the Sage-backed subquotient
    representation of the image inside that ambient.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Subobjects(), Sets().Subquotients()]

    class ParentMethods:
        @abstract_method
        def __eq__(self, other: Set) -> bool: ...

        @abstract_method
        def __ne__(self, other: Set) -> bool: ...

        @abstract_method
        def __hash__(self) -> Integer: ...

        @override
        @abstract_method
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @override
        @abstract_method
        def ambient(self) -> Set:
            r"""Return the codomain ambient set containing this image."""
            ...

        @override
        @abstract_method
        def lift(self, x: SetElement) -> SetElement:
            r"""Lift an image element into ``ambient()``."""
            ...

        @override
        @abstract_method
        def retract(self, x: SetElement) -> SetElement:
            r"""Retract an ambient element to this image when defined."""
            ...

        @override
        @abstract_method
        def cardinality(self) -> Cardinality: ...

        @override
        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstract_method
        def _an_element_(self) -> SetElement: ...

        @override
        @abstract_method
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...

    class MorphismMethods: ...
