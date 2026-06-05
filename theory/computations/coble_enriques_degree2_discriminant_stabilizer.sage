r"""Finite discriminant stabilizer for the degree-2 Enriques polarization.

This is the finite target associated with

    S_En = U(2) + E_8(2) = 2B,  B = U + E_8(-1),

and the K3-side degree-2 Enriques polarization vector ``h=e+f`` in the ``U(2)``
summand.  The discriminant group is identified with ``B/2B``.  The quadratic form is
encoded by

    Q(v) = B(v,v) mod 4,

which represents ``2 q_S(v/2 + S_En)``.

The group computed below is the full finite automorphism group of this discriminant
quadratic form, realized as the subgroup of ``GL(B/2B)`` preserving all fibers of
``Q``.  The final stabilizer is the stabilizer of the discriminant class ``h/2``.

This computes the finite stabilizer target for the discriminant-action description of
``Gamma_En,2``.  The integral stabilizer of ``h`` in ``O(S_En)=O(B)`` has complement
``h^perp = <e-f> + E_8(-1)``, so it has order ``2 |W(E_8)|``.  The finite stabilizer
below is larger by a factor of ``68``; it is a finite container, not the actual image
of the integral stabilizer.
"""

from sage.all import (
    GF,
    GL,
    ZZ,
    Permutation,
    PermutationGroup,
    WeylGroup,
    block_diagonal_matrix,
    matrix,
    vector,
)
from sage.libs.gap.libgap import libgap

F = GF(2)
RANK = 10
H_BITS = 0b11

E8 = matrix(
    ZZ,
    [
        [2, -1, 0, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, 0],
        [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, -1],
        [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0],
        [0, 0, 0, 0, -1, 0, 0, 2],
    ],
)

GRAM_B = block_diagonal_matrix(
    matrix(ZZ, [[0, 1], [1, 0]]),
    -E8,
)


def residue_vector(bits):
    r"""Return the element of ``B/2B`` encoded by an integer bitmask."""
    return vector(ZZ, [(bits >> i) & 1 for i in range(RANK)])


def quadratic_value(bits):
    r"""Return ``B(v,v) mod 4`` for a residue vector ``v in B/2B``."""
    v = residue_vector(bits)
    return int((v * GRAM_B * v.column())[0]) % 4


def act_bits(bits, g):
    r"""Return the bitmask for the right action of ``g in GL(B/2B)``."""
    v = vector(F, [(bits >> i) & 1 for i in range(RANK)])
    w = v * g
    return sum((1 << i) for i, entry in enumerate(w) if int(entry))


def main():
    r"""Compute the finite orthogonal group and the stabilizer of ``h/2``."""
    general_linear_group = GL(RANK, F)
    action_generators = [
        Permutation([act_bits(bits, g) + 1 for bits in range(1 << RANK)])
        for g in general_linear_group.gens()
    ]
    permutation_action = PermutationGroup(action_generators)

    fibers = {
        value: [bits + 1 for bits in range(1 << RANK) if quadratic_value(bits) == value]
        for value in range(4)
    }

    orthogonal_group = permutation_action.gap()
    for value in range(4):
        orthogonal_group = libgap.Stabilizer(
            orthogonal_group,
            libgap(fibers[value]),
            libgap.OnSets,
        )

    h_stabilizer = libgap.Stabilizer(
        orthogonal_group,
        libgap(H_BITS + 1),
        libgap.OnPoints,
    )
    integral_h_stabilizer_order = 2 * ZZ(WeylGroup(["E", 8], prefix="s").cardinality())

    print("fiber_sizes", {value: len(fibers[value]) for value in range(4)})
    print("orthogonal_group_order", orthogonal_group.Size())
    print("h_bits", H_BITS)
    print("h_q_mod4", quadratic_value(H_BITS))
    print("h_stabilizer_order", h_stabilizer.Size())
    print("integral_h_stabilizer_order", integral_h_stabilizer_order)
    print(
        "finite_container_index_over_integral_stabilizer",
        ZZ(h_stabilizer.Size()) // integral_h_stabilizer_order,
    )


if __name__ == "__main__":
    main()
