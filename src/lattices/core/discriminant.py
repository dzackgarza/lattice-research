from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Self

from sage.all import QQ, ZZ, Integer, matrix, vector
from sage.structure.sequence import Sequence as SageSequence

from src.lattices.core.abstract import QuadraticModule
from src.lattices.core.elements import RationalLatticeElement
from src.lattices.core.torsion import TorsionBilinearModule
from src.lattices.validation.presentations import DiscriminantPresentation, PrimePresentation, canonical_modulo

if TYPE_CHECKING:
    from src.lattices.core.integral import Lattice


class DiscriminantGroupElement:
    def __init__(self, parent: DiscriminantGroup, sage_element):
        self._parent = parent
        self._sage_element = sage_element

    def parent(self):
        return self._parent

    def _sage_like(self):
        return self._sage_element

    def vector(self):
        return self._sage_element.vector()

    def lift(self):
        dual_lattice = self.parent().dual_lattice()
        if dual_lattice is None:
            return self._sage_element.lift()
        return dual_lattice.element_from_dual_coordinates(self.vector())

    def q(self):
        return self.parent().q(self)

    def b(self, other):
        return self.parent().b(self, other)

    def is_isotropic(self):
        return self.q() == 0

    def additive_order(self):
        return self._sage_element.additive_order()

    def __eq__(self, other):
        return isinstance(other, DiscriminantGroupElement) and self.parent() is other.parent() and self.vector() == other.vector()

    def __hash__(self):
        return hash((id(self.parent()), tuple(int(entry) for entry in self.vector())))

    def __repr__(self):
        return repr(self._sage_element)


class DiscriminantGroup(TorsionBilinearModule, QuadraticModule):
    Element = DiscriminantGroupElement

    def __init__(self, sage_group, *, lattice: Lattice | None = None):
        self._sage_group = sage_group
        self._lattice = lattice

    @classmethod
    def _from_sage_like(cls, group, *, lattice: Lattice | None = None) -> Self:
        return cls(group, lattice=lattice)

    @classmethod
    def from_invariants_and_gram(
        cls,
        invariants: Sequence[int],
        gram,
        *,
        modulus: int = 1,
        quadratic_modulus: int = 2,
    ) -> Self:
        from sage.modules.torsion_quadratic_module import FreeQuadraticModule

        presentation = DiscriminantPresentation(
            invariants=invariants,
            gram=gram,
            modulus=modulus,
            quadratic_modulus=quadratic_modulus,
        )
        invariant_factors = presentation.invariants
        gram_matrix = presentation.gram
        ambient_gram = matrix(
            ZZ,
            [
                [Integer(invariant_factors[i] * invariant_factors[j] * gram_matrix[i, j]) for j in range(len(invariant_factors))]
                for i in range(len(invariant_factors))
            ],
        )
        ambient = FreeQuadraticModule(ZZ, len(invariant_factors), inner_product_matrix=ambient_gram)
        if not invariant_factors:
            zero_submodule = ambient.zero_submodule()
            sage_group = type(ambient.discriminant_group())(zero_submodule, zero_submodule, (), Integer(modulus), Integer(quadratic_modulus))
            return cls._from_sage_like(sage_group)
        generator_vectors = []
        integral_basis = []
        for index, invariant in enumerate(invariant_factors):
            generator_coordinates = [QQ.zero()] * len(invariant_factors)
            generator_coordinates[index] = QQ.one() / invariant
            generator_vectors.append(vector(QQ, generator_coordinates))
            basis_coordinates = [QQ.zero()] * len(invariant_factors)
            basis_coordinates[index] = QQ.one()
            integral_basis.append(vector(QQ, basis_coordinates))
        sage_group = type(ambient.discriminant_group())(
            ambient.span(tuple(generator_vectors)),
            ambient.span(tuple(integral_basis)),
            tuple(generator_vectors),
            Integer(modulus),
            Integer(quadratic_modulus),
        )
        return cls._from_sage_like(sage_group)

    @classmethod
    def from_lattice(cls, lattice: Lattice) -> Self:
        return lattice.discriminant_group()

    def _sage_like(self):
        return self._sage_group

    def lattice(self):
        return self._lattice

    def dual_lattice(self):
        return None if self._lattice is None else self._lattice.dual()

    def invariants(self):
        return tuple(Integer(entry) for entry in self._sage_group.invariants())

    def element_from(self, coordinates):
        return self(coordinates)

    def __call__(self, value):
        if isinstance(value, DiscriminantGroupElement):
            assert value.parent() is self, "Discriminant-group elements belong to a fixed parent"
            return value
        if isinstance(value, RationalLatticeElement):
            return self.Element(self, self._sage_group(value._ambient_vector()))
        return self.Element(self, self._sage_group(vector(QQ, value)))

    def zero(self):
        return self(self._sage_group.zero())

    def gens(self):
        return tuple(self.Element(self, generator) for generator in self._sage_group.gens())

    def smith_form_gens(self):
        return tuple(self.Element(self, generator) for generator in self._sage_group.smith_form_gens())

    def __iter__(self):
        for element in self._sage_group:
            yield self.Element(self, element)

    def cardinality(self):
        return Integer(self._sage_group.cardinality())

    def q(self, value):
        return canonical_modulo(self(value)._sage_like().quadratic_product(), 2)

    def b(self, left, right):
        return canonical_modulo(self(left)._sage_like().inner_product(self(right)._sage_like()), 1)

    def is_p_elementary(self, p):
        prime = PrimePresentation(prime=p).prime
        return all(invariant == prime for invariant in self.invariants())

    def isomorphic_as_groups(self, other):
        right = other if isinstance(other, DiscriminantGroup) else DiscriminantGroup._from_sage_like(other)
        return self.invariants() == right.invariants()

    def is_isometric_to(self, other):
        right = other if isinstance(other, DiscriminantGroup) else DiscriminantGroup._from_sage_like(other)
        left_normal_form = self._sage_group.normal_form()
        right_normal_form = right._sage_group.normal_form()
        same_value_module = self._sage_group._modulus == right._sage_group._modulus and self._sage_group._modulus_qf == right._sage_group._modulus_qf
        return (
            same_value_module
            and left_normal_form.invariants() == right_normal_form.invariants()
            and left_normal_form.gram_matrix_quadratic() == right_normal_form.gram_matrix_quadratic()
        )

    def hom(self, codomain):
        from src.lattices.morphisms.discriminant import DiscriminantGroupHomSpace

        right = codomain if isinstance(codomain, DiscriminantGroup) else DiscriminantGroup._from_sage_like(codomain)
        return DiscriminantGroupHomSpace(self, right)

    def _hom_from_smith(self, images):
        from src.lattices.morphisms.discriminant import DiscriminantGroupMorphism

        image_tuple = tuple(images)
        codomain = self if not image_tuple else image_tuple[0].parent()
        sage_images = SageSequence([codomain(image)._sage_like() for image in image_tuple], universe=codomain._sage_like())
        return DiscriminantGroupMorphism(self, codomain, self._sage_group._hom_from_smith(sage_images))

    def submodule(self, generators):
        sage_generators = tuple(self(generator)._sage_like() for generator in generators)
        return type(self)._from_sage_like(self._sage_group.submodule(sage_generators), lattice=self._lattice)

    def orthogonal_submodule_to(self, subgroup):
        other = subgroup if isinstance(subgroup, DiscriminantGroup) else type(self)._from_sage_like(subgroup, lattice=self._lattice)
        return type(self)._from_sage_like(self._sage_group.orthogonal_submodule_to(other._sage_group), lattice=self._lattice)

    def __truediv__(self, subgroup):
        other = subgroup if isinstance(subgroup, DiscriminantGroup) else type(self)._from_sage_like(subgroup, lattice=self._lattice)
        return type(self)._from_sage_like(self._sage_group / other._sage_group, lattice=self._lattice)

    def orthogonal_group(self):
        from src.lattices.groups.orthogonal import DiscriminantOrthogonalGroup

        return DiscriminantOrthogonalGroup(self)

    def __eq__(self, other):
        return isinstance(other, DiscriminantGroup) and self.is_isometric_to(other)

    def __repr__(self):
        return repr(self._sage_group)


DiscriminantForm = DiscriminantGroup
