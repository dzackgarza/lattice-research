---
trackerStatus:
  type: decision
title: Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees before full tensor-calculus method mapping
status: to-do
tags:
- category-specs
- decision
- tensors
- mapping
- needs-decision
- theme-decisions
planId: SPR-ALG-TENSOR-01KQN9
---

# Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees before full tensor-calculus method mapping
## Summary

The deleted Tensor Algebra Components triage records an intentionally minimal current
scope and the deferred tensor-calculus surface.

## Source Provenance

- `category_specs/tensor_algebra_components/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/tensor_algebra_components/docs/TRIAGE.md`.
- Original migrated line: `Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees before full tensor-calculus method mapping from category_specs/tensor_algebra_components/docs/TRIAGE.md`

## Context

- Current scope includes component modules T_R(M)[p,q], central Tensor type, constructor stubs, scalar matrix constructors as (0,2) tensors, and module-element matrix constructors as (1,2) tensors.
- Deferred work includes exhaustive tensor calculus method mapping, symmetry and antisymmetry subtrees, component storage API, contraction, trace, display, index notation, and detailed migration for old component containers.

## Decision Grounding Required

This decision cannot be settled from migrated backlog text alone. Before moving to `decided`, record the source paths inspected, the exact mathematical or category-theoretic alternatives, hypotheses and owner categories, consequences for public methods/constructors/types, and any proof or Sage-evidence obligations. Negative Sage-source findings must use the five-field search format.

## Acceptance Criteria

- [ ] The decision record lists the alternatives, selected outcome, rationale, consequences, and affected tracker items.
- [ ] If the decision changes category ownership, the relevant MAPPING.md is updated in the same work or a linked spec-work item.
- [ ] The decision status moves from needs-decision to decided only after the consequence is explicit enough for implementation.
- [ ] Do not expand tensor API beyond the mapped minimal surface without first freezing the deferred mapping.
- [ ] Run just smoke-file tensor_algebra_components/smoketest.sage after constructor or refinement changes.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

