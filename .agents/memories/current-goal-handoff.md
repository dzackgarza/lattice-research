# Current Goal Handoff

This is the rolling IWE-visible pickup note for the active goal. It is a routing aid, not a tracker. Cards and plans remain authoritative for status, dependencies, source grounding, and acceptance.

## Current phase

Category-spec and semantic-vocabulary phase remains the active phase marker in `.agents/current-goal-phase.md`. `GOAL.md` is not fully discharged; downstream implementation, universal-algorithm, lattice, geometry, and Coble research features remain unstarted or phase-gated.

## Recent decision delta

- Added concrete GOAL.md coverage feature cards instead of mirroring `GOAL.md` stages mechanically:
  - `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER`
  - `FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS`
  - `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`
- Enforced the semantic-base gate in feature `dependsOn` frontmatter:
  - `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` depends on `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`.
  - `FEATURE-GEOMETRY-CATEGORY-INTERFACES` depends on `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`.
  - `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER` depends on category specs, ModulesWithForms/lattices, and geometry interfaces.
  - `FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS` depends on the categorical implementation layer.
  - `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION` depends on implementation, universal algorithms, ModulesWithForms/lattices, and geometry interfaces.
  - Downstream Coble research features depend on the Coble geometric lattice foundation.
- Reset downstream Coble feature roots from completed/in-progress to `unstarted` where their own acceptance criteria require the missing geometric lattice foundation.
- Wired downstream Coble features through `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`.
- Regenerated `plans/card-progress-report.md`; it shows 263 cards, 250 completed, 95.1% overall progress, 10 active feature trees, and 8 completed feature trees.
- Process repair after user correction: task creation now has a documented hard
  phase-owner preflight in `.agents/skills/task/SKILL.md`,
  `.agents/skills/research-project-workflow/SKILL.md`,
  `.agents/skills/research-project-workflow/references/project-workflow.md`,
  `plans/AGENTS.md`, and `/home/dzack/ai/planning/AGENTS.md`. Plan-level `tasks/`
  directories are explicitly forbidden and treated as skipped phase-gate process
  failures, not ordinary card cleanup.
- Process repair after validator correction: the embedded relaxed Python
  `plan-validate` implementation in `justfile` was removed. `just plan-validate` now
  delegates to `/home/dzack/ai/planning/justfile validate`; centralized validation is
  the only planning pass/fail authority.
- Co-mathematician workflow migration started from Zheng et al. arXiv:2605.06651v1:
  - Added `research-co-mathematician-workflow` skill and architecture reference.
  - Added activity/workstream/uncertainty fields to plan, phase, and task schemas.
  - Added repo-local agent role prompts under `.agents/agent-roles/`.
  - Added living LaTeX working paper scaffold under `paper/` and workstream report
    root under `reports/workstreams/`.
  - Updated workflow, state-machine, orchestration, proof-audit, task, repo-structure,
    and planning docs to treat intake, workstreams, native paper artifacts,
    uncertainty lifecycle, and failed explorations as first-class process surfaces.
  - Normalized tracker schemas for centralized validation by admitting existing spec
    `requirement`/`acceptanceCriteria`, decision metadata, and phase `reviewLog`.
  - Aligned `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` and
    `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` statuses with their already-started
    children so centralized hierarchy validation passes.

## Next pickup

- Audit the moved smoke/static-refinement task cards under their new phase owners and
  finish any provenance/status cleanup only after the phase-gate process repair is
  reviewed.
- Next workflow migration leaf: convert at least one active plan into the new intake +
  workstream + report + paper-anchor pattern, then use that as the concrete exemplar
  before batch-reframing older cards.
- Current phase-local path: continue `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`, especially `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP`; it is now an explicit dependency of the categorical implementation layer.
- Next GOAL coverage planning gap: write specs/plans for `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER` and `FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS` only after the owning layer is approved.
- Coble foundation remains downstream: `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION` must not start until the semantic substrate dependencies are satisfied.

## Non-goals

- Do not claim `GOAL.md` is complete from tracker percentages.
- Do not treat historical recovery feature completion as completion of Coble mathematical verification.
- Do not attack Coble orbit, arithmetic-group, Coxeter, involution, stable-model, or moduli comparison cards until their declared dependencies are satisfied.

## Validation state

- `just plan-validate` passes and regenerated `plans/plan-dag.md`.
- `just plan-progress-report` passes and regenerated `plans/card-progress-report.md`.
- `just paper-build` passes for `paper/main.tex`; generated LaTeX build products are
  ignored by `paper/.gitignore`.
- `git diff --check` and `python -m py_compile .agents/scripts/generate_card_progress_report.py`
  pass.
