---
id: SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
- '[[SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE]]'
title: Recover Vinberg algorithm input and enumeration contract
status: needs-review
priority: medium
requirement: Vinberg algorithm recovery must specify exact typed inputs, root enumeration
  semantics, backend ownership, integrality checks, and termination evidence.
acceptanceCriteria:
- Inputs are a hyperbolic lattice, control vector or chamber seed, root predicate,
  and exact backend route.
- Root candidates are lattice elements satisfying sourced norm, angle, integrality,
  and chamber constraints.
- Enumeration states whether it is complete for the reported distance shell or chamber
  and records the backend/theorem that proves completeness.
- Number-field and rational/integral coordinate systems are explicit when a backend
  diagonalizes over a fraction field.
complexity: 90
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Recover Vinberg algorithm input and enumeration contract

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md`
  and docs: Julia/Hecke implementation, number-field support, root iteration.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/README.md`: Sage
  implementation route and examples.
- `src.bak/backends/external/vinbergs_algorithm/references/AlVin/README.md`: C++
  reference implementation pointer.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/vinbergs_algo.jl`:
  distance ordering, diagonal-coordinate search, integrality checks, and partial
  continuation state.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/quad_forms.jl`:
  root-length and integral-root predicates in the Julia/Hecke route.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/docs/vin-alg-pseudocode-old.txt`
  and `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/vinal.py`:
  Sage route through original lattice coordinates and positive-definite equations in
  the control-vector orthogonal complement.
- `.agents/memories/theory/backends/vinberg-algorithm.md`: integrality checks,
  diagonal-coordinate versus original-coordinate enumeration, reference examples, and
  positive-definite subproblem notes.
- `.agents/memories/theory-backend-routing.md` and
  `.agents/memories/theory/backends/library-integration.md`: repo backend route says
  `Lattice.vinberg_*()` uses Oscar `vinberg_algorithm` or a verified Vinberg backend,
  not ad hoc enumeration.
- `theory/foundations/reflective-two-elementary-lattices.md`: definitions of root,
  reflection, reflection group, Coxeter diagram, parabolic diagram, fundamental
  polyhedron, Lanner subgraph, and Vinberg's algorithm.
- `.agents/skills/vinberg-algorithm/SKILL.md`: local workflow trigger.

## Mathematical Objects

The public target is the reflection group `W(L)` of a hyperbolic lattice `L`, generated
by reflections in roots of `L`. A control vector or chamber seed chooses the Weyl
chamber returned by the algorithm; it does not define a different group.

For this spec, a root is a non-isotropic lattice element `v in L` such that the
reflection

```text
s_v(x) = x - (2 * b(x, v) / b(v, v)) * v
```

preserves `L`. Equivalently, the integrality condition
`2 * b(x, v) / b(v, v) in ZZ` must hold for every `x in L`. Norm-and-divisibility
shortcuts such as `v^2 = -2`, or `v^2 = -4` with divisibility `2`, are theorem-backed
specializations for even two-elementary lattices; they are not the general definition of
root.

## Public Contract

The recovered Vinberg surface is owned by the lattice/reflection-group layer, with a
compatibility spelling such as `L.vinberg_*()` only if it delegates to the semantic
reflection-group operation. Inputs are:

- a typed hyperbolic lattice or formed module whose form, signature convention, basis,
  base ring, and exact coordinate system are recorded;
- a control vector or chamber seed in the positive/timelike cone, with the sign
  convention stated by the lattice form;
- a root predicate, including root-length restrictions only when they are source-backed
  for the category of `L`;
- an exact backend route and any backend-specific coordinate transform.

The result is a typed Vinberg search result. It records:

- `lattice`: the parent lattice;
- `reflection_group`: the target `W(L)` or requested reflection subgroup;
- `control_vector`: the chamber seed actually used;
- `root_predicate`: the sourced predicate used to admit roots;
- `roots`: simple-root candidates as elements of `L`, not raw coordinate rows;
- `reflections`: elements of `L.Aut()` induced by the roots;
- `ordering`: exact distance or shell ordering used by the backend;
- `backend`: the exact route, version/source, and limitations;
- `coordinate_maps`: original lattice coordinates, diagonal/number-field coordinates if
  used, and the proof that converted candidates lie in `L`;
- `search_state`: enough continuation state to resume a partial backend search;
- `completeness_status`: one of partial-prefix, shell-complete, chamber-complete,
  nonreflective/does-not-terminate with evidence, or unsupported;
- `termination_evidence`: backend certificate or theorem branch proving the reported
  completeness status.

Docstrings defining public Vinberg surfaces must mention the global diagnostic flag for
surprise logging. When the flag is enabled, returning a partial prefix, changing
coordinate systems over a fraction field, applying a special root-length theorem, or
detecting an unsupported termination branch should log the precise condition and tell
the user which mathematical object was returned.

## Backend Routing

Preferred route: Oscar/Hecke `vinberg_algorithm` when its documented domain supports
the input lattice and requested root predicate.

Candidate audited backends:

- VinbergsAlgorithmNF: Julia/Hecke number-field route. It may diagonalize over a field
  of fractions or number field, enumerate in diagonal coordinates, then check that each
  candidate converts back to integral canonical lattice coordinates.
- VinAl/vinal: Sage route that works in original lattice coordinates and reduces root
  search to positive-definite equations in the orthogonal complement of the control
  vector.
- AlVin: C++ reference/candidate route for rational, quadratic, and selected cyclotomic
  coefficient settings, pending a bridge audit.
- Normaliz, polymake, LattE, 4ti2, Sage, and related polyhedral libraries are only
  candidate owners for bounded cone or Hilbert-basis subproblems, not replacements for
  Vinberg termination proofs.

If none of these routes supports the requested input, the implementation task must
create a backend-gap card with the exact lattice category, coefficient ring, root
predicate, termination need, and candidate software checked. It must not begin a local
bespoke enumeration by default.

## Enumeration and Evidence

If a backend diagonalizes over a field of fractions or number field, the bridge must
record:

- the original lattice basis and form;
- the diagonal or backend coordinate system;
- the transformation maps in both directions;
- the ring in which coordinates are allowed;
- the integrality check proving a candidate is an element of `L`;
- the exact distance or shell key used to sort candidates.

Root candidates are admitted only after checking all active obligations: membership in
`L`, the root predicate, chamber-side inequality with the control vector, acute-angle
inequalities with previously accepted simple roots, and any backend-specific
coordinate-integrality condition.

Completeness claims must be tied to the backend algorithm or a stated theorem branch.
A finite window, fixed number of roots, timeout, or diagram shape alone is not
evidence of chamber completeness. A bounded prefix is useful only as a partial search
state.

## Non-Preservation Boundaries

- Do not hand-roll root enumeration before checking Oscar, VinbergsAlgorithmNF, AlVin,
  VinAl, Sage, Normaliz, and polyhedral backends.
- Do not hide the coordinate system used by the backend.
- Do not return raw vectors without parent lattice and root predicate evidence.
- Do not call a finite prefix of roots a fundamental domain unless the termination
  criterion is satisfied.
- Do not treat special two-elementary root classifications as the definition of root in
  arbitrary lattices.
- Do not treat the control vector as changing the reflection group; it selects the
  chamber for `W(L)`.
- Do not present a Coxeter diagram match, plotted polyhedron, or copied reference
  output as a certificate unless the typed roots, reflections, and chamber evidence are
  verified.

## Acceptance Criteria

- [x] Inputs and root predicates are typed and source-grounded.
- [x] Candidate enumeration records integrality and completeness evidence.
- [x] Backend routes are documented with exact domains and limitations.
- [x] The result object distinguishes partial search state from complete chamber data.
