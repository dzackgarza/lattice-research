# Current gaps

## Literature / citation gaps

- C. Thas (1994) has been acquired in local machine-parseable form
  (`papers/extracted/thas_1994.md`, 757 lines).
  The paper provides explicit rational parametric equations for a 10-nodal sextic
  associated with a Desargues configuration (Section 3, Main Theorem).
  The parametric representation is given as rational functions in a parameter t with
  coefficients depending on three parameters a, b, c. **Comparison complete**: The
  repo's three Task 1.1 examples are INDEPENDENT constructions from Thas (1994). Thas
  uses degree patterns (6, 5, 5) with geometric parameters (a, b, c) encoding Desargues
  configuration; repo uses fixed integer coefficients with degree-6 in all three
  coordinates. See `audit/thas_vs_task1_1_comparison.md` for details.
  **Gap**: The repo's independent sextic constructions could still be connected to other
  literature sources (e.g., Coble 1917, Coolidge) or verified against additional primary
  sources.
- The stronger Desargues/Thas uniqueness claim is now directly inspectable at the
  secondary-source level via Dolgachev's archived 2016 MPI abstract, while C. Thas
  (1994) remains the directly inspected primary source for the weaker
  existence/construction claim.
  The underlying `J. Thas` primary source behind the stronger uniqueness wording remains
  unresolved.
- The repo's Task 1.1 examples are confirmed independent from Thas (1994) but still lack
  connection to other literature sources.
  They should continue to be treated as repo-native computational constructions unless
  connected to additional literature.
- Coolidge has now been directly inspected for the classical nine-/ten-node discussion,
  but the stronger all-ten-from-any-nine theorem wording quoted via MathOverflow still
  needs a cleaner primary-text extraction before the repo should cite it in that form.

## Computation-to-literature interface gaps

- Task 1.1 now has `audit/task1_1_birationality_note.md` and
  `audit/task1_1_exact_coordinate_note.md` documenting the exact computation path.

## Genuine mathematical / implementation gaps

- The old Task 5.1 involution construction failed, but the current exact script now
  replaces it with a verified glued-model route: primitive `S_Co \hookrightarrow Λ_K3`,
  true orthogonal complement, and a sign involution that is integral and satisfies
  `θ ∈ O(Λ_K3)` on that explicit ambient lattice model.
- The remaining Task 5.1 gap is no longer raw existence of `θ`; it is to keep longer
  prose and literature-facing claims consistent with
  `audit/task5_1_exact_involution_note.md` without overclaiming beyond the verified
  glued model.
- `audit/task5_1_route_reset.md` remains canonical for the route order: primitive
  embedding and orthogonal complement first, involution only afterward; CARAT remains
  auxiliary only on finite positive-definite subproblems.
- Lean formalization remains secondary until the literature spine and blocked
  computations are stabilized.

## Computational bugs (resolved 2026-03-30)

**Task 1.2 T_Co Gram matrix bug**: FIXED. Changed embedding construction in
`task1_2_gram_matrices_fixed.sage` to use single coordinates instead of pairs.
T_Co Gram diagonal now correct `[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]` with
determinant -2048. See BUGS.md for details.

**Task 1.3 T_Co embedding**: NOT A BUG. Discriminant form verification confirmed
computed T_Co has correct discriminant form.
Non-diagonal Gram matrix is different basis representation of same lattice.
See BUGS.md for details.

## Immediate next targets

- None — all immediate literature and computation-to-literature interface gaps are now
  documented.
