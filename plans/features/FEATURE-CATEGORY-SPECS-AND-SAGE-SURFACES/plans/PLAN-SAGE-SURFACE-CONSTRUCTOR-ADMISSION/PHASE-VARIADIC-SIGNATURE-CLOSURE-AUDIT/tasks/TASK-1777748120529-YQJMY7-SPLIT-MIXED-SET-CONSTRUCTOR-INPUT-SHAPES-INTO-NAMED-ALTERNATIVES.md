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
  cardinality base inputs. The initial runtime implementation still delegated the
  broad mixed union to Sage; this was corrected by the 2026-05-07 rework below.
- 2026-05-07: Gate 2 review found that the overload declarations were still backed
  by broad mixed-union bodies delegating directly to Sage. Reworked the runtime path
  so fixed-base set-partition constructors first dispatch through a closed helper
  over the three admitted cases: Sage integer cardinality, categorical set object,
  or finite iterable materialized as a tuple.

## Validation

- `python -m py_compile category_specs/sets/__init__.py` passed.
- `git diff --check -- category_specs/sets/__init__.py category_specs/sets/smoketest.sage plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-1777748120529-YQJMY7-SPLIT-MIXED-SET-CONSTRUCTOR-INPUT-SHAPES-INTO-NAMED-ALTERNATIVES.md` passed.
- `just --justfile category_specs/justfile smoke-file sets/smoketest.sage` passed,
  with the pre-existing Sage warning about `Sets.Topological` not subclassing
  `CategoryWithAxiom`.
- 2026-05-07 rework validation:
  - `python -m py_compile category_specs/sets/__init__.py` passed.
  - `git diff --check -- category_specs/sets/__init__.py` passed.
  - `just --justfile category_specs/justfile smoke-file sets/smoketest.sage` passed,
    with the same pre-existing Sage warning about `Sets.Topological` not subclassing
    `CategoryWithAxiom`.

## Spec-Weakening Review

- Reviewed the task-local diff for generic `Set(X)` admission, deleted abstract
  methods, removed constructor obligations, narrowed smoke assertions, and
  Sage-gap-driven interface shrinkage.
- Result: passed. The diff preserves the `Set(X)` rejection, adds the named
  singleton surface, and adds overload declarations without removing obligations.

## Review Log

### Review 2026-05-07 (Popper)

**Gates passed:** Gate 1 Definition Grounding
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** revision-required, then reworked within this card's scope; independent
re-review still required

#### Gate 2 Finding: Mixed Union Bodies Still Delegated To Sage

- The card requires closed admitted cases and no duck-typed wrapper admission.
- The implementation had overloads, but the concrete bodies still accepted
  `Set | Iterable[SetElement] | Integer` and delegated directly to Sage for
  `SetPartitions`, `SetPartitionsWithBlockCount`, and
  `SetPartitionsWithBlockSizes`.
- This also conflicted with the parent phase criterion to audit remaining placeholder
  union data shapes.

#### Rework

- Added `_set_partitions_base(...)` as the closed runtime dispatch point for the three
  admitted shapes.
- Integer-cardinality input is recognized by Sage's `Integer` type and adds the
  finite-totally-ordered-base refinement.
- Existing set-object input is recognized by Sage `CategoryObject` plus membership in
  `Sets()`.
- Finite iterable input is materialized as a tuple before delegation to Sage.
- Other input shapes now raise `TypeError` instead of falling through to Sage's broad
  constructor behavior.

### Re-review 2026-05-07 (Lorentz)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- Confirmed the grounding cites Sage inventory, mapping, style authority, owner, and
  return-object data.
- Confirmed `_set_partitions_base(...)` dispatches over the three admitted cases:
  Sage `Integer`, Sage `CategoryObject` with membership in `Sets()`, and finite
  iterable materialized as a tuple. Other inputs raise `TypeError`.
- Confirmed the three public set-partition constructors call the helper before Sage
  delegation.
- Confirmed the rework tightens dispatch and adds review evidence without narrowing
  smokes or weakening the `Set(X)` rejection.
- Confirmed smoke coverage includes all three partition base shapes.
- Confirmed no `*args`, `**kwargs`, public option bag, or generic `Set(X)` surface was
  introduced.

#### Residual Risk

- Re-review relied on the local validation recorded above rather than rerunning the
  validation commands independently.
