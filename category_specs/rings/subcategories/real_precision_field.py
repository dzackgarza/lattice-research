r"""RealPrecisionFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method
from sage.rings.abc import RealBallField as SageRealBallField
from sage.rings.abc import RealDoubleField as SageRealDoubleField
from sage.rings.abc import RealField as SageRealField
from sage.rings.abc import RealIntervalField as SageRealIntervalField
from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from .. import Rings

from .approximate import ApproximateRingsCategory
from ._lazy_subcategories import (
    _CompleteRings,
    _Fields,
    _LocalFields,
)

if TYPE_CHECKING:
    from ...types import (
        Field,
    )


class _RealPrecisionFields(Category_singleton):
    r"""Common category for Sage real approximate fields with fixed precision.

    Constructor target: real floating, interval, ball, and double-field
    constructors refine through this precision-family category.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "real precision fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [ApproximateRingsCategory(), _Fields(), _CompleteRings(), _LocalFields(), Rings().Characteristic(0)]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(
            R,
            (
                SageRealField,
                SageRealDoubleField,
                SageRealIntervalField,
                SageRealBallField,
            ),
        )

    class ParentMethods:
        @abstract_method
        def precision(self) -> Integer: ...

        @override
        @final
        def change_precision(
            self, precision: Integer, precision_type: str | None = None
        ) -> Field:
            assert precision_type is None, (
                "Sage real precision-field change is source-backed for default "
                "precision type"
            )
            if isinstance(
                self, (SageRealField, SageRealDoubleField, SageRealIntervalField)
            ):
                return self.to_prec(precision)
            assert isinstance(self, SageRealBallField)
            return self.__class__(precision)

        @abstract_method
        def complex_field(self) -> Field: ...

    class ElementMethods: ...

    class MorphismMethods: ...
