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
- The approved `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]` pivot gate is complete.
- `main` now contains the source-truth follow-through milestones from
  `dzack/spec-core-source-truth-lanes`; do not restart that branch.
- `main` now includes the constructor-provenance source-truth milestone: every
  admitted `Constructors()` collector is queryable through spec-core provenance and
  `category_specs/spec_core/README.md` documents the extension query workflow. The
  generic adapter now derives per-method target routes from constructor return
  annotations unless explicit metadata overrides them.
- Use `just next-tasks 10` before selecting the next leaf; do not restart the completed
  vertical-slice branch sequence.
- Use IWE to retrieve the selected card before reading broad plan history.

## Milestone Order

- The spec-core vertical slice has focused validation: `GF(5)^3` reports finite
  cartesian-power cardinality `125`; `ZZ^2` reports countable cartesian-power
  provenance and the product/countable-set enumeration obligation.
- Constructor provenance coverage is now the active source-truth lane: all admitted
  collectors should expose `.provenance()`, including empty `TopologicalSpaces` and
  `Lattices` registries, deferred q-adic extension precision-cap records, and no
  owner-only target routes for non-empty registries.
- Resume Hom/End/Aut human-gated cards only if the user explicitly returns to that
  lane.
- Resolve the QC/mypy gate only at the approved frontier; do not chase plugin
  implementation while parallel plugin work is active.
- Finish ModulesWithForms and lattice vocabulary after the slice and category-spec
  dependencies are settled.
- Only then consider categorical implementation, universal categorical algorithms, and
  downstream Coble work.

## Current Frontier

- `main` is ahead of `origin/main` with the integrated source-truth work: report query
  helpers, reusable free-module witness helpers, `Spec.of` inspection, constructor
  provenance models/adapters, category-spec obligation closure, generated-law tests,
  and an expanded `just test-spec-core-vertical-slice` target.
- Do not open a PR unless the user explicitly asks. Continue substantial new
  source-truth work on a clean branch if it needs multiple commits; otherwise keep
  small integration edits on `main` with focused commits.
- `TASK-MYPY-PARSER` has passed fresh-context agent review for the invariant-core
  manifest source-module coverage pivot and is now human-gated. Continue the Sage
  mypy-plugin lane only through `just next-tasks`; the next executable leaf should be
  the next phase-one review card, not the obsolete parser surface.
- `/home/dzack/sage-mypy-plugin` has committed plugin evidence at `bd656d2`
  (`just test -q`: `73 passed`) and the plugin worktree is clean. Treat later
  uncommitted plugin changes as occupied parallel work unless the selected card
  explicitly owns them.
- Do not treat broad smoke failures, q-adic constructor gaps, Hom runtime human gates,
  or mypy-plugin work as blockers for the spec-core slice unless the selected slice
  task proves a direct dependency.
- Do not run `just test` as evidence for the slice while parallel mypy-plugin work
  makes the result non-diagnostic. Use focused checks that answer the selected leaf's
  question.

## Human Gates

Do not present the existing `needs-human-input` frontier as human decisions merely
because clean reviews await closure. Root policy now treats that as workflow debt:
source-forced facts, policy-forced routing, DAG order, and clean agent reviews are
agent work, not human input.

Next pickup should audit the current `needs-human-input` cards and reclassify any card
whose only question is "approve this reviewed work as complete." A card should remain
`needs-human-input` only if its body records a specific human-only decision that source
review, mathematical grounding, repo policy, and the DAG cannot answer.

The Hom/End/Aut cards should not be reopened as design questions if they merely apply
the existing owner policy: generic Hom/End/Aut containers route through the project
Hom-category framework, while concrete object-family behavior stays with the relevant
Sage-backed category, subcategory, or method owner.

## Validation Routing

- The slice success metric is the focused spec report plus generated-law and
  constructor-provenance checks, not broad category-smoke recovery. Use
  `just test-spec-core-vertical-slice` for the focused validation target.
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
