---
title: Current Goal Handoff
---

# Handoff

## Current Phase

Category-spec vocabulary.
The purpose is to give later lattice and Coble work precise mathematical objects,
morphisms, constructions, invariants, category refinements, and witness data
grounded in Sage/source evidence.

## Next Work

Do not continue Sage inventory or mapping from subtree docs alone.
Start with `[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]` and perform semantic extraction
from the relevant Sage method body/docs/examples before reporting any mathematical
mapping progress. The first question is what behavior Sage actually implements. Then
introduce the required vocabulary, weakest structure, hypotheses, owner, return object,
category/refinement membership, and witness data.

The constructor/factory batch currently populated in the operation map covers
`FreeQuadraticModule`, `QuadraticSpace`/`InnerProductSpace`, `IntegralLattice`,
`IntegralLatticeDirectSum`, `IntegralLatticeGluing`, `TorsionQuadraticForm`, and
`TorsionQuadraticModule`.
Do not redo these rows.
For any future constructor work, derive new constructor names from scoped source
artifacts and add source-backed operation rows before claiming mathematical progress.

Compatibility, runtime, display, private, test-helper, package-export, and backend
methods are nonmathematical residue unless they change the mathematical interface or
block construction of a required spec object. Discard them after a one-line
classification.

The concrete lattice Hom and morphism evidence block is mapped in:

- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`

The `FreeModuleHomspace`, `FreeModuleMorphism`, inherited `MatrixMorphism`,
`FGP_Module_class.hom`, `_Hom_`, `FGP_Homset`, `FGP_Morphism`, formed `cokernel()`
descent, formed/lattice Aut, finite discriminant-form Aut, and
`O(L) -> O(A_L,q_L)` rows have split theorem-shaped mappings in
`SPEC-MAPPING-LATTICES`. Use those rows as the baseline; do not collapse them back into
Sage-class labels, raw matrices, generated-group algorithms, or backend summaries.

Next mathematical obligation:
For a group object acting on a typed object or finite set, state the exact orbit,
stabilizer, and centralizer constructions needed by the lattice/Coble pipeline.
The next mapping must distinguish:

- the subgroup definition `Stab_G(x) = {g in G | g.x = x}`;
- the centralizer definition `C_G(h) = {g in G | gh = hg}`;
- finite orbit enumeration for typed finite carriers such as isotropic elements of
  `A_L`;
- generated subgroup computation only when `G` has generator witnesses;
- lattice/discriminant specializations for `O(L)`, `O(A_L,q_L)`, typed polarization
  data, and involutions.

Controlling source evidence:
Read the Sage method bodies/docs/examples for `FqfOrthogonalGroup._get_action_`,
`ActionOnFqf`, the relevant GAP-backed finite group or matrix-group `orbit`,
`stabilizer`, and `centralizer` methods, and the current
`SPEC-MAPPING-LATTICES` finite-action rows before editing. Then state the weakest
category/refinement, hypotheses, witnesses, codomain or return object, and source
evidence for each operation.

Success condition:
The lattice mapping separates formal subgroup objects from finite/generated algorithms:
`Stab_G(x)`, `C_G(h)`, orbit sets, and orbit representatives are stated at the category
where they are defined, while explicit generators, finite enumeration, and GAP-backed
returns appear only under finite, generated, matrix-group, or project-specific
refinements with witnesses.

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
- `Aut(X)` is the group of invertible endomorphisms in the ambient category. It lies in
  `Groups`; generator methods belong only to finite-generation or generated-subgroup
  refinements.
- A morphism has a matrix only after choosing finite free presentations or bases.

Only after the behavior record and mathematical sentence are present should the row
assign a project owner.

## Current Decisions

- `SPEC-MAPPING-LATTICES` is the routing source for lattice, module, torsion, Homset,
  and form-adjacent Sage names.
- `IntegralLattice`, `IntegralLatticeDirectSum`, and `IntegralLatticeGluing` are the
  admitted `Lattices(ZZ).Constructors()` names and have source-backed operation rows.
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
- Do not record progress as complete unless the relevant Sage behavior has a
  source-backed operation row, a one-line residue classification, or an unresolved
  mathematical question.
- Do not use this handoff as a changelog. The mapping spec and git history carry past
  work.
