---
title: What Category Specs Actually Is — The One-Sentence Purpose
date: 2026-05-27
status: active
---
# What Category Specs Actually Is

## The one-sentence purpose

`category_specs` is a **complete, source-grounded mathematical category hierarchy**
where every method is owned by the largest category on which it makes sense, and
subcategories refine via internal `@override` on `ParentMethods` / `ElementMethods` /
`SubcategoryMethods`.

## What this means

### Internal hierarchy, not Sage wrapper

The category graph is **self-contained** and **internal**. It does not depend on Sage
stubs, Sage categories, or Sage method containers for its inheritance structure.

- `_NumberFields.ParentMethods.degree` exists because the spec defines it there.
- `_QQ.ParentMethods.degree` has `@override` because `_QQ` is a subcategory of
  `_NumberFields` in the local graph.
- The fact that `sage.rings.rational_field.RationalField` also has a `degree` method is
  **irrelevant** to the internal override chain.

### Sage interop is ONLY at constructor boundaries

The only place where Sage runtime API matters is in **constructors**:

- `Rings().Constructors()` calls `QQ`, `GF`, `NumberField`, etc., then refines the
  result into a local category.
- `Sets().Constructors()` calls `FiniteEnumeratedSet`, `IntegerRange`, etc., then
  refines.
- `Modules(R).Constructors()` calls `FreeModule`, `VectorSpace`, etc., then refines.

After the constructor boundary, the object lives in the internal spec surface.
Its method obligations are owned by the internal category graph, not by Sage stubs.

Refinement at that boundary is a declaration that an existing Sage object is being
viewed inside the local category universe as an object of a more specific project
category. It imports the Sage object as a partial implementation of the project spec:
concrete Sage providers may satisfy declared abstract obligations, while missing
obligations must remain visible through instantiation or smoke failure. Refinement is
not the implementation phase and must not hide the gap between current Sage behavior
and the ideal spec.

### The plugin exists to bridge static and dynamic inheritance

Sage's runtime method-container inheritance (`C.ParentMethods` injected dynamically) is
invisible to mypy. The plugin (`SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`) is designed to make
`C.ParentMethods @override` pass by projecting the semantic ancestry that Sage computes
at runtime.

If an `@override` on `C.ParentMethods` fails, the first question is **never** "is the
Sage stub missing this method?"

The first question is: **"Does the base method exist in an internal ancestor
`ParentMethods` class?"**

- If yes: plugin work or graph work.
- If no: spec work (the method is missing from the intended owner category).
- Only if the failing expression is a direct Sage API call: stub work.

## What this is NOT

`category_specs` is NOT:
- A consumer of Sage stubs for internal inheritance.
- A replacement for Sage's category system (it runs parallel to it).
- A project whose mypy errors are automatically evidence for stub work.
- A system where removing `@override` markers is an acceptable fix.

## The test for any analysis

Before working on any mypy error in `category_specs`, ask:

1. Is the error on an internal method container (`ParentMethods`, `ElementMethods`,
   `SubcategoryMethods`)?
2. If yes, does the base method exist in another internal `category_specs` file?
3. If yes, the error is plugin or graph work — never stub work.
4. If no, the error is spec work — the method is missing from its intended owner
   category.
5. Only if the error is on a direct Sage constructor call or import is it stub work.

If you find yourself discussing stubs, sidecars, or Sage method containers in the
context of an internal `@override` error, you have lost the plot.

## The mathematical coherence test

Before accepting any category graph or method ownership as correct, step back and ask:

**"Does this make sense mathematically?"**

- Does `NumberFields` inherit directly from `Fields` when it should inherit from
  `GlobalFields`? Is the intended chain `NumberFields <= GlobalFields <= Fields` encoded
  correctly?
- Does `_QQ` list redundant direct ancestors (`_Fields`, `_NumberFields`,
  `_GlobalFields`) when it should only list immediate parents?
- Is `QuotientFields` the right name for fraction fields/localizations?
  (No — it is not.)
- Does a method like `degree` belong on `_QQ` or on `_NumberFields`? (The largest
  category on which it makes sense.)

Agents in the past have been so focused on plugin behavior, stub coverage, and ledger
counts that they accepted mathematically incoherent structures without question.
They saw `_QQ.super_categories()` return five direct parents and analyzed it as a
"plugin visibility problem" instead of recognizing it as a graph design problem.

**If the graph is mathematically wrong, no amount of plugin work or stub work will fix
it.**

The mathematical structure is the foundation.
The plugin and stubs are implementation details.
Never optimize implementation details while ignoring mathematical incoherence.

## Category specs must converge toward usable mathematical vocabulary

`category_specs` is not complete because many cards exist or many abstract classes
type-check. It is complete only insofar as it gives downstream research code the
correct nouns, operations, coercions, morphisms, and obligations.

Do not expand `category_specs` horizontally unless the expansion supports a concrete
mathematical vocabulary needed by the current research phase.

Specs may declare operations that Sage already implements. The spec obligation records
the mathematical contract; the Sage method is only a possible concrete provider for
refined Sage objects. Do not remove, weaken, or move an abstract obligation merely
because an existing Sage category or parent has a method with the same name.
