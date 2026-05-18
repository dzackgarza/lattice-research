---
title: Current Goal Handoff
referencedBy:
- key: index
  title: Agent Memories
---

# Current Goal Handoff

Purpose: route the next session only. Cards, plans, and git history remain the
authorities for status, evidence, dependencies, and completed work.

## Start Here

- Active phase: category-spec and semantic-vocabulary.
- Read `.agents/current-goal-phase.md`, then inspect the active `.agents/plans/`
  frontier with IWE before selecting work.
- Use the earliest incomplete dependency frontier. Do not rank or select downstream
  work whose incoming `dependsOn` paths are incomplete.

## Milestone Order

- Finish active category-spec vocabulary first, especially Hom/End/Aut and subtree
  homset mirroring.
- Resolve the QC/mypy gate only at the approved frontier; do not chase plugin
  implementation while parallel plugin work is active.
- Finish ModulesWithForms and lattice vocabulary after category-spec dependencies are
  settled.
- Only then consider categorical implementation, universal categorical algorithms, and
  downstream Coble work.

## Current Frontier

- No autonomous leaf remains in the scoped handoff frontier after fresh-context review
  of `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME`.
- That Hom runtime card is now `needs-human-input`; ask the human to approve it or
  send it back.
- The prior Sage `Category` import blocker is not a blocker for this card. Focused
  validation now reaches the Hom runtime path; the remaining full category-smoke
  failure is the separately tracked q-adic split lattice-cap constructor gap.
- Do not run `just test` as evidence while parallel mypy-plugin work makes the result
  non-diagnostic. Use focused checks that answer the selected leaf's question.

## Human Gates

- `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME` is currently
  human-gated after clean fresh-context review.
- The per-subtree homset mirroring audits are currently human-gated:
  `MODULES`, `SETS`, `RINGS`, `ALGEBRAS`, `POSETS`, `TOPOLOGICAL-SPACES`, `CAT`, and
  `LATTICES`.
- `TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING` is also
  human-gated.
- `TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION` is
  `unstarted` and DAG-gated by the POSETS audit, not blocked.

## Validation Routing

- Treat the q-adic split lattice-cap constructor failure as already routed through
  `TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED`
  and its linked Sage-support research card. Do not invent a local q-adic
  implementation to make aggregate smoke pass.
- Before advancing any category-spec card, run the spec-weakening review over staged
  and unstaged diffs: no deleted obligations, narrowed smokes, or moved surfaces
  without a source-grounded replacement owner.
- Keep review findings in the relevant card or review artifact. Keep this handoff as
  routing guidance only.

## Collision Boundaries

- Treat `/home/dzack/sage-mypy-plugin` as occupied parallel work unless the user
  explicitly redirects there.
- Do not broad-stage research-repo changes; checkpoint and stage only the file or leaf
  currently being edited.
- Do not add local casts around `_with_axiom`, `category_of`, `refine_category`,
  Hom/End/Aut selectors, callable parent projection, method-container aliases,
  construction selectors, or provider assignment specialization unless the executing
  card proves a source defect.
- Use `with_axiom(...)` for axiom refinement; do not reintroduce direct `_with_axiom`
  calls in touched `SubcategoryMethods`.
- `MorphismMethods` is banned in category specs; morphism behavior belongs on the
  relevant Hom-category `ElementMethods`.
- Do not delete
  `category_specs/modules/subcategories/constructions/cartesian_products.py` overrides
  for `__init_extra__` or `_lmul_`, and do not replace them with local casts. Their
  checker behavior belongs to plugin/static-model work unless a source defect is
  separately proved.
- Do not replace construction selectors such as `TopologicalSpaces().Subobjects()`
  with local casts merely to satisfy mypy.
- Do not recreate root-level plugin fixtures such as `test_override.py`.

## Gated Work

- QC=0 is required before real implementation enters main.
- QC order is basic typing hygiene, dynamic inheritance plugin review, stubs, then
  downstream cleanup.
- Categorical implementation, universal algorithms, and all Coble features remain
  gated by category specs, QC, ModulesWithForms/lattices, and implementation-layer
  prerequisites.
