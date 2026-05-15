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
- The first source boundary to inspect is the remaining mixed `category_specs/rings/__init__.py`
  diff. It combines real constructor/API corrections with many selector casts.
  Split source defects from checker-model gaps before staging anything there.
- Plugin repo `/home/dzack/sage-mypy-plugin` has source committed through
  `4ffb11f`; only the tracked generated `__pycache__/plugin.cpython-312.pyc`
  remains dirty after tests.

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
- `just test` still fails at mypy with 429 errors; this is the active QC frontier,
  not a completion signal.
- Plugin targeted fixtures passed for cached methods, constructors, functorial
  constructors, classcall kwargs, operator surfaces, `_with_axiom`, final binding,
  abstract binding, and a focused final-binding rerun after removing debug output.
