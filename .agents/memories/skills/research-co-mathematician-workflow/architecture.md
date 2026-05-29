---
title: Co-Mathematician Workflow Architecture
status: active
date: 2026-05-29
---
# Co-Mathematician Workflow Architecture

Adapts the workflow architecture from Zheng et al.,
`AI Co-Mathematician: Accelerating Mathematicians with Agentic AI`
(`arXiv:2605.06651v1`) to this repo.

## Preserved Substrate

- durable markdown cards under `.agents/plans/`;
- schema validation through `.nimbalyst/trackers/` and `just`;
- IWE/bash-indexable text;
- git provenance;
- a coherent hierarchy.

Everything above that substrate can evolve.

## Workspace Model

The repo is a mathematical workspace with five coordinated surfaces:

- `.agents/plans/`: indexable state, dependencies, workstream structure, and review
  gates.
- `paper/`: the living LaTeX working paper with margin-note style claim status.
- `reports/workstreams/`: workstream reports and attachments that feed the paper.
- `.agents/agent-roles/`: repo-local prompts and delegation contracts for specialist
  agents.
- source roots such as `theory/`, `notes/`, `src/`, `tests/`, and `lean/`: evidence and
  implementation artifacts.

Cards are not the final mathematical medium.
They route work and preserve state.
The working paper and workstream reports rebuild the human mental model.

## Intake

Intake is a durable phase, not a conversation warmup.
It must record:

- the user's research question in the user's terms;
- refined goals and non-goals;
- hard constraints and forbidden shortcuts;
- source context and primers supplied by the user;
- candidate workstreams;
- success criteria and uncertainty policy;
- what requires human approval before execution.

Do not open autonomous research workstreams until the intake framing is approved.

## Activity Taxonomy

Research tasks classified by `activityType`. First-class activities: intent refinement,
literature search and source mining, brainstorming and conjecture generation,
counterexample search, proof attempt and proof repair, formalization,
computation/numerical experiment/simulation, implementation, validation and citation
checking, synthesis and exposition, review, failure analysis, user escalation.

Different activities have different evidence standards.
A numerical experiment builds intuition; it does not prove a theorem.
A literature search supplies exact hypotheses; it does not discharge implementation.
A failed proof can still preserve a useful strategy.

## Workstreams

Use phase cards with `phaseKind: workstream` for substantial branches.
A workstream: attaches to an approved goal, follows one branch type, has an agent
roster, produces a report artifact, sends serious claims to review, preserves failed
explorations.
