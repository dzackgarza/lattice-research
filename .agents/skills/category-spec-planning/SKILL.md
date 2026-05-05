---
name: category-spec-planning
description: Use after the user asks to plan category-spec work, decompose an approved
  plan into cards, or organize plan phases into task/decision/research work.
---

# Category Spec Planning

Use this skill for planning and plan decomposition around `category_specs`.

## Planning gate

Plans are human + LLM collaborative artifacts. Do not create or enact an operative plan unilaterally.

Before implementation:

- Switch to planning mode when creating or materially revising a plan.
- Iterate with the user until the plan is explicitly approved.
- Store the approved plan under root `plans/features/FEATURE-ID/plans/PLAN-ID/`.
- Decompose the approved plan into concrete tracked cards.

## Decomposition rules

- Use `feature` cards only for feature roots.
- Use `spec` cards for feature-owned spec surfaces.
- Use `task` cards for executable implementation, research, bug-fix, smoke-triage, and audit work.
- Use `decision` cards for unresolved mathematical or organizational choices.
- Put executable tasks under the relevant plan phase's `tasks/` directory.
- Add acceptance criteria and source provenance to every executable card.
- Link cards back to the approved plan.

## References

Load `category-spec-workflow` for the canonical planning workflow, priority rubric, theme grouping, and card requirements.
