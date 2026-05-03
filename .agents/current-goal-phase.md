# Current Goal Phase

Current phase: category-spec and semantic-vocabulary phase.

This file is the repo-local phase marker for the staged plan in `GOAL.md`. Agents use
it to avoid drifting into downstream work before the prerequisite mathematical language
exists.

The operative staged-program plan is
`.agents/plans/phase-00-overall-program/pln-research-staged-program.md`.

## Active phase

The repo is currently in the spec phase.

Current phase plan:

- `.agents/plans/phase-01-category-specs/pln-phase-01-category-specs.md`

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

When a phase transition is proposed, QC becomes mandatory for the affected committed
implementation surface. Passing QC is evidence for moving between phases; it is not a
substitute for mathematical review.

## Auto-fix policy

Auto-fixes produced by hooks, formatters, linters, or other tooling are carried forward.
Do not roll them back, undo them, or "restore" pre-fix formatting. If auto-fixes touch
unexpected files, report the tool and paths and let the user decide the follow-up.
