---
trackerStatus:
  itemId: impl_01KQN9YGCN4F4M2DH9GP2A00XZ
  title: Implement TensorAlgebraComponents constructors for module-element matrices
    structure constants and multiplication-tensor handoff to Algebras(R)
  type: implementation-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - cat
  - category-specs
  - implementation-work
  - tensor-algebra-components
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Implement TensorAlgebraComponents constructors for module-element matrices structure constants and multiplication-tensor handoff to Algebras(R)

## Summary

Tensor mapping fixes tensor component ownership, coordinate interop constructors, dual-
object interpretation, and the algebra multiplication-tensor handoff.

## Source Provenance

- `plans/category_specs/tensor_algebra_components/docs/MAPPING.md`
- Original migrated line: `Implement TensorAlgebraComponents constructors for module-element matrices structure constants and multiplication-tensor handoff to Algebras(R) from plans/category_specs/tensor_algebra_components/docs/MAPPING.md`

## Context

- A tensor is an element of T_R(M)[p,q]; tensor_type() is the public tuple-valued type.
- Matrix inputs construct (0,2) tensors; module-element matrices construct (1,2) multiplication tensors.
- Algebras(R).Constructors().from_multiplication_tensor receives only the canonical tensor element after TensorAlgebraComponents converts coordinate shapes.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Confirm tensor_type() == (1,2) and base-module compatibility before algebra handoff.
- [ ] Do not expose catch-all component data as public constructor surface.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

