---
id: SPEC-01KQN9J3WNN6TDRX3X15GGJ3PN-FINISH-MODULES-SAGE-WRAPPER-MIGRATION-MAPPING-AND-DELETE-ONLY-WRAPPERS-W
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
title: Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods
  have real mathematical owners
status: needs-review
priority: critical
requirement: 'The deleted module wrapper migration plan is a phased migration contract: map
  methods first, define the category graph, rewrite constructors, move methods to real owners,
  then delete wrappers.'
acceptanceCriteria:
- The mathematical owner, public surface, classification, and migration consequence are recorded
  in `category_specs/modules/docs/MAPPING.md`.
- No new subtree-local TRIAGE or process document is created.
- No implementation blocker was discovered in this source-map pass.
- The deleted plan's phase-specific validation commands are preserved as implementation-phase
  guidance; this leaf performs mapping only.
- '`modules/docs/MAPPING.md` has no known unresolved wrapper-candidate bucket after this pass;
  closure still requires human review.'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
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

- The migrated source path in the original card text is stale. The deleted file
  actually lived at `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`
  and was removed in commit `8d1c21c`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Finish modules Sage-wrapper migration mapping and delete only wrappers whose methods have real mathematical owners from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`
- Recovery check: the pre-removal plan requires mapping first, category graph second,
  constructors third, method ownership fourth, and wrapper deletion last.

Stale-path check:

- Searched: `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`,
  then broadened with `git ls-tree -r --name-only 8d1c21c^ | rg 'SAGE_WRAPPER_MIGRATION_PLAN|modules/docs|plans/category_specs/modules'`.
- Found: the `category_specs/...` path is absent at `8d1c21c^`; the recoverable file
  is `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Conclusion: inference - the card's migrated source path was stale, but the exact
  source plan is recoverable from the deleted `plans/` tree.
- Confidence: High.
- Gaps: none for the existence and location of this deleted source file.

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

- [x] The mathematical owner, public surface, classification, and migration consequence are recorded in `category_specs/modules/docs/MAPPING.md`.
- [x] No new subtree-local TRIAGE or process document is created.
- [x] No implementation blocker was discovered in this source-map pass.
- [x] The deleted plan's phase-specific validation commands are preserved as implementation-phase guidance; this leaf performs mapping only.
- [x] `modules/docs/MAPPING.md` has no known unresolved wrapper-candidate bucket after this pass; closure still requires human review.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the deleted wrapper plan from `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` after the migrated `category_specs/...` provenance path proved stale.
- Added a wrapper-candidate classification audit to `category_specs/modules/docs/MAPPING.md`: constructor-only interop shells, forms-owned owners, lattice-owned owner, and retained real module-category owners.
- Checked exact wrapper-name references in `category_specs/modules`; deleted wrapper names remain in mapping/provenance documentation, while live code references are retained real-category surfaces.
- Skipped subtree smoke and global QC intentionally; this is a documentation/source-map review-state handoff, not implementation integration or a phase transition.
