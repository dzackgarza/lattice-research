# Coble Moduli Project Goals

## Priority 1 — Centralize canonical literature

- Build a single reference spine for the standard facts the repo keeps reusing:
  - Coble's 10-nodal rational sextic and blowup construction
  - the K3 double cover picture
  - the lattice setup for the hyperplane class and exceptional divisors
  - the period-domain/moduli description and its 9-dimensional count once the lattice is
    fixed
  - the Enriques/Coble moduli and compactification background
- Treat those references as the default justification layer in repo prose.

## Priority 2 — Keep exact numerical evidence aligned with the literature

- Preserve and extend exact Sage evidence for representative sextic examples, isotropic
  orbit computations, stabilizer computations, and related lattice checks.
- For every computational artifact, state which literature-backed claim it is
  supporting, illustrating, stress-testing, or extending.

## Priority 3 — Resolve genuinely open computational blocks

- Replace the disproved Task 5.1 involution route with a mathematically coherent route.
- Use CARAT selectively for finite positive-definite orthogonal-group / normalizer /
  orbit-stabilizer subproblems when that is cleaner than bespoke search code.

## Priority 4 — Formalize only the right statements

- Use Lean/Aristotle for local lemmas or repo-specific arguments once literature and
  computations are stable.
- Avoid formalizing statements that already exist upstream or that should first be cited
  directly from the literature.

## Non-goals for the current reset

- Do not keep re-deriving standard literature facts from scratch.
- Do not start broad new computational searches until the literature spine and plan are
  stable.
- Do not present computational output as if it were the primary justification for known
  background results.
