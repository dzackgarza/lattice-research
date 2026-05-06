---
id: TASK-CATEGORY-METHOD-INVENTORY-SPEC-ASSEMBLY
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING]]'
title: Assemble trackable method ownership spec files
status: unstarted
priority: critical
owner: Zack
description: Assemble the topical method rows into one or more trackable spec files
  with consistent table schema, cross-links, and no duplicated source authority.
successCriteria:
- The repository contains the final method ownership spec file or a linked family
  of method ownership spec files under the tracker hierarchy.
- All topical inventory rows use the same schema and cite source paths.
- Duplicate method names with distinct meanings are split into separate rows, and
  overloaded names state their hypotheses and codomains.
- The assembled spec links follow-up implementation, audit, smoke, or decision cards
  without creating meta-planning tasks.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Assemble trackable method ownership spec files

## Summary

Assemble the topical method rows into the durable trackable spec artifact requested by
the user. This card is complete only when the output is actual method-owner spec
content, not a list of future cards.

## Source Provenance

- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`
- Topical outputs from the sibling inventory tasks in this phase.
- Existing spec cards under
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/` when they already
  own a local method-owner decision.

## Context

The assembly pass should decide whether the inventory remains in
`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` or is split into multiple spec cards
such as sets/topology, algebra/modules, Hom/forms/lattices, posets/tensors, and backend
routing. Splitting is allowed only when it improves readability and each split file is a
real spec surface with method rows.

## Complexity And Ownership

- Owner/role: category-spec integration editor.
- Complexity: `80` (high).
- Rationale: this integrates high-risk semantic rows across subtrees but remains
  bounded to spec-file assembly and tracker cross-linking.
- Split/promote note: do not promote this into another plan. If the content is too
  large, split the spec files, not the workflow.

## Acceptance Criteria

- [ ] The repository contains the final method ownership spec file or a linked family of method ownership spec files under the tracker hierarchy.
- [ ] All topical inventory rows use the same schema and cite source paths.
- [ ] Duplicate method names with distinct meanings are split into separate rows, and overloaded names state their hypotheses and codomains.
- [ ] The assembled spec links follow-up implementation, audit, smoke, or decision cards without creating meta-planning tasks.

## Dependencies And Boundaries

- Do not replace source docs with summaries; the method inventory points to canonical
  source paths and records decisions.
- Do not create cards whose only purpose is "record grounding" unless the actual work is
  source mining for an unresolved method owner.
- Do not close the phase if any topical table is only represented by prose.

## Work Log

- 2026-05-05: Created as the spec assembly leaf for the literal method ownership inventory phase.
