---
id: TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS
trackerStatus:
  type: task
parents:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
dependsOn:
- '[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]'
blocks:
- '[[TASK-01KQN9YGCMD0K84CK3BKZH0Z8Z-IMPLEMENT-MODULE-CATEGORY-GRAPH-PHASE-FOR-AMBIENT-FREE-VECTOR-SUBOBJECT]]'
title: Ground root module abstract-method ownership before any migration
status: needs-review
priority: high
description: Audit the project abstract methods currently installed on generic `Modules(R)`
  objects and preserve each ideal-interface obligation under its grounded owner before
  any method is moved, implemented, or rejected.
successCriteria:
- Each root `Modules(R).ParentMethods` abstract method is either kept on the root
  with a source-grounded generic implementation obligation, preserved under the weakest
  grounded mathematical owner, or routed to a decision/source-mining card when the
  owner is ambiguous.
- The ownership record cites `category_specs/modules/docs/MAPPING.md`, `category_specs/modules/docs/SAGE_INVENTORY.md`,
  Sage written docs/source, or an approved decision card for each method touched.
- Constructor and refinement smoke failures preserve exact remaining surfaces; do
  not bypass `_test_not_implemented_methods`, switch smokes to `test=False`, or add
  placeholder methods just to pass.
- No obligation is deleted or weakened because Sage lacks a current implementation.
  A move is valid only when a grounded replacement owner carries the same mathematical
  surface or a sharper source-backed surface.
- No moved method is broadened beyond its hypotheses, especially finite-rank, free,
  ordered-basis, PID, field, subobject, quotient, tensor, dual, symmetric/exterior
  construction, or forms-owned hypotheses.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE
---
# Ground root module abstract-method ownership before any migration

## Summary

`modules/smoketest.sage` now reaches constructor routing for refined module
subcategories, but the first constructor smoke fails during `refine_category(...,
test=True)` because current Sage objects do not yet satisfy the full project spec.
This task must not treat that as evidence against the spec. Its job is to ground each
root abstract-method obligation and either preserve it on `Modules(R)`, preserve it
under a source-grounded owner, or route an explicit decision/source-mining item.

## Source Provenance

- Triggering implementation card: `[[TASK-01KQN9YGCMD0K84CK3BKZH0Z8Z-IMPLEMENT-MODULE-CATEGORY-GRAPH-PHASE-FOR-AMBIENT-FREE-VECTOR-SUBOBJECT]]`.
- Runtime frontier: `just smoke-file modules/smoketest.sage` fails first with `AssertionError: Not implemented method: alternating_algebra` after refined subcategories gain `Constructors()`.
- Direct source surface: `category_specs/modules/__init__.py`, `_RModObjects`.
- Mapping authority: `category_specs/modules/docs/MAPPING.md`, especially the method-owner table placing `dual`, `linear_form`, `alternating_form`, symmetric and exterior powers on `DualObjects()` or appropriate symmetric/exterior construction owners over finite-rank free modules, determinant and Gram/form data on forms-owned categories, submodule and quotient operations on `Subobjects()` and `Quotients()`, and tensor operations on `TensorProducts()`.
- Sage inventory authority: `category_specs/modules/docs/SAGE_INVENTORY.md`, especially the finite-rank tensor-module and representation-module inventories.
- Deleted-plan authority: recover `plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` with `git show 8d1c21c^:plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`; its order is mapping, category graph, constructor routing, method coverage, wrapper deletion.

## Context

The current generic root abstract surface includes at least:

- `annihilator`
- `torsion_submodule`
- `tensor_algebra`
- `base_change`
- `module_structure`
- `modify_module_structure`
- `symmetric_algebra`
- `alternating_algebra`
- `dual`
- `determinant_module`
- `cardinality`
- `is_isomorphic_to`
- `is_submodule_of`
- `direct_sum`
- `tensor`
- `intersection`
- `span`
- `__mul__`
- `quotient_module`
- `natural_pairing`

The first smoke failure is only the alphabetically earliest missing Sage implementation
on the sampled free module. The real issue is not to shrink the root surface until the
mathematics says it is too broad. Some methods are generic module obligations, some
require subobject, quotient, finite-rank, basis, dual, form, PID, field, or sidedness
hypotheses, and that distinction must be proved method by method.

Generic root ownership is the default whenever an operation is mathematically defined
for arbitrary `R`-modules. A method may move off `Modules(R)` only after this task or
`[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` records the missing datum, hypothesis,
or counterexample showing that the operation is not well-defined for arbitrary modules.
Current Sage gaps, smoke failures, algorithmic difficulty, or the result object's
construction category are not evidence against root ownership.

## Mathematical Review Finding

The first owner table drafted for this task is invalid. It pattern-matched method
names against Sage/mapping rows and confused construction codomains with method
ownership. In particular, saying that `quotient_module(N)` is owned by quotient
objects is mathematically incoherent: a module `M` is quotiented by a submodule
`N <= M`, and the result `M/N` is the quotient object.

This task is therefore a mathematical review task before it is an implementation
task. Each method disposition below must parse as a mathematical sentence about the
object on which the method is called, the data supplied, the construction or predicate
being asserted, the codomain/result, and the hypotheses under which the statement is
well-defined. Sage inventory is evidence only after that sentence is coherent.

## Root Method Ownership Re-Audit Draft

The tracked method mapping now lives in
`[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`. This task implements or decomposes
from that spec; do not recreate an untracked ownership table here.

The local invariant is the category-spec project purpose: specs define the ideal
mathematical interface inside Sage's category/object universe. Current Sage coverage
is not the adequacy standard, while Sage interop remains a design constraint where
mathematically appropriate. Sage inventory is implementation evidence and a feasibility
witness, helping preserve existing functionality and avoid unimplementable wishlists.
Smoke failures must be recorded as current implementation/refinement gaps unless a
source-grounded replacement owner preserves the same mathematical obligation.

## Acceptance Criteria

- [ ] Before any method is moved, deleted, or assigned to a narrower owner, the card
      records the source-grounded replacement owner and the preserved mathematical
      obligation.
- [ ] Before any method is moved off `Modules(R)`, the card or linked spec records why
      the operation itself is not mathematically defined for arbitrary modules, naming
      the missing datum, extra hypothesis, or counterexample. If that evidence is not
      present, the root abstract obligation remains and subcategories may only refine
      implementation, algorithms, or return types.
- [ ] Each method disposition is reviewed as a mathematical sentence before Sage
      inventory is used: caller object, required data, hypotheses, construction or
      predicate, and codomain/result are explicit and coherent.
- [ ] Before this task is advanced, review `git diff --cached`, `git diff`, and any
      commits created during the task for deleted abstract methods, removed
      constructor/category obligations, narrowed smokes, or Sage-gap-driven interface
      shrinkage.
- [ ] The root method list above is audited against the mapping and Sage inventory.
- [ ] Methods left on generic `Modules(R)` have grounded generic definitions and an
      implementation path that does not rely on duck typing.
- [ ] Methods moved off the root are installed only on the weakest grounded owner
      category, with hypotheses and codomain recorded in the relevant mapping doc or
      card body.
- [ ] No method obligation is deleted, weakened, or treated as optional because current
      Sage classes fail the smoke.
- [ ] Ambiguous surfaces become decision cards rather than speculative code.
- [ ] `just smoke-file modules/smoketest.sage` is rerun and the new frontier is
      recorded in this card and the blocking implementation card.

## Dependencies And Boundaries

- This task may edit `category_specs/modules/__init__.py`, module construction-category
  files, module subcategory files, and module mapping docs.
- Do not edit forms, lattices, rings, or tensor algebra component files except to
  connect an already-grounded owner; cross-subtree uncertainty becomes a decision card.
- Do not mark the blocking implementation card complete. It remains human-review gated
  after the smoke frontier is updated.
- Do not weaken the smoke harness or validation utilities to hide missing abstract
  methods.

## Work Log

- Created from the module constructor-routing smoke frontier after refined module
  subcategories gained `Constructors()` and the next blocker became over-broad root
  abstract method ownership.
- Planning validation passed after card creation: `just plan-validate` validated 179
  root planning cards, and the central planning validator regenerated
  `plans/plan-dag.md`.
- Scoped smoke confirmation: `just smoke-file modules/smoketest.sage` still fails
  first on `AssertionError: Not implemented method: alternating_algebra`; this task
  owns the root method-owner audit needed before that smoke can reach the previous
  deleted-plan frontier.
- 2026-05-06: Updated `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` so standard
  commutative-ring and integral-domain module surfaces have explicit owners instead
  of vague decision-needed rows. Added
  `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` for the remaining
  sidedness, scalar-action transport, torsion-over-zero-divisor, and overloaded
  `__mul__` conventions. Commit: `a281c4a`.
- 2026-05-06: Repaired the process drift that treated the owner table as a relocation
  recipe. `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` now states that generic
  root ownership is the default for operations mathematically defined on arbitrary
  `R`-modules, and that moving a method off `Modules(R)` requires a missing datum,
  extra hypothesis, or counterexample. Re-audited the rows for `annihilator`,
  `tensor_algebra`, `dual`, `tensor`, and `natural_pairing` so convention or
  implementation gaps do not by themselves move the obligation off the root.
- 2026-05-06 smoke frontier: `just --justfile category_specs/justfile smoke-file
  modules/smoketest.sage` still fails as gap evidence. The repeated first frontier is
  `AssertionError: Not implemented method: alternating_algebra`; additional preserved
  findings include QQ inner-product vector-space `ValueError`, representation-module
  `KeyError: (256, 229)`, graded-module Sage/project base-category mismatch,
  integer-lattice and torsion-quadratic `KeyError: (256, 260)`, ideal submodule
  `_refine_category_` absence, and ring-as-module missing ring abstract methods.
