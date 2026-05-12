---
id: TASK-MYPY-HOOK-CALLBACK
trackerStatus:
  type: task
parents:
- '[[PHASE-MYPY-SIDE-HARNESS]]'
dependsOn:
- '[[TASK-MYPY-PLUGIN-CLASS]]'
title: Implement MRO hook callback for base injection
status: revision-required
priority: high
description: 'Implement sage_method_container_mro_hook: calls method_container_direct_bases,
  resolves each to a mypy TypeInfo, injects into the class MRO. Handles deferral when TypeInfo
  not yet available.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- hook callback calls introspection API correctly
- TypeInfo lookup succeeds for all ancestor containers (or defers)
- injected bases appended after explicit bases
- MRO recalculated after injection
complexity: 25
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-MYPY-SIDE-HARNESS
---
# Task: Implement MRO Hook Callback

## Summary

Implement `sage_method_container_mro_hook(ctx)` — the callback that does the
actual base injection during mypy type-checking.

## Context

Pseudo-procedure from the technical addendum:
1. Get `info.fullname` from `ctx.cls.info`
2. Call `method_container_direct_bases(fullname)` → list of ancestor fullnames
3. For each: `lookup_typeinfo(ctx, base_fullname)` → TypeInfo
4. If any missing: `ctx.api.defer()` and return
5. Inject all TypeInfos as bases (after explicit bases)
6. Recalculate MRO

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`:
  "Hook Callback Behavior" (pseudo-procedure)

## Acceptance Criteria

- Works for a category with one ancestor
- Works for a category with multiple ancestors (preserves Sage order)
- Explicit bases on the method container are preserved (come first)
- Missing TypeInfo triggers deferral (does not crash)
- Hook does not run for non-Sage-method-container classes
- Hook path works for an eligible third-party subtree fullname outside
  `sage.categories.*`

## Work Log

- Reopened 2026-05-10 after confirming that the current callback path is not
  actually reached for repo-local `category_specs.*` containers because the
  plugin's prefix gate filters them out first.

## Current Status

Revision required. Base injection logic exists, but the clarified external-subtree
contract is not satisfied until valid non-Sage namespaces can reach the callback.
