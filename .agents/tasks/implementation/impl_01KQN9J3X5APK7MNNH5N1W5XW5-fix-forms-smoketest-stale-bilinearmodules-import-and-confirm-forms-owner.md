---
trackerStatus:
  type: feature
title: Fix forms smoketest stale _BilinearModules import and confirm forms owner identity through compatibility paths
status: in-review
priority: high
progress: 90
planId: SPR-MODULE-WRAPPER-01KQN9
tags:
- category-specs
- implementation
- feature
- smoke
- modules
- forms
- imports
- theme-modules-tensors
---

# Fix forms smoketest stale _BilinearModules import and confirm forms owner identity through compatibility paths
## Summary

The deleted Forms triage recorded ownership separation: formed-module category classes
live in forms, while module and lattice paths preserve compatibility re-exports.

## Source Provenance

- `plans/category_specs/forms/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/forms/docs/TRIAGE.md`.
- Original migrated line: `Fix forms smoketest stale _BilinearModules import and confirm forms owner identity through compatibility paths from plans/category_specs/forms/docs/TRIAGE.md`

## Context

- FormedModules(R) names the forms owner while preserving Modules(R).WithForms().
- forms/smoketest.sage checks owner identity through module and lattice compatibility paths.
- Axiom registration remains centralized in axioms.py.
- IntegerLattices remains a module constructor-route surface until lattice constructors move behind Lattices(R).Constructors().

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just smoke-file forms/smoketest.sage after forms ownership changes.
- [x] Keep forms-owned category classes in forms rather than module or lattice wrapper paths.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Initial scoped smoke: `just smoke-file forms/smoketest.sage` from `category_specs/`
  failed with `ImportError: cannot import name '_BilinearModules' from
  'category_specs.forms.subcategories.bilinear'`.
- Updated module and lattice compatibility shim files to re-export the current
  forms-owned public category packages, updated the smoke to assert identity through
  those public compatibility paths, and corrected the migrated source path to
  `plans/category_specs/forms/docs/TRIAGE.md`.
- Final scoped smoke: `just smoke-file forms/smoketest.sage` from `category_specs/`
  exited 0 with no output.
