---
title: Lattice Interface Style Guide
status: active
date: 2026-05-29
---
# Lattice Interface Style Guide

Lattice-specific code conventions for the `src/lattices/` hierarchy.

## Design Goal: A Mathematical DSL

The goal is a domain-specific language for lattice theory in algebraic geometry.
The standard for usability: can the code be read aloud as the corresponding paragraph in
a paper?

## The Sage module ecosystem being replaced

Sage has multiple largely incompatible hierarchies for finitely generated modules and
lattices, none suited for general indefinite lattice theory:

| Module | Role | Limitation |
| FreeModule | Free R-modules | No bilinear form |
| FGP_Module | Finitely generated modules over PIDs | No form |
| FiniteRankFreeModule | Tensor calculus over arbitrary rings | No inner product |
| CombinatorialFreeModule | Combinatorially indexed free modules | No bilinear form |
| QuadraticForm | Quadratic forms over ZZ/QQ | Assumes positive-definite |
| TorsionQuadraticModule | Torsion quadratic modules | Separate hierarchy |

**The definiteness trap.** Most Sage lattice/form code was written for definite forms.
It was never validated against indefinite inputs.
Code that "happens to work" on indefinite forms is an accident.

## Core development principles

- Use noun-owned mathematical APIs, not helper-function piles.
- Treat lattices as presented modules with forms.
- Do not use Sage's ambient-vector-space convention.
- Dual and discriminant semantics route through real categorical objects.
- Indefinite forms are the primary target.
- Validate all algorithms against indefinite inputs.
- No optional arguments that silently change mathematical semantics.
- Backend isolation: Sage/Julia/GAP are calculation engines, not the public API.

## Bad patterns to avoid

- Helper functions for dead simple Sage one-liners.
- `hasattr` instead of proper typing.
- `pass` stubs instead of real ABCs.
- Hardcoding `ZZ` at levels where general `R` is specified.
- Returning `None` from mathematical operations.
- `inclusion_matrix` (not mathematically well-defined without embedding data).
- `projection_matrix` (not in the spec).
- Making things `Optional` when they should always be defined.
- Raw `diagonal_matrix()` when semantic constructors exist.
