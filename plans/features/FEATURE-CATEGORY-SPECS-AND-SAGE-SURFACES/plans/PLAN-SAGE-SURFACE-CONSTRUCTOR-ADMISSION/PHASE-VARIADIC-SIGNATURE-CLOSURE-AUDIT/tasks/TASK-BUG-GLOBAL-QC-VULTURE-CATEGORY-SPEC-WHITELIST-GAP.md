---
id: TASK-BUG-GLOBAL-QC-VULTURE-CATEGORY-SPEC-WHITELIST-GAP
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Resolve category-spec vulture findings through code fixes, not whitelist entries
status: unstarted
priority: high
description: 'Resolve the 762 category-spec vulture findings by fixing the code, not by
  expanding the global vulture whitelist. The whitelist approach was the wrong framing.'
successCriteria:
- "Classify each vulture finding into one of three buckets: underscore-prefix for internal helpers, smoke/test call for genuinely public surfaces, or delete for actual dead code."
- "For underscored items: verify the item is used at least once in its own file. An underscored item with zero local callers is suspect."
- "For public surfaces: add a smoke or test call that exercises the surface. The call proves category wiring correctness and gives vulture a cross-file usage to see."
- "Delete genuinely dead code that is neither an intentional internal helper nor a public vocabulary item."
- "Do not add any new entries to the global vulture whitelist."
- "Do not add local vulture bypasses, ignore files, or QC overrides."
- "After cleanup, run `just test` and verify vulture passes."
complexity: 76
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Resolve category-spec vulture findings through code fixes

## Summary

The original framing (expand the global vulture whitelist) was wrong. The vulture
findings are not false positives from a tool that doesn't understand our patterns.
They are genuine signals that our code has unreferenced names. The fix is in the
code, not in a bypass file.

This card is not blocked. It is a ready cleanup/audit task on the DAG: execute it
only when it is selected from the ready frontier, and do not mark it blocked unless
the selected cleanup path hits a real external prerequisite.

## Why the whitelist approach was wrong

- The repo style guide explicitly forbids `__all__` exports and requires Python's
  underscore convention for public/private distinction (`research-code-style` lines
  230--235).
- Vulture respects this convention: names starting with `_` are automatically
  ignored.
- Vulture does cross-file analysis: if `Foo` in `types.py` is imported and used in
  `rings/subcategories/fields.py`, vulture sees the usage and does not flag it.
- Therefore, every vulture finding means the name is genuinely unreferenced in our
  codebase. Adding whitelist entries hides signal that the code isn't following the
  convention we chose.

## Context

The 2026-05-03 Codex Spark triage found 762 category-spec vulture findings after
Ruff normalization passed. These include:

- Public type aliases in `category_specs/types.py` with no cross-file importers.
- Abstract methods on Sage category `ParentMethods`/`ElementMethods` classes with
  no call sites in our code.
- Package re-export variables in `category_specs/__init__.py` that nothing imports.
- Private-looking helpers that lack underscore prefixes.

The abstract methods are a special case. Sage dispatches them dynamically through
category machinery that vulture cannot trace. But if e.g. `Sets().cardinality()`
is an abstract method we specify, and no smoke test calls `cardinality()` on a set
object, vulture correctly reports it as unused. The fix is to call it in a smoke,
which also validates that the category graph routes correctly.

## Resolution Strategy

For each of the 762 findings, classify into exactly one bucket:

### Bucket 1: Underscore-prefix (internal)

For items that are genuinely internal helpers, prefix with `_`. Vulture ignores
`_`-prefixed names. This is the style guide's mechanism and vulture's escape hatch.

**Subtlety:** an underscored item with zero callers even within its own defining
file is still suspect. If an internal helper exists only to exist, it is dead code
and belongs in Bucket 3. Do not mechanically `_`-prefix everything -- verify each
item is actually used.

### Bucket 2: Smoke/test call (public surface)

For items that are genuinely part of our public API, add a smoke or test call that
exercises the surface. Examples:

- `types.py` exports `ModuleElement` but nothing imports it -> add a smoke that
  imports and uses it.
- `Sets().ParentMethods.cardinality` is specified but never called -> add a smoke
  that constructs a set object and calls `.cardinality()` on it.
- `__init__.py` re-exports `Rings` but no downstream module imports from the
  package -> either find the intended consumer and add the import, or determine
  that the re-export itself is dead (Bucket 3).

The call validates category wiring and gives vulture the cross-file usage chain it
needs. It is not onerous checkboxing -- it proves the category graph routes
correctly.

### Bucket 3: Delete (dead code)

Items that are not used, not intended to be public, and not justifiable as internal
helpers. Delete them.

## What has already been done

- The global QC `_python-qc-files` and `_sage-qc-files` recipes now exclude
  `**/*.bak/**` directories. Vulture no longer scans `src.bak/` or `tests.bak/`.
- The spec backup files that produced 3 of the original findings were moved to
  `src.bak/spec-backups/`. Those findings are resolved.
- The 762 remaining findings are all in `category_specs/**`.

## Boundaries

- Do not add entries to `/home/dzack/ai/quality-control/vulture_whitelist.py`.
- Do not add local vulture bypasses, ignore files, or QC overrides.
- Do not delete category-spec API surfaces that are intended to be public.
- Do not mechanically `_`-prefix without verifying the item is actually used.
- Do not add smoke calls that are tautological (`assert Foo is not None`).

## Validation

- After cleanup, run `just test` and verify vulture passes with zero findings.
- If any finding remains, it must be justified in this card body -- either a
  legitimate Sage dynamic dispatch edge case (rare after smoke calls) or an item
  that needs splitting into a follow-up card.

## Work Log

- 2026-05-03: Created from read-only vulture triage (original whitelist framing).
- 2026-05-06: Reframed as code-fix task after user identified that underscore
  convention + smoke calls resolve findings without whitelist entries.
