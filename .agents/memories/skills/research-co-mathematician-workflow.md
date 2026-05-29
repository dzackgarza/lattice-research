---
title: Research Co-Mathematician Workflow
status: active
date: 2026-05-29
---
# Research Co-Mathematician Workflow

Treats the repo as a stateful mathematical workspace, not a task queue with proof checks
attached.

## Core Policy

- Start substantial research with intake: clarify the user's question, goals, non-goals,
  hard constraints, source context, success criteria, and approved initial workstreams.
- Treat mathematics as multi-modal work: literature search, source mining,
  brainstorming, conjecture formation, counterexample search, numerical exploration,
  simulation, implementation, proof, formalization, exposition, review, and failure
  analysis.
- Maintain native mathematical artifacts: living LaTeX working paper with margin-note
  style uncertainty annotations.
- Organize agents as a hierarchy: active chat/harness is coordinator; delegated agents
  are workstream coordinators, literature/source agents, computational explorers, proof
  strategists, implementers, reviewers, and uncertainty auditors.
- Track uncertainty as state: disputed lemma, missing citation, unreplayed computation,
  stalled review = claim-state transition visible to user and future agents.
- Preserve failed explorations when they teach.
  Do not preserve broken code.

## Required Reading

Read `mem:skills/research-co-mathematician-workflow/architecture` before creating or
revising intake artifacts, workstream phases, report templates, paper sections,
agent-role prompts, or uncertainty rules.

## Decision Procedures

Intake when: user asks for new research direction, plan would encode vague goals, source
primer needs translation.

Workstreams when: goal naturally splits into branches, user needs async steering, branch
can fail while still producing useful information.

Living paper when: claim shapes mathematical narrative, result should be readable
outside card system, margin notes expose provenance better than task log.

Escalate when: review stalls on precise assertion, reviewers only agree after weakening,
next step depends on mathematical taste.

## Artifact work must feed the research narrative

A report, card, or handoff is useful only if it changes the living mathematical
narrative: a claim, obstruction, construction, computation, proof route, or
source-grounded implementation boundary.

## Validation

- Planning/card changes: `just plan-validate`.
- Living paper changes: `just paper-build`.
- Reports and paper sections must link back to cards, sources, computations, or review
  artifacts.
