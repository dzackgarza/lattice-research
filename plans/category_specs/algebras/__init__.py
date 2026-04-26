"""Static algebra category surface for the category spec redesign."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.misc.abstract_method import abstract_method

from ..modules import Modules

if TYPE_CHECKING:
    from ..types import Ring


def Rings(*args, **kwds):
    from ..rings import Rings as _Rings

    return _Rings(*args, **kwds)


class _AlgebraParentMethods:
    @abstract_method
    def base_ring(self) -> Ring: ...

    @abstract_method
    def change_ring(self, R: Ring): ...

    @abstract_method
    def center(self): ...

    @abstract_method
    def center_basis(self): ...

    @abstract_method
    def radical(self, *args, **kwds): ...

    @abstract_method
    def radical_basis(self, *args, **kwds): ...

    @abstract_method
    def subalgebra(self, *args, **kwds): ...

    @abstract_method
    def derivations_basis(self): ...

    @abstract_method
    def hochschild_complex(self, *args, **kwds): ...

    @abstract_method
    def has_standard_involution(self) -> bool: ...

    @abstract_method
    def idempotent_lift(self, *args, **kwds): ...

    @abstract_method
    def peirce_decomposition(self): ...

    @abstract_method
    def semisimple_quotient(self): ...


class Algebras(Category_over_base_ring):
    r"""Category of algebras over a fixed base ring."""

    def _repr_object_names(self) -> str:
        return f"algebras over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Rings().RingsUnder(R),
            Modules(R).NamedModules().RingObjectsAsModules(),
        ]

    ParentMethods = _AlgebraParentMethods
