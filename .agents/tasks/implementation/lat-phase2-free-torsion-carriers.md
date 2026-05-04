---
trackerStatus:
  type: task
title: Implement concrete free and torsion carriers
status: to-do
priority: critical
created: '2026-05-03'
complexity: 65
progress: 0
planId: PLN-LAT-020
tags:
- category-specs
- implementation
- lattices
- phase-plan
- theme-modules-tensors
---

# Implement concrete free and torsion carriers

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-020` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.6: Concrete Free and Torsion Carriers
- Parent plan: `PLN-LAT-020`
- Program plan: `PLN-CAT-000`

## Definition Grounding Required Before Implementation

This card is not executable from the migrated source section alone. Before editing code, the worker must record in this card or a linked spec/decision the canonical definition source, exact mathematical object, hypotheses, return/codomain, and invariance or equivalence obligations for every public noun or method touched.

For lattice/module work, start with `.agents/skills/lattice-redesign/references/category-abc-spec.md`, `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`, `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`, `theory/foundations/bilinear-forms-duals-morphisms.md`, and `theory/spec_backups/lattices_written_spec_backup.py`. Old `plans/PHASE_*.md` text is migration provenance, not standalone definition authority.

If the source section conflicts with those definitions or uses ambiguous terms, stop this leaf, update it to `blocked`, and file the needed source-mining or decision card.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/free.py; src/lattices/core/torsion.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.
