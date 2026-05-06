---
id: TASK-1777748120685-4VX3GB-STRIP-IMPORT-AND-LAZYIMPORT-BLOAT-FROM-RING-SUBCATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Strip import and LazyImport bloat from ring subcategory constructors
status: needs-review
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

## Blocker (Resolved 2026-05-06)

- ~~The implementation cleanup is present in the working tree and passed local syntax/search/planning checks, but it is not committed.~~
- ~~A normal non-markdown commit is blocked by the repo pre-commit hook, which runs `just test`; that currently fails during global mypy with broad existing Sage/pytest import-stub and category typing errors.~~
- The global QC justfile `_python-qc-files` recipe now excludes `**/*.bak/**` directories (`src.bak/`, `tests.bak/`) from all Python tool passes. Retry `git commit` to verify the mypy failure is cleared.

## Blocker Resolution (2026-05-06)

The global QC justfile `_python-qc-files` recipe now excludes `**/*.bak/**` directories
(`src.bak/`, `tests.bak/`) from all Python tool passes, which should clear the mypy
failure that blocked this commit. Retry `git commit` to verify, then mark complete.

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
