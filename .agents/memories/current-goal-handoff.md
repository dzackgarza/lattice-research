---
title: Current Goal Handoff
---

# Handoff

## Current Phase

Category-spec vocabulary.
The purpose is to give later lattice and Coble work precise mathematical objects,
morphisms, constructions, and invariants.

## Next Work

Do not continue Sage inventory or mapping from subtree docs alone.
Start with `[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]` and populate its
source-grounded primary universe `U_math` for the active scope before reporting any
mathematical mapping progress.

For the active lattice task, the first work product is a generated finite symbol
universe `U_lattices_math`, not another handoff pointer or one-cluster mapping patch.
Populate it from the lattice Sage-source frontier, then classify rows through
`Remaining_lattices_math`.

Compatibility, runtime, display, private, test-helper, package-export, and backend rows
are a separate audit lane. Do not count them as progress on the mathematical foundation
unless they block a named implementation or spec obligation.

The previous concrete audit target remains lattice Hom and morphism evidence, but it is
now subordinate to the frontier ledger.
When the ledger has the relevant rows, continue the Sage inventory and mapping audit for
`category_specs/lattices` from these evidence files:

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
