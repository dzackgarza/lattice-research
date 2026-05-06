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
status: needs-review
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
- `src.bak/backends/dawes_orbit_backend.py`: determinant, real spinor, discriminant
  action, and structured subgroup constraints.
- `src.bak/backends/isotropic_gamma_orbit_backend.py`: finite quotient presentation
  consumption for subgroup-aware orbit splitting.
- `.agents/memories/bilinear-form-category-semantics.md`: public action convention
  and subgroup naming.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`:
  backend matrix normalization and witness verification.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md`:
  finite quotient, centralizer, discriminant-image, and subgroup-preimage contracts.
- `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/specs/SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md`:
  `O(M,b) = Aut(M,b)` in the formed-module category.

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

## Definition Grounding

- Orthogonal group: for a formed module or lattice `(M, b)`, the orthogonal group is
  `Aut(M, b)`, the invertible formed-module endomorphisms preserving `b`.
- Public membership: a matrix or backend datum becomes a group element only by entering
  the Aut/Hom parent and satisfying the centralized containment rule: source and target
  parent match, the underlying module map is invertible, and the form is preserved.
- Public action: group elements act on lattice/module elements by the repo-standard
  left action on column-coordinate presentations. Backend row/right-action matrices are
  normalized before this surface sees them.
- Discriminant orthogonal group: `O(A_L, q)` or `O(A_L, b)` is the Aut object of the
  finite discriminant formed module. It is not a raw Sage group.
- Structured subgroup: a subgroup is represented by its parent group, construction
  data, membership predicate/containment rule, optional generator backend provenance,
  and optional finite quotient/preimage metadata.

## Recovered Orthogonal Group Surface

The admitted public lattice surface is:

- `L.Aut()` as the canonical formed-module automorphism group;
- `L.orthogonal_group()` as a compatibility spelling for `L.Aut()` where the lattice
  literature expects `O(L)`;
- `O.lattice()` or `O.object()` returning the parent formed object;
- `O.identity()`, `O(g)` or `O.from_matrix(g)` as Aut-parent constructors that validate
  membership;
- `g.matrix()` or `g.to_matrix()` as presentation readback for a group element;
- `g.inverse()`, composition, equality, determinant where the carrier is finite free,
  and action on elements/subobjects through the public group action.

Generator computation is separate from group definition. `O(L)` exists as an Aut object
even when generators are not yet available. A backend route may provide generators, but
each generator must be normalized and admitted through `O(L)` before `O.gens()` returns
it.

## Structured Subgroup Surface

The historical subgroup methods recover named subgroup constructors:

| Historical surface | Admitted public construction |
| --- | --- |
| `special_orthogonal_subgroup()` | determinant-one subgroup `SO(L) = ker(det: O(L) -> {+/-1})` where determinant is defined |
| `plus_subgroup()` | positive real-spinor-kernel subgroup with source-backed spinor convention |
| `special_plus_subgroup()` | intersection of the determinant-one and positive-spinor kernels |
| `kernel_of_discriminant_action()` | kernel of the discriminant representation `O(L) -> O(A_L)` |
| `preimage_of_discriminant_subgroup(H)` | preimage of a subgroup `H <= O(A_L)` under the discriminant action |
| `centralizer(f)` | centralizer subgroup `Z_{O(L)}(f)` for `f in O(L)` |
| `stabilizer(x)` and isotropic stabilizers | subgroup of the acting group preserving the target object, specified in the orbit/stabilizer spec |

Subgroup intersection is a subgroup meet with combined construction data. A generated
join may be admitted when the result is explicitly the subgroup generated by the two
inputs. Do not expose set-theoretic union of subgroups as a subgroup operation; a union
is usually not a subgroup.

The finite quotient presentation used by Dawes/isotropic backends is public only as
group homomorphism data:

- determinant sign factor;
- positive real spinor sign factor;
- discriminant-action image/preimage factor;
- product target finite group;
- allowed subgroup image;
- source-to-target homomorphism.

This metadata must survive subgroup intersections and be visible to orbit/stabilizer
backend contracts.

## Discriminant Aut Surface

The historical `DiscriminantOrthogonalGroup` and `DiscriminantOrthogonalSubgroup`
recover the finite formed-module Aut surface:

- `A.Aut()` where `A` is a discriminant formed module;
- `A.Aut().gens()` admitted only after Sage/GAP/Oscar generators are converted into
  public Aut elements;
- `A.Aut().subgroup(generators)` returning a structured subgroup of `A.Aut()`;
- `A.Aut().stabilizer(a)` for a discriminant element or subobject, returning a subgroup
  with verified action;
- intersections of discriminant subgroups as subgroup meets in the same parent.

Actions return discriminant elements or subobjects, not coordinate vectors. Coordinate
matrix action is implementation data behind the finite formed-module parent.

## Backend And Generator Provenance

Public groups/subgroups should record generator provenance:

- definite orthogonal generators from Sage/definite quadratic-form code;
- indefinite generators from Indefinite.jl/polyhedral routes;
- centralizer-image or finite quotient data from Oscar/GAP routes;
- CARAT only when the task has reduced to a positive-definite form or finite matrix
  group within the documented CARAT domain.

If no generator backend is available for a subgroup, the subgroup object may still exist
with exact containment data, but generator enumeration must report unsupported rather
than silently performing an unrelated search.

## Non-Preservation Boundaries

- Do not preserve `condition_set` accessors as public subgroup state.
- Do not merge subgroup constraints by raw Python predicate algebra when the subgroup
  has a named mathematical construction.
- Do not make backend generator availability define the subgroup; the subgroup exists
  mathematically even when generator computation is delayed or delegated.
- Do not expose discriminant orthogonal groups as raw Sage groups.
- Do not expose `condition_set | condition_set` as subgroup union. Use a generated join
  only when the subgroup generated by both inputs is the mathematical construction.
- Do not treat `MatrixSpace(ZZ, n)` containment as group membership; Aut containment is
  the membership owner.

## Acceptance Criteria

- [x] Orthogonal group membership is centralized in Aut/Hom containment.
- [x] Structured subgroups retain named construction data and generator provenance.
- [x] Backend matrices are required to be normalized and verified once before exposure.
- [x] Discriminant orthogonal groups are recovered as Aut objects of discriminant
  forms.
