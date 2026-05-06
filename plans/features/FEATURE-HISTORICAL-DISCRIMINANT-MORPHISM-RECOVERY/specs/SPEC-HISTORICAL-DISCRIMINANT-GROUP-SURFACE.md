---
id: SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]'
title: Recover discriminant group and quotient-valued form surface
status: unstarted
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
- IWE `bilinear-form-category-semantics`: `A_L = L#/L` as a cokernel with coefficient
  data, not a matrix shortcut.

## Contract

For a nondegenerate integral lattice `L`, the discriminant object is the finite torsion
module obtained from the dual inclusion together with descended quotient-valued form
data. The public surface must expose the torsion carrier and the form as mathematical
structure, not as a Sage torsion module escape hatch.

The operations recovered from the old code must be admitted with distinct meanings:
group invariants classify the underlying finite abelian group; form isometry classifies
the quotient-valued formed object; automorphisms are form-preserving automorphisms in
the discriminant category.

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

- [ ] The source lattice, dual map, quotient map, and descended form data are explicit.
- [ ] Group-level and form-level comparison predicates are separate.
- [ ] Orthogonal-group access is routed through the standard Hom/End/Aut hierarchy.
- [ ] Backend finite-torsion calls are encapsulated behind the discriminant noun.
