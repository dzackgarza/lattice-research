---
id: SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE]]'
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
title: Recover orthogonal group and structured subgroup surfaces
status: unstarted
priority: high
requirement: Orthogonal groups and subgroups from historical code must be recovered
  as Aut-category objects and structured subgroup objects with explicit action, membership,
  generators, and finite quotient semantics.
acceptanceCriteria:
- L.orthogonal_group() or the standard Aut surface returns an object whose membership
  is the centralized form-preservation condition.
- Subgroups such as determinant-one, positive-spinor, discriminant-kernel, discriminant-preimage,
  and centralizer subgroups retain structured metadata without exposing raw ConditionSet
  as the public model.
- Group actions use the repo-standard left action on column vectors or elements, with
  backend row-action matrices normalized at the backend boundary.
- Generators returned by a backend are verified as group elements before entering
  public group semantics.
complexity: 85
tags:
- FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY
---
# Recover orthogonal group and structured subgroup surfaces

## Source Provenance

- `src.bak/lattices/groups/orthogonal.py`: `LatticeOrthogonalGroup`,
  `LatticeOrthogonalSubgroup`, special/plus/stable/discriminant-preimage subgroup
  methods, centralizer, and discriminant orthogonal groups.
- `src.bak/lattices/core/integral.py`: `orthogonal_group`,
  `_column_action_isometry_from_row_action_matrix`, and backend generator routing.
- IWE `bilinear-form-category-semantics`: public action convention and subgroup
  naming.

## Contract

The recovered orthogonal group of a lattice is the automorphism object of the formed
lattice in the appropriate category. A public group element acts on lattice elements by
the repo-standard action convention. Matrix equations are centralized membership checks
inside the group or Hom/Aut parent.

Subgroups must be structured mathematical objects. Determinant, spinor, discriminant
action, centralizer, and finite quotient constraints are metadata and predicates of
subgroup objects, not opaque intersections of arbitrary Python predicates. Subgroup
algebra may use intersections or generated joins internally, but the public model must
state the subgroup construction.

## Non-Preservation Boundaries

- Do not preserve `condition_set` accessors as public subgroup state.
- Do not merge subgroup constraints by raw Python predicate algebra when the subgroup
  has a named mathematical construction.
- Do not make backend generator availability define the subgroup; the subgroup exists
  mathematically even when generator computation is delayed or delegated.
- Do not expose discriminant orthogonal groups as raw Sage groups.

## Acceptance Criteria

- [ ] Orthogonal group membership is centralized in Aut/Hom containment.
- [ ] Structured subgroups retain named construction data and generator provenance.
- [ ] Backend matrices are normalized and verified once before exposure.
- [ ] Discriminant orthogonal groups are recovered as Aut objects of discriminant
  forms.
