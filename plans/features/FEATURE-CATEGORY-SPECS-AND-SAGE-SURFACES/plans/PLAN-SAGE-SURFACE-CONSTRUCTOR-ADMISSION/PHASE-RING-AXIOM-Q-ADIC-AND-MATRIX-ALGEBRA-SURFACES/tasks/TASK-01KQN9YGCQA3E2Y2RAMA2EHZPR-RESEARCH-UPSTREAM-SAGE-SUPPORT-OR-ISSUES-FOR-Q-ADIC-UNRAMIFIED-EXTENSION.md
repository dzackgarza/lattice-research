---
id: TASK-01KQN9YGCQA3E2Y2RAMA2EHZPR-RESEARCH-UPSTREAM-SAGE-SUPPORT-OR-ISSUES-FOR-Q-ADIC-UNRAMIFIED-EXTENSION
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Research upstream Sage support or issues for q-adic unramified extensions with split
  lattice precision caps
status: needs-review
priority: high
description: Rings mapping records constructor namespace decisions, split p-adic and q-adic
  precision routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
  lattice-precision gaps.
successCriteria:
- The research result cites the exact sources searched and separates source evidence from
  inference.
- 'Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence,
  Gaps.'
- Any admitted design consequence is linked to a spec-work or design-decision item rather
  than buried in prose.
- For q-adic precision items, preserve the five-field negative finding format when updating
  evidence.
- For topological ring work, check both ring and topological-space category membership.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Research upstream Sage support or issues for q-adic unramified extensions with split lattice precision caps
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Research upstream Sage support or issues for q-adic unramified extensions with split lattice precision caps from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [x] The research result cites the exact sources searched and separates source evidence from inference.
- [x] Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence, Gaps.
- [x] Any admitted design consequence is linked to a spec-work or design-decision item rather than buried in prose.
- [x] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [x] For topological ring work, check both ring and topological-space category membership.

## Research Result

Source evidence:

- Sage 10.8 p-adics docs for `factory` document `Zq`/`Qq` as unramified q-adic
  constructors with integer precision examples and precision models capped-relative,
  capped-absolute, fixed-modulus, and floating-point; they do not document q-adic
  lattice-cap or lattice-float constructors.
- Sage 10.8 p-adics docs for `padic_base_leaves` document `pAdicRingLattice` and
  `pAdicFieldLattice` as base `Zp`/`Qp` lattice-precision parents whose `prec` is a
  pair `(relative_cap, absolute_cap)`.
- Sage 10.8 p-adics docs for `generic_nodes` document `PrecisionLattice`,
  `precision_cap_relative()`, and `precision_cap_absolute()` for base lattice p-adics.
- Sage `develop` raw `sage/rings/padics/factory.py` imports `pAdicRingLattice` and
  `pAdicFieldLattice`, but its `ext_table` has unramified extension entries only for
  capped-relative, capped-absolute, fixed-modulus, and floating-point bases.
- Sage `develop` raw `factory.py` still coerces `Zq`/`Qq` precision with
  `prec = Integer(prec)` in the q-adic constructor path, while `get_key_base` handles
  pair precision for base `Zp`/`Qp` lattice constructors.
- The stale `sagetrac-mirror` branch for issue `#25915` and draft PR `#34993`
  (`roed314/sage:general-extensions`) were also searched. They add relative/general
  p-adic extension machinery, but the searched `factory.py` branches still do not add
  unramified lattice extension leaves keyed by `pAdicRingLattice` or
  `pAdicFieldLattice`.

Repository and upstream issue evidence:

- Sage issue `#23505` is the closed base p-adic lattice-precision implementation
  ticket. It describes the precision datum as a lattice attached to the parent and
  implemented by `PrecisionLattice`.
- Sage issues `#24809` and `#30692` remain open lattice-precision follow-up/bug
  tickets, which supports treating lattice precision as an experimental/incomplete
  upstream surface even before q-adic extension support.
- Sage issue `#25915` is open and targets unramified extensions of arbitrary p-adic
  fields. Its public body does not claim lattice-precision q-adic support.
- Sage issue `#28466` and draft PR `#34993` are open general p-adic extension work.
  PR `#34993` is draft/needs-work and its searched branch still does not provide the
  q-adic split lattice-cap constructor route needed here.

Negative finding:

- Searched: Sage 10.8 p-adics docs for `factory`, `generic_nodes`, and
  `padic_base_leaves`; Sage `develop` raw source for `factory.py`,
  `padic_extension_leaves.py`, `padic_base_leaves.py`, and `generic_nodes.py`; GitHub
  issue/PR searches for `Zq Qq lattice-cap`, `pAdicLatticeGeneric unramified
  extension`, `lattice precision q-adic`, `pAdicRingLattice pAdicFieldLattice
  extension`, and `PrecisionLattice`; issues `#23505`, `#24809`, `#25915`, `#28466`,
  `#30692`; draft PR `#34993`; the stale `sagetrac-mirror` branch for `#25915`; and
  PR `#34993` branch `roed314/sage:general-extensions`.
- Found: base `Zp`/`Qp` lattice precision is documented and implemented; q-adic
  `Zq`/`Qq` docs and source still route precision as an integer and do not expose
  split lattice-cap q-adic constructors. Public upstream work exists for base lattice
  precision, arbitrary unramified p-adic extensions, and general extensions, but the
  searched issue bodies and branches do not provide a usable unramified q-adic
  extension parent with split relative/absolute lattice precision caps.
- Conclusion: inference -- the existing mapping is still correct: retain
  `ZqWithPrecisionCaps(...)` and `QqWithPrecisionCaps(...)` as admitted but deferred
  frontier names, and make any implementation body report the Sage gap instead of
  passing through to a broken constructor path.
- Confidence: High for public Sage docs, current `develop`, public GitHub issue/PR
  metadata, and the searched public branches.
- Gaps: GitHub issue comments could not be loaded through `gh issue view --comments`
  because GitHub's classic-project GraphQL field failed; private branches and
  non-GitHub developer discussions were not searched.

Design consequence:

- No new decision card is needed. The consequence is already represented by
  `[[TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED]]`
  and by the retained deferred names in `[[SPEC-MAPPING-RINGS]]`.
- This is not topological-ring implementation work. No ring/topological-space category
  membership changed; the topological inheritance rule remains the mapping table row
  for `Zp(...)`, `Qp(...)`, `Zq(...)`, `Qq(...)`, and named split precision routes in
  `[[SPEC-MAPPING-RINGS]]`.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06: Completed upstream Sage docs/source/issue/PR research. Confirmed public
  Sage sources still lack a q-adic unramified extension route with split lattice
  precision caps; preserved the deferred admitted names and linked the implementation
  gap card.
