r"""Zp ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, assert_never, final, override


from ...cat import Category, Category_singleton

from ._lazy_subcategories import (
    _CompleteDiscreteValuationRings,
    _LocalRings,
    _PAdicRings,
)

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Ideal,
    )


class _Zp(Category_singleton):
    r"""Category of p-adic integer rings (all primes p, all precision types).

    Constructor target: ``Rings().Constructors().Zp(...)`` and compatible
    p-adic integer-ring constructors refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "p-adic integer rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_PAdicRings(), _CompleteDiscreteValuationRings(), _LocalRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.rings.padics.generic_nodes import pAdicRingGeneric

        return isinstance(R, pAdicRingGeneric)

    class ParentMethods:
        @override
        @final
        def completion(self, I: Ideal) -> CompleteRing:
            match I:
                case _ if I.is_zero():
                    return self
                case _ if not I.is_zero():
                    return self
                case unreachable:
                    assert_never(unreachable)

    class ElementMethods: ...

    class MorphismMethods: ...
