"""
Exact Sage-backed lattice nouns for the Coble project.
"""

from __future__ import annotations

import logging
from collections.abc import Sequence
from functools import reduce
from itertools import repeat
from typing import Self

from sage.all import QQ, ZZ, Integer, IntegralLattice, MatrixSpace, gcd, matrix
from sage.misc.cachefunc import cached_method
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.vector_integer_dense import Vector_integer_dense

from research.isometry_backend import ISOMETRY_BACKEND
from src.external.py_polyhedral import (
    indefinite_form_automorphism_group,
    indefinite_form_isotropic_k_plane,
    indefinite_form_isotropic_k_flag,
    indefinite_form_stabilizer_vector,
    indefinite_form_stabilizer_isotropic_line,
    indefinite_form_stabilizer_isotropic_plane_2d,
    indefinite_form_stabilizer_isotropic_flag,
)

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

    def orthogonal_group(self, gens=None) -> DiscriminantOrthogonalGroup:
        r"""Return O(A_L) as a :class:`DiscriminantOrthogonalGroup`.

        The returned object wraps Sage's ``FqfOrthogonalGroup`` and exposes
        generators as plain ZZ-matrices with LEFT action (G * v, treating
        discriminant group elements as column vectors).  Since A_L is finite,
        O(A_L) is finite and membership is always decidable via GAP.
        """
        if gens is not None:
            # Sage-internal call (e.g., _isom_fqf passes gens=() for normal form)
            return _DiscriminantGroupBase.orthogonal_group(self, gens)
        return DiscriminantOrthogonalGroup(self)


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

    def __add__(self, other: Self) -> Self:
        return type(self).from_sage(self.direct_sum(other))

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

    # ------------------------------------------------------------------
    # High-level computational methods (route to polyhedral_common binaries)
    # ------------------------------------------------------------------

    def _gram_rows(self):
        """Return the Gram matrix as a list of lists of Python ints."""
        return [[int(x) for x in row] for row in self.inner_product_matrix().rows()]

    def _vec_to_list(self, v):
        """Convert a LatticeElement / vector to a list of Python ints."""
        return [int(x) for x in v]

    def _matrices_from_raw(self, raw_matrices):
        """Convert raw output of binary (list of list-of-lists) to sage matrices."""
        n = self.rank()
        return [matrix(ZZ, n, n, [ZZ(x) for row in M for x in row])
                for M in raw_matrices]

    def orthogonal_group(self) -> LatticeOrthogonalGroup:
        r"""Return O(self) as a :class:`LatticeOrthogonalGroup`.

        Generators come from the ``INDEF_FORM_AutomorphismGroup`` binary.
        The returned group uses LEFT action: ``G * v`` (column-vector convention),
        opposite to Sage's default right action ``v * G``.
        Membership: ``G in O(L)`` iff ``G * Q * G^T == Q``.
        """
        gens = self._matrices_from_raw(
            indefinite_form_automorphism_group(self._gram_rows())
        )
        return LatticeOrthogonalGroup(self, gens)

    def stabilizer_of_vector(self, v) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(v) as a :class:`LatticeOrthogonalSubgroup`.

        v: a LatticeElement or integer vector (isotropic or non-isotropic).
        Generators satisfy G*Q*G^T = Q and G*v = v (left action on columns).
        """
        raw = indefinite_form_stabilizer_vector(
            self._gram_rows(), self._vec_to_list(v)
        )
        return LatticeOrthogonalSubgroup(self, self._matrices_from_raw(raw))

    def stabilizer_of_isotropic_line(self, v) -> LatticeOrthogonalSubgroup:
        r"""Return the setwise stabilizer of span(v) as a :class:`LatticeOrthogonalSubgroup`.

        v: a primitive isotropic LatticeElement.
        Generators satisfy G*Q*G^T = Q and map span(v) → span(v) setwise
        (some generators may send v → −v).
        """
        raw = indefinite_form_stabilizer_isotropic_line(
            self._gram_rows(), self._vec_to_list(v)
        )
        return LatticeOrthogonalSubgroup(self, self._matrices_from_raw(raw))

    def stabilizer_of_isotropic_plane(self, v, w) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(span(v,w)) as a :class:`LatticeOrthogonalSubgroup`.

        v, w: LatticeElements spanning a totally isotropic 2-plane.
        Generators satisfy G*Q*G^T = Q and map span(v,w) to itself setwise.
        """
        raw = indefinite_form_stabilizer_isotropic_plane_2d(
            self._gram_rows(),
            self._vec_to_list(v),
            self._vec_to_list(w),
        )
        return LatticeOrthogonalSubgroup(self, self._matrices_from_raw(raw))

    def stabilizer_of_isotropic_flag(self, ordered_basis) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(flag) as a :class:`LatticeOrthogonalSubgroup`.

        ordered_basis: ordered list of LatticeElements [v_1, ..., v_k] where
            the i-th prefix [v_1, ..., v_i] spans a totally isotropic i-plane.
            The ORDER matters: the stabiliser fixes the flag
            span(v_1) ⊂ span(v_1,v_2) ⊂ ... ⊂ span(v_1,...,v_k)
            not just the unordered subspaces.
        Returns generators satisfying G*Q*G^T = Q.
        """
        raw = indefinite_form_stabilizer_isotropic_flag(
            self._gram_rows(),
            [self._vec_to_list(v) for v in ordered_basis],
        )
        return LatticeOrthogonalSubgroup(self, self._matrices_from_raw(raw))

    def isotropic_line_orbits(self):
        r"""Return orbit representatives of primitive isotropic lines under O(self).

        Returns a list of LatticeElements, one per O(self)-orbit of primitive
        isotropic lines (1-dimensional totally isotropic subspaces).
        """
        raw = indefinite_form_isotropic_k_plane(self._gram_rows(), 1)
        # raw is a list of vectors (list of ints), one per orbit
        return [self(v) for v in raw]

    def isotropic_plane_orbits(self):
        r"""Return orbit representatives of totally isotropic planes under O(self).

        Returns a list of pairs (v, w) of LatticeElements spanning one
        representative totally isotropic 2-plane per O(self)-orbit.
        """
        raw = indefinite_form_isotropic_k_plane(self._gram_rows(), 2)
        # raw is a list of 2×n matrices (list of two row-vectors)
        return [(self(rows[0]), self(rows[1])) for rows in raw]

    def isotropic_flag_orbits(self, k):
        r"""Return orbit representatives of isotropic flags of depth k under O(self).

        k=1: orbits of isotropic lines (same as isotropic_line_orbits)
        k=2: orbits of flags line ⊂ plane
        Returns a list of lists of LatticeElements.
        """
        raw = indefinite_form_isotropic_k_flag(self._gram_rows(), k)
        return [[self(row) for row in rows] for rows in raw]


# ---------------------------------------------------------------------------
# Orthogonal group classes — LEFT action (G * v, column-vector convention)
# ---------------------------------------------------------------------------
# Sage's GroupOfIsometries / MatrixGroup uses a RIGHT action: the natural
# multiplication `g * v` in Sage is really v * g.matrix() because vectors
# are row vectors.  All four classes below instead expose a LEFT action:
#   G.act(v)  =  G * v   (matrix times column vector)
# which matches standard mathematical notation.
#
# Action convention diagram:
#   Sage default:   v_row  * G         = (G^T v_col)^T     [RIGHT]
#   Our convention: G      * v_col     = G v_col           [LEFT]


class LatticeOrthogonalGroup:
    r"""The orthogonal group O(L) of a lattice, with LEFT action G*v.

    Generators are plain ``matrix(ZZ, n, n)`` objects.  Membership is
    decided by the matrix equation::

        G in O(L)  iff  G * Q * G^T == Q

    where Q = L.inner_product_matrix().  No GAP call is needed for
    membership in the full O(L).

    Subgroups are obtained via :meth:`subgroup`; their membership test
    additionally delegates to GAP (feasible for definite L, where O(L) is
    finite; see :class:`LatticeOrthogonalSubgroup` for the limitation note).
    """

    def __init__(self, lattice: Lattice, generators: list):
        self._lattice = lattice
        self._Q = lattice.inner_product_matrix()
        self._generators = list(generators)

    @property
    def lattice(self) -> Lattice:
        return self._lattice

    def generators(self) -> list:
        """Return the generating ZZ-matrices of O(L)."""
        return list(self._generators)

    def __contains__(self, G) -> bool:
        r"""G in O(L)  iff  G * Q * G^T == Q."""
        try:
            return G * self._Q * G.transpose() == self._Q
        except Exception:
            return False

    def act(self, G, v):
        r"""Apply G to v from the left: return G * v (column-vector convention)."""
        from sage.all import vector as sage_vector
        return G * sage_vector(ZZ, v)

    def subgroup(self, generators) -> LatticeOrthogonalSubgroup:
        r"""Return the :class:`LatticeOrthogonalSubgroup` generated by *generators*.

        generators: iterable of ZZ-matrices each satisfying G*Q*G^T = Q.
        """
        return LatticeOrthogonalSubgroup(self._lattice, list(generators))

    def __repr__(self) -> str:
        return (
            f"LatticeOrthogonalGroup of rank-{self._lattice.rank()} lattice"
            f" ({len(self._generators)} generator(s))"
        )


class LatticeOrthogonalSubgroup:
    r"""A finitely-generated subgroup of O(L), with matrix-equation membership.

    Membership testing:

    1. Check ``G * Q * G^T == Q`` (necessary for ``G in O(L)``).
    2. Delegate to GAP via Sage's ``orthogonal_group().subgroup(...)``
       for subgroup membership.

    **Limitation**: step 2 requires Sage to construct O(L) as a finite GAP
    group, which is only possible for definite lattices.  For indefinite L,
    ``__contains__`` raises ``NotImplementedError``.  No general algorithm
    for membership in arbitrary finitely-generated subgroups of O(L) for
    indefinite L is currently available in Sage, GAP, or Julia's
    Indefinite.jl; this is a known open computational problem.
    """

    def __init__(self, lattice: Lattice, generators: list):
        self._lattice = lattice
        self._Q = lattice.inner_product_matrix()
        self._generators = list(generators)
        self._sage_subgroup = None  # built lazily

    def _require_sage_subgroup(self):
        if self._sage_subgroup is not None:
            return self._sage_subgroup
        try:
            sage_og = self._lattice._native_lattice().orthogonal_group()
            self._sage_subgroup = sage_og.subgroup(
                [sage_og(G) for G in self._generators]
            )
        except Exception as exc:
            raise NotImplementedError(
                "GAP-backed subgroup membership requires O(L) to be a finite "
                "group (definite L).  For indefinite lattices, membership in "
                "arbitrary subgroups of O(L) is not algorithmically decidable "
                "with currently available tools."
            ) from exc
        return self._sage_subgroup

    @property
    def lattice(self) -> Lattice:
        return self._lattice

    def generators(self) -> list:
        """Return the generating ZZ-matrices."""
        return list(self._generators)

    def __contains__(self, G) -> bool:
        r"""Test membership: first check G*Q*G^T == Q, then delegate to GAP."""
        try:
            if G * self._Q * G.transpose() != self._Q:
                return False
        except Exception:
            return False
        sg = self._require_sage_subgroup()
        return sg(G) in sg

    def act(self, G, v):
        r"""Apply G to v from the left: return G * v (column-vector convention)."""
        from sage.all import vector as sage_vector
        return G * sage_vector(ZZ, v)

    def __repr__(self) -> str:
        return (
            f"LatticeOrthogonalSubgroup of O(rank-{self._lattice.rank()} lattice)"
            f" ({len(self._generators)} generator(s))"
        )


class DiscriminantOrthogonalGroup:
    r"""The orthogonal group O(A_L) of a discriminant group, with LEFT action.

    Wraps Sage's ``FqfOrthogonalGroup``.  Since A_L is a finite group,
    O(A_L) is finite and membership is always decidable via GAP.

    Generators are plain ZZ-matrices (action on the free abelian ambient of
    the discriminant group); LEFT action convention G*v.
    """

    def __init__(self, disc: DiscriminantGroup):
        self._disc = disc
        # Delegate to the native TorsionQuadraticModule orthogonal_group()
        self._sage_group = _DiscriminantGroupBase.orthogonal_group(disc)

    @property
    def discriminant_group(self) -> DiscriminantGroup:
        return self._disc

    def generators(self) -> list:
        """Return generating ZZ-matrices."""
        return [g.matrix() for g in self._sage_group.gens()]

    def __contains__(self, G) -> bool:
        r"""Test G in O(A_L) via GAP (always decidable)."""
        try:
            return self._sage_group(G) in self._sage_group
        except Exception:
            return False

    def act(self, G, v):
        r"""Apply G to discriminant element v from the left: G * v."""
        from sage.all import vector as sage_vector
        vec = v.vector() if hasattr(v, "vector") else sage_vector(ZZ, v)
        return G * vec

    def subgroup(self, generators) -> DiscriminantOrthogonalSubgroup:
        r"""Return the :class:`DiscriminantOrthogonalSubgroup` generated by *generators*."""
        return DiscriminantOrthogonalSubgroup(self._disc, list(generators), self._sage_group)

    def __repr__(self) -> str:
        return f"DiscriminantOrthogonalGroup of {self._disc!r}"


class DiscriminantOrthogonalSubgroup:
    r"""A subgroup of O(A_L), with GAP-backed membership (always decidable).

    Since O(A_L) is finite (A_L is a finite group), membership in any
    subgroup is decidable via GAP.
    """

    def __init__(self, disc: DiscriminantGroup, generators: list, parent_sage_group):
        self._disc = disc
        self._generators = list(generators)
        self._sage_subgroup = parent_sage_group.subgroup(
            [parent_sage_group(G) for G in generators]
        )

    @property
    def discriminant_group(self) -> DiscriminantGroup:
        return self._disc

    def generators(self) -> list:
        return list(self._generators)

    def __contains__(self, G) -> bool:
        r"""Test G in subgroup via GAP (always decidable since O(A_L) is finite)."""
        try:
            return self._sage_subgroup(G) in self._sage_subgroup
        except Exception:
            return False

    def act(self, G, v):
        r"""Apply G to discriminant element v from the left: G * v."""
        from sage.all import vector as sage_vector
        vec = v.vector() if hasattr(v, "vector") else sage_vector(ZZ, v)
        return G * vec

    def __repr__(self) -> str:
        return (
            f"DiscriminantOrthogonalSubgroup of O({self._disc!r})"
            f" ({len(self._generators)} generator(s))"
        )

