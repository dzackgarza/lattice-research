---
title: How Category Spec Work Should Proceed — No Bureaucracy, Just Thinking
date: 2026-05-27
status: active
---
# How Category Spec Work Should Proceed

## The graph is a tree

The category inheritance poset should be **mostly a tree**.

- Root entry points (e.g., `Rings`, `Sets`) bridge to Sage.
- Everything below them should inherit through **one immediate local parent**, forming a
  chain.
- Multiple local supercategories are **suspicious** unless they genuinely introduce a
  mixed structure (e.g., a topological ring is both a ring and a topological space).

If a category lists multiple local parents, ask: is this a true intersection of
independent structures, or is one parent a consequence/ancestor of another?
If the latter, fix the graph.

## There are exactly three kinds of problems

When you see a mypy error in `category_specs`:

### 1. Real spec error

**Shape:** `@override` on a subcategory, but no parent category in the local graph
defines the method.

**Action:** Add the method to the correct parent category.
The spec is incomplete.

### 2. Plugin error

**Shape:** `@override` on a subcategory, and the parent category DOES define the method,
but mypy cannot see the inheritance edge.

**Action:** Write a minimal red test for the plugin.
The plugin needs to project the dynamic method-container inheritance into static
visibility.

### 3. True stub need

**Shape:** A direct call to Sage runtime API (constructor, import, explicit method call)
where `category_specs` cannot type the boundary without external type information.

**Action:** Add a stub to `sage-stubs` ONLY for that specific boundary call.

**Everything else is not a stub problem.**

## The stub surface is almost empty

The research repo has **total control** over output types.
`Cat().Constructors()` calls a Sage constructor and then `refine_category(...)` to cast
the result into the local spec surface.
After refinement, the object lives in the internal hierarchy.
Its methods are owned by the internal graph, not by Sage stubs.

Stubs are only needed for the **thin touchpoint** where the raw Sage object enters the
system. Even then, the stub surface should be derived from the explicit constructor
inventory, not from internal method-container diagnostics.

**The inventory of constructors is finite and known.** Collect them on
`Cat().Constructors()`. For each, inventory the exact Sage callable and the local
refined output type.
That is the complete stub surface.
Nothing else belongs in `sage-stubs`.

## How to audit the graph

1. Extract every `super_categories()` return in `category_specs/`.
2. Build the graph.
3. Flag every category with more than one **local** parent.
4. For each multi-parent category: is it a true mixed structure, or is the graph wrong?
5. Flag every category whose parents are not minimal (one parent is an ancestor of
   another).
6. Output a plain tree for human mathematical review.

This is not a complex tool.
It is a simple script.
Without it, the graph will accumulate absurdities.

## Organizational requirements

The repo currently has no clear way to answer these questions:
- What are all the constructors?
- What is the true error signal?
- What is the actual stub surface?

Fix this by making the constructor inventory the single source of truth.
Every constructor should be collected on `Cat().Constructors()`. Every boundary call
should be traceable to that inventory.
Every mypy error should be classified against the three problem types above.

## The anti-pattern

- Adding direct ancestors to make a method available locally instead of fixing the
  intermediate graph.
- Classifying internal `@override` errors as stub work.
- Inventing jargon to obscure simple truths.
- Producing strategy documents instead of concrete audits.
- Treating the ledger as a scoreboard rather than a diagnostic signal.

## The core principle

**Think.** Do not checkbox.
Step back and ask if the graph makes sense.
If it does not, fix the graph.
Do not add a workaround.
Do not suppress the error.
Do not write a document explaining why the absurdity is acceptable.
