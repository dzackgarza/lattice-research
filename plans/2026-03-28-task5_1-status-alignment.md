# Task 5.1 post-theta status alignment

## Goal

- Current defect/state: the exact glued-model route now verifies a primitive
  decomposition and an integral lattice involution, but the directive layer still talks
  as if theta verification were the next step.
- Target state: the repo's active docs state the exact post-theta status clearly and
  make one narrow follow-on task explicit: record what the current computation proves,
  and what still belongs to the literature-backed interpretation layer.
- Why this matters: after a hard-won exact verification pass, stale blocked-language is
  just as misleading as stale solved-language was earlier.

## Constraints

- Required:
  - Keep `audit/task5_1_route_reset.md` canonical for the corrected route order.
  - Keep `computations/task5_1_involution.sage` and its checked artifacts as the exact
    source of truth for the glued-model verification.
  - Distinguish exact lattice verification from broader geometric interpretation.
- Forbidden:
  - No reopening the disproved ad hoc theta route.
  - No overclaim that the current exact model alone replaces the literature layer.
  - No broad cleanup drift.

## Scope

- Included targets:
  - `PLAN.md`
  - `GAPS.md`
  - `audit/task5_1_route_reset.md`
  - `audit/task5_1_exact_involution_note.md`
- Excluded for this slice:
  - new computational searches
  - Lean formalization
  - unrelated report cleanup

## Phase 0: Normalize directive files

Goal: remove stale pre-theta wording from the active docs.

- Location: `PLAN.md`, `GAPS.md`, this plan file
- Description:
  - record that theta verification now passes on the explicit glued model;
  - point the active work thread at claim/status alignment instead of more raw lattice
    construction.
- Dependencies: none.
- Acceptance criteria: no directive file says theta verification is still pending.
- Validation: inspect
  `git diff -- PLAN.md GAPS.md plans/2026-03-28-task5_1-status-alignment.md`.

## Phase 1: Update the canonical route note

Goal: keep the reset note accurate after the route has succeeded.

- Location: `audit/task5_1_route_reset.md`
- Description:
  - preserve the failure record and corrected route order;
  - replace the stale "next target" section with the new post-theta status and next
    prose boundary.
- Dependencies: Phase 0.
- Acceptance criteria: the note still explains the old failure, but no longer instructs
  already-completed work.
- Validation: inspect `git diff -- audit/task5_1_route_reset.md`.

## Phase 2: Define the next claim-alignment note

Goal: choose the canonical place to state what the glued-model involution proves and
what it does not yet claim.

- Location: `audit/task5_1_exact_involution_note.md`
- Description:
  - state the exact lattice result;
  - state the remaining interpretation boundary.
- Dependencies: Phase 1.
- Acceptance criteria: future agents have one canonical prose target for the post-theta
  status instead of rediscovering it from output files.
- Validation: inspect this plan plus `GAPS.md` and ensure both point to
  `audit/task5_1_exact_involution_note.md`.

## System-Level Validation

- Active docs no longer advertise theta verification as pending.
- The canonical route note stays accurate after the successful glued-model check.
- One follow-on prose target is named for claim-boundary alignment.

## Risks / Rollback

- Risks:
  - overclaiming from the exact model;
  - scattering the post-theta status across multiple prose files.
- Mitigations:
  - write one canonical note and point to it elsewhere;
  - keep literature-backed claims separate from computation-backed claims.
- Rollback path:
  - if the chosen prose location proves wrong, move the status note in a follow-up
    commit without changing the underlying computation artifacts.

## Stop Rules

- Do not reopen the computation unless a claimed fact cannot be tied to the checked
  output files.
- Do not broaden into general literature cleanup in this thread.

## Execution Progress

### Phase 0

- [x] Normalize `PLAN.md` and `GAPS.md`

### Phase 1

- [x] Update `audit/task5_1_route_reset.md`

### Phase 2

- [x] Choose `audit/task5_1_exact_involution_note.md` as the canonical post-theta status
  note target

### Quality Gates

- [x] Directive files match the verified post-theta state
- [x] The route note no longer instructs completed work
- [x] A single follow-on prose target is named
