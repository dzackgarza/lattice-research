"""
Exact Sage-backed lattice nouns for the Coble project.
"""

from __future__ import annotations

import logging
from collections.abc import Sequence
from functools import reduce
from itertools import repeat
from typing import Self

from sage.all import QQ, ZZ, Integer, IntegralLattice, MatrixSpace, gcd
from sage.misc.cachefunc import cached_method
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.vector_integer_dense import Vector_integer_dense

from research.isometry_backend import ISOMETRY_BACKEND

_A1_POSITIVE = IntegralLattice("A1")
_A1_POSITIVE_VECTOR = next(iter(_A1_POSITIVE.basis()))
_A1_SCALE = _A1_POSITIVE_VECTOR.inner_product(_A1_POSITIVE_VECTOR)
_SAMPLE_LATTICE = IntegralLattice("U")
_SAMPLE_MODULE = _SAMPLE_LATTICE.ambient_module()
_SAMPLE_GROUP = _A1_POSITIVE.discriminant_group()

_FreeBilinearModuleBase = type(_SAMPLE_MODULE)
_LatticeBase = type(_SAMPLE_LATTICE)
_DiscriminantGroupBase = type(_SAMPLE_GROUP)
_DiscriminantGroupElementBase = type(next(iter(_SAMPLE_GROUP.gens())))
_LOGGER = logging.getLogger(__name__)
_NIKULIN_DOMAIN_WARNING = (
    "Computing Nikulin invariants outside the theorem-backed domain of even "
    "indefinite 2-elementary lattices. The triple (r, a, delta) still carries "
    "semantic information, while generic indefinite isometry is delegated to "
    "the Dutour-backed backend."
)


class FreeBilinearModuleElement(Vector_integer_dense):
    def is_isotropic(self):
        norm = self.inner_product(self)
        assert norm in ZZ
        return norm.is_zero()


class LatticeElement(FreeBilinearModuleElement):
    def divisibility(self):
        pairings = tuple(self * self.parent().inner_product_matrix())
        divisor = gcd(pairings).abs()
        assert divisor in ZZ
        return divisor

    def is_primitive(self):
        divisor = self.divisibility()
        assert divisor in ZZ
        return divisor.is_one()

    def discriminant_class(self):
        discriminant_group = self.parent().discriminant_group()
        discriminant_element = discriminant_group(self)
        assert discriminant_element.parent() is discriminant_group
        return discriminant_element


class LatticeMorphism(FreeModuleMorphism):
    def image_lattice(self):
        image = self.image()
        assert image.base_ring() is ZZ
        return Lattice.from_sage(image)

    def orthogonal_complement_of_image(self):
        codomain = self.codomain()
        assert codomain.base_ring() is ZZ
        return codomain.orthogonal_complement(self.image_lattice())


class DiscriminantGroupElement(_DiscriminantGroupElementBase):
    def is_isotropic(self):
        value = self.quadratic_product()
        assert self.parent().base_ring() is ZZ
        return value.is_zero()


class DiscriminantGroupMorphism(FGP_Morphism):
    def image_generators(self):
        images = tuple(self.im_gens())
        assert all(image.parent() is self.codomain() for image in images)
        return images

    def image_group(self):
        image = self.image()
        assert image.base_ring() is ZZ
        return image

    def is_identity(self):
        image_group = self.image_group()
        assert image_group.base_ring() is ZZ
        same_domain = self.domain() is self.codomain()
        same_image_size = image_group.cardinality() == self.domain().cardinality()
        return (
            same_domain
            and same_image_size
            and self.image_generators() == tuple(self.domain().gens())
        )

    def is_injective(self):
        image_group = self.image_group()
        assert image_group.base_ring() is ZZ
        return image_group.cardinality() == self.domain().cardinality()

    def is_surjective(self):
        image_group = self.image_group()
        assert image_group.base_ring() is ZZ
        return image_group.cardinality() == self.codomain().cardinality()


class FreeBilinearModule(_FreeBilinearModuleBase):
    Element = FreeBilinearModuleElement

    @classmethod
    def from_sage(cls, module: _FreeBilinearModuleBase) -> Self:
        converted = cls(
            module.base_ring(),
            module.rank(),
            module.inner_product_matrix(),
            sparse=module.is_sparse(),
        )
        assert converted.base_ring() is module.base_ring()
        return converted


class DiscriminantGroup(_DiscriminantGroupBase):
    Element = DiscriminantGroupElement

    @classmethod
    def from_sage(cls, group: _DiscriminantGroupBase) -> Self:
        generator_lifts = tuple(generator.lift() for generator in group.gens())
        converted = cls(
            group.V(),
            group.W(),
            generator_lifts,
            group._modulus,
            group._modulus_qf,
        )
        assert converted.base_ring() is group.base_ring()
        assert all(
            generator.additive_order() * generator.lift() in converted.W()
            for generator in converted.gens()
        )
        return converted

    @classmethod
    def from_lattice(cls, lattice: Lattice) -> Self:
        native_group = lattice._native_lattice().discriminant_group()
        converted = cls.from_sage(native_group)
        assert converted.base_ring() is native_group.base_ring()
        return converted

    def p_rank(self, p):
        """
        Return ``dim_{F_p}(A_L / pA_L)`` for the discriminant group ``A_L``.
        """
        prime = Integer(p)
        invariants = tuple(self.invariants())
        count = sum(prime.divides(invariant) for invariant in invariants)
        count_integer = Integer(count)
        assert count_integer in ZZ
        return count_integer

    def is_p_elementary(self, p):
        """
        Return whether ``A_L`` is an elementary abelian ``p``-group.

        This describes the finite abelian group ``A_L`` itself, not only the
        Nikulin ``2``-elementary branch. The trivial
        discriminant group is ``p``-elementary of rank ``0`` for every prime ``p``.
        """
        prime = Integer(p)
        invariants = tuple(self.invariants())
        assert prime.is_prime()
        return all(invariant == prime for invariant in invariants)

    def nikulin_a(self):
        """
        Return Nikulin's invariant ``a = dim_{F_2}(A_L / 2A_L)``.

        For even indefinite ``2``-elementary lattices, Nikulin's theorem uses
        this integer as the ``a`` in ``(r, a, delta)``. For other lattices it
        still records the ``2``-primary rank of ``A_L``.

        Sources:
        - ``theory/THEORY.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        two_primary_rank = self.p_rank(2)
        assert two_primary_rank in ZZ
        return two_primary_rank

    def coparity(self):
        """
        Return Nikulin's coparity ``delta`` for the discriminant quadratic form.

        By definition, ``delta = 0`` iff the discriminant form takes
        integral values on every class in ``A_L``; otherwise ``delta = 1``.
        The same discriminant-form computation is used both inside and outside
        the even indefinite ``2``-elementary theorem domain.

        Sources:
        - ``theory/THEORY.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        has_integral_discriminant_form = all(
            element.quadratic_product().lift() in ZZ for element in self
        )
        coparity = ZZ.zero() if has_integral_discriminant_form else ZZ.one()
        assert coparity.is_zero() or coparity.is_one()
        return coparity

    def delta(self):
        """
        Return the coparity invariant using Nikulin's ``delta`` notation.
        """
        delta_value = self.coparity()
        assert delta_value.is_zero() or delta_value.is_one()
        return delta_value

    def has_isomorphic_group_structure_to(self, other):
        """
        Return whether the underlying finite abelian groups are isomorphic.

        This compares the invariant factors of the discriminant groups, so it
        forgets the quadratic form and retains only the abstract group
        structure.
        """
        left_invariants = tuple(self.invariants())
        right_invariants = tuple(other.invariants())
        assert self.base_ring() is ZZ
        assert other.base_ring() is ZZ
        return left_invariants == right_invariants

    def has_isomorphic_quadratic_module_to(self, other):
        """
        Return whether the discriminant quadratic modules are isomorphic.

        Sage's torsion-quadratic-module normal form follows [MirMor2009,
        IV Definition 4.6]. Its contract states that two torsion quadratic
        modules are isomorphic if and only if they have the same value modules
        and the same normal form, so this method compares exactly those data.

        Sources:
        - Sage ``TorsionQuadraticModule.normal_form`` documentation
        - Miranda--Morrison, *The number of embeddings of integral quadratic
          forms. II* (2009), IV Definition 4.6
        """
        left_normal_form = self.normal_form()
        right_normal_form = other.normal_form()
        same_value_module = (
            self._modulus == other._modulus and self._modulus_qf == other._modulus_qf
        )
        same_invariant_factors = (
            left_normal_form.invariants() == right_normal_form.invariants()
        )
        same_canonical_quadratic_matrix = (
            left_normal_form.gram_matrix_quadratic()
            == right_normal_form.gram_matrix_quadratic()
        )
        assert self.base_ring() is ZZ
        assert other.base_ring() is ZZ
        return (
            same_value_module
            and same_invariant_factors
            and same_canonical_quadratic_matrix
        )

    def hom(self, codomain: Self, images: Sequence[DiscriminantGroupElement]):
        sage_hom = _DiscriminantGroupBase.hom(self, images, codomain)
        assert all(image.parent() is codomain for image in sage_hom.im_gens())
        return DiscriminantGroupMorphism(sage_hom.parent(), sage_hom)


class Lattice(_LatticeBase):
    Element = LatticeElement

    @classmethod
    def from_sage(cls, lattice: _LatticeBase) -> Self:
        converted = cls(
            lattice.ambient_module(),
            lattice.basis_matrix(),
            lattice.inner_product_matrix(),
        )
        assert converted.base_ring() is lattice.base_ring()
        return converted

    @cached_method
    def _native_lattice(self):
        native_lattice = _LatticeBase(
            self.ambient_module(),
            self.basis_matrix(),
            self.inner_product_matrix(),
        )
        assert native_lattice.base_ring() is self.base_ring()
        return native_lattice

    def _coerce_lattice(self, other):
        return other if type(other) is type(self) else type(self).from_sage(other)

    @cached_method
    def _quadratic_form(self):
        native_lattice = self._native_lattice()
        assert native_lattice.base_ring() is ZZ
        return native_lattice.quadratic_form()

    @cached_method
    def _rational_quadratic_form(self):
        return self._quadratic_form().change_ring(QQ)

    def has_isomorphic_discriminant_group_to(self, other):
        """
        Return whether the lattices have isomorphic discriminant groups.

        This is the abstract finite-abelian-group check on ``A_L``. It is a
        cheap necessary condition for integral isometry, but it ignores the
        discriminant quadratic form.
        """
        other_lattice = self._coerce_lattice(other)
        return self.discriminant_group().has_isomorphic_group_structure_to(
            other_lattice.discriminant_group()
        )

    def has_isomorphic_discriminant_form_to(self, other):
        """
        Return whether the discriminant quadratic modules are isomorphic.

        An integral lattice isometry induces an isomorphism of discriminant
        quadratic modules, so this is a stronger necessary condition than
        abstract discriminant-group isomorphism.
        """
        other_lattice = self._coerce_lattice(other)
        return self.discriminant_group().has_isomorphic_quadratic_module_to(
            other_lattice.discriminant_group()
        )

    def is_rationally_isometric_to(self, other):
        """
        Return whether the lattices become isometric over ``QQ``.

        This delegates to Sage's exact quadratic-form equivalence test over
        ``QQ`` after changing the associated integral quadratic forms from
        ``ZZ`` to ``QQ``.
        """
        other_lattice = self._coerce_lattice(other)
        return self._rational_quadratic_form().is_rationally_isometric(
            other_lattice._rational_quadratic_form()
        )

    @cached_method
    def genus(self):
        return self._native_lattice().genus()

    @cached_method
    def local_genus_symbol(self, p):
        """
        Return the local genus symbol at prime p.

        This uses Sage's implementation which follows Conway--Sloane (1999).
        For p ≠ 2: returns triples [valuation, rank, det] (Theorem 9).
        For p = 2: returns quintuples [valuation, rank, det, parity, oddity]
        including the oddity invariant needed for completeness (§7.3-7.6).
        """
        prime = Integer(p)
        assert prime.is_prime()
        return self._quadratic_form().local_genus_symbol(prime)

    def is_locally_isometric_to(self, other, p):
        """
        Return whether the lattices are isometric over ``ZZ_p``.

        The comparison is performed on Sage's exact local genus symbols at the
        prime ``p``.

        Mathematical foundation: For p ≠ 2, Conway--Sloane (1999), Theorem 9
        establishes that the local genus symbol (triple [valuation, rank, det])
        is a complete invariant. For p = 2, Sage uses quintuples
        [valuation, rank, det, parity, oddity] which include the additional
        oddity invariant needed for completeness (Conway--Sloane, §7.3-7.6).
        """
        other_lattice = self._coerce_lattice(other)
        prime = Integer(p)
        assert prime.is_prime()
        # Compare the actual genus symbol objects which handle canonicalization
        self_symbol = self.local_genus_symbol(prime)
        other_symbol = other_lattice.local_genus_symbol(prime)
        return self_symbol == other_symbol

    def is_in_same_genus_as(self, other):
        """
        Return whether the lattices lie in the same genus.

        Equivalently, they are isometric over ``R`` and over ``ZZ_p`` for every
        prime ``p``. This is the exact adelic precheck used before any full
        integral-isometry backend.

        Sources:
        - ``theory/THEORY.md``, discussion of genera and Nikulin's uniqueness
          theorem
        - Sage genus documentation for integral quadratic forms
        """
        other_lattice = self._coerce_lattice(other)
        return self.genus() == other_lattice.genus()

    def is_isometric_to(self, other):
        """
        Return the integral-lattice isometry predicate provided by this layer.

        Definite lattices defer to Sage. Even indefinite ``2``-elementary
        lattices use Nikulin's classification by signature and
        ``(r, a, delta)``. The remaining indefinite cases are delegated to the
        Dutour `Indefinite.jl` backend documented in
        ``theory/indefinite_isometry_backend.md``.

        Sources:
        - ``theory/THEORY.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        - Generic indefinite backend: ``theory/indefinite_isometry_backend.md``
        """
        right_lattice = self._coerce_lattice(other)
        assert right_lattice.base_ring() is ZZ
        return ISOMETRY_BACKEND.is_isometric(self, right_lattice)

    def nikulin_invariants(self):
        """
        Return Nikulin's triple ``(r, a, delta)`` for the lattice.

        A warning is logged when the lattice lies outside the even indefinite
        ``2``-elementary theorem domain.

        Sources:
        - ``theory/THEORY.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        positive_rank, negative_rank = self.signature_pair()
        discriminant_group = self.discriminant_group()
        invariants = (
            Integer(self.rank()),
            discriminant_group.nikulin_a(),
            discriminant_group.delta(),
        )
        outside_domain = (
            (not self.is_even())
            or (not positive_rank)
            or (not negative_rank)
            or (not discriminant_group.is_p_elementary(2))
        )
        if outside_domain:
            _LOGGER.warning(_NIKULIN_DOMAIN_WARNING)
        assert all(invariant in ZZ for invariant in invariants)
        return invariants

    @classmethod
    def rank_one(cls, scale) -> Self:
        native_lattice = IntegralLattice(MatrixSpace(ZZ, ZZ.one())([scale]))
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def hyperbolic_plane(cls) -> Self:
        native_lattice = IntegralLattice("U")
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def U(cls) -> Self:
        return cls.hyperbolic_plane()

    @classmethod
    def a1_negative(cls) -> Self:
        native_lattice = IntegralLattice(-_A1_POSITIVE.inner_product_matrix())
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def e8_negative(cls) -> Self:
        native_lattice = IntegralLattice(-IntegralLattice("E8").inner_product_matrix())
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def E8(cls) -> Self:
        return cls.e8_negative()

    def twist(self, n: int) -> Self:
        twisted = type(self).from_sage(IntegralLattice(n * self.inner_product_matrix()))
        return twisted

    @classmethod
    def coble_picard(cls) -> Self:
        positive_line = cls.rank_one(_A1_SCALE)
        negative_line = cls.rank_one(-_A1_SCALE)
        native_lattice = reduce(
            _LatticeBase.direct_sum,
            repeat(
                negative_line,
                int(IntegralLattice("E8").rank() + IntegralLattice("U").rank()),
            ),
            positive_line,
        )
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def coble_transcendental(cls) -> Self:
        native_lattice = _LatticeBase.direct_sum(
            _LatticeBase.direct_sum(
                cls.rank_one(_A1_SCALE),
                cls.hyperbolic_plane(),
            ),
            cls.e8_negative(),
        )
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def k3(cls) -> Self:
        native_lattice = reduce(
            _LatticeBase.direct_sum,
            (
                cls.hyperbolic_plane(),
                cls.hyperbolic_plane(),
                cls.e8_negative(),
                cls.e8_negative(),
            ),
            cls.hyperbolic_plane(),
        )
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @cached_method
    def discriminant_group(self, s=ZZ.zero()):
        native_group = self._native_lattice().discriminant_group(s)
        converted = DiscriminantGroup.from_sage(native_group)
        assert all(
            generator.additive_order() * generator.lift() in converted.W()
            for generator in converted.gens()
        )
        return converted

    def orthogonal_complement(self, sublattice: Self):
        native_complement = _LatticeBase.orthogonal_complement(self, sublattice)
        converted = type(self).from_sage(native_complement)
        assert converted.base_ring() is native_complement.base_ring()
        return converted

    def hom(self, codomain: Self, images: Sequence[LatticeElement]):
        morphism = LatticeMorphism(self.Hom(codomain), tuple(images))
        assert morphism.image().base_ring() is ZZ
        return morphism
