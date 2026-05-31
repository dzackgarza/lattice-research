---
title: Object Method Resolution Goal State
status: active-partial
tags: [goal-state, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Goal State

## Preserved Object

This note preserves the object-method-resolution contract for category refinement:
`ParentMethods` abstract methods are requirements on objects, concrete Sage/project
object methods satisfy those requirements only when dynamic lookup reaches the concrete
method, and genuinely missing requirements must fail at the refinement/class-system
boundary.

## Current Mode

`RECONCILE` with targeted ABC-boundary commits through `3734d409`. Do not claim this
goal complete.
Do not treat `bac2ab28` or `1c6f3b65` as acceptance evidence; they recorded a false
completion state before the missing-obligation leak was tested at the right boundary.

The current patch targets the Sage dynamic `parent_class` abstract set and the
`refine_category` boundary. Do not patch by method name, cache state, source-shape
checks, or assertion-body methods.

## Red Witness

Authoritative adversarial-test commits:

- `ecac9da8` records the default/optimized missing-obligation regression in
  `category_specs/rings/tests/regression/object_method_resolution.sage`.
- `5f3cd1cd` adds the joined-parent-class abstract propagation guard in
  `category_specs/rings/tests/regression/object_method_resolution.sage`.
- `ce1ed355` adds the failed-refinement atomicity guard: rejection must not leave the
  parent in the rejected category.

Run:

```bash
just -f category_specs/justfile smoke-file rings/tests/regression/object_method_resolution.sage
```

Former failure:

```text
AssertionError: default refine_category accepted missing ParentMethods obligation
default refine_category returned after missing obligation
optimized refine/call accepted missing ParentMethods obligation
optimized refine_category returned after missing obligation
optimized missing object method call returned silently
```

These tests guard three request-witness facts:

- default `refine_category(ZZ, [C])` accepts an incomplete `ParentMethods` obligation;
- the generated `assert False` method body is not enforcement, because `sage -python -O`
  strips it and the missing method call returns silently.
- a joined Sage dynamic `parent_class` can lose inherited abstract obligations.

## Positive Residue

The targeted regression now checks the concrete-method shadowing symptom with a live
Sage-backed category whose `ParentMethods` declares abstract `ideal_monoid`: refinement
keeps Sage's concrete `sage.categories.rngs.Rngs.parent_class.ideal_monoid` as the
winning method.

This positive residue is not enough for the larger provider-satisfaction goal.
Strict enforcement now exposes separate root ring-surface obligations that are not yet
resolved for `Rings().Constructors().ZZ()`/`QQ()`.

## Required Source Direction

The ABC-boundary patch makes these relation claims true in the targeted regression:

- the actual Sage dynamic `X.category().parent_class` has a computed
  `__abstractmethods__` set after category joins/refinement;
- abstract markers remain requirements, not implementations;
- concrete inherited object methods remove their names from the abstract set only when
  refined lookup reaches the concrete method;
- `refine_category` checks `X.category().parent_class.__abstractmethods__`, not
  `type(X).__abstractmethods__`, because existing Sage parents such as `ZZ` remain
  `IntegerRing_class`;
- no generated missing-obligation method body may rely on `assert`.

The low-level implementation path applies ABCMeta's abstract-set algorithm to Sage's
preferred dynamic parent class and rejects unresolved obligations in `refine_category`
before mutating the parent. For existing Sage/Cython parents, concrete methods on the
actual parent type are accepted as realizations; unresolved names remain refinement
blockers.

## Next Pickup

Commit or review the current ABC-boundary patch, then source-ground and repair the root
`Rings().Constructors().ZZ()`/`QQ()` abstract obligations revealed by strict
enforcement. Do not loosen `refine_category` or restore import-time eager refinement to
make those constructors pass.
