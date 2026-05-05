---
trackerStatus:
  type: task
title: Audit category-spec duck-type object-shape probes
status: to-do
priority: critical
planId: SPR-DUCKTYPE-AUDIT-20260505
complexity: 60
progress: 0
created: '2026-05-05'
updated: '2026-05-05'
tags:
- category-specs
- implementation
- task
- audit
- theme-audit-uniformity
---

# Audit category-spec duck-type object-shape probes

## Summary

Audit category-spec implementation code for `getattr`, `hasattr`, optional attribute
fallbacks, and private-slot probes that infer object shape instead of matching real
Sage/project types, documented wrappers, or category membership.

## Source Provenance

- Owning sprint: `SPR-DUCKTYPE-AUDIT-20260505`.
- Parent audit plan: `PLN-AUDIT-000`.
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

- [ ] Scan `category_specs/` implementation files for `getattr`, `hasattr`, optional
  attribute fallback, and private-slot probe patterns.
- [ ] For each finding, record whether the branch is Sage interop, a documented wrapper
  boundary, real category/type dispatch, or invalid duck-type probing.
- [ ] Replace invalid probes with real Sage/project type checks, category
  membership/subcategory checks, or named wrapper/accessor boundaries when the fix is
  local and source-backed.
- [ ] Split any nonlocal or mathematically ambiguous remediation into owner-scoped
  follow-up cards instead of guessing inside the audit.
- [ ] Do not weaken smokes or add broad exception-catching to hide the audit finding.

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
  duck-type object-shape probing is audited deliberately during `PLN-AUDIT-000`, not
  opportunistically inside unrelated smoke implementation work.
