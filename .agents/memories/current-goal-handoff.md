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

The provider-satisfaction/object-method-resolution repair has targeted ABC-boundary
commits through `29ecc149`. The patch computes `__abstractmethods__` on Sage dynamic
`parent_class` construction, propagates joined abstract sets, removes the generated
`assert False` missing-method body, and makes `refine_category` reject missing
obligations before mutating the parent category.

Treat `2e457c43` and `29ecc149` as the adversarial-test guards for this contract. They
expand `rings/tests/regression/object_method_resolution.sage` so future repairs must
satisfy standalone and joined parent-class abstractness, multiple missing obligations,
concrete Sage parent-type realization, mixed realized/missing rejection, concrete project
category overrides, dynamically generated obligation names, and optimized-mode
failed-refinement atomicity.

The targeted regression now passes:

```bash
just -f category_specs/justfile smoke-file rings/tests/regression/object_method_resolution.sage
```

Do not claim the larger provider-satisfaction goal complete yet. Strict ABC enforcement
exposes a separate root ring-surface debt: `Rings().Constructors().ZZ()` now correctly
raises on unresolved abstract obligations such as
`hilbert_polynomial`, `is_number_field`, `is_complete_ring`, and related root predicate
methods. `category_specs/__init__.py` no longer eagerly refines `ZZ`/`QQ` at import
time, because import-time construction of abstract parents hid the invalid surface.

Next pickup: review the ABC-boundary commits, then source-ground the root
`Rings().Constructors().ZZ()`/`QQ()` abstract obligations or split that as the next
explicit ring-surface repair. Do not reintroduce generated assertion-body enforcement or
skip the refinement guard to make those constructors pass.

Before further category-spec edits, run
`just --justfile category_specs/justfile check-banned-spec-patterns`. It is warning-only
while inherited debt remains, but new `typing.cast`, `with_axiom(self, ...)`,
cache-priming, or post-hoc object mutation would be a fresh defect.

## Required context

Before the next source edit, load:

- `mem:category-spec-epistemic-foundation`
- `mem:category-spec-refinement-category-declaration`
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
- No `with_axiom(self, "...")`; use Sage's direct `self._with_axiom("...")`
  idiom where the descriptor binding is correct.
- `NotImplementedError` remains rejected by pre-commit hook.
