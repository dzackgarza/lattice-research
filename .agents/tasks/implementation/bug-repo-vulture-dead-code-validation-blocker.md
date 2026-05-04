---
trackerStatus:
  type: bug
title: Triage global vulture dead-code validation blocker
status: to-do
priority: high
planId: SPR-VARIADIC-AUDIT-01KQN9
complexity: 78
progress: 45
created: '2026-05-03'
updated: '2026-05-03'
tags:
  - category-specs
  - implementation
  - bug
  - audit
  - validation
  - quality-control
  - vulture
  - theme-audit-uniformity
---

# Triage global vulture dead-code validation blocker

## Summary

`just test` now passes Ruff normalization and fails at the global vulture dead-code
detection stage. The failure is broad and includes category-spec abstract/public
surfaces plus `theory/spec_backups/lattices_written_spec_backup.py`.

## Source Provenance

- Discovered while validating the Cat final-marker task after resolving the Ruff
  normalization blocker.
- `just test` on 2026-05-03 reports `All checks passed!` for Ruff, then fails in
  `=== Running: vulture dead code detection ===` with exit code 3.
- Representative findings include package re-export variables in
  `category_specs/__init__.py`, abstract category/spec methods throughout
  `category_specs/**`, many public type aliases in `category_specs/types.py`, and
  unreachable code in `theory/spec_backups/lattices_written_spec_backup.py`.
- The global QC command uses `/home/dzack/ai/quality-control/vulture_whitelist.py`.
  That whitelist already contains category-spec abstract interface names, so this is
  likely an outdated or incomplete global whitelist/policy surface rather than one
  local implementation bug.

## Context

Vulture does not understand Sage's dynamic method-provider and public type-surface
patterns without a whitelist. Many findings are intentional category-spec API surfaces,
not dead code that can be deleted. At the same time, some findings may be real stale
spec debris or backup-file issues. Treat this as a triage problem before deleting or
whitelisting anything.

## Triage Result

Codex Spark read-only triage on 2026-05-03 reproduced the vulture failure with 764
parsed findings:

- 762 findings under `category_specs`.
- 3 findings under `theory/spec_backups/lattices_written_spec_backup.py`, including
  one syntax warning and two unreachable-code findings.

The dominant category-spec findings are intentional public or dynamic surfaces: abstract
category methods, Sage method-provider hooks, package re-export variables, and public
type-package aliases. The current global whitelist in
`/home/dzack/ai/quality-control/vulture_whitelist.py` is therefore incomplete for the
current category-spec surface.

The blocker is split into:

- `.agents/tasks/implementation/bug-global-qc-vulture-category-spec-whitelist-gap.md`
- `.agents/tasks/implementation/bug-theory-spec-backup-vulture-cleanup.md`

## Complexity And Ownership

- Owner role: validation/QC triage worker with parent review.
- Complexity: 78, high band.
- Rationale: the work crosses global QC policy, category-spec public surfaces, and
  theory backup files. It is not safe to mechanically delete or globally whitelist
  every finding without classifying which names are intentional framework surfaces,
  stale debris, or real dead code.

## Acceptance Criteria

- [ ] Reproduce the vulture failure after Ruff normalization passes.
- [ ] Classify findings by owner and cause: intentional category-spec API, Sage dynamic
  method surface, type alias public surface, generated/backup debris, or real dead code.
- [ ] Do not add project-local vulture bypasses, ignores, or QC overrides.
- [ ] If a global QC whitelist update is necessary, document the exact proposed global
  change and request approval before editing `/home/dzack/ai/quality-control`.
- [ ] Split owner-specific cleanup cards for real dead code or stale backup artifacts
  that should be fixed in this repo.
- [ ] Record the remaining validation blocker after triage.

## Dependencies And Boundaries

- Parent blocker:
  `.agents/tasks/implementation/bug-category-specs-ruff-normalization-blocker.md`.
- Do not delete category-spec methods, aliases, or standard type packages just because
  vulture cannot see dynamic Sage usage.
- Do not edit the global vulture whitelist without explicit approval for a global QC
  policy change.
- Do not hide the failure behind local lint-bypass comments, local whitelist files, or
  project-local QC configuration.

## Validation Requirements

- Run `just test` after any attempted fix or approved global QC change.
- If only triaging, preserve enough representative vulture output to route the next
  card.

## Work Log

- 2026-05-03: Created after Ruff normalization blockers were resolved and `just test`
  advanced to global vulture dead-code detection.
- 2026-05-03: Codex Spark read-only triage classified the failure as primarily a
  global vulture whitelist/policy gap for category-spec public dynamic surfaces, with a
  small separate theory backup cleanup surface.
