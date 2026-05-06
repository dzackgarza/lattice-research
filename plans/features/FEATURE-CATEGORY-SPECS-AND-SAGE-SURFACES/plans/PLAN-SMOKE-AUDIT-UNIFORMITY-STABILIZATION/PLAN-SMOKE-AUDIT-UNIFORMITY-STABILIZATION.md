---
id: PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Smoke audit and uniformity stabilization
status: needs-review
priority: critical
owner: Zack
description: Group smoke-frontier, audit, variadic-signature, import hygiene, wrapper,
  type, and anti-slop compliance work so it supports the foundational plan instead
  of becoming a disconnected cleanup backlog.
successCriteria:
- Smoke failures are routed to spec, implementation, research, or decision cards by
  mathematical cause.
- Audit cards link to the plan or source map whose correctness they protect.
- Audit coverage includes duck-typed object-shape probes where category-spec code
  should match real Sage/project types, documented wrappers, or category membership.
- '`/home/dzack/ai/quality-control/vulture_whitelist.py` remains global QC tooling
  support, not a planning document.'
- Compliance findings are not buried in chat or loose TODO files.
phases:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Smoke audit and uniformity stabilization

## Objective

Group smoke-frontier, audit, variadic-signature, import hygiene, wrapper, type, and anti-slop compliance work so it supports the foundational plan instead of becoming a disconnected cleanup backlog.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Source corpus

- `plans/LATTICE_STYLE_GUIDE.md`
- `plans/lattice_redesign_corrections_spec.md`
- `/home/dzack/ai/quality-control/vulture_whitelist.py`
- Existing smoke and variadic sprint plans under `plans/features/`.
- Existing implementation cards under `plans/features/`.

## Priority rule

Audit work is critical when it prevents downstream poisoning: wrong definitions, wrong method ownership, stale docs, broad variadic surfaces, fake wrappers, or public APIs that make future work implement the wrong mathematics. Routine formatting and presentation cleanup is not critical.

## Subplans

- `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT`: variadic signature closure across modules, rings, tensors, algebras, lattices, posets, sets, and RealSet constructors.
- `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT`: object-shape probing audit for `getattr`/`hasattr`
  patterns that should be real type/category dispatch.

Leaf task ownership is encoded by `parents` containment under phase cards; this parent
plan should not own executable cards directly.

## Acceptance Criteria

- [ ] Smoke failures are routed to spec, implementation, research, or decision cards by mathematical cause.
- [ ] Audit cards link to the plan or source map whose correctness they protect.
- [ ] Audit coverage includes duck-typed object-shape probes where category-spec code
  should match real Sage/project types, documented wrappers, or category membership.
- [ ] `/home/dzack/ai/quality-control/vulture_whitelist.py` remains global QC tooling support, not a planning document.
- [ ] Compliance findings are not buried in chat or loose TODO files.
