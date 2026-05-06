---
id: SPEC-01KQN9J3WKCASMD9XVMGT6JP8K-CENTRALIZE-REMAINING-CATEGORY-HIERARCHY-TYPE-ALIASES-IN-TYPES-PY
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION]]'
title: Centralize remaining category hierarchy type aliases in types.py
status: needs-review
priority: critical
requirement: The source backlog identifies category-spec design work around dual objects
  as Hom objects, method ownership generalization, centralized type aliases, and a
  TwistedForms category.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this alias pass.
- Review the affected public type aliases and category methods against the recovered
  `plans/todo.md` content before closing.
- Relevant cheap verification was run for `types.py`; no subtree smoke was run because
  this pass changed only aliases and global smoke/QC is not the controlling activity
  for phase-01 spec churn.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Centralize remaining category hierarchy type aliases in types.py
## Summary

The source backlog identifies category-spec design work around dual objects as Hom
objects, method ownership generalization, centralized type aliases, and a TwistedForms
category.

## Source Provenance

- `plans/todo.md`
- recovered with `git show 8d1c21c^:plans/todo.md`; the old path is no longer in the
  current worktree
- Original migrated line: `Centralize remaining category hierarchy type aliases in types.py from plans/todo.md`

## Context

- Dual objects should route through Homsets: M* = Hom_R(M, R), so dual-object category wiring must not bypass the hom-category surface.
- Methods should move to the most general category where they make mathematical sense, rather than remaining on forms-specific wrappers.
- types.py should own standard mathematical aliases for module objects, elements, Hom/End/Aut objects, dual modules, forms, and scalar categories.
- TwistedForms should be a real form-object category rather than ad hoc form handling inside ModulesWithForms.

## Grounded Spec Contract

This card owns alias centralization only where the owner category is already grounded in
the current mapping docs and style rules.

- Standard type-package names live in `types.py` and follow
  `.agents/skills/category-spec-style/references/style.md`: each public category
  package names the category, object, element, morphism, Hom, End, and Aut surfaces it
  actually owns.
- Category-object and functor-category aliases must follow
  `category_specs/cat/docs/MAPPING.md` and `category_specs/homsets/docs/MAPPING.md`:
  `Hom`, `End`, and `Aut` names belong to the category whose objects and morphisms they
  classify, and subtree aliases must refine rather than shadow the generic hom/end/aut
  hierarchy.
- Dual-object aliases for modules must reflect the hom routing recorded in
  `category_specs/modules/docs/MAPPING.md` and
  `.agents/skills/category-framework-design/references/homsets-structural-core.md`:
  a dual module is the grounded `Hom_R(M, R)` object, not an independent wrapper role.
- Formed-module and lattice aliases must use the owner split from
  `category_specs/forms/docs/MAPPING.md`,
  `category_specs/lattices/docs/MAPPING.md`, and
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`: forms own
  `WithForms`, bilinear/quadratic, and generic dual/discriminant semantics; lattices
  add only the named lattice endpoints and lattice-specific construction categories.
- Discriminant-group, lattice, and scalar-category aliases may be centralized only when
  the owning subtree already exposes the mathematical noun in its mapping doc. If an
  alias candidate still depends on an unmapped owner or unresolved export surface, keep
  that alias out of `types.py` and record the concrete blocker in this card.

## Execution Result

Recovered source-path note:

- Searched: current worktree `find` for todo-like files, `rg` for the migrated todo
  text, `git log --all --name-only` for todo paths, and
  `git show 8d1c21c^:plans/todo.md`.
- Found: `plans/todo.md` is not present in the current worktree, but the exact source
  content is recoverable from `8d1c21c^:plans/todo.md`.
- Conclusion: inference -- the card's source provenance is historical and should stay
  attached to the recovered git object rather than a live worktree path.
- Confidence: High.
- Gaps: no external issue trackers or archived branches were searched because the
  needed source text was recovered from git history.

Alias decision executed:

- `DualModule`, `DualModuleElement`, and `DualModuleMorphism` now point to
  `Modules(R).DualObjects()` method surfaces through
  `modules/subcategories/constructions/dual_objects.py`.
- `RModDual`, `RModuleDual`, `RModDualElement`, `RModuleDualElement`,
  `RModDualMorphism`, and `RModuleDualMorphism` are compatibility aliases for that
  same dual-object surface.
- The previous `DualModule = RModule` and `RModDualElement = RModuleElement` aliases
  were rejected because `category_specs/modules/docs/MAPPING.md` states that
  `M^* = Hom_R(M, R)` must route through `Modules(R).DualObjects()` and the module Hom
  layer, not through plain module aliases.
- Hom/End/Aut alias names were left on the existing `Hom`, `End`, and `Aut` surfaces;
  the old `Homset`/`Endset`/`Autset` spelling remains Sage-interoperability vocabulary
  rather than new public aliases.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this alias pass.
- [x] Review the affected public type aliases and category methods against the recovered `plans/todo.md` content before closing.
- [x] Relevant cheap verification was run for `types.py`; no subtree smoke was run because this pass changed only aliases and global smoke/QC is not the controlling activity for phase-01 spec churn.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recovered historical `plans/todo.md` from git, corrected dual-module
  aliases in `types.py` to point at `Modules(R).DualObjects()` surfaces, and left
  Hom/End/Aut on the existing standard names rather than reintroducing old `Homset`
  spelling as public alias vocabulary.
