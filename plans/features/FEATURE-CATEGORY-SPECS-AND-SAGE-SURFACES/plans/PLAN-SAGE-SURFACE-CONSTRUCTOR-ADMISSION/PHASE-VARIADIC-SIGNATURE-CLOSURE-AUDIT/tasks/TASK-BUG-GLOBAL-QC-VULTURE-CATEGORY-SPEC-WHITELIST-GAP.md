---
id: TASK-BUG-GLOBAL-QC-VULTURE-CATEGORY-SPEC-WHITELIST-GAP
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Resolve category-spec vulture findings through code fixes, not whitelist entries
status: in-progress
priority: high
description: 'Resolve the 762 category-spec vulture findings by fixing the code, not by
  expanding the global vulture whitelist. The whitelist approach was the wrong framing.'
successCriteria:
- "Classify each vulture finding into one of three buckets: underscore-prefix for internal helpers, smoke/test call for genuinely public surfaces, or delete for actual dead code."
- "For underscored items: verify the item is used at least once in its own file. An underscored item with zero local callers is suspect."
- "For public surfaces: add a smoke or test call that exercises the surface. The call proves category wiring correctness and gives vulture a cross-file usage to see."
- "Delete genuinely dead code that is neither an intentional internal helper nor a public vocabulary item."
- "Do not add local vulture bypasses, ignore files, or QC overrides."
- "After exhausting all code fixes, identify any remaining findings that genuinely cannot be resolved through code (e.g., Sage dynamic dispatch that cannot be expressed as a static call). Present these to the user for review before adding any whitelist entry."
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

- Do not add entries to `/home/dzack/ai/quality-control/vulture_whitelist.py` without
  prior user review and approval.
- Do not add local vulture bypasses, ignore files, or QC overrides.
- Do not delete category-spec API surfaces that are intended to be public.
- Do not mechanically `_`-prefix without verifying the item is actually used.
- Do not add smoke calls that are tautological (`assert Foo is not None`).

## Final whitelist gate (user review)

After all three buckets are exhausted, some genuine edge cases may remain: Sage
dynamic dispatch patterns where the method cannot be expressed as a static call in
our code. Present these to the user with:

- The exact name and defining file
- Why it cannot be resolved through underscore prefix (it is genuinely public)
- Why it cannot be resolved through a smoke call (no statically-callable surface exists)
- The proposed whitelist entry

Do not add whitelist entries silently. Agents were previously too eager to whitelist
violations to silence QC rather than addressing the issues they unearthed.

## Validation

- After cleanup, run `just test` and verify vulture passes.
- All remaining findings must either be resolved through code fixes or presented to
  the user in the final whitelist gate.

## Progress

- 2026-05-06 first bounded slice: root package re-export findings in
  `category_specs/__init__.py` were resolved by adding real Cat smoke assertions that
  use the root package module exports for `algebras`, `cat`, `forms`, `homsets`,
  `lattices`, `modules`, `posets`, `rings`, `sets`, and `topological_spaces`.
- The same Cat smoke slice now exercises the opt-in category diagnostic utility
  surface in `category_specs/utils.py`: disabled-by-default behavior, enable/disable,
  logger access, history clearing, and once-per-key emission.
- `category_specs/cat/smoketest.sage` passes after these assertions.
- A vulture-only diagnostic through the global QC recipe confirms these names no longer
  appear in the vulture finding list. This diagnostic is inventory evidence only; final
  validation remains `just test`.
- 2026-05-06 second bounded slice: generated Sage-file findings under
  `category_specs/**` were resolved by using the exterior algebra generator `yE` in the
  module smoke, deleting a genuinely dead reversed diamond-cover predicate from the
  poset smoke, removing a stale unused number-field import, and making the finite
  iterator witness assert its empty finite-set behavior. The same pass corrected the
  iterator regression file to use the project constructor's nullary iterator-factory
  contract.
- Validation for the second slice:
  `just --justfile category_specs/justfile smoke-file posets/smoketest.sage` passed;
  `just --justfile category_specs/justfile smoke-file sets/tests/regression/enumerated_set_from_iterator.sage`
  passed; vulture-only diagnostic no longer reports generated Sage findings under
  `category_specs/**`.
- `just --justfile category_specs/justfile smoke-file modules/smoketest.sage` still
  fails on existing module category implementation gaps; the edited exterior-algebra
  assertions now fail only at the pre-existing Sage/category base-class mismatch rather
  than the temporary nonhomogeneous relation error. `rings/tests/regression/number_fields.sage`
  reaches the existing `hilbert_polynomial` implementation gap after the stale import
  path was corrected.
- 2026-05-06 third bounded slice: 100%-confidence unused-parameter findings were
  cleared in abstract/spec method stubs without changing public parameter names. The
  affected files were `category_specs/algebras/__init__.py`,
  `category_specs/algebras/subcategories/with_basis.py`,
  `category_specs/cat/homsets.py`,
  `category_specs/lattices/subcategories/over_integers.py`,
  `category_specs/modules/subcategories/finitely_presented_graded_modules.py`,
  `category_specs/modules/subcategories/finitely_presented_over_pid.py`,
  `category_specs/modules/subcategories/integer_lattices.py`, and
  `category_specs/modules/subcategories/with_basis.py`.
- Validation for the third slice: the vulture-only diagnostic no longer reports the
  targeted unused formal parameters from those files. Remaining 100%-confidence
  category-spec findings are in other surfaces such as forms, rings, sets, and tensor
  components.
- 2026-05-06 fourth bounded slice: the remaining 100%-confidence formal-parameter
  findings under `category_specs/**` were cleared while preserving the public
  signatures. This covered the remaining forms, module, ring, set, and tensor-component
  abstract or overload stubs.
- Validation for the fourth slice: the vulture-only diagnostic no longer reports any
  100%-confidence findings under `category_specs/**`. The remaining category-spec
  diagnostics are 60%-confidence public surfaces that need smoke coverage, deletion,
  or source-grounded internalization.
- 2026-05-06 fifth bounded slice: generated Sage test locals outside
  `category_specs/**` were resolved by turning the locals into substantive assertions
  or by correcting an unused bivariate polynomial-ring declaration to the univariate
  ring actually used by the hyperelliptic-curve witness.
- Validation for the fifth slice: the vulture-only diagnostic no longer reports
  generated Sage findings under `tests/sage_spec/**` or `tests/variety_spec/**`.
  Remaining vulture output is now concentrated in `category_specs/**`
  60%-confidence public surfaces.
- Current public `just test` still fails before vulture at the global mypy stage with
  the existing Sage/stub/type surface. That is not a blocker for this leaf's continued
  vulture cleanup, but it means final acceptance cannot yet claim full QC success.
- Spec-weakening review: this slice added smoke coverage and did not delete abstract
  methods, narrow smokes, remove constructor obligations, or move any spec surface.
  The third slice preserved public signatures and only made existing stub bodies refer
  to their documented parameters so vulture can distinguish intentional API from dead
  locals.

## Work Log

- 2026-05-03: Created from read-only vulture triage (original whitelist framing).
- 2026-05-06: Reframed as code-fix task after user identified that underscore
  convention + smoke calls resolve findings without whitelist entries.
- 2026-05-06: Moved to `in-progress` and completed the first bounded cleanup slice:
  root package re-export usage plus category diagnostic utility usage in the Cat smoke.
- 2026-05-06: Completed the second bounded cleanup slice for generated category-spec
  Sage findings and recorded the remaining validation frontier.
- 2026-05-06: Completed the third bounded cleanup slice for selected 100%-confidence
  unused formal parameters in abstract/spec method stubs.
- 2026-05-06: Completed the fourth bounded cleanup slice for all remaining
  100%-confidence category-spec formal-parameter findings.
- 2026-05-06: Completed the fifth bounded cleanup slice for generated Sage test locals
  outside `category_specs/**`.
