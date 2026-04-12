from __future__ import annotations

from sage.all import QQ, IntegralLattice, matrix

from src.lattices.core.free import FreeBilinearModule
from src.lattices.core.elements import DualLatticeElement, RationalLatticeElement
from src.lattices.validation.presentations import RationalLatticePresentation
from src.lattices.validation.presentations import matrix_has_entries_in

_SAGE_LATTICE = type(IntegralLattice("U"))


class RationalLattice(FreeBilinearModule):
    Element = RationalLatticeElement

    def __init__(self, gram):
        presentation = RationalLatticePresentation(gram=gram)
        super().__init__(presentation.gram)

    @classmethod
    def from_gram(cls, gram):
        from src.lattices.core.integral import Lattice

        gram_matrix = matrix(QQ, gram)
        if matrix_has_entries_in(ZZ, gram_matrix) and gram_matrix.det() != 0:
            return Lattice.from_gram(matrix(ZZ, gram_matrix))
        return cls(gram_matrix)

    @classmethod
    def _from_embedded_presentation(
        cls,
        gram,
        *,
        ambient_parent: FreeBilinearModule,
        inclusion_matrix,
    ):
        from src.lattices.core.integral import Lattice

        gram_matrix = matrix(QQ, gram)
        if matrix_has_entries_in(ZZ, gram_matrix) and gram_matrix.det() != 0:
            return Lattice._from_embedded_presentation(
                matrix(ZZ, gram_matrix),
                ambient_parent=ambient_parent,
                inclusion_matrix=inclusion_matrix,
            )
        wrapped = cls(gram_matrix)
        wrapped._set_embedded_data(ambient_parent, inclusion_matrix)
        return wrapped

    @classmethod
    def _from_sage_like(cls, lattice):
        from src.lattices.core.integral import Lattice

        if isinstance(lattice, _SAGE_LATTICE):
            return Lattice._from_sage_like(lattice)
        return cls.from_gram(lattice.gram_matrix())

    def is_integral(self):
        return matrix_has_entries_in(ZZ, self.gram_matrix())

    def twist(self, scalar):
        return RationalLattice.from_gram(QQ(scalar) * self.gram_matrix())

    def rescale(self, scalar):
        return self.twist(scalar)

    def dual(self):
        return RationalLattice.from_gram(self.gram_matrix().inverse())

    def hom(self, codomain):
        from src.lattices.morphisms.homspaces import RationalLatticeHomSpace

        return RationalLatticeHomSpace(self, codomain)

    @classmethod
    def _neg_root_gram_qq(cls, cartan_type: str):
        from sage.all import RootSystem

        space = RootSystem(cartan_type).ambient_space()
        simple_roots = list(space.simple_roots())
        return -matrix(QQ, [[left.inner_product(right) for right in simple_roots] for left in simple_roots])

    @classmethod
    def F4(cls):
        return cls.from_gram(cls._neg_root_gram_qq("F4"))

    @classmethod
    def G2(cls):
        from src.lattices.core.integral import Lattice

        return cls.from_gram(Lattice._integral_root_gram("G2"))


class DualLattice(RationalLattice):
    Element = DualLatticeElement

    def __init__(self, source_lattice):
        self._source_lattice = source_lattice
        super().__init__(source_lattice.gram_matrix().inverse())
        self._set_embedded_data(source_lattice, source_lattice.gram_matrix().inverse())

    @classmethod
    def from_lattice(cls, lattice):
        return cls(lattice)

    def source_lattice(self):
        return self._source_lattice

    def dual(self):
        return self._source_lattice

    def element_from_dual_coordinates(self, coordinates):
        return self.element_from(coordinates)

    def project_to_discriminant(self, value):
        element = value if value in self else self.element_from(value)
        return self._source_lattice.discriminant_group()(element._ambient_vector())

    def discriminant_group(self):
        return self._source_lattice.discriminant_group()

    def __truediv__(self, other):
        assert other is self._source_lattice, "The canonical discriminant quotient is defined relative to the source lattice"
        return self.discriminant_group()
