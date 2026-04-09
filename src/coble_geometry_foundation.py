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
from sage.all import MatrixSpace as _MatrixSpace
from sage.misc.cachefunc import cached_method
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.sets.condition_set import ConditionSet as _ConditionSet

from research.isometry_backend import ISOMETRY_BACKEND
from src.external.py_polyhedral import (
    indefinite_form_automorphism_group,
    indefinite_form_isotropic_k_flag,
    indefinite_form_isotropic_k_plane,
    indefinite_form_stabilizer_isotropic_flag,
    indefinite_form_stabilizer_isotropic_line,
    indefinite_form_stabilizer_isotropic_plane_2d,
    indefinite_form_stabilizer_vector,
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


def _default_orbit_constraints():
    return {
        "determinant": None,
        "spinor": None,
        "discriminant_subgroup": None,
        "opaque": False,
    }


def _clone_orbit_constraints(constraints):
    return {
        "determinant": constraints["determinant"],
        "spinor": constraints["spinor"],
        "discriminant_subgroup": constraints["discriminant_subgroup"],
        "opaque": constraints["opaque"],
    }


def _merge_orbit_constraints(left, right):
    merged = _clone_orbit_constraints(left)
    for key in ("determinant", "spinor"):
        if right[key] is not None:
            if merged[key] is not None:
                assert merged[key] == right[key]
            merged[key] = right[key]
    if right["discriminant_subgroup"] is not None:
        if merged["discriminant_subgroup"] is None:
            merged["discriminant_subgroup"] = right["discriminant_subgroup"]
        elif merged["discriminant_subgroup"] is not right["discriminant_subgroup"]:
            merged["opaque"] = True
            merged["discriminant_subgroup"] = None
    merged["opaque"] = merged["opaque"] or right["opaque"]
    return merged


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

    def _column_action_isometry_from_row_action_matrix(self, raw_matrix):
        """Convert a row-action isometry matrix into the public column-action form."""
        raw = matrix(ZZ, raw_matrix)
        candidate = raw.transpose()
        gram = self.inner_product_matrix()
        assert candidate.transpose() * gram * candidate == gram
        return candidate

    def _matrices_from_raw(self, raw_matrices):
        """Convert row-action backend matrices into public column-action matrices."""
        return [
            self._column_action_isometry_from_row_action_matrix(raw_matrix)
            for raw_matrix in raw_matrices
        ]

    def orthogonal_group(self) -> LatticeOrthogonalGroup:
        r"""Return O(self) as a :class:`LatticeOrthogonalGroup`.

        Construction is cheap; generators are computed lazily on first call to
        ``gens()``.  Membership uses the column-action equation G^T*Q*G == Q.
        """
        gram_rows = self._gram_rows()
        return LatticeOrthogonalGroup.from_lattice(
            self,
            lambda: self._matrices_from_raw(
                indefinite_form_automorphism_group(gram_rows)
            ),
        )

    def stabilizer_of_vector(self, v) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(v) as a :class:`LatticeOrthogonalSubgroup`.

        v: a LatticeElement or integer vector (isotropic or non-isotropic).
        Membership: M in O(L) and M*v == v  (left action, column convention).
        """
        from sage.all import vector as sage_vector

        v_col = sage_vector(ZZ, self._vec_to_list(v))
        vlist = self._vec_to_list(v)
        gram_rows = self._gram_rows()
        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(
                indefinite_form_stabilizer_vector(gram_rows, vlist)
            ),
            predicate=lambda M, _v=v_col: M * _v == _v,
        )

    def stabilizer_of_isotropic_line(self, v) -> LatticeOrthogonalSubgroup:
        r"""Return setwise Stab_{O(self)}(span(v)) as a
        :class:`LatticeOrthogonalSubgroup`.

        v: a primitive isotropic LatticeElement.
        Membership: M in O(L) and M*v in span(v) over ZZ (allows M*v = ±v).
        """
        from sage.all import vector as sage_vector

        v_col = sage_vector(ZZ, self._vec_to_list(v))
        span_v = self.ambient_module().span([v_col])
        vlist = self._vec_to_list(v)
        gram_rows = self._gram_rows()
        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(
                indefinite_form_stabilizer_isotropic_line(gram_rows, vlist)
            ),
            predicate=lambda M, _s=span_v, _v=v_col: M * _v in _s,
        )

    def stabilizer_of_isotropic_plane(self, v, w) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(span(v,w)) as a :class:`LatticeOrthogonalSubgroup`.

        v, w: LatticeElements spanning a totally isotropic 2-plane.
        Membership: M in O(L) and M*v, M*w both in span(v,w) over ZZ.
        """
        from sage.all import vector as sage_vector

        v_col = sage_vector(ZZ, self._vec_to_list(v))
        w_col = sage_vector(ZZ, self._vec_to_list(w))
        plane = self.ambient_module().span([v_col, w_col])
        vlist, wlist = self._vec_to_list(v), self._vec_to_list(w)
        gram_rows = self._gram_rows()
        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(
                indefinite_form_stabilizer_isotropic_plane_2d(gram_rows, vlist, wlist)
            ),
            predicate=lambda M, _p=plane, _v=v_col, _w=w_col: (
                M * _v in _p and M * _w in _p
            ),
        )

    def stabilizer_of_isotropic_flag(self, ordered_basis) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(flag) as a :class:`LatticeOrthogonalSubgroup`.

        ordered_basis: ordered list of LatticeElements [v_1, ..., v_k].
            The ORDER is essential: the stabilizer fixes the nested flag
            span(v_1) ⊂ span(v_1,v_2) ⊂ ... ⊂ span(v_1,...,v_k).
        Membership: M in O(L) and M*v_j in span(v_1,...,v_j) for each j.
        """
        from sage.all import vector as sage_vector

        cols = [sage_vector(ZZ, self._vec_to_list(vi)) for vi in ordered_basis]
        strata = [self.ambient_module().span(cols[: i + 1]) for i in range(len(cols))]
        basis_lists = [self._vec_to_list(vi) for vi in ordered_basis]
        gram_rows = self._gram_rows()

        def _flag_predicate(M, _strata=strata, _cols=cols):
            return all(M * c in s for c, s in zip(_cols, _strata))

        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(
                indefinite_form_stabilizer_isotropic_flag(gram_rows, basis_lists)
            ),
            predicate=_flag_predicate,
        )

    def isotropic_line_orbits(self):
        r"""Return orbit representatives of primitive isotropic lines under O(self).

        Returns a list of LatticeElements, one per O(self)-orbit of primitive
        isotropic lines (1-dimensional totally isotropic subspaces).
        """
        raw = indefinite_form_isotropic_k_plane(self._gram_rows(), 1)
        return [self(rows[0]) for rows in raw]

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

    def _eigenspace_sublattice(self, iota_matrix, eigenvalue: int) -> Lattice:
        r"""Return the eigenspace sublattice for eigenvalue ±1 of *iota_matrix*.

        Returns {v ∈ L : iota*v = eigenvalue*v} as a :class:`Lattice`.
        The Gram matrix of the returned sublattice is the restriction of the
        inner product to the ZZ-kernel of (iota - eigenvalue*I).
        """
        from sage.all import identity_matrix

        n = self.rank()
        ev = ZZ(eigenvalue)
        A = matrix(ZZ, iota_matrix) - ev * identity_matrix(ZZ, n)
        ker = A.kernel()  # free ZZ-submodule of ZZ^n
        B = ker.basis_matrix()  # rows are ZZ basis vectors of the eigenspace
        if B.nrows() == 0:
            return Lattice.from_sage(IntegralLattice(matrix(ZZ, 0, 0, [])))
        Q = self.inner_product_matrix()
        gram = B * Q * B.transpose()
        return Lattice.from_sage(IntegralLattice(gram))

    def invariant_sublattice(self, iota_matrix) -> Lattice:
        r"""Return the (+1)-eigenspace sublattice L^ι = {v ∈ L : ι*v = v}.

        iota_matrix: a square ZZ-matrix representing an isometry of L.
        The sublattice is equipped with the inner product restricted from L.
        """
        return self._eigenspace_sublattice(iota_matrix, +1)

    def coinvariant_sublattice(self, iota_matrix) -> Lattice:
        r"""Return the (−1)-eigenspace sublattice L_ι = {v ∈ L : ι*v = −v}.

        iota_matrix: a square ZZ-matrix representing an isometry of L.
        The sublattice is equipped with the inner product restricted from L.
        """
        return self._eigenspace_sublattice(iota_matrix, -1)

    def centralizer_of_involution(self, iota_matrix) -> LatticeOrthogonalSubgroup:
        r"""Return Z_{O(L)}(ι) = {g ∈ O(L) : g*ι = ι*g} as a subgroup.

        iota_matrix: a square ZZ-matrix representing an isometry of L.

        Membership test: ``M in Z_{O(L)}(ι)``  iff  M ∈ O(L) and M*ι = ι*M.

        Generators:
          - Definite L: computed via GAP Centralizer (O(L) is finite).
          - Indefinite L: requires OSCAR's ``integer_lattice_with_isometry`` +
            ``image_centralizer_in_Oq``; call :func:`oscar_centralizer_gens`
            from ``computations/oscar_centralizer.py`` and pass the result
            directly as generators.

        Note: Z_{O(L)}(ι) ≠ O^0(L, ι) in general.  Sterk's Γ_En is obtained
        by further intersection::

            centralizer_of_involution(ι)
                .kernel_of_discriminant_action()
                & stabilizer_of_vector(h)
        """
        iota_mat = matrix(ZZ, iota_matrix)

        def _gens_fn():
            p, q = self.signature_pair()
            if q == 0 or p == 0:  # positive or negative definite
                return self._centralizer_gens_via_gap(iota_mat)
            assert False, (
                "Centralizer generators for indefinite lattices require OSCAR's "
                "image_centralizer_in_Oq data"
            )

        return self.orthogonal_group().subgroup(
            gens_fn=_gens_fn,
            predicate=lambda M, _ι=iota_mat: M * _ι == _ι * M,
        )

    def _centralizer_gens_via_gap(self, iota_mat) -> list:
        r"""Compute generators of Z_{O(L)}(ι) via GAP Centralizer (definite only).

        Converts ι to a GAP matrix group element, calls GAP's ``Centralizer``,
        then converts the resulting generators back to ZZ-matrices.
        """
        sage_L = IntegralLattice(self.inner_product_matrix())
        og = sage_L.orthogonal_group()
        iota_elt = og(iota_mat)
        centralizer_gap = og.gap().Centralizer(iota_elt.gap())
        result = []
        for g_gap in centralizer_gap.GeneratorsOfGroup():
            g_elt = og(g_gap)
            result.append(
                self._column_action_isometry_from_row_action_matrix(g_elt.matrix())
            )
        return result


# ---------------------------------------------------------------------------
# Orthogonal group classes — LEFT action (G * v, column-vector convention)
# ---------------------------------------------------------------------------
# Sage and the Dutour-Sikirić backends return lattice isometries in a row-action
# convention.  Lattice._matrices_from_raw converts those matrices into the
# standard column-action convention used below:
#   G.act(v)  =  G * v   (matrix times column vector)
# with defining equation G^T Q G = Q.
#
# Action convention diagram:
#   Row-action input:  v_row * R = (R^T v_col)^T
#   Public API:        G * v_col = G v_col
#                      where G = R^T for group generators/stabilizers
#
# Generators are computed lazily via a zero-arg callable supplied at
# construction.  Pass a lambda that calls the appropriate binary; the result
# is cached after the first call to gens().
#
# Membership is handled internally by a ConditionSet over the MatrixSpace.
# Subgroups intersect their parent's ConditionSet with a new predicate.
# & / | produce new subgroups by intersecting / unioning ConditionSets.


def _acts_trivially_on_discriminant(lattice: Lattice, M) -> bool:
    r"""Return True if M ∈ O(L) acts trivially on A_L = L*/L.

    The action of M on A_L = L*/L sends the coset x + L to M*x + L for x ∈ L*.
    M acts trivially iff M*x − x ∈ L for every basis vector x of L*.

    For an integer lattice with Gram matrix Q, the dual lattice L* has basis
    given by the rows of Q^{-1}.  We check all dual-basis vectors.
    """
    from sage.all import vector as sage_vector

    Q = lattice.inner_product_matrix()
    # Rows of Q^{-1} are a basis for L* in the ambient QQ^n
    Qinv = Q.inverse()  # QQ-matrix
    for x_row in Qinv.rows():
        x = sage_vector(QQ, x_row)
        diff = M * x - x
        # diff ∈ L = ZZ^n iff all coordinates are integers
        if not all(c in ZZ for c in diff):
            return False
    return True


class LatticeOrthogonalGroup:
    r"""The orthogonal group O(L) of a lattice, with LEFT action G*v.

    Construction is O(1).  Generators are computed lazily by :meth:`gens`.

    Membership:  ``G in O(L)``  iff  ``G^T * Q * G == Q``,
    implemented via an internal ``ConditionSet`` over ``MatrixSpace(ZZ, n)``.

    Subgroups are obtained via :meth:`subgroup`; they intersect this group's
    ``ConditionSet`` with an additional predicate.  Use ``&`` / ``|`` to
    intersect or union subgroups.
    """

    @classmethod
    def from_lattice(cls, lattice: Lattice, gens_fn) -> LatticeOrthogonalGroup:
        r"""Construct O(L) with a lazy generator callable.

        gens_fn: zero-arg callable returning a list of ZZ-matrices.
                 Called at most once; result cached on first :meth:`gens` call.
        """
        return cls(lattice, gens_fn)

    def __init__(self, lattice: Lattice, gens_fn):
        self._lattice = lattice
        self._Q = lattice.inner_product_matrix()
        self._gens_fn = gens_fn
        self._gens_cache = None
        self._orbit_constraints = _default_orbit_constraints()
        MS = _MatrixSpace(ZZ, lattice.rank())
        Q = self._Q
        self._condition_set = _ConditionSet(
            MS,
            lambda M: M.transpose() * Q * M == Q,
        )

    @property
    def lattice(self) -> Lattice:
        return self._lattice

    @property
    def condition_set(self):
        return self._condition_set

    def gens(self) -> list:
        """Return the generating ZZ-matrices of O(L), computing them if needed."""
        if self._gens_cache is None:
            self._gens_cache = self._gens_fn()
        return list(self._gens_cache)

    def __contains__(self, G) -> bool:
        r"""G in O(L)  iff  G^T * Q * G == Q."""
        return G in self._condition_set

    def act(self, G, v):
        r"""Apply G to v from the left: return G * v (column-vector convention)."""
        from sage.all import vector as sage_vector

        return G * sage_vector(ZZ, v)

    def subgroup(self, gens_fn, predicate) -> LatticeOrthogonalSubgroup:
        r"""Return a :class:`LatticeOrthogonalSubgroup` of O(L).

        gens_fn:   zero-arg callable returning the list of generator matrices.
        predicate: callable ``M -> bool`` encoding the geometric condition
                   (e.g. M*v == v for a vector stabilizer).
        """
        return LatticeOrthogonalSubgroup(self, gens_fn, predicate)

    def __and__(self, other) -> LatticeOrthogonalSubgroup:
        r"""Intersection: subgroup satisfying both membership conditions."""
        cs = self._condition_set & other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            other._orbit_constraints,
        )
        return subgroup

    def __or__(self, other) -> LatticeOrthogonalSubgroup:
        r"""Union: elements satisfying either membership condition."""
        cs = self._condition_set | other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _default_orbit_constraints()
        subgroup._orbit_constraints["opaque"] = True
        return subgroup

    def _structured_subgroup(
        self,
        predicate,
        *,
        constraints,
        gens_fn=None,
    ) -> LatticeOrthogonalSubgroup:
        subgroup = LatticeOrthogonalSubgroup(self, gens_fn, predicate)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            constraints,
        )
        return subgroup

    def special_orthogonal_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self._structured_subgroup(
            lambda M: ZZ(M.det()) == ZZ.one(),
            constraints={
                "determinant": 1,
                "spinor": None,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        from research.dawes_orbit_backend import real_spinor_norm_sign

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice: real_spinor_norm_sign(_lattice, M) == 1,
            constraints={
                "determinant": None,
                "spinor": 1,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def special_plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self.special_orthogonal_subgroup().plus_subgroup()

    def preimage_of_discriminant_subgroup(self, subgroup) -> LatticeOrthogonalSubgroup:
        from research.dawes_orbit_backend import induced_discriminant_action

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice, _subgroup=subgroup: (
                induced_discriminant_action(_lattice, M) in _subgroup
            ),
            constraints={
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": subgroup,
                "opaque": False,
            },
        )

    def find_vector_isometry(self, v1, v2):
        from research.dawes_orbit_backend import find_vector_isometry_in_group

        return find_vector_isometry_in_group(self, v1, v2)

    def vectors_are_equivalent(self, v1, v2) -> bool:
        from research.dawes_orbit_backend import vectors_are_equivalent_in_group

        return vectors_are_equivalent_in_group(self, v1, v2)

    def isotropic_line_orbits(self):
        from research.isotropic_gamma_orbit_backend import isotropic_line_orbits_in_group

        return isotropic_line_orbits_in_group(self)

    def isotropic_plane_orbits(self):
        from research.isotropic_gamma_orbit_backend import isotropic_plane_orbits_in_group

        return isotropic_plane_orbits_in_group(self)

    def isotropic_flag_orbits(self, k):
        from research.isotropic_gamma_orbit_backend import isotropic_flag_orbits_in_group

        return isotropic_flag_orbits_in_group(self, k)

    def isotropic_lines_are_equivalent(self, v1, v2) -> bool:
        from research.isotropic_gamma_orbit_backend import (
            isotropic_lines_are_equivalent_in_group,
        )

        return isotropic_lines_are_equivalent_in_group(self, v1, v2)

    def isotropic_planes_are_equivalent(self, basis1, basis2) -> bool:
        from research.isotropic_gamma_orbit_backend import (
            isotropic_planes_are_equivalent_in_group,
        )

        return isotropic_planes_are_equivalent_in_group(self, basis1, basis2)

    def kernel_of_discriminant_action(self) -> LatticeOrthogonalSubgroup:
        r"""Return the subgroup of O(L) acting trivially on A_L = L*/L.

        This is the kernel of π: O(L) → O(A_L).

        Membership: M ∈ O(L) and M*x ≡ x (mod L) for all x ∈ L*,
        i.e. M*x − x ∈ L for every dual-lattice generator x.

        Use this to refine centralisers toward Sterk's arithmetic groups::

            L.centralizer_of_involution(ι).kernel_of_discriminant_action()
        """
        lattice = self._lattice
        cs = _ConditionSet(
            _MatrixSpace(ZZ, lattice.rank()),
            lambda M: _acts_trivially_on_discriminant(lattice, M),
        )
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(
            lattice, self._condition_set & cs
        )
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            {
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": lattice.discriminant_group()
                .orthogonal_group()
                .subgroup([]),
                "opaque": False,
            },
        )
        return subgroup

    def __repr__(self) -> str:
        if self._gens_cache is not None:
            cached = f"{len(self._gens_cache)} gens"
        else:
            cached = "gens not yet computed"
        return f"LatticeOrthogonalGroup(rank={self._lattice.rank()}, {cached})"


class LatticeOrthogonalSubgroup:
    r"""A subgroup of O(L) defined by a ConditionSet.

    Membership:  ``M in subgroup``  iff  ``M`` is in the internal
    ``ConditionSet``, which is the intersection of:

      - the parent O(L) condition  ``M^T * Q * M == Q``, and
      - the geometric predicate supplied at construction.

    Examples of predicates:

    - Pointwise stabilizer of v:   ``lambda M: M * v == v``
    - Setwise stabilizer of line:  ``lambda M: M * v in span(v)``
    - Setwise stabilizer of plane: ``lambda M: M*v in P and M*w in P``
    - Flag stabilizer:             ``lambda M: all(M*v_j in stratum_j ...)``

    ``&`` / ``|`` produce new subgroups by intersecting / unioning ConditionSets.

    Generators are computed lazily via :meth:`gens`.
    """

    @classmethod
    def _from_condition_set(cls, lattice, condition_set):
        """Internal constructor from a pre-built ConditionSet (for & / |)."""
        obj = object.__new__(cls)
        obj._lattice = lattice
        obj._condition_set = condition_set
        obj._gens_fn = None
        obj._gens_cache = None
        obj._orbit_constraints = _default_orbit_constraints()
        return obj

    def __init__(
        self,
        ambient_group: LatticeOrthogonalGroup,
        gens_fn,
        predicate,
    ):
        self._lattice = ambient_group.lattice
        self._gens_fn = gens_fn
        self._gens_cache = None
        self._orbit_constraints = _clone_orbit_constraints(
            ambient_group._orbit_constraints
        )
        self._orbit_constraints["opaque"] = True
        self._condition_set = ambient_group.condition_set & _ConditionSet(
            _MatrixSpace(ZZ, self._lattice.rank()), predicate
        )

    @property
    def lattice(self) -> Lattice:
        return self._lattice

    @property
    def condition_set(self):
        return self._condition_set

    def gens(self) -> list:
        """Return the generating ZZ-matrices, computing them if needed."""
        if self._gens_cache is None:
            if self._gens_fn is None:
                assert False, (
                    "Generator computation requires an explicit generator function"
                )
            self._gens_cache = self._gens_fn()
        return list(self._gens_cache)

    def __contains__(self, M) -> bool:
        return M in self._condition_set

    def act(self, G, v):
        r"""Apply G to v from the left: return G * v (column-vector convention)."""
        from sage.all import vector as sage_vector

        return G * sage_vector(ZZ, v)

    def __and__(self, other) -> LatticeOrthogonalSubgroup:
        cs = self._condition_set & other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            other._orbit_constraints,
        )
        return subgroup

    def __or__(self, other) -> LatticeOrthogonalSubgroup:
        cs = self._condition_set | other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _default_orbit_constraints()
        subgroup._orbit_constraints["opaque"] = True
        return subgroup

    def _structured_subgroup(
        self,
        predicate,
        *,
        constraints,
        gens_fn=None,
    ) -> LatticeOrthogonalSubgroup:
        subgroup = LatticeOrthogonalSubgroup(self, gens_fn, predicate)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            constraints,
        )
        return subgroup

    def special_orthogonal_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self._structured_subgroup(
            lambda M: ZZ(M.det()) == ZZ.one(),
            constraints={
                "determinant": 1,
                "spinor": None,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        from research.dawes_orbit_backend import real_spinor_norm_sign

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice: real_spinor_norm_sign(_lattice, M) == 1,
            constraints={
                "determinant": None,
                "spinor": 1,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def special_plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self.special_orthogonal_subgroup().plus_subgroup()

    def preimage_of_discriminant_subgroup(self, subgroup) -> LatticeOrthogonalSubgroup:
        from research.dawes_orbit_backend import induced_discriminant_action

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice, _subgroup=subgroup: (
                induced_discriminant_action(_lattice, M) in _subgroup
            ),
            constraints={
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": subgroup,
                "opaque": False,
            },
        )

    def find_vector_isometry(self, v1, v2):
        from research.dawes_orbit_backend import find_vector_isometry_in_group

        return find_vector_isometry_in_group(self, v1, v2)

    def vectors_are_equivalent(self, v1, v2) -> bool:
        from research.dawes_orbit_backend import vectors_are_equivalent_in_group

        return vectors_are_equivalent_in_group(self, v1, v2)

    def isotropic_line_orbits(self):
        from research.isotropic_gamma_orbit_backend import isotropic_line_orbits_in_group

        return isotropic_line_orbits_in_group(self)

    def isotropic_plane_orbits(self):
        from research.isotropic_gamma_orbit_backend import isotropic_plane_orbits_in_group

        return isotropic_plane_orbits_in_group(self)

    def isotropic_flag_orbits(self, k):
        from research.isotropic_gamma_orbit_backend import isotropic_flag_orbits_in_group

        return isotropic_flag_orbits_in_group(self, k)

    def isotropic_lines_are_equivalent(self, v1, v2) -> bool:
        from research.isotropic_gamma_orbit_backend import (
            isotropic_lines_are_equivalent_in_group,
        )

        return isotropic_lines_are_equivalent_in_group(self, v1, v2)

    def isotropic_planes_are_equivalent(self, basis1, basis2) -> bool:
        from research.isotropic_gamma_orbit_backend import (
            isotropic_planes_are_equivalent_in_group,
        )

        return isotropic_planes_are_equivalent_in_group(self, basis1, basis2)

    def kernel_of_discriminant_action(self) -> LatticeOrthogonalSubgroup:
        r"""Return the sub-subgroup acting trivially on A_L = L*/L.

        Intersects this subgroup's ConditionSet with the predicate
        ``M*x − x ∈ L`` for all dual-lattice generators x.  See
        :meth:`LatticeOrthogonalGroup.kernel_of_discriminant_action`.
        """
        lattice = self._lattice
        cs = _ConditionSet(
            _MatrixSpace(ZZ, lattice.rank()),
            lambda M: _acts_trivially_on_discriminant(lattice, M),
        )
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(
            lattice, self._condition_set & cs
        )
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            {
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": lattice.discriminant_group()
                .orthogonal_group()
                .subgroup([]),
                "opaque": False,
            },
        )
        return subgroup

    def __repr__(self) -> str:
        if self._gens_cache is not None:
            cached = f"{len(self._gens_cache)} gens"
        else:
            cached = "gens not yet computed"
        return f"LatticeOrthogonalSubgroup(rank={self._lattice.rank()}, {cached})"


class DiscriminantOrthogonalGroup:
    r"""The orthogonal group O(A_L) of a discriminant group, with LEFT action.

    Wraps Sage's ``FqfOrthogonalGroup``.  Since A_L is finite, O(A_L) is
    finite and membership is always decidable via GAP.

    Generators are computed lazily by :meth:`gens`.
    """

    def __init__(self, disc: DiscriminantGroup):
        self._disc = disc
        self._sage_group = None  # built lazily
        self._gens_cache = None

    def _require_sage_group(self):
        if self._sage_group is None:
            self._sage_group = _DiscriminantGroupBase.orthogonal_group(self._disc)
        return self._sage_group

    @property
    def discriminant_group(self) -> DiscriminantGroup:
        return self._disc

    def gens(self) -> list:
        """Return generating ZZ-matrices, computing them if needed."""
        if self._gens_cache is None:
            self._gens_cache = [g.matrix() for g in self._require_sage_group().gens()]
        return list(self._gens_cache)

    def __contains__(self, G) -> bool:
        r"""Test G in O(A_L) via GAP (always decidable, O(A_L) is finite)."""
        try:
            sg = self._require_sage_group()
            return sg(G) in sg
        except Exception:
            return False

    def act(self, G, v):
        r"""Apply G to discriminant element v from the left: G * v."""
        from sage.all import vector as sage_vector

        vec = v.vector() if hasattr(v, "vector") else sage_vector(ZZ, v)
        return G * vec

    def subgroup(self, generators) -> DiscriminantOrthogonalSubgroup:
        r"""Return the subgroup generated by *generators*."""
        return DiscriminantOrthogonalSubgroup(
            self._disc, list(generators), self._require_sage_group()
        )

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

    def gens(self) -> list:
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
