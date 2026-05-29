---
title: Category Spec Workflow Reference
status: active
date: 2026-05-29
---
This reference is the full workflow.md for category-spec work.

## Contents

- Tracking and planning: Use Nimbalyst tracker files.
  No separate backlog.
  Approved plans and active tracked cards are the concrete continuation surface.
- Theme grouping: Use `theme-*` tags to group workstreams.
  They do not order work.
- Rubric skills: Load `category-spec-priority-rubric` and
  `category-spec-complexity-rubric` before scoring cards.
- Plan creation workflow: Plans are human + LLM artifacts, approved before
  decomposition.
- Human-facing visual artifacts: Visuals are windows into complex systems, not
  authoritative state.
- TODO scratchpad: `.agents/TODO.md` is a scratch receptacle for vague findings before
  they become cards.
- Retired card holding: `.agents/retired/` is temporary.
  Durable history in git.
- Full task card requirements: Card ID matches filename stem.
  Use `trackerStatus` frontmatter.
- Tangential discovery: File real tracked cards for concrete findings.
  `.agents/TODO.md` for investigation-needed.
- Delegation contracts: Include task statement, files in scope, allowed/forbidden
  actions, expected output, exit condition.
- Agent execution workflow: Follow `research-state-machine` stages.
- Branch and PR policy: Work in worktrees.
  PRs for significant work only.
- Smoke test and triage: Do not run smoke when violations remain unresolved.
  Route smoke findings to cards.
- Documentation lifecycle: Completed work should migrate docs to `docs/` or
  `archived_docs/`.
