---
id: TASK-MYPY-PARSER
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn: []
title: Implement parse_method_container_fullname and is_sage_method_container
status: needs-agent-review
priority: high
description: 'Implement the fullname parser in ~/sage-mypy-plugin/sage_mypy_category_plugin/introspection.py
  that splits a dotted fullname into module + category path + method kind.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- "parse_method_container_fullname(\"sage.categories.rings.Rings.ParentMethods\") \u2192 CategoryMethodContainer(module=\"\
  sage.categories.rings\", category_path=(\"Rings\",), method_kind=\"ParentMethods\")"
- "parse_method_container_fullname(\"sage.categories.objects.Objects.Homsets.ParentMethods\"\
  ) \u2192 CategoryMethodContainer(module=\"sage.categories.objects\", category_path=(\"Objects\"\
  , \"Homsets\"), method_kind=\"ParentMethods\")"
- Parser does not reject a valid third-party subtree solely because the fullname
  is outside `sage.categories.*`; namespace and semantic validation are separate
- "parse_method_container_fullname(\"some.random.ParentMethods\") \u2192 None"
- is_sage_method_container returns True for the above, False for non-Sage paths
- 'Accepted terminal names: ParentMethods, ElementMethods, MorphismMethods, SubcategoryMethods'
complexity: 15
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Implement Fullname Parser

## Summary

Implement `parse_method_container_fullname` and `is_sage_method_container` in
`~/sage-mypy-plugin/sage_mypy_category_plugin/introspection.py`.

## Context

These functions parse a dotted Python fullname like
`sage.categories.rings.Rings.ParentMethods` into its components:
the module, the dotted category path within the module, and the method kind
(ParentMethods/ElementMethods/MorphismMethods/SubcategoryMethods).

`is_sage_method_container` is the gatekeeper: it should reject random classes
named `ParentMethods`, but it must not confuse "not under `sage.categories.*`"
with "not a Sage category subtree."

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`:
  "Matching Target Classes", "Sage-Side Helper"

## Acceptance Criteria

- Parser handles flat categories: `Rings.ParentMethods` → path=("Rings",), kind="ParentMethods"
- Parser handles nested paths: `Objects.Homsets.ParentMethods` → path=("Objects", "Homsets"), kind="ParentMethods"
- Parser handles axiom paths: `Monoids.Finite.ParentMethods` → path=("Monoids", "Finite"), kind="ParentMethods"
- Parser rejects terminal names that aren't recognized method kinds
- Rejects fullnames where the enclosing class isn't a Sage category

## Dependencies And Boundaries

None. This is the first task in the phase.

## Work Log

- Reopened 2026-05-10 after confirming that the current parser/admission path
  hard-codes a `sage.categories.*` prefix requirement and therefore rejects the
  repo-local `category_specs.*` subtree before semantic validation.
- Updated 2026-05-10: parser now splits on the first class-like segment instead
  of requiring a Sage prefix, so
  `category_specs.algebras.subcategories.semisimple._SemisimpleAlgebras.ParentMethods`
  parses successfully while `some.random.ParentMethods` still returns `None`.

## Current Status

Needs agent review. The parser now supports namespace-agnostic structural admission and
preserves the semantic boundary for unrelated non-category fullnames.
