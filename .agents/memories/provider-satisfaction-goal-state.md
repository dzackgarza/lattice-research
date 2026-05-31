---
title: Object Method Resolution Goal State
status: active-red
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

`RECONCILE` with a committed red test. Do not claim this goal complete.
Do not treat `bac2ab28` or `1c6f3b65` as acceptance evidence; they recorded a false
completion state before the missing-obligation leak was tested at the right boundary.

After user approval of the red-test proof, the next source repair must target the
Sage dynamic `parent_class` abstract set and the `refine_category` boundary. Do not
patch by method name, cache state, source-shape checks, or assertion-body methods.

## Red Witness

Authoritative red-test commit:

- `ecac9da8` records the live regression proof in
  `category_specs/rings/tests/regression/object_method_resolution.sage`.

Run:

```bash
just -f category_specs/justfile smoke-file rings/tests/regression/object_method_resolution.sage
```

Current failure:

```text
AssertionError: default refine_category accepted missing ParentMethods obligation
default refine_category returned after missing obligation
optimized refine/call accepted missing ParentMethods obligation
optimized refine_category returned after missing obligation
optimized missing object method call returned silently
```

This proves two request-witness facts are still false:

- default `refine_category(ZZ, [C])` accepts an incomplete `ParentMethods` obligation;
- the generated `assert False` method body is not enforcement, because `sage -python -O`
  strips it and the missing method call returns silently.

## Positive Residue

Commit `75cfa0c7` still fixes the specific concrete-method shadowing symptom:
`Rings().Constructors().ZZ().ideal_monoid()` resolves to Sage's concrete
`sage.categories.rngs.Rngs.parent_class.ideal_monoid`.

That positive residue is not enough for the goal. The class-system contract remains red
until missing obligations are represented on the actual dynamic parent class and
rejected by refinement.

## Required Source Direction

The next repair should make these relation claims true:

- the actual Sage dynamic `X.category().parent_class` has a computed
  `__abstractmethods__` set after category joins/refinement;
- abstract markers remain requirements, not implementations;
- concrete inherited object methods remove their names from the abstract set only when
  refined lookup reaches the concrete method;
- `refine_category` checks `X.category().parent_class.__abstractmethods__`, not
  `type(X).__abstractmethods__`, because existing Sage parents such as `ZZ` remain
  `IntegerRing_class`;
- no generated missing-obligation method body may rely on `assert`.

The likely low-level implementation path is to apply ABCMeta's abstract-set algorithm
to Sage's preferred dynamic parent class, or compose/use an ABC-aware metaclass where
Sage allows it. Source repair must be justified from Sage dynamic-class source and live
runtime facts before editing.

## Next Pickup

First explain why the red test proves the bug, then wait for user approval before
source repair. After approval, load `provider-satisfaction-goal-contract`,
`category-spec-style`, `research-state-machine`, `research-code-style`,
`research-software-wiring`, `test-guidelines`, `systematic-debugging`,
`systematic-deduction`, `anti-slop`, `llm-failure-modes`, and `git-guidelines`.
