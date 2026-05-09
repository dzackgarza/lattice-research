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

Start here. Execute in this order:

### Phase 1 — smoke plan fixes (4 tasks, all independent, dispatch in parallel)
Path: plans/features/.../PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/tasks/
- TASK-FIX-DEAD-LINKS — one edit to plan body: remove 2 dead source paths, replace 2 vague refs
- TASK-FIX-PHASE-INVENTORY — one edit: remove variadic phase from body subplans
- TASK-FIX-SCOPE — one edit: narrow description to match actual phase inventory
- TASK-FIX-CIRCULAR-DEP — one edit to wrapup task: remove self-reference from dependsOn

### Phase 2 — static refinement audits (3 tasks, independent, dispatch in parallel)
Path: plans/features/.../PLAN-STATIC-CATEGORY-REFINEMENT-ORDER/tasks/
- TASK-AUDIT-RINGS — grep category_specs/rings/ for super_categories(, write inventory into plan body
- TASK-AUDIT-SETS-MODULES — grep sets/ + modules/, write inventory
- TASK-AUDIT-REMAINING — grep 8 remaining subtrees, write inventory

### Phase 3 — static refinement fill (1 task, depends on all 3 audits)
- TASK-FILL-TABLE — read the 3 inventory sections now in the plan body, fill the admitted-edges table, add source citations, fix PartitionedSets contradiction

### Phase 4 — static refinement hygiene (1 task, independent)
- TASK-FIX-PLAN-HYGIENE — remove dead source ref, deduplicate criteria, clarify scope, declare soft dep

After all 9 tasks complete: both plans cascade to complete → FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES → complete. Phase is done.

## Non-goals

- Coble specs (SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION, SPEC-COBLE-LIFTING-THEOREM-VERIFICATION) remain `unstarted` — downstream phase, correct per DAG.
- Lattice roadmap (PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP) remains `approved-and-unstarted` — gated behind spec→implementation phase transition.

## Validation state

`just plan-validate` reports 63 pre-existing schema violations (spec cards with unexpected fields, missing dependsOn refs). Not blocking current work.
