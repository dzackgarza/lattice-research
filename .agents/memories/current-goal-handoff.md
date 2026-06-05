---
title: Current Goal Handoff
---
# Handoff

## Current Phase

Category-spec vocabulary. The purpose is to give later lattice and Coble work precise
mathematical objects, morphisms, constructions, invariants, category refinements, and
witness data grounded in Sage/source evidence.

## Next Work

Next mathematical obligation: state the lattice-level lifting claims relating finite
discriminant-form orbits to primitive isotropic lattice vectors. Do not treat this as a
method on the finite discriminant group alone.

The finite formed-module side now has source-backed rows in
`[[SPEC-MAPPING-LATTICES]]` and `[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]`:

- `O(A,q)=Aut(A,q)` for Sage torsion quadratic modules is realized by
  `TorsionQuadraticModule.orthogonal_group()` and `FqfOrthogonalGroup`.
- Supplied generators define generated subgroups of `O(A,q)` after coercion to finite
  abelian-group automorphisms.
- The full Sage group is computed by `_isom_fqf(A)` as a slow brute-force finite
  search over form-compatible images of Smith generators.
- `ActionOnFqf` supplies the right action on `A` and invariant subquotients.
- `FqfOrthogonalGroup` does not expose public `orbit`, `orbits`, or `stabilizer`
  methods; orbit/stabilizer enumeration must be specified as a bounded local
  construction from finite carrier, generated group, and certified action, or as an
  explicit GAP conversion.

The next source-backed statement should classify the lattice lifting problem:

```text
For an even nondegenerate integral lattice L with discriminant form (A_L,q_L),
the natural homomorphism O(L) -> O(A_L,q_L) has kernel ~O(L).
A claim that a finite discriminant-form orbit corresponds to primitive isotropic
vectors in L requires additional hypotheses or algorithms: Nikulin surjectivity,
Eichler transvections, stable-plus subgroup data, finite quotient image data, or a
named building/isotropic-orbit backend.
```

Controlling source evidence: use
`theory/foundations/reflective-two-elementary-lattices.md`,
`theory/foundations/coble-task-background.md`, `theory-orbit-and-building-backends`,
`bilinear-form-category-semantics`, `SPEC-MAPPING-LATTICES`, and
`SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` before editing code or specs.

Success condition: the spec states exactly which discriminant-form orbit claims are
finite formed-module statements, which are lattice-level theorems, and which require
backend/literature algorithms. No method should be placed on `A_L` merely because the
theorem mentions discriminant classes.

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
- `TASK-FORMED-COKERNEL-DESCENDED-FORM` stays closed unless new source contradicts its formed-cokernel construction.
- `stable_orthogonal_group()` denotes `~O(L)=ker(O(L)->O(A_L,q_L))`, not `O^+(L)`.
  `O^+(L)` is the real-spinor-kernel subgroup.
- `SO(L)`, `~O(L)`, `O^+(L)`, `SO^+(L)`, `~SO(L)`, and `~SO^+(L)` are distinct
  subgroup objects in the lattice Aut mapping; generator methods remain absent unless a
  stronger finite/generated/backend refinement supplies witnesses.

## Non-Goals

- Do not turn Sage implementation classes into method owners.
- Do not add lattice methods merely because lattice code uses them.
- Do not record progress as complete unless the relevant Sage behavior has a
  source-backed operation row, a one-line residue classification, or an unresolved
  mathematical question.
- Do not use this handoff as a changelog. The mapping spec and git history carry past
  work.
