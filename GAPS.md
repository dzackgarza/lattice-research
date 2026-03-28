# Current audit gaps

## Highest-priority mathematical gaps

- **Task 1.1 still needs a publication-grade explanation, not new computation.** Current
  artifacts now prove degree-6 extraction, irreducibility over `QQ`,
  reducedness/squarefreeness, 10 node coordinates, and generic injectivity of the
  parametrization for all three sextic examples.
  The remaining gap is to write down a clean mathematical explanation that cites these
  computations and states explicitly why generic fiber degree 1 gives birationality onto
  the sextic image.
- **The `GOAL.md` 9-dimensional moduli claim is not yet settled in-repo.** The claim
  appears in project prose, but no repo-local derivation or citation currently pins down
  the dimension count.
- **Task 5.1 remains mathematically blocked.** The rerun log in
  `audit/task5_1_rerun_20260327T122004Z.txt` shows `θ^T G θ = G: False`,
  `G θ = θ^T G: False`, and `V_+ ⟂ V_-: False`, so the current involution construction
  does not define an isometry of `Λ_K3`.

## Delegation / formalization gaps

- **Aristotle support-lemma work is progressing, but the full node criterion is still
  untrusted.** Completed artifacts have produced useful Hessian support lemmas, but one
  artifact still packaged nodehood tautologically and another returned an unfinished
  proof file despite a positive summary.

## Immediate next targets

- Recover a repo-grounded derivation or authoritative citation for the moduli-dimension
  claim.
- Turn the new Task 1.1 birationality computation into a concise evidence note or audit
  citation, so the rationality claim is easy to reuse downstream.
- Turn the Task 1.1 exact-coordinate machinery into a short reusable audit note, so the
  repo cites the exact `QQbar.polynomial_root(..., isolating_interval(...))` output
  route instead of rediscovering it from code.
- Replace the current Task 5.1 non-orthogonal-basis construction with a route grounded
  in orthogonal complements or another genuine lattice isometry construction.
- Use the CARAT capability audit in `audit/carat_capability_audit.md` to test whether
  `Aut_grp`, `Normalizer`, or `Orbit` can take over finite positive-definite
  orthogonal-group / stabilizer subproblems before adding more custom lattice-search
  code.
