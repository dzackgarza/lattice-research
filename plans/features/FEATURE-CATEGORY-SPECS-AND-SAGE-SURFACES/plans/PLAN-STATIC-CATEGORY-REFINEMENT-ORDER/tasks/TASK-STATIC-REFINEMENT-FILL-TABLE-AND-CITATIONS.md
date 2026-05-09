---
id: TASK-STATIC-REFINEMENT-FILL-TABLE-AND-CITATIONS
trackerStatus:
  type: task
parents:
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
dependsOn:
- '[[TASK-STATIC-REFINEMENT-AUDIT-SUPER-CATEGORIES]]'
title: Fill admitted-edges table with audit results and add source citations
status: unstarted
priority: critical
description: 'Using the audit gap report, add missing rows to the admitted-edges table,
  add source citations (MAPPING.md file or Sage source path) to every row, fix the
  PartitionedSets contradiction, and remove or decision-card any edges whose supercategories
  are not yet settled.'
successCriteria:
- Every documented super_categories() edge in the admitted-edges table has a traceable
  source citation (MAPPING.md path, Sage source path, or decision card ID).
- The PartitionedSets contradiction is resolved: either the code is corrected to
  match the table, or the table is corrected to match the code, with justification.
- Edges whose supercategories are not yet settled are either removed from the table
  or linked to an approved decision card.
- The table is brought into agreement with the audit inventory for all non-exempt
  edges.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
---
# Fill admitted-edges table with audit results and add source citations

## Summary

The audit from TASK-STATIC-REFINEMENT-AUDIT-SUPER-CATEGORIES will produce a gap
report. This task takes that report and brings the admitted-edges table into
agreement with the codebase: adding missing rows, citing sources, fixing
contradictions, and handling unsettled edges.

## Actions

1. For each undocumented edge from the audit: add a row to the admitted-edges
   table with the subcategory, its supercategories, and a source citation.
2. For each existing row without a source citation: find the controlling
   MAPPING.md or Sage source and add it.
3. For the PartitionedSets contradiction: inspect
   `category_specs/sets/subcategories/partitioned.py` to determine the actual
   `super_categories()` return. If it returns `[]`, fix the table. If it should
   return `[Sets().Countable(), Sets().Subobjects()]`, fix the code.
4. For edges referencing unsettled supercategories: remove from the table or
   link to an approved decision card.
5. Run `just plan-validate` after changes.

## Source citation format

Each row's justification must cite at least one of:
- `category_specs/<subtree>/docs/MAPPING.md` with line reference
- Sage source path (e.g., `sage/categories/rings.py`) with class/method reference
- Decision card ID (e.g., `[[DECISION-...]]`) for deferred edges

Prose justifications without file paths ("Free modules are modules") are not
acceptable per the 6-gate review G1 finding.
