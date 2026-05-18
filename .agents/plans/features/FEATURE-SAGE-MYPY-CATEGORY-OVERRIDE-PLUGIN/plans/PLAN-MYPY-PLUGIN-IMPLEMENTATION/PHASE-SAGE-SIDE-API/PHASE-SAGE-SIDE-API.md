---
id: PHASE-SAGE-SIDE-API
trackerStatus:
  type: phase
parents:
- '[[PLAN-MYPY-PLUGIN-IMPLEMENTATION]]'
dependsOn: []
title: Sage introspection API
status: needs-review
priority: high
description: 'Build the introspection module that maps source-level method-container fullnames
  to Sage category instances, queries their dynamic parent_class/element_class/morphism_class
  bases, and projects those back to source-level container fullnames for the mypy plugin.
  Admission must work for importable Sage category subtrees outside `sage.categories.*`.
  Lives in the standalone `~/sage-mypy-plugin/` repo.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-MYPY-PARSER]]'
- '[[TASK-MYPY-INSTANTIATE]]'
- '[[TASK-MYPY-DIRECT-BASES]]'
- '[[TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION]]'
successCriteria:
- parser correctly extracts category path and method kind from fullnames
- instantiation succeeds for singleton categories via an_instance()
- "direct_bases returns correct source container fullnames for a representative category (e.g.,\
  \ Rings.ParentMethods \u2192 [Rngs.ParentMethods, Semirings.ParentMethods])"
- debug_projection produces expected output shape
- parser/admission does not reject a valid third-party subtree solely because
  its fullname is outside `sage.categories.*`
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
---
# Phase: Sage Introspection API

## Summary

Build the introspection layer that the mypy plugin calls at type-checking time.
Uses Sage's existing `an_instance()`, `parent_class`, `element_class`,
`morphism_class`, and `all_super_categories()` — no Sage source modification.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`, sections:
  "Sage-Side Helper: Direct Dynamic-Base Projection",
  "Category Instantiation Rule",
  "Debug Oracle",
  "Minimal Implementation Surface"

## Location

- Repo: `~/sage-mypy-plugin/`
- Module: `sage_mypy_category_plugin/introspection.py`
- Imports Sage at runtime; no files placed inside Sage's source tree.

## Task Cards

- `TASK-MYPY-PARSER`: Implement `parse_method_container_fullname` and
  `is_sage_method_container`
- `TASK-MYPY-INSTANTIATE`: Implement `instantiate_category_from_source_path`
- `TASK-MYPY-DIRECT-BASES`: Implement `method_container_direct_bases`,
  `module_method_container_dependencies`, and `debug_projection`
- `TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION`: Separate semantic validation from
  `sage.categories.*` namespace assumptions so third-party subtrees are admissible

## Exit Criteria

- `method_container_direct_bases("sage.categories.rings.Rings.ParentMethods")`
  returns correct ancestor list
- Debug oracle command produces valid output
- All three sub-functions have docstrings and type annotations

## Work Log

- Created 2026-05-10.
- Corrected 2026-05-10: lives in standalone repo, not in Sage source tree.
- Reopened 2026-05-10 after confirming that parser/admission logic currently
  hard-codes a `sage.categories.*` requirement and rejects repo-local
  `category_specs.*` method containers.
- Updated 2026-05-10: `parse_method_container_fullname()` is now
  namespace-agnostic, the introspection path preserves semantic validation for
  unrelated classes, and repo-local `category_specs.*` reproduction now passes
  through projection when the plugin is enabled.

## Current Status

Needs review. The introspection API now keeps namespace and semantic validation
separate, accepts valid importable third-party subtrees, and still rejects
unrelated `ParentMethods`-shaped classes that do not resolve to Sage category
semantics.
