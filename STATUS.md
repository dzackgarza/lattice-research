# Research Repo Status

Current phase: category-spec and semantic-vocabulary
Source: GOAL.md via .agents/current-goal-phase.md

## DAG summary: 221/251 cards complete (88%)

| Status | Count | Meaning |
|--------|-------|---------|
| complete | 221 | Done, ACs satisfied |
| decided | 18 | Decisions recorded, non-executable |
| needs-human-input | 7 | Blocked on human mathematical decision |
| in-progress | 4 | Feature-level coords, blocked by needs-human-input children |
| approved-and-unstarted | 1 | Lattice roadmap, blocked by spec phase |

## Needs human input (7)

### FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES (4)
- plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/tasks/TASK-1777748120751-VP7D5V-FIX-TENSOR-COMPONENT-PLACEHOLDER-METHODS-AND-TYPE-LEAKS.md
  Fix tensor-component placeholder methods and type leaks. Implementation done, Gate 1 rework completed. Needs human signoff on abstract lift_from_product approach.
- plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/tasks/TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS.md
  Move nontrivial algebra construction out of category constructors. Current surface already compliant per analysis. Needs human verification.
- plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER.md
  Plan for static category refinement order. Needs human approval before decomposition.
- plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION.md
  Plan for smoke audit uniformity stabilization. Needs human approval before decomposition.

### FEATURE-GEOMETRY-CATEGORY-INTERFACES (1)
- plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-VARIETIES-CATEGORY.md
  Research category integration for varieties. Depends on Schemes category integration. Needs human decision on variety category surface.

### FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION (2)
- plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/specs/SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION.md
  Spec for isotropic orbit enumeration. Needs human mathematical decision.
- plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/specs/SPEC-COBLE-LIFTING-THEOREM-VERIFICATION.md
  Spec for Coble lifting theorem verification. Needs human mathematical decision.

## In-progress features (4)

These are feature-level coordination cards that remain in-progress only because they have needs-human-input children. No agent-executable work remains in any of them.

- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION (2 needs-human-input + 1 decided)
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES (1 approved-and-unstarted, blocked by spec phase)
- FEATURE-GEOMETRY-CATEGORY-INTERFACES (1 needs-human-input)
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES (4 needs-human-input + 16 decided)

## Blocked by spec phase (1)

- plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP.md
  Lattice/ModulesWithForms implementation roadmap. Correctly blocked: implementation cannot start until category-spec vocabulary is settled. Phase 0 (Sage patches) was premature during spec phase.

## Next steps for human

1. Review the 7 needs-human-input cards. For the 2 tensor/algebra tasks, verify the implementation analysis and sign off. For the 4 plan-level cards, approve decomposition or provide direction.
2. Once all needs-human-input are resolved, the 4 in-progress feature cards will cascade to complete (all their children will be done).
3. After spec phase is complete (FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES and FEATURE-GEOMETRY-CATEGORY-INTERFACES are complete), the lattice roadmap can be unblocked and phase-transition criteria in GOAL.md can be evaluated.

Last updated: 2026-05-08 (commit 736a045 on dzack/reviews-bugfixes-and-phase-completion-2026-05-07)
