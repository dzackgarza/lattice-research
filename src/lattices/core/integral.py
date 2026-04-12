from __future__ import annotations

import logging
import re

from sage.all import QQ, ZZ, Integer, IntegralLattice, QuadraticForm, identity_matrix, matrix, vector
from sage.misc.cachefunc import cached_method

from src.backends.external.py_polyhedral import (
    indefinite_form_automorphism_group,
    indefinite_form_isotropic_k_flag,
    indefinite_form_isotropic_k_plane,
)
from src.backends.isometry_backend import ISOMETRY_BACKEND
from src.lattices.core.elements import LatticeElement
from src.lattices.core.rational import DualLattice, RationalLattice
from src.lattices.groups.orthogonal import LatticeOrthogonalGroup
from src.lattices.validation.presentations import IntegralCoordinatePresentation, LatticePresentation, PrimePresentation
from src.lattices.validation.presentations import matrix_has_entries_in, right_kernel_basis

_LOGGER = logging.getLogger(__name__)
_NIKULIN_DOMAIN_WARNING = (
    "Computing Nikulin invariants outside the theorem-backed domain of even "
    "indefinite 2-elementary lattices. The triple (r, a, delta) still carries "
    "semantic information, while generic indefinite isometry is delegated to "
    "the Dutour-backed backend."
)
_A1_SCALE = Integer(IntegralLattice("A1").gram_matrix()[0, 0])


class Lattice(RationalLattice):
    Element = LatticeElement

    def __init__(self, gram):
        presentation = LatticePresentation(gram=gram)
        super().__init__(presentation.gram)
        self._sage_lattice = IntegralLattice(presentation.gram)

    @classmethod
    def from_gram(cls, gram):
        presentation = LatticePresentation(gram=gram)
        return cls(presentation.gram)

    @classmethod
    def _from_embedded_presentation(cls, gram, *, ambient_parent, inclusion_matrix):
        wrapped = cls(gram)
        wrapped._set_embedded_data(ambient_parent, inclusion_matrix)
        return wrapped

    @classmethod
    def _from_sage_like(cls, lattice):
        wrapped = cls(matrix(ZZ, lattice.gram_matrix()))
        wrapped._sage_lattice = lattice
        return wrapped

    def element_from(self, coordinates):
        presentation = IntegralCoordinatePresentation(rank=self.rank(), coordinates=coordinates)
        return self.Element(self, presentation.coordinates)

    def _sage_like(self):
        return self._sage_lattice

    def is_integral(self):
        return True

    def gram_matrix(self):
        return matrix(ZZ, self._gram)

    def inner_product_matrix(self):
        return self.gram_matrix()

    def _scalar_multiple(self, element, scalar):
        scalar = QQ(scalar)
        scaled_coordinates = scalar * element.to_vector()
        if all(entry in ZZ for entry in scaled_coordinates):
            return self.element_from(vector(ZZ, scaled_coordinates))
        dual_coordinates = scalar * self.gram_matrix() * element.to_vector().column()
        if all(entry in ZZ for entry in dual_coordinates.list()):
            return self.dual().element_from(vector(ZZ, dual_coordinates.column(0)))
        return self.as_rational_lattice().element_from(vector(QQ, scaled_coordinates))

    def as_rational_lattice(self):
        return RationalLattice.from_gram(self.gram_matrix())

    def dual(self):
        return DualLattice.from_lattice(self)

    def scale(self):
        return ZZ.ideal(self.gram_matrix().list()).gen()

    def is_even(self):
        return all(Integer(self.gram_matrix()[index, index]).is_even() for index in range(self.rank()))

    def _quadratic_form(self):
        return self._sage_lattice.quadratic_form()

    def genus(self):
        return self._sage_lattice.genus()

    def local_genus_symbol(self, p):
        prime = PrimePresentation(prime=p).prime
        return self._quadratic_form().local_genus_symbol(prime)

    def has_isomorphic_discriminant_group_to(self, other):
        right = other if isinstance(other, Lattice) else Lattice._from_sage_like(other)
        return self.discriminant_group().isomorphic_as_groups(right.discriminant_group())

    def has_isomorphic_discriminant_form_to(self, other):
        right = other if isinstance(other, Lattice) else Lattice._from_sage_like(other)
        return self.discriminant_group().is_isometric_to(right.discriminant_group())

    def is_rationally_isometric_to(self, other):
        right = other if isinstance(other, Lattice) else Lattice._from_sage_like(other)
        return QuadraticForm(QQ, self.gram_matrix()).is_rationally_isometric(QuadraticForm(QQ, right.gram_matrix()))

    def is_locally_isometric_to(self, other, p):
        right = other if isinstance(other, Lattice) else Lattice._from_sage_like(other)
        return self.local_genus_symbol(p) == right.local_genus_symbol(p)

    def is_in_same_genus_as(self, other):
        right = other if isinstance(other, Lattice) else Lattice._from_sage_like(other)
        return self.genus() == right.genus()

    def is_isometric_to(self, other):
        right = other if isinstance(other, Lattice) else Lattice._from_sage_like(other)
        return ISOMETRY_BACKEND.is_isometric(self, right)

    def nikulin_a(self):
        return Integer(sum(Integer(2).divides(invariant) for invariant in self.discriminant_group().invariants()))

    def coparity(self):
        discriminant_group = self.discriminant_group()
        has_integral_values = all(discriminant_group.q(element) in ZZ for element in discriminant_group)
        return ZZ.zero() if has_integral_values else ZZ.one()

    def delta(self):
        return self.coparity()

    def nikulin_invariants(self):
        positive_rank, negative_rank = self.signature_pair()
        discriminant_group = self.discriminant_group()
        invariants = (Integer(self.rank()), self.nikulin_a(), self.delta())
        outside_domain = (
            (not self.is_even()) or (not positive_rank) or (not negative_rank) or (not discriminant_group.is_p_elementary(2))
        )
        if outside_domain:
            _LOGGER.warning(_NIKULIN_DOMAIN_WARNING)
        return invariants

    @classmethod
    def Z(cls):
        return cls.from_gram([[1]])

    @classmethod
    def U(cls):
        return cls._from_sage_like(IntegralLattice("U"))

    @classmethod
    def _integral_root_gram(cls, cartan_type: str):
        gram = RationalLattice._neg_root_gram_qq(cartan_type)
        assert matrix_has_entries_in(ZZ, gram), f"{cartan_type} does not define an integral root lattice"
        return matrix(ZZ, gram)

    @classmethod
    def A(cls, n: int):
        return cls.from_gram(cls._integral_root_gram(f"A{int(n)}"))

    @classmethod
    def B(cls, n: int):
        return cls.from_gram(cls._integral_root_gram(f"B{int(n)}"))

    @classmethod
    def C(cls, n: int):
        return cls.from_gram(cls._integral_root_gram(f"C{int(n)}"))

    @classmethod
    def D(cls, n: int):
        return cls.from_gram(cls._integral_root_gram(f"D{int(n)}"))

    @classmethod
    def E(cls, n: int):
        return cls.from_gram(cls._integral_root_gram(f"E{int(n)}"))

    @classmethod
    def F4(cls):
        return RationalLattice.F4()

    @classmethod
    def G2(cls):
        return cls.from_gram(cls._integral_root_gram("G2"))

    @classmethod
    def coble_picard(cls):
        return cls.Z().twist(_A1_SCALE) + cls.Z().twist(-_A1_SCALE) ** 10

    @classmethod
    def coble_transcendental(cls):
        return cls.Z().twist(_A1_SCALE) + cls.U() + cls.E(8)

    @classmethod
    def k3(cls):
        return cls.II(3, 19)

    @classmethod
    def I(cls, p: int, q: int):
        pieces = [cls.Z()] * int(p) + [cls.Z().twist(-1)] * int(q)
        assert pieces, "I(p, q) requires positive rank"
        return sum(pieces[1:], pieces[0])

    @classmethod
    def II(cls, p: int, q: int):
        p = int(p)
        q = int(q)
        assert (p - q) % 8 == 0, "Even unimodular indefinite lattices require p - q ≡ 0 mod 8"
        pieces = [cls.U()] * min(p, q)
        difference = p - q
        if difference > 0:
            pieces.extend([cls.E(8)] * (difference // 8))
        elif difference < 0:
            pieces.extend([cls.E(8).twist(-1)] * ((-difference) // 8))
        assert pieces, "II(p, q) requires positive rank"
        return sum(pieces[1:], pieces[0])

    @classmethod
    def from_string(cls, text: str):
        dispatch = {
            "A": cls.A,
            "B": cls.B,
            "C": cls.C,
            "D": cls.D,
            "E": cls.E,
            "F": lambda _n: cls.F4(),
            "G": lambda _n: cls.G2(),
        }

        def parse_term(raw: str):
            raw = raw.strip()
            power_match = re.fullmatch(r"(.*?)(?:\^\{?(\d+)\}?)?", raw)
            assert power_match is not None, f"Cannot parse lattice token {raw!r}"
            base = power_match.group(1).strip()
            exponent = int(power_match.group(2) or "1")

            scalar_match = re.fullmatch(r"<(-?\d+)>", base)
            if scalar_match:
                lattice = cls.Z().twist(int(scalar_match.group(1)))
                return lattice**exponent if exponent > 1 else lattice

            hyperbolic_match = re.fullmatch(r"U(?:\((-?\d+)\))?", base)
            if hyperbolic_match:
                lattice = cls.U()
                if hyperbolic_match.group(1):
                    lattice = lattice.twist(int(hyperbolic_match.group(1)))
                return lattice**exponent if exponent > 1 else lattice

            even_match = re.fullmatch(r"II_\{(\d+),(\d+)\}", base)
            if even_match:
                lattice = cls.II(int(even_match.group(1)), int(even_match.group(2)))
                return lattice**exponent if exponent > 1 else lattice

            odd_match = re.fullmatch(r"I_\{(\d+),(\d+)\}", base)
            if odd_match:
                lattice = cls.I(int(odd_match.group(1)), int(odd_match.group(2)))
                return lattice**exponent if exponent > 1 else lattice

            family_match = re.fullmatch(r"([A-G])_(?:\{(\d+)\}|(\d))(?:\((-?\d+)\))?", base)
            if family_match:
                family = family_match.group(1)
                n = int(family_match.group(2) or family_match.group(3))
                lattice = dispatch[family](n)
                if family_match.group(4):
                    lattice = lattice.twist(int(family_match.group(4)))
                return lattice**exponent if exponent > 1 else lattice

            assert family_match is not None, f"Cannot parse lattice token {base!r}"

        terms = [parse_term(term) for term in re.split(r"\s*\+\s*", text.strip()) if term.strip()]
        assert terms, f"Empty lattice expression: {text!r}"
        return sum(terms[1:], terms[0])

    @cached_method
    def discriminant_group(self):
        from src.lattices.core.discriminant import DiscriminantGroup

        return DiscriminantGroup._from_sage_like(self._sage_lattice.discriminant_group(), lattice=self)

    def hom(self, codomain):
        from src.lattices.morphisms.homspaces import RationalLatticeHomSpace

        return RationalLatticeHomSpace(self, codomain)

    def _gram_rows(self):
        return [[int(entry) for entry in row] for row in self.gram_matrix().rows()]

    def _column_action_isometry_from_row_action_matrix(self, raw_matrix):
        candidate = matrix(ZZ, raw_matrix).transpose()
        assert candidate.transpose() * self.gram_matrix() * candidate == self.gram_matrix(), (
            "Matrix does not preserve the lattice form"
        )
        return candidate

    def _matrices_from_raw(self, raw_matrices):
        return [self._column_action_isometry_from_row_action_matrix(raw_matrix) for raw_matrix in raw_matrices]

    def _definite_orthogonal_group_generators(self):
        positive_rank, negative_rank = self.signature_pair()
        definite_gram = -self.gram_matrix() if positive_rank == 0 else self.gram_matrix()
        orthogonal_group = IntegralLattice(definite_gram).orthogonal_group()
        return [self._column_action_isometry_from_row_action_matrix(generator.matrix()) for generator in orthogonal_group.gens()]

    def orthogonal_group(self):
        positive_rank, negative_rank = self.signature_pair()
        gens_fn = self._definite_orthogonal_group_generators if (not positive_rank) or (not negative_rank) else lambda: self._matrices_from_raw(indefinite_form_automorphism_group(self._gram_rows()))
        return LatticeOrthogonalGroup.from_lattice(self, gens_fn)

    def stabilizer_of_vector(self, value):
        return self.orthogonal_group().stabilizer(value)

    def stabilizer_of_isotropic_line(self, value):
        return self.orthogonal_group().stabilizer_of_isotropic_line(value)

    def stabilizer_of_isotropic_plane(self, left, right):
        return self.orthogonal_group().stabilizer_of_isotropic_plane(left, right)

    def stabilizer_of_isotropic_flag(self, ordered_basis):
        return self.orthogonal_group().stabilizer_of_isotropic_flag(ordered_basis)

    def isotropic_line_orbits(self):
        return [self.element_from(row) for rows in indefinite_form_isotropic_k_plane(self._gram_rows(), 1) for row in rows]

    def isotropic_plane_orbits(self):
        return [(self.element_from(rows[0]), self.element_from(rows[1])) for rows in indefinite_form_isotropic_k_plane(self._gram_rows(), 2)]

    def isotropic_flag_orbits(self, depth: int):
        return [[self.element_from(row) for row in rows] for rows in indefinite_form_isotropic_k_flag(self._gram_rows(), depth)]

    def _eigenspace_sublattice(self, involution_matrix, eigenvalue: int):
        kernel_matrix = right_kernel_basis(matrix(ZZ, involution_matrix) - Integer(eigenvalue) * identity_matrix(ZZ, self.rank()))
        return self._submodule_from_generators(kernel_matrix.rows())

    def invariant_sublattice(self, involution_matrix):
        return self._eigenspace_sublattice(involution_matrix, 1)

    def coinvariant_sublattice(self, involution_matrix):
        return self._eigenspace_sublattice(involution_matrix, -1)

    def centralizer_of_involution(self, involution_matrix):
        involution = matrix(ZZ, involution_matrix)
        positive_rank, negative_rank = self.signature_pair()
        gens_fn = None
        if (not positive_rank) or (not negative_rank):
            gens_fn = lambda: self._centralizer_gens_via_gap(involution)
        return self.orthogonal_group().subgroup(
            gens_fn=gens_fn,
            predicate=lambda M, _involution=involution: M * _involution == _involution * M,
        )

    def _centralizer_gens_via_gap(self, involution_matrix):
        positive_rank, negative_rank = self.signature_pair()
        definite_gram = -self.gram_matrix() if positive_rank == 0 else self.gram_matrix()
        orthogonal_group = IntegralLattice(definite_gram).orthogonal_group()
        centralizer = orthogonal_group.gap().Centralizer(orthogonal_group(involution_matrix).gap())
        return [self._column_action_isometry_from_row_action_matrix(orthogonal_group(generator).matrix()) for generator in centralizer.GeneratorsOfGroup()]
