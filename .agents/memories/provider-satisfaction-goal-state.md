---
title: Object Method Resolution Goal State
status: review-accepted
tags: [goal-state, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Goal State

## Preserved Object

This note preserves the object-method-resolution contract for category refinement:
`ParentMethods` abstract methods are requirements on objects, concrete Sage/project
object methods satisfy those requirements only when dynamic lookup reaches the concrete
method, and genuinely missing requirements stay visibly abstract.

## Current Mode

`SYNTHESIZE` accepted for the provider-satisfaction/object-method-resolution goal.
Do not reopen source reconstruction for this contract unless a new live Sage/refinement
witness contradicts the accepted relation.

## Accepted Relation

For `Rings().Constructors().ZZ()`, the project `_RingObjectMethods.ideal_monoid`
abstract requirement is not an implementation. The requirement is satisfied because
the refined object resolves `ideal_monoid` to Sage's concrete
`sage.categories.rngs.Rngs.parent_class.ideal_monoid`, and the call returns the real
ideal monoid of `ZZ`.

For an incomplete category declaring only
`ParentMethods.required_regression_operation`, refinement does not silently turn the
abstract method into a callable implementation. The generated parent class retains the
requirement in `__abstractmethods__`, and calling it fails with the explicit abstract
requirement assertion.

## Source Boundary

Authoritative commits:

- `62c16d6912e123f292029eb54b15481c815b3f43` records the red live regression test.
- `75cfa0c7888ec3dcb4bbb8fc99e5a0d05ba6f03e` records the source repair.

The repair belongs at the Sage named-class boundary. Sage constructs category
`parent_class` surfaces through `Category._make_named_class` and `dynamic_class`;
`dynamic_class` copies method-provider dictionaries into a `DynamicMetaclass` class and
does not compose `ABCMeta`. The accepted repair therefore computes the object-method
surface before constructing the dynamic parent class, instead of mutating refined
objects after the fact.

Rejected mechanisms remain rejected:

- no cache priming;
- no per-method `ideal_monoid` patch;
- no spec implementation that turns an abstract requirement into behavior;
- no source-shape regression test;
- no broad validator pretending to repair lookup order.

## Verification State

Required targeted verification has passed:

- `just -f category_specs/justfile smoke-file rings/tests/regression/object_method_resolution.sage`
- `git diff --check 62c16d69..75cfa0c7 -- category_specs/cat/base_category_types.py category_specs/utils.py category_specs/rings/tests/regression/object_method_resolution.sage`
- `just --justfile category_specs/justfile check-banned-spec-patterns`

Independent state-machine review accepted the repair after inspecting the red test,
source diff, Sage boundary source, runtime witness, and residual warning surface.

`just category-specs-mypy-structural-report` still fails before mypy on an existing
plugin projection conflict:

```text
AssertionError: Conflicting provider projections for category_specs.modules.homsets._RModHomCategoryObjectMethods: homset_parent -> category_specs.modules.homsets.RModuleHomCategory.parent_class vs homset_parent -> category_specs.modules.homsets.RModuleHomCategory.parent_class
```

That structural-report failure is not the object-method-resolution repair, but it is the
next category-spec verification residue if the active DAG selects structural typing
work. Its regenerated `reports/workstreams/category-specs-mypy-structural/latest.*`
files may be dirty in the working tree.

## Next Pickup

If resuming this goal, first read `provider-satisfaction-goal-contract`.
There is no remaining source-edit residue for the accepted object-method-resolution
contract unless a new live witness falsifies it.

For new category-spec work, return to the planning DAG and the current handoff instead
of extending this state note.
