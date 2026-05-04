---
name: lattice-redesign
description: Use when working on the lattice redesign, ModulesWithForms, lattice DSL semantics, dual/discriminant descent, bilinear/quadratic module categories, or orthogonal/Coxeter layers.
---

# Lattice Redesign

This skill owns the canonical lattice-redesign source doctrine migrated from the retired `plans/` directory.

## Load references by task

- `references/category-abc-spec.md`: load for `ModulesWithForms`, form codomains, parent/element/morphism methods, homsets, tensor/cartesian/dual objects, cokernels, discriminant descent, and named downstream categories.
- `references/lattice-interface-style-guide.md`: load before editing or reviewing lattice APIs, public mathematical vocabulary, morphism semantics, discriminant groups, orthogonal groups, predicates, validation, or anti-wrapper compliance.
- `references/lattice-redesign-corrections-spec.md`: load when resolving design disputes, interpreting user corrections, or checking non-negotiable preservation/source-of-truth rules.

## Hard rules

- The spec is the target; incomplete implementation is not evidence that the spec is stale.
- Use noun-owned mathematical APIs, not helper-function piles.
- Treat lattices as presented modules with forms. Changing generators or basis data
  produces a distinct but possibly isometric object, not the same object.
- Do not import Sage's ambient-vector-space lattice convention into public semantics.
- Dual and discriminant semantics must route through real categorical objects and morphisms.
- Do not preserve compatibility shims unless explicitly requested.
