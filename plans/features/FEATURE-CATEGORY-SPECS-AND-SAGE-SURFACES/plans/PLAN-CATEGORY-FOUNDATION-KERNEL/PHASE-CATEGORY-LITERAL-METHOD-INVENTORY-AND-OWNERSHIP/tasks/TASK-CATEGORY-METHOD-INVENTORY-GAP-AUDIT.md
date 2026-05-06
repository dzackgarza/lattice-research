---
id: TASK-CATEGORY-METHOD-INVENTORY-GAP-AUDIT
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SPEC-ASSEMBLY]]'
title: Audit method inventory gaps and create owner decisions
status: needs-review
priority: high
owner: Zack
description: Audit the assembled method ownership spec for missing owners, duplicated
  meanings, ambiguous codomains, backend gaps, and implementation-poisoning risks.
successCriteria:
- Every `decision-needed`, `backend-gap`, or `source-needed` row has a linked decision
  or research card with exact sources checked.
- The inventory has no method rows that cite only migrated TODOs, common terminology,
  or plausible textbook memory as authority.
- The audit records which implementation cards are now unblocked and which paths remain
  blocked by real source or decision gaps.
- The phase can be marked needs-review without relying on global QC as proof of spec
  completeness.
complexity: 58
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Audit method inventory gaps and create owner decisions

## Summary

Audit the assembled method-owner inventory for gaps and ambiguity. This is an audit of
spec completeness, not a QC phase transition.

## Source Provenance

- Assembled method-owner spec files from this phase.
- Decision cards under
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/`.
- Backend and source-acquisition cards created by the sibling tasks.
- Category-spec audit skill criteria and local anti-confabulation rules in `AGENTS.md`.

## Context

The inventory is useful only if missing owners are visible and trackable. This audit
must catch rows where a method name is present but the mathematical owner, hypotheses,
codomain, or backend route is still unclear.

## Complexity And Ownership

- Owner/role: category-spec audit reviewer.
- Complexity: `58` (moderate).
- Rationale: this is bounded review and card creation, but it requires checking
  mathematical grounding and dependency effects across the assembled inventory.
- Split/promote note: individual unresolved conflicts should become decision cards, not
  sub-plans.

## Acceptance Criteria

- [x] Every `decision-needed`, `backend-gap`, or `source-needed` row has a linked decision or research card with exact sources checked.
- [x] The inventory has no method rows that cite only migrated TODOs, common terminology, or plausible textbook memory as authority.
- [x] The audit records which implementation cards are now unblocked and which paths remain blocked by real source or decision gaps.
- [x] The phase can be marked needs-review without relying on global QC as proof of spec completeness.

## Dependencies And Boundaries

- QC is not the blocker for this spec phase unless the user asks for a phase transition.
- Do not create broad "audit everything later" cards. Each unresolved issue gets a
  specific owner-decision or source-mining card.
- Do not downgrade ambiguous mathematics into implementation TODOs.

## Work Log

- 2026-05-05: Created as the gap-audit leaf for the literal method ownership inventory phase.
- 2026-05-06: Audited the assembled inventory for `decision-needed`, `source-needed`,
  and backend-gap rows; linked geometry gaps to existing source-admission research
  cards, linked q-adic and backend gaps to existing specs/tasks, and created
  `DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER` for the remaining
  Picard group/lattice owner split.
