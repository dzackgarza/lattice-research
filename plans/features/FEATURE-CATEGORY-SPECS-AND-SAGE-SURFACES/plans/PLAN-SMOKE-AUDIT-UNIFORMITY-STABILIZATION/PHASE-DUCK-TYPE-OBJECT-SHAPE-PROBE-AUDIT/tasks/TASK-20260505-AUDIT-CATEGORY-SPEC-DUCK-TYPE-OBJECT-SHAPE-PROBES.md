---
id: TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES
trackerStatus:
  type: task
parents:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
dependsOn: []
title: Audit category-spec duck-type object-shape probes
status: needs-review
priority: critical
description: Audit category-spec implementation code for `getattr`, `hasattr`, optional
  attribute fallbacks, and private-slot probes that infer object shape instead of
  matching real Sage/project types, documented wrappers, or category membership.
successCriteria:
- Scan `category_specs/` implementation files for `getattr`, `hasattr`, optional attribute
  fallback, and private-slot probe patterns.
- For each finding, record whether the branch is Sage interop, a documented wrapper
  boundary, real category/type dispatch, or invalid duck-type probing.
- Replace invalid probes with real Sage/project type checks, category membership/subcategory
  checks, or named wrapper/accessor boundaries when the fix is local and source-backed.
- Split any nonlocal or mathematically ambiguous remediation into owner-scoped follow-up
  cards instead of guessing inside the audit.
- Do not weaken smokes or add broad exception-catching to hide the audit finding.
complexity: 60
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
- PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT
---
# Audit category-spec duck-type object-shape probes

## Summary

Audit category-spec implementation code for `getattr`, `hasattr`, optional attribute
fallbacks, and private-slot probes that infer object shape instead of matching real
Sage/project types, documented wrappers, or category membership.

## Source Provenance

- Owning sprint: `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT`.
- Parent audit plan: `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`.
- Repo style policy: `.agents/skills/category-spec-style/references/style.md`.
- Proof-audit warning:
  `.agents/skills/research-proof-auditing/references/proof-auditing.md`.
- Lattice interface audit guidance:
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- Triggering observation: 2026-05-05 smoke implementation exposed `getattr`/`hasattr`
  patterns in category-spec set wrappers; the user directed that this be left to a
  real audit phase rather than fixed opportunistically inside the active smoke card.

## Context

Duck-type object-shape probes are dangerous in category-spec code because they make
mathematical dispatch depend on storage accidents. The audit should distinguish
between legitimate Sage interop machinery and project code that should instead use
source-backed type checks, explicit wrapper classes, named accessors, or category
membership/subcategory predicates.

## Complexity And Ownership

- Owner role: category-spec audit worker, with parent-agent review.
- Complexity: 60, moderate band.
- Rationale: the first pass is a bounded static audit across category-spec implementation
  surfaces plus classification. Remediation may touch several files, but independent
  owner surfaces should be split rather than handled as one broad rewrite.

## Acceptance Criteria

- [x] Scan `category_specs/` implementation files for `getattr`, `hasattr`, optional
  attribute fallback, and private-slot probe patterns.
- [x] For each finding, record whether the branch is Sage interop, a documented wrapper
  boundary, real category/type dispatch, or invalid duck-type probing.
- [x] Replace invalid probes with real Sage/project type checks, category
  membership/subcategory checks, or named wrapper/accessor boundaries when the fix is
  local and source-backed.
- [x] Split any nonlocal or mathematically ambiguous remediation into owner-scoped
  follow-up cards instead of guessing inside the audit.
- [x] Do not weaken smokes or add broad exception-catching to hide the audit finding.

## Static Audit Result

- `category_specs/cat/base_category_types.py`: constructor forwarding, provider
  assembly, predicate validation, and Sage axiom descriptor interop. Classified as
  documented Sage/project wrapper boundary or real category dispatch.
- `category_specs/cat/subcategories/constructions/subobjects.py`: invalid
  object-shape probes on `ambient_category` and `defining_predicates`. Replaced with
  matching against the project `CategoryWithAxiom` wrapper classes before calling the
  required methods.
- `category_specs/sets/__init__.py`: root `Sets().__contains__` used optional
  `category` lookup. Replaced with the real Sage `Parent` type boundary plus Sage
  category membership. The generic `element_class` check remains classified as Sage
  parent interop.
- `category_specs/sets/subcategories/image.py`: local `ImageSubobject` wrapper probes
  Sage backing storage. Classified as documented wrapper boundary.
- `category_specs/sets/subcategories/integer_range.py`,
  `category_specs/sets/subcategories/enumerated_from_iterator.py`, and
  `category_specs/sets/subcategories/recursively_enumerated.py`: private-slot and
  optional-attribute probes require Sage source grounding before rewrite. Routed to
  `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES`.
- `category_specs/utils.py`: class/module and abstract-method inspection. Classified
  as project validation boundary, not mathematical object-shape dispatch.

## Dependencies And Boundaries

- This card belongs to the audit phase and should not block ordinary approved smoke
  implementation cards unless a duck-type probe is the direct cause of the active
  failure being fixed.
- Do not replace Sage internals or documented Sage dispatch mechanics merely because
  they contain `getattr`/`hasattr`; classify those separately.
- Do not use this card to perform unrelated typing cleanup, formatter normalization, or
  API redesign.

## Validation Requirements

- Run a targeted static search showing remaining `getattr`/`hasattr` patterns and their
  classifications.
- Run the narrowest relevant category-spec smoke or static checks for files changed by
  local remediations.
- If validation is skipped because this card only routes findings, record that clearly
  in the work log.

## Work Log

- 2026-05-05: Created from user correction and routing decision. This card exists so
  duck-type object-shape probing is audited deliberately during `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`, not
  opportunistically inside unrelated smoke implementation work.
- 2026-05-06: Ran static searches for `getattr`, `hasattr`, optional fallbacks, private
  slots, and `try`/attribute fallback patterns under `category_specs/`. Fixed the two
  local invalid implementation probes in `Cat().Subobjects().__contains__` and
  `Sets().__contains__`. Left source-dependent set-wrapper private-slot cases to
  `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES` instead of guessing.
  No smoke assertions or spec obligations were weakened.
