---
name: category-spec-visuals
description: Use when creating or updating human-facing visual windows for category-spec
  structure, workstream dependencies, category inheritance, constructor routing, audit
  surfaces, or plan/task decomposition.
---

# Category Spec Visuals

Use this skill when a visual artifact would help a human understand or steer complex category-spec work.

## Canonical references

Before creating or updating visuals:

- Load `category-spec-workflow`, especially the human-facing visual artifact policy.
- Read `.agents/visuals/README.md`.

## Visual routing

- Use Mermaid for versionable diagrams: dependencies, category inheritance, constructor routing, state machines, and plan-to-task breakdowns.
- Use Excalidraw for spatial architecture, ambiguous organization, and whiteboarding.
- Use data models for tracker metadata, plan/task relationships, audit state, and category/spec object relationships.
- Use mockups for cheap browsable windows into dashboards, audit status, and complex category views.

## Rules

- Visuals are windows into complex systems, not authoritative state.
- Link each visual to the owning plan, card, decision, or PR.
- Do not create a visual-only work tracker.
- Update or retire visuals when their owning artifact changes.
