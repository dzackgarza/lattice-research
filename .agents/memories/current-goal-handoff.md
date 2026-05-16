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
  `518743f`; only the tracked generated `__pycache__/plugin.cpython-312.pyc`
  remains dirty after tests.
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
  final-override error; many unrelated active QC findings remain.
