r"""ComplexIntervalFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method
from sage.rings.abc import ComplexIntervalField as SageComplexIntervalField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _ComplexPrecisionFields,
    _ScientificNotationFields,
)

if TYPE_CHECKING:
    from ...types import (
        Field,
    )


class _ComplexIntervalFields(Category_singleton):
    r"""Category of Sage complex interval fields ``ComplexIntervalField(prec)``.

    Constructor target: ``Rings().Constructors().ComplexIntervalField(prec)``
    and the fixed ``CIF`` constructor refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complex interval fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields(), _ScientificNotationFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageComplexIntervalField)

    class ParentMethods:
        @abstract_method
        def real_field(self) -> Field: ...

        @abstract_method
        def middle_field(self) -> Field: ...

    class ElementMethods: ...

    class MorphismMethods: ...
