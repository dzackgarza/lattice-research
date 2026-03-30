# Current gaps

## Literature / citation gaps

- The stronger Desargues/Thas uniqueness claim is now directly inspectable at the
  secondary-source level via Dolgachev's archived 2016 MPI abstract, while C. Thas, *A
  rational sextic associated with a Desargues configuration* (1994), remains the
  directly inspected primary source for the weaker existence/construction claim.
  The underlying `J. Thas` primary source behind the stronger uniqueness wording remains
  unresolved.
- A literature-backed explicit polynomial family for a 10-nodal rational sextic is still
  not yet verified in-repo at the level of directly inspected full-text formulas.
  The existing Task 1.1 examples should still be treated as repo-native computational
  constructions unless and until a directly inspected source yields explicit equations
  or a comparable full construction record.
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

## Computational bugs

**Task 1.2 T_Co Gram matrix bug**: Computed T_Co has diagonal
`[2, 2, -2, -2, -2, -2, -2, -2, -2, -1, -1]` instead of expected
`[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]`. Determinant is 1024 instead of -2048. Root
cause: likely bug in orthogonal complement computation.
Tracked in BUGS.md.

**Task 1.3 T_Co embedding bug**: Computed T_Co from embedding is non-diagonal and may
not be isometric to correct T_Co. Signature and determinant match but this does NOT
imply isometry for indefinite lattices.
Needs discriminant form verification.
Tracked in BUGS.md.

**Impact**: Most downstream computations (Task 2.1, 2.2, 3.1, 3.2, 6.1) use correct T_Co
from coble_geometry.sage, so bugs are isolated to Task 1.2 and 1.3 scripts only.

## Immediate next targets

- None — all immediate literature and computation-to-literature interface gaps are now
  documented.
