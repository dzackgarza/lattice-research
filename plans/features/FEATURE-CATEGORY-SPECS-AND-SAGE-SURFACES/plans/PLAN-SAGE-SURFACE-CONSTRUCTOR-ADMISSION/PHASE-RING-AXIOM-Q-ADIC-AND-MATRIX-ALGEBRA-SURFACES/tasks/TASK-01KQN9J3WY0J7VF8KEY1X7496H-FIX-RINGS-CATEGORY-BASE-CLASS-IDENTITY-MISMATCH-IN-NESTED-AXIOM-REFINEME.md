---
id: TASK-01KQN9J3WY0J7VF8KEY1X7496H-FIX-RINGS-CATEGORY-BASE-CLASS-IDENTITY-MISMATCH-IN-NESTED-AXIOM-REFINEME
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Fix Rings category base-class identity mismatch in nested axiom refinement
status: needs-review
priority: high
description: 'The deleted Rings triage recorded ring smoke blockers: nested axiom category
  identity mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
  split.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken smokes
  or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with exact
  failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only
  categories.
- Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- Confirm failures are reduced without weakening constructor membership assertions.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
- category-specs
- rings
- theme-constructor-routing
---
# Fix Rings category base-class identity mismatch in nested axiom refinement
## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- `plans/category_specs/rings/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Fix Rings category base-class identity mismatch in nested axiom refinement from category_specs/rings/docs/TRIAGE.md`

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix smoke must not be moved or weakened to hide the surface split.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- [x] Confirm failures are reduced without weakening constructor membership assertions.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Replaced the `_base_category_class_and_axiom` parent entries that
  were module-local `LazyImport` placeholders with eager imports of the resolved
  parent category classes. This was applied only to nested ring axiom categories:
  fields, integral domains, number/global/local/finite/algebraically closed fields,
  PID/UFD/GCD/Dedekind/Euclidean/integrally closed refinements, local/noetherian/reduced
  rings, complete rings, discrete valuation rings, and quadratic/cyclotomic/global-field
  refinements. Unrelated lazy imports for downstream return categories were preserved.
- Verification:
  - `git diff --cached --check` passed.
  - `python -m py_compile category_specs/rings/subcategories/{algebraically_closed_field,archimedean_global_field,complete,cyclotomic_field,dedekind_domain,discrete_valuation_ring,euclidean_domain,field,finite_field,gcd_domain,global_field,integral_domain,integrally_closed_domain,local,local_field,noetherian,nonarchimedean_global_field,number_field,principal_ideal_domain,quadratic_number_field,reduced,unique_factorization_domain}.py` passed.
  - `command ruff check` on the same scoped files passed. `uv run ruff check ...`
    failed before Ruff started because Hatch cannot infer the root `research` package
    wheel file selection.
  - Sage runtime probe confirmed representative `_Fields`, `_IntegralDomains`, and
    `_CompleteRings` base entries are resolved `ClasscallMetaclass` objects, not
    `LazyImport` placeholders.
  - `just smoke-file rings/smoketest.sage` no longer reports the base category
    class-identity mismatch. It now fails on the next tracked rings smoke surfaces:
    `__richcmp__`, finite-ring `ideal_monoid`, p-adic `_change_print_mode`, deferred
    q-adic precision-cap constructors, `QuadraticField(5, 'a')` constructor routing,
    and `MatrixRing(ZZ, 2)` algebra/module MRO refinement.
