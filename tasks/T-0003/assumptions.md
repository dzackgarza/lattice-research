# Mathematical Assumptions for Task T-0003

## Objects

- $S_{\mathrm{Co}}$: Coble lattice, rank 11, signature (1,10), Gram = diag(2, -2, ...,
  -2)
- $T_{\mathrm{Co}}$: Transcendental lattice, rank 11, signature (2,9)
- $\Lambda_{\mathrm{K3}}$: Standard K3 lattice, rank 22, signature (3,19), unimodular
- $E_S$: $22 \times 11$ embedding matrix for $S_{Co} \hookrightarrow \Lambda_{K3}$
- $E_T$: $22 \times 11$ embedding matrix for $T_{Co} \hookrightarrow \Lambda_{K3}$

## Definitions

- Primitive embedding: an embedding $\iota: L \hookrightarrow M$ is primitive if
  $M/\iota(L)$ is torsion-free
- Orthogonal complement: for $S \subset \Lambda_{K3}$, $S^\perp = \{x \in \Lambda_{K3} :
  \langle x, s \rangle = 0 \ \forall s \in S\}$
- Glue code: the identification of $A_S \cong A_T$ via $q_S = -q_T$ that determines how
  $S \oplus T$ sits inside $\Lambda_{K3}$

## Conventions

- All computations exact (rational/integer arithmetic)
- Embedding matrices expressed in standard bases from `coble_geometry_foundation.sage`
- $E_S^T G_{K3} E_S = G_{S_{Co}}$ (Gram matrix preserved)
- $E_T^T G_{K3} E_T = G_{T_{Co}}$ (Gram matrix preserved)
- $E_S^T G_{K3} E_T = 0$ (orthogonality)

## Expected Results

- $[\Lambda_{K3} : S_{Co} \oplus T_{Co}] = |A_{S_{Co}}| = 2^{11}$
- The glue isomorphism $A_{S_{Co}} \to A_{T_{Co}}$ is an anti-isometry

## References

- Nikulin, V. V. "Integral symmetric bilinear forms and their applications."
  Math. USSR-Izv. 14 (1980)
- T-0001 results: verified Gram matrices and invariants
- Task 1.3 in GOAL.md provides target specification
