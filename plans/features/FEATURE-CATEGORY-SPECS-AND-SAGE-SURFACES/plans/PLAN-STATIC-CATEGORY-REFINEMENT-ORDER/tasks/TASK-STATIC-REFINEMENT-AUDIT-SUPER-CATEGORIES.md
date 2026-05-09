---
id: TASK-STATIC-REFINEMENT-AUDIT-SUPER-CATEGORIES
trackerStatus:
  type: task
parents:
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
dependsOn: []
title: Audit all super_categories() returns against admitted-edges table
status: unstarted
priority: critical
description: 'Enumerate every super_categories() call in category_specs/, compare against
  the admitted-edges table in PLAN-STATIC-CATEGORY-REFINEMENT-ORDER, and produce a
  gap report listing undocumented edges with their source file and line number.'
successCriteria:
- Every super_categories() return in category_specs/ is inventoried with file path
  and line number.
- Each return is classified as: documented in table, missing from table, or exempt
  (construction category, axiom class with empty return, etc.).
- Gap report is written into the plan body as an extension of the admitted-edges
  table.
- Contradictions (table says X but code returns Y) are flagged with exact evidence.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
---
# Audit all super_categories() returns against admitted-edges table

## Summary

The 6-gate review of PLAN-STATIC-CATEGORY-REFINEMENT-ORDER found that the
admitted-edges table (11 rows) covers only ~20% of the ~30+ `super_categories()`
calls in `category_specs/`. This task inventories every call, classifies each one,
and produces a gap report.

## Method

1. Search: `rg -n "super_categories\(" category_specs/ --include='*.py'`
2. For each hit, extract the file, line number, and the returned list
3. Cross-reference against the plan's admitted-edges table
4. Classify each as: documented / undocumented / exempt
5. Flag contradictions where the table and code disagree
6. Write results into the plan body

## Known contradictions to verify

- `PartitionedSetsCategory` returns `[]` (empty) but the table claims
  `Sets().Countable()` and `Sets().Subobjects()` — either code or table is wrong.
- Rings subcategory hierarchy (Fields, Commutative, IntegralDomain, etc.) has
  dozens of `super_categories()` returns not in the table.
- Topological spaces categories not in table.
- Construction categories (CartesianProducts, Quotients, Subobjects, etc.) not in table.

## Output

Write a new section `## Audited super_categories() inventory` into the plan body
with the full inventory and gap classification.
