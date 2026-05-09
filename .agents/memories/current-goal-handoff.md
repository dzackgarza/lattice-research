# Current Goal Handoff

This is the rolling IWE-visible pickup note for the active goal. It is a routing aid, not a tracker. Cards and plans remain authoritative for status, dependencies, source grounding, and acceptance.

## Current phase

The active phase is category-spec and semantic-vocabulary work. Use `.agents/current-goal-phase.md`, `GOAL.md`, and `plans/card-progress-report.md` for the current phase surface and card rollup.

## Recent decision delta

`STATUS.md` was retired because it framed routine cleanup, source-forced facts, and downstream dependency order as human decisions. The current policy is:

- `needs-human-input` is only for genuine human judgment after source review, mathematical grounding, repo policy, and declared `dependsOn` edges have been checked.
- A phase gate means a literal dependency path declared in cards; unmet dependencies keep downstream cards `unstarted`.
- IWE is the repo markdown query and resume layer. Use it to locate memories, plans, cards, specs, and recent handoff context before scanning broadly.

Former `STATUS.md` items were normalized as follows:

- Tensor-component placeholder/type-leak cleanup, algebra constructor boundary, and varieties category integration are agent-reviewable work, not open human decisions.
- Static category refinement order and smoke/audit stabilization are agent-owned plan remediation.
- Coble isotropic orbit enumeration and lifting theorem verification are downstream `unstarted` work with explicit dependencies; do not pull them forward without a declared dependency update or explicit human override.

## Next pickup

Resume with agent-owned review/remediation on the category-spec phase cards, especially:

- `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER`
- `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`
- `TASK-1777748120751-VP7D5V-FIX-TENSOR-COMPONENT-PLACEHOLDER-METHODS-AND-TYPE-LEAKS`
- `TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS`
- `TASK-INTEGRATE-VARIETIES-CATEGORY`

Before executing a card, inspect its declared `dependsOn` edges and current frontmatter status. Do not infer blockers from phase prose if the dependency is missing; repair the card dependency instead.

## Validation state

`just plan-validate` passed after this reclassification and IWE/Hermes memory reorganization, validating 251 root planning cards.

## Handoff discipline

Update this note by replacement only when the resumption path changes. Do not append a session log or duplicate tracker state here.
