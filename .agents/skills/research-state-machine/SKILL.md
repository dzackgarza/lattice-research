---
name: research-state-machine
description: Use when moving research work from plan to execution, deciding whether
  a card is atomic, routing implementation/self-check/adversarial audit, promoting
  or rejecting results, or claiming GOAL.md discharge.
---

# Research State Machine

This skill is the canonical execution-state authority for the research repo.

## Canonical source

The source of truth is this skill plus `references/execution-kernel.md`.

Read `references/execution-kernel.md` before moving work from planning into execution, delegating implementation, judging whether a card is atomic, routing replay/attack, accepting/rejecting/splitting work, or claiming parent-plan or `GOAL.md` discharge.


## Core model

- Nimbalyst plans and cards are the task specs.
- Git branches, PRs, commits, and worktrees are the provenance and review layer.
- Produced proof/computation/code artifacts live in their natural durable roots.
- Proof and evidence sufficiency is governed by `research-proof-auditing`.
- Heavy controls trigger only when theorem burden, parent-plan discharge, or `GOAL.md` discharge is being promoted.

## Live stages

- Plan: collaborate with the human and approve complex plans before decomposition.
- Specify card: create a tracked card with exact claim/work target, scope, provenance, dependencies, acceptance criteria, and verification plan.
- Preflight: reject or split hidden-major-work cards before execution.
- Execute: run scoped implementation in the required branch/worktree and update card metadata.
- Replay and attack: independently test the strongest claim and proof/evidence surface.
- Promote, reject, split, or retire: human-gated promotion; otherwise split or reject and keep active paths forward-facing.

## Hard stops

- Do not execute an unapproved complex plan.
- Do not one-shot an overscoped card that hides major theorem, algorithm, convention, classification, or trusted-base work.
- Do not patch around missing mathematical vocabulary or missing trusted-base operations.
- Do not let an implementing agent mark work accepted, done, or closed.
- Do not claim `GOAL.md` discharge without final composed-goal audit and human approval.

Hard stops are scoped to the affected card, path, or promotion claim unless the current
approved phase has no other executable leaves. When a hard stop fires, file or update
the prerequisite card/decision/research item, then continue another approved active
leaf. Do not exit the user's active goal merely because one path is blocked.

Before reporting that all paths are blocked, enumerate the approved active plans and
leaf cards considered, name each current-phase blocker, and exclude downstream guards,
non-transition QC failures, and implementation-only gates that do not apply to current
spec work.

## Load with

- Load `research-project-workflow` for Nimbalyst plan/card mechanics.
- Load `research-proof-auditing` for proof, evidence, formal verification, and fraud checks.
- Load `research-orchestration` for subagent contracts, worktrees, self-check, adversarial audit, and durable artifact handoff.
- Load `research-math-boundary` when preflight reveals missing foundational mathematical nouns, methods, conventions, or backend bridges.
