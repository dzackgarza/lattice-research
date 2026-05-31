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

The provider-satisfaction/object-method-resolution repair has passed targeted
state-machine review. Do not continue source reconstruction for that contract unless a
new live Sage/refinement witness contradicts `mem:provider-satisfaction-goal-contract`
and `mem:provider-satisfaction-goal-state`.

The next category-spec pickup should return to the earliest incomplete approved DAG
leaf. If the chosen leaf is structural typing verification, the known residue is that
`just category-specs-mypy-structural-report` fails before mypy with a conflicting
provider projection for
`category_specs.modules.homsets._RModHomCategoryObjectMethods`.

Do not commit structural-report output from the object-method verification attempt.
The report generation was run in a noisy worktree and its generated files were cleaned
back to the committed baseline. Rerun that report only inside the structural-typing leaf
that owns the provider-projection conflict.

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
