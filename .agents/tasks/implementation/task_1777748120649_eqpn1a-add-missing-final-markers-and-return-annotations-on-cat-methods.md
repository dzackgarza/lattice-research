---
trackerStatus:
  type: task
title: Add missing final markers and return annotations on Cat methods
status: in-review
priority: critical
planId: SPR-CAT-SURFACE-01KQN9
complexity: 50
progress: 90
updated: '2026-05-03'
tags:
- category-specs
- implementation
- task
- cat
- theme-audit-uniformity
---
# Add missing final markers and return annotations on Cat methods

## Summary

Add missing `@final` markers and explicit return annotations on concrete `Cat` method
surfaces, and remove public Sage option-bag exposure from the affected Cat API surface.

## Source Provenance

- Pasted backlog, 2026-05-02.
- Owning plan: `SPR-CAT-SURFACE-01KQN9`.
- Relevant guidance: `category_specs/AGENTS.md`, `category-spec-style`, and
  `category-spec-subtrees` Cat ownership rules.

## Context

`Cat()` owns the category-object surface and the root wrappers for category classes.
The task is an API-hardening pass, not a redesign: add finality and return typing where
the existing concrete Cat methods already have a stable mathematical owner, and remove
Sage option-bag vocabulary from the public surface when it is only interop detail.

## Complexity And Ownership

- Owner role: Codex Spark implementation worker, with parent-agent review.
- Complexity: 50, moderate band.
- Rationale: the work combines finality markers, return annotations, and option-bag
  cleanup across Cat method surfaces. It is broader than a single signature edit but
  remains bounded to the Cat surface and does not require a new mathematical ownership
  decision unless preflight finds a method whose owner is unclear.

## Acceptance Criteria

- [ ] Concrete Cat methods touched by the task have appropriate `@final` markers when
  subclass override is not part of the public contract.
- [ ] Touched methods have explicit return annotations using project/Sage mathematical
  types rather than `Any` where a real type is available.
- [ ] Public Cat method signatures do not expose Sage option bags as project API.
- [ ] No new helper registry, post-hoc splicing, class mutation, or compatibility shim
  is introduced.
- [ ] Any unclear method owner is surfaced as a tracker decision or follow-up card
  instead of being guessed inside implementation.

## Dependencies And Boundaries

- Work under `category_specs/cat/` first; only touch other subtrees for direct call-site
  updates or validation fallout.
- `cat/base_category_types.py` remains the Sage category-base touch point.
- Do not change mathematical category ownership or constructor routing as part of this
  card.
- Do not mark this card done or accepted; implementation handoff must return changed
  files and validation evidence for review.

## Validation Requirements

- Run the narrowest relevant `just` recipe available for category-spec or Cat smoke
  validation. If no narrower recipe exists, report that and run `just test` only if the
  dependency environment is available.
- Run a targeted static search/check showing no newly exposed public Cat method option
  bags in touched files.
- Report any validation blocker without substituting a different test.

## Work Log

- Created from pasted backlog on 2026-05-02.
- 2026-05-03: Normalized for execution after plan approval; set complexity to 50 and
  moved status to in-progress for delegated implementation.
- 2026-05-03: Delegated implementation to Codex Spark worker `Euler` (`019dee37-df2c-7523-9c54-380605dafc1e`).
- 2026-05-03: Spark worker returned Cat-surface implementation changes under
  `category_specs/cat/**`. Parent review confirmed the diff is scoped to final markers,
  return annotations, and formatting/import ordering.
- 2026-05-03: Fixed the global QC `justfile` heredoc parse blocker in
  `/home/dzack/ai/quality-control/justfile`, then reran `just test` from this repo.
  Validation now reaches Ruff normalization but fails with 534 remaining pre-existing
  Ruff findings across `category_specs`; Ruff auto-fixed 26 files, and those auto-fixes
  are carried forward per repo policy.
- 2026-05-03: Static Cat option-bag search found only existing private/internal
  forwarding hooks in `category_specs/cat/base_category_types.py`; no new public Cat
  option-bag signatures were introduced.
- 2026-05-03: Parent ran `python -m compileall category_specs/cat`; Cat files
  compile successfully. Full `just test` validation remains blocked by
  `.agents/tasks/implementation/bug-category-specs-ruff-normalization-blocker.md`.
- 2026-05-05: Filled the remaining concrete Cat wrapper typing/finality holes in
  `category_specs/cat/base_category_types.py`: `_CatObjectMixin._make_named_class`
  now has explicit parameter and return annotations and is final, and both singleton
  `__classcall__` bridges have explicit `cls` and return annotations.
- 2026-05-05: Moved this card to `in-review`; human review is still required before
  closure.
