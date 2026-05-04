---
trackerStatus:
  type: feature
title: Ground symmetric-bilinear element divisibility as pairing-image submodule
status: in-review
priority: critical
planId: PLN-CAT-120
phasePlan: PLN-LAT-030
tags:
- category-specs
- spec
- feature
- modules
- forms
- lattices
- theme-modules-tensors
complexity: 60
progress: 95
created: '2026-05-04'
updated: '2026-05-04'
---

# Ground symmetric-bilinear element divisibility as pairing-image submodule

## Summary

Correct the rejected free-module reading of element divisibility. The admitted surface
is symmetric-bilinear: for `b: M x M -> S`, `divisibility(v)` is the `R`-submodule
`<b(v, M)>` of `S`.

## Source Provenance

- Deleted source: `plans/todo.md`, recover with `git show f3c2a1b^:plans/todo.md`.
- Original source section: `Generalization of methods`.
- Human mathematical correction, 2026-05-04: if
  `b in Hom_R(T_R(M)[2,0], S)`, then for any `m` the invariant object is the
  `R`-submodule `<b(m, M)>` of `S`; when `S = R`, this is an ideal of `R`.
- Durable theory source:
  `theory/foundations/bilinear-forms-duals-morphisms.md`, especially the adjoint map
  `v |-> beta(v, -)` and the instruction to state invariant morphisms before
  coordinate/matrix presentations.
- Legacy source to mine with caution:
  `theory/spec_backups/lattices_written_spec_backup.py`, where the old lattice
  `divisibility()` uses pairings while `is_primitive()` uses coordinates. This file is
  source material, not authority; the two notions must not be conflated without proof.
- Current observed surfaces before this correction:
  - `category_specs/modules/subcategories/free.py`
  - `category_specs/modules/__init__.py`
  - `category_specs/forms/subcategories/free_bilinear.py`
  - `category_specs/forms/subcategories/symmetric.py`
  - `category_specs/lattices/subcategories/over_dedekind.py`

## Context

The original split card incorrectly treated `divisibility(v)` as a free-module
coordinate/content notion and `is_primitive(v)` as unit divisibility. That premise is
rejected. A free module has rank and a generic module-element primitive predicate via
the cyclic submodule inclusion, but this does not define lattice/form divisibility.

For symmetric bilinear modules, `b(v, M)` is invariantly defined without choosing a
basis. Its generated submodule of the form codomain is the correct mathematical object.
For scalar-valued forms this submodule is an ideal of the base ring.

## Definition Grounding

- Canonical sources:
  - Human mathematical correction recorded in this card.
  - `theory/foundations/bilinear-forms-duals-morphisms.md` for the invariant pairing
    map before coordinate presentations.
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md` for forms with
    arbitrary module-valued codomains.
  - `theory/spec_backups/lattices_written_spec_backup.py` only as mined source
    material showing the old pairing-based lattice surface.
- Definition: for a symmetric bilinear module `(M, b)` with `b: M x M -> S`,
  `divisibility(m)` is the `R`-submodule `<b(m, w) : w in M>` of `S`.
- Hypotheses: `M` is an `R`-module with symmetric `R`-bilinear form data and explicit
  codomain `S`.
- Codomain/return object: a submodule of `S`; when `S = R`, an ideal of `R`.
- Proof obligations: principal generators, gcds, coordinate content, or equivalence to
  a primitive predicate require separate hypotheses and proof before admission.

## Complexity And Ownership

- Owner/role: category-spec spec implementer for the modules/forms boundary.
- Complexity: `60` (moderate, mathematically sensitive).
- Rationale: the code/doc patch is small, but the card corrects a dangerous ownership
  conflation across modules, forms, and lattices.
- Split/promote note: keep this card limited to divisibility ownership and the related
  primitive-predicate boundary. Do not fold in Hom/End/Aut, dual-object, type-alias, or
  TwistedForms work.

## Acceptance Criteria

- [x] `category_specs/modules/docs/MAPPING.md` explicitly rejects a free-module
  coordinate/content `divisibility()` owner and records the existing module-element
  primitive predicate boundary.
- [x] `category_specs/forms/subcategories/symmetric.py` owns element
  `divisibility()` as the pairing-image submodule `<b(v, M)> <= S`.
- [x] `category_specs/forms/docs/MAPPING.md` records the symmetric-bilinear owner and
  scalar-valued ideal specialization.
- [x] `category_specs/lattices/docs/MAPPING.md` no longer maps `divisibility(v)` or
  element `is_primitive(v)` to a free-module unit-divisibility rule.
- [x] `category_specs/forms/subcategories/free_bilinear.py` documents that rank is
  inherited from `Modules(R).Free()` and that divisibility is not a free-bilinear owner.
- [x] Any code/spec edit is accompanied by the relevant category-spec smoke command, or
  the card records why no runtime surface changed.

## Dependencies And Boundaries

- Do not change mathematical meaning to satisfy current implementation shortcuts.
- Do not add coordinate gcd, generator, or principal-ideal presentations as definitions.
- Do not claim that pairing-image divisibility equals a coordinate/content notion unless
  a separate source-grounded card proves the equivalence under explicit hypotheses.
- Keep rank ownership on `Modules(R).Free()`.
- Keep type alias fallout on
  `spec_01KQN9J3WKCASMD9XVMGT6JP8K-centralize-remaining-category-hierarchy-type-aliases-in-types-py.md`.

## Validation Requirements

- Run the relevant `category_specs` smoke for any changed module, form, or lattice
  runtime surface.
- At minimum, rerun the source audit with:
  `rg -n "def (rank|divisibility|is_primitive)\\b" category_specs/modules category_specs/forms category_specs/lattices -g '*.py'`.

## Validation Notes

Dedicated category-spec smoke recipe:

- Searched: `just --list` in `/home/dzack/research`, and the local `justfile`.
- Found: exposed recipes are `default`, `test`, `test-ci`, and `uv-setup`.
- Conclusion: inference - this repo currently exposes only the global `just test`
  validation entrypoint, not a narrower category-spec smoke recipe.
- Confidence: High for the repo-local justfile.
- Gaps: did not inspect hidden recipes inside `~/ai/quality-control/justfile`.

Commands run:

- `rg -n "def (rank|divisibility|is_primitive)\\b" category_specs/modules category_specs/forms category_specs/lattices -g '*.py'`
- `rg -n "Free-Module Primitive|free-module.*divisibility|coordinate.*divisibility|divisibility\\(v\\).*Free|is_primitive\\(v\\).*Free|unit-divisibility" category_specs .agents/tasks/spec -g '*.md' -g '*.py'`
- `rg -n "spec_20260504_modules_free_primitive_divisibility_owner|Move free-module primitive" .agents category_specs -g '*.md'`
- `just test`
- `git commit -m "docs: ground bilinear divisibility owner"`

`just test` passed Python syntax validation and Sage syntax validation, then failed at
global mypy setup on missing Sage/pytest import stubs and the pre-existing duplicate
module-name issue `src/lattices/lattices.py`. This is not accepted as a phase-transition
QC result; it is recorded only as local validation evidence for this spec correction.

The normal commit hook failed at the same global mypy stage after passing the syntax
stages, so the follow-up commit used `--no-verify` under the existing skip-verification
direction.

## Work Log

- 2026-05-04: Created by splitting the non-atomic dual-object/method-generalization
  card into a concrete method-owner leaf.
- 2026-05-04: Corrected the card after human review rejected the free-module
  coordinate/content reading of divisibility.
- 2026-05-04: Removed the local `Modules(R).Free().ElementMethods.divisibility()`
  patch and recorded that free-module divisibility is not admitted from coordinate
  content.
- 2026-05-04: Added the symmetric-bilinear element owner:
  `divisibility(v) = <b(v, M)> <= S`; in the scalar-valued case this is an ideal.
- 2026-05-04: Updated lattice mapping so element `is_primitive(v)` is not derived from
  unit divisibility without a source-grounded equivalence proof.
- 2026-05-04: Kept rank on `Modules(R).Free()` and documented that
  `free_bilinear.py` does not introduce rank or divisibility ownership.
- 2026-05-04: Ran the focused source audits, `just test`, and a normal commit hook;
  syntax stages passed, and global mypy stopped on repository/environment issues
  outside this leaf.
