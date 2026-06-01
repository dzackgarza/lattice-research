---
title: Current Goal Handoff
---
# Handoff

## Anchor

Read `mem:repo-purpose-mathematical-research-machine` before any card or plan.

## Current phase

Category-spec vocabulary: building the semantic substrate so downstream lattice/Coble
work has named objects, morphisms, and invariants, not raw matrices.

## Current next action

Branch `fix/spec-refinement-class-api` exists to correct the ABC/refinement API boundary.
The bridge target is now narrow: class/type-returning refinement for project-owned spec
implementation classes. Instance-level `refine_category(X, ...) -> X` remains an
existing-Sage-parent declaration path and a post-construction category declaration path
after a project-owned class has already been instantiated through its refined class.

Do not reintroduce refinement-time validation, abstract-name subtraction, generated
failure bodies, cache priming, casts, or method-name cases. The model is:

- `refine_category(ProjectParentClass, categories)` returns a dynamic class combining
  the implementation class with the target category `parent_class`;
- canonical project constructors instantiate that refined class so ABCMeta raises at
  construction for missing project `ParentMethods` obligations;
- existing Sage constructors may build a Sage parent and then declare it into project
  categories by instance refinement;
- Sage `__init__` methods that overwrite the instance category may require the sequence
  class-refined instantiation first, then instance category declaration. That is the
  current `Sets().Constructors().ImageSubobject(...)` pattern because Sage
  `ImageSubobject.__init__` computes its own subobject category via `Parent.__init__`.

Current verified bridge evidence:

- abstract-only project `ElementMethods` are declaration surfaces and are not installed
  as runtime ellipsis bodies on Sage element lookup;
- Hom-category lifting skips raw Sage join categories whose class MRO does not declare
  the project functor category;
- `OrderTwoGroups().Constructors().Partial()` fails during refined-class instantiation
  with ABCMeta naming only `is_abelian`; `Complete()` returns a usable object in
  `OrderTwoGroups`;
- AST/probe route audit found `constructor_redefinitions.py`, `rings`, `modules`,
  `sets`, `posets`, `algebras`, hom/end/aut, and tensor-component routes. The only
  project-owned wrapper route found using raw instance refinement was
  `Sets().Constructors().ImageSubobject`, now routed through refined-class
  instantiation before instance declaration.

Current verification frontier:

- `python3 -m py_compile category_specs/sets/__init__.py category_specs/utils.py
  category_specs/cat/base_category_types.py category_specs/homsets/homsets.py` passes.
- `rings/tests/regression/object_method_resolution.sage` passes.
- `rings/tests/regression/finite_fields.sage` passes.
- `rings/tests/regression/integer_mod_rings.sage` passes.
- `sets/tests/regression/set_partitions.sage` passes.
- `sets/smoketest.sage` passes, with existing Sage warning noise about topological-set
  axiom binding.
- `homsets/smoketest.sage` passes.
- `just --justfile category_specs/justfile check-banned-spec-patterns` reports 439
  repo-wide findings and 13 staged findings in
  `category_specs/rings/subcategories/rational_field.py`.
  Treat those staged rational-field findings as a separate QC/staging issue unless the
  live constructor/refinement task explicitly touches that file.
- `rings/smoketest.sage` still fails on number-field base-category identity, p-adic/Zq
  keyword drift, deferred lattice-precision extension constructors, multivariate
  power-series keyword drift, and a Puiseux-series metaclass conflict.

Next pickup should keep the constructor/refinement objective narrow: every project-owned
canonical constructor must class-refine before instantiation, while existing Sage
parents and singletons use named instance-declaration compatibility paths. Treat the
rings smoke frontier and staged rational-field banned-pattern findings as separate
failures unless a route is shown to be a raw-then-refined project-owned constructor
violation. Do not restart from `finite_fields.sage`, `integer_mod_rings.sage`,
`sets/smoketest.sage`, `homsets/smoketest.sage`, or the OrderTwoGroup fixture unless
one of those regressions fails again.

## Required context

Before the next source edit, load:

- `mem:category-spec-epistemic-foundation`
- `mem:category-spec-repo-model-corrections`
- `mem:category-spec-refinement-category-declaration`
- `mem:category-spec-methods-are-abstract`
- `mem:provider-satisfaction-goal-contract`
- `mem:provider-satisfaction-goal-state`
- `mem:category-spec-rotten-core-indicators`
- `mem:mathematical-sanity-check`
- `mem:sage-axiom-binding-is-descriptor-binding`
- `category_specs/AGENTS.md`
- `category-spec-style`
- `research-state-machine`

## Constraints

- No sage-stubs writing.
- No downstream Coble work.
- No `# type: ignore`.
- No `typing.cast` additions in category-spec code.
- No refinement-time abstract-method satisfaction checks.
- No generated failure bodies for missing spec obligations.
- No `with_axiom(self, "...")`; use Sage's direct `self._with_axiom("...")`
  idiom where the descriptor binding is correct.
- `NotImplementedError` remains rejected by pre-commit hook.
