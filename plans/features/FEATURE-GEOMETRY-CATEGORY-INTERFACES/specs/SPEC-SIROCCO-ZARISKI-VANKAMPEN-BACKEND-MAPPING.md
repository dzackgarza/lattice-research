---
id: SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS]]'
title: Map Sirocco and Sage Zariski-Van Kampen as plane-curve complement group
  backends
status: needs-review
priority: medium
requirement: Record the source-backed boundary for using Sirocco through Sage to
  compute braid monodromy and finitely presented fundamental groups of affine and
  projective plane-curve complements.
acceptanceCriteria:
- Upstream SIROCCO2 README/source and Sage Zariski-Van Kampen docs/source are cited.
- The exact mathematical objects exposed by Sage are named.
- Sirocco root continuation is separated from project-level curve-complement group
  ownership.
- Local availability and limitations are recorded.
complexity: 40
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Sirocco Zariski-Van Kampen Backend Mapping

## Source Scope

- Upstream SIROCCO2 repository:
  <https://github.com/miguelmarco/sirocco2>.
- Temporary upstream checkout inspected at `/tmp/tmp.NCIpabPSo3/SIROCCO2`.
- Upstream files inspected:
  `README.md`, `ZVK.py`, `sage-sirocco_interface.pyx`, and `include/sirocco.h`.
- Sage documentation, Zariski-Van Kampen method:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html>.
- Sage documentation, projective plane curve `fundamental_group()`:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/projective_curve.html>.
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/zariski_vankampen.py`.
- Local import checks:
  `sage -c 'from sage.schemes.curves.zariski_vankampen import fundamental_group, braid_monodromy'`
  succeeded, and `sage.libs.sirocco` resolves to
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/libs/sirocco.cpython-312-x86_64-linux-gnu.so`.

## Backend Boundary

Sirocco is not a curve-complement group library by itself. Its core C/C++ surface
is certified continuation of roots of bivariate complex polynomials along a
one-dimensional parameter path. Upstream exposes `homotopyPath`,
`homotopyPath_mp`, `homotopyPath_comps`, and `homotopyPath_mp_comps`; the Sage
interface exposes corresponding continuation helpers such as `contpath` and
`contpath_mp`.

Sage's `zariski_vankampen.py` is the geometry-facing layer. It uses Sirocco to
follow strands, converts piecewise-linear strands to braids, computes braid
monodromy for plane-curve projections, and converts braid monodromy to finite
presentations of fundamental groups of affine or projective plane-curve
complements.

The project-level public owner should therefore be one of:

- a plane-curve complement object;
- a braid-monodromy object for a chosen plane-curve projection;
- a finitely presented fundamental group object attached to the complement.

It should not be a raw Sirocco wrapper. Sirocco is a backend bridge below the
mathematical owner.

## Candidate Surface Mapping

| Backend surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| SIROCCO2 `homotopyPath*` | backend bridge only | Certified continuation of one root of `f(x,y)` along a parameter segment | Backend evidence; not public geometry vocabulary. |
| Sage `followstrand(f, factors, x0, x1, y0a, prec)` | braid-monodromy computation internals | Piecewise-linear certified path of a root, avoiding roots of optional factors | Internal backend step. |
| Sage `braid_from_piecewise(strands)` | braid group / braid-monodromy object | Braid represented by piecewise-linear strands | Candidate backend utility after braid object ownership exists. |
| Sage `braid_monodromy(f, arrangement=(), vertical=False)` | plane-curve projection braid monodromy | Images of a geometric basis of the complement of the discriminant in `CC` | Candidate public method on plane-curve projection/complement spec. |
| Sage `fundamental_group_from_braid_mon(...)` | finitely presented group from braid monodromy | Zariski-Van Kampen presentation construction | Candidate backend bridge once group/presentation ownership exists. |
| Sage `fundamental_group(f, simplified=True, projective=False, puiseux=True)` | affine or projective plane-curve complement | Presentation of `pi_1` of the curve complement | Candidate public method through a curve-complement spec. |
| Sage plane curve `C.fundamental_group()` | plane curve complement | Presentation of the complement group of `C` | Candidate source evidence for method placement. |

## Mathematical Inputs And Outputs

For `braid_monodromy`, the mathematical input is not an arbitrary curve object:
it is a bivariate polynomial defining a plane curve over `QQ` or a number field
with a fixed complex embedding, together with a chosen projection and optional
arrangement/component data.

The output is braid monodromy of the projection: braids associated to a
geometric basis of loops around the discriminant of the projection, plus
bookkeeping that relates strands to arrangement factors and vertical components.

For `fundamental_group`, the input is a plane affine curve polynomial and flags
selecting affine/projective and Puiseux behavior. The output is a finitely
presented group representing the fundamental group of the complement of the
curve, as computed by Zariski-Van Kampen from braid monodromy.

For projective plane curves, Sage documentation exposes `C.fundamental_group()`
as a curve method requiring `sirocco`; the returned object is still a finite
presentation, not a canonical topological space object.

## Limitations And Audit Requirements

- The backend is restricted to plane-curve complement computations as checked
  here. It is not a general fundamental-group backend for arbitrary varieties,
  manifolds, complements, or higher-dimensional arrangements.
- The polynomial must be over `QQ` or a number field with a complex embedding in
  the Sage route checked here.
- The method depends on projection choices, vertical-component handling,
  discriminant loops, and optional simplification of the resulting presentation.
  Specs must record which data is mathematical output and which data is a
  backend presentation choice.
- A finitely presented group returned by Sage is not automatically a canonical
  group object for equality or isomorphism questions. Later specs need a policy
  for presentations, simplification, meridians, arrangement-factor labeling, and
  comparison.
- Sirocco continuation failures are backend failures, not reasons to change the
  mathematical meaning of the requested group.

## Local Availability Finding

- Searched: `sage -c` imports for `fundamental_group` and `braid_monodromy`;
  `sage -python` import for `sage.libs.sirocco`; installed Sage source path;
  upstream README/source.
- Found: `sage -c` imports succeeded; `sage.libs.sirocco` is installed as a
  compiled extension; a small Sage example for `x^2 + y^3` computed braid
  monodromy `([(s1*s0)^2], {0: 0, 1: 0, 2: 0}, {}, 3)` and a finitely presented
  group `< x0, x1 | x1^-1*x0^-1*x1^-1*x0*x1*x0 >`.
- Conclusion: inference based on the checked local environment: Sirocco is
  available through Sage here and can support future implementation work after
  geometry owner specs are written.
- Confidence: High for local availability of this Sage route.
- Gaps: no package installation test was run; no broad example suite or
  long-running projective/arrangement case was executed.

## Non-Admission Finding

- Searched: upstream SIROCCO2 README/source; Sage Zariski-Van Kampen docs/source;
  local Sage import and one small execution example; existing geometry backend
  mapping specs.
- Found: source-backed support for root continuation, braid monodromy, and
  finite presentations of plane-curve complement groups, but no repo-level
  category owner for plane-curve complements, braid monodromy, finitely presented
  groups with meridians, or presentation comparison policy.
- Conclusion: inference based on the checked sources: create no implementation
  card yet. The mapping is admitted as backend evidence for later geometry
  category specs.
- Confidence: High.
- Gaps: the future geometry category spec still needs to decide method names,
  ownership, presentation semantics, and how this relates to existing Sage curve
  methods.

## Follow-Up Consequence

No new wrapper or dependency-admission task is warranted from this card alone.
Future geometry category specs should decide:

- whether `C.complement().fundamental_group()` or `C.fundamental_group()` is the
  public owner;
- whether braid monodromy is exposed as an intermediate mathematical object;
- how presentations, meridians, arrangements, and vertical components are typed;
- whether projective-complement relations and affine-complement relations live
  on separate complement objects or as flags on one construction.
