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

The provider-satisfaction/object-method-resolution repair is not complete.
Commit `ecac9da8` is the current red-test proof: missing `ParentMethods` obligations
still pass through `refine_category`, and optimized Python strips the generated
`assert False` method body so the missing method call returns silently.

Before source repair, explain the red proof and wait for user approval. After approval,
repair the class/refinement boundary itself: compute or propagate
`__abstractmethods__` on the actual Sage dynamic `X.category().parent_class`, and have
`refine_category` reject nonempty category-parent abstract sets. Existing Sage parents
such as `ZZ` remain `IntegerRing_class`, so checking `type(X).__abstractmethods__` is
insufficient.

The `ideal_monoid` shadowing symptom remains positively fixed by `75cfa0c7`, but that
is only a partial interop fix. Do not preserve the generated assertion-body missing
method as enforcement; it is the current slop surface.

Before further category-spec edits, run
`just --justfile category_specs/justfile check-banned-spec-patterns`. It is warning-only
while inherited debt remains, but new `typing.cast`, `with_axiom(self, ...)`,
cache-priming, or post-hoc object mutation would be a fresh defect.

## Required context

Before the next source edit, load:

- `mem:category-spec-epistemic-foundation`
- `mem:category-spec-refinement-purpose-and-provider-satisfaction`
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
