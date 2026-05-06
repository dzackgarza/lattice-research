r"""Qp ring subcategory spec."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from ...cat import Category, Category_singleton

from ._lazy_subcategories import (
    _CompleteDiscreteValuationFields,
    _LocalFields,
    _PAdicRings,
)

if TYPE_CHECKING:
    from ...types import (
        Field,
        RingElement,
    )


class _Qp(Category_singleton):
    r"""Category of p-adic fields (all primes p, all precision types).

    Constructor target: ``Rings().Constructors().Qp(...)`` and compatible
    p-adic field constructors refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "p-adic fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_PAdicRings(), _CompleteDiscreteValuationFields(), _LocalFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.rings.padics.generic_nodes import pAdicFieldGeneric

        return isinstance(R, pAdicFieldGeneric)

    class ParentMethods:
        @abstract_method
        def composite(self, subfield1: Field, subfield2: Field) -> Field: ...

        @abstract_method
        def subfield(self, generators: Sequence[RingElement]) -> Field: ...

        @abstract_method
        def subfields_of_degree(self, n: Integer) -> Integer: ...

        @abstract_method
        def exact_field(self) -> Field: ...

    class ElementMethods: ...

    class MorphismMethods: ...
