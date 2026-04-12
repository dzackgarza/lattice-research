from __future__ import annotations

from sage.all import QQ, ZZ, Integer, matrix, vector

from src.lattices.validation.presentations import right_kernel_basis


class RationalLatticeMorphism:
    def __init__(self, domain, codomain, matrix_data):
        self._domain = domain
        self._codomain = codomain
        self._matrix = matrix(QQ, matrix_data)
        assert self._matrix.nrows() == codomain.rank() and self._matrix.ncols() == domain.rank(), (
            "Morphism matrix has the wrong shape"
        )

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def to_matrix(self):
        return self._matrix

    def __call__(self, value):
        element = value if value in self._domain else self._domain.element_from(value)
        image_coordinates = self._matrix * element.to_vector().column()
        return self._codomain.element_from(vector(QQ, image_coordinates.column(0)))

    def images(self):
        return tuple(self(generator) for generator in self._domain.gens())

    def image(self):
        return self._codomain.span(self.images())

    def perp(self):
        image_rows = matrix(QQ, [image.to_vector() for image in self.images()])
        complement_rows = right_kernel_basis(image_rows * self._codomain.gram_matrix())
        return self._codomain._submodule_from_generators(complement_rows.rows())

    def orthogonal_complement_of_image(self):
        return self.perp()

    def __contains__(self, value):
        return value in self._codomain

    def cokernel(self):
        assert self._domain.rank() == self._codomain.rank(), (
            "Finite-index cokernels are currently defined only for same-rank morphisms"
        )
        assert self._domain.is_integral(), (
            "Finite-index cokernels currently require an integral domain lattice so the quotient lands in A_L"
        )
        dual = self._domain.dual()
        discriminant_group = self._domain.discriminant_group()
        codomain_dual_coordinates = self.to_matrix().transpose() * self._codomain.gram_matrix()
        generators = tuple(
            discriminant_group(
                dual.element_from_dual_coordinates(vector(QQ, list(codomain_dual_coordinates.column(index))))
            )
            for index in range(self._codomain.rank())
        )
        return discriminant_group.submodule(generators)


class LatticeMorphism(RationalLatticeMorphism):
    def __init__(self, domain, codomain, matrix_data):
        super().__init__(domain, codomain, matrix(ZZ, matrix_data))

    def to_matrix(self):
        return matrix(ZZ, self._matrix)

    def is_primitive(self):
        smith_form, _left, _right = self.to_matrix().smith_form()
        diagonal = [smith_form[index, index] for index in range(min(smith_form.nrows(), smith_form.ncols())) if smith_form[index, index] != 0]
        return all(Integer(entry) == 1 for entry in diagonal)

    def cokernel(self):
        if self.domain().rank() == self.codomain().rank():
            return super().cokernel()

        complement = self.perp()
        if self.is_primitive() and self.image().rank() + complement.rank() == self.codomain().rank():
            direct_sum = self.image() + complement
            if direct_sum.is_isometric_to(self.codomain()):
                return complement
        assert False, "Cokernel construction currently requires a finite-index inclusion or an orthogonal direct-sum splitting"
