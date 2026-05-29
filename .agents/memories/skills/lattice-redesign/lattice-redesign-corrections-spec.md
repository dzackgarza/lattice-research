---
title: Lattice Redesign Corrections Spec
status: active
date: 2026-05-29
---
# Lattice Redesign Corrections Spec

Durable preservation artifact for detailed user corrections.
The normalized design directives distilled from these corrections now live in
`lattice-interface-style-guide.md` and `category-abc-spec.md`.

## Non-Negotiable Preservation Rule

The generated redesign code must be reorganized and corrected, not discarded wholesale.
The correct procedure is: stub the intended hierarchy, migrate correct code into the
right files, remove dead code after verification, never discard wholesale.

## Key corrections preserved

- The spec is the target, not aspirational.
  A spec IS ahead of implementation by definition.
- Morphisms are not containers and do not have `perp`.
- Most methods belong at the `BilinearModules` level, not deeper.
- `BilinearModules(R)` is a new category emulating `sage.categories.modules.py`.
- Use `ModulesWithForms(R)` as the foundational contract.
- Objects are presented modules with form data.
  Changing generators produces a distinct object.
- `contains` is a parent check.
  `v = vector(ZZ, [1,0])` is NOT an element of `U`. Use `U.element_from(v)`.
- No `hasattr` — use proper typing.
- No `pass` stubs — define real ABCs.
- `gens()` is perfectly well-defined: n symbols that behave as elements.
- Discriminant descent through cokernel construction: `L -> L^* -> A_L`.
