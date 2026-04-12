from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.all import QQ, ZZ, Integer, QuadraticForm, block_diagonal_matrix, identity_matrix, matrix, vector, zero_matrix

from src.lattices.core.abstract import BilinearModule
from src.lattices.core.elements import FreeBilinearModuleElement
from src.lattices.validation.presentations import FreeModulePresentation

if TYPE_CHECKING:
    from src.lattices.morphisms.homspaces import RationalLatticeHomSpace


class FreeBilinearModule(BilinearModule):
    Element = FreeBilinearModuleElement

    def __init__(
        self,
        gram,
        *,
        generator_names: Sequence[str] = (),
    ):
        presentation = FreeModulePresentation(module_ring=ZZ, value_ring=QQ, gram=gram, generator_names=generator_names)
        self._gram = presentation.gram
        self._generator_names = presentation.generator_names
        self._ambient_parent = self
        self._inclusion_matrix = identity_matrix(QQ, self.rank())
        self._inclusion = None
        self._embeddings = ()

    def _set_embedded_data(self, ambient_parent: FreeBilinearModule, inclusion_matrix) -> None:
        self._ambient_parent = ambient_parent
        self._inclusion_matrix = matrix(QQ, inclusion_matrix)
        assert self._inclusion_matrix.ncols() == self.rank(), "Inclusion matrix has the wrong source rank"
        assert self._inclusion_matrix.nrows() == ambient_parent.rank(), "Inclusion matrix has the wrong ambient rank"
        self._inclusion = self.hom(ambient_parent).element_from_matrix(inclusion_matrix)

    @classmethod
    def _from_embedded_presentation(
        cls,
        gram,
        *,
        ambient_parent: FreeBilinearModule,
        inclusion_matrix,
        generator_names: Sequence[str] = (),
    ):
        wrapped = cls(gram, generator_names=generator_names)
        wrapped._set_embedded_data(ambient_parent, inclusion_matrix)
        return wrapped

    def gram_matrix(self):
        return self._gram

    def inner_product_matrix(self):
        return self.gram_matrix()

    def rank(self) -> int:
        return self.gram_matrix().nrows()

    def det(self):
        return self.gram_matrix().det()

    def determinant(self):
        return self.det()

    def signature_pair(self):
        positive, negative, _zero = QuadraticForm(QQ, self.gram_matrix()).signature_vector()
        return Integer(positive), Integer(negative)

    def signature(self):
        return self.signature_pair()

    def generator_names(self) -> tuple[str, ...]:
        return self._generator_names

    def _ambient_coordinates_of(self, coordinates):
        local = vector(QQ, coordinates)
        if self._ambient_parent is self:
            return local
        ambient_coordinates = self._inclusion_matrix * local.column()
        return self._ambient_parent._ambient_coordinates_of(vector(QQ, ambient_coordinates.column(0)))

    def gens(self):
        generators = []
        for index in range(self.rank()):
            coordinates = [QQ.zero()] * self.rank()
            coordinates[index] = QQ.one()
            generators.append(self.Element(self, coordinates))
        return tuple(generators)

    def element_from(self, coordinates):
        return self.Element(self, coordinates)

    def hom(self, codomain: FreeBilinearModule) -> RationalLatticeHomSpace:
        from src.lattices.morphisms.homspaces import RationalLatticeHomSpace

        return RationalLatticeHomSpace(self, codomain)

    def __contains__(self, value):
        return isinstance(value, FreeBilinearModuleElement) and value.parent() is self

    def _scalar_multiple(self, element, scalar):
        scaled = QQ(scalar) * element.to_vector()
        assert all(entry in ZZ for entry in scaled), f"{scalar} * {element!r} is not an element of {self!r}"
        return self.element_from(vector(ZZ, scaled))

    def span(self, elements: Sequence[FreeBilinearModuleElement]):
        generators = tuple(elements)
        if not generators:
            return _wrap_free_module(zero_matrix(QQ, 0, 0), ambient_parent=self, inclusion_matrix=matrix(QQ, self.rank(), 0, []))
        assert all(element.parent() is self for element in generators), "Spans are defined by generators from a single parent"
        rows = matrix(QQ, [element.to_vector() for element in generators])
        sub_gram = rows * self.gram_matrix() * rows.transpose()
        return _wrap_free_module(sub_gram, ambient_parent=self, inclusion_matrix=rows.transpose())

    def _submodule_from_generators(self, rows):
        generator_matrix = matrix(QQ, rows)
        sub_gram = generator_matrix * self.gram_matrix() * generator_matrix.transpose()
        return _wrap_free_module(sub_gram, ambient_parent=self, inclusion_matrix=generator_matrix.transpose())

    def __add__(self, other):
        direct_sum = _wrap_free_module(matrix(QQ, block_diagonal_matrix([self.gram_matrix(), other.gram_matrix()], subdivide=False)))
        left_matrix = matrix(ZZ, direct_sum.rank(), self.rank(), 0)
        right_matrix = matrix(ZZ, direct_sum.rank(), other.rank(), 0)
        for index in range(self.rank()):
            left_matrix[index, index] = 1
        for index in range(other.rank()):
            right_matrix[self.rank() + index, index] = 1
        left_embedding = self.hom(direct_sum).element_from_matrix(left_matrix)
        right_embedding = other.hom(direct_sum).element_from_matrix(right_matrix)
        direct_sum._embeddings = (left_embedding, right_embedding)
        return direct_sum

    def __pow__(self, exponent: int):
        exponent = int(exponent)
        assert exponent >= 1, "Direct-sum powers require a positive exponent"
        factors = exponent * [self]
        return sum(factors[1:], factors[0])

    def __eq__(self, other):
        if not isinstance(other, FreeBilinearModule):
            return False
        if type(self) is not type(other):
            return False
        return self.gram_matrix() == other.gram_matrix()

    def __repr__(self):
        return f"{type(self).__name__}(gram={self.gram_matrix()!r})"


def _wrap_free_module(
    gram,
    *,
    ambient_parent: FreeBilinearModule | None = None,
    inclusion_matrix=None,
):
    from src.lattices.core.integral import Lattice
    from src.lattices.core.rational import RationalLattice
    from src.lattices.validation.presentations import matrix_has_entries_in

    gram_matrix = matrix(QQ, gram)
    if ambient_parent is None:
        if gram_matrix.det() == 0:
            return FreeBilinearModule(gram_matrix)
        if matrix_has_entries_in(ZZ, gram_matrix):
            return Lattice.from_gram(matrix(ZZ, gram_matrix))
        return RationalLattice.from_gram(gram_matrix)
    if gram_matrix.det() == 0:
        wrapped = FreeBilinearModule._from_embedded_presentation(
            gram_matrix,
            ambient_parent=ambient_parent,
            inclusion_matrix=inclusion_matrix,
        )
    elif matrix_has_entries_in(ZZ, gram_matrix):
        wrapped = Lattice._from_embedded_presentation(
            matrix(ZZ, gram_matrix),
            ambient_parent=ambient_parent,
            inclusion_matrix=inclusion_matrix,
        )
    else:
        wrapped = RationalLattice._from_embedded_presentation(
            gram_matrix,
            ambient_parent=ambient_parent,
            inclusion_matrix=inclusion_matrix,
        )
    return wrapped
