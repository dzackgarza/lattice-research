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
status: needs-review
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
- `src.bak/backends/external/py_polyhedral/binaries.py`: exact vector, isotropic
  subspace, flag equivalence/stabilizer/orbit backend wrappers.
- `.agents/memories/theory-backend-routing.md` and
  `.agents/memories/theory/backends/indefinite-jl.md`: Indefinite.jl orbit and
  stabilizer routing.
- `.agents/memories/theory/backends/gap-orbits.md`: finite action, stabilizer, and
  double-coset routing.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`:
  exact backend domains and witness verification.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md`:
  finite quotient filtering and lifting contracts.
- `plans/features/FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY/specs/SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE.md`:
  group/subgroup ownership and action conventions.

## Contract

Orbit and stabilizer methods are owned by the acting group or subgroup. The caller
must be able to read the statement as a mathematical action: a group acts on vectors,
isotropic lines, isotropic planes, or isotropic flags in a lattice, and the method
returns representatives, witnesses, or stabilizer subgroups for that action.

Representatives must be typed lattice elements or typed subobjects. Normalization of a
primitive isotropic line is an internal representative convention, not a replacement
for the line object. Witness matrices returned by backends become group elements only
after membership verification.

## Definition Grounding

- Acting object: an orthogonal group or structured subgroup `G <= L.Aut()`.
- Acted-on objects: lattice elements, primitive isotropic lines as rank-one subobjects,
  isotropic planes as rank-two formed subobjects with inclusion into `L`, and flags as
  nested isotropic subobjects.
- Orbit relation: `x ~ y` means there exists `g in G` such that `g.x = y` for vectors
  or `g(S) = T` for subobjects/flags under the stated pointwise or setwise action.
- Stabilizer: `G.stabilizer(x)` is a subgroup of `G`; for an element it fixes the
  element, for a line/plane it preserves the subobject setwise unless the method name
  explicitly says pointwise, and for a flag it preserves every stratum in the chain.
- Witness: an equivalence method returning true must return or expose a group element
  witness when the backend route computes one. A negative result is exact only when the
  selected backend/theorem branch is complete for the stated domain.

## Public Orbit And Stabilizer Surface

The admitted group-owned surface is:

- `G.orbit_representatives(objects=...)` for a typed finite or backend-supported
  object family;
- `G.isotropic_line_orbits()`, `G.isotropic_plane_orbits()`, and
  `G.isotropic_flag_orbits(length=...)` as compatibility spellings for the lattice
  literature;
- `G.are_equivalent(x, y)` or object-specific compatibility spellings for orbit
  membership, returning exact evidence and a witness when available;
- `G.find_witness(x, y)` or `G.transport(x, y)` returning a group element when
  equivalence holds;
- `G.stabilizer(x)` for elements and subobjects;
- `G.stabilizer_of_isotropic_line(line)`, `G.stabilizer_of_isotropic_plane(plane)`,
  and `G.stabilizer_of_isotropic_flag(flag)` as compatibility spellings that delegate
  to `G.stabilizer(...)` after constructing typed objects.

These methods live on the acting group or subgroup. Lattice-local spellings may remain
only as convenience routes that call `L.orthogonal_group().method(...)`; the mathematical
owner is the acting group.

## Typed Representatives

Vector orbits return elements of `L`, not coordinate lists. A norm-orbit method must
record the norm, parent, backend completeness claim, and whether the representative is
integral, rational, metric-dual, or in another explicitly named parent.

Primitive isotropic line orbits return rank-one subobjects with inclusion into `L`.
Over `ZZ`, `v` and `-v` generate the same line; normalizing to a primitive generator is
representative data, not the definition of the line. Docstrings must state when a method
acts on vectors and when it acts projectively on lines.

Isotropic plane orbits return rank-two isotropic subobjects with selected generator
data when a backend needs rows. Flags return nested subobject chains
`L_1 <= L_2 <= ... <= L_k <= L`, with inclusion maps and isotropy checks at every
stratum. A tuple of backend rows is not a public flag.

## Backend Contracts

Ambient indefinite orbits and stabilizers route through the exact Indefinite.jl or
polyhedral_common bridge specified by
`SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT`. Backend rows and row-action
matrices are normalized at the bridge and verified through `G <= L.Aut()`.

Subgroup-aware splitting routes through the finite quotient contract from
`SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS`. The public result must
record the ambient orbit/stabilizer, the finite quotient homomorphism, the subgroup
image, the stabilizer image, and the double-coset or lifting condition used to split
ambient orbits into subgroup orbits.

The Dawes non-isotropic vector backend is admitted only as a route for the precise
domain it states: non-isotropic vector orbit equivalence under a structured subgroup,
with determinant, spinor, and discriminant-action constraints exposed as finite
quotient/preimage data. It must not be treated as a generic vector-orbit oracle.

## Stabilizer Contracts

Element stabilizer:

- Input: `x in L`.
- Condition: `g(x) == x`.
- Output: a subgroup of `G` with generators verified as elements of `G` fixing `x`.

Line stabilizer:

- Input: a rank-one primitive isotropic subobject or a generator promoted to that
  subobject.
- Condition: setwise preservation of the subobject unless the method says pointwise.
- Output: subgroup of `G`; in the projective line case, `g(v) = +/- v` is a generator
  check, not a replacement for subobject containment.

Plane and flag stabilizers:

- Input: a typed isotropic plane or flag.
- Condition: setwise preservation of the plane, or preservation of every flag stratum.
- Output: subgroup of `G` with generator verification against the target subobjects.

## Equivalence Results

Equivalence methods must distinguish:

- `equivalent=True` with a verified witness `g in G`;
- `equivalent=False` with an exact backend/theorem reason;
- `unsupported` or backend failure, which is not a proof of non-equivalence.

The result object or return contract should retain the acting group, source object,
target object, witness when present, and backend route/provenance. A bare boolean is
not sufficient when a proof or later computation needs the witness.

## Non-Preservation Boundaries

- Do not present finite quotient filtering as proof unless the quotient map, image,
  subgroup image, and lifting condition are explicit.
- Do not use raw tuples of rows as the final public representation of isotropic planes
  or flags.
- Do not treat a missing backend witness as a proof of non-equivalence unless the
  backend contract says the search is complete for the stated inputs.
- Do not allow subgroup constraints to become opaque bags of predicates.
- Do not preserve cache hits as mathematical evidence; cached representatives must be
  deserialized into typed objects and revalidated.
- Do not conflate vector orbits with line orbits. Projectivizing by `v ~ -v` changes the
  acted-on object.
- Do not expose row tuples, ambient Sage spans, or backend normalization choices as the
  final public representation of lines, planes, or flags.

## Acceptance Criteria

- [x] Acting group, acted-on object, and equivalence relation are explicit.
- [x] Orbit methods return typed representatives with normalization provenance.
- [x] Stabilizer methods return subgroup objects with verified generators.
- [x] Equivalence methods return witnesses when equivalence holds and exact evidence
  when it does not.
