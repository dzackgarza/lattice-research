# Current Goal Handoff

This is the rolling IWE-visible pickup note for the active goal. It is a routing aid, not a tracker. Cards and plans remain authoritative for status, dependencies, source grounding, and acceptance.

## Current phase

Category-spec and semantic-vocabulary. `.agents/current-goal-phase.md`, `GOAL.md`, `plans/card-progress-report.md` for phase surface and card rollup.

## Recent decision delta

- STATUS.md retired. `needs-human-input` reserved for genuine human judgment only.
- 3 cards passed 6-gate review → complete: tensor placeholder fixes, algebra constructor boundary, varieties integration.
- FEATURE-GEOMETRY-CATEGORY-INTERFACES promoted → complete.
- Both plans decomposed into atomic tasks (see Next pickup).

## Next pickup

9 atomic tasks ready for execution, all `unstarted`:

PLAN-STATIC-CATEGORY-REFINEMENT-ORDER (5 tasks):
- TASK-AUDIT-RINGS — grep rings/ for super_categories(, write inventory into plan body
- TASK-AUDIT-SETS-MODULES — grep sets/ + modules/, write inventory
- TASK-AUDIT-REMAINING — grep 8 remaining subtrees, write inventory
- TASK-FILL-TABLE — depends on all 3 audits. Fill admitted-edges table from inventories, add source citations, fix PartitionedSets contradiction
- TASK-FIX-PLAN-HYGIENE — remove dead source ref, deduplicate criteria, clarify scope, declare soft dep

PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION (4 tasks):
- TASK-FIX-DEAD-LINKS — remove 2 dead source paths, replace 2 vague refs
- TASK-FIX-PHASE-INVENTORY — remove variadic phase from body subplans (it lives under sibling plan)
- TASK-FIX-SCOPE — narrow description to match actual phase inventory
- TASK-FIX-CIRCULAR-DEP — remove self-reference from wrapup task dependsOn

## Non-goals

- Coble specs (SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION, SPEC-COBLE-LIFTING-THEOREM-VERIFICATION) remain `unstarted` — downstream phase, correct per DAG.
- Lattice roadmap (PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP) remains `approved-and-unstarted` — gated behind spec→implementation phase transition.

## Validation state

`just plan-validate` reports 63 pre-existing schema violations (spec cards with unexpected fields, missing dependsOn refs). Not blocking current work.
