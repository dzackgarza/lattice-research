"""
Task 5.1: Primitive S_Co embedding and orthogonal complement gate.

This script implements only the current exact Task 5.1 slice:
- build a primitive S_Co embedding into a concrete K3-lattice model;
- compute the true orthogonal complement inside that ambient lattice;
- verify discriminant-form compatibility on the computed complement;
- stop before any theta reconstruction or export.
"""

import sys
from sage.all import *


RESULTS_FILE = "/home/dzack/research/computations/task5_1_primitive_results.txt"
def fail(message):
    print(f"ERROR: {message}")
    raise SystemExit(1)


def smith_diagonal(M):
    S, _, _ = M.smith_form()
    return [S[i, i] for i in range(min(S.nrows(), S.ncols())) if S[i, i] != 0]


def primitive_kernel_basis(A):
    """Return an integral basis for ker(A: Z^n -> Z^m)."""
    D, U, V = A.smith_form()
    rank = sum(1 for i in range(min(D.nrows(), D.ncols())) if D[i, i] != 0)
    return V[:, rank:]


def matrix_signature(G):
    p, n, _ = QuadraticForm(G).signature_vector()
    return (p, n)


def build_glued_k3_model():
    """
    Construct an even unimodular (3,19)-lattice by gluing
    S_Co = <2> + <-2>^10 and T_Co = <2>^2 + <-2>^9 along a graph isometry of
    discriminant forms.
    """
    S_expected = diagonal_matrix(ZZ, [2] + [-2] * 10)
    T_expected = diagonal_matrix(ZZ, [2, 2] + [-2] * 9)
    ambient_split_gram = block_diagonal_matrix([S_expected, T_expected])

    # Basis for a discriminant-form graph A_S -> A_T with q_T(phi(x)) = -q_S(x).
    glue_bits = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    ]

    doubled_generators = []
    for i in range(22):
        row = [0] * 22
        row[i] = 2
        doubled_generators.append(row)

    for i in range(11):
        row = [0] * 22
        row[i] = 1
        for j, bit in enumerate(glue_bits[i]):
            row[11 + j] = bit
        doubled_generators.append(row)

    hermite = matrix(ZZ, doubled_generators).hermite_form()
    ambient_basis_rows = [hermite.row(i) / 2 for i in range(hermite.nrows()) if hermite.row(i) != 0]
    ambient_basis = matrix(QQ, [list(row) for row in ambient_basis_rows])
    ambient_gram = ambient_basis * ambient_split_gram * ambient_basis.transpose()

    if ambient_basis.nrows() != 22:
        fail(f"glued ambient lattice has rank {ambient_basis.nrows()}, expected 22")
    if any(entry not in ZZ for entry in ambient_gram.list()):
        fail("glued ambient Gram matrix is not integral")
    ambient_gram = ambient_gram.change_ring(ZZ)
    if any(ambient_gram[i, i] % 2 != 0 for i in range(22)):
        fail("glued ambient lattice is not even")
    if ambient_gram.determinant() != -1:
        fail(f"glued ambient determinant is {ambient_gram.determinant()}, expected -1")
    if matrix_signature(ambient_gram) != (3, 19):
        fail(f"glued ambient signature is {matrix_signature(ambient_gram)}, expected (3, 19)")

    return {
        "S_expected": S_expected,
        "T_expected": T_expected,
        "ambient_split_gram": ambient_split_gram,
        "ambient_basis": ambient_basis,
        "ambient_gram": ambient_gram,
        "glue_bits": glue_bits,
    }


def solve_coordinates(basis_rows, target_row):
    column = matrix(QQ, basis_rows.ncols(), 1, list(target_row))
    solution = basis_rows.transpose().solve_right(column)
    return vector(QQ, [solution[i, 0] for i in range(solution.nrows())])


def embed_expected_sco(ambient_basis):
    embedded_rows = []
    for i in range(11):
        target = [0] * 22
        target[i] = 1
        embedded_rows.append(solve_coordinates(ambient_basis, vector(QQ, target)))
    return matrix(QQ, embedded_rows)


def compute_true_complement(embedded_sco, ambient_gram):
    pairing_constraints = (embedded_sco * ambient_gram).change_ring(ZZ)
    complement_columns = primitive_kernel_basis(pairing_constraints)
    complement = complement_columns.transpose().change_ring(ZZ)
    return complement


print("=" * 80)
print("Task 5.1: Primitive S_Co embedding and orthogonal complement gate")
print("=" * 80)
print()

print("[1] Building exact glued K3-lattice model")
model = build_glued_k3_model()
ambient_basis = model["ambient_basis"]
ambient_gram = model["ambient_gram"]
S_expected = model["S_expected"]
T_expected = model["T_expected"]

print(f"  Ambient rank: {ambient_gram.nrows()}")
print(f"  Ambient signature: {matrix_signature(ambient_gram)}")
print(f"  Ambient determinant: {ambient_gram.determinant()}")
print(f"  Ambient even: {all(ambient_gram[i, i] % 2 == 0 for i in range(22))}")
print()

print("[2] Embedding S_Co with exact target Gram matrix")
embedded_sco = embed_expected_sco(ambient_basis)
if any(entry not in ZZ for entry in embedded_sco.list()):
    fail("embedded S_Co coordinates are not integral in the ambient basis")
embedded_sco = embedded_sco.change_ring(ZZ)
embedded_sco_gram = embedded_sco * ambient_gram * embedded_sco.transpose()

print(f"  Embedded S_Co rank: {embedded_sco.nrows()}")
print(f"  Embedded S_Co Smith diagonal: {smith_diagonal(embedded_sco)}")
print(f"  Embedded S_Co Gram diagonal: {embedded_sco_gram.diagonal()}")

if embedded_sco_gram != S_expected:
    fail("embedded S_Co Gram matrix does not match diag(2, -2, ..., -2)")
if smith_diagonal(embedded_sco) != [1] * 11:
    fail("embedded S_Co is not primitive in the ambient lattice")

print("  PASS: embedded S_Co has the exact expected Gram matrix")
print("  PASS: embedded S_Co is primitive")
print()

print("[3] Computing the true orthogonal complement T = S_Co^perp")
complement = compute_true_complement(embedded_sco, ambient_gram)
complement_gram = complement * ambient_gram * complement.transpose()
cross_pairing = embedded_sco * ambient_gram * complement.transpose()
combined = embedded_sco.stack(complement)

print(f"  Complement rank: {complement.nrows()}")
print(f"  Complement signature: {matrix_signature(complement_gram)}")
print(f"  Complement determinant: {complement_gram.determinant()}")
print(f"  Complement Smith diagonal: {smith_diagonal(complement)}")
print(f"  Cross pairing zero: {cross_pairing.is_zero()}")
print(f"  Combined Smith diagonal: {smith_diagonal(combined)}")

if complement.nrows() != 11:
    fail(f"computed complement rank is {complement.nrows()}, expected 11")
if matrix_signature(complement_gram) != (2, 9):
    fail(f"computed complement signature is {matrix_signature(complement_gram)}, expected (2, 9)")
if not cross_pairing.is_zero():
    fail("computed complement is not orthogonal to embedded S_Co")
if abs(complement_gram.determinant()) != 2048:
    fail(f"computed complement determinant is {complement_gram.determinant()}, expected +/-2048")
if smith_diagonal(complement) != [1] * 11:
    fail("computed complement is not primitive in the ambient lattice")
if smith_diagonal(combined) != ([1] * 11 + [2] * 11):
    fail("embedded S_Co plus computed complement does not have the expected index-2^11 gluing profile")

print("  PASS: true complement has rank 11, signature (2,9), zero cross-pairing, and |det| = 2048")
print()

print("[4] Checking discriminant compatibility on the actual computed complement")
S_lattice = IntegralLattice(S_expected)
T_actual_lattice = IntegralLattice(complement_gram)

A_S = S_lattice.discriminant_group()
A_T_actual = T_actual_lattice.discriminant_group()
q_T_actual = A_T_actual.gram_matrix_quadratic()

brown_S = (1 - 10) % 8
brown_T_actual = (matrix_signature(complement_gram)[0] - matrix_signature(complement_gram)[1]) % 8
expected_brown = (-brown_S) % 8

print(f"  |A_S|: {A_S.cardinality()}")
print(f"  |A_T(actual)|: {A_T_actual.cardinality()}")
print(f"  A_T(actual) invariants: {A_T_actual.invariants()}")
print(f"  Brown(q_S): {brown_S}")
print(f"  Brown(q_T(actual)): {brown_T_actual}")
print(f"  Expected Brown(q_T(actual)): {expected_brown}")
print(f"  q_T(actual) diagonal sample: {list(q_T_actual.diagonal()[:5])}")

if A_T_actual.cardinality() != 2048:
    fail(f"actual complement discriminant-group order is {A_T_actual.cardinality()}, expected 2048")
if A_T_actual.invariants() != (2,) * 11:
    fail(f"actual complement discriminant-group invariants are {A_T_actual.invariants()}, expected (2^11)")
if brown_T_actual != expected_brown:
    fail(
        f"actual complement Brown invariant is {brown_T_actual}, expected {expected_brown} = -Brown(q_S) mod 8"
    )

print("  PASS: discriminant-group compatibility is verified on the actual computed complement")
print()

lines = [
    "Task 5.1 primitive embedding and complement gate",
    "=" * 80,
    "",
    "Ambient lattice:",
    f"  Rank: {ambient_gram.nrows()}",
    f"  Signature: {matrix_signature(ambient_gram)}",
    f"  Determinant: {ambient_gram.determinant()}",
    "",
    "Embedded S_Co:",
    f"  Primitive: {smith_diagonal(embedded_sco) == [1] * 11}",
    f"  Gram diagonal: {embedded_sco_gram.diagonal()}",
    "",
    "Computed orthogonal complement:",
    f"  Rank: {complement.nrows()}",
    f"  Signature: {matrix_signature(complement_gram)}",
    f"  Determinant: {complement_gram.determinant()}",
    f"  Cross pairing zero: {cross_pairing.is_zero()}",
    "",
    "Actual complement discriminant group:",
    f"  Order: {A_T_actual.cardinality()}",
    f"  Invariants: {A_T_actual.invariants()}",
    f"  Brown(q_T(actual)): {brown_T_actual}",
    f"  Expected -Brown(q_S): {expected_brown}",
    "",
    "Stop rule:",
    "  No theta matrix was constructed or exported.",
]

with open(RESULTS_FILE, "w") as handle:
    handle.write("\n".join(str(line) for line in lines) + "\n")

print("[5] Results written")
print(f"  Results file: {RESULTS_FILE}")
print()
print("Task 5.1 primitive/complement gate passed.")
