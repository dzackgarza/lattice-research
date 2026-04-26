"""Matrix-algebra and algebra-over-a-ring categories."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from ..modules import Modules
from .constructions import _Category_over_base_integer_pair

if TYPE_CHECKING:
    from ..types import Ring, RingElement


def Rings(*args, **kwds):
    from . import Rings as _Rings

    return _Rings(*args, **kwds)


class _AlgebrasOver(Category_over_base_ring):
    r"""Ring objects equipped with a structure map from a fixed base ring."""

    def _repr_object_names(self) -> str:
        return f"algebras over {self.base_ring()}"

    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Rings().RingsUnder(R),
            Modules(R).NamedModules().RingObjectsAsModules(),
        ]

    class ParentMethods:
        @abstract_method
        def base_ring(self) -> Ring: ...

        @abstract_method
        def change_ring(self, R: Ring) -> Ring: ...

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


class _MatrixAlgebras(_Category_over_base_integer_pair):
    r"""Category of rings of square matrices over a base ring.

    ``_MatrixAlgebras(R, n, n)`` is the category whose single object is
    ``MatrixSpace(R, n, n)``.
    """

    def __init__(self, base_ring: Ring, n: Integer, m: Integer):
        if Integer(n) != Integer(m):
            raise ValueError("matrix rings require square matrix spaces")
        super().__init__(base_ring, n, m)

    def _repr_object_names(self) -> str:
        return f"rings of {self._n} by {self._n} matrices over {self._base_ring}"

    def __contains__(self, R: object) -> bool:
        from sage.matrix.matrix_space import MatrixSpace

        return (
            isinstance(R, MatrixSpace)
            and R.base_ring() == self.base_ring()
            and Integer(R.nrows()) == self.nrows()
            and Integer(R.ncols()) == self.ncols()
        )

    def object(self) -> Ring:
        from sage.matrix.matrix_space import MatrixSpace

        return MatrixSpace(self.base_ring(), self.nrows(), self.ncols())

    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        cats: list[Category] = [
            _AlgebrasOver(R),
            Modules(R).Free().FiniteRank(),
        ]
        if self._n == 1:
            from .specialized import _CommutativeRings

            if R in _CommutativeRings():
                cats.append(_CommutativeRings())
        return cats

    class ParentMethods:
        @abstract_method
        def nrows(self) -> Integer: ...

        @abstract_method
        def ncols(self) -> Integer: ...

        @abstract_method
        def dims(self) -> tuple[Integer, Integer]: ...

        @abstract_method
        def matrix(self, *args, **kwds) -> RingElement: ...

        @abstract_method
        def rank(self) -> Integer: ...

        @abstract_method
        def echelon_form(self, *args, **kwds): ...

        @abstract_method
        def column_space(self): ...

        @abstract_method
        def row_space(self): ...

        @abstract_method
        def diagonal_matrix(self, entries: Any) -> RingElement: ...

        @abstract_method
        def identity_matrix(self) -> RingElement: ...

        @abstract_method
        def zero_matrix(self) -> RingElement: ...

        @abstract_method
        def matrix_space(self, nrows=None, ncols=None, sparse=False): ...

        @abstract_method
        def from_vector(
            self,
            vector: RingElement,
            order: Any = None,
            coerce: bool = True,
        ) -> RingElement: ...

        @abstract_method
        def is_dense(self) -> bool: ...

        @abstract_method
        def is_sparse(self) -> bool: ...
