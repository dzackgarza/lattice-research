---
title: Current Goal Handoff
---
# Handoff

## Current Phase

Category-spec vocabulary. The purpose is to give later lattice and Coble work precise
mathematical objects, morphisms, constructions, invariants, category refinements, and
witness data grounded in Sage/source evidence.

## Next Work

Next mathematical obligation: produce the implementation witness for the finite-action
conversion used by discriminant-form orbit computation.  For a typed finite subset
`X <= A` of a finite torsion quadratic module `(A,q)` and a certified generated
subgroup `G <= O(A,q)`, the code or source-backed design must define the bijection
between elements of `X` and finite action labels, prove each generator preserves `X`,
and convert orbit/stabilizer backend output back to elements of `A` and subgroups of
the original generated `G`.

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
  methods; the spec now states the bounded construction from finite carrier, generated
  group, and certified action.
- `PermutationGroup.orbit`, `PermutationGroup.orbits`, and
  `PermutationGroup.stabilizer` are Sage/GAP implementation evidence only after the
  typed conversion to and from the finite permutation/action domain is specified.

The lattice lifting statement has been separated from the finite formed-module orbit
claims.  The spec now states:

```text
For primitive v in L with div(v)=d, the class v/d + L lies in A_L; if v^2=0,
that class is isotropic.  O(L)-equivalence implies equivalence of these classes
under im(O(L)->O(A_L,q_L)).  The converse requires a checked Nikulin/Eichler theorem
or a named primitive-isotropic orbit backend.
```

Controlling source evidence for the next obligation: `sage/groups/fqf_orthogonal.py`
for `ActionOnFqf`, `sage/groups/perm_gps/permgroup.py` for finite orbits and
stabilizers through GAP-backed permutation actions, `sage/modules/torsion_quadratic_module.py`
for `TorsionQuadraticModule.orthogonal_group()`, and the finite-action rows in
`[[SPEC-MAPPING-LATTICES]]` and `[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]`.

Success condition: the project has a source-backed operation row or implementation
design for the conversion
`X <-> finite action labels`, the generator-stability check for `X`, and the return
conversion from backend orbits and stabilizers to discriminant-form elements and
subgroups of `G`.  Raw GAP tuples, Smith-coordinate lists, or permutation labels must
not be public return objects.

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
