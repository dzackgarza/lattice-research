---
trackerStatus:
  type: feature
title: Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods have real mathematical owners
status: to-do
priority: critical
planId: SPR-MODULE-WRAPPER-01KQN9
tags:
- category-specs
- spec
- feature
- sage
- modules
- wrappers
- mapping
- theme-modules-tensors
---

# Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods have real mathematical owners
## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- `category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods have real mathematical owners from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Source-Mining Contract

This card is executable only as a wrapper-to-owner mapping pass, not as blanket wrapper
deletion.

- Primary source anchors:
  - `category_specs/modules/docs/MAPPING.md`;
  - `category_specs/forms/docs/MAPPING.md`;
  - `category_specs/lattices/docs/MAPPING.md`;
  - `.agents/skills/category-spec-style/references/style.md`;
  - Sage written docs/source for the exact wrapper surface being migrated.
- For each wrapper candidate, record a concrete classification before any deletion:
  constructor-only interop shell, real module-category owner, forms-owned owner,
  lattice-owned owner, or unresolved owner that still needs source mining.
- For each migrated method, record the minimal owner category, explicit hypotheses
  (`WithBasis`, ordered basis, chosen generators, PID, field, free, finite-rank, form
  codomain, torsion, or lattice predicates), and the mathematical return object.
- Cross-subtree moves must respect the mapping split already recorded in the docs:
  modules own plain module structure, forms own `WithForms` and formed-module methods,
  lattices own only the named lattice endpoints and lattice-specific construction
  surfaces.
- A wrapper is deletable only after every public method on it has a grounded owner and
  no remaining non-provenance references depend on the wrapper name for public
  semantics.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Use the phase-specific validation commands from the deleted plan when implementing a child item.
- [ ] Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
