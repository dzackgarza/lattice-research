# Active Plan Index

## Current operating rule

Literature comes first.
Standard facts belong to canonical references and concise repo citations; computations
support those claims, they do not substitute for them.

## Active work thread

- None — awaiting next directive.

## Documentation budget

Canonical notes stay in audit/, transient artifacts get archived.
Recent pruning:
- Archived 14 .txt transcripts (3593 lines) superseded by solved proof notes
- Archived 2 duplicate audit reports
- Removed reports/ directory (content duplicated GAPS.md)

## Recently completed plans

- `plans/2026-03-30-verify-all-computations.md` — INCOMPLETE: Phase 1-3 verified scripts
  execute without errors (15/17 pass, 2 failures in alternative implementations not
  referenced by proof notes).
  Phase 4 mathematical correctness verification was circular (compared documentation to
  itself) and needs Prover subagent work.
- `plans/2026-03-30-refactor-stabilizer-orbit-utilities.md` — completed refactoring of
  duplicate utilities; consolidated to_affine and dehomogenize_at_one into
  coble_geometry.sage (88 lines eliminated), fixed K_a ring structure bug.
- `plans/2026-03-30-refactor-duplicate-lattice-definitions.md` — completed lattice
  definition refactoring; consolidated hyperbolic_plane and E8_lattice into
  coble_geometry.sage (45 lines eliminated).
- `plans/2026-03-30-documentation-pruning.md` — completed documentation pruning;
  archived 14 .txt transcripts (3593 lines) and 2 duplicate audit reports, removed
  reports/ directory.
- `plans/2026-03-30-remaining-verification-notes.md` — completed verification note
  creation for all remaining computational tasks; repo now has 10 solved proof notes
  covering all 20 computation scripts (task1_1, task1_2, task1_3, task2_1, task2_2,
  task3_1, task3_2, task4_1, task5_1, task6_1).
- `plans/2026-03-30-mathematical-verification-work.md` — completed mathematical
  verification work plan; created 3 new solved proof notes (task2_1, task4_1, task5_1)
  after user correction about documentation churn.
- `plans/2026-03-30-weave-citations-into-prose.md` — completed citation-weaving plan;
  inline literature citations now added to solved proof notes for K3/lattice setup and
  2-elementary lattice classification.
- `plans/2026-03-29-stronger-source-boundary-audit.md` — completed stronger-source
  boundary audit; both stronger-wording layers (Coolidge theorem paraphrase and J. Thas
  uniqueness attribution) are now explicitly fenced as unresolved at primary-source
  level.
- `plans/2026-03-29-explicit-family-source-audit.md` — completed source-audit plan;
  surviving explicit-family leads are now split into direct primary support, archived
  secondary support, and unresolved stronger-source wording.
- `plans/2026-03-28-task5_1-status-alignment.md` — completed post-theta status-alignment
  plan; live Task 5.1 prose now routes readers to the canonical exact involution note.
- `plans/2026-03-28-task5_1-theta-verification.md` — completed exact theta-verification
  plan; the sign action now passes integrality and isometry checks on the explicit glued
  ambient lattice.
- `plans/2026-03-28-task5_1-primitive-complement.md` — completed Task 5.1 gate plan; the
  primitive embedding / orthogonal complement slice now passes exact verification.
- `plans/2026-03-28-literature-first-reorientation.md` — completed literature-first
  reset that established the current citation spine and claim notes.
- `plans/2026-03-28-task5_1-prose-cleanup.md` — completed prose-alignment and narrow
  cleanup thread that rewrote the solved proof notes and removed explicitly triaged
  debris.

## Archived plans

- `plans/archive/2026-03-28-audit-first-recovery-plan.md` — superseded because it let
  local recomputation outrun literature grounding.
- `plans/archive/task1_1_example2-legacy.md` — completed narrow example plan archived
  out of `.serena/`.

## Current priorities

- Centralize the literature spine in `REFERENCES.md`.
- Keep exact numerical evidence, but attach each computation to a literature-backed
  claim.
- Use `audit/task5_1_exact_involution_note.md` as the canonical post-theta boundary
  note, and isolate any remaining claim-alignment or prose gaps without reopening the
  disproved route; keep CARAT auxiliary only for finite positive-definite subproblems.
