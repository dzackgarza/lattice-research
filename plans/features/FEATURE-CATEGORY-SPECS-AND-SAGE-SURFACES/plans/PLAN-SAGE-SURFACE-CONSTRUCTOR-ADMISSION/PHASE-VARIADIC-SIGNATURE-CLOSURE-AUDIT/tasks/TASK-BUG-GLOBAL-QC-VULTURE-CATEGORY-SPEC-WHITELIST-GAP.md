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
- 2026-05-06 sixth bounded slice: Cat smoke coverage was extended for alias routing
  (`Slice`, `Coslice`, `Endsets`), the Cat subobject construction class,
  `CatEndCategory.Autset`, endofunctor/autofunctor predicates, and axiom defining
  predicates.
- Validation for the sixth slice:
  `just --justfile category_specs/justfile smoke-file cat/smoketest.sage` passed, and
  the vulture-only diagnostic no longer reports the targeted Cat alias,
  subobject-class, end/aut predicate, or base-category defining-predicate findings.
  Remaining Cat diagnostics are concentrated in abstract construction-functor methods
  and slice/coslice structure-category stubs.
- 2026-05-06 seventh bounded slice: a dedicated `category_specs/types_smoketest.sage`
  was added to exercise centralized `types.py` alias packages against their intended
  category/object/element/morphism anchors, and the category-spec smoke recipe now runs
  that smoke file first.
- Validation for the seventh slice:
  `just --justfile category_specs/justfile smoke-file types_smoketest.sage` passed, and
  the vulture-only diagnostic no longer reports `category_specs/types.py` findings or
  generated findings from the new type smoke.
- 2026-05-06 eighth bounded slice: finite-poset smoke coverage was added for
  `Posets().Finite()` class routing and the finite diamond poset's top/bottom,
  extremal elements, cover relation iterator, intervals, height/width certificates,
  semilattice certificates, chains, antichains, and linear extensions.
- Validation for the eighth slice:
  `just --justfile category_specs/justfile smoke-file posets/smoketest.sage` passed,
  and the vulture-only diagnostic no longer reports
  `category_specs/posets/subcategories/finite.py` findings.
- 2026-05-06 ninth bounded slice: finite-lattice smoke coverage was added for the
  project-refined diamond lattice's complements, atomic/coatomic/complemented/
  distributive certificates, modular and semidistributive surfaces, sublattice
  construction, congruence generation, and congruence lattice construction.
- Validation for the ninth slice:
  `just --justfile category_specs/justfile smoke-file posets/smoketest.sage` passed,
  and the vulture-only diagnostic no longer reports
  `category_specs/posets/subcategories/finite_lattice.py` findings.
- 2026-05-06 tenth bounded slice: forms-chain smoke coverage was added for concrete
  formed/bilinear/symmetric/integral predicate forwarding plus abstract method ownership
  on the finite-rank formed-module axiom chain.
- Validation for the tenth slice:
  `just --justfile category_specs/justfile smoke-file forms/smoketest.sage` passed, and
  the vulture-only diagnostic no longer reports `category_specs/forms/chain.py`
  findings.
- 2026-05-06 eleventh bounded slice: modules-with-basis smoke coverage was added for
  with-basis and with-ordered-basis category ownership, combinatorial-free-module
  term/coefficient/monomial surfaces, basis-index and basis-order forwarding helpers,
  and explicit abstract ownership of reduction, basis-map morphism construction,
  echelonized-basis-matrix, coordinate-vector, and coordinate-module surfaces.
- Validation for the eleventh slice:
  `just --justfile category_specs/justfile smoke-file modules/smoketest.sage` still
  fails on the existing module implementation-gap frontier, but the new with-basis
  assertions are not among the reported failures. The vulture-only diagnostic no longer
  reports `category_specs/modules/subcategories/with_basis.py` findings.
- 2026-05-06 twelfth bounded slice: topological-space smoke coverage was added for
  root topological axiom ownership, topological/metric/connected/compact/complete
  predicate surfaces, topological and metric Hom/Aut element predicates, direct
  Sage-supercategory splice policy, and objects-over/objects-under structure-space
  surfaces.
- Validation for the twelfth slice:
  `just --justfile category_specs/justfile smoke-file topological_spaces/smoketest.sage`
  passed, and the vulture-only diagnostic no longer reports
  `category_specs/topological_spaces/**` findings.
- 2026-05-06 thirteenth bounded slice: generic Hom/End smoke coverage was added for
  the owned `is_endomorphism_set` semantics: Hom objects compute the predicate from
  domain/codomain equality, while End objects report true by construction.
- Validation for the thirteenth slice:
  `just --justfile category_specs/justfile smoke-file homsets/smoketest.sage` passed,
  and the vulture-only diagnostic no longer reports
  `category_specs/homsets/homsets.py` or `category_specs/homsets/endsets.py`
  predicate findings.
- 2026-05-06 fourteenth bounded slice: Cat smoke coverage was extended for the
  category-internal functor surface and Sage construction-functor combinator surface:
  `_coerce_into_domain`, `_apply_functor`, `_apply_functor_to_morphism`,
  `coercion_reversed`, `pushout`, `merge`, `commutes`, `expand`, and `common_base`.
- Validation for the fourteenth slice:
  `just --justfile category_specs/justfile smoke-file cat/smoketest.sage` passed, and
  the vulture-only diagnostic no longer reports `category_specs/cat/homsets.py`
  findings.
- 2026-05-06 fifteenth bounded slice: modules smoke coverage was extended for the
  base `Modules(R)` object surface's default negative predicates for specialized
  subcategories: lattice, representation-module, free-graded, finitely-presented
  graded, Ore, torsion-quadratic, and ring-object-as-module.
- Validation for the fifteenth slice:
  `just --justfile category_specs/justfile smoke-file modules/smoketest.sage` still
  fails on the existing module implementation-gap frontier, but the new base-predicate
  assertion is not among the reported failures. The vulture-only diagnostic no longer
  reports the targeted `category_specs/modules/__init__.py` predicate findings.
- 2026-05-06 sixteenth bounded slice: poset smoke coverage was extended for root
  reverse comparisons, lower covers, order ideals, order filters, poset Hom/End/Aut
  predicates, objects-over/objects-under structure-poset surfaces, finite meet/join
  semilattice extremal elements, operation matrices, pseudocomplements, and generated
  meet/join subsemilattices.
- Validation for the sixteenth slice:
  `just --justfile category_specs/justfile smoke-file posets/smoketest.sage` passed,
  and the vulture-only diagnostic no longer reports `category_specs/posets/**`
  findings.
- 2026-05-06 seventeenth bounded slice: partitioned-set smoke coverage was added for
  fixed-base partition blocks as subsets of the powerset, refinement/strict-refinement
  order, ordered finite partition statistics, noncrossing/nonnesting predicates, and
  finite-totally-ordered-base ownership. The slice also fixed `blocks()` so a refined
  Sage set partition is converted through its blocks rather than passed directly to
  `SageSet`.
- Validation for the seventeenth slice:
  `just --justfile category_specs/justfile smoke-file sets/smoketest.sage` passed, and
  the vulture-only diagnostic no longer reports
  `category_specs/sets/subcategories/partitioned.py` findings.
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
- 2026-05-06: Completed the sixth bounded cleanup slice for Cat smoke coverage of
  alias routing, end/aut predicates, subobject routing, and defining predicates.
- 2026-05-06: Completed the seventh bounded cleanup slice for centralized type alias
  smoke coverage.
- 2026-05-06: Completed the eighth bounded cleanup slice for finite-poset smoke
  coverage.
- 2026-05-06: Completed the ninth bounded cleanup slice for finite-lattice smoke
  coverage.
- 2026-05-06: Completed the tenth bounded cleanup slice for forms-chain smoke coverage.
- 2026-05-06: Completed the eleventh bounded cleanup slice for modules-with-basis
  smoke coverage.
- 2026-05-06: Completed the twelfth bounded cleanup slice for topological-space smoke
  coverage.
- 2026-05-06: Completed the thirteenth bounded cleanup slice for generic Hom/End
  endomorphism-set predicate smoke coverage.
- 2026-05-06: Completed the fourteenth bounded cleanup slice for Cat functor and
  construction-functor smoke coverage.
- 2026-05-06: Completed the fifteenth bounded cleanup slice for base module predicate
  smoke coverage.
- 2026-05-06: Completed the sixteenth bounded cleanup slice for poset root, Hom, slice,
  and finite semilattice smoke coverage.
- 2026-05-06: Completed the seventeenth bounded cleanup slice for partitioned-set
  smoke coverage and the partition blocks conversion bug.
