---
trackerStatus:
  type: feature
title: Expand TensorAlgebraComponents beyond the minimal tensor constructor surface only after mapping symmetry storage contraction trace display and migration needs
status: in-review
priority: critical
progress: 90
updated: '2026-05-05'
planId: SPR-ALG-TENSOR-01KQN9
tags:
- category-specs
- spec
- feature
- constructors
- algebras
- tensors
- mapping
- theme-constructor-routing
---

# Expand TensorAlgebraComponents beyond the minimal tensor constructor surface only after mapping symmetry storage contraction trace display and migration needs
## Summary

The deleted Tensor Algebra Components triage records an intentionally minimal current
scope and the deferred tensor-calculus surface.

## Source Provenance

- The migrated source path in the original card text is stale. The deleted file actually lived at `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`.
- Original migrated line: `Expand TensorAlgebraComponents beyond the minimal tensor constructor surface only after mapping symmetry storage contraction trace display and migration needs from category_specs/tensor_algebra_components/docs/TRIAGE.md`
- Recovery check: the pre-removal file records the deferred surface exactly as `Exhaustive tensor calculus method mapping`, `Symmetry and antisymmetry subtrees`, `Full component-storage API`, and `Tensor contraction, trace, display, and index-notation surfaces`.

## Context

- Current scope includes component modules T_R(M)[p,q], central Tensor type, constructor stubs, scalar matrix constructors as (0,2) tensors, and module-element matrix constructors as (1,2) tensors.
- Deferred work includes exhaustive tensor calculus method mapping, symmetry and antisymmetry subtrees, component storage API, contraction, trace, display, index notation, and detailed migration for old component containers.

## Source-Mining Contract

Sources to mine before any tensor-surface expansion:

- `category_specs/tensor_algebra_components/docs/MAPPING.md`, especially the rows for
  `tensor_type()`, `base_module()`, named interop constructors, and the dual-object
  rule `T_R(M)[p,q]^* = T_R(M)[q,p]`.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`, especially the
  Sage definition of tensors as multilinear maps `(M*)^k x M^l -> R`, the
  `tensor_type()` and `tensor_rank()` distinction, and the component-assignment
  interop rows.
- The deleted source named in `Source Provenance`, but only as migration context for
  which deferred surfaces still need an owner and return-object decision.

Decisions this leaf must produce before any public expansion beyond the current minimal
constructor surface:

- For each deferred surface named in this card, identify the exact owner category:
  `TensorAlgebraComponents(R)`, a tensor-component subcategory such as a symmetry or
  antisymmetry refinement, `Tensor` element methods, or `Modules(R).HomCategory().Forms()`
  when the surface is evaluation rather than tensor ownership.
- For each deferred surface, state the hypotheses and return object/codomain. At
  minimum this applies to symmetry/antisymmetry refinements, contraction, trace,
  display/index-notation interop, storage/component access, and any migration route
  from old component containers.
- For contraction and trace, decide whether the output is another tensor component
  `T_R(M)[p',q']`, a scalar in `R`, or only an interop/display helper, and record the
  exact tensor-type transformation.
- For storage or display surfaces, decide whether the public result is a tensor object,
  a typed finite collection of coordinates, or private interop only. Do not admit raw
  component-container APIs without a mapped mathematical owner.

Rejection/retirement condition:

- Retire or reject any proposed public tensor surface that cannot be anchored to the
  Sage tensor definition and the current mapping owner rules, or whose only support is
  the deleted triage prose without an exact owner and return-object decision.

## Execution Result

The required deferred-surface owner and codomain decisions now already exist in the
frozen tensor mapping, so this leaf is review-ready without further public API edits:

- `category_specs/tensor_algebra_components/docs/MAPPING.md` already records exact
  owner, hypotheses, codomain, and migration consequences for symmetry metadata,
  component storage, `trace(...)`, `contract(...)`, display, and index notation.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` already records
  the Sage tensor-definition and tensor-calculus facts that ground those decisions.
- `category_specs/tensor_algebra_components/__init__.py` already exposes the minimal
  admitted public tensor-calculus surface via abstract `Tensor.trace(...)` and
  `Tensor.contract(...)` signatures, with the scalar-vs-tensor codomain rule stated
  in the docstrings.

No additional public tensor surface remains missing in this bounded spec pass. The
remaining follow-up is implementation, not further owner mapping:

- concrete Sage-backed tensor wrappers still need method bodies realizing
  `trace(contravariant_position, covariant_position)` and
  `contract(left_position, other, right_position)` under the already-frozen
  signatures;
- any surviving historical index-notation or component-container callers must be
  migrated at call sites to constructor metadata, `trace(...)`, or explicit
  `contract(...)` when those implementation leaves execute.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered in this bounded spec pass; the remaining work is concrete method implementation and caller migration under already-frozen signatures.
- [x] The tensor API was not expanded past the frozen mapping in this pass; the existing admitted public surface is `trace(...)` and explicit `contract(...)` only.
- [x] No constructor or refinement changes were made in this pass, so `tensor_algebra_components/smoketest.sage` did not apply.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Broadened the stale deleted-triage provenance from `category_specs/...`
  to `plans/category_specs/...`, confirmed that the recovered triage target is fully
  covered by freeze commit `1e10d9c`, and moved this expansion leaf to `in-review`
  because the required owner/codomain decisions and minimal public `trace(...)` /
  `contract(...)` tensor surface already exist.
