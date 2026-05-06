---
id: TASK-1777748120440-BRC1SX-SPLIT-BOOLEAN-AND-OPTIONAL-RETURN-SHAPE-SIGNATURES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Split boolean and optional return-shape signatures
status: needs-review
priority: critical
description: Split boolean and optional return-shape signatures
successCriteria:
- Split boolean and optional return-shape signatures is resolved according to the
  body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Split boolean and optional return-shape signatures
Source: pasted backlog 2026-05-02.

Task: split the mixed boolean|None and T|None return-type signatures on Category and Map classes into explicit @overload declarations.

## Grounding

- Source provenance: recovered variadic sprint source at
  `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` in commit
  `8d1c21c^`, plus the current sprint plan
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT.md`.
- Style authority: `.agents/skills/category-spec-style/references/style.md` requires
  closed overloads for finite Sage casework and source-backed return objects.
- Sage grounding:
  - `NumberField.galois_closure(map=False)` returns the Galois closure field, while
    `map=True` returns the field with an embedding of the source field into it.
  - Algebraic `nth_root(all=False)` and `sqrt(all=False)` return one root; `all=True`
    returns the finite list of all roots.
- Canonical local mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`
  records the overload policy, exact Sage source paths, owner categories, hypotheses,
  codomains, and branch-choice obligations for these boolean-controlled return-shape
  methods.
- Exact Sage sources:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/number_field/number_field.py:9177-9219`
  for `NumberField.galois_closure(names=None, map=False)`;
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/structure/element.pyx:3263-3284`,
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/qqbar.py:4312-4329`,
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/complex_mpfr.pyx:2988-2997`
  for `sqrt(..., all=...)`; and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/qqbar.py:4393-4429`
  plus
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/rings/complex_mpfr.pyx:3058-3079`
  for `nth_root(n, all=...)`.
- Owner/codomain contract: `galois_closure` belongs to number-field parent methods and
  returns either the closure field or `(closure field, source embedding)`;
  `sqrt` and `nth_root` belong to ring element methods on root-capable ring/field
  element surfaces and return either one root or the finite list of all roots. The
  overload split types Sage's documented branch behavior; it does not assert
  choice-independent equality of selected roots or Galois-closure presentations.

## Result

- Added `Literal[False]`, `Literal[True]`, and non-literal `bool` fallback overloads
  for root-return shapes in `category_specs/rings/__init__.py`.
- Added the same overload split for specialized `nth_root` overrides in
  `category_specs/rings/subcategories/algebraic_closure_of_rational_field.py` and
  `category_specs/rings/subcategories/real_algebraic_field.py`.
- Added `map=False`/`map=True` overloads plus a non-literal `bool` fallback for
  `galois_closure` in `category_specs/rings/subcategories/number_field.py` and
  `category_specs/rings/subcategories/rational_field.py`.

## Review Log

### Review 2026-05-06 (Dirac)

**Gates passed:** None
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Source-Grounding For Boolean Return Shapes

- The card introduced public overloads for `nth_root`/`sqrt` and `galois_closure`, but
  grounded them only in prose behavior and the legacy `category_specs/rings/docs/MAPPING.md`
  redirect.
- The canonical rings spec recorded the return-shape policy but did not yet record exact
  Sage source paths, definitions, owner categories, hypotheses, codomains, or branch
  choice/equivalence obligations for each affected method.

#### Rework

- Added exact installed Sage source paths for `galois_closure`, `sqrt`, and
  `nth_root` to this card and to `SPEC-MAPPING-RINGS.md`.
- Recorded the owner category, hypotheses, codomain/return object, and branch-choice
  obligation for each affected overload family.

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
