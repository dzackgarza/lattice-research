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

- Specced vocabulary must exist before implementation proceeds.
- Mathematical definitions are foundational; do not treat them as ordinary code style.
- Complexity belongs behind mathematical nouns, not helper sprawl.
- Do not weaken specs to make current code pass.
- Do not rewrite specs unless the user explicitly requests that exact edit.

## Required output behavior

When a task reveals a missing definition, incorrect ownership boundary, Sage-mapping ambiguity, or style violation, do not patch around it silently. Route it to the project workflow by loading `category-spec-workflow` and either creating a real tracked card, adding a TODO scratchpad note, or requesting a human decision.
