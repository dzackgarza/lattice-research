---
name: category-spec-style
description: Use when editing, reviewing, or authoring category specs, type surfaces,
  Sage wrappers, constructors, method ownership, smoke files, or category-spec implementation
  code.
---

# Category Spec Style

This skill is the canonical agent-facing style authority for category-spec mathematical and implementation compliance.

## Canonical source

The source of truth is this skill plus `references/style.md`.

Read `references/style.md` before acting on category-spec content, code, specs, smoke files, or compliance questions.

## Use this skill for

- Type signatures, overloads, and variadic Sage surfaces.
- Standard type packages and `types.py` ownership.
- Category, object, element, morphism, Hom, End, and Aut surfaces.
- Constructor admission and named constructor design.
- Sage wrappers and interop boundaries.
- Smoke files and compliance checks.
- Minimal indirection, anti-slop, and mathematical ownership review.

## Hard reminders

- The spec defines a Sage-grounded, feasibility-classified mathematical interface inside
  Sage's category/object universe, not an unconstrained ideal API.
- Current Sage coverage is not automatically the adequacy standard, but exact
  feasibility is an admission constraint. Sage interop remains a design constraint:
  refined Sage objects should remain usable by existing Sage code when mathematically
  appropriate.
- Use Sage as implementation evidence and a feasibility witness: preserve inventoried
  Sage functionality, avoid unimplementable wishlists, and add mathematically required
  surfaces that Sage lacks only with an admission status: Sage-backed, backend-backed,
  bounded local extension, or deferred research algorithm.
- Specced vocabulary must exist before implementation proceeds.
- Mathematical definitions are foundational; do not treat them as ordinary code style.
- A spec row is a mathematical claim before it is a Sage/source-map row. If it cannot
  be stated coherently in mathematical language, it is not grounded.
- For methods, ownership means the category of objects on which the operation is
  defined. The category of the constructed result is codomain/target data, not by
  itself the method owner.
- Every spec claim must be grounded in a canonical mathematical source before edit:
  repo theory, references, spec backups, Sage written docs/source, or an approved
  decision card. A migrated TODO/card is provenance only, not definition authority.
- If a term has multiple plausible meanings, or if an invariant/equivalence needs a
  proof or hypotheses, stop the leaf and route a decision/source-mining card instead of
  guessing the familiar meaning.
- Complexity belongs behind mathematical nouns, not helper sprawl.
- Do not weaken specs to make current code pass. A smoke failure usually records an
  implementation, wrapper, or deferred-algorithm gap against the admitted spec.
- A typing fix is a proof obligation, not a way to quiet mypy. Before changing an
  annotation, adding a cast, or narrowing a return, ask whether the change makes the
  mathematical surface more explicit. If the code already expresses the correct Sage
  category structure and the checker only fails to see dynamic inheritance,
  `category_of`, `_with_axiom`, `refine_category`, or method-container projection,
  the fix belongs in the static model, plugin, stub, or QC tooling lane, not as a
  local cast-only patch.
- Do not rewrite specs unless the user explicitly requests that exact edit.

## Required output behavior

When a task reveals a missing definition, incorrect ownership boundary, Sage-mapping ambiguity, or style violation, do not patch around it silently. Route it to the project workflow by loading `category-spec-workflow` and either creating a real tracked card, adding a TODO scratchpad note, or requesting a human decision.
