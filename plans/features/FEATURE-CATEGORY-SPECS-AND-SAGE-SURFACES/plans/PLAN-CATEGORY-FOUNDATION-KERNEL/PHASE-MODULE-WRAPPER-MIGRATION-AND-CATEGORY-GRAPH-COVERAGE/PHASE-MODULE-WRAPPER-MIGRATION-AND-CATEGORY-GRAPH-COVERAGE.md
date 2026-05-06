---
id: PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
dependsOn: []
title: Sprint module wrapper migration phase one through category graph constructor
  routing method coverage and deletion gates
status: in-progress
priority: critical
description: 'The deleted module wrapper migration plan is a phased migration contract:
  map methods first, define the category graph, rewrite constructors, move methods
  to real owners, then delete wrappers.'
successCriteria:
- The sprint has a bounded set of child tracker items and an explicit scope statement.
- Completion requires each child item to be done, superseded with rationale, or split
  with remaining work linked.
- The sprint closing note records smoke/test commands run and any unresolved blockers.
- Use the phase-specific validation commands from the deleted plan when implementing
  a child item.
- Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
---
# Sprint module wrapper migration phase one through category graph constructor routing method coverage and deletion gates

## Sprint Grounding Requirements

This sprint coordinates approved leaves; it is not mathematical definition authority.
Before a sprint item changes a spec, constructor, mapping, type, or implementation
surface, its card must cite the canonical source path, exact definition, owner category,
hypotheses, codomain/return object, and proof or Sage-evidence obligations.

If a sprint finding lacks that grounding, the sprint action is source mining, decision
capture, or splitting into a prerequisite card. QC and smoke findings identify work, but
they do not define the mathematical surface being repaired.

Every child card in this phase must reread `category-spec-style` just in time before
editing a module spec or method surface. The local task must preserve the ideal
mathematical interface inside Sage's category/object universe: current Sage coverage
is not the adequacy standard, Sage interop remains a design constraint where
mathematically appropriate, Sage method presence is evidence for mapping and
feasibility, Sage method absence is implementation-gap evidence, and smoke progress is
never a reason to delete or weaken a spec obligation.

Before advancing this phase or any child task, review the staged diff, unstaged diff,
and any commits created during the work for spec weakening. In particular, check for
deleted abstract methods, removed constructor/category obligations, narrowed smoke
assertions, or moved method owners without source-grounded replacement owners.

Before implementing a method move in this phase, perform a mathematical review of the
proposed owner. The review must state the caller object, required data, hypotheses,
construction or predicate, and codomain/result in ordinary mathematical language.
Rows copied from Sage inventory or mapping tables do not pass unless that statement is
coherent independently of the source-map wording.

## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- `category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Sprint module wrapper migration phase one through category graph constructor routing method coverage and deletion gates from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Acceptance Criteria

- [ ] The sprint has a bounded set of child tracker items and an explicit scope statement.
- [ ] Completion requires each child item to be done, superseded with rationale, or split with remaining work linked.
- [ ] Each child item that edits module specs or method surfaces states how the ideal
      interface obligation is preserved when Sage smokes fail.
- [ ] The sprint closing note records smoke/test commands run and any unresolved blockers.
- [ ] Use the phase-specific validation commands from the deleted plan when implementing a child item.
- [ ] Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
