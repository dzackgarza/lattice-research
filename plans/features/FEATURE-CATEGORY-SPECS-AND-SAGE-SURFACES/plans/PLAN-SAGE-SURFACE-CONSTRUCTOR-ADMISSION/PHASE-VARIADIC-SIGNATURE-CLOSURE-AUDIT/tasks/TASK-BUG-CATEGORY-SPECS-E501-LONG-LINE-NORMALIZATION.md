---
id: TASK-BUG-CATEGORY-SPECS-E501-LONG-LINE-NORMALIZATION
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Normalize category_specs Ruff E501 long-line blockers
status: needs-review
priority: medium
description: Resolve the remaining Ruff `E501` line-length blockers in `category_specs`
  while preserving mathematical and public API meaning.
successCriteria:
- Reproduce the remaining `E501` findings for `category_specs`.
- Wrap long import, lazy-import, type-alias, docstring, and expression lines in the
  smallest semantics-preserving way.
- Avoid broad rewrites, comment churn, or source-prose edits unrelated to Ruff `E501`.
- Do not add local Ruff ignores, bypasses, whitelists, or quality-control exceptions.
- Keep public names and import side effects stable.
complexity: 64
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Normalize category_specs Ruff E501 long-line blockers

## Summary

Resolve the remaining Ruff `E501` line-length blockers in `category_specs` while
preserving mathematical and public API meaning.

## Source Provenance

- Split from `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- Codex Spark triage on 2026-05-03 reported 420 `E501` findings after `just test`
  reached the global QC Ruff normalization stage.
- Representative surfaces include `category_specs/algebras/__init__.py`,
  `category_specs/modules/__init__.py`, `category_specs/rings/__init__.py`,
  `category_specs/rings/subcategories/*.py`, and `category_specs/forms/chain.py`.

## Context

Line length is not a mathematical priority by itself, but it is currently a validation
gate for implementation cards because global QC runs Ruff normalization before the rest
of `just test`. Keep the cleanup mechanical and avoid changing source meaning.

## Complexity And Ownership

- Owner role: implementation cleanup worker with parent review.
- Complexity: 64, high band.
- Rationale: the work is mostly mechanical but spans many files and package surfaces.
  Risk comes from accidentally changing import, lazy-import, or type-aggregation
  semantics while wrapping long expressions.

## Acceptance Criteria

- [x] Reproduce the remaining `E501` findings for `category_specs`.
- [x] Wrap long import, lazy-import, type-alias, docstring, and expression lines in the
  smallest semantics-preserving way.
- [x] Avoid broad rewrites, comment churn, or source-prose edits unrelated to Ruff
  `E501`.
- [x] Do not add local Ruff ignores, bypasses, whitelists, or quality-control
  exceptions.
- [x] Keep public names and import side effects stable.

## Dependencies And Boundaries

- Parent blocker: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- Coordinate with the import-hygiene card if the same package `__init__.py` lines are
  also `F401` or `E402` findings.
- Do not use this card to change mathematical specifications, constructor routing, or
  category ownership.

## Validation Requirements

- Run `just test` after the cleanup attempt.
- If `just test` remains blocked, record the first remaining blocker and representative
  rule families in this card and the parent blocker.

## Work Log

- 2026-05-03: Created from Codex Spark triage of the category-specs Ruff normalization
  blocker.
- 2026-05-03: Reproduced and cleared all `E501` findings in
  `category_specs` via `uvx --from ruff ruff check --select E501 category_specs`,
  resolving the reported 424+ overlong lines to zero.
- 2026-05-03: Reformatted targeted long-line offenders in
  `category_specs/{algebras/forms/modules/rings/**}/**/*.py` and resolved residual
  long-docstring/import line issues manually with minimal wrapping in
  `category_specs/forms/__init__.py` and `category_specs/algebras/__init__.py`.
- 2026-05-03: `python -m compileall category_specs` passed without syntax/runtime compile
  errors.
- 2026-05-03: `just test` now fails at `vulture` dead-code detection stage with
  broad pre-existing unused-code findings (hundreds of hits); no remaining `E501`
  or `Ruff format/check` errors remain from this leaf.
- 2026-05-06: Rechecked current state and found the 2026-05-03 "no remaining `E501`"
  note is stale. `uvx --from ruff ruff check --select E501 category_specs
  --output-format json | jq 'length'` reports 844 current E501 findings. Cleared the
  11 current `category_specs/utils.py` findings with mechanical wrapping only;
  `uvx --from ruff ruff check --select E501 category_specs/utils.py`, `uvx --from
  ruff ruff check --select UP047 category_specs/utils.py`, and `python -m compileall
  category_specs/utils.py` now pass. Remaining E501 work stays on this ready leaf; it
  is not a dependency blocker for unrelated DAG-ready cards.
- 2026-05-06: Cleared the `category_specs/modules/__init__.py` slice with
  `uvx --from ruff ruff format category_specs/modules/__init__.py` plus two manual
  wraps that the formatter left over. `uvx --from ruff ruff check --select E501
  category_specs/modules/__init__.py` and `python -m compileall
  category_specs/modules/__init__.py` now pass. Repo-wide E501 count is now 755 by
  `uvx --from ruff ruff check --select E501 category_specs --output-format json |
  jq 'length'`.
- 2026-05-06: Cleared the `category_specs/rings/__init__.py` slice with
  `uvx --from ruff ruff format category_specs/rings/__init__.py` plus two short
  q-adic constructor docstring wraps. `uvx --from ruff ruff check --select E501
  category_specs/rings/__init__.py` and `python -m compileall
  category_specs/rings/__init__.py` now pass. Repo-wide E501 count is now 681.
- 2026-05-06: Cleared the `category_specs/sets/__init__.py` slice with
  `uvx --from ruff ruff format category_specs/sets/__init__.py` plus short manual
  docstring/message wraps. `uvx --from ruff ruff check --select E501
  category_specs/sets/__init__.py` and `python -m compileall
  category_specs/sets/__init__.py` now pass. Repo-wide E501 count is now 616.
- 2026-05-06: Cleared the
  `category_specs/rings/subcategories/_lazy_subcategories.py` slice with
  `uvx --from ruff ruff format`. `uvx --from ruff ruff check --select E501
  category_specs/rings/subcategories/_lazy_subcategories.py` and `python -m
  compileall category_specs/rings/subcategories/_lazy_subcategories.py` now pass.
  Repo-wide E501 count is now 571.
- 2026-05-06: Cleared the `category_specs/posets/__init__.py` slice with
  `uvx --from ruff ruff format` plus short manual semilattice docstring wraps.
  `uvx --from ruff ruff check --select E501 category_specs/posets/__init__.py`
  and `python -m compileall category_specs/posets/__init__.py` now pass.
  Repo-wide E501 count is now 529.
- 2026-05-06: Cleared the `category_specs/cat/base_category_types.py` slice with
  `uvx --from ruff ruff format` plus manual wrapping of one long Sage import alias
  and assertion messages. `uvx --from ruff ruff check --select E501
  category_specs/cat/base_category_types.py` and `python -m compileall
  category_specs/cat/base_category_types.py` now pass. Repo-wide E501 count is now
  489.
- 2026-05-06: Cleared the `category_specs/algebras/__init__.py` slice with
  `uvx --from ruff ruff format` plus manual wrapping of algebra constructor
  docstrings, assertion messages, and one long finite-dimensional-algebra import.
  `uvx --from ruff ruff check --select E501 category_specs/algebras/__init__.py`
  and `python -m compileall category_specs/algebras/__init__.py` now pass.
  Repo-wide E501 count is now 452.
- 2026-05-06: Cleared the
  `category_specs/rings/subcategories/number_field.py` slice with `uvx --from
  ruff ruff format`. `uvx --from ruff ruff check --select E501
  category_specs/rings/subcategories/number_field.py` and `python -m compileall
  category_specs/rings/subcategories/number_field.py` now pass. Repo-wide E501
  count is now 427.
- 2026-05-06: Cleared the `category_specs/tensor_algebra_components/__init__.py`
  slice with `uvx --from ruff ruff format` plus manual wrapping of tensor
  assertion messages and short constructor docstrings. `uvx --from ruff ruff
  check --select E501 category_specs/tensor_algebra_components/__init__.py` and
  `python -m compileall category_specs/tensor_algebra_components/__init__.py`
  now pass. Repo-wide E501 count is now 403.
- 2026-05-06: Cleared the
  `category_specs/rings/subcategories/rational_field.py` slice with `uvx --from
  ruff ruff format`. `uvx --from ruff ruff check --select E501
  category_specs/rings/subcategories/rational_field.py` and `python -m
  compileall category_specs/rings/subcategories/rational_field.py` now pass.
  Repo-wide E501 count is now 380.
- 2026-05-06: Cleared the `category_specs/forms/chain.py` slice with `uvx
  --from ruff ruff format` plus manual wrapping of canonical-chain docstrings
  and a long `LazyImport`. `uvx --from ruff ruff check --select E501
  category_specs/forms/chain.py` and `python -m compileall
  category_specs/forms/chain.py` now pass. Repo-wide E501 count is now 362.
- 2026-05-06: Cleared the `category_specs/forms/__init__.py` slice with `uvx
  --from ruff ruff format` plus manual cleanup of long chain re-export aliases.
  `uvx --from ruff ruff check --select E501 category_specs/forms/__init__.py`
  and `python -m compileall category_specs/forms/__init__.py` now pass.
  Repo-wide E501 count is now 346.
- 2026-05-06: Cleared the `category_specs/forms/subcategories/bilinear.py` slice
  with `uvx --from ruff ruff format` plus manual wrapping of bilinear-form method
  docstrings. `uvx --from ruff ruff check --select E501
  category_specs/forms/subcategories/bilinear.py` and `python -m compileall
  category_specs/forms/subcategories/bilinear.py` now pass. Repo-wide E501 count
  is now 331.
- 2026-05-06: Cleared the
  `category_specs/sets/subcategories/constructions/subobjects.py` slice with `uvx
  --from ruff ruff format` plus manual wrapping of subset docstrings and
  `NotImplementedError` messages. `uvx --from ruff ruff check --select E501
  category_specs/sets/subcategories/constructions/subobjects.py` and `python -m
  compileall category_specs/sets/subcategories/constructions/subobjects.py` now
  pass. Repo-wide E501 count is now 319.
- 2026-05-06: Cleared the
  `category_specs/posets/subcategories/finite_lattice.py` slice with `uvx --from
  ruff ruff format` plus manual wrapping of finite-lattice certificate
  docstrings. `uvx --from ruff ruff check --select E501
  category_specs/posets/subcategories/finite_lattice.py` and `python -m
  compileall category_specs/posets/subcategories/finite_lattice.py` now pass.
  Repo-wide E501 count is now 308.
- 2026-05-07: Cleared the
  `category_specs/sets/subcategories/recursively_enumerated.py` slice with `uvx
  --from ruff ruff format` plus manual wrapping of recursive-enumeration messages
  and one graph-constructor docstring. `uvx --from ruff ruff check --select E501
  category_specs/sets/subcategories/recursively_enumerated.py` and `python -m
  compileall category_specs/sets/subcategories/recursively_enumerated.py` now
  pass. Repo-wide E501 count is now 298.
- 2026-05-07: Cleared the
  `category_specs/modules/subcategories/constructions/quotients.py` slice with
  `uvx --from ruff ruff format` plus manual wrapping of quotient-constructor
  docstrings. `uvx --from ruff ruff check --select E501
  category_specs/modules/subcategories/constructions/quotients.py` and `python
  -m compileall category_specs/modules/subcategories/constructions/quotients.py`
  now pass. Repo-wide E501 count is now 289.
- 2026-05-07: Cleared the `category_specs/modules/subcategories/quadratic.py`
  compatibility re-export slice with `uvx --from ruff ruff format`. `uvx --from
  ruff ruff check --select E501 category_specs/modules/subcategories/quadratic.py`
  and `python -m compileall category_specs/modules/subcategories/quadratic.py`
  now pass. Repo-wide E501 count is now 281.
- 2026-05-07: Cleared the `category_specs/modules/subcategories/free.py` slice
  with `uvx --from ruff ruff format`. `uvx --from ruff ruff check --select E501
  category_specs/modules/subcategories/free.py` and `python -m compileall
  category_specs/modules/subcategories/free.py` now pass. Repo-wide E501 count is
  now 273.
- 2026-05-07: Cleared the `category_specs/modules/subcategories/bilinear.py`
  compatibility re-export slice with `uvx --from ruff ruff format`. `uvx --from
  ruff ruff check --select E501 category_specs/modules/subcategories/bilinear.py`
  and `python -m compileall category_specs/modules/subcategories/bilinear.py` now
  pass. Repo-wide E501 count is now 265.
- 2026-05-07: Cleared the `category_specs/lattices/__init__.py` slice with `uvx
  --from ruff ruff format`, preserving the lattice axiom chain and constructor
  names. `uvx --from ruff ruff check --select E501 category_specs/lattices/__init__.py`
  and `python -m compileall category_specs/lattices/__init__.py` now pass.
  Repo-wide E501 count is now 257.
- 2026-05-07: Cleared the `category_specs/modules/subcategories/with_forms.py`
  compatibility re-export slice with `uvx --from ruff ruff format`. `uvx --from
  ruff ruff check --select E501 category_specs/modules/subcategories/with_forms.py`
  and `python -m compileall category_specs/modules/subcategories/with_forms.py`
  now pass. Repo-wide E501 count is now 250.
- 2026-05-07: Cleared the `category_specs/rings/subcategories/integral_domain.py`
  slice with `uvx --from ruff ruff format`. `uvx --from ruff ruff check --select
  E501 category_specs/rings/subcategories/integral_domain.py` and `python -m
  compileall category_specs/rings/subcategories/integral_domain.py` now pass.
  Repo-wide E501 count is now 244.
- 2026-05-07: Cleared the `category_specs/posets/subcategories/finite.py` slice
  with `uvx --from ruff ruff format`. `uvx --from ruff ruff check --select E501
  category_specs/posets/subcategories/finite.py` and `python -m compileall
  category_specs/posets/subcategories/finite.py` now pass. Repo-wide E501 count
  is now 238.
- 2026-05-07: Cleared the `category_specs/modules/subcategories/with_basis.py`
  slice with `uvx --from ruff ruff format`. `uvx --from ruff ruff check --select
  E501 category_specs/modules/subcategories/with_basis.py` and `python -m
  compileall category_specs/modules/subcategories/with_basis.py` now pass.
  Repo-wide E501 count is now 232.
- 2026-05-07: Cleared the
  `category_specs/forms/subcategories/nondegenerate.py` slice with `uvx --from
  ruff ruff format` plus manual wrapping of the module docstring header. `uvx
  --from ruff ruff check --select E501
  category_specs/forms/subcategories/nondegenerate.py` and `python -m compileall
  category_specs/forms/subcategories/nondegenerate.py` now pass. Repo-wide E501
  count is now 226.
