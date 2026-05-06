---
id: TASK-1777748120565-B5H5VY-RESTORE-BINARY-PRIMITIVES-FOR-MODULE-AND-SET-PRODUCT-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Restore binary primitives for module and set product constructors
status: needs-review
priority: high
complexity: 58
description: Restore binary primitives for module and set product constructors
successCriteria:
- Restore binary primitives for module and set product constructors is resolved according
  to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Restore binary primitives for module and set product constructors
Source: pasted backlog 2026-05-02.

Task: restore the binary-only variants of the module and set product constructors, deprecate the n-ary forms, and add missing @final markers to the concrete implementations.

## Definition Grounding

- Project rule: binary operations are primitive mathematical surfaces; a finite
  aggregate operation may exist only as an explicit sequence overload/fold, never as a
  variadic catch-all or optional-argument option bag. Source:
  `.agents/skills/category-spec-style/references/style.md`, "Binary Operations Are
  Foldable" and "No Variadic Signatures".
- Set source: Sage documents `cartesian_product([A, B, ...])` as a finite-collection
  constructor and implements `sage.sets.cartesian_product.CartesianProduct(sets,
  category, flatten=False)` as the raw product parent. Source:
  `sage.categories.cartesian_product.cartesian_product` docstring and
  `sage.sets.cartesian_product.CartesianProduct` signature/docstring.
- Module source: local module specs already expose binary `direct_sum(self, other)` and
  `tensor(self, other)` as primitives with explicit sequence overloads, and Sage
  free-module `direct_sum(self, other)` is binary. Source:
  `category_specs/modules/__init__.py` and `sage.modules.free_module.FreeModule_generic.direct_sum`.
- Ownership: `CartesianProduct(left, right)` is owned at `Sets()` because every pair of
  sets has a Cartesian product set. Finite-factor construction is a compatibility
  aggregate returning the same one-object refinement category, not the primitive
  owner.

## Acceptance Criteria

- [x] `Sets().Constructors().CartesianProduct(left, right)` is the documented binary
      primitive and refines into Cartesian-product sets.
- [x] Finite-factor Sage compatibility remains available through an explicit
      non-variadic sequence surface.
- [x] Existing two-factor smoke/regression assertions exercise the binary primitive.
- [x] Multi-factor compatibility is still covered without treating Sage's sequence
      constructor as the only project surface.
- [x] Module product surfaces are audited for binary primitives and `@final` concrete
      implementations; no module change is made unless the audit finds a real gap.
- [x] Spec-weakening review confirms no constructor obligation was deleted or narrowed
      to satisfy current Sage behavior.

## Complexity Justification
- Owner: C58
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Restore binary primitives for module and set product constructors
- Why this specific score:
  - This work is confined to product-constructor APIs, but it enforces deprecation and behavior-preserving API transitions (`binary` vs `n-ary`) across module/set surfaces plus concrete implementation markers. That creates more than a trivial signature edit but not architecture-wide dependency spread.
- Item-specific evidence:
  - The task text explicitly constrains the scope to module and set product constructors and states both API migration steps and concrete `@final` enforcement.
  - There is a clear deprecation path and no explicit multi-file implementation plan, which narrows the verification burden to compatibility and consistency checks.

## Work Log

- 2026-05-06: Restored the set-product binary primitive as
  `Sets().Constructors().CartesianProduct(left, right)` and kept Sage's finite-factor
  constructor surface as the explicit `CartesianProductFromFactors(factors)` plus the
  legacy lowercase `cartesian_product(factors)` compatibility method. Updated set
  smoke/regression assertions so two-factor products exercise the binary primitive and
  three-factor products exercise the finite-factor compatibility path.
- 2026-05-06: Audited module product surfaces. `category_specs/modules/__init__.py`
  already exposes binary `direct_sum(self, other)` and `tensor(self, other)` primitives
  with sequence overloads, and concrete module Cartesian/tensor product construction
  methods under `category_specs/modules/subcategories/constructions/` already carry
  `@final` where they implement behavior. No module edit was needed.
- 2026-05-06: Added direct `cardinality()` and `is_finite()` delegations on the
  Cartesian-product set refinement to Sage's CartesianProducts provider. These are
  product-category laws in terms of factor cardinalities/finite status, not new
  project-specific mathematics.
- 2026-05-06: Replaced the oversized `Permutations(10)` regression witness with a
  small `GF(5) x IntegerRange(3)` product. The previous witness checked the same
  product-cardinality law at an inappropriate scale for constructor validation.
- 2026-05-06: Added the concrete Cartesian-product coercion criterion on the refined
  product category: a product coerces from another product exactly when the factor
  lists have the same length and each target factor coerces from the matching source
  factor. This mirrors Sage's criterion without calling Sage's fallback path, which
  re-enters the refined category method.

## Verification

- Passed: `python -m py_compile category_specs/sets/__init__.py category_specs/sets/subcategories/cartesian_product.py`
- Passed: `git diff --check -- category_specs/sets/__init__.py category_specs/sets/subcategories/cartesian_product.py category_specs/sets/smoketest.sage category_specs/sets/tests/regression/cartesian_product.sage plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-1777748120565-B5H5VY-RESTORE-BINARY-PRIMITIVES-FOR-MODULE-AND-SET-PRODUCT-CONSTRUCTORS.md`
- Passed with the existing Sage topological-axiom warning:
  `just --justfile category_specs/justfile smoke-file sets/smoketest.sage`
- Passed: `sage category_specs/sets/tests/regression/cartesian_product.sage`

## Spec-Weakening Review

- Reviewed staged/unstaged changes for this task. The diff adds a binary primitive,
  adds a named finite-factor compatibility surface, preserves lowercase Sage-style
  compatibility, and strengthens smoke coverage for the binary primitive. No abstract
  method, constructor obligation, smoke assertion, or owner surface was deleted or
  narrowed to make Sage pass.
