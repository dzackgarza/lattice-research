from __future__ import annotations

from dataclasses import dataclass

from sage.all import ZZ, MatrixGroup, matrix, vector
from sage.libs.gap.libgap import libgap

from research.dawes_orbit_backend import (
    induced_discriminant_action,
    real_spinor_norm_sign,
)
from src.external.py_polyhedral import (
    indefinite_form_test_equivalence_isotropic_k_plane,
    indefinite_form_test_equivalence_vector,
)


def isotropic_line_orbits_in_group(group):
    return _IsotropicOrbitBackend(group, "line").orbit_representatives()


def isotropic_plane_orbits_in_group(group):
    return _IsotropicOrbitBackend(group, "plane").orbit_representatives()


def isotropic_flag_orbits_in_group(group, k):
    return _IsotropicOrbitBackend(group, "flag", flag_depth=k).orbit_representatives()


def isotropic_lines_are_equivalent_in_group(group, v1, v2) -> bool:
    return _IsotropicOrbitBackend(group, "line").objects_are_equivalent(v1, v2)


def isotropic_planes_are_equivalent_in_group(group, basis1, basis2) -> bool:
    return _IsotropicOrbitBackend(group, "plane").objects_are_equivalent(
        tuple(basis1),
        tuple(basis2),
    )


@dataclass(frozen=True)
class _StructuredSubgroupSpec:
    lattice: object
    determinant: int | None
    spinor: int | None
    discriminant_subgroup: object | None
    opaque: bool


@dataclass
class _FiniteQuotientSpec:
    ambient_group: object
    source_group: object
    source_gap_group: object
    target_gap_group: object
    subgroup_image: object
    hom: object
    image_from_matrix: object

    def image(self, M):
        return self.image_from_matrix(matrix(ZZ, M))

    def image_subgroup(self, matrices):
        return _gap_subgroup(
            self.target_gap_group,
            [self.image(M) for M in matrices],
        )

    def lift(self, target_element):
        lifted = libgap.PreImagesRepresentative(self.hom, target_element)
        return matrix(ZZ, lifted)


class _IsotropicOrbitBackend:
    def __init__(self, group, orbit_kind, *, flag_depth=None):
        self._group = group
        self._lattice = group.lattice
        self._orbit_kind = orbit_kind
        self._flag_depth = flag_depth
        self._spec = _compile_subgroup_spec(group)
        self._finite_quotient = _finite_quotient_spec(group, self._spec)

    def orbit_representatives(self):
        ambient_orbits = _ambient_isotropic_orbits(
            self._lattice,
            self._orbit_kind,
            flag_depth=self._flag_depth,
        )
        if self._finite_quotient is None:
            return list(ambient_orbits)
        orbit_reps = []
        for ambient_rep in ambient_orbits:
            stabilizer_gens = _ambient_stabilizer_generators(
                self._lattice,
                self._orbit_kind,
                ambient_rep,
            )
            stabilizer_image = self._finite_quotient.image_subgroup(stabilizer_gens)
            double_cosets = libgap.DoubleCosets(
                self._finite_quotient.target_gap_group,
                stabilizer_image,
                self._finite_quotient.subgroup_image,
            )
            for double_coset in double_cosets:
                representative = libgap.Representative(double_coset)
                lift = self._finite_quotient.lift(representative)
                orbit_reps.append(
                    _apply_ambient_isometry(
                        self._lattice,
                        self._orbit_kind,
                        ambient_rep,
                        lift,
                    )
                )
        return orbit_reps

    def objects_are_equivalent(self, left, right) -> bool:
        ambient_witness = _ambient_equivalence_witness(
            self._lattice,
            self._orbit_kind,
            left,
            right,
        )
        if ambient_witness is None:
            return False
        if ambient_witness in self._group:
            return True
        assert self._finite_quotient is not None, (
            "Subgroup isotropic equivalence requires a computable finite quotient image"
        )
        stabilizer_gens = _ambient_stabilizer_generators(
            self._lattice,
            self._orbit_kind,
            _normalize_isotropic_object(self._lattice, self._orbit_kind, right),
        )
        stabilizer_image = self._finite_quotient.image_subgroup(stabilizer_gens)
        identity_double_coset = libgap.DoubleCoset(
            stabilizer_image,
            libgap.One(self._finite_quotient.target_gap_group),
            self._finite_quotient.subgroup_image,
        )
        return self._finite_quotient.image(ambient_witness) in identity_double_coset


def _compile_subgroup_spec(group):
    constraints = getattr(
        group,
        "_orbit_constraints",
        {
            "determinant": None,
            "spinor": None,
            "discriminant_subgroup": None,
            "opaque": False,
        },
    )
    return _StructuredSubgroupSpec(
        lattice=group.lattice,
        determinant=constraints["determinant"],
        spinor=constraints["spinor"],
        discriminant_subgroup=constraints["discriminant_subgroup"],
        opaque=constraints["opaque"],
    )


def _finite_quotient_spec(group, spec):
    if _is_full_ambient_group(group):
        return None
    assert not spec.opaque, (
        "Subgroup isotropic splitting requires structured subgroup constraints"
    )
    factors = []
    if spec.discriminant_subgroup is not None:
        ambient_disc_group = spec.lattice.discriminant_group().orthogonal_group()
        sage_disc_group = ambient_disc_group._require_sage_group()
        disc_gap_group = libgap(sage_disc_group)
        allowed_disc_group = libgap(spec.discriminant_subgroup._sage_subgroup)

        def _disc_image(M, _lattice=spec.lattice, _sage_disc_group=sage_disc_group):
            return libgap(_sage_disc_group(induced_discriminant_action(_lattice, M)))

        factors.append(
            (
                disc_gap_group,
                allowed_disc_group,
                _disc_image,
            )
        )
    if spec.determinant is not None:
        assert spec.determinant == 1, (
            "Finite subgroup images only support determinant kernel constraints"
        )
        c2_det = libgap.CyclicGroup(2)
        det_gen = c2_det.GeneratorsOfGroup()[0]

        def _det_image(M, _det_gen=det_gen, _c2_det=c2_det):
            return libgap.One(_c2_det) if ZZ(M.det()) == 1 else _det_gen

        factors.append(
            (
                c2_det,
                _gap_subgroup(c2_det, []),
                _det_image,
            )
        )
    if spec.spinor is not None:
        assert spec.spinor == 1, (
            "Finite subgroup images only support positive spinor kernel constraints"
        )
        c2_spin = libgap.CyclicGroup(2)
        spin_gen = c2_spin.GeneratorsOfGroup()[0]

        def _spin_image(M, _spin_gen=spin_gen, _c2_spin=c2_spin, _lattice=spec.lattice):
            return (
                libgap.One(_c2_spin)
                if real_spinor_norm_sign(_lattice, M) == 1
                else _spin_gen
            )

        factors.append(
            (
                c2_spin,
                _gap_subgroup(c2_spin, []),
                _spin_image,
            )
        )
    assert factors, (
        "Subgroup isotropic splitting requires determinant, spinor, or discriminant-image data"
    )
    ambient_group = spec.lattice.orthogonal_group()
    ambient_generators = [matrix(ZZ, generator) for generator in ambient_group.gens()]
    source_group = MatrixGroup(ambient_generators)
    source_gap_group = libgap(source_group)

    if len(factors) == 1:
        target_gap_group, allowed_group, image_fn = factors[0]
        target_images = [image_fn(generator) for generator in ambient_generators]

        def _image_from_matrix(M, _image_fn=image_fn):
            return _image_fn(M)

    else:
        target_gap_group = libgap.DirectProduct(*[factor[0] for factor in factors])
        embeddings = [
            libgap.Embedding(target_gap_group, index + 1)
            for index in range(len(factors))
        ]
        target_images = []
        for generator in ambient_generators:
            product_image = libgap.One(target_gap_group)
            for embedding, (_, _, image_fn) in zip(embeddings, factors, strict=True):
                product_image *= libgap.Image(embedding, image_fn(generator))
            target_images.append(product_image)
        allowed_gens = []
        for embedding, (_, allowed_factor, _) in zip(embeddings, factors, strict=True):
            allowed_gens.extend(
                libgap.Image(embedding, gen)
                for gen in allowed_factor.GeneratorsOfGroup()
            )
        allowed_group = _gap_subgroup(target_gap_group, allowed_gens)

        def _image_from_matrix(M, _embeddings=embeddings, _factors=factors, _target=target_gap_group):
            product_image = libgap.One(_target)
            for embedding, (_, _, image_fn) in zip(_embeddings, _factors, strict=True):
                product_image *= libgap.Image(embedding, image_fn(M))
            return product_image

    target_image_group = _gap_subgroup(target_gap_group, target_images)
    subgroup_image = libgap.Intersection(target_image_group, allowed_group)
    hom = libgap.GroupHomomorphismByImagesNC(
        source_gap_group,
        target_gap_group,
        source_gap_group.GeneratorsOfGroup(),
        target_images,
    )
    return _FiniteQuotientSpec(
        ambient_group=ambient_group,
        source_group=source_group,
        source_gap_group=source_gap_group,
        target_gap_group=target_image_group,
        subgroup_image=subgroup_image,
        hom=hom,
        image_from_matrix=_image_from_matrix,
    )


def _is_full_ambient_group(group) -> bool:
    constraints = getattr(group, "_orbit_constraints", None)
    if constraints is None:
        return False
    return (
        group.__class__.__name__ == "LatticeOrthogonalGroup"
        and constraints["determinant"] is None
        and constraints["spinor"] is None
        and constraints["discriminant_subgroup"] is None
        and not constraints["opaque"]
    )


def _gap_subgroup(parent_group, generators):
    generators = list(generators)
    if generators:
        return libgap.Subgroup(parent_group, generators)
    return libgap.TrivialSubgroup(parent_group)


def _ambient_isotropic_orbits(lattice, orbit_kind, *, flag_depth=None):
    if orbit_kind == "line":
        return tuple(
            lattice(_normalize_primitive_line(v))
            for v in lattice.isotropic_line_orbits()
        )
    if orbit_kind == "plane":
        return tuple(tuple(lattice(v) for v in pair) for pair in lattice.isotropic_plane_orbits())
    assert orbit_kind == "flag"
    assert flag_depth is not None and flag_depth >= 1
    return tuple(
        tuple(lattice(v) for v in flag)
        for flag in lattice.isotropic_flag_orbits(flag_depth)
    )


def _ambient_stabilizer_generators(lattice, orbit_kind, isotropic_object):
    if orbit_kind == "line":
        return lattice.stabilizer_of_isotropic_line(isotropic_object).gens()
    if orbit_kind == "plane":
        return lattice.stabilizer_of_isotropic_plane(*isotropic_object).gens()
    assert orbit_kind == "flag"
    return lattice.stabilizer_of_isotropic_flag(list(isotropic_object)).gens()


def _normalize_primitive_line(v):
    primitive = vector(ZZ, list(v))
    gcd_value = ZZ.zero()
    for entry in primitive:
        gcd_value = gcd_value.gcd(ZZ(entry))
    assert gcd_value > 0
    primitive = vector(ZZ, [ZZ(entry) // gcd_value for entry in primitive])
    for entry in primitive:
        if entry:
            return -primitive if entry < 0 else primitive
    assert False, "Primitive isotropic line representative must be nonzero"


def _normalize_isotropic_object(lattice, orbit_kind, isotropic_object):
    if orbit_kind == "line":
        return lattice(_normalize_primitive_line(isotropic_object))
    if orbit_kind == "plane":
        return tuple(lattice(vector(ZZ, list(row))) for row in isotropic_object)
    assert orbit_kind == "flag"
    return tuple(lattice(vector(ZZ, list(row))) for row in isotropic_object)


def _apply_ambient_isometry(lattice, orbit_kind, isotropic_object, M):
    if orbit_kind == "line":
        image = lattice(M * vector(ZZ, list(isotropic_object)))
        return lattice(_normalize_primitive_line(image))
    images = tuple(
        lattice(M * vector(ZZ, list(row)))
        for row in isotropic_object
    )
    return images


def _ambient_equivalence_witness(lattice, orbit_kind, left, right):
    if orbit_kind == "line":
        left_vec = vector(ZZ, list(_normalize_primitive_line(left)))
        right_vec = vector(ZZ, list(_normalize_primitive_line(right)))
        for target in (right_vec, -right_vec):
            raw = indefinite_form_test_equivalence_vector(
                lattice._gram_rows(),
                [int(entry) for entry in left_vec],
                [int(entry) for entry in target],
            )
            if raw is None:
                continue
            return _normalize_vector_witness(lattice, raw, left_vec, target)
        return None
    left_rows = _object_basis_rows(left)
    right_rows = _object_basis_rows(right)
    raw = indefinite_form_test_equivalence_isotropic_k_plane(
        lattice._gram_rows(),
        left_rows,
        right_rows,
        choice="plane",
    )
    if raw is None:
        return None
    return _normalize_subspace_witness(
        lattice,
        raw,
        left_rows,
        right_rows,
    )


def _object_basis_rows(isotropic_object):
    return [[int(entry) for entry in row] for row in isotropic_object]


def _normalize_vector_witness(lattice, raw_matrix, source, target):
    gram = lattice.inner_product_matrix()
    raw = matrix(ZZ, raw_matrix)
    candidate = raw.inverse().transpose()
    assert candidate.transpose() * gram * candidate == gram
    assert candidate * source == target
    return candidate


def _normalize_subspace_witness(lattice, raw_matrix, source_rows, target_rows):
    gram = lattice.inner_product_matrix()
    raw = matrix(ZZ, raw_matrix)
    candidate = raw.inverse().transpose()
    assert candidate.transpose() * gram * candidate == gram
    source_basis = matrix(ZZ, source_rows)
    target_basis = matrix(ZZ, target_rows)
    source_image = source_basis * raw
    assert source_image.row_module() == target_basis.row_module()
    return candidate
