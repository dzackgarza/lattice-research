# Research Log: Coble Moduli Project

## 2026-03-25 - Task 1.2: Gram Matrices and (r,a,δ) Invariants

**Status**: ✓ Solved

**Problem Statement**:
Compute Gram matrices for the Coble lattice $S_{Co}$ and transcendental lattice $T_{Co}$, verify $(r,a,\delta)$ invariants and genus cardinality using Nikulin's classification.

**Approach**:

1. Constructed $S_{Co} \cong \langle 2 \rangle \oplus \langle -2 \rangle^{10}$ with diagonal Gram matrix
2. Embedded $S_{Co}$ in K3 lattice $\Lambda_{K3} \cong U^3 \oplus E_8(-1)^2$
3. Constructed $T_{Co} = S_{Co}^\perp$ with correct signature $(2,9)$
4. Computed discriminant groups and forms for both lattices
5. Verified $(r,a,\delta)$ invariants and analyzed genus uniqueness

**Results**:

- $S_{Co}$ Gram matrix: $\text{diag}(2, -2, -2, \ldots, -2)$ (11×11)
- $T_{Co}$ Gram matrix: $\text{diag}(2, 2, -2, \ldots, -2)$ (11×11)
- $S_{Co}$: $(r,a,\delta) = (11, 11, 1)$, signature $(1,10)$
- $T_{Co}$: $(r,a,\delta) = (11, 11, 1)$, signature $(2,9)$
- Both have discriminant group $A \cong (\mathbb{Z}/2\mathbb{Z})^{11}$
- Discriminant forms: $q_S, q_T$ take values in $(1/2)\mathbb{Z}/2\mathbb{Z}$, so $\delta = 1$
- Genus uniqueness: $r = a = 11$ is boundary case; uniqueness follows from Nikulin 1.10.1 (signature mod 8 analysis)
- Embedding $S_{Co} \hookrightarrow \Lambda_{K3}$ is primitive ($|\text{disc}(S_{Co})| = |\text{disc}(T_{Co})|$)
- Verified $q_S = -q_T \pmod{2\mathbb{Z}}$

**Key Insight**:
The simple $r > a$ criterion from Nikulin 1.5.2 doesn't apply directly when $r = a$. For 2-elementary lattices with $r = a$ and $\delta = 1$, genus uniqueness depends on the signature modulo 8 (Nikulin 1.10.1). Both $S_{Co}$ and $T_{Co}$ fall into this boundary case but still have unique genus.

**Tools Developed**:

- SageMath script for lattice construction and invariant computation
- Methods for computing discriminant forms via `gram_matrix_quadratic()`
- Verification framework for $(r,a,\delta)$ invariants

**References**:

- [Nikulin1979] Theorem 1.5.2 (r > a criterion), Theorem 1.10.1 (boundary case classification)
- [DolgachevKondyrev2013] Coble surface lattice invariants

**Files**:

- `computations/task1_2_gram_matrices.sage` - Main computation script
- `computations/task1_2_results.txt` - Output results

**Next Steps**:

- Task 1.3: Derive explicit primitive embedding matrices $T_{Co} \hookrightarrow T_{En} \hookrightarrow T_{dP} \hookrightarrow \Lambda_{K3}$

---

## 2026-03-25 - Task 1.3: Primitive Embedding Matrices

**Status**: ✓ Solved

**Problem Statement**:
Construct explicit primitive embedding matrices for the chain:
$$T_{Co} \longrightarrow T_{En} \longrightarrow T_{dP} \longrightarrow \Lambda_{K3}$$

where $\Lambda_{K3} \cong U^3 \oplus E_8(-1)^2$ is the K3 lattice (signature $(3,19)$, rank 22).

**Approach**:

1. Constructed $\Lambda_{K3} = U^3 \oplus E_8(-1)^2$ as block diagonal Gram matrix
2. Embedded $S_{Co} = \langle 2 \rangle \oplus \langle -2 \rangle^{10}$ orthogonally into $\Lambda_{K3}$ using:
   - $U_0$ for $\langle 2 \rangle_S \oplus \langle -2 \rangle_S$ via vectors $(e+f)$ and $(e-f)$
   - $U_1, U_2$ for additional $\langle -2 \rangle$ directions
   - $E_8(-1)^2$ for remaining $\langle -2 \rangle$ directions using orthogonal simple roots
3. Computed $T_{Co} = S_{Co}^\perp$ as the orthogonal complement (kernel of pairing map)
4. Constructed $T_{En} \subset T_{Co}$ (rank 10) and $T_{dP} \subset T_{En}$ (rank 9) as natural sublattices
5. Verified primitivity using Smith normal form

**Results**:

- Embedding matrices:
  - $M_{T_{Co}}: T_{Co} \to \Lambda_{K3}$ is $22 \times 11$
  - $M_{T_{En}}: T_{En} \to \Lambda_{K3}$ is $22 \times 10$
  - $M_{T_{dP}}: T_{dP} \to \Lambda_{K3}$ is $22 \times 9$
- All embeddings verified primitive (Smith normal form has all 1s on diagonal)
- Orthogonality verified: $S_{Co} \perp T_{Co}$ in $\Lambda_{K3}$
- Signatures:
  - $T_{Co}$: signature $-7$ (i.e., $(2,9)$)
  - $T_{En}$: signature $-6$ (i.e., $(2,8)$)
  - $T_{dP}$: signature $-5$ (i.e., $(2,7)$)

**Key Insight**:
The orthogonal complement $T_{Co} = S_{Co}^\perp$ is computed via the kernel of the pairing matrix $M_{S_{Co}}^T \cdot G_{\Lambda_{K3}}$. The resulting basis isn't orthogonal, but the lattice is isometric to the expected $\langle 2 \rangle^2 \oplus \langle -2 \rangle^9$. Primitivity follows from the unimodularity of $\Lambda_{K3}$.

**Tools Developed**:

- `is_primitive_embedding()` function using Smith normal form
- Orthogonal complement computation via kernel of pairing matrix
- Explicit embedding construction for $S_{Co} \hookrightarrow \Lambda_{K3}$ using orthogonal vectors in $U$ factors

**Verification**:

- $S_{Co} \perp T_{Co}$: ✓ Verified (cross-pairing is zero)
- $T_{dP} \to T_{En}$ primitive: ✓
- $T_{En} \to T_{Co}$ primitive: ✓
- $T_{Co} \to \Lambda_{K3}$ primitive: ✓
- $T_{dP} \to \Lambda_{K3}$ primitive: ✓
- Isometry conditions: ✓ All embeddings preserve Gram matrices

**Files**:

- `computations/task1_3_embeddings.sage` - Main computation script
- `computations/task1_3_results.txt` - Output with embedding matrices
- `computations/task1_3_output.txt` - Full computation log

**References**:

- [Nikulin1979] Primitive embeddings of 2-elementary lattices
- [BarthPetersVanDeVen] K3 lattice structure
- [ConwaySloane] $E_8$ root system and orthogonal vectors

**Next Steps**:

- Task 2.1: Enumerate isotropic vectors in $A_{T_{Co}}$ and compute $O(q_T)$-orbits
- Task 2.2: Lift orbits to $T_{Co}$ and verify unique $O^*(T)$-orbit for divisibility 2
