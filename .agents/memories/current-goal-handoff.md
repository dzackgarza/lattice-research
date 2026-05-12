# Current Goal Handoff

This is the rolling IWE-visible pickup note for the active goal. It is a routing aid, not a tracker. Cards and plans remain authoritative for status, dependencies, source grounding, and acceptance.

## Current phase

Category-spec and semantic-vocabulary remains the active staged-program phase per `.agents/current-goal-phase.md`.

Repo-visible root state at this handoff refresh:

- `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`: `in-progress` (reopened on the
  Hom/End/Aut path by the generic homset owner mismatch)
- `FEATURE-GEOMETRY-CATEGORY-INTERFACES`: `complete`
- `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`: `in-progress`, but DAG-gated by `FEATURE-QC-WARNINGS-ZERO` and the already-complete category-spec root

## Recent decision delta

- Implemented the plugin rewrite chain on 2026-05-10:
  - `TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION`
  - `TASK-MYPY-NAMESPACE-AGNOSTIC-HOOK-MATCHING`
  - `TASK-MYPY-TEST-THIRD-PARTY-SUBTREES`
- Coupled reopened cards that were failing for the same reason were advanced with the implementation:
  - `TASK-MYPY-PARSER`
  - `TASK-MYPY-PLUGIN-CLASS`
  - `TASK-MYPY-TEST-ARTIFICIAL`
  - `TASK-MYPY-TEST-MYPY-INTEGRATION`
- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`, `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`, and the three plugin phases are now in review-ready state rather than implementation-rewrite state.
- The plugin repo now accepts semantically valid third-party subtree method containers outside `sage.categories.*`, and the global QC mypy config at `/home/dzack/ai/quality-control/mypy-global.ini` now loads `sage_mypy_category_plugin.plugin`.
- Repo QC follow-up on `category_specs/homsets/*` found the remaining Hom/End/Aut
  override failures are mixed, not plugin-only, but the semantic conclusion changed:
  the repo does not inherit Sage generic homsets as its semantic base. It redefines
  and mirrors retained Sage homset behavior through project `HomCategory`
  construction and subtree hom specs.
- Rewrote `DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION` around the
  project-owned HomCategory route; the generic Hom/End/Aut task now covers only the
  generic owner-story/QC framing.
- Runtime MRO tracing refined that cleanup: only the generic Hom-layer methods and
  the first-definition subtree markers are non-overrides. The End/Aut method-surface
  overrides and `Sets().HomCategory().is_isomorphism` are real runtime overrides and
  were restored.
- Reopened `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` and
  `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT` with new leaf tasks for
  Cat, Sets, Rings, Algebras, Modules, Posets, TopologicalSpaces, and Lattices hom
  mapping audits.

## Next pickup

- As of the 2026-05-12 state audit, the branch is even with its upstream and the
  regenerated card progress report has no `blocked` items. DAG priority is still the
  reopened category-spec Hom/End/Aut path before ModulesWithForms/lattices.
- User clarified on 2026-05-12 that priority descriptions must use the DAG frontier:
  if a card or feature depends on an incomplete root, its internal progress and child
  statuses are irrelevant and should not be considered until all prerequisites are
  complete.
- The card progress report generator now enforces this rule: `plans/card-progress-report.md`
  renders high-priority work as `High-Priority DAG Frontier` plus `High-Priority
  DAG-Gated Items`, and inherited parent dependencies gate child plans/tasks.
- Execute `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME` to update the
  generic Hom/End/Aut owner story, then work through the reopened subtree mapping
  audit tasks under `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`.
- The next homset/plugin pass should split remaining mypy findings into:
  1. live plugin misses on runtime-real overrides (`endsets.py`,
     `autsets.py`, and `sets/homsets.py:is_isomorphism`), and
  2. non-plugin construction/type issues (`Of`, `default_super_categories`,
     `Endset`, and similar construction-level cases).
- For each homset-bearing subtree, ensure Sage homset/container methods that remain in
  scope are explicitly mirrored onto the project hom specs rather than assumed inherited.
- The plugin feature tree itself remains review-ready; do not reopen it unless the
  post-cleanup runtime-inherited cases still fail statically.
- `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` is the next mathematical feature root, but it is not the current pickup while the QC/plugin prerequisite chain remains open in the tracker DAG.

## Non-goals

- Do not resume already-complete category-spec cleanup phases unless a new review finding reopens them.
- Do not treat Sage-prefixed fixture passes alone as sufficient plugin evidence; the new external-subtree coverage and plugin-loaded QC config path are now part of the contract.
- Do not treat every remaining Hom/End/Aut `misc: override` error as plugin debt, and
  do not treat backend Sage container reuse as semantic inheritance.
- Do not start ModulesWithForms/lattices implementation or downstream Coble features while the QC/plugin prerequisite chain remains unresolved in the tracker graph.

## Validation state

- In `~/sage-mypy-plugin`, `just test` passes (`27 passed, 3 warnings`).
- Third-party subtree integration coverage passes in `tests/test_mypy_integration.py`.
- The repo-local reproduction `test_override.py` passes under a plugin-enabled mypy config.
- Under `/home/dzack/ai/quality-control/mypy-global.ini`, `test_override.py` no longer reports the override error, which is the config-path proof that the plugin now loads on that validation path.
- Sage runtime MRO probes still show that `category_specs.homsets.homsets.HomCategory.parent_class`
  does not inherit `sage.categories.homset.Homset`, but the current durable ruling is
  that the project does not semantically inherit Sage generic homsets anyway.
- Concrete objects built through Sage `Hom(...)` still use Sage homset container
  classes as backend runtime objects; that is backend evidence, not semantic ownership.
- Focused mypy still rejects the restored runtime-real overrides in
  `category_specs/homsets/endsets.py`, `category_specs/homsets/autsets.py`, and
  `category_specs/sets/homsets.py:is_isomorphism`; those are the current plugin/glue
  failures. The generic Hom-layer overrides remain correctly removed, and the
  construction-level `Of` / `default_super_categories` / `Endset` errors remain
  separate non-plugin issues.
- Plugin-local diagnosis now splits those glue failures further:
  - `endsets.py` / `autsets.py`: plugin introspection resolves the correct runtime
    projections and a direct mypy build shows the helper classes end with injected
    MROs (`UniversalEnd* -> UniversalHom*`, `UniversalAut* -> UniversalEnd*`), yet
    mypy still emits `no base method was found`. This is a helper-class/plugin
    interaction beyond simple projection failure.
  - `sets/homsets.py:is_isomorphism`: plugin projection for `_SetMorphisms` fails
    earlier with `ParameterizedCategoryError` because alias resolution maps it to
    `SetHomCategory.ElementMethods`, and `instantiate_category_from_source_path`
    cannot build `SetHomCategory` without a `base_category`.
- Plugin repo TDD reproductions now exist in `~/sage-mypy-plugin` and fail live:
  - `test_third_party_helper_alias_parent_methods_override`
  - `test_third_party_helper_alias_element_methods_override`
  - `test_third_party_helper_alias_parameterized_override`
  - `test_third_party_helper_alias_parent_methods_transitive_override`
  - `test_third_party_helper_alias_element_methods_transitive_override`
  - `test_third_party_helper_alias_parameterized_parent_methods_override`
  with real third-party fixtures under
  `tests/fixtures/third_party_pkg/categories/mypy_test_fixtures/`.
  A focused run of the helper-alias red set now reports `6 failed`, and each failure
  message includes the plugin's own projection summary:
  dynamic class, dynamic bases, static bases, and unmapped dynamic bases. The
  crucial observation is that the plugin often reports the expected static base
  (for example `_AliasBaseParentMethods`) while mypy still emits
  `no base method was found`.
- The remaining observed non-plugin failure shapes are now also covered in the plugin
  repo by passing rejection tests:
  - helper-alias first-definition misuse of `@override`
  - final instance-method override
  - final classmethod override
  - final class-attribute override
  - final + incompatible-signature override (`Of`-shaped)
- `just plan-validate` passes after the new decision/task and status updates.
- 2026-05-12 state audit: `git fetch origin` left the current branch even with
  `origin/dzack/reviews-bugfixes-and-phase-completion-2026-05-07`; `just
  plan-validate` passed with all schemas valid and rewrote `plans/plan-dag.md`; `just
  plan-progress-report` regenerated `plans/card-progress-report.md` at
  `2026-05-12 10:55 UTC`.
