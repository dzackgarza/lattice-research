# Current Goal Phase

Current phase: category-spec and semantic-vocabulary phase.

This file is the repo-local phase marker for the staged plan in `GOAL.md`. Agents use
it to avoid drifting into downstream work before the prerequisite mathematical language
exists.

The operative staged-program source is `GOAL.md`. Do not mirror the staged program as a
tracker feature; active tracker cards start at concrete deliverable features under
`plans/features/`.

## Active phase

The repo is currently in the spec phase.

Current phase plan:

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-PROGRAM/PLAN-CATEGORY-SPEC-PROGRAM.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PLAN-CATEGORY-FOUNDATION-KERNEL.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION.md`
- `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`

Primary work:

- Create and audit category specs extending Sage's category layer.
- Establish uniform semantic vocabulary for sets, modules, Hom/End/Aut objects, modules
  with forms, lattices, and later scheme/variety interfaces.
- Research Sage and open-source backend capabilities needed to support those specs.
- Create plans and cards for implementation gaps discovered during spec work.
- Preserve mathematical intent in docs that can be reviewed by mathematicians.

Blocked by default:

- Downstream Coble experimental research.
- Ad hoc lattice, matrix, polynomial, orbit, or group computations.
- Attempts to prove Coble claims before the lattice/category vocabulary exists.
- QC-driven code cleanup unrelated to an approved phase transition or implementation card.
- Rolling back formatter, linter, or hook auto-fixes.

These defaults block only attempts to do that downstream or unrelated work. They do not
block phase-01 spec execution, source mining, audit drafting, decision capture, or
decomposition under approved phase-01 plans.

## Phase dependency

Each stage in `GOAL.md` blocks the next. It is pointless to attempt Coble research before
there is a lattice spec capable of semantically expressing objects such as
`Pic(S)`, lattice isometry types, discriminant forms, Hom spaces, and pullback/pushforward
maps.

Raw computations do not satisfy the project goal. A 21-by-21 matrix calculation that is
not expressed through reviewed mathematical objects, typed morphisms, vetted algorithms,
and source-backed semantics is not a result for this project. It is exploratory scratch
at best and should not be promoted as evidence.

## QC gate policy

QC is a gate for phase transitions and commit-integrated implementation work. It exists
so quality debt cannot be forgotten indefinitely.

QC is not the controlling activity during churn-heavy spec work. Specs undergo human/LLM
planning, audit, review, and rewrite before settling. During the spec phase, agents
should not chase incidental QC failures or hook noise unless the user explicitly asks
for QC work or the repo is being prepared for a phase transition.

If QC, implementation validation, or a downstream research guard fails during ordinary
spec work, record the finding in the appropriate card/TODO/decision only when durable
tracking is needed, then continue another approved active spec leaf.

When a phase transition is proposed, QC becomes mandatory for the affected committed
implementation surface. Passing QC is evidence for moving between phases; it is not a
substitute for mathematical review.

## Auto-fix policy

Auto-fixes produced by hooks, formatters, linters, or other tooling are carried forward.
Do not roll them back, undo them, or "restore" pre-fix formatting. If auto-fixes touch
unexpected files, report the tool and paths and let the user decide the follow-up.
