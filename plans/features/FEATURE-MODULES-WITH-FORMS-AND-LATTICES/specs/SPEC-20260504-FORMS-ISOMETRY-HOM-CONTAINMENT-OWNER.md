---
id: SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Route form-preserving isometry predicates through formed-module Hom containment
status: needs-review
priority: critical
requirement: Split the `plans/todo.md` method-generalization item into an atomic owner-fix
  card for form-preserving and isometry predicates on morphisms.
acceptanceCriteria:
- The forms or modules mapping docs state that form preservation is represented by
  membership in the formed-module Hom category.
- '`category_specs/forms/subcategories/free_bilinear.py` does not own a redundant
  generic `is_isometry()` predicate unless it is explicitly documented as a compatibility
  alias over Hom containment.'
- Lattice hom/aut surfaces distinguish lattice isometries as morphisms/aut objects
  in `Lattices(R).HomCategory()` / `Lattices(R).AutCategory()`, not as the owner of
  the generic form-preservation predicate.
- Any implementation blockers are split into implementation cards with source provenance,
  or no new blocker remains after the local spec-surface correction.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
---
# Route form-preserving isometry predicates through formed-module Hom containment

## Summary

Split the `plans/todo.md` method-generalization item into an atomic owner-fix card for
form-preserving and isometry predicates on morphisms.

## Source Provenance

- Deleted source: `plans/todo.md`, recover with `git show f3c2a1b^:plans/todo.md`.
- Original source section: `Removal of Redundant Predicates`.
- Current observed surfaces:
  - `category_specs/forms/subcategories/free_bilinear.py`
  - `category_specs/lattices/homsets.py`
  - `category_specs/topological_spaces/homsets.py` for a same-name but different
    metric-space use that must not be conflated with formed-module isometry.

## Context

The source note says to remove `is_isometry()` and `is_form_preserving()` from
forms-local bilinear morphism methods and replace them with homset containment:

```text
phi in Hom(L, M, category=Modules(R).WithForms().Bilinear())
```

At the spec level, a morphism preserves form data exactly when it is an element of the
hom object in the category of modules carrying that form. Orthogonal groups are then
aut objects in the formed-module category, not ad hoc boolean filters on ordinary
module morphisms.

## Definition Grounding

- Canonical sources:
  - `category_specs/cat/docs/MAPPING.md` for direct `A.Hom(B)` ownership and
    Hom/End/Aut routing.
  - `category_specs/forms/docs/MAPPING.md` for formed-module ownership of bilinear
    evaluation and orthogonal groups.
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`, "Presented
    Object Identity" and morphism semantics.
  - `theory/foundations/bilinear-forms-duals-morphisms.md`, "Base Change and
    Morphisms".
- Definition: a morphism of bilinear `R`-modules
  `f: (M1, beta1) -> (M2, beta2)` is an `R`-module morphism satisfying
  `beta1(v, w) = beta2(f(v), f(w))` for all `v, w in M1`. An isometry is an
  isomorphism with this property.
- Owner: the formed-module Hom category owns containment/form-preservation; the Aut
  category owns invertible form-preserving endomorphisms.
- Hypotheses: source and target carry compatible bilinear form data over the same base
  ring or an explicitly recorded semilinear/base-change map.
- Codomain/return object: containment returns membership in a Hom/Aut parent, not a
  standalone boolean method unless documented as a compatibility alias over that
  membership.
- Proof obligations: any matrix criterion must be proven equivalent to the categorical
  form-preservation equation under explicit presentation/basis hypotheses.

## Complexity And Ownership

- Owner/role: category-spec spec implementer for Hom/End/Aut and forms.
- Complexity: `65` (high).
- Rationale: this affects public morphism semantics across forms and lattices and must
  distinguish formed-module isometry from metric-space isometry.
- Split/promote note: keep this card limited to formed-module/lattice morphism
  containment. Do not include topological/metric isometry unless an audit proves that
  surface has the same owner.

## Acceptance Criteria

- [x] The forms or modules mapping docs state that form preservation is represented by
  membership in the formed-module Hom category.
- [x] `category_specs/forms/subcategories/free_bilinear.py` does not own a redundant
  generic `is_isometry()` predicate unless it is explicitly documented as a compatibility
  alias over Hom containment.
- [x] Lattice hom/aut surfaces distinguish lattice isometries as morphisms/aut objects
  in `Lattices(R).HomCategory()` / `Lattices(R).AutCategory()`, not as the owner of the
  generic form-preservation predicate.
- [x] Any implementation blockers are split into implementation cards with source
  provenance, or no new blocker remains after the local spec-surface correction.

## Grounded Spec Decision

Decision: form preservation is Hom containment in the relevant formed-module category.

For `C <= FormedModules(R)` and objects `M, N in C`, the public form-preserving morphism
surface is `C.HomCategory().Of(M, N)`. A candidate plain module morphism starts in
`Modules(R).HomCategory()` and belongs to the formed-module Hom object exactly when it
satisfies the form-compatibility equation recorded in the source grounding above.

Consequences recorded in this pass:

- `category_specs/forms/docs/MAPPING.md` now states the Hom-containment owner,
  isomorphism/isometry distinction, orthogonal-group owner, and metric-isometry
  boundary.
- `category_specs/modules/docs/MAPPING.md` now states the same rule at the module Hom
  layer so future module-Hom work does not reintroduce a boolean predicate owner.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md` now aligns the ABC
  sketch with Hom containment and treats `is_isometry()` as `is_isomorphism()` inside an
  already form-preserving Hom object.
- `category_specs/forms/subcategories/free_bilinear.py` and
  `category_specs/lattices/homsets.py` now document `is_isometry()` as an isomorphism
  compatibility query, not as the owner of form preservation.

Matrix equations remain valid implementation checks only after a presentation and
generators have been fixed; they are not the public definition of form preservation or
isometry.

## Dependencies And Boundaries

- Depends on the Cat/Hom ownership rules in `category_specs/cat/docs/MAPPING.md`.
- Do not weaken lattice orthogonal-group semantics; preserve the categorical meaning
  `O(M,b) = Aut(M,b)` in the formed-module category.
- Do not conflate metric-space isometries in `topological_spaces/homsets.py` with
  formed-module isometries.

## Validation Requirements

- Run the relevant category-spec smoke for any changed forms, lattice, or homsets
  runtime surface.
- At minimum, rerun:
  `rg -n "is_form_preserving|is_isometry" category_specs -g '*.py'`.

## Work Log

- 2026-05-04: Created by splitting the non-atomic dual-object/method-generalization
  card into a concrete Hom-containment owner leaf.
- 2026-05-04: Added definition grounding for formed-module isometry as Hom/Aut
  containment, with matrix criteria demoted to implementation checks under explicit
  presentation hypotheses.
- 2026-05-05: Updated forms/modules mapping docs, the lattice ABC source, and the
  local free-bilinear/lattice hom surfaces so form preservation is Hom containment and
  `is_isometry()` asks for isomorphism inside the already form-preserving Hom object.
