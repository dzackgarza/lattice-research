r"""
Executable lattice-interface semantics migrated from the implemented portion of
``lattice_interface_spec.sage``.

This file records only the exact surface that the current lattice foundation
actually exposes.  The remaining aspirational dual/Weyl/Eichler API in the
legacy top-level draft is left there until it can be migrated faithfully.
"""

from src import Lattice

# ============================================================================
# 1. CONSTRUCTORS, PARSING, AND ELEMENT SEMANTICS
# ============================================================================

Z = Lattice.Z()
U = Lattice.U()
e, f = tuple(U.basis())

assert Z.rank() == 1
assert Z.gram_matrix() == matrix(ZZ, [[1]])
assert Z.twist(2).gram_matrix() == matrix(ZZ, [[2]])

assert Lattice.II(0, 8).is_isometric_to(Lattice.E(8))
assert Lattice.II(3, 19).is_isometric_to(Lattice.k3())
assert Lattice.I(1, 10).signature_pair() == (1, 10)
assert Lattice.from_string("U(2) + A_1").is_isometric_to(Lattice.U().twist(2) + Lattice.A(1))
assert Lattice.from_string("U^{3} + D_{6} + E_{8}").rank() == 20

module_U = FreeBilinearModule.from_sage(IntegralLattice("U"))
module_generator = next(iter(module_U.gens()))
assert module_generator.is_isotropic()

assert e.is_isotropic() and f.is_isotropic()
assert e.inner_product(f) == 1
assert e.divisibility() == 1
assert e.is_primitive()
assert e.discriminant_class().is_zero()


# ============================================================================
# 2. U(2): DISCRIMINANT FORM, NIKULIN DATA, AND GENUS PRECHECKS
# ============================================================================

NativeLattice = type(IntegralLattice("U"))

native_u2 = IntegralLattice(2 * IntegralLattice("U").inner_product_matrix())
u2_first, u2_second = tuple(native_u2.basis())
native_u2_changed = NativeLattice(
    native_u2.ambient_module(),
    native_u2.submodule((u2_first, u2_first + u2_second)).basis_matrix(),
    native_u2.inner_product_matrix(),
)
native_u2_split = NativeLattice.direct_sum(
    Lattice.Z().twist(2),
    Lattice.Z().twist(-2),
)

U2 = Lattice.from_sage(native_u2)
U2_changed = Lattice.from_sage(native_u2_changed)
U2_split = Lattice.from_sage(native_u2_split)

assert U2.is_even()
assert U2.signature_pair() == (1, 1)
assert U2.determinant() == -4
assert U2.discriminant_group().cardinality() == 4
assert U2.discriminant_group().is_p_elementary(2)
assert U2.discriminant_group().p_rank(2) == 2
assert U2.discriminant_group().delta() == 0
assert U2.nikulin_invariants() == (2, 2, 0)

assert U2.is_isometric_to(U2_changed)
assert U2.has_isomorphic_discriminant_group_to(U2_split)
assert not U2.has_isomorphic_discriminant_form_to(U2_split)
assert U2.is_rationally_isometric_to(U2_split)
assert not U2.is_locally_isometric_to(U2_split, 2)
assert U2.is_locally_isometric_to(U2_split, 3)
assert U2.is_locally_isometric_to(U2_split, 5)
assert not U2.is_in_same_genus_as(U2_split)
assert not U2.is_isometric_to(U2_split)


# ============================================================================
# 3. U(3): GENERAL INDEFINITE BASIS CHANGES
# ============================================================================

native_u3 = IntegralLattice(3 * IntegralLattice("U").inner_product_matrix())
u3_first, u3_second = tuple(native_u3.basis())
native_u3_changed = NativeLattice(
    native_u3.ambient_module(),
    native_u3.submodule((u3_first, u3_first + u3_second)).basis_matrix(),
    native_u3.inner_product_matrix(),
)

U3 = Lattice.from_sage(native_u3)
U3_changed = Lattice.from_sage(native_u3_changed)

assert U3.discriminant_group().is_p_elementary(3)
assert not U3.discriminant_group().is_p_elementary(2)
assert U3.has_isomorphic_discriminant_group_to(U3_changed)
assert U3.has_isomorphic_discriminant_form_to(U3_changed)
assert U3.is_rationally_isometric_to(U3_changed)
assert U3.is_locally_isometric_to(U3_changed, 2)
assert U3.is_locally_isometric_to(U3_changed, 3)
assert U3.is_locally_isometric_to(U3_changed, 5)
assert U3.is_in_same_genus_as(U3_changed)
assert U3.is_isometric_to(U3_changed)


# ============================================================================
# 4. K3 / COBLE MODELS AND EXACT MORPHISM CONTRACTS
# ============================================================================

K3 = Lattice.k3()
assert K3.is_even()
assert K3.signature_pair() == (3, 19)
assert K3.discriminant_group().cardinality() == 1
assert K3.nikulin_invariants() == (22, 0, 0)

k3_identity = K3.hom(K3, tuple(K3.basis()))
assert k3_identity.image_lattice().is_isometric_to(K3)
assert k3_identity.orthogonal_complement_of_image().rank() == 0

coble_picard = Lattice.coble_picard()
coble_transcendental = Lattice.coble_transcendental()

assert coble_picard.signature_pair() == (1, 10)
assert coble_picard.discriminant_group().is_p_elementary(2)
assert coble_picard.nikulin_invariants() == (11, 11, 1)
assert coble_picard.is_isometric_to(Lattice.Z().twist(2) + (Lattice.Z().twist(-2) ** 10))

assert coble_transcendental.signature_pair() == (2, 9)
assert coble_transcendental.discriminant_group().cardinality() == 2
assert coble_transcendental.nikulin_invariants() == (11, 1, 1)
assert coble_transcendental.is_isometric_to(Lattice.Z().twist(2) + Lattice.U() + Lattice.E(8))


# ============================================================================
# 5. ISOTROPIC-ORBIT SPLITTING AND STABILIZERS
# ============================================================================

I2 = identity_matrix(ZZ, 2)
minus_I2 = -I2

O_U = U.orthogonal_group()
SO_U = O_U.special_orthogonal_subgroup()

assert len(O_U.isotropic_line_orbits()) == 1
assert len(SO_U.isotropic_line_orbits()) == 2
assert O_U.isotropic_lines_are_equivalent(e, f)
assert not SO_U.isotropic_lines_are_equivalent(e, f)

assert I2 in U.stabilizer_of_vector(e)
assert minus_I2 not in U.stabilizer_of_vector(e)
assert minus_I2 in U.stabilizer_of_isotropic_line(e)

U_plus_U = Lattice.from_sage(IntegralLattice("U").direct_sum(IntegralLattice("U")))
assert len(U_plus_U.orthogonal_group().isotropic_plane_orbits()) == 1
assert len(U_plus_U.orthogonal_group().special_orthogonal_subgroup().isotropic_plane_orbits()) == 2
assert len(U_plus_U.orthogonal_group().isotropic_flag_orbits(2)) == 1
assert len(U_plus_U.orthogonal_group().special_orthogonal_subgroup().isotropic_flag_orbits(2)) == 2


# ============================================================================
# 6. INVOLUTION EIGENLATTICES, CENTRALIZERS, AND DISCRIMINANT KERNELS
# ============================================================================

A2 = Lattice.from_sage(IntegralLattice("A2"))
minus_A2 = -identity_matrix(ZZ, 2)

assert A2.invariant_sublattice(minus_A2).rank() == 0
coinv_A2 = A2.coinvariant_sublattice(minus_A2)
assert coinv_A2.rank() == A2.rank()
assert coinv_A2.inner_product_matrix() == A2.inner_product_matrix()

centralizer_A2 = A2.centralizer_of_involution(minus_A2)
assert minus_A2 in centralizer_A2
assert identity_matrix(ZZ, 2) in centralizer_A2.kernel_of_discriminant_action()
assert minus_A2 not in centralizer_A2.kernel_of_discriminant_action()

A1_plus_A1 = Lattice.from_sage(IntegralLattice(matrix(ZZ, [[2, 0], [0, 2]])))
swap_involution = matrix(ZZ, [[1, 0], [0, -1]])
swap_matrix = matrix(ZZ, [[0, 1], [1, 0]])

assert swap_involution in A1_plus_A1.orthogonal_group()
inv_A1A1 = A1_plus_A1.invariant_sublattice(swap_involution)
coinv_A1A1 = A1_plus_A1.coinvariant_sublattice(swap_involution)
assert inv_A1A1.rank() == 1
assert coinv_A1A1.rank() == 1
assert inv_A1A1.rank() + coinv_A1A1.rank() == A1_plus_A1.rank()
assert swap_matrix in A1_plus_A1.orthogonal_group()
assert swap_matrix not in A1_plus_A1.centralizer_of_involution(swap_involution)

minus_U = -identity_matrix(ZZ, 2)
kernel_U = U.centralizer_of_involution(minus_U).kernel_of_discriminant_action()
assert minus_U in kernel_U

combined = U.centralizer_of_involution(minus_U) & U.stabilizer_of_vector(vector(ZZ, [1, 0]))
assert identity_matrix(ZZ, 2) in combined
assert minus_U not in combined
