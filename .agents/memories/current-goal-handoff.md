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

- Active phase: QC/mypy cleanup (gated on plugin PR merge by human).
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
- `TASK-MYPY-PARSER` has passed fresh-context agent review and is now human-gated.
  The plugin rewrite completed all phases 0–9 (2026-05-19 through 2026-05-20).
  Current plugin HEAD is `2effacf` on `rewrite/invariant-core` (PR open:
  `rewrite/invariant-core → main`). `just test -q`: `187 passed` (7 suites) as of
  2026-05-20. All Phase 7 E1–E6 cache lifecycle tests pass. All Gemini HIGH/MEDIUM
  review comments addressed. Kilo review on `0a49db1` confirmed clean (4 warnings all
  resolved). `2effacf` adds docstring-only docs update; Kilo confirmed "No New Issues
  Found | Recommendation: Merge" on `2effacf`. Plugin parallel work is no longer active;
  QC gate is unblocked. Remaining blocker: human merge of `rewrite/invariant-core → main`
  PR.
- Tracker cleanup 2026-05-21 (commit `a0d5683e`): All 12 tasks and 3 phases in
  `PLAN-MYPY-PLUGIN-IMPLEMENTATION` reclassified from `needs-agent-review`/`needs-human-input`
  to `complete`. `TASK-MYPY-PARSER` current-status updated to record policy resolution.
  `PLAN-MYPY-PLUGIN-IMPLEMENTATION` plan card advanced to `complete`. All task evidence:
  - PHASE-SAGE-SIDE-API: TASK-MYPY-PARSER (current-status updated + complete),
    TASK-MYPY-INSTANTIATE, TASK-MYPY-DIRECT-BASES, TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION
  - PHASE-MYPY-SIDE-HARNESS: TASK-MYPY-PLUGIN-CLASS, TASK-MYPY-HOOK-CALLBACK,
    TASK-MYPY-DEPS-DIAGNOSTICS, TASK-MYPY-NAMESPACE-AGNOSTIC-HOOK-MATCHING
  - PHASE-TEST-VERIFICATION: TASK-MYPY-TEST-ARTIFICIAL, TASK-MYPY-TEST-MYPY-INTEGRATION,
    TASK-MYPY-TEST-DEBUG-ORACLE, TASK-MYPY-TEST-THIRD-PARTY-SUBTREES
  `just next-tasks 10` returns "No outstanding DAG-ready tasks found" — everything is
  gated on the human plugin PR merge.
- Research repo fixes 2026-05-21: sage.all initialization added to
  `test_spec_core_constructor_specs.py` (commit `c3197f6b`) — test was passing only
  when run after other tests that imported sage.all first; now passes in isolation.
  QC justfile heredoc bug fixed in `dzackgarza/ai` (commit `4cf232c`) — `just test`
  now runs correctly in research repo (confirmed: 401 passthrough mypy errors, 34/52
  category_specs tests pass in full suite; vertical slice 29/29 still passes).
- Research repo fix 2026-05-21: `_prime_method_cache_before_refinement` added to
  `category_specs/utils.py` (commit `50769a06`). Root cause: for Cython extension
  types (ZZ, QQ, etc.), `_refine_category_` updates `_category` without replacing
  `__class__` or clearing `_cached_methods`. When the incoming categories include
  category_specs `ParentMethods` stubs (e.g. `_RingObjectMethods.ideal_monoid` at
  MRO position 20 vs `Rngs.ParentMethods.ideal_monoid` at position 24), the first
  uncached `__getattr__` lookup after refinement caches the stub (returning None)
  instead of Sage's real implementation. The fix pre-populates `_cached_methods` from
  the current (pre-refinement) `_category` for all method names defined in project-
  owned stubs within the incoming categories, so subsequent lookups hit the primed
  cache regardless of MRO order. Full suite now 40/52 (up from 34/52); vertical slice
  29/29; remaining 12 failures are known test_spec_smoke gated on plugin PR merge.
- `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY` work log updated 2026-05-20 with the
  TypeAlias fix milestone (commit `a5e1ecbe`): 735 `[valid-type]` errors eliminated
  by adding `TypeAlias` annotations across `types.py` and six category `__init__.py`
  files. Additional hygiene fixes 2026-05-20: `[no-untyped-def]` in
  `test_free_module_witnesses.py` (commit `6e1ba481`), `[assignment]` in
  `test_spec_core_generated_laws.py` (commit `838db94b`). Additional fixes 2026-05-20:
  `provenance()` return type annotations in 9 `_Constructors` classes
  (commit `3fbc96eb`, 3 `[attr-defined]` cleared); `cast(Category, with_axiom(...))` in
  `number_field.py` (commit `85aa2110`, 2 `[no-any-return]` cleared); proper
  Universal* base class inheritance in `lattices/homsets.py` for
  `_LatticeHomCategoryObjectMethods`, `_LatticeEndomorphisms`, `_LatticeAutomorphisms`
  (commit `03dc3d05`, 3 `[assignment]` cleared). QC frontier:
  `Found 399 errors in 115 files` (down from 1152 on 2026-05-15, down from 407 at
  session start). Error breakdown: `misc` 295, `attr-defined` 59, `call-arg` 14,
  `arg-type` 14, `return-value` 13, `operator` 4. No `[valid-type]`,
  `[untyped-decorator]`, `[redundant-cast]`, `[return]`, `[no-untyped-def]`,
  `[assignment]`, or `[no-any-return]` findings remain. The 295 `[misc]` are
  `@override` without base method — requires the Sage category MRO plugin to inject
  inheritance. All remaining groups are dynamic-inheritance, Hom/End/Aut, or
  plugin-shaped; they are gated on the plugin review completing and entering the
  downstream cleanup phases. Ruff gate cleared 2026-05-20 (commit `624c5fab`): 114
  ruff normalization errors resolved across 23 files (UP040/UP047 TypeAlias→type
  keyword, F401 re-export aliases, E402 noqa for post-sage-init imports, E501 line
  wrapping). Ruff now passes: 0 errors.
- Tracker debt cleared 2026-05-20: 10 hom-audit `needs-human-input` cards reclassified
  to `complete` (commit `c6a5ef00`). `TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION`
  completed with source evidence (no public `FinitePoset.automorphism_group()`; private
  route via `_hasse_diagram` returns index-based PermutationGroup, not poset-element
  automorphisms; surface rejected from public API). `SPEC-MAPPING-POSETS` row 388
  updated. `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`,
  `PHASE-HOM-END-AUT-WORK-QUEUE`, `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`, and
  `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` closed (all tasks complete, commit `2fbda470`).
  `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` closed 2026-05-20 (all 8 plans complete,
  all 6 exit criteria verified and checked, commit `dccd451b`).
  `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` closed (all 5 phases complete).
  `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN` advanced from `needs-agent-review` to
  `needs-human-input` (phase 9 correctness proof in SPEC.md complete, HANDOFF.md updated
  to include phase 9, plugin HEAD now `af5c9be`, commit `60bbf10f`).
  DAG has only `TASK-MYPY-PARSER` (human-gated) as the next leaf; all other work is
  blocked by `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN` being merged to main.
- Do not treat broad smoke failures, q-adic constructor gaps, or Hom runtime human
  gates as blockers for the spec-core slice unless the selected slice task proves a
  direct dependency.
- Post-merge plugin activation workflow (all pre-work done 2026-05-21, commit
  `4cf232c` on `dzackgarza/ai` main — supersedes `a798aaa` which had a just 1.46
  parse bug: heredoc body at column 0 caused just to tokenize `.` in `sys.argv[1]`
  as an expression operator; fix moved the ConfigParser merge script to
  `quality-control/scripts/merge_ini.py`): the global QC justfile `_mypy` recipe
  now detects a project-root `sage-mypy-plugin.ini` and merges it with the global
  config via ConfigParser before invoking mypy. After the plugin PR is merged, create
  `/home/dzack/research/sage-mypy-plugin.ini` with the following content and commit
  it to the research repo:
  ```ini
  [mypy]
  mypy_path = /home/dzack/research/.cache/sage-mypy-plugin/stubs

  [sage-mypy-category-plugin]
  packages =
      category_specs
  roles =
      parent
      element
      subcategory
      morphism
      homset_parent
      homset_element
  cache_dir = /home/dzack/research/.cache/sage-mypy-plugin
  ```
  IMPORTANT: `mypy_path` must be in the config file (not set by the plugin at runtime)
  because mypyc-compiled mypy 2.0 runs `compute_search_paths()` before `Plugin.__init__`,
  so runtime mutation of `options.mypy_path` has no effect on the search path. The stubs
  root is `/home/dzack/research/.cache/sage-mypy-plugin/stubs/` (generated on first run).
  Expected first-run error count with plugin: ~620 errors (up from 401 passthrough).
  The increase is correct — the plugin injects real MROs and mypy finds previously-masked
  type errors. Error breakdown: 225 `[misc]`, 139 `[attr-defined]`, 57 `[arg-type]`,
  43 `[list-item]`, 31 `[operator]`, 28 `[override]`, 27 `[return-value]`, 22
  `[redundant-cast]`, 19 `[call-arg]`, 10 `[type-var]`, 9 `[no-any-return]`, 5
  `[assignment]`, 4 `[return]`, 1 `[index]`. These are the
  `PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` tasks.

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
