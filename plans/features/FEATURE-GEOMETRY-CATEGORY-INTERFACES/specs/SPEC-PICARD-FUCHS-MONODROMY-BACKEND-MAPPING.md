---
id: SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES]]'
title: Map Picard-Fuchs and Gauss-Manin backends for family monodromy and Jordan
  data
status: needs-review
priority: medium
requirement: Record the mathematically typed backend boundary for computing
  Picard-Fuchs operators, Gauss-Manin systems, local-system monodromy matrices,
  and Jordan normal forms for curve and surface families.
acceptanceCriteria:
- Source scope cites the Noether-Lefschetz `foliation.lib`, Singular Gauss-Manin
  manual, local quarantined foliation notes, Sage Riemann-surface mapping, and
  `ore_algebra` mapping.
- Curve-family and surface-family inputs and outputs are separated.
- Backend responsibilities distinguish geometric Picard-Fuchs derivation from
  operator-level analytic monodromy.
- Local environment gaps and unverified candidate routes are recorded in
  five-field negative-finding format.
complexity: 45
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Picard-Fuchs Monodromy Backend Mapping

## Source Scope

- Noether-Lefschetz code repository:
  <https://github.com/movasati/NoetherLefschetz/tree/master>.
- Temporary Noether-Lefschetz checkout inspected at
  `/tmp/tmp.3NuVp2o61S/NoetherLefschetz`.
- `foliation.lib` procedures inspected in that checkout:
  `gaussmanin`, `gaussmaninvf`, `gaussmaninmatrix`, `PFequ`, `PFeq`, `dbeta`,
  `sysdif`, `HodgeNumber`, `PeriodMatrix`, `DimHodgeCycles`,
  `BasisHodgeCycles`, `IntersectionMatrix`, `Matrixpij`, `TranCoho`,
  `LinearCoho`, and `PeriodLinearCycle`.
- Singular manual, Gauss-Manin connection:
  <https://www.singular.uni-kl.de/Manual/latest/sing_997.htm>.
- Movasati, "Calculation of mixed Hodge structures, Gauss-Manin connections and
  Picard-Fuchs equations":
  <https://w3.impa.br/~hossein/myarticles/saocarlos-2006.pdf>.
- Local theory spec:
  `tests/theory_spec/monodromy_foliation_backend.md`.
- Local backend memory:
  `.agents/memories/theory/backends/foliation-lib-reusable-procedures.md`.
- Quarantined prior implementation and tests:
  `src.bak/backends/foliation_backend.py` and
  `tests.bak/test_foliation_backend.py`.
- Existing geometry backend mappings:
  `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING.md`
  and
  `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-ORE-ALGEBRA-BACKEND-MAPPING.md`.
- Macaulay2 general documentation:
  <https://www.macaulay2.com/> and
  <https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Macaulay2Doc/html/_reading_spthe_spdocumentation.html>.

## Mathematical Boundary

The project should distinguish three mathematical objects:

- A family of varieties `pi: X -> B`, usually restricted here to a
  one-parameter punctured base.
- A cohomology bundle or local system such as `R^i pi_* C` or its algebraic de
  Rham counterpart with the Gauss-Manin connection.
- A scalar Picard-Fuchs operator or first-order Gauss-Manin system that controls
  periods of specified differential forms or cohomology classes.

The Jordan normal form target is not a property of a polynomial alone. It is a
property of a monodromy operator on a chosen local system or solution space, after
choosing a loop in the base and a basis. A backend result is admissible only when
the spec records the family, the cohomological degree, the chosen forms/classes,
the base loop, the basis convention, and whether the output basis is topological,
de Rham/Gauss-Manin, period-solution, numerical, or exact.

## Curve-Family Route

For a family of plane curves `f(x, y, t) = 0`, the public input should be a
mathematical family object with:

- a one-parameter base or punctured parameter domain;
- a curve fiber object or plane model over the appropriate base field;
- the cohomological target, for example `H_1(C_t, ZZ)`, `H^1(C_t)`, holomorphic
  differentials, periods, or a Jacobian/period lattice;
- comparison data between fibers if the output is global family monodromy.

There are two candidate backend routes:

- Sage `RiemannSurface` can compute analytic data for individual plane-curve
  fibers and can support a numerical curve-family monodromy workflow by
  comparing period matrices or homology bases along sampled parameter paths.
  This is a curve analytic backend, not an exact Picard-Fuchs derivation.
- `foliation.lib` can compute Picard-Fuchs equations of Abelian integrals in a
  Brieskorn-module setting. The operator then controls periods of the selected
  form, subject to the hypotheses and basis convention of that computation.

These routes can be complementary, but a spec must not silently identify their
bases or certification levels. A numerical period comparison does not by itself
prove the same statement as an exact Picard-Fuchs operator with a proved
geometric interpretation.

## Surface-Family Route

For a family of surfaces `f(x, y, z, t) = 0`, the useful route is
Gauss-Manin/Picard-Fuchs first, then operator monodromy. The public input should
include:

- the surface family and parameter;
- the cohomology target, typically a piece of `H^2`;
- the selected differential form, algebraic cycle, period, or sub-local system;
- singular parameter values and loops around them;
- the required basis convention for the resulting matrices.

`foliation.lib` provides source evidence for deriving Gauss-Manin connections,
Picard-Fuchs equations, Hodge numbers, period matrices, intersection matrices,
Hodge-cycle spaces, and related Fermat/hypersurface calculations. Its procedures
are specialized computational Hodge theory infrastructure and should be treated
as a candidate Singular bridge, not as generic helper code.

`ore_algebra` can enter after an operator exists. Its operator monodromy routines
can compute monodromy matrices of the solution sheaf around singularities of a
differential operator, but they do not certify that the operator is the correct
Picard-Fuchs operator for the desired geometric local system.

## Candidate Surface Mapping

| Backend surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| Singular `gaussmanin(f, params, diform)` | family de Rham cohomology / Gauss-Manin connection | Connection action on a specified differential form in a Brieskorn module | Backend evidence; owner spec missing. |
| Singular `gaussmaninmatrix(f, params, which)` | Gauss-Manin system object | First-order connection matrices for a basis of `H'` or `H''` | Candidate after family/cohomology spec. |
| Singular `PFequ(f, P, vecfield)` | Picard-Fuchs operator surface | Scalar operator for a chosen form and vector-field direction | Candidate backend; hypotheses and basis must be recorded. |
| Singular `PFeq(f, P, param)` plus `sysdif` | Picard-Fuchs operator surface | Scalar operator derived from a Gauss-Manin system and projection vector | Candidate backend; slower route but useful for audit. |
| Singular `HodgeNumber`, `PeriodMatrix`, `IntersectionMatrix`, Hodge-cycle procedures | Hodge/period/cycle specs | Explicit Fermat/hypersurface Hodge and period computations | Research evidence for later Hodge category specs. |
| `ore_algebra.analytic.monodromy.monodromy_matrices` | differential-equation local system | Monodromy matrices for a known differential operator | Candidate only after an operator exists and environment repair succeeds. |
| Sage `RiemannSurface` period and homology methods | curve analytic/homology/Jacobian specs | Numerical analytic monodromy and period comparison for plane curves | Candidate curve route; separate from surface Picard-Fuchs derivation. |
| Macaulay2 | possible commutative-algebra or period backend | General algebraic-geometry backend candidate | Not admitted in this card; no local command or source-backed PeriodIntegrals route found. |

## Exactness And Review Requirements

- Record the hypotheses under which the family is tame, has isolated
  singularities, or otherwise fits the backend algorithm.
- Record the chosen Brieskorn-module representative and whether the form lives
  in `H'` or `H''`.
- Record the basis of the output matrix/operator. The prior quarantined tests
  show that period/Gauss-Manin bases and integral homology bases must not be
  conflated.
- Treat Jordan normal form as downstream linear algebra on a specified
  monodromy matrix, not as the core backend capability.
- Use source-backed expected values for tests. Internal consistency of a
  generated Picard-Fuchs operator is not a proof oracle.

## Negative And Limited Findings

- Searched: `command -v M2`; `command -v Macaulay2`; Macaulay2 home page; Macaulay2
  documentation-reading page; web searches for `Macaulay2 PeriodIntegrals
  Picard-Fuchs` and `PeriodIntegrals Macaulay2 Picard`.
- Found: no local `M2` or `Macaulay2` command in this environment; general
  Macaulay2 documentation describes an algebraic-geometry and commutative-algebra
  system, but the checked sources did not expose a source-backed
  `PeriodIntegrals` Picard-Fuchs route.
- Conclusion: inference based on the checked sources: Macaulay2 should remain a
  possible future backend-research target, but it is not admitted as the
  preferred Picard-Fuchs route by this card.
- Confidence: Medium.
- Gaps: Macaulay2 was not installed or searched through an in-session help index;
  the full Macaulay2 package repository was not cloned and searched locally.

- Searched: local quarantined `src.bak/backends/foliation_backend.py`, quarantined
  `tests.bak/test_foliation_backend.py`, and
  `tests/theory_spec/monodromy_foliation_backend.md`.
- Found: prior code attempts to combine Singular `foliation.lib` and
  `ore_algebra`; the theory spec explicitly warns that several assertions were
  internal consistency checks or basis-dependent statements lacking literature
  grounding.
- Conclusion: inference based on the checked local artifacts: quarantined code is
  useful source evidence for future implementation shape, but cannot be
  resurrected without source-grounded expected values and basis conventions.
- Confidence: High.
- Gaps: Movasati book, Griffiths, Brieskorn, and SGA 7 references named in the
  theory spec were not acquired or extracted in this card.

- Searched: Noether-Lefschetz checkout `README.md` and `foliation.lib`, Singular
  manual Gauss-Manin page, and Movasati 2006 article.
- Found: strong evidence for algorithms computing Gauss-Manin iterations,
  Picard-Fuchs equations of Abelian integrals, mixed Hodge data, spectra,
  monodromy, and Hodge-cycle-related Fermat/hypersurface computations.
- Conclusion: inference based on the checked sources: Singular/Movasati is the
  best current candidate for geometric Picard-Fuchs derivation, subject to
  source-grounded hypotheses and basis documentation.
- Confidence: High for candidate-backend status; Medium for exact project API
  shape because family/cohomology owner specs are not written yet.
- Gaps: no implementation or execution of `foliation.lib` was attempted; no
  theorem-level proof audit of the algorithms was performed.

## Follow-Up Consequence

No implementation task is admitted directly from this mapping. The next durable
work should be geometry category specs for families, cohomology/local systems,
Gauss-Manin connections, Picard-Fuchs operators, period maps, and monodromy
operators. After those owners exist, implementation cards can decide whether to:

- bridge Singular `foliation.lib` for geometric Picard-Fuchs derivation;
- repair and admit `ore_algebra` for operator-level monodromy;
- use Sage `RiemannSurface` for numerical curve-family analytic monodromy; or
- reopen Macaulay2 package/source research if a concrete PeriodIntegrals-style
  route is found.
