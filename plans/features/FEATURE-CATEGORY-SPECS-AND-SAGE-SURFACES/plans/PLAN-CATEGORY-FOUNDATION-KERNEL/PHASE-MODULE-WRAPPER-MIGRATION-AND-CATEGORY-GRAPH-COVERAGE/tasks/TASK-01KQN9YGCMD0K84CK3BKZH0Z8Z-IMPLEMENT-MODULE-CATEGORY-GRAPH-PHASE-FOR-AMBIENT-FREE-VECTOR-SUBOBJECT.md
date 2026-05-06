---
id: TASK-01KQN9YGCMD0K84CK3BKZH0Z8Z-IMPLEMENT-MODULE-CATEGORY-GRAPH-PHASE-FOR-AMBIENT-FREE-VECTOR-SUBOBJECT
trackerStatus:
  type: task
parents:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
dependsOn:
- '[[TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS]]'
title: Implement module category graph phase for ambient free vector subobject quotient
  form graded Ore and representation surfaces
status: in-progress
priority: high
description: 'The deleted module wrapper migration plan is a phased migration contract:
  map methods first, define the category graph, rewrite constructors, move methods
  to real owners, then delete wrappers.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Use the phase-specific validation commands from the deleted plan when implementing
  a child item.
- Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE
---
# Implement module category graph phase for ambient free vector subobject quotient form graded Ore and representation surfaces
## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- `category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Implement module category graph phase for ambient free vector subobject quotient form graded Ore and representation surfaces from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Before any spec or method-surface edit, reread `category-spec-style` and apply
      the ideal-interface invariant locally: current Sage coverage is not the
      adequacy standard, Sage interop remains a design constraint where
      mathematically appropriate, Sage is implementation evidence and a feasibility
      witness, and Sage gaps are implementation/wrapper findings rather than evidence
      against the spec obligation.
- [ ] Before implementing method-owner changes, the relevant task or mapping doc
      states the mathematical review in ordinary mathematical language: caller object,
      required data, hypotheses, construction or predicate, and codomain/result.
- [ ] Smoke failures are recorded as gap evidence. Do not advance this task by
      deleting, weakening, or moving abstract methods unless the obligation is
      preserved under a source-grounded replacement owner.
- [ ] Before this task is advanced, review `git diff --cached`, `git diff`, and any
      commits created during the task for deleted abstract methods, removed
      constructor/category obligations, narrowed smokes, or Sage-gap-driven interface
      shrinkage.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Use the phase-specific validation commands from the deleted plan when implementing a child item.
- [ ] Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Began implementation against `category_specs/modules/smoketest.sage`.
- Initial smoke frontier: `Modules(Zmod(6)).Constructors().FreeModule(2)` failed before constructor assertions because the refined `_OverCommutativeRing_with_category` object had no `Constructors()` method.
- Added `Modules.SubcategoryMethods.Constructors()` so base-ring-dispatched module subcategories expose the same constructor collector as `Modules(R)`.
- Post-patch smoke frontier: constructor exposure works, but `refine_category(..., test=True)` now fails on project abstract root module methods before the constructor assertions can reach the deleted-plan frontier. The first repeated failure is `AssertionError: Not implemented method: alternating_algebra`.
- Additional post-patch smoke findings preserved for the next implementation pass: QQ inner-product vector-space rows raise `ValueError: base must be a ring or a subcategory of Rings()`; representation modules raise `KeyError: (256, 229)`; graded rows report a base-category-class mismatch between Sage `GradedModules` and project `Modules`; integer-lattice and torsion-quadratic rows raise `KeyError: (256, 260)`; ideal submodule refinement raises `AttributeError: 'Ideal_pid' object has no attribute '_refine_category_'`; ring-as-module rows expose missing ring abstract methods such as `hilbert_polynomial`, `cardinality`, `completion`, `characteristic`, and `algebra_generators`.
- Split the root abstract-method ownership blocker into `[[TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS]]` because `category_specs/modules/docs/MAPPING.md` already says dual, alternating-form, symmetric/exterior-power, determinant/form, quotient, subobject, and tensor surfaces require narrower mathematical owners rather than generic `Modules(R)` placement.
- Validation: `just plan-validate` passed with 179 root planning cards; the central planning validator passed and regenerated `plans/plan-dag.md`.
- Scoped smoke rerun: `just smoke-file modules/smoketest.sage` fails as expected on the recorded frontier, first with `AssertionError: Not implemented method: alternating_algebra`.
- 2026-05-06: Root method ownership was re-audited in
  `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` after a process drift treated
  subcategory implementation gaps as evidence against root obligations. The next
  implementation pass must preserve root abstract methods whenever the operation is
  mathematically defined on arbitrary `R`-modules; moving off root requires a recorded
  missing datum, extra hypothesis, or counterexample.
- 2026-05-06 scoped smoke rerun: `just --justfile category_specs/justfile smoke-file
  modules/smoketest.sage` still fails as expected on gap evidence. The repeated first
  failure is `AssertionError: Not implemented method: alternating_algebra`; the same
  broader frontier remains for QQ inner-product vector spaces, representation modules,
  graded-module category-class mismatch, integer-lattice and torsion-quadratic key
  errors, ideal submodule refinement, and ring-as-module inherited ring methods.
- 2026-05-06 implementation pass: added finite-rank-free implementations of
  `symmetric_algebra()` and `alternating_algebra()` in
  `category_specs/modules/subcategories/free.py`. The implementation is source-backed:
  Sage's `ExteriorAlgebra` documentation defines the exterior algebra of a free module
  over a commutative ring and accepts a free module as input, while the symmetric
  algebra of a finite free module is represented by the polynomial algebra over the
  base ring on finite-rank generators. Direct provider validation passed on
  `FreeModule(IntegerModRing(6), 2)`.
- 2026-05-06 scoped smoke rerun after the finite-rank-free algebra patch:
  `just --justfile category_specs/justfile smoke-file modules/smoketest.sage` still
  fails, but the first standard free-module frontier moved from
  `alternating_algebra` to `alternating_form`. Remaining preserved gap evidence
  includes `alternating_algebra` on basis/subobject/quotient families,
  `annihilator` on free modules without basis and tensor-calculus finite-rank free
  modules, QQ inner-product vector-space base-category errors, representation-module
  `KeyError: (256, 229)`, graded-module Sage/project base-category mismatch,
  integer-lattice and torsion-quadratic `KeyError: (256, 260)`, ideal submodule
  `_refine_category_` absence, and ring-as-module inherited ring method gaps.
