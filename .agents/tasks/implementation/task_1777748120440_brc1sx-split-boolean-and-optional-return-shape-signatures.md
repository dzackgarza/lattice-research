---
trackerStatus:
  type: task
title: Split boolean and optional return-shape signatures
status: in-review
priority: critical
planId: SPR-VARIADIC-AUDIT-01KQN9
progress: 90
tags:
- category-specs
- implementation
- task
- signatures
- theme-audit-uniformity
---

# Split boolean and optional return-shape signatures
Source: pasted backlog 2026-05-02.

Task: split the mixed boolean|None and T|None return-type signatures on Category and Map classes into explicit @overload declarations.

## Grounding

- Source provenance: recovered variadic sprint source at
  `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` in commit
  `8d1c21c^`, plus the current sprint plan
  `.agents/plans/phase-01-category-specs/sprints/sprint_01KQN9YGC00PT283PKG13EWPA9-sprint-variadic-signature-closure-audit-across-modules-rings-tensors-alg.md`.
- Style authority: `.agents/skills/category-spec-style/references/style.md` requires
  closed overloads for finite Sage casework and source-backed return objects.
- Sage grounding:
  - `NumberField.galois_closure(map=False)` returns the Galois closure field, while
    `map=True` returns the field with an embedding of the source field into it.
  - Algebraic `nth_root(all=False)` and `sqrt(all=False)` return one root; `all=True`
    returns the finite list of all roots.
- Local mapping: `category_specs/rings/docs/MAPPING.md` records the overload policy for
  these boolean-controlled return-shape methods.

## Result

- Added `Literal[False]`, `Literal[True]`, and non-literal `bool` fallback overloads
  for root-return shapes in `category_specs/rings/__init__.py`.
- Added the same overload split for specialized `nth_root` overrides in
  `category_specs/rings/subcategories/algebraic_closure_of_rational_field.py` and
  `category_specs/rings/subcategories/real_algebraic_field.py`.
- Added `map=False`/`map=True` overloads plus a non-literal `bool` fallback for
  `galois_closure` in `category_specs/rings/subcategories/number_field.py` and
  `category_specs/rings/subcategories/rational_field.py`.

## Out Of Scope Findings

- Searched: `category_specs/cat/docs/MAPPING.md`, `category_specs/cat/docs/SAGE_INVENTORY.md`,
  `category_specs/cat/*.py`, `category_specs/homsets/*.py`, current `category_specs`
  Python signatures for `map: bool`, `all: bool`, `transformation: bool`, `bool | None`,
  and union return types, plus Sage installed docs/source for number-field closures,
  algebraic roots, and matrix echelon forms.
- Found: no current Cat/functor-hom core method with a closed boolean-controlled return
  shape. Concrete source-backed hits are in ring and algebraic-number surfaces.
  `echelon_form(transformation=True)` is not patched here because Sage matrix docs/source
  allow backend-dependent behavior rather than a clean closed overload contract.
  Generic `extension(..., map=...)` forwarding needs separate source grounding before
  changing its public contract.
- Conclusion: inference - this card's executable scope is the source-backed ring/root
  overload split above, not a broad Cat/homsets rewrite.
- Confidence: Medium-high.
- Gaps: this pass covered current textual signatures and relevant Sage docs/source for
  the found hits; it is not a fresh semantic review of every Sage boolean parameter in
  every possible upstream backend.

## Complexity Justification
- Owner: C55
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Split boolean and optional return-shape signatures
- Why this specific score:
  - This is a typed-API refactor scoped to category/map methods, but it touches many call signatures and forces coherent overload behavior across public methods. The risk is concentrated (typing correctness) rather than runtime behavior, matching a moderate complexity window.
- Item-specific evidence:
  - The task is tightly scoped to `Category` and `Map` return-shape changes and calls out `bool|None` / `T|None` unbundling, indicating a coordinated but bounded interface contract clean-up.
  - No additional files are named, so validation burden is mostly static typing consistency and downstream method callsites.
