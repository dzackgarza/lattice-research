# Current Goal Phase

Current phase: category-spec and semantic-vocabulary phase.

This file is the repo-local phase marker for the staged plan in `GOAL.md`. Agents use
it to avoid drifting into downstream work before the prerequisite mathematical language
exists.

The operative staged-program source is `GOAL.md`. Do not mirror the staged program as a
tracker feature; active tracker cards start at concrete deliverable features under
`.agents/plans/features/`.

## Active phase

The repo is currently in the spec phase.

Frame the spec phase as an inventory-to-spec translation problem: explore Sage's
existing mathematical surfaces, determine which constructions are feasible with current
exact backends, and admit only bounded source-grounded vocabulary plus explicitly
justified extensions. The phase is not "write the ideal categorical API and later
implement it."

Current phase plan:

- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SPEC-CORE-VERTICAL-SLICE/PLAN-SPEC-CORE-VERTICAL-SLICE.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-PROGRAM/PLAN-CATEGORY-SPEC-PROGRAM.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PLAN-CATEGORY-FOUNDATION-KERNEL.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER/PLAN-STATIC-CATEGORY-REFINEMENT-ORDER.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION/PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`
- `.agents/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`

Primary work:

- Discover Sage surfaces for each mathematical family under consideration: constructors,
  categories, parent/element classes, coercions, canonical maps, methods, return types,
  and documented or runtime-observed limitations.
- Translate mathematical needs to Sage or exact-backend behavior, not to invented API.
  Free modules, formed modules, lattices, discriminant forms, orthogonal complements,
  embeddings, isometries, base change, and stabilizers are admitted only through source
  evidence, named backend support, bounded local construction, or deferred-algorithm
  classification.
- Assign every proposed operation an admission status: Sage-backed, backend-backed,
  bounded local extension, or deferred research algorithm.
- Stratify every operation by feasibility: Level 0 definitional vocabulary, Level 1
  certification/checking, Level 2 finite-data construction, Level 3 bounded or finite
  search, or Level 4 global algorithmic computation.
- Decide category ownership for each admitted operation at the highest mathematically
  valid layer. For example, deterministic enumeration belongs first to countable
  sets/products/free modules before becoming lattice-local bounded-vector search, and
  form-preserving maps belong to modules with forms or lattices rather than arbitrary
  modules.
- Produce specs sufficient for the lattice-theoretic layer only where the operation is
  actually feasible or explicitly deferred: discriminant forms, primitive embeddings,
  orthogonal complements, local invariants, base change, and Nikulin-style criteria.
- Advance by vertical slices:
  mathematical need -> Sage inventory -> admitted vocabulary -> witness object ->
  proof/check/report.
- Execute the approved spec-core vertical slice: typed obligation/provider/witness
  reports for `GF(5)^3`, `ZZ^2`, and a missing-obligation claimant.
- Create and audit category specs extending Sage's category layer.
- Establish uniform semantic vocabulary for sets, modules, Hom/End/Aut objects, modules
  with forms, lattices, and later scheme/variety interfaces without implying generic
  computability of Level 4 operations such as full automorphism groups.
- Research Sage and open-source backend capabilities needed to support those specs.
- Create plans and cards for implementation gaps discovered during spec work.
- Preserve mathematical intent in docs that can be reviewed by mathematicians.
- Treat broad category expansion, global QC cleanup, and broad smoke recovery as
  non-goals unless they directly change the active slice reports.

Blocked by default:

- Downstream Coble experimental research.
- Ad hoc lattice, matrix, polynomial, orbit, or group computations.
- Attempts to prove Coble claims before the lattice/category vocabulary exists.
- Complete redesigns of Sage, full algebraic-geometry library work, arbitrary
  concrete-method catalogs, or general Sage ergonomics unrelated to the Coble/K3
  lattice pipeline.
- Abstract ontology expansion or generic API surfaces admitted only because the
  mathematical name exists.
- Generic `Aut(L)`, full automorphism-group, stabilizer, orbit-decomposition, Vinberg
  chamber, Coxeter-parabolic, or hyperbolic-lattice group computation unless the
  surface is restricted by hypotheses and has a named Sage/backend/algorithmic owner.
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

The practical success condition for this phase is source-grounded sufficiency for the
research pipeline: an implementation agent can build the category/spec layer without
inventing the mathematics or implying unavailable algorithms, because the objects,
morphisms, ownership boundaries, feasibility levels, required invariants, Sage bridge
points, backend witnesses, and known gaps are already stated at the mathematical level.

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
