---
title: Research Math Boundary Reference
status: active
date: 2026-05-29
---
# Research Math Boundary Reference

## Current lattice/module redesign plan

Durable planning lives under the modules-with-forms feature in root `.agents/plans/`. If
the task touches `src/lattices/`, `tests/lattice_spec/`, or `tests/sage_spec/`, read the
relevant plan/skill before acting.
Dependency order: foundational rings/fields/finitely generated module semantics →
bilinear-module category and nouns → lattice/dual/discriminant specializations →
orthogonal/root/Weyl/Coxeter/Eichler and indefinite-isometry work → final
human-in-the-loop spec revision.

## Existing software first

Mathematical implementation starts by checking whether a mature open-source backend
already implements the operation.
Canonical workflow: `research-software-wiring` skill plus
`theory/backends/software-capability-map.md`.

## Shared code boundary

Trusted shared code must be a semantic mathematical base.
Required public vocabulary: `FreeBilinearModule`, `FreeBilinearModuleElement`,
`Lattice`, `LatticeElement`, `LatticeMorphism`, `DiscriminantGroup`,
`DiscriminantGroupElement`, `DiscriminantGroupMorphism`.

Constructors, coercions, exact transforms, predicates, and invariant extractors live on
these nouns as methods.
If a public operation takes a lattice, lattice element, discriminant group, or morphism
as its primary argument, that is a design smell.
Attach the verb to the noun.

Raw matrices, vectors, dicts, and lists may appear inside implementations and backend
bridges, but they are not the public mathematical vocabulary.
Do not expose nonmathematical Sage infrastructure names such as `Parent` or `Element` as
the public return type of mathematical surfaces.

Good shared interfaces include canonical constructors such as
`Lattice.hyperbolic_plane()`, exact methods such as `lattice.discriminant_group()` or
`element.inner_product(other)`, and exact transforms such as `morphism.image()`.

Bad shared interfaces include task-shaped helpers like `assert_primitive_embedding`,
wrapper aliases like `lattice_determinant(L)`, free functions like `norm(v, L)`, and
`verify_*` functions that silently absorb mathematical burden.

## Argument-level boundary

The same boundary applies to mathematical prose and computational proof artifacts.
A claim should be expressible as a chain of public mathematical objects and morphisms,
not as a pile of representations with prose wrapped around it.
