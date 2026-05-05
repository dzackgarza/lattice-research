---
trackerStatus:
  type: feature
title: Fix Sets root containment refined-constructor __richcmp__ Primes iteration RealSet element-constructor and topological axiom warning
status: in-progress
priority: high
planId: SPR-SETS-TOPO-01KQN9
progress: 35
tags:
- category-specs
- implementation
- feature
- constructors
- richcmp
- sets
- realset
- topology
- primes
- theme-constructor-routing
---

# Fix Sets root containment refined-constructor __richcmp__ Primes iteration RealSet element-constructor and topological axiom warning
## Summary

The deleted Sets triage recorded the mapped enumeration smoke surface and current
failures for containment, rich comparison, Primes iteration, RealSet element
construction, and topological axiom resolution.

## Source Provenance

- `plans/category_specs/sets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/sets/docs/TRIAGE.md`.
- Original migrated line: `Fix Sets root containment refined-constructor __richcmp__ Primes iteration RealSet element-constructor and topological axiom warning from category_specs/sets/docs/TRIAGE.md`

## Context

- sets/smoketest.sage uses indexed access, rank, iteration, cardinality, and Python conversion protocols rather than Sage first/next/unrank/list/tuple helpers.
- ZZ in Sets() currently fails at the root containment statement.
- Most refined set constructors expose missing __richcmp__; Primes() exposes missing __iter__.
- RealSet interval input exposes missing _element_constructor_.
- SetPartitions(s) maps to Sets().Partitioned(), while SetPartitions() remains countable-only because it lacks a fixed powerset ambient.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file sets/smoketest.sage after set constructor or comparison changes.
- [ ] Preserve the mapped enumeration vocabulary and do not reintroduce Sage fallback helper names.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Fixed the root `Sets()` containment path so existing Sage set parents
  such as `ZZ` are recognized through their Sage set category. Implemented the
  project root set comparison surface with set-theoretic subset/proper-subset
  semantics, plus concrete root defaults for SymPy export, construction metadata,
  cartesian products, unions, subsets, and subset lattices. Added infinite-set
  cardinality/is-empty defaults so infinite set refinements no longer shadow Sage with
  abstract placeholders.
- Verification:
  - `python -m py_compile category_specs/sets/__init__.py category_specs/sets/subcategories/infinite.py` passed.
  - `command ruff check category_specs/sets/__init__.py category_specs/sets/subcategories/infinite.py` passed after removing an unused import and fixing import spacing.
  - `just smoke-file sets/smoketest.sage` no longer reports `ZZ in Sets()` or blanket
    `__richcmp__` failures. The current frontier is `facade_for` on facade-backed set
    constructors, `cardinality` on several countable/subobject constructors, Primes
    `__iter__`, the intentionally removed `Constructors().RealSet` legacy route,
    RealSet `_element_constructor_`, and partition `_sympy_`.
  - `just smoke-file rings/smoketest.sage` also advanced past the previous root
    `__richcmp__` failures; the current rings frontier is now ring-specific
    implementation gaps such as `hilbert_polynomial`, topological `boundary`,
    `ideal_monoid`, `_change_print_mode`, q-adic deferred constructors, and matrix
    algebra/module MRO refinement.
