---
id: SPEC-HISTORICAL-ISOTROPIC-ORBIT-STABILIZER-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE]]'
- '[[SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS]]'
title: Recover vector, isotropic line, plane, flag orbit and stabilizer surfaces
status: unstarted
priority: high
requirement: Historical orbit and stabilizer algorithms must be recovered as methods
  on orthogonal groups or subgroups, returning typed representatives, witnesses, and
  stabilizer subgroup objects.
acceptanceCriteria:
- Vector equivalence returns a witness or an exact negative result justified by the
  backend/theorem branch.
- Isotropic lines, planes, and flags are typed subobjects or bases in the lattice,
  not ambient Sage spans.
- Orbit representative methods state the acting group, the objects acted on, and the
  equivalence relation.
- Stabilizer methods return subgroup objects whose generators and membership predicates
  are verified against the target subobject.
complexity: 90
tags:
- FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY
---
# Recover vector, isotropic line, plane, flag orbit and stabilizer surfaces

## Source Provenance

- `src.bak/lattices/groups/orthogonal.py`: `stabilizer`, `stabilizer_of_isotropic_line`,
  `stabilizer_of_isotropic_plane`, `stabilizer_of_isotropic_flag`,
  `find_vector_isometry`, `vectors_are_equivalent`, `isotropic_line_orbits`,
  `isotropic_plane_orbits`, `isotropic_flag_orbits`, and equivalence predicates.
- `src.bak/backends/dawes_orbit_backend.py`: vector orbit witness search under
  subgroup constraints.
- `src.bak/backends/isotropic_gamma_orbit_backend.py`: ambient and subgroup isotropic
  orbit representatives, equivalence witnesses, and finite quotient filtering.
- IWE `theory/algorithms/isotropic-gamma-orbit-backend`.

## Contract

Orbit and stabilizer methods are owned by the acting group or subgroup. The caller
must be able to read the statement as a mathematical action: a group acts on vectors,
isotropic lines, isotropic planes, or isotropic flags in a lattice, and the method
returns representatives, witnesses, or stabilizer subgroups for that action.

Representatives must be typed lattice elements or typed subobjects. Normalization of a
primitive isotropic line is an internal representative convention, not a replacement
for the line object. Witness matrices returned by backends become group elements only
after membership verification.

## Non-Preservation Boundaries

- Do not present finite quotient filtering as proof unless the quotient map, image,
  subgroup image, and lifting condition are explicit.
- Do not use raw tuples of rows as the final public representation of isotropic planes
  or flags.
- Do not treat a missing backend witness as a proof of non-equivalence unless the
  backend contract says the search is complete for the stated inputs.
- Do not allow subgroup constraints to become opaque bags of predicates.

## Acceptance Criteria

- [ ] Acting group, acted-on object, and equivalence relation are explicit.
- [ ] Orbit methods return typed representatives with normalization provenance.
- [ ] Stabilizer methods return subgroup objects with verified generators.
- [ ] Equivalence methods return witnesses when equivalence holds and exact evidence
  when it does not.
