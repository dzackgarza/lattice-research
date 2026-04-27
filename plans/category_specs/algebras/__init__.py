"""Static algebra category surface for the category spec redesign.

Subcategory hierarchy::

    Algebras(R)

Concrete algebra subcategories are added under ``subcategories/`` once their Sage
surfaces have been inventoried.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

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


class _AlgebraElementMethods:
    r"""Methods on elements of algebras."""


class _AlgebraMorphismMethods:
    r"""Methods on algebra morphisms."""


class Algebras(Category_over_base_ring):
    r"""Category of algebras over a fixed base ring."""

    def __contains__(self, A: Any) -> bool:
        match A:
            case _ if isinstance(A, Category) and A.is_subcategory(self):
                return True
            case _ if A in SageAlgebras(self.base_ring()):
                return True
            case _:
                return False

    def _repr_object_names(self) -> str:
        return f"algebras over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Rings().RingsUnder(R),
            Modules(R).Constructors().RingObjectsAsModules(),
        ]

    ParentMethods = _AlgebraParentMethods
    ElementMethods = _AlgebraElementMethods
    MorphismMethods = _AlgebraMorphismMethods

    class Constructors:
        r"""Algebra constructors over a fixed base ring.

        Concrete constructor methods are admitted after the corresponding Sage
        surfaces are inventoried in ``docs/SAGE_INVENTORY.md``.
        """

        def __init__(self, category):
            self._category = category

        def category(self):
            return self._category

        def base_ring(self):
            return self.category().base_ring()

    _Constructors = Constructors

    @cached_method
    def Constructors(self):
        return self.__class__._Constructors(self)
