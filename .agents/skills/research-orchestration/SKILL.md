---
name: research-orchestration
description: Use when orchestrating research work in this repo. Delegates execution to STATE_MACHINE.md as the one source of truth and enforces its delegation, worktree, and acceptance requirements.
---

# Research Orchestration

## Required Reading

Re-read any item below completely if it is not already in context.
This is mandatory required reading, not optional.
Any source cross-referenced by this skill or by `subagent-delegation` that becomes relevant to self-assessment must also be re-read completely before you rely on it.
Honest self-assessment requires current source text, not memory or summary.

- `STATE_MACHINE.md`
- `PROOF_AUDITING.md`
- `subagent-delegation`

## One Source of Truth

- `STATE_MACHINE.md` is the execution constitution and the one source of truth for task states, role boundaries, worktree requirements, and acceptance.
- `PROOF_AUDITING.md` is the one source of truth for proof, evidence, fraud handling, and audit sufficiency.
- `subagent-delegation` is the one source of truth for when delegation is warranted, how delegation prompts must be framed, startup-cost calibration, transcript review, and anti-theater correction.
- This skill is only a repo-local overlay. It does not restate delegation policy.

## Repo Overlay

- NEVER weaken acceptance criteria.
- NEVER allow hand-rolled code; use library docs.
- NEVER allow implementation outside of worktrees.
- NEVER accept code or audits until it is proved that the `STATE_MACHINE` process was followed COMPLETELY.
- ALWAYS encode contract assertions into reusable functions.
- If ANYTHING has been violated, trash poisoned work IMMEDIATELY and restart.
- Continue from `STATE_MACHINE.md`, not from improvised process.
- Implementation, self-check, and adversarial-audit ownership are defined by `STATE_MACHINE.md`; do not collapse or reassign them ad hoc.

## Project Lens

- The goal is substantive mathematical work with trustworthy independent verification, not maximum visible activity.
- Apply `subagent-delegation` through the lens of mathematical value: real uncertainty reduced, real claims checked, and real downstream trust improved.
- Re-read `subagent-delegation` when the work starts to look like process maintenance, transcript churn, or metadata theater instead of mathematical progress.
- If the task is blocked because the semantic base lacks the right noun, method, morphism, coercion, or interop bridge, stop and treat that as a task-boundary failure. Re-read `STATE_MACHINE.md` and surface the need for a base task plus a redesigned dependent task; do not patch around it locally.
- If the current work is on-track, the relevant sources are already in context, and the trust guards are functioning as intended, this reminder should be a no-op. Continue.
