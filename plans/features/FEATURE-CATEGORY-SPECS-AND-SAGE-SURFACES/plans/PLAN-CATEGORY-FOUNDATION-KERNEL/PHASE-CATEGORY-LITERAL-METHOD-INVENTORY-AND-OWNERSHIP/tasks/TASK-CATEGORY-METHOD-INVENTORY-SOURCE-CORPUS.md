---
id: TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn: []
title: Build source corpus for literal method ownership inventory
status: unstarted
priority: critical
owner: Zack
description: Enumerate the local inventory, mapping, theory, backend, and spec-backup
  sources that must be mined before method-owner rows are written.
successCriteria:
- The target method-inventory spec records the complete source corpus with paths and
  per-source scope.
- Every `category_specs/*/docs/SAGE_INVENTORY.md` and `category_specs/*/docs/MAPPING.md`
  file is assigned to a topical inventory task.
- Backend and external software notes under `theory/backends/` are assigned to the
  backend mapping task, including Julia/Oscar, GAP, Singular, Macaulay2, CARAT, and
  Indefinite.jl material where present.
- '`theory/spec_backups/*` is marked as mineable source material with the explicit
  warning that it is not current API authority.'
complexity: 55
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Build source corpus for literal method ownership inventory

## Summary

Enumerate the source corpus for the method ownership inventory before writing method
rows. This card is the only corpus-building leaf. Later leaves must use its assignment
rather than rediscovering sources ad hoc.

## Source Provenance

- `category_specs/cat/docs/SAGE_INVENTORY.md`
- `category_specs/cat/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`
- `category_specs/topological_spaces/docs/MAPPING.md`
- `category_specs/rings/docs/SAGE_INVENTORY.md`
- `category_specs/rings/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/algebras/docs/SAGE_INVENTORY.md`
- `category_specs/algebras/docs/MAPPING.md`
- `category_specs/homsets/docs/SAGE_INVENTORY.md`
- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/forms/docs/SAGE_INVENTORY.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- `category_specs/lattices/docs/MAPPING.md`
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- `category_specs/tensor_algebra_components/docs/MAPPING.md`
- `category_specs/posets/docs/SAGE_INVENTORY.md`
- `category_specs/posets/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`
- `theory/backends/abstract-to-external-mapping.md`
- `theory/backends/library-integration.md`
- `theory/backends/comprehensive-tool-docs.md`
- `theory/backends/oscar-lattices.md`
- `theory/backends/gap-orbits.md`
- `theory/backends/indefinite-jl.md`
- `theory/backends/carat.md`
- `theory/backends/vinberg-algorithm.md`
- `theory/spec_backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`
- `theory/spec_backups/lattices_written_spec_backup.py`

## Context

The user asked for all literal expected methods and the subcategory that introduces
each method. The work therefore starts with a corpus map. A method row without a source
path is not acceptable.

## Complexity And Ownership

- Owner/role: category-spec source-mining implementer.
- Complexity: `55` (moderate).
- Rationale: the work touches many files but produces a bounded source assignment,
  not mathematical ownership decisions.
- Split/promote note: do not split unless new inventory families are discovered outside
  the listed corpus.

## Acceptance Criteria

- [ ] The target method-inventory spec records the complete source corpus with paths and per-source scope.
- [ ] Every `category_specs/*/docs/SAGE_INVENTORY.md` and `category_specs/*/docs/MAPPING.md` file is assigned to a topical inventory task.
- [ ] Backend and external software notes under `theory/backends/` are assigned to the backend mapping task, including Julia/Oscar, GAP, Singular, Macaulay2, CARAT, and Indefinite.jl material where present.
- [ ] `theory/spec_backups/*` is marked as mineable source material with the explicit warning that it is not current API authority.

## Dependencies And Boundaries

- Do not write final method-owner rows here unless they are needed to illustrate the
  corpus assignment format.
- Do not use `theory/spec_backups/*` as current API authority. Treat it as mathematical
  source material requiring later reconciliation.
- If another inventory root is found, add it to the corpus and assign it to exactly one
  topical task.

## Work Log

- 2026-05-05: Created as first leaf for the literal method ownership inventory phase.
