---
title: Current Goal Handoff
---
# Handoff

## Anchor

Read `mem:repo-purpose-mathematical-research-machine` before any card or plan.

## Current phase

Category-spec vocabulary: building the semantic substrate so downstream lattice/Coble
work has named objects, morphisms, and invariants, not raw matrices.

## Keystone preflight for this next action

Before the current next action, load:
- `mem:category-spec-epistemic-foundation`
- `category_specs/AGENTS.md`
- `category-spec-style`
- `research-state-machine`
- `research-state-machine/references/review-kernel.md`

The object is method-ownership classification, not diagnostic-row cleanup.

## Next action

1. **Verify fixes via mypy structural report.** Run:
   `just category-specs-mypy-structural-report` The 31+ private-stub type-alias fixes
   and 11 RealSet collision fixes are uncommitted in the working tree.
   Run the report through Sage to confirm the errors are resolved.

2. **Clean up unused private-stub imports.** Several files still import private stubs
   that are no longer used at module level after the alias fixes:
   - `sets/__init__.py`: `_SetMorphisms`, `_SetEndomorphisms`, `_SetAutomorphisms`,
     `_SetHomCategoryObjectMethods` (only used in class bodies now)
   - `rings/__init__.py`: `_RingHomomorphisms`, `_RingEndomorphisms`,
     `_RingAutomorphisms`, `_RingHomCategoryObjectMethods`
   - `modules/__init__.py`: `_RModMorphisms` Remove these imports.
     Do NOT remove private names used inside class bodies (e.g.,
     `ParentMethods = _RingObjectMethods` inside `class Rings`).

3. **Address `complement` collision.** `_Subobjects.ParentMethods.complement` is still
   `@final`, and `_RealSets.ParentMethods.complement` is now `@abstractmethod` without
   `@override`. Sage's dynamic mixing may handle this differently from standard Python
   MRO — verify with the mypy report.

4. **Smoke tests.** If mypy report is clean, run relevant smoke tests to ensure the
   type-alias changes don't break runtime behavior.

## Migration completed: skills → memories

26 former local skills migrated to `mem:skills/` under `.agents/memories/skills/`. 9
skills remain for always-in-context dynamic triggering.
AGENTS.md and onboarding updated.

## What was done

- **Private-stub type aliases fixed** (~31 occurrences across 10 files): All
  module-level type aliases now use public names (e.g.,
  `RingsObject = Rings.ParentMethods` instead of `_RingObjectMethods`). Fixed in: rings,
  sets, modules, algebras, lattices, topological_spaces, and subcategory files (ideals,
  approximate, partitioned, tensor_algebra_components).

- **RealSet set-operation collisions fixed** (11 changes):
  - Removed `@final` from `union`, `intersection`, `difference`, `symmetric_difference`
    in `_Subobjects.ParentMethods` (subobjects.py)
  - Removed `@final` from `union` and `is_subset` in `_SetObjectMethods`
    (sets/**init**.py)
  - Removed invalid `@override` from `union`, `intersection`, `difference`,
    `symmetric_difference`, `complement` in `_RealSets.ParentMethods` (real_set.py)

## Constraints

- No sage-stubs writing.
- No downstream Coble work.
- No `# type: ignore`.
- `NotImplementedError` rejected by pre-commit hook.

## Non-goals

- Ledger classification, card creation, handoff expansion, memory writing before source
  reading.
