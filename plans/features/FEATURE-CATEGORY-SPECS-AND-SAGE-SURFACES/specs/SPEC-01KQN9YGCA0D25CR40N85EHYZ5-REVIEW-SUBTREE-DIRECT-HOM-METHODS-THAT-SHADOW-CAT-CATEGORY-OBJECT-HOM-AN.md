---
id: SPEC-01KQN9YGCA0D25CR40N85EHYZ5-REVIEW-SUBTREE-DIRECT-HOM-METHODS-THAT-SHADOW-CAT-CATEGORY-OBJECT-HOM-AN
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Review subtree direct Hom methods that shadow Cat category-object Hom and specify the
  uniform owner
status: needs-review
priority: critical
requirement: The deleted Cat triage recorded structural Cat smoke scope and future uniformization
  work for category-object Hom behavior and functor/autofunctor modeling.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in the relevant
  MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance; no current implementation blocker was discovered in this pass.
- Run just smoke-file cat/smoketest.sage after any Cat or category-object surface change;
  no Cat or category-object runtime surface changed in this pass.
- Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.
complexity: 55
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
- hom-end-aut
- cat
- forms
- theme-category-core
updated: '2026-05-04'
---
# Review subtree direct Hom methods that shadow Cat category-object Hom and specify the uniform owner
## Summary

The deleted Cat triage recorded structural Cat smoke scope and future uniformization
work for category-object Hom behavior and functor/autofunctor modeling.

## Source Provenance

- `plans/category_specs/cat/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/cat/docs/TRIAGE.md`.
- Original migrated line: `Review subtree direct Hom methods that shadow Cat category-object Hom and specify the uniform owner from category_specs/cat/docs/TRIAGE.md`

## Context

- Some subtree classes define direct Hom methods that may shadow Cat-level category-object Hom at runtime.
- Natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors.
- Generic Sage functors do not provide a uniform invertibility certificate, so concrete autofunctor membership is a future refinement.
- The Cat smoke is structural: Cat instantiation, category-object membership, functor HomCategory instantiation, and standard construction navigation.

## Grounded Review Outcome

Sources: `category_specs/cat/docs/MAPPING.md`,
`category_specs/homsets/docs/MAPPING.md`, and the recovered deleted triage source
named in `Source Provenance`.

The owner rule is now fixed: for category objects `A, B in Cat()`, direct `A.Hom(B)` is
the Cat-owned functor homspace `Hom_Cat(A, B)`. Lower category subtrees may refine
`HomCategory`, `EndCategory`, `AutCategory`, or concrete `HomCategory().Of(A, B)`
parents for their own object-level morphisms, but they must not define a direct `Hom`
method that changes the meaning of category-object Hom.

Audit result: `rg -n "def Hom\b" category_specs` found direct `def Hom` definitions
only in `category_specs/cat/__init__.py` and `category_specs/cat/base_category_types.py`.
Lower-subtree matches were construction-category or nested HomCategory refinements and
are permitted by the mapping rule.

Spec consequence: future direct lower-subtree `Hom` definitions are implementation
refactor work against the Cat mapping owner rule, not new mathematical decisions for
this card.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance; no current implementation blocker was discovered in this pass.
- [x] Run just smoke-file cat/smoketest.sage after any Cat or category-object surface change; no Cat or category-object runtime surface changed in this pass.
- [x] Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Complexity And Ownership

- Owner/role: category-spec spec agent, with Cat subtree ownership.
- Complexity: `55` (moderate).
- Rationale: the card required a bounded cross-subtree audit of direct `Hom` definitions
  and a Cat mapping update, but did not require implementation or a new mathematical
  ownership decision.
- Split/promote note: no split needed unless a future lower-subtree direct `Hom`
  definition appears; that should become an implementation refactor card tied to the
  Cat mapping rule.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-04: Corrected deleted-source provenance to
  `plans/category_specs/cat/docs/TRIAGE.md`; the migrated card path had omitted the
  old `plans/` prefix.
- 2026-05-04: Recorded the direct `Hom` ownership and migration rule in
  `category_specs/cat/docs/MAPPING.md`. Public `A.Hom(B)` for category objects remains
  Cat-owned; lower subtrees refine `HomCategory`, `EndCategory`, and `AutCategory`
  surfaces instead of shadowing `A.Hom(B)`.
- 2026-05-04: Audited `category_specs/**/*.py` with `rg -n "def Hom\b"` and found
  direct `def Hom` definitions only in `category_specs/cat/__init__.py` and
  `category_specs/cat/base_category_types.py`. Lower-subtree matches were
  `HomCategory` assignments or nested `class HomCategory(...)` refinements, which are
  allowed by the mapping rule.
- 2026-05-04: No `just smoke-file cat/smoketest.sage` run was needed because this pass
  changed mapping/card documentation only, not the Cat or category-object runtime
  surface.
