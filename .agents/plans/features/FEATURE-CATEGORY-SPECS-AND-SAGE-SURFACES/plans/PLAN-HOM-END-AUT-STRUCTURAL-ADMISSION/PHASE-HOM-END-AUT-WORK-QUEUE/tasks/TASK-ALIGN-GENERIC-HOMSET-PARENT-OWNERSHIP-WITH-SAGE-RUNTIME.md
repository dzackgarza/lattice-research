---
id: TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME
trackerStatus:
  type: task
parents:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
title: Rewrite generic homset ownership for project HomCategory mirroring
status: unstarted
priority: critical
description: Rewrite the generic Hom/End/Aut owner story around project
  HomCategory mirroring rather than Sage generic homset inheritance, then update
  QC/visual/spec surfaces to match that semantic-base decision.
activityType: implementation
workstreamRole: implementation
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- "`category_specs/homsets/*` uses a source-grounded generic owner map consistent with `DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION`."
- Generic hom-layer `@override` annotations remain only where the runtime owner chain
  makes them real overrides.
- "`SPEC-MAPPING-HOMSETS.md`, `plans/visuals/homsets-category-hierarchy.md`, and the relevant homsets docstrings/comments record the corrected owner split."
- "`FEATURE-QC-WARNINGS-ZERO.md` no longer treats the generic Hom/End/Aut residuals as uniformly plugin false positives."
- Relevant Hom/End/Aut QC evidence is rerun and the exact remaining plugin-vs-spec
  failures are recorded in the card body or a linked review artifact.
complexity: 74
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
- PHASE-HOM-END-AUT-WORK-QUEUE
---
# Rewrite generic homset ownership for project HomCategory mirroring

## Summary

The project does not semantically inherit Sage's generic homset construction. This
task rewrites the generic Hom/End/Aut ownership docs and QC framing so
`HomCategoryConstruction` is the semantic base and Sage generic homset behavior is
treated as source inventory/backing behavior to mirror explicitly where desired.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-HOMSETS.md`
- `category_specs/homsets/homsets.py`
- `category_specs/homsets/endsets.py`
- `category_specs/homsets/autsets.py`
- `category_specs/homsets/__init__.py`
- `plans/visuals/homsets-category-hierarchy.md`
- `plans/features/FEATURE-QC-WARNINGS-ZERO/FEATURE-QC-WARNINGS-ZERO.md`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homsets.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/homset.py`

## Context

The follow-up no longer tries to make the project generic hom layer inherit or
bridge Sage's generic `Homset` owner chain. The new ruling is:

- project `HomCategoryConstruction` is the semantic owner of generic Hom/End/Aut;
- Sage generic homset/container behavior is thin inventory/backing behavior;
- subtree mapping specs, not generic runtime inheritance, must explicitly capture
  any Sage homset/container methods that remain part of the project surface.

That still leaves a QC consequence:

- generic hom-layer `@override` claims must not be justified by supposed Sage
  inheritance that the project no longer claims as semantic ownership;
- remaining plugin follow-up is confined to cases where there is real runtime
  inheritance inside the project-owned category chain.

## Acceptance Criteria

- [ ] `SPEC-MAPPING-HOMSETS.md` states that project Hom/End/Aut are redefined and
      mirrored through `HomCategoryConstruction` rather than inherited from Sage
      generic homsets.
- [ ] `plans/visuals/homsets-category-hierarchy.md` and any directly affected
      homsets docstrings/comments reflect the project-owned semantic base.
- [ ] `FEATURE-QC-WARNINGS-ZERO.md` no longer frames the generic hom-layer residuals
      as a Sage inheritance repair.
- [ ] The card body points the subtree method-coverage work to the reopened mapping
      audit tasks instead of collapsing it into this generic card.

## Dependencies And Boundaries

- Do not turn this generic card into the cross-subtree audit itself.
- Do not treat backend reuse of Sage container classes as evidence that the project
  semantically inherits generic homsets.
- Keep subtree method-surface coverage in the mapping-audit phase tasks.

## Complexity And Ownership

- Owner/role: category-spec ownership/documentation follow-up under the Hom/End/Aut plan.
- Complexity: 58/100 (moderate).
- Why this score: the decision is now made and this card is limited to the generic
  owner story, visual/doc wording, and QC framing. The subtree mapping audits are
  split out separately.
- Item-specific evidence:
  - installed Sage source and `SPEC-MAPPING-HOMSETS.md` already ground the intended
    owner map;
  - the affected implementation and documentation surface is concentrated in the
    generic hom/end/aut files plus one visual and one QC tracker file;
  - validation must recheck runtime MRO truth and the Hom/End/Aut QC slice, not just
    syntax.

## Work Log

- 2026-05-10: Created after repo QC follow-up showed a source-grounded owner mismatch
  between `SPEC-MAPPING-HOMSETS.md` and the current generic `HomCategory` runtime MRO.
- 2026-05-10: Reframed after user direction: the repo redefines/mirrors Sage homset
  behavior through `HomCategoryConstruction`; subtree method coverage moved to
  dedicated mapping-audit tasks.
