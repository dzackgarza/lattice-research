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
Start with `[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]` and perform semantic extraction
from the relevant Sage method body/docs/examples before reporting any mathematical
mapping progress. The first question is what behavior Sage actually implements. Then
introduce the required vocabulary, weakest structure, hypotheses, and owner.

The constructor/factory batch currently populated in the frontier ledger covers
`FreeQuadraticModule`, `QuadraticSpace`/`InnerProductSpace`, `IntegralLattice`,
`IntegralLatticeDirectSum`, `IntegralLatticeGluing`, `TorsionQuadraticForm`, and
`TorsionQuadraticModule`.
Do not redo these rows.
For any future constructor work, derive new constructor names from scoped source
artifacts and add source-read frontier rows before claiming movement.

Compatibility, runtime, display, private, test-helper, package-export, and backend rows
are a separate audit lane. Do not count them as progress on the mathematical foundation
unless they block a named implementation or spec obligation.

The concrete next lattice audit target is Hom and morphism evidence, subordinate to the
frontier ledger.
Continue the Sage inventory and mapping audit for `category_specs/lattices` from these
evidence files:

- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`

The active local repair target is the Hom and morphism block around
`FreeModuleHomspace`, `FreeModuleMorphism`, and inherited `MatrixMorphism`.
Then continue the broader semantic-extraction audit of lattice/form/module method
clusters.

## Mapping Rule

Read Sage behavior before choosing the mathematical vocabulary. Do not accept a mapping
row until it contains both a behavior statement grounded in body/docs/examples and a
sentence a mathematician can read without knowing Sage.

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

Only after the behavior record and mathematical sentence are present should the row
assign a project owner.

## Current Decisions

- `SPEC-MAPPING-LATTICES` is the routing source for lattice, module, torsion, Homset,
  and form-adjacent Sage names.
- `IntegralLattice`, `IntegralLatticeDirectSum`, and `IntegralLatticeGluing` are the
  admitted `Lattices(ZZ).Constructors()` names and have classified frontier rows.
- `FreeQuadraticModule` is forms/module-owned, not a lattice constructor;
  `QuadraticSpace`/`InnerProductSpace` is the field-valued free bilinear wrapper, not a
  lattice constructor.
- `TorsionQuadraticForm` and generic `TorsionQuadraticModule` are forms-owned torsion
  quadratic constructors. They become lattice discriminant-group constructions only
  through explicit lattice metric-dual descent `A_L = coker(L -> L^#)`.
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
