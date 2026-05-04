---
trackerStatus:
  type: feature
title: Move free-module primitive and divisibility surfaces to Modules.Free owners
status: to-do
priority: critical
planId: PLN-CAT-120
phasePlan: PLN-LAT-030
tags:
- category-specs
- spec
- feature
- modules
- forms
- theme-modules-tensors
complexity: 55
progress: 0
created: '2026-05-04'
---

# Move free-module primitive and divisibility surfaces to Modules.Free owners

## Summary

Split the `plans/todo.md` method-generalization item into an atomic owner-fix card for
free-module primitive and divisibility surfaces.

## Source Provenance

- Deleted source: `plans/todo.md`, recover with `git show f3c2a1b^:plans/todo.md`.
- Original source section: `Generalization of methods`.
- Current observed surfaces:
  - `category_specs/modules/subcategories/free.py`
  - `category_specs/modules/__init__.py`
  - `category_specs/forms/subcategories/free_bilinear.py`
  - `category_specs/lattices/subcategories/over_dedekind.py`

## Context

The source note says `rank` belongs to `Modules.Free`, and element-level
`divisibility` and `is_primitive` belong to the free-module surface rather than
forms-specific wrappers. The current tree already has `rank()` on
`Modules(R).Free().ParentMethods`, but `forms/subcategories/free_bilinear.py` still
declares form-local `rank`, `divisibility`, and `is_primitive` surfaces, and lattice
Dedekind refinements still restate rank/primitive-submodule semantics.

## Complexity And Ownership

- Owner/role: category-spec spec implementer for the modules/forms boundary.
- Complexity: `55` (moderate).
- Rationale: the work touches several related spec surfaces in one ownership boundary,
  but the target owner is clear from `plans/todo.md` and the current modules subtree.
- Split/promote note: keep this card limited to rank, divisibility, and primitive
  ownership. Do not fold in Hom/End/Aut, dual-object, type-alias, or TwistedForms work.

## Acceptance Criteria

- [ ] `category_specs/modules/docs/MAPPING.md` records the final owner and migration
  consequence for free-module rank, element divisibility, and primitive predicates.
- [ ] `Modules(R).Free()` or the appropriate free finite-rank refinement owns any
  required public method surface.
- [ ] Forms and lattice refinements do not duplicate the same method as if it first
  became meaningful only after adding a form; any remaining method is explicitly a
  form/lattice-specific refinement.
- [ ] Any code/spec edit is accompanied by the relevant category-spec smoke command, or
  the card records why no runtime surface changed.

## Dependencies And Boundaries

- Do not change mathematical meaning to satisfy current implementation shortcuts.
- Do not remove a form/lattice method unless the recovered public behavior is documented
  through the module owner or a deliberate compatibility alias.
- Keep type alias fallout on
  `spec_01KQN9J3WKCASMD9XVMGT6JP8K-centralize-remaining-category-hierarchy-type-aliases-in-types-py.md`.

## Validation Requirements

- Run the relevant `category_specs` smoke for any changed module, form, or lattice
  runtime surface.
- At minimum, rerun the source audit with:
  `rg -n "def (rank|divisibility|is_primitive)\\b" category_specs/modules category_specs/forms category_specs/lattices -g '*.py'`.

## Work Log

- 2026-05-04: Created by splitting the non-atomic dual-object/method-generalization
  card into a concrete method-owner leaf.
