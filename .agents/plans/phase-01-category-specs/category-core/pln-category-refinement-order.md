---
trackerStatus:
  type: plan
title: 'Static category refinement and constructor interception order'
status: needs-approval
planId: PLN-CAT-110
planType: spec-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
tags:
  - category-specs
  - plan
  - category-refinement
  - constructors
  - theme-category-core
  - theme-constructor-routing
---

# Static category refinement and constructor interception order

## Objective

Turn `CATEGORY_REFINEMENT_PHASES.md` into the governing order for category-spec admission: static hierarchy first, concrete interceptors second, top-level constructor redefinitions last.

## Source corpus

- `plans/CATEGORY_REFINEMENT_PHASES.md`
- `plans/category_creation_notes.md`
- `plans/axioms_with_generators_finitely_presented.md`

## Phases

- Static hierarchy and method surface: enumerate mathematical categories and method owners explicitly.
- Concrete category interceptors: refine returned parents only from the correct owner method.
- Top-level constructor redefinitions: call Sage constructors once, then refine through the target category.

## Leaf work

- `task_1777748120685_4vx3gb`: import and LazyImport bloat in ring subcategory constructors.
- `task_1777748120483_nam4mw`: number-field and rational-field option bags.
- `task_1777748120784_23rowb`: public ring constructor option bags.
- `task_1777748120529_yqjmy7`: mixed set-constructor input shapes.

## Acceptance Criteria

- [ ] Runtime discovery is used only as source research, never as the operative spec.
- [ ] Constructor routing never contains hierarchy policy.
- [ ] Every admitted constructor has a mathematical owner and a Sage-source provenance note.


## Migrated Source Bodies

### Former `plans/CATEGORY_REFINEMENT_PHASES.md`

# Category Refinement Phases

## Goal

Build the Sage category refinement surface as a static mathematical spec before
installing behavior.  The category hierarchy is the source of truth.  Runtime
inspection may be used once to learn Sage's existing method names on examples,
but the resulting method lists are recorded explicitly in the spec.

## Constraints

- `Rings` is only a staging namespace so the spec does not clobber
  Sage's `Rings` category during development.
- Subcategories are mathematical categories, not software categories.
- Predicates are mathematical names such as `is_field`, `is_number_field`,
  `is_complete_ring`, and `is_pid`.
- No runtime method discovery, generic routing tables, or exception-driven type
  checks belong in the spec.
- Constructor interception is deferred until the category hierarchy and method
  surfaces are explicit.

## Phase 1: Static Hierarchy And Method Surface

Define the full ring and module subcategory hierarchy first.  For each
subcategory, statically enumerate the relevant existing Sage method names on
`ParentMethods`, `ElementMethods`, or `MorphismMethods`.

Runtime examples may be inspected only as source material.  Once selected, each
method is written into the appropriate subcategory by name.  Methods remain
abstract unless the category itself owns a trivial predicate.

Acceptance:
- `category_specs/rings.py` imports.
- `category_specs/sage_modules.py` imports.
- The category spec files themselves are the reviewed artifact.
- There are no runtime method-list discovery checks or generic routing helpers.

## Phase 2: Concrete Category Interceptors

Replace selected abstract methods with concrete methods only when the
subcategory can reuse an existing same-named Sage implementation through the
MRO.

The implementation pattern is:

```python
result = super().method_name(*args, **kwds)
result._refine_category_(target_category)
return result
```

Methods that do not return rings, ideals, or module parents may remain abstract
as documentation.

Acceptance:
- Concrete methods appear only on the mathematically correct subcategory.
- Each concrete method calls the inherited implementation by the same name.
- Result refinement is local to the method that produced the result.

## Phase 3: Top-Level Constructor Redefinitions

Redefine top-level constructors only after Phase 1 and Phase 2 are stable.
Each redefinition has the same shape:

```python
obj = SageConstructor(*args, **kwds)
obj = TargetCategory(...)(obj)
return obj
```

Constructor redefinitions do not contain hierarchy policy.  The category call
performs refinement into the correct mathematical subcategory.

Acceptance:
- `FreeModule(R, n)` refines through `Modules(R)`.
- Ring constructors refine through `Rings`.
- Constructor code contains no generic routing beyond calling the target
  category.
