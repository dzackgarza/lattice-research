---
id: SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MAPPING-LATTICES]]'
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
title: Define discriminant-form isotropic orbit objects
status: in-progress
priority: medium
requirement: 'The Coble cusp and discriminant-orbit arguments require finite
  discriminant-form objects, their automorphism groups, isotropic subsets, finite orbit
  sets, stabilizers, and the separate lattice-lifting theorem or algorithm that relates
  discriminant-form orbits to primitive isotropic lattice vectors.'
acceptanceCriteria:
- Each object or operation is stated as a mathematical claim with category/refinement,
  hypotheses, witnesses, codomain or return object, and source evidence.
- The finite formed-module objects are separated from lattice-level lifting and
  primitive-isotropic orbit theorems.
- The spec does not promise generators, presentations, or full lattice orbit algorithms
  unless the stronger group category or backend witness is named.
- Sage TorsionQuadraticModule, QuadraticForm, GAP, Oscar, Hecke, and stored Dawes or
  building evidence are used only as implementation witnesses for the stated
  mathematical operations.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Spec: Discriminant-Form Isotropic Orbit Objects

## Relationship to existing specs

Phase 4 (PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT) already specifies
discriminant-group methods: `b(x,y)`, `q(x)`, `invariants()`, `cardinality()`,
`isotropic_elements()`, `elements_of_norm(n)`, `is_isometric_to(other)`,
`isomorphic_as_groups(other)`, `is_p_elementary(p)`, `p_rank(p)`, `value_map()`.

These operations give the finite torsion module `A`, the quotient-valued quadratic
form `q: A -> Q/2Z`, and the subset of isotropic elements.  The remaining mathematical
objects needed for cusp and orbit computations are:

- the automorphism group `O(A,q) = Aut_{TorsionQuadraticModules}(A,q)`;
- the action of `O(A,q)` or a specified subgroup `G <= O(A,q)` on the finite set `A`;
- the finite subset `Iso(A,q) = {a in A : q(a) = 0}`;
- orbit sets such as `Iso(A,q)/G` and `{a in A : q(a)=n}/G`;
- stabilizers `Stab_G(a)` or `Stab_G(S)` for elements or subgroups;
- the separate lattice theorem or algorithm relating a discriminant class to primitive
  isotropic vectors in a lattice with discriminant form `(A,q)`.

## Mathematical Claims

### Discriminant Orthogonal Group

For a finite torsion quadratic module `(A,q)`, the orthogonal group

`O(A,q) = Aut_{Modules(ZZ).WithForms().Quadratic().Torsion()}(A,q)`

is the group of automorphisms of the underlying finite abelian group preserving `q`
and the associated bilinear form where present.

Weakest category:
`Modules(ZZ).WithForms().Quadratic().Torsion().AutCategory()`.

Witnesses:
finite torsion module presentation, quotient-valued quadratic form, and a certified
automorphism or stronger finite/generated group representation when generator methods
are claimed.

Computational consequence:
membership of a proposed automorphism is checkable by finite abelian group
automorphism data plus form preservation.  Methods such as `gens()`,
`presentation()`, or a concrete matrix-group return are valid only for a refinement
whose construction supplies generator or presentation witnesses.

### Isotropic Elements and Norm Fibers

For a finite torsion quadratic module `(A,q)`,

`Iso(A,q) = {a in A : q(a) = 0 in Q/2Z}`

is a finite subset of `A`.  More generally, for a value `n in Q/2Z`,

`A_n = {a in A : q(a) = n}`.

Weakest category:
finite torsion quadratic modules with an enumerable finite carrier.

Witnesses:
finite presentation of `A`, value codomain for `q`, exact equality in `Q/2Z`, and
enumeration of the finite carrier or a source-backed finite subset constructor.

### Orbit Sets and Stabilizers

For a subgroup `G <= O(A,q)` acting on a finite subset `X <= A` preserved by `G`, the
orbit set

`X/G`

is a finite quotient set.  For `x in X`, the stabilizer is

`Stab_G(x) = {g in G : g(x) = x}`.

Weakest category:
finite group actions when `G` is finite with an enumerable or generated action; lazy
group-action objects when `G` is only defined by predicates and membership witnesses.

Witnesses:
the subgroup inclusion `G <= O(A,q)`, a certified action on `A`, proof or check that
`X` is `G`-stable, and finite enumeration or generator witnesses when orbit
representatives are requested.

Public consequences:
`isotropic_orbits()` is shorthand for `Iso(A,q)/O(A,q)` only when the chosen
orthogonal-group realization supplies the finite action data needed to enumerate
orbits.  Otherwise the spec should expose the orbit object and membership/equality
claims without promising representatives.

### Lattice Lifting

Let `L` be an even nondegenerate integral lattice with discriminant form `(A_L,q_L)`.
The natural homomorphism

`O(L) -> O(A_L,q_L)`

is a group homomorphism induced by the action on `L^#/L`.  Its kernel is the stable
orthogonal group `\widetilde O(L)`.

A statement that a discriminant-form orbit lifts to a class of primitive isotropic
lattice vectors is not an operation on `A_L` alone.  It is a lattice-level theorem or
algorithm requiring hypotheses such as Nikulin surjectivity, Eichler-type
transvections, stable-plus subgroup data, or a named backend for primitive-isotropic
orbit computation.

Weakest category:
lattices with discriminant descent plus a specified orthogonal subgroup/refinement.

Witnesses:
the lattice `L`, the discriminant descent `L -> L^# -> A_L`, the subgroup of `O(L)`,
the image subgroup in `O(A_L,q_L)`, and the theorem or backend that identifies the
lattice orbit with the finite discriminant-form orbit.

## Implementation Evidence To Check

- Sage: `TorsionQuadraticModule.orthogonal_group()` (or
  `QuadraticForm.automorphism_group()`) only if it supplies the finite formed-module
  automorphism group with a basis/presentation map back to `A`.
- Sage: finite abelian-group and finitely presented module enumeration for the carrier
  of `A`.
- GAP: finite group actions and orbit/stabilizer computation once a generated finite
  action on `A` is available.
- Oscar/Hecke: discriminant-form orthogonal-group and spinor-norm routines when they
  return exact formed-module automorphism witnesses.
- Stored theory: `theory-orbit-and-building-backends`, `theory-backend-routing`, and
  `theory/foundations/reflective-two-elementary-lattices.md` for the distinction
  between finite discriminant-form orbits and lattice-level stable/plus orbit
  algorithms.

## Non-Goals

- Do not re-specify the discriminant group's bilinear/quadratic form evaluation (Phase 4).
- Do not specify lattice-level isometry backends as methods on the finite discriminant
  object.
- Do not identify `O(A,q)` with a matrix group carrying generators unless the chosen
  realization actually supplies that stronger finite generated group data.
- Do not implement orbit enumeration from first principles before surveying existing
  finite-group orbit methods in GAP/Sage/Oscar.

## Current Missing Evidence

This card is not complete until the implementation evidence above is source-mined into
ordinary mathematical operation rows.  In particular, the next source-backed rows must
settle:

- whether Sage has a direct `TorsionQuadraticModule` automorphism-group constructor for
  quotient-valued finite forms, or only lower-level finite-module and quadratic-form
  ingredients;
- how a Sage or backend automorphism-group representation acts on the project
  discriminant-group elements;
- which finite orbit and stabilizer operations are inherited from finite group actions;
- which lattice-level lifting claims require Nikulin surjectivity, Eichler
  transvections, stable-plus hypotheses, or a named building/orbit backend.
