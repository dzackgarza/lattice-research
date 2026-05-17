# Current Goal Handoff

Purpose: route the next session only. Cards, plans, and git history remain the
authorities for status, evidence, and completed work.

## Start Here

- Active phase: category-spec and semantic-vocabulary.
- Read `.agents/current-goal-phase.md`, then use IWE to inspect the active
  `.agents/plans/` frontier before selecting work.
- Refresh live repository state from git and tracker cards. This note records
  routing constraints, not the authoritative dirty tree or test status.

## Milestone Order

- Finish active category-spec vocabulary first, especially Hom/End/Aut and
  subtree homset mirroring.
- Resolve the QC/mypy gate only at the approved frontier; do not chase plugin
  implementation while parallel plugin work is active.
- Finish ModulesWithForms and lattice vocabulary after category-spec
  dependencies are settled.
- Only then consider categorical implementation, universal categorical
  algorithms, and downstream Coble work.

## Ordered Current Frontier

- `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`
- `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`
- Per-subtree homset mirroring audits:
  - `TASK-AUDIT-MODULES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-SETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-RINGS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-ALGEBRAS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-TOPOLOGICAL-SPACES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-CAT-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
  - `TASK-AUDIT-LATTICES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
- `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME`
- Then wrap or review the affected Hom/End/Aut and source-map plans.

## Collision Boundaries

- Treat `/home/dzack/sage-mypy-plugin` as occupied parallel work unless the user
  explicitly redirects there.
- Do not broad-stage research-repo changes; checkpoint and stage only the file or
  leaf currently being edited.
- Do not add local casts around `_with_axiom`, `category_of`,
  `refine_category`, Hom/End/Aut selectors, callable parent projection,
  method-container aliases, construction selectors, or provider assignment
  specialization unless the executing card proves a source defect.
- Use `with_axiom(...)` for axiom refinement; do not reintroduce direct
  `_with_axiom` calls in touched `SubcategoryMethods`.
- `MorphismMethods` is banned in category specs; morphism behavior belongs on
  the relevant Hom-category `ElementMethods`.
- Do not delete `category_specs/modules/subcategories/constructions/cartesian_products.py`
  overrides for `__init_extra__` or `_lmul_`, and do not replace them with local
  casts. Their checker behavior belongs to plugin/static-model work unless a
  source defect is separately proved.
- Do not replace construction selectors such as
  `TopologicalSpaces().Subobjects()` with local casts merely to satisfy mypy.
- Do not recreate root-level plugin fixtures such as `test_override.py`.

## Plugin-Owned Checker Gaps

- Every mypy class must become either a source fix with evidence or a plugin-spec
  failing reproducer with expected checker behavior.
- P-adic `return self` and field zero-ideal completion `return self` false
  positives are routed through plugin value/transitive method-container fixtures;
  do not rework those paths in research source.
- Construction-category extra-super behavior, especially the CartesianProducts
  `extra_super_categories() == [base_category()]` inheritance shape, is plugin
  model work unless live cards redirect it back into source.

## Gated Work

- QC=0 is required before real implementation enters main.
- QC order is basic typing hygiene, dynamic inheritance plugin review, stubs,
  then downstream cleanup.
- Categorical implementation, universal algorithms, and all Coble features remain
  gated by category specs, QC, ModulesWithForms/lattices, and implementation-layer
  prerequisites.
- Some completed-plan metadata depends on in-progress plans. Use the first
  incomplete dependency frontier from cards, not raw progress percentages, when
  selecting work.

## What Not To Store Here

- Do not store changelogs, commit-by-commit source-fix history, validation logs,
  or stale dirty-tree snapshots in this handoff.
- Preserve durable guardrails and next-session routing only; cards, plans, git,
  and test commands are the live authorities for status and evidence.
