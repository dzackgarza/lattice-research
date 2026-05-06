---
id: SPEC-HISTORICAL-FAMILY-MONODROMY-BACKEND-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE]]'
title: Recover family, Picard-Fuchs, and monodromy backend surface
status: needs-review
priority: medium
requirement: Historical family and foliation backend code must be recovered as a source-admitted
  monodromy interface for one-parameter hypersurface families.
acceptanceCriteria:
- A family object exposes fibers, specialization, and a unique hypersurface equation
  only under explicit hypotheses.
- Picard-Fuchs, indicial polynomial, Milnor number, semisimple and nilpotent monodromy,
  and Jordan data have typed result objects.
- Singular/Ore algebra backend calls are isolated behind a backend contract with exact
  input and output validation.
- Monodromy outputs are not used as Coble evidence until connected to the relevant
  family and source theorem.
complexity: 75
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover family, Picard-Fuchs, and monodromy backend surface

## Source Provenance

- `src.bak/varieties/varieties.py`: `FamilyOfVarieties`,
  `hypersurface_family_equation`, `hodge_theoretic_monodromy`,
  `picard_fuchs_operator`, `indicial_polynomial`, `monodromy_matrix`, and
  nilpotent monodromy methods.
- `src.bak/backends/foliation_backend.py`: `HodgeTheoreticMonodromy`,
  Picard-Fuchs operator construction, indicial polynomial, Jordan blocks, and monodromy
  matrices.
- `.agents/memories/theory-graph-monodromy-hodge-methods.md`: stored monodromy,
  Riemann-surface, Picard-Fuchs, and foliation/Hodge backend guidance.
- `.agents/memories/theory/backends/foliation-lib-reusable-procedures.md`: reusable
  `foliation.lib` procedure families, especially Gauss-Manin and Picard-Fuchs
  procedures.
- `.agents/memories/theory-backend-routing.md`: family, Picard-Fuchs, and monodromy
  backend owner routes.
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md`

## Contract

The recovered family surface applies to a family with explicit base, total space, and
fiber operation. A one-parameter hypersurface helper is valid only when the base is a
curve and the total space has exactly one defining equation.

Monodromy output must be a typed result object containing the Picard-Fuchs operator,
indicial polynomial, Milnor number, logarithmic Jordan data, semisimple part,
nilpotent part, and monodromy matrices. Backend calls to Singular, Ore algebra, or
related exact systems are implementation details behind this object.

## Family Surface

`FamilyOfVarieties` is a morphism `f: X -> S` with total space `X`, base `S`, and typed
fiber operation. The family object must record the hypotheses under which its fibers
are varieties of the intended category, such as flatness, base dimension, smooth locus,
singular fibers, and any compactification or boundary model.

The one-parameter hypersurface shortcut is admitted only when:

- `S` is a curve or a selected one-parameter base;
- `X` is a presented hypersurface over `S`;
- exactly one defining equation is selected;
- the parameter and spatial variables are identified by a source-backed convention;
- the coefficient field and characteristic are recorded.

For any other family, the shortcut is unavailable. A backend can still be researched,
but it must not silently squeeze a multi-parameter or non-hypersurface family into the
old helper shape.

## Typed Result Objects

The recovered public result is a `HodgeTheoreticMonodromy`-type object, but with
mathematical provenance rather than hidden mutable cache state. It must record:

- the source family and parameter/basepoint;
- the chosen loop or degeneration point when a monodromy matrix is computed;
- Picard-Fuchs differential operator, with coefficient ring and operator algebra;
- indicial polynomial and the point at which it is taken;
- Milnor number or rank/dimension invariant, with source/backend evidence;
- logarithmic Jordan form and its basis;
- semisimple and nilpotent logarithmic parts;
- semisimple, unipotent, nilpotent, and total monodromy matrices;
- Jordan blocks with exponents, eigenvalues, and block sizes;
- backend route, version/source, and validation checks;
- exactness status: exact symbolic, algebraic-number exact, certified numerical, or
  unsupported.

Docstrings must mention the global diagnostic flag where users may be surprised. With
diagnostics enabled, implementations should warn when matrices are in a logarithmic
Jordan basis rather than a geometric homology/cohomology basis, when symbolic complex
exponentials are used instead of an exact algebraic-number representation, when a
regular-singular assumption is being checked only by backend output, or when a result
is backend-cached but not recomputed.

## Backend Routes And Limits

Candidate routes:

- Singular `foliation.lib`: high-value reusable procedures include `gaussmanin`,
  `gaussmaninvf`, `gaussmaninmatrix`, `PFequ`, `PFeq`, `sysdif`, and `dbeta`; trivial
  helpers such as monomial list builders are not public API.
- `ore_algebra`: candidate owner for Ore/differential-operator objects and indicial
  polynomial operations once the interface research card admits the dependency.
- Sage Riemann-surface tools: candidate route for one-parameter curve-family monodromy
  by analytic continuation of period data; this is not automatically a surface/K3
  route.
- Macaulay2 `PeriodIntegrals`, Singular Gauss-Manin tools, and literature-tabulated
  Picard-Fuchs equations remain candidate routes for hypersurface and surface-family
  Picard-Fuchs computation.

The old backend uses `PFequ`, then builds an Ore operator and derives Jordan data from
an indicial polynomial. This is only a candidate path. Future implementation cards must
explain what theorem connects that operator and indicial data to the desired monodromy
representation for the specific family.

## Verification Contract

Implementation or fixture cards consuming this spec must verify:

- family hypotheses before calling the hypersurface shortcut;
- the backend input polynomial, parameter, spatial variables, term order, and weights;
- that the Picard-Fuchs coefficient list has the expected length for the rank/Milnor
  number used;
- that the indicial polynomial is taken at the claimed degeneration point;
- whether the singularity is regular enough for the Jordan extraction being used;
- that monodromy matrices are expressed over the declared ring/field and basis;
- that any numerical or symbolic transcendental step is marked as such and not treated
  as an exact algebraic proof.

Monodromy outputs are not Coble evidence until a downstream card names the family, map,
degeneration, theorem, and object whose monodromy is being used.

## Non-Preservation Boundaries

- Do not cache monodromy data as mutable hidden state without a reproducible backend
  contract.
- Do not use symbolic complex exponentials as exact proof without a stated coefficient
  field and normalization.
- Do not apply the hypersurface-family shortcut to non-hypersurface or multi-parameter
  families.
- Do not use monodromy data as a substitute for the geometric construction that
  defines the family.
- Do not preserve the old `getattr`/hidden-cache pattern as public semantics; caching
  is an implementation detail and must not change the mathematical result object.
- Do not treat `degree(indicial_polynomial) == milnor_number` as a complete proof of
  the regular-singular or monodromy hypotheses without the theorem/backend certificate
  that makes the check adequate.

## Acceptance Criteria

- [x] Family hypotheses are explicit before monodromy methods apply.
- [x] Picard-Fuchs and monodromy outputs are typed and reproducible.
- [x] Backend calls are isolated and validated.
- [x] Downstream geometry or Coble use records the map from the family to the claim.
