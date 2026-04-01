# Task T-0003: Embedding Matrices (GOAL.md Task 1.3)

## Origin

GOAL.md Task 1.3: "Compute explicit embedding matrices for $S_{Co} \hookrightarrow
\Lambda_{K3}$ and $T_{Co} \hookrightarrow \Lambda_{K3}$."

## Objective

Compute explicit matrices representing the primitive embeddings of $S_{Co}$ and $T_{Co}$
into the K3 lattice $\Lambda_{K3} = U^3 \oplus E_8(-1)^2$, and verify:
- The embeddings are primitive (no torsion in the quotient)
- $S_{Co} \oplus T_{Co}$ has finite index in $\Lambda_{K3}$
- The discriminant glue between $S_{Co}$ and $T_{Co}$ is correctly identified

## Deliverable type

Exact computation with certificate.

## Acceptance criteria

1. Explicit $22 \times 11$ embedding matrix $E_S: S_{Co} \to \Lambda_{K3}$ computed
2. Explicit $22 \times 11$ embedding matrix $E_T: T_{Co} \to \Lambda_{K3}$ computed
3. Primitivity verified: $\Lambda_{K3} / \text{im}(E_S)$ and $\Lambda_{K3} /
   \text{im}(E_T)$ are torsion-free
4. Orthogonality verified: $E_S^T G_{K3} E_T = 0$ (the images are orthogonal)
5. Index computation: $[\Lambda_{K3} : S_{Co} \oplus T_{Co}] = 2^{11}$ (from
   discriminant group size)
6. Glue code: explicit isomorphism $A_{S_{Co}} \cong A_{T_{Co}}$ identifying $q_S =
   -q_T$

## Non-goals

- Computing automorphism group actions on embeddings (Task 2.2)
- Enumerating isotropic vectors (Task 2.1)
- Computing Coble surface equations (Task 1.1)

## Allowed dependencies

- `coble_geometry_foundation.sage` for lattice constructors
- SageMath for lattice computations
- Nikulin's primitive embedding theorems (literature)
- T-0001 results (Gram matrices and invariants)

## Required conventions

- $\Lambda_{K3} = U^3 \oplus E_8(-1)^2$ in the standard basis from `Lambda_K3_lattice()`
- $S_{Co} = \langle 2 \rangle \oplus \langle -2 \rangle^{10}$ from `S_Co_lattice()`
- $T_{Co}$ from `T_Co_lattice()` (rank 11, signature (2,9))
- Embedding matrices expressed in the standard bases of domain and codomain

## Failure conditions

- Embedding not primitive (quotient has torsion)
- Orthogonality condition fails
- Index computation doesn't match $|A_{S_{Co}}| = 2^{11}$
- Glue isomorphism doesn't satisfy $q_S = -q_T$
