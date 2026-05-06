---
id: SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]'
title: Recover discriminant group and quotient-valued form surface
status: needs-review
priority: high
requirement: The discriminant object surface from src.bak must be recovered as a finite
  torsion formed-module quotient with explicit bilinear and quadratic structure.
acceptanceCriteria:
- A discriminant object constructed from a lattice records the source lattice, dual
  inclusion, quotient map, and descended form data.
- q and b evaluation, generators, cardinality, invariant factors, p-elementary checks,
  finite iteration, submodules, quotients, and orthogonal submodules are owned by
  the discriminant object or its category.
- Orthogonal groups of discriminant forms are Aut objects of the finite formed-module
  object, not raw Sage groups.
- Equality, isomorphism as groups, and isometry as forms are distinct public predicates.
complexity: 70
tags:
- FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY
---
# Recover discriminant group and quotient-valued form surface

## Source Provenance

- `src.bak/lattices/core/discriminant.py`: `DiscriminantGroup`,
  `DiscriminantGroupElement`, `from_invariants_and_gram`, `from_lattice`, `q`, `b`,
  `is_p_elementary`, `isomorphic_as_groups`, `is_isometric_to`, `submodule`,
  `orthogonal_submodule_to`, quotient, and `orthogonal_group`.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: quotient-valued
  torsion bilinear and quadratic module semantics.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  discriminant dual distinction, quotient codomain rules, comparison-predicate
  ownership, and validation rules for invariant-factor presentations.
- `.agents/memories/bilinear-form-category-semantics.md`: `A_L = L^#/L` as a
  cokernel with coefficient-module data, not a matrix shortcut.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`:
  mapping rows for `discriminant_group`, torsion quadratic modules, quotient-valued
  form data, `is_p_elementary`, `normal_form`, `brown_invariant`, and discriminant
  Hom/End/Aut standard names.

## Contract

For a nondegenerate integral lattice `L`, the discriminant object is the finite torsion
module obtained from the dual inclusion together with descended quotient-valued form
data. The public surface must expose the torsion carrier and the form as mathematical
structure, not as a Sage torsion module escape hatch.

The operations recovered from the old code must be admitted with distinct meanings:
group invariants classify the underlying finite abelian group; form isometry classifies
the quotient-valued formed object; automorphisms are form-preserving automorphisms in
the discriminant category.

## Recovered Construction Surface

For an integral nondegenerate lattice `L`, the primary constructor is the categorical
discriminant descent:

```text
L  --i-->  L^#  --pi-->  A_L := coker(i).
```

The public discriminant object must record:

- `source_lattice()` or `lattice()` when the object is constructed from a lattice;
- the metric dual object `L^# = L.dual_lattice()`;
- `inclusion_morphism(): L -> L^#`;
- the quotient projection `pi: L^# -> A_L`;
- the underlying finite torsion module;
- the bilinear form `b_A: A_L tensor A_L -> K/R`;
- the quadratic refinement `q_A: A_L -> K/2R` when the source form and parity
  hypotheses make it descend.

The historical `from_invariants_and_gram(invariants, gram, modulus, quadratic_modulus)`
path is admitted only as a constructor for a finite torsion formed module with explicit
quotient codomain data. It is not a replacement definition for `L.discriminant_group()`.
It must validate rank agreement, positive invariant factors, symmetry of the bilinear
or quadratic data, and the integrality compatibility `d_i*d_j*gram[i,j] in R` for the
chosen generator presentation.

## Recovered Object And Element Surface

The discriminant parent owns the finite torsion carrier and quotient-valued form data:

- `gens()`, `ngens()`, `invariants()`, `smith_form_gens()`, and `cardinality()` are
  finite torsion module surfaces.
- `zero()`, `__iter__()`, and finite listing/enumeration are admitted because the
  carrier is finite; they must not become proof substitutes outside finite contexts.
- `gram_matrix_bilinear()` and `gram_matrix_quadratic()` are quotient-valued form
  presentation data, distinct from free-lattice Gram matrices.
- `b(x, y)` returns a value in `K/R`; `q(x)` returns a value in `K/2R` when quadratic
  data is present.
- `is_p_elementary(p)` is a finite torsion module predicate. `delta`, `coparity`, and
  `(r, a, delta)` are lattice theorem-context invariants, not discriminant-object
  methods.

The element surface is parent-local:

- `A.element_from(coordinates)` or `A(value)` constructs a discriminant element from
  coordinates in the selected finite generator presentation.
- `x.vector()` or coordinate readback is presentation data.
- `x.lift()` is public only when it returns an element of the recorded metric dual or
  rational source object; a bare Sage lift is interop/private.
- `x.q()`, `x.b(y)`, `x.is_isotropic()`, and `x.additive_order()` are element methods
  routed through the parent form and torsion module.

## Recovered Subobject, Quotient, And Comparison Surface

Discriminant subobjects are finite torsion formed submodules, not raw lists of Sage
generators:

- `A.submodule(generators)` constructs a subobject with inclusion into `A`.
- `A.orthogonal_submodule_to(B)` requires `B` as a subobject or discriminant subgroup
  with parent data, and returns the orthogonal subobject for the quotient-valued
  bilinear form.
- `A / B` is admitted only as the quotient/cokernel of the recorded inclusion
  `B -> A`, with descended form data when it exists.
- `primary_part(p)` is admitted for prime-power primary decomposition; composite
  selectors require an explicit decomposition rule.

Comparison predicates must stay separated:

- `A == B` means equal presented discriminant formed objects, or a canonical equality
  criterion explicitly recorded by the implementation.
- `A.isomorphic_as_groups(B)` compares only the underlying finite abelian groups, for
  example via invariant factors.
- `A.is_isometric_to(B)` compares quotient-valued formed objects and must include the
  codomain data (`K/R` versus `K/2R`) and form values, not only the group invariants.
- `normal_form()` is backend evidence for isometry only after its hypotheses and
  quotient codomain are stated.

## Recovered Hom, End, Aut Surface

The discriminant Hom/End/Aut surface is the standard finite torsion formed-module
surface:

- `A.Hom(B)` is the parent of discriminant morphisms `A -> B`.
- Hom constructors may accept generator images, dictionaries, callables, or matrices
  only through named Hom-parent constructors such as `from_images(...)` or
  `from_matrix(...)`.
- A morphism element owns `kernel()`, `image()`, `cokernel()`, `lift()`,
  `is_injective()`, `is_surjective()`, `is_bijective()`, and `is_isomorphism()`.
- `A.End()` and `A.Aut()` are the endomorphism and automorphism parents; orthogonal
  groups are `Aut` objects in the discriminant formed-module category.
- Raw Sage automorphism groups and matrices are backend witnesses or constructor
  inputs; they are not public automorphism elements until containment in `A.Aut()` has
  validated the torsion module and form preservation.

## Non-Preservation Boundaries

- Do not identify the group and form notions merely because the old code used one
  class for both.
- Do not expose Sage element classes, normal forms, or private modulus fields as public
  semantics.
- Do not treat `delta` or coparity as discriminant-group-owned when the current
  correction source says they are lattice invariants.
- Do not use iteration over all elements as proof of a general theorem unless the
  finite carrier and exhaustive enumeration are part of the stated contract.

## Acceptance Criteria

- [x] The source lattice, dual map, quotient map, and descended form data are explicit.
- [x] Group-level and form-level comparison predicates are separate.
- [x] Orthogonal-group access is routed through the standard Hom/End/Aut hierarchy.
- [x] Backend finite-torsion calls are encapsulated behind the discriminant noun.
