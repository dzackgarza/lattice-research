---
trackerStatus:
  type: plan
title: 'Smoke audit and uniformity stabilization'
status: needs-approval
planId: PLN-AUDIT-000
planType: stabilization-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
tags:
  - category-specs
  - plan
  - audit
  - smoke
  - theme-audit-uniformity
---

# Smoke audit and uniformity stabilization

## Objective

Group smoke-frontier, audit, variadic-signature, import hygiene, wrapper, type, and anti-slop compliance work so it supports the foundational plan instead of becoming a disconnected cleanup backlog.

## Source corpus

- `plans/LATTICE_STYLE_GUIDE.md`
- `plans/lattice_redesign_corrections_spec.md`
- `/home/dzack/ai/quality-control/vulture_whitelist.py`
- Existing smoke and variadic sprint plans under `.agents/plans/`.
- Existing implementation cards under `.agents/tasks/implementation/`.

## Priority rule

Audit work is critical when it prevents downstream poisoning: wrong definitions, wrong method ownership, stale docs, broad variadic surfaces, fake wrappers, or public APIs that make future work implement the wrong mathematics. Routine formatting and presentation cleanup is not critical.

## Acceptance Criteria

- [ ] Smoke failures are routed to spec, implementation, research, or decision cards by mathematical cause.
- [ ] Audit cards link to the plan or source map whose correctness they protect.
- [ ] `/home/dzack/ai/quality-control/vulture_whitelist.py` remains global QC tooling support, not a planning document.
- [ ] Compliance findings are not buried in chat or loose TODO files.
