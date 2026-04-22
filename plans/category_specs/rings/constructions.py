"""Reusable categorical constructions for the redesigned ring surface."""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category, CategoryWithParameters
from sage.categories.category_types import Category_over_base_ring
from sage.categories.covariant_functorial_construction import (
    CovariantConstructionCategory,
    RegressiveCovariantConstructionCategory,
)
from sage.categories.quotients import QuotientsCategory
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.subquotients import SubquotientsCategory
from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer


class _Category_over_base_integer(CategoryWithParameters):
    r"""Base class for categories indexed by an integer and a base category."""

    parameter_name = "integer"

    @staticmethod
    def __classcall_private__(cls, category, base_integer):
        return super().__classcall__(cls, category, Integer(base_integer))

    def __init__(self, category, base_integer):
        self._base_category = category
        self._base_integer = Integer(base_integer)
        Category.__init__(self)

    def base_category(self):
        return self._base_category

    def base_integer(self):
        return self._base_integer

    def super_categories(self) -> list[Any]:
        return [self.base_category()]

    def _make_named_class_key(self, name):
        return (self.base_category(), self.base_integer())


class _CharacteristicRings(_Category_over_base_integer):
    parameter_name = "characteristic"

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.characteristic() == self.characteristic()

    def characteristic(self):
        return self.base_integer()

    def _repr_object_names(self):
        return f"{self.base_category()._repr_object_names()} of characteristic {self.characteristic()}"

    class ParentMethods:
        @abstract_method
        def characteristic(self) -> Integer: ...


class _KrullDimension(_Category_over_base_integer):
    parameter_name = "Krull dimension"

    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.krull_dimension() == self.dimension()

    def dimension(self):
        return self.base_integer()

    def _repr_object_names(self):
        return f"{self.base_category()._repr_object_names()} of Krull dimension {self.dimension()}"

    class ParentMethods:
        @abstract_method
        def krull_dimension(self) -> Integer: ...


class _Subobjects(SubobjectsCategory):
    r"""Ring subobjects: subrings in the current ring category."""

    def _repr_object_names(self):
        return f"subobjects of {self.base_category()._repr_object_names()}"


class _Subquotients(SubquotientsCategory):
    r"""Ring subquotients in the current ring category."""

    def _repr_object_names(self):
        return f"subquotients of {self.base_category()._repr_object_names()}"


class _Quotients(QuotientsCategory):
    r"""Ring quotients in the current ring category."""

    def _repr_object_names(self):
        return f"quotients of {self.base_category()._repr_object_names()}"


class _RingsUnder(CovariantConstructionCategory, Category_over_base_ring):
    _functor_category = "RingsUnder"

    @classmethod
    def default_super_categories(cls, category, base):
        from . import Rings

        return Category.join(
            [
                category,
                Rings(),
                super().default_super_categories(category, base),
            ]
        )

    def _repr_object_names(self):
        return f"rings under {self.base_ring()}"

    class ParentMethods:
        def structure_ring(self):
            return self.base_ring()

        def structure_map(self, *args, **kwds):
            return self.coerce_map_from(self.structure_ring())

        def structure_domain(self):
            return self.structure_ring()

        def structure_codomain(self):
            return self


class _RingsOver(RegressiveCovariantConstructionCategory, Category_over_base_ring):
    _functor_category = "RingsOver"

    @classmethod
    def default_super_categories(cls, category, ambient):
        from . import Rings

        return Category.join(
            [
                Rings(),
                super().default_super_categories(category, ambient),
            ]
        )

    def _repr_object_names(self):
        return f"rings over {self.base_ring()}"

    class ParentMethods:
        def structure_ring(self):
            return self.base_ring()

        def structure_map(self, *args, **kwds):
            return self.structure_ring().coerce_map_from(self)

        def structure_domain(self):
            return self

        def structure_codomain(self):
            return self.structure_ring()


class _Category_over_base_integer_pair(CategoryWithParameters):
    r"""Base class for categories indexed by a base ring and two integers."""

    parameter_name = "integer_pair"

    @staticmethod
    def __classcall_private__(cls, base_ring, n: int, m: int | None = None):
        if m is None:
            m = n
        return super().__classcall__(cls, base_ring, Integer(n), Integer(m))

    def __init__(self, base_ring: Any, n: Integer, m: Integer):
        self._base_ring = base_ring
        self._n = Integer(n)
        self._m = Integer(m)
        Category.__init__(self)

    def base_ring(self) -> Any:
        return self._base_ring

    def nrows(self) -> Integer:
        return self._n

    def ncols(self) -> Integer:
        return self._m

    def _make_named_class_key(self, name: str):
        return (self._base_ring, self._n, self._m)

    def super_categories(self) -> list[Any]:
        from . import Rings

        return [Rings()]


class _MatrixAlgebras(_Category_over_base_integer_pair):
    r"""Category of rings of square matrices over a base ring.

    ``_MatrixAlgebras(R, n, n)`` is the category whose single object is
    ``MatrixSpace(R, n, n)``.
    """

    def __init__(self, base_ring: Any, n: Integer, m: Integer):
        if Integer(n) != Integer(m):
            raise ValueError("matrix rings require square matrix spaces")
        super().__init__(base_ring, n, m)

    def _repr_object_names(self) -> str:
        return f"rings of {self._n} by {self._n} matrices over {self._base_ring}"

    def __contains__(self, R: Any) -> bool:
        from sage.matrix.matrix_space import MatrixSpace

        return (
            isinstance(R, MatrixSpace)
            and R.base_ring() == self.base_ring()
            and Integer(R.nrows()) == self.nrows()
            and Integer(R.ncols()) == self.nrows()
        )

    def object(self):
        from sage.matrix.matrix_space import MatrixSpace

        return MatrixSpace(self.base_ring(), self.nrows(), self.ncols())

    def super_categories(self) -> list[Any]:
        from . import Rings

        cats: list[Any] = [Rings()]
        if self._n == 1:
            from .specialized import _CommutativeRings

            if self._base_ring in _CommutativeRings():
                cats.append(_CommutativeRings())
        return cats

    class ParentMethods:
        @abstract_method
        def base_ring(self): ...

        @abstract_method
        def nrows(self) -> Integer: ...

        @abstract_method
        def ncols(self) -> Integer: ...

        @abstract_method
        def dims(self) -> tuple[Integer, Integer]: ...

        @abstract_method
        def matrix(self, *args, **kwds): ...

        @abstract_method
        def rank(self) -> Integer: ...

        @abstract_method
        def echelon_form(self, *args, **kwds): ...

        @abstract_method
        def column_space(self): ...

        @abstract_method
        def row_space(self): ...

        @abstract_method
        def diagonal_matrix(self, *args, **kwds): ...

        @abstract_method
        def identity_matrix(self): ...

        @abstract_method
        def zero_matrix(self): ...

        @abstract_method
        def change_ring(self, R): ...

        @abstract_method
        def matrix_space(self, nrows=None, ncols=None, sparse=False): ...

        @abstract_method
        def basis(self): ...

        @abstract_method
        def dimension(self) -> Integer: ...

        @abstract_method
        def from_vector(self, v, *args, **kwds): ...

        @abstract_method
        def is_dense(self) -> bool: ...

        @abstract_method
        def is_sparse(self) -> bool: ...

        @abstract_method
        def intersection(self, other): ...

        @abstract_method
        def submodule(self, *args, **kwds): ...

        @abstract_method
        def annihilator(self, *args, **kwds): ...

    class SquareParentMethods:
        r"""Methods available only on square matrix rings (n == m)."""

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
