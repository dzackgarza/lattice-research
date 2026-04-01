# Task 2.1: Enumerate isotropic vectors in A_{T_Co} and compute O(q_T)-orbits.
# GOAL.md Task 2.1.
#
# Computes O(q_T) orbits by constructing explicit generators of the orthogonal
# group of the torsion quadratic form q_T on A_T = (Z/2Z)^11, then running BFS
# orbit enumeration. Does NOT assume the orbit count from nondegeneracy.

load("/home/dzack/research/computations/coble_geometry_foundation.sage")
from itertools import product as cart_product

# ============================================================================
# Step 1: Construct T_Co and extract discriminant form data
# ============================================================================
print("=" * 72)
print("Task 2.1: Isotropic Orbit Enumeration in A_{T_Co}")
print("=" * 72)

T_Co = T_Co_lattice()
T_Co_gram = T_Co.gram_matrix()
A_T = T_Co.discriminant_group()
n = A_T.ngens()

assert A_T.cardinality() == 2**11, f"Expected |A_T| = 2^11, got {A_T.cardinality()}"
assert A_T.invariants() == (2,) * 11, f"Expected (Z/2Z)^11, got {A_T.invariants()}"

print(f"T_Co: rank {T_Co.rank()}, signature {T_Co.signature()}, det {T_Co.determinant()}")
print(f"A_T: (Z/2Z)^{n}, order {A_T.cardinality()}")

# Extract q-values on generators and bilinear form
q_diag = A_T.gram_matrix_quadratic().diagonal()
B_gram = A_T.gram_matrix_bilinear()

print(f"q_T on generators: {list(q_diag)}")
print(f"Bilinear form diagonal: {list(B_gram.diagonal())}")
assert B_gram == matrix(QQ, n, n, lambda i,j: QQ(1)/2 if i==j else 0), \
    "Expected diagonal bilinear form (1/2)*I"

# Classify generators by q-value
type_half = [i for i in range(n) if q_diag[i] == QQ(1)/2]
type_three_half = [i for i in range(n) if q_diag[i] == QQ(3)/2]
print(f"Generators with q=1/2: indices {type_half} (count {len(type_half)})")
print(f"Generators with q=3/2: indices {type_three_half} (count {len(type_three_half)})")
assert len(type_half) + len(type_three_half) == n

# ============================================================================
# Step 2: Enumerate all isotropic vectors in A_T
# ============================================================================
print()
print("Enumerating all 2^11 = 2048 elements of A_T...")

# Compute q(v) for each vector in (Z/2Z)^11
# q(sum c_i g_i) = sum c_i q(g_i) (since bilinear form is diagonal, cross terms vanish)
# A vector is isotropic iff q(v) = 0 in Q/2Z

iso_vecs = []  # list of tuples of GF(2) coefficients
for coeffs in cart_product([0, 1], repeat=n):
    qval = sum(c * q_diag[i] for i, c in enumerate(coeffs))
    # qval is in Q; isotropic iff qval mod 2Z = 0, i.e. qval in 2*ZZ
    if qval in ZZ and ZZ(qval) % 2 == 0:
        iso_vecs.append(tuple(coeffs))

print(f"Isotropic vectors: {len(iso_vecs)}")
print(f"  Zero vector: {(0,)*n in iso_vecs}")
nonzero_iso = [v for v in iso_vecs if any(c != 0 for c in v)]
print(f"  Nonzero isotropic: {len(nonzero_iso)}")

# Verify count against combinatorial formula:
# q(v) = (k * 1/2) + (m * 3/2) where k = #active type-1/2 coords, m = #active type-3/2 coords
# Isotropic iff (k + 3m)/2 in 2Z iff k + 3m in 4Z iff k - m in 4Z (since 3 = -1 mod 4)
from math import comb
predicted = sum(
    comb(len(type_half), k) * comb(len(type_three_half), m)
    for k in range(len(type_half) + 1)
    for m in range(len(type_three_half) + 1)
    if (k - m) % 4 == 0
)
assert len(iso_vecs) == predicted, f"Count mismatch: {len(iso_vecs)} != {predicted}"
assert len(iso_vecs) == 528, f"Expected 528 isotropic vectors, got {len(iso_vecs)}"
print(f"Isotropic count verified: {len(iso_vecs)} = 528")

# ============================================================================
# Step 3: Construct generators of O(q_T)
# ============================================================================
print()
print("Constructing generators of O(q_T)...")

# The bilinear form is diagonal: b(g_i, g_j) = delta_{ij}/2.
# The form splits as q = q_1 (on type-1/2 coords) ⊕ q_2 (on type-3/2 coords).
# O(q_T) = O(q_1) × O(q_2) since the two blocks are orthogonal.
#
# Generators of O(q_T):
# (A) Permutations within each block (permuting same-q-value generators).
# (B) Transvections T_v(x) = x + b_F2(x,v)*v for isotropic v, where
#     b_F2(x,v) = 2*b(x,v) mod 2 (mapping Q/Z to F_2 via r/2 -> r mod 2).
#     Since b is diagonal, b_F2(x,v) = sum_i x_i*v_i mod 2.
#
# We construct generators as n×n matrices over GF(2).

F2 = GF(2)

def tuple_to_F2vec(t):
    return vector(F2, t)

def F2vec_to_tuple(v):
    return tuple(int(x) for x in v)

def perm_matrix_F2(n, i, j):
    """Transposition matrix swapping coordinates i and j."""
    M = identity_matrix(F2, n)
    M[i, i] = F2(0); M[j, j] = F2(0)
    M[i, j] = F2(1); M[j, i] = F2(1)
    return M

def transvection_matrix_F2(n, v_tuple):
    """Transvection T_v(x) = x + (sum x_i v_i) * v over F_2."""
    v = vector(F2, v_tuple)
    # T_v has matrix I + v^T * v (outer product), since b_F2(x,v) = x . v
    return identity_matrix(F2, n) + matrix(F2, n, 1, list(v)) * matrix(F2, 1, n, list(v))

# (A) Transpositions within type-1/2 block
gens = []
for idx in range(len(type_half) - 1):
    gens.append(perm_matrix_F2(n, type_half[idx], type_half[idx + 1]))

# Transpositions within type-3/2 block
for idx in range(len(type_three_half) - 1):
    gens.append(perm_matrix_F2(n, type_three_half[idx], type_three_half[idx + 1]))

# (B) Transvections by isotropic vectors
# We don't need all of them; a generating set suffices.
# Use isotropic vectors of small weight.
for v in iso_vecs:
    if sum(v) == 0:
        continue  # skip zero
    T = transvection_matrix_F2(n, v)
    if T != identity_matrix(F2, n):
        gens.append(T)
    if len(gens) > 200:
        break  # enough generators

# Verify all generators are isometries of q_T
def is_qT_isometry(M):
    """Check that M preserves q_T on all of (Z/2Z)^11."""
    for coeffs in cart_product([0, 1], repeat=n):
        v = vector(F2, coeffs)
        Mv = M * v
        qv = sum(int(coeffs[i]) * q_diag[i] for i in range(n))
        qMv = sum(int(Mv[i]) * q_diag[i] for i in range(n))
        # Compare in Q/2Z
        if (qv - qMv) not in 2 * ZZ:
            return False
    return True

print(f"Generated {len(gens)} candidate generators")
print("Verifying all generators are O(q_T) isometries...")
for idx, g in enumerate(gens):
    assert is_qT_isometry(g), f"Generator {idx} is not an isometry of q_T"
print(f"All {len(gens)} generators verified as O(q_T) isometries")

# ============================================================================
# Step 4: Compute orbits of isotropic vectors under O(q_T) by BFS
# ============================================================================
print()
print("Computing O(q_T)-orbits of isotropic vectors by BFS...")

iso_set = set(iso_vecs)
visited = set()
orbits = []

for seed in iso_vecs:
    if seed in visited:
        continue
    # BFS from seed
    orbit = set()
    queue = [seed]
    orbit.add(seed)
    while queue:
        current = queue.pop()
        for g in gens:
            img = F2vec_to_tuple(g * tuple_to_F2vec(current))
            if img not in orbit:
                assert img in iso_set, f"Generator mapped isotropic {current} to non-isotropic {img}"
                orbit.add(img)
                queue.append(img)
    visited |= orbit
    orbits.append(orbit)

print(f"Number of O(q_T)-orbits: {len(orbits)}")
for idx, orb in enumerate(orbits):
    rep = min(orb)  # canonical representative
    print(f"  Orbit {idx}: size {len(orb)}, representative {list(rep)}")

# Verify all isotropic vectors are accounted for
assert sum(len(o) for o in orbits) == len(iso_vecs), "Not all isotropic vectors assigned to orbits"

# ============================================================================
# Step 5: Assertions against GOAL.md predictions
# ============================================================================
print()
print("Verification against GOAL.md / Nikulin predictions:")

# The zero vector is always its own orbit
zero_orbit = [o for o in orbits if (0,)*n in o]
assert len(zero_orbit) == 1, "Zero vector should be in exactly one orbit"
assert len(zero_orbit[0]) == 1, "Zero orbit should have size 1"

# All nonzero isotropic vectors should be in a single orbit
nonzero_orbits = [o for o in orbits if (0,)*n not in o]
assert len(nonzero_orbits) == 1, \
    f"Expected 1 nonzero isotropic orbit, got {len(nonzero_orbits)}"
assert len(nonzero_orbits[0]) == 527, \
    f"Expected nonzero orbit size 527, got {len(nonzero_orbits[0])}"

# Total: exactly 2 orbits
assert len(orbits) == 2, f"Expected 2 orbits (zero + nonzero), got {len(orbits)}"

print(f"  Orbits: 2 (zero orbit of size 1, nonzero orbit of size 527)")
print(f"  PASS: all 527 nonzero isotropic vectors form a SINGLE O(q_T)-orbit")
print(f"  PASS: computed (not assumed) via BFS with {len(gens)} verified generators")

# ============================================================================
# Step 6: Record orbit representative for Task 2.2
# ============================================================================
nonzero_rep = list(min(nonzero_orbits[0]))
print()
print(f"Nonzero orbit representative (for Task 2.2): {nonzero_rep}")

print()
print("=" * 72)
print("Task 2.1 Complete")
print("=" * 72)
