---
title: Category Spec Graph Minimality — Immediate Parents Only
date: 2026-05-27
status: active
---
# Rule: `super_categories()` Must List Immediate Mathematical Parents Only

## The principle

A category's `super_categories()` should return only its **immediate** mathematical
parents. It should not list derived ancestors, consequence closures, or compensatory
direct attachments to categories that should be reachable through the graph.

## What violates minimality

- Listing `_Fields()` directly when the category is already under `_NumberFields` or
  `_GlobalFields`, and those categories themselves refine `_Fields`.
- Listing multiple direct ancestors that form a chain (e.g., `_QQ` listing `_Fields`,
  `_NumberFields`, `_GlobalFields` when the intended graph is
  `NumberFields <= GlobalFields <= Fields`).
- Listing theorem-level consequences as parents (e.g., `FiniteSets` listing `Countable`
  when finite-implies-countable is a derived property, not a direct parent).
- Including `SageXxx()` categories inside the local spec tree.
  Root entry points (e.g., `Rings`) may legitimately bridge to Sage root categories.
  Internal subcategories should inherit through local parents.

## The test

For any category with more than one project-local supercategory, classify each parent:

- **Valid root Sage bridge**: root entry category attaches to Sage root category.
- **Valid local immediate parent**: ordinary internal spec inheritance.
- **True mixed-structure**: category genuinely combines independent structures.
- **Redundant consequence closure**: lists derived parents that should be inferred.
- **Missing edge**: a required local parent is absent, causing compensatory direct
  attachments.
- **Wrong/misnamed edge**: mathematical inclusion is incorrect (e.g., `QuotientFields`
  for fraction fields/localizations).

## The fix

If a category lists redundant ancestors, the fix is usually in the graph, not in the
category. Add the missing edge to the intermediate category, then remove the redundant
direct attachment.
