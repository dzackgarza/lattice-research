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
  - Leave `TASK-AUDIT-MODULES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
    for human approval if it is still `needs-human-input`; autonomous work
    should continue with:
  - Leave `TASK-AUDIT-SETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
    for human approval if it is still `needs-human-input`; autonomous work
    should continue with:
  - `TASK-AUDIT-RINGS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
    Leave it and `TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING`
    for human approval if they are still `needs-human-input`; autonomous work should
    continue with ALGEBRAS.
  - `TASK-AUDIT-ALGEBRAS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
    Leave it for human approval if it is still `needs-human-input`; autonomous work
    should continue with POSETS.
  - `TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`
    Leave it for human approval if it is still `needs-human-input`; autonomous work
    should continue with TOPOLOGICAL-SPACES. Treat
    `TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION` as
    downstream of the POSETS audit, not the next frontier leaf.
  - Leave `TASK-AUDIT-TOPOLOGICAL-SPACES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES` for human approval if it is still `needs-human-input`; autonomous work should continue with CAT.
  - Leave `TASK-AUDIT-CAT-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES` for human approval if it is still `needs-human-input`; autonomous work should continue with LATTICES.
  - Leave `TASK-AUDIT-LATTICES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES` for human approval if it is still `needs-human-input`; autonomous work should continue with:
- Leave `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME` for human
  approval if it is still `needs-human-input`. Rerun runtime MRO after the Sage
  `ImportError: cannot import name Category` gap is resolved, and do not run full
  `just test` while parallel mypy-plugin work makes that recipe non-diagnostic for
  this leaf.
- The affected Hom/End/Aut and source-map wrappers should only need routing review
  unless human approval changes a child status. Do not start
  `TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION` until
  `TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES` leaves the human
  gate; while the Posets audit remains `needs-human-input`, that source-grounding card
  is ordinary DAG-gated `unstarted` work, not the next autonomous leaf.
- If the audit/generic cards above still need human input and the Posets
  source-grounding card is still dependency-gated, this handoff frontier has no
  autonomous leaf remaining. Do not substitute QC/plugin work or downstream
  ModulesWithForms/lattice implementation unless a new user directive changes the
  frontier.

## Current Human Decisions Needed

- Decide whether to approve or send back each `needs-human-input` per-subtree homset
  mirroring audit: MODULES, SETS, RINGS, ALGEBRAS, POSETS, TOPOLOGICAL-SPACES, CAT,
  and LATTICES.
- Decide whether to approve or send back
  `TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING`.
- Decide whether to approve or send back
  `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME`, accepting that the
  current evidence is source/doc/review based and runtime MRO validation must wait
  until the Sage `ImportError: cannot import name Category` gap is resolved.
- Decide the Posets branch next step after the Posets audit review. If approved,
  `TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION` becomes the
  next autonomous source-grounding leaf; if not approved, follow the review feedback on
  the Posets audit first.
- Decide whether the Sage runtime import gap should be repaired now as environment/QC
  work or left gated until the active plugin lane reaches this repo frontier.
- Decide whether to redirect into QC/plugin work. Without that direction, keep treating
  `/home/dzack/sage-mypy-plugin` as occupied parallel work and do not use full
  `just test` as evidence for this handoff frontier.

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
