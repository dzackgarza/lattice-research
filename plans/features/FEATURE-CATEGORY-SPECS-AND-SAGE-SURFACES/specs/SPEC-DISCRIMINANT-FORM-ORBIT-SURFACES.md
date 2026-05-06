---
id: SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MAPPING-LATTICES]]'
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
title: Spec discriminant-form isotropic orbit method surfaces
status: needs-review
priority: medium
requirement: 'The lattice spec lists nikulin_invariants() but the isotropic orbit
  analysis (Tasks 2.1-2.2, FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION) requires the full
  discriminant form and orbit computation in the finite discriminant group. Specify
  the missing method surfaces on DiscriminantGroup that support: (a) the full discriminant
  form q_T: A -> Q/2Z, (b) the orthogonal group O(A,q) and its action on A, (c) orbit
  enumeration of isotropic elements under O(A,q), (d) orbit representatives and their
  lifts to the lattice.'
acceptanceCriteria:
- Every method required by the orbit classification is placed at the correct category
  level (discriminant group, torsion quadratic module, or lattice).
- Sage sources TorsionQuadraticModule, QuadraticForm, and Oscar/Hecke discriminant-form
  APIs are surveyed as implementation evidence.
- The surface does not duplicate methods already specified in SPEC-MAPPING-FORMS or
  Phase 4 discriminant-group tasks.
- The orbit enumeration methods distinguish finite-group orbits (Burnside) from lattice-level
  orbits (spinor norm/Eichler).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Spec: Discriminant-form isotropic orbit method surfaces

## Relationship to existing specs

Phase 4 (PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT) already specifies
discriminant-group methods: `b(x,y)`, `q(x)`, `invariants()`, `cardinality()`,
`isotropic_elements()`, `elements_of_norm(n)`, `is_isometric_to(other)`,
`isomorphic_as_groups(other)`, `is_p_elementary(p)`, `p_rank(p)`, `value_map()`.

These methods give the quadratic form q: A -> Q/2Z and the set of isotropic elements,
but they do NOT provide:

1. **The orthogonal group O(A, q)** — generators or the full matrix group of
   automorphisms of the finite quadratic form.
2. **Orbits of isotropic elements under O(A, q)** — orbit decomposition, orbit
   representatives, stabilizer sizes.
3. **The spinor norm kernel** — the connecting homomorphism O(T) -> O(A_T, q_T) and its
   image, needed for lifting orbits from the discriminant group to the lattice.

## Method surfaces to add

These methods should be specified on the `DiscriminantGroup` (or `TorsionQuadraticForm`)
object, which is a `ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()` object:

### 1. Discriminant orthogonal group

```
D.orthogonal_group() -> MatrixGroup
    The finite group O(D, q_D) of automorphisms of the discriminant quadratic form.
    Backend: Sage QuadraticForm.automorphism_group() or Oscar/Hecke.
    Returns generators as a matrix group over Z (acting on the invariant-factor basis).
```

### 2. Isotropic orbit decomposition

```
D.isotropic_orbits() -> list[Orbit]
    Orbit decomposition of the set {x in D : q(x) = 0} under O(D, q).
    Each Orbit records a representative element, stabilizer subgroup, and size.
```

### 3. General norm-orbit decomposition

```
D.orbits_of_norm(n) -> list[Orbit]
    Orbit decomposition of {x in D : q(x) = n (mod 2Z)} under O(D, q).
    Specialized for n=0 by isotropic_orbits() when n=0.
```

### 4. Orbit lifting

```
D.lift_orbit_to_lattice(orbit_rep, lattice) -> IsometryClass
    Given an O(q_T)-orbit representative in A_T, produce the set of primitive
    isotropic vectors in T with that discriminant class, up to O*(T).
    Requires: Nikulin surjectivity (or backend), spinor norm computation.
```

## Implementation evidence needed

- Sage: `TorsionQuadraticModule.orthogonal_group()` (or
  `QuadraticForm.automorphism_group()`)
- Sage: `QuadraticForm.automorphism_group()` for computing O(q) on finite forms
- Oscar/Hecke: `orthogonal_group` on discriminant forms, orbit methods
- GAP: `SO`, `GO` on finite quadratic forms, `OrbitsDomain` for group actions

## Non-Goals

- Do not re-specify the discriminant group's bilinear/quadratic form evaluation (Phase 4).
- Do not specify lattice-level isometry backends (Phase 5).
- Do not implement orbit enumeration from first principles before surveying existing
  finite-group orbit methods in GAP/Sage/Oscar.
