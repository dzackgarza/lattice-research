---
id: PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
dependsOn: []
title: Category literal method inventory and ownership
status: needs-review
priority: critical
owner: Zack
description: Build source-grounded method ownership spec files that list every literal
  expected method and the minimal category or construction owner that introduces it.
successCriteria:
- The method inventory target spec is filled or split into smaller method-owner spec
  cards with the required row format.
- Sets, topology, algebra, modules, Hom/End/Aut, forms, lattices, tensors, posets,
  geometry, and backend-routed methods are covered by source-grounded rows.
- External software capability maps are translated into method/backend ownership rows
  with explicit codomains and routing status.
- All unresolved owner conflicts are converted into decision cards rather than left
  as prose or implementation guesswork.
tasks:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-SPEC-ASSEMBLY]]'
- '[[TASK-CATEGORY-METHOD-INVENTORY-GAP-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
---
# Category literal method inventory and ownership

## Summary

Build the exhaustive method-owner inventory required by
`SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`. The phase is complete only when
the repo has actual trackable spec files that answer which mathematical category or
construction first introduces each expected method.

## Source Provenance

- Parent plan: `PLAN-CATEGORY-FOUNDATION-KERNEL`.
- Target spec card: `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`.
- Current inventory roots: `category_specs/*/docs/SAGE_INVENTORY.md` and
  `category_specs/*/docs/MAPPING.md`.
- External method mapping roots: `theory/backends/software-capability-map.md`,
  `theory/backends/abstract-to-external-mapping.md`, and backend-specific notes under
  `theory/backends/`.
- Lattice-source warning: `theory/spec_backups/*` files may be mined for mathematical
  content, but their interface can change and they are not current implementation
  authority.

## Context

The existing plans already contain many method-owner decisions, but they are spread
across mapping docs, source inventories, lattice notes, backend maps, and tracker cards.
This phase centralizes them into a literal inventory organized by minimal owner
subcategory. The output prevents downstream work from treating method names as obvious
or letting Sage implementation inheritance masquerade as mathematical ownership.

## Acceptance Criteria

- [x] The method inventory target spec is filled or split into smaller method-owner spec cards with the required row format.
- [x] Sets, topology, algebra, modules, Hom/End/Aut, forms, lattices, tensors, posets, geometry, and backend-routed methods are covered by source-grounded rows.
- [x] External software capability maps are translated into method/backend ownership rows with explicit codomains and routing status.
- [x] All unresolved owner conflicts are converted into decision cards rather than left as prose or implementation guesswork.

## Dependencies And Boundaries

- This is spec work, not implementation. It may create or update spec cards and
  decision cards; it should not edit category implementation files.
- A method row may reject a Sage method as public API, but the rejection must name the
  replacement surface or explain why the method is interop-only.
- Method owners must be minimal in the category refinement order. Inherited availability
  is a consequence, not an owner.
- When a method name has multiple meanings, split the meanings into separate rows
  instead of forcing one owner.

## Work Log

- 2026-05-05: Created phase to execute the literal method ownership inventory requested by the user.
- 2026-05-06: Started phase execution by completing the source corpus assignment in the target spec.
- 2026-05-06: Completed topical row assembly, gap audit, and decision/source routing;
  marked phase needs-review pending human acceptance.
