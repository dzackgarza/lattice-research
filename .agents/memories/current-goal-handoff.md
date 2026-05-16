# Current Goal Handoff

Purpose: route the next session only. Cards, plans, and git history remain the
authorities for status, evidence, and completed work.

## Current Phase

- Active phase: category-spec and semantic-vocabulary.
- Active QC frontier: `FEATURE-QC-WARNINGS-ZERO` ->
  `PLAN-QC-MYPY-FOUNDATION-ORDER` -> `PHASE-QC-BASIC-TYPING-HYGIENE`.
- Continue stabilizing mixed diffs before judging completion.

## Current Pickup

- Remaining research repo dirty tree is still large; prefer more narrow commits
  or patch artifacts over broad staging.
- Recent source fix: `6252e88` removed `_Fields.ParentMethods.gcd` because
  fields inherit the final principal-ideal-domain `gcd`; focused research mypy
  no longer reports `category_specs/rings/subcategories/field.py:141`.
- Recent source fix: `3309ce3` removed duplicate `Rings.SubcategoryMethods`
  `Finite`/`Topological` selectors because those final selectors are inherited
  from `Sets.SubcategoryMethods`; focused research mypy no longer reports the
  two `category_specs/rings/__init__.py` final-override errors.
- Recent source fix: `428c936` removed `@final` from the wrapped
  `Homsets.Endset` bridge because its documented purpose is to let project
  subclasses declare `Endset` axiom classes; focused research mypy no longer
  reports `category_specs/homsets/homsets.py:122`.
- The first source boundary to inspect is the remaining mixed `category_specs/rings/__init__.py`
  diff. It combines real constructor/API corrections with many selector casts.
  Split source defects from checker-model gaps before staging anything there.
- Plugin repo `/home/dzack/sage-mypy-plugin` has source committed through
  `c329ae6`; only the tracked generated `__pycache__/plugin.cpython-312.pyc`
  remains dirty after tests.
- `category_specs/sets/__init__.py:646` `TopologicalSpaces().Subobjects()`
  is handled by plugin fixture `test_construction_selector_class_attribute.py`;
  do not replace construction selectors with local casts in source.
- `category_specs/modules/subcategories/constructions/cartesian_products.py`
  override errors for `__init_extra__` and `_lmul_` are routed to plugin
  fixture `test_construction_extra_super_category_methods.py`; do not delete
  the overrides or add local casts in source.
- The p-adic `return self` false positive is routed through the plugin's
  transitive method-container return fixture and should not be reworked in
  source. The field zero-ideal completion `return self` false positive is routed
  through the plugin's value-dependent completion fixture and should not be
  reworked in source.

## Routing Constraints

- QC=0 is required before real implementation enters main.
- Every mypy class must become either a source fix with evidence or a plugin-spec
  failing reproducer with expected checker behavior.
- Do not add local casts around `_with_axiom`, `category_of`, `refine_category`,
  Hom/End/Aut selectors, callable parent projection, method-container aliases, or
  provider assignment specialization unless a source defect is proved.
- Use `with_axiom(...)` for axiom refinement; do not reintroduce direct
  `_with_axiom` calls in touched `SubcategoryMethods`.
- `MorphismMethods` is banned in category specs; morphism behavior belongs on the
  relevant Hom-category `ElementMethods`.
- Do not recreate root-level plugin fixtures such as `test_override.py`.

## Validation State

- `just plan-validate` passed after the planning tree moved under `.agents/plans`.
- `just test` still fails at mypy; this is the active QC frontier, not a
  completion signal.
- Plugin `just test` passes in `/home/dzack/sage-mypy-plugin`. Focused research
  mypy no longer reports the p-adic or field-completion `return self` errors.
  It also no longer reports `category_specs/rings/subcategories/field.py:141`;
  focused mypy on `category_specs/rings/__init__.py` no longer reports local
  `Finite`/`Topological` final-override errors; focused mypy on
  `category_specs/homsets/homsets.py` no longer reports the local `Endset`
  final-override error; focused mypy on `category_specs/sets/__init__.py`
  no longer reports the local construction-selector `[call-arg]`; many
  unrelated active QC findings remain.

## Interrupted Session State (codex 019e2a36, start 2026-05-15 05:57)

The last session was implementing the plugin model for construction categories
whose method containers inherit through `extra_super_categories() ->
[base_category()]`. It was interrupted mid-mypy-run. Both repos have unstaged
WIP.

### sage-mypy-plugin

- `sage_mypy_category_plugin/plugin.py` — has unstaged work-in-progress adding
  `_construction_owner_method_container_bases()`. The implementation probes
  construction_bases via a debug `ctx.api.fail(...)` call on line 158 that
  dumps the computed bases as a mypy error. This debug line is the evidence
  trail — do not remove until the fix is verified.
- `tests/fixtures/local_wrapper_pkg/category_specs_like/mypy_test_fixtures/
  test_construction_extra_super_category_methods.py` — reorganized fixture.
  `_CartesianProducts` now declares `@override` methods and `_Modules` has
  `CartesianProducts = _CartesianProducts` as a class attribute.
- Latest commit: `c329ae6` (test: spec construction extra-super method gap)
- `__pycache__/plugin.cpython-312.pyc` is stale, ignore.

### Research repo

- Dirty tree (~130+ files across .agents/skills/, category_specs/, src/).
  Intentional QC edits from the session — described by the agent as "heavily
  mixed." Do not broad-stage; prefer narrow commits.
- Last commit: `a59695d` (chore: route cartesian product override QC gap)
- CartesianProducts override errors are routed to plugin spec but the fix is
  not yet implemented.

### Next action

Implement the plugin model so construction categories with
`extra_super_categories() == [base_category()]` contribute the base category's
ParentMethods and ElementMethods to the MRO. Then prove the exact
CartesianProducts errors move by running focused mypy on
`category_specs/modules/subcategories/constructions/cartesian_products.py`.
Work in the plugin repo first — a trial source edit at the research level did
not remove the errors.

### Non-goals

- Do not remove the debug probe until implementation is verified.
- Do not add new process/planning artifacts.
- Do not touch the old routing constraints or phase structure.
