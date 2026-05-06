---
id: SPEC-01KQN9YGCB7YYAXVHWHQWGV281-FREEZE-TENSOR-SYMMETRY-ANTISYMMETRY-STORAGE-CONTRACTION-TRACE-DISPLAY-AN
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
title: Freeze tensor symmetry antisymmetry storage contraction trace display and index-notation
  mapping before expanding TensorAlgebraComponents
status: needs-review
priority: critical
requirement: The deleted Tensor Algebra Components triage records an intentionally
  minimal current scope and the deferred tensor-calculus surface.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  `category_specs/tensor_algebra_components/docs/MAPPING.md` and, for admitted operations,
  `category_specs/tensor_algebra_components/__init__.py`.
- No new subtree-local TRIAGE or process document is created.
- 'This leaf does not expand the tensor API beyond the frozen decisions: symmetry/antisymmetry
  remain constructor metadata; component storage, display, and index notation remain
  nonpublic; contraction and trace use named tensor-element methods only.'
- The stale provenance path is broadened and corrected to the deleted `plans/category_specs/.../TRIAGE.md`
  path.
- 'Verification remains cheap and local: parse/diff checks only in this leaf; subtree
  smoke and global QC are intentionally not part of this review-state handoff.'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Freeze tensor symmetry antisymmetry storage contraction trace display and index-notation mapping before expanding TensorAlgebraComponents
## Summary

The deleted Tensor Algebra Components triage records an intentionally minimal current
scope and the deferred tensor-calculus surface.

## Source Provenance

- The migrated source path in the original card text is stale. The deleted file actually lived at `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md` and was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`.
- Original migrated line: `Freeze tensor symmetry antisymmetry storage contraction trace display and index-notation mapping before expanding TensorAlgebraComponents from category_specs/tensor_algebra_components/docs/TRIAGE.md`
- Recovery check: the pre-removal file records the deferred surface exactly as `Symmetry and antisymmetry subtrees`, `Full component-storage API`, and `Tensor contraction, trace, display, and index-notation surfaces`.

## Context

- Current scope includes component modules T_R(M)[p,q], central Tensor type, constructor stubs, scalar matrix constructors as (0,2) tensors, and module-element matrix constructors as (1,2) tensors.
- Deferred work includes exhaustive tensor calculus method mapping, symmetry and antisymmetry subtrees, component storage API, contraction, trace, display, index notation, and detailed migration for old component containers.

## Source-Mining Contract

Source anchors that must be frozen into the mapping before tensor-surface expansion:

- `category_specs/tensor_algebra_components/docs/MAPPING.md` rows for named interop
  constructors, `tensor_type()`, dual objects, and the rule that component arrays are
  constructor inputs rather than public tensor objects.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` sections
  `Mathematical Definition Recorded By Sage`, `Construction And Recovery`, and
  `Component Interop`.
- The deleted triage file named in `Source Provenance` only for the list of deferred
  migration targets that still require an owner decision.

This card is a bounded source-mining and freeze leaf. It must produce a concrete mapping
decision for each of these deferred notions:

- symmetry and antisymmetry: decide whether they are tensor-component subcategories,
  tensor-element predicates, or purely constructor metadata inherited from Sage
  `sym=` / `antisym=` interop;
- storage/component access: decide which coordinate views remain private interop and
  which, if any, become typed finite collection returns on public constructors or
  helper methods;
- contraction and trace: identify owner category, required tensor-type hypotheses, and
  output tensor component or scalar codomain;
- display and index notation: decide whether the surface is mathematical notation on
  `Tensor` elements or nonpublic rendering/interchange support.

Required output of this leaf:

- exact owner category for each deferred surface;
- exact hypotheses on `tensor_type()` and base module;
- exact return object/codomain;
- exact migration consequence for old component-container and index-notation usages.

Rejection/retirement condition:

- reject any proposed public surface whose only rationale is convenience or old storage
  API parity, and retire any migration target that cannot be stated as a source-backed
  tensor owner rule with explicit hypotheses and codomain.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in `category_specs/tensor_algebra_components/docs/MAPPING.md` and, for admitted operations, `category_specs/tensor_algebra_components/__init__.py`.
- [x] No new subtree-local TRIAGE or process document is created.
- [x] This leaf does not expand the tensor API beyond the frozen decisions: symmetry/antisymmetry remain constructor metadata; component storage, display, and index notation remain nonpublic; contraction and trace use named tensor-element methods only.
- [x] The stale provenance path is broadened and corrected to the deleted `plans/category_specs/.../TRIAGE.md` path.
- [ ] Verification remains cheap and local: parse/diff checks only in this leaf; subtree smoke and global QC are intentionally not part of this review-state handoff.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the deleted triage file from `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md` after the migrated `category_specs/.../TRIAGE.md` path proved stale.
- Froze the deferred tensor-surface mapping: constructor-only `sym=` / `antisym=`, private component storage/rendering/index notation, and explicit tensor-element `trace(...)` / `contract(...)` ownership with codomain rules.
