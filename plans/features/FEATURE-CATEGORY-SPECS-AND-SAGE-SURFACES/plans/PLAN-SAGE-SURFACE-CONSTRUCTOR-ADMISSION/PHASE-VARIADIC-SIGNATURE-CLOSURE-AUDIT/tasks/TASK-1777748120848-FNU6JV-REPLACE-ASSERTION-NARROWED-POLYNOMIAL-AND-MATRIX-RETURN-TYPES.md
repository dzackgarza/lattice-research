---
id: TASK-1777748120848-FNU6JV-REPLACE-ASSERTION-NARROWED-POLYNOMIAL-AND-MATRIX-RETURN-TYPES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Replace assertion-narrowed polynomial and matrix return types
status: needs-review
priority: high
complexity: 55
description: Replace assertion-narrowed polynomial and matrix return types
successCriteria:
- Replace assertion-narrowed polynomial and matrix return types is resolved according
  to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Replace assertion-narrowed polynomial and matrix return types
Source: pasted backlog 2026-05-02.

Task: replace assertion-narrowed polynomial and matrix return types (via result of isinstance checks) with proper static union types using X|None patterns.

## Grounding

- Source provenance: recovered variadic sprint source at
  `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` in commit
  `8d1c21c^`; current phase card
  `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT.md`; tracked ring mapping
  `SPEC-MAPPING-RINGS.md`; tracked module mapping `SPEC-MAPPING-MODULES.md`.
- Style authority: `.agents/skills/category-spec-style/references/style.md`
  requires explicit closed overloads, no variadic public call shapes, and real
  mathematical types instead of duck-typed shape checks.
- Concrete source targets:
  - `category_specs/rings/__init__.py` has closed `PolynomialRing` overloads, but
    the implementation still uses `assert n is not None` to narrow impossible
    `var_array` and unnamed cases. Those should be explicit invalid-call-shape
    errors while keeping `n: Integer | None` in the closed implementation.
  - `category_specs/modules/subcategories/finitely_presented_over_pid.py` types
    `from_matrix(matrix: Matrix)` where `Matrix = SageMatrix` in
    `category_specs/types.py`, but then re-checks the same fact with
    `assert isinstance(matrix, SageMatrix)`. The static type already carries the
    matrix requirement; the runtime assertion is not the public contract.
- Mathematical owner:
  - `Rings().Constructors().PolynomialRing(...)` owns polynomial-ring constructor
    casework.
  - `Modules(R).FinitelyPresented().OverPID().from_matrix(matrix)` owns PID matrix
    presentations as cokernel constructions.
- Return objects: `PolynomialRing` returns a refined polynomial ring object;
  `from_matrix` returns the finitely presented module `coker(matrix)` via invariant
  factors.

## Acceptance Criteria

- [x] Preserve the existing closed `PolynomialRing` overload family and do not
  reintroduce broad positional or variadic Sage constructor surfaces.
- [x] Replace `assert n is not None` call-shape narrowing in `PolynomialRing` with
  explicit `TypeError` branches for invalid closed-overload combinations.
- [x] Remove the redundant `assert isinstance(matrix, SageMatrix)` check from the PID
  matrix-presentation constructor without weakening the `Matrix` annotation.
- [x] Keep matrix-presentation semantics as `coker(matrix)` over a PID.
- [x] Run syntax validation and a targeted regression/smoke check, or record the
  exact phase-local blocker.
- [x] Run and record a spec-weakening review before moving the card to
  `needs-review`.

## Complexity And Ownership

- Owner: category-spec ring/module type-surface implementation agent.
- Complexity: 55, Moderate (41-60).
- Complexity band: Moderate (41-60).
- Why this specific score:
  - The complexity is moderate because this is primarily a type-system replacement task with explicit static behavior (`isinstance`-based narrowing -> explicit union types). It is broader than a pure annotation tweak, but avoids cross-module architectural redesign.
- Item-specific evidence:
  - The concrete targets are two narrow source files:
    `category_specs/rings/__init__.py` and
    `category_specs/modules/subcategories/finitely_presented_over_pid.py`.
  - The work preserves existing constructors and result categories, but it touches
    public constructor type surfaces and therefore needs syntax plus targeted smoke
    validation.

## Work Log

- 2026-05-06: Began execution. Grounded the vague migrated card against the
  recovered variadic inventory, the ring and module mapping specs, and the current
  source sites using assertion narrowing.
- 2026-05-06: Replaced the two `PolynomialRing` `assert n is not None` branches
  with explicit `TypeError` invalid-call-shape errors, preserving the overload
  family and runtime Sage delegation.
- 2026-05-06: Removed the redundant `SageMatrix` import and
  `assert isinstance(matrix, SageMatrix)` check from
  `FinitelyPresentedModulesOverPID.from_matrix`; the public annotation remains
  `matrix: Matrix`, and the method still returns
  `module_category.from_invariant_factors(matrix.elementary_divisors())`.
- 2026-05-07: Review found one remaining call-shape assertion in the
  `PolynomialRing` closed dispatch: the multiple-variable-specification branch still
  used `assert variable_spec_count <= 1`. Replaced it with an explicit `TypeError`
  while preserving the closed overload family.

## Validation

- `python -m py_compile category_specs/rings/__init__.py category_specs/modules/subcategories/finitely_presented_over_pid.py` passed.
- `git diff --check -- category_specs/rings/__init__.py category_specs/modules/subcategories/finitely_presented_over_pid.py plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-1777748120848-FNU6JV-REPLACE-ASSERTION-NARROWED-POLYNOMIAL-AND-MATRIX-RETURN-TYPES.md` passed.
- Direct Sage check for `Rings().Constructors().PolynomialRing(QQ)` raising
  `TypeError` passed.
- `just --justfile category_specs/justfile smoke-file rings/smoketest.sage`
  failed on pre-existing smoke-frontier gaps including `hilbert_polynomial`,
  `boundary`, `ideal_monoid`, q-adic deferred constructors, and matrix-ring MRO.
- `just --justfile category_specs/justfile smoke-file modules/smoketest.sage`
  failed on pre-existing smoke-frontier gaps including `alternating_algebra`,
  graded-module category-base mismatches, lattice key errors, ideal refinement
  gaps, and ring-object-as-module gaps.
- Direct Sage check of
  `FinitelyPresentedModulesOverPID.from_matrix(Modules(ZZ), matrix(...))` remains
  blocked by an existing category-method exposure gap:
  `Modules(ZZ)` does not expose `from_invariant_factors` at runtime. This is not a
  new blocker introduced by this task; the task-local diff preserves the intended
  `coker(matrix)` delegation.
- 2026-05-07 re-validation after the review fix:
  `python -m py_compile category_specs/rings/__init__.py
  category_specs/modules/subcategories/finitely_presented_over_pid.py` passed.
- `git diff --check -- category_specs/rings/__init__.py
  category_specs/modules/subcategories/finitely_presented_over_pid.py` passed.
- `rg -n "assert n is not None|assert variable_spec_count|assert
  isinstance\(matrix, SageMatrix\)"
  category_specs/rings/__init__.py
  category_specs/modules/subcategories/finitely_presented_over_pid.py` found no
  remaining targeted assertion-narrowing sites.
- Tiny Sage check of
  `Rings().Constructors().PolynomialRing(QQ, name="x", names="y")`,
  `Rings().Constructors().PolynomialRing(QQ, var_array="x")`, and
  `Rings().Constructors().PolynomialRing(QQ, name="x")` passed: the invalid closed
  shapes raise `TypeError`, and the valid named constructor still returns a
  polynomial ring with variable name `x`.
- `just plan-validate` passed on 225 root planning cards.
- Targeted Ruff check
  `uvx --from ruff ruff check category_specs/rings/__init__.py
  category_specs/modules/subcategories/finitely_presented_over_pid.py` still reports
  the pre-existing `E741` parameter-name finding at
  `category_specs/rings/__init__.py:462`, outside this card's assertion-narrowing
  surface.

## Spec-Weakening Review

- Reviewed the task-local diff for deleted overloads, removed constructor
  obligations, narrowed smokes, moved owners, generic Sage call-shape admission, and
  Sage-gap-driven interface shrinkage.
- Result: passed. The diff only replaces assertion narrowing with explicit call-shape
  errors and removes a redundant runtime type check whose static `Matrix`
  annotation remains intact.
- 2026-05-07 re-review of the follow-up diff: passed. The extra change converts an
  invalid closed-overload combination from `assert` to `TypeError`; it does not
  delete overloads, narrow smokes, move ownership, or shrink the polynomial-ring
  constructor surface.
