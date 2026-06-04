---
title: Current Goal Handoff
---

# Handoff

## Current Phase

Category-spec vocabulary.
The purpose is to give later lattice and Coble work precise mathematical objects,
morphisms, constructions, and invariants.

## Next Work

Continue the Sage inventory and mapping audit for `category_specs/lattices`.
Start with these files:

- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`

The active local repair target is the Hom and morphism block around
`FreeModuleHomspace`, `FreeModuleMorphism`, and inherited `MatrixMorphism`.
Then continue the broader symbol-by-symbol audit of the lattice/form/module Sage
sources.

## Mapping Rule

Read Sage first to learn which names exist.
Then write the mathematics that makes each name exist.
Do not accept a mapping row until it contains a sentence a mathematician can read
without knowing Sage.

Examples:

- In any category, morphisms have domains and codomains and compose.
- In a concrete category, morphisms can be evaluated on elements.
- In an additive category, each `Hom(X,Y)` is an abelian group and composition is
  bilinear.
- In an `R`-linear category, each `Hom(X,Y)` is an `R`-module and composition is
  `R`-bilinear.
- In an abelian category, kernels and cokernels exist, images and coimages are defined,
  and monomorphisms and epimorphisms are detected by the corresponding kernel and
  cokernel conditions.
- `End(X)=Hom(X,X)` contains the identity endomorphism.
- `Aut(X)` is the group of invertible endomorphisms.
- A morphism has a matrix only after choosing finite free presentations or bases.

Only after that sentence is present should the row mention the Sage class or method that
implements the construction in one case.

## Current Decisions

- `SPEC-MAPPING-LATTICES` is the routing source for lattice, module, torsion, Homset,
  and form-adjacent Sage names.
- `IntegralLattice`, `IntegralLatticeDirectSum`, and `IntegralLatticeGluing` are the
  admitted `Lattices(ZZ).Constructors()` names.
- `invariants()` and `invariant_factors()` belong to finitely presented modules over a
  PID. Lattices and discriminant/torsion objects inherit them only through that module
  structure.
- `BinaryQF`, `BQFClassGroup`, and `TernaryQF` belong to forms or binary/ternary
  quadratic-form vocabulary, not to `Lattices(ZZ)` constructors.
- Package exports such as `sage.modules.all`, `sage.quadratic_forms.genera.all`, and
  `sage.geometry.all` are import evidence. They do not create mathematical owners.
- `TASK-FORMED-COKERNEL-DESCENDED-FORM` stays closed unless new source contradicts its
  formed-cokernel construction.

## Non-Goals

- Do not turn Sage implementation classes into method owners.
- Do not add lattice methods merely because lattice code uses them.
- Do not record progress as complete until the final semantic audit proves that every
  relevant Sage name is inventoried, mapped, mathematically owned, or explicitly rejected
  with a reason.
- Do not use this handoff as a changelog. The mapping spec and git history carry past
  work.
