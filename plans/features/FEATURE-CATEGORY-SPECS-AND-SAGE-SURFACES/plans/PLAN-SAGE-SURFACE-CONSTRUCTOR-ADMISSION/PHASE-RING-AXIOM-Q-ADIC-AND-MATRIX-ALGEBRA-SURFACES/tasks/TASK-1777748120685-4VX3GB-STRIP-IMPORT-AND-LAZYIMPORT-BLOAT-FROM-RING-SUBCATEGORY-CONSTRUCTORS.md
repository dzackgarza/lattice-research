---
id: TASK-1777748120685-4VX3GB-STRIP-IMPORT-AND-LAZYIMPORT-BLOAT-FROM-RING-SUBCATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Strip import and LazyImport bloat from ring subcategory constructors
status: blocked
blocked_reason: "Implementation complete but commit blocked: pre-commit hook `just test` fails during global mypy with Sage/pytest import-stub errors."
priority: high
description: Strip import and LazyImport bloat from ring subcategory constructors
successCriteria:
- Ring subcategory modules no longer duplicate top-level LazyImport blocks for shared
  private subcategory references.
- Shared Sage ring class tuples and shared lazy subcategory references are centralized
  without weakening the public category/spec surface.
- Remaining LazyImport calls are limited to intentional public axiom/subcategory constructors
  or the centralized helper module.
- Python syntax validation passes for category_specs/rings/subcategories.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
complexity: 58
---
# Strip import and LazyImport bloat from ring subcategory constructors
Source: pasted backlog 2026-05-02.

Task: strip import and LazyImport bloat from the ring subcategory constructors, fix the public surface to use canonical constructors.

## Grounding And Scope

- This is implementation-hygiene work inside `category_specs/rings/subcategories/`, not a mathematical ownership change.
- Preserve the existing ring category/spec obligations and public axiom constructor surface.
- Do not make smoke tests pass by weakening the ideal interface; Sage gaps route to implementation, wrapper, decision, or source-mining work.
- Blocked children are not acceptance. This card is review-ready only because its own scoped cleanup has been implemented and validated.

## Work Completed

- Added `category_specs/rings/subcategories/_lazy_subcategories.py` as the single local source for shared private lazy references between ring subcategories.
- Added `category_specs/rings/subcategories/_sage_ring_classes.py` as the single local source for Sage polynomial, power-series, Laurent-series, Puiseux-series, and lazy-series class tuples.
- Replaced copied top-level private `LazyImport(...)` blocks in ring subcategory modules with imports from the shared helper.
- Preserved the intentional indented `LazyImport(...)` class attributes that expose public axiom/subcategory constructors such as `Commutative().Field`, `IntegralDomains().Gcd`, and `Fields().NumberFields`.
- Removed duplicate imports of Sage series/polynomial classes from individual subcategory modules that now consume the centralized class tuples.

## Current Blocker

- The implementation cleanup is present in the working tree and passed local syntax/search/planning checks, but it is not committed.
- A normal non-markdown commit is blocked by the repo pre-commit hook, which runs `just test`; that currently fails during global mypy with broad existing Sage/pytest import-stub and category typing errors.
- This is a provenance/workflow blocker for this leaf, not evidence that the cleanup itself is accepted and not a reason to stop other markdown/spec leaves.
- Resolution path: fix the global QC/type-checking hook failure, or get an explicit human instruction changing the commit-gate policy. Do not count this blocked card as parent acceptance.

## Acceptance Notes

- `rg -n "^_[A-Za-z0-9]+ = LazyImport\(" category_specs/rings/subcategories -g '!_lazy_subcategories.py'` returns no matches.
- `rg -n "LazyImport\(" category_specs/rings/subcategories -g '!_lazy_subcategories.py'` now finds only indented axiom/subcategory constructor attributes.
- `python -m compileall -q category_specs/rings/subcategories` passed.
- Spec-weakening review: this diff centralizes imports and shared runtime class tuples only; it does not delete abstract methods, narrow smoke assertions, move mathematical obligations, or change category ownership.

## Complexity Justification

- Owner: C58.
- Complexity band: Moderate (41-60).
- Tracker type: task.
- Why this specific score: focused cleanup in the ring subcategory constructor path with moderate coupling. Import/lazy-import shape and canonical constructor exposure affect module load behavior and API consistency, but the work stays inside a bounded ring-subcategory surface.
- Item-specific evidence: deterministic refactoring, no new mathematical algorithm, and validation through static search plus Python syntax compilation.
