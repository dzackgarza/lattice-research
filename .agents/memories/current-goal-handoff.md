---
title: Current Goal Handoff
---
# Handoff

## Anchor

Read `mem:repo-purpose-mathematical-research-machine` before any card or plan.

## Current phase

Category-spec vocabulary: building the semantic substrate so downstream lattice/Coble
work has named objects, morphisms, and invariants, not raw matrices.

## Current next action

The provider-satisfaction/object-method-resolution branch must be reconciled with the
corrected category-spec model in `mem:category-spec-repo-model-corrections`.
Prior ABC-boundary commits and tests that require refinement-time rejection, failed
refinement atomicity, or "invalid refined objects cannot enter project categories" are
not acceptance criteria.

Next pickup: continue from committed bridge repair `6c7e6648`, not from old summaries.
That commit removes a local subclass-filter from `_abc_parent_class_bases`, so the
project bridge uses Sage's `_super_categories_for_classes` base sequence instead of
recomputing a smaller MRO base set. That clears the finite ring/finite-field
parent-class MRO layer while preserving the corrected model: refinement declares
category view, and Python/Sage MRO handles concrete parent methods without method-name
satisfaction logic.

Current hard core: the parent-class MRO layer is no longer the first failure, but the
goal is not complete. `rings/tests/regression/finite_fields.sage` now reaches
`F7(3).inverse()` and fails because project `ElementMethods.inverse` is still installed
as an ellipsis body that shadows Sage's concrete element inverse path. A trial
generalization of the ABC bridge to `element_class` made that inverse witness pass but
broke `sets/smoketest.sage`: Sage later builds concrete element classes with upstream
`dynamic_class`, which cannot compose with an ABCMeta category `element_class`. Do not
resume that blanket element-class route.

`rings/tests/regression/integer_mod_rings.sage` is committed as red witness `0d042624`
and reaches later constructor behavior before failing in the Hom/coercion path:
`JoinCategory_with_category` lacks `HomCategory`. This is a separate category/Hom
join-surface gap, not evidence for reintroducing abstract-name filtering or refinement
validation.

Current verification frontier:

- `rings/tests/regression/object_method_resolution.sage` passes.
- `sets/tests/regression/set_partitions.sage` passes.
- `sets/smoketest.sage` passes, with existing Sage warning noise about topological-set
  axiom binding and set-hom element-provider superclass shape.
- `posets/smoketest.sage` passes.
- `python3 -m py_compile category_specs/cat/base_category_types.py` passes.
- `just --justfile category_specs/justfile check-banned-spec-patterns` reports 442
  inherited repo-wide findings and zero staged findings.
- `rings/tests/regression/finite_fields.sage` fails at `F7(3).inverse() == F7(5)`.
- `rings/tests/regression/integer_mod_rings.sage` fails later at
  `R7.multiplicative_generator()` through the Hom/coercion path.
- Full `just --justfile category_specs/justfile test` is not clean. The latest broad
  run still failed in `types_smoketest.sage`, `tensor_algebra_components`,
  `algebras`, `rings`, `modules`, and `lattices`; rerun only after deciding whether
  the remaining element/Hom failures are in the current bridge boundary or separate
  source-grounded implementation cards.

Do not widen this into a Sage hook, method-only parallel hierarchy, or refinement
validator. The next code change should preserve the intended model: extend Sage's
dynamic classes with ABC-compatible metaclasses and use those dynamic classes in this
category hierarchy; refinement declares category view; ordinary lookup may reach
concrete Sage/project methods; missing project obligations remain visible to smokes and
later implementation work.

Do not claim the larger provider-satisfaction goal complete. Root
`Rings().Constructors().ZZ()`/`QQ()` obligations remain visible implementation gaps
unless separate source-grounded work supplies those methods.

Before further category-spec edits, run
`just --justfile category_specs/justfile check-banned-spec-patterns`. It is warning-only
while inherited repo-wide findings remain, but new `typing.cast`, `with_axiom(self, ...)`,
cache-priming, or post-hoc object mutation would be a fresh defect.

## Required context

Before the next source edit, load:

- `mem:category-spec-epistemic-foundation`
- `mem:category-spec-repo-model-corrections`
- `mem:category-spec-refinement-category-declaration`
- `mem:category-spec-methods-are-abstract`
- `mem:provider-satisfaction-goal-contract`
- `mem:provider-satisfaction-goal-state`
- `mem:category-spec-rotten-core-indicators`
- `mem:mathematical-sanity-check`
- `mem:sage-axiom-binding-is-descriptor-binding`
- `category_specs/AGENTS.md`
- `category-spec-style`
- `research-state-machine`

## Constraints

- No sage-stubs writing.
- No downstream Coble work.
- No `# type: ignore`.
- No `typing.cast` additions in category-spec code.
- No refinement-time abstract-method satisfaction checks.
- No generated failure bodies for missing spec obligations.
- No `with_axiom(self, "...")`; use Sage's direct `self._with_axiom("...")`
  idiom where the descriptor binding is correct.
- `NotImplementedError` remains rejected by pre-commit hook.
