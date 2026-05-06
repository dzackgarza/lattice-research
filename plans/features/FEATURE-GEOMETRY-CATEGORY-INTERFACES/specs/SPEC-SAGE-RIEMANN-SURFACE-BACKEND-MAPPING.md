---
id: SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]'
title: Map Sage RiemannSurface as an analytic curve backend, not a raw wrapper target
status: needs-review
priority: medium
requirement: Record how Sage `RiemannSurface` functionality should inform future curve,
  Jacobian, Abel-Jacobi, period, and monodromy category specs before any public wrapper
  or backend bridge is implemented.
acceptanceCriteria:
- Constructor and method surfaces cite Sage documentation and installed source paths.
- Public project owners are stated as mathematical nouns rather than Sage helper names.
- Numerical/certified-homotopy limitations are explicit.
- Implementation work remains blocked until curve/Jacobian/family ownership is specified
  in a later geometry category spec.
complexity: 45
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Sage RiemannSurface Backend Mapping

## Source Scope

- Sage documentation: <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html>.
- Installed Sage source: `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`.
- Installed curve entry points:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/affine_curve.py`
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/projective_curve.py`.
- Local backend memory: `theory-graph-monodromy-hodge-methods`, which records that
  Sage Riemann-surface chaining is a candidate route for one-parameter curve-family
  monodromy.

## Backend Boundary

Sage `RiemannSurface(f, prec=53, certification=True, differentials=None,
integration_method='rigorous')` models the compact analytic Riemann surface determined
by a bivariate plane-curve equation `f(z,w)=0` over a subfield of the complex numbers.
The surface is interpreted as a covering of the coordinate plane in the first variable.
The constructor is therefore not a general project constructor for all curves or all
schemes. It is a backend route for plane-curve analytic data after the project has a
curve object, a chosen plane model/projection, and a complex embedding.

The public project noun should be an analytic curve/Riemann-surface refinement attached
to a curve, not a raw `RiemannSurface` wrapper. The existing Sage entry points
`AffineCurve.riemann_surface(**kwargs)` and `ProjectivePlaneCurve.riemann_surface(**kwargs)`
are source evidence for a future method such as `C.analytic_riemann_surface(...)` on
the appropriate complex curve category. The exact method name and owner should be
settled with the future geometry category spec.

## Candidate Surface Mapping

| Sage surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| `RiemannSurface(f, prec, certification, differentials, integration_method)` | backend constructor behind a curve method | Analytic surface of a plane algebraic curve with projection to the first coordinate | Backend evidence only; not public API. |
| `C.riemann_surface(**kwargs)` | complex plane curve or smooth projective curve refinement | Construct analytic Riemann-surface data from a curve model | Candidate future method after curve-category ownership exists. |
| `monodromy_group()` | branched cover or plane-curve projection data | Local monodromy permutations around finite branch points and infinity | Backend evidence for curve-cover monodromy, not fundamental-group output. |
| `homology_basis()` | topological homology of compact Riemann surface | Homology cycles represented by lifted graph paths | Candidate backend for `H_1(X, ZZ)` once homology objects exist. |
| `cohomology_basis()` | holomorphic differentials on a smooth curve | Basis of regular differentials represented by `g/(df/dw) dz`; uses Singular unless user supplies differentials | Candidate backend for `H^0(X, Omega^1)` with explicit backend caveat. |
| `period_matrix()` / `riemann_matrix()` | Jacobian or period-lattice surface | Numerical period/Riemann matrices from a symplectic homology basis | Candidate backend for Jacobian/period data; not exact proof data by itself. |
| `endomorphism_basis()` / `homomorphism_basis()` | Jacobian/period-lattice morphisms | Numerical integer near-solutions for endomorphism or homomorphism lattices | Research evidence only until exactness/proof criteria are specified. |
| `symplectic_isomorphisms()` / `symplectic_automorphism_group()` | Jacobian isomorphism or automorphism surface | Numerical symplectic isomorphisms between Jacobians/period lattices | Research evidence only; requires proof/audit policy before use. |
| `abel_jacobi(...)`, `divisor_to_divisor_list(...)`, `reduce_over_period_lattice(...)` | Abel-Jacobi map from divisors to a Jacobian/period torus | Numerical Abel-Jacobi representatives modulo the period lattice | Candidate backend after divisor and Jacobian categories exist. |
| `downstairs_graph()`, `upstairs_graph()`, `edge_permutations()` | backend graph/interoperability data | Voronoi and lifted graph data used to compute homology and monodromy | Interop evidence; not public geometry vocabulary. |

## Limitations And Audit Requirements

- The backend is numerical. The documentation and source describe certified homotopy
  continuation and rigorous integration options, but period matrices, endomorphism
  bases, homomorphism bases, and Abel-Jacobi values are still numerical artifacts that
  need explicit certification or proof-audit criteria before being used as exact
  mathematical evidence.
- `cohomology_basis()` currently calls Singular `adjointIdeal` for regular
  differentials unless `differentials` are supplied. The source notes that user-supplied
  differentials make the computation independent from Singular and are required in
  examples over number fields with complex embeddings.
- `monodromy_group()` returns permutations for the chosen plane projection and branch
  locus. It should not be confused with the fundamental group of a curve complement or
  with global family monodromy on cohomology.
- Wrapper work is premature until geometry specs define curve, analytic surface,
  divisor, Jacobian, period lattice, homology, and family-monodromy owners.

## Follow-Up Consequence

The next durable work should be a geometry category spec for curve/Jacobian/period-lattice
ownership. That later spec can consume this mapping and decide whether
`C.analytic_riemann_surface(...)`, `C.period_matrix(...)`,
`C.jacobian().period_lattice(...)`, or a different public surface best expresses the
mathematics.

## Non-Admission Finding

- Searched: Sage documentation page linked above; installed source file
  `sage/schemes/riemann_surfaces/riemann_surface.py`; installed curve entry points
  `sage/schemes/curves/affine_curve.py` and
  `sage/schemes/curves/projective_curve.py`; local memory
  `theory-graph-monodromy-hodge-methods`.
- Found: Sage exposes a rich numerical analytic backend, but the checked sources do
  not define the project-level owners for curve analytic refinements, Jacobians,
  period lattices, Abel-Jacobi maps, homology objects, or family monodromy.
- Conclusion: inference based on the checked sources: no implementation card is
  admitted from this pass; wrapper implementation should wait for those geometry
  owner specs rather than exposing raw Sage helper names.
- Confidence: High for this source-admission card's scope.
- Gaps: broader geometry category specs, Sage Jacobian docs, and family-monodromy
  backend cards remain to be researched separately.
