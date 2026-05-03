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
- Store the approved plan under `.agents/plans/`.
- Decompose the approved plan into concrete tracked cards.

## Decomposition rules

- Use `task` or `feature` cards for executable work.
- Use `bug` cards for defects.
- Use `decision` cards for unresolved mathematical or organizational choices.
- Use research cards for source, Sage, literature, or backend investigation.
- Add acceptance criteria and source provenance to every executable card.
- Link cards back to the approved plan.

## References

Load `category-spec-workflow` for the canonical planning workflow, priority rubric, theme grouping, and card requirements.
