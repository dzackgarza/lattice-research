---
name: category-spec-triage
description: Use when organizing category-spec cards, applying theme groups, setting
  priority metadata from the documented rubric, triaging TODO entries, or preparing
  high-level dependency views.
---

# Category Spec Triage

Use this skill for project-management triage of `category_specs` work. This skill routes agents to the canonical workflow skill.

## Required references

Load `category-spec-workflow` before changing card metadata.

Use the workflow reference for:

- Theme grouping for `theme-*` workstream tags.
- Priority rubric for the `priority` metadata field.
- TODO scratchpad and inline task marker policy.
- Retired-card holding policy.
- Human-facing visual artifact policy.

## Rules

- Encode priority only in the `priority` field.
- Do not create `priority-*` tags.
- Use tags for topic, domain, workstream, and workflow class.
- Use `.agents/visuals/` for high-level dependency views.
- Keep active cards forward-facing; move resolved cards to `.agents/retired/` only temporarily.
- Do not create a separate backlog.

## Triage steps

- Confirm every active card has `trackerStatus`, `status`, and topic/workstream tags.
- Confirm task-like cards have `priority` metadata.
- Group cards with `theme-*` tags when free-floating work becomes hard to review.
- Update or create a high-level dependency graph when priority depends on workstream ordering.
- Convert clear `.agents/TODO.md` entries into real cards.
- Retire or delete resolved cards after durable history is recorded elsewhere.
