---
trackerStatus:
  type: plan
title: Research staged semantic mathematics program
status: approved
planId: PLN-RESEARCH-000
planType: program
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
tags:
  - plan
  - phase-control
  - category-specs
  - semantic-math
---

# Research staged semantic mathematics program

## Objective

Turn the strategic staging in `GOAL.md` into the operative plan tree for the repo.
Downstream Coble research is blocked until the semantic category, lattice, and geometry
language exists and can express the relevant mathematical arguments without ad hoc raw
matrix or polynomial scripts.

## Phase tree

- `PLN-PHASE-01`: category specs and semantic vocabulary.
- `PLN-PHASE-02`: Sage refinement and gap discovery.
- `PLN-PHASE-03`: owned categorical implementation layer.
- `PLN-PHASE-04`: universal categorical algorithms.
- `PLN-PHASE-05`: lattice-theoretic implementation, with small Lean formalization targets.
- `PLN-PHASE-06`: scheme, variety, curve, surface, and family interfaces, with geometry-facing formalization vocabulary.
- `PLN-PHASE-07`: confined experimental Coble research, publishable findings, and proof formalization.

## Current state

The repo is in `PLN-PHASE-01`. Existing active plans have been organized under
`.agents/plans/phase-01-category-specs/` because they all support spec, vocabulary,
Sage-source, lattice-spec, or geometric-category groundwork.

## Gate policy

Each phase blocks the next. QC gates implementation surfaces and phase transitions, but
spec drafting is controlled by human/LLM review, source audits, and mathematical rewrite
cycles before implementation QC becomes relevant.

## Formalization thread

Lean formalization is mixed into the later research phases, not deferred as one giant
end-stage proof attempt. The project should formalize small definitions, lemmas, and
library vocabulary as soon as the corresponding semantic objects are stable enough to
state cleanly. Aristotle can run asynchronously for bounded formalization attempts, but
its output is research evidence only after the resulting Lean code is checked, reviewed,
and tied back to the mathematical plan.

The final phase includes both finding publishable mathematical results and formalizing
the proofs that are mature enough to support the paper-level argument.

## Acceptance Criteria

- [ ] Every active plan lives under the phase directory it advances.
- [ ] Current phase is recorded in `.agents/current-goal-phase.md`.
- [ ] Downstream implementation and Coble research cards link to the prerequisite phase plans.
- [ ] Later-phase plans contain explicit Lean/Aristotle formalization tracks for small results before major theorems.
- [ ] No phase transition is claimed without mathematical review and relevant QC evidence.
