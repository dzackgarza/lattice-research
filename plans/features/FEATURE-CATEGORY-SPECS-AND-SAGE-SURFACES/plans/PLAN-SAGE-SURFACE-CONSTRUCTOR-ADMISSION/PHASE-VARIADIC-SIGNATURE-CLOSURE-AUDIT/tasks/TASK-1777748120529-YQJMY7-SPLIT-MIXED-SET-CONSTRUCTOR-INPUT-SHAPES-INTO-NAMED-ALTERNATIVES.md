---
id: TASK-1777748120529-YQJMY7-SPLIT-MIXED-SET-CONSTRUCTOR-INPUT-SHAPES-INTO-NAMED-ALTERNATIVES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Split mixed set-constructor input shapes into named alternatives
status: needs-review
priority: high
complexity: 56
description: Split mixed set-constructor input shapes into named alternatives
successCriteria:
- Split mixed set-constructor input shapes into named alternatives is resolved according
  to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Split mixed set-constructor input shapes into named alternatives
Source: pasted backlog 2026-05-02.

Task: split the mixed input shapes on set constructors (objects, collection, and single object) into explicit alternatives using @overload.

## Grounding

- Source provenance: recovered variadic sprint source at
  `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` in commit
  `8d1c21c^`; current phase card
  `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT.md`; Sage set inventory
  `category_specs/sets/docs/SAGE_INVENTORY.md`; tracked set mapping spec
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`.
- Style authority: `.agents/skills/category-spec-style/references/style.md`
  requires non-variadic public constructor surfaces, explicit overloads for finite
  Sage casework, and no software-shaped helper types.
- Sage grounding:
  - `sage.sets.set.Set(X, category=None)` accepts existing Sage category objects,
    finite iterable collections, and other iterable/wrapper cases; it rejects Sage
    elements without a defined underlying set. The project mapping explicitly rejects
    this generic wrapper as a public constructor.
  - `Set(X)` collection behavior is recovered by
    `Sets().Constructors().from_iterable(elements)` and
    `FiniteEnumeratedSet(elements)`.
  - A single element determines the singleton finite set `{x}`; this is a named
    finite-enumerated construction, not the generic Sage wrapper.
  - Existing set objects already lie in `Sets()` and must not be wrapped merely to
    satisfy a constructor call shape.
  - Fixed-base set-partition constructors still expose collapsed base-set shapes:
    a set object, an iterable collection of elements, or an integer cardinality for
    the standard totally ordered finite base `{1, ..., n}`.
- Mathematical owner: `Sets().Constructors()` owns named set-entry constructors;
  `Sets().Partitioned()` owns the fixed-base set-partition result surface.
- Return objects: finite iterable and singleton inputs return finite countable set
  objects; fixed-base partition constructors return `SetPartitionSet`; integer
  fixed-base inputs additionally refine through
  `Sets().Partitioned().FiniteTotallyOrderedBase()`.

## Acceptance Criteria

- [x] Do not admit a catch-all project `Set(X)` constructor.
- [x] Preserve existing finite-collection behavior through
  `from_iterable(elements)` and `FiniteEnumeratedSet(elements)`.
- [x] Add or preserve a named singleton finite-set path for a single element.
- [x] Split fixed-base set-partition constructor signatures into explicit overloads
  for set object, finite iterable collection, and integer cardinality inputs.
- [x] Keep implementations closed over the admitted cases and avoid `*args`,
  `**kwargs`, or duck-typed wrapper admission.
- [x] Add smoke or regression coverage using small finite examples.
- [x] Run syntax/smoke validation, or record the exact phase-local blocker.
- [x] Run and record a spec-weakening review before moving the card to
  `needs-review`.

## Complexity And Ownership

- Owner: category-spec set constructor implementation agent.
- Complexity: 56, Moderate (41-60).
- Complexity band: Moderate (41-60).
- Why this specific score:
  - The task touches multiple constructor overload surfaces for set creation, which is broader than a single method edit but still bounded to API typing. The complexity is moderate because behavior should remain same while call-shape space is decomposed, requiring careful static compatibility checks.
- Item-specific evidence:
  - The source-backed scope is limited to set constructor entry points in
    `category_specs/sets/__init__.py`, set smoke/regression coverage, and this card.
  - The work does not change method ownership or admit a new wrapper category.
  - The main coupling risk is preserving Sage-compatible fixed-base partition
    construction while making the public signatures explicit.

## Work Log

- 2026-05-06: Began execution. Grounded the vague migrated card against Sage `Set`
  source, the set inventory, the tracked set mapping spec, and the category-spec
  style rules. Scoped implementation to named alternatives and fixed-base
  set-partition overloads, not to a generic `Set(X)` wrapper.
- 2026-05-06: Added `Sets().Constructors().SingletonSet(element)` as the named
  singleton finite-set path, documented it in `SPEC-MAPPING-SETS.md`, and added
  smoke coverage with a small integer witness.
- 2026-05-06: Added explicit `@overload` declarations for
  `SetPartitions`, `SetPartitionsWithBlockCount`, and
  `SetPartitionsWithBlockSizes` for set-object, finite-iterable, and integer
  cardinality base inputs. The runtime implementation still delegates to Sage's
  fixed-base constructor and refines through the existing partition categories.

## Validation

- `python -m py_compile category_specs/sets/__init__.py` passed.
- `git diff --check -- category_specs/sets/__init__.py category_specs/sets/smoketest.sage plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-1777748120529-YQJMY7-SPLIT-MIXED-SET-CONSTRUCTOR-INPUT-SHAPES-INTO-NAMED-ALTERNATIVES.md` passed.
- `just --justfile category_specs/justfile smoke-file sets/smoketest.sage` passed,
  with the pre-existing Sage warning about `Sets.Topological` not subclassing
  `CategoryWithAxiom`.

## Spec-Weakening Review

- Reviewed the task-local diff for generic `Set(X)` admission, deleted abstract
  methods, removed constructor obligations, narrowed smoke assertions, and
  Sage-gap-driven interface shrinkage.
- Result: passed. The diff preserves the `Set(X)` rejection, adds the named
  singleton surface, and adds overload declarations without removing obligations.
