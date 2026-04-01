# Plan for T-0003: Embedding Matrices

## Subtask decomposition

### S1: Construct S_Co embedding into Λ_K3

- S_Co = ⟨2⟩ ⊕ ⟨-2⟩^10, rank 11
- Λ_K3 = U^3 ⊕ E8(-1)^2, rank 22
- Strategy: find 11 orthogonal vectors in Λ_K3 with norms (2, -2, ..., -2)
- The first vector (norm 2) can be taken from the U summands
- The remaining 10 vectors (norm -2) can be taken from the E8(-1)^2 roots

### S2: Construct T_Co embedding as orthogonal complement

- Compute kernel of E_S^T · G_K3 to find the orthogonal complement
- Verify the complement has the correct Gram matrix (isometric to T_Co)
- Extract explicit basis vectors → E_T matrix

### S3: Verification assertions

- E_S^T · G_K3 · E_S = G_{S_Co} (Gram preservation)
- E_T^T · G_K3 · E_T = G_{T_Co} (Gram preservation)
- E_S^T · G_K3 · E_T = 0 (orthogonality)
- Primitivity: coker(E_S) and coker(E_T) are torsion-free (Smith normal form = identity)
- Index: [Λ_K3 : S_Co ⊕ T_Co] = 2^11 = |A_{S_Co}|

### S4: Glue code computation

- Compute explicit isomorphism A_{S_Co} → A_{T_Co}
- Verify q_S = -q_T under this identification

## Execution order

S1 → S2 → S3 → S4 (strictly sequential, each depends on previous)
