r"""CC ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override


from ...cat import Category, Category_singleton

from ._lazy_subcategories import (
    _AlgebraicallyClosedFields,
    _CompleteRings,
    _ComplexFields,
    _Fields,
    _LocalFields,
)

if TYPE_CHECKING:
    pass


class _CC(Category_singleton):
    r"""Sage's precision-53 complex field.

    Constructor target: ``Rings().Constructors().CC()`` and
    ``Rings().Constructors().ComplexField(53)`` refine here when Sage returns
    the canonical ``CC`` object.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complex field with 53 bits of precision"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            _ComplexFields(),
            _Fields(),
            _CompleteRings(),
            _LocalFields(),
            _AlgebraicallyClosedFields(),
        ]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import CC

        return x is CC

    @final
    def object(self):
        from sage.all import CC

        return CC

    class ParentMethods: ...

    class ElementMethods: ...

    class MorphismMethods: ...
