---
id: TASK-01KQN9J3WWCX4AA36TK4QVCNBK-FIX-CAT-SMOKE-HOM-END-AUT-OBJECTSOVER-OBJECTSUNDER-AND-WITHFORMS-FRONTIE
trackerStatus:
  type: task
parents:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
dependsOn: []
title: Fix Cat smoke Hom End Aut ObjectsOver ObjectsUnder and WithForms frontier
status: needs-review
priority: critical
description: The deleted Cat triage recorded structural Cat smoke scope and future
  uniformization work for category-object Hom behavior and functor/autofunctor modeling.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file cat/smoketest.sage after any Cat or category-object surface
  change.
- Check that direct subtree Hom methods do not hide the Cat-owned category-object
  operation.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
- PHASE-HOM-END-AUT-WORK-QUEUE
---
# Fix Cat smoke Hom End Aut ObjectsOver ObjectsUnder and WithForms frontier
## Summary

The deleted Cat triage recorded structural Cat smoke scope and future uniformization
work for category-object Hom behavior and functor/autofunctor modeling.

## Source Provenance

- Archived Cat triage content from commit `8d1c21c` lives at `plans/category_specs/cat/docs/TRIAGE.md`; recover it with `git show 8d1c21c^:plans/category_specs/cat/docs/TRIAGE.md`.
- Original migrated line: `Fix Cat smoke Hom End Aut ObjectsOver ObjectsUnder and WithForms frontier from category_specs/cat/docs/TRIAGE.md`

## Context

- Some subtree classes define direct Hom methods that may shadow Cat-level category-object Hom at runtime.
- Natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors.
- Generic Sage functors do not provide a uniform invertibility certificate, so concrete autofunctor membership is a future refinement.
- The Cat smoke is structural: Cat instantiation, category-object membership, functor HomCategory instantiation, and standard construction navigation.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just smoke-file cat/smoketest.sage after any Cat or category-object surface change.
- [x] Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Implemented the Cat smoke frontier fix and moved this card to in-review.

## Grounding

- `category_specs/cat/docs/MAPPING.md` owns category-object semantics: `Cat().meet(...)` must be a greatest lower bound in Sage's category order; `C.ObjectsOver(T)` and `C.ObjectsUnder(T)` are Cat-owned slice/coslice selectors; `C.HomCategory()` is the project name for hom categories, with Sage `Homsets()` spelling retained only as interop vocabulary.
- `category_specs/cat/docs/SAGE_INVENTORY.md` records Sage's category order, `Homsets()` / `Endsets()` runtime expectations, and local Cat files for hom/end/aut and standard construction categories.
- `category_specs/forms/subcategories/with_forms.py`, `bilinear.py`, and `quadratic.py` own the forms chain used by the Cat subobject smoke for `Modules(ZZ).WithForms()` and `.Bilinear()`.
- `category_specs/modules/docs/MAPPING.md` records that `Modules(R).WithForms()` remains the Sage-compatible spelling while forms owns the formed-module category surface.

## Result

- Added Cat-owned Sage interop aliases `Homsets()` and `Endsets()` that delegate to `HomCategory()` and `EndCategory()`, so Sage's `Parent.Hom(...)` construction can categorize category-object homsets without changing the project public naming.
- Restored Cat universal `ObjectsOver(...)` / `ObjectsUnder(...)` dispatch by exporting `_ObjectsOver` / `_ObjectsUnder` aliases from the Cat slice and coslice files, and removed ring-specific `ObjectsOver = _RingsOver` / `ObjectsUnder = _RingsUnder` aliases so `Rings().ObjectsOver(Sets())` uses the generic Cat-owned selector while ring-specific structure remains under `RingsOver(...)` / `RingsUnder(...)`.
- Made `Cat().meet([C, D, ...])` verify Sage's returned category is actually below every input; if Sage returns a non-lower-bound fallback, Cat returns the local `EmptyCategory()` bottom object.
- Added PID-specialized formed-module axiom classes for `Modules(R).OverPID().WithForms()`, `.Bilinear()`, `.Quadratic()`, and the immediate bilinear child axioms `Symmetric`, `Alternating`, `Nondegenerate`, `Integral`, and `Rational`. This prevents Sage's axiom descriptor from binding generic formed-module classes against the PID-specialized base category.

## Smoke Frontier

- Initial current run failed on Cat meet lower-bound checks, Cat Hom/End/Aut homset category construction, Cat slice/coslice imports, `Rings().ObjectsOver(Sets())` / `.ObjectsUnder(Sets())` ring-base validation, and PID `WithForms()` subobject metadata.
- After the Cat interop and slice dispatch patch, the frontier reduced to PID `WithForms().Bilinear()` axiom dispatch.
- Final `just smoke-file cat/smoketest.sage` passes. Sage still emits a non-fatal warning about `Sets.Topological` not being a `CategoryWithAxiom`; this card does not own that topological-space warning.

## Negative Findings

- Searched: `category_specs/cat/smoketest.sage`; `category_specs/cat/docs/MAPPING.md`; `category_specs/cat/docs/SAGE_INVENTORY.md`; current Cat, forms, modules, rings, sets, algebras, and topological-space files; archived `plans/category_specs/cat/docs/TRIAGE.md`; direct search for `def Hom` under `category_specs/`; targeted Sage runtime probes for Hom/End/Aut, ObjectsOver/ObjectsUnder, and WithForms chains.
- Found: no lower-subtree direct `def Hom` definitions shadowing Cat-owned category-object `A.Hom(B)`; direct `Hom` definitions remain limited to `cat/__init__.py` and `cat/base_category_types.py`.
- Conclusion: inference - the migrated direct-Hom shadowing risk is not currently present in `category_specs/`, so no Hom shadowing refactor was needed for this card.
- Confidence: High for current `category_specs/`; Medium for historical migrated plans.
- Gaps: no exhaustive search outside `category_specs/` was needed because the card concerns the category-spec smoke surface.

## Verification

- `python -m py_compile` on the touched Cat, forms, modules, and rings files.
- Targeted Sage runtime probe for `Modules(ZZ).WithForms()`, `.Bilinear()`, `.Quadratic()`, and immediate bilinear child axioms.
- `git diff --check`
- `just check-abstract-redefinitions` from `category_specs/`
- `just smoke-file cat/smoketest.sage` from `category_specs/`
