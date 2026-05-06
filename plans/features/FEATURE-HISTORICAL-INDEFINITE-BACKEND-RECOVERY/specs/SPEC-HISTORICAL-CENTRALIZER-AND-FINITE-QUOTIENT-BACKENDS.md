---
id: SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
- '[[SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE]]'
title: Recover centralizer, invariant coinvariant, and finite quotient backend contracts
status: needs-review
priority: medium
requirement: Historical Oscar/GAP centralizer and finite quotient filtering code must
  be recovered as backend contracts feeding structured subgroup and discriminant-action
  objects.
acceptanceCriteria:
- Invariant and coinvariant sublattices of an isometry are constructed as typed subobjects
  with inclusion data.
- Centralizer computations state whether they are definite GAP, Oscar, discriminant-action
  image, or finite quotient computations.
- Finite quotient filters expose the homomorphism, target image, subgroup image, and
  lifting condition they use.
- CARAT and GAP finite group operations are used only within their documented finite
  or definite domains.
complexity: 80
tags:
- FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY
---
# Recover centralizer, invariant coinvariant, and finite quotient backend contracts

## Source Provenance

- `src.bak/backends/oscar_centralizer/__init__.py` and
  `src.bak/backends/oscar_centralizer/oscar_centralizer.jl`: invariant and
  coinvariant bases plus image of centralizer in discriminant data.
- `src.bak/lattices/core/integral.py`: invariant and coinvariant sublattice kernels,
  definite centralizer via GAP.
- `src.bak/backends/dawes_orbit_backend.py`: discriminant actions, spinor norm signs,
  and subgroup constraints.
- `src.bak/backends/isotropic_gamma_orbit_backend.py`: finite quotient specification,
  target image group, subgroup image, and image-from-matrix maps.
- `.agents/memories/theory-backend-routing.md`: Oscar, GAP, CARAT, and Indefinite
  backend ownership.
- `.agents/memories/theory/backends/oscar-lattices.md`: Oscar/Hecke calls
  `integer_lattice_with_isometry`, `invariant_lattice`, `coinvariant_lattice`,
  `image_centralizer_in_Oq`, and discriminant representation surfaces.
- `.agents/memories/theory/backends/gap-orbits.md`: GAP `Orbit`, `Orbits`,
  `OrbitsDomain`, `Stabilizer`, `OrbitStabilizer`, `DoubleCosets`, and finite action
  selectors.
- `.agents/memories/theory/backends/carat.md`: CARAT positive-definite and finite
  matrix-group limitations.

## Contract

Centralizer and finite quotient computations are backend services for structured
subgroups. Invariant and coinvariant outputs must be promoted to typed subobjects with
maps, not raw row bases. Discriminant-action images and finite quotient homomorphisms
must be explicit enough that an orbit/stabilizer result can be audited as a group
action computation.

CARAT remains an auxiliary for positive-definite forms and finite matrix groups. GAP
finite group calls are appropriate only after the acting set, action, and finite group
object have been constructed.

## Definition Grounding

- Public objects: a lattice or formed module `L`, an isometry `f in L.Aut()`, subobjects
  such as `L^f` and `L_f`, discriminant formed modules `A_L`, finite group objects, and
  homomorphisms between group objects.
- Invariant subobject: `L^f = ker(f - id_L)`, constructed as the kernel object of the
  morphism `f - id_L` with inclusion into `L`.
- Coinvariant subobject: for an involution, the historical branch computes
  `ker(f + id_L)`. More generally, coinvariant data must name the exact construction
  being used: eigenspace, image/cokernel of `f - id`, or Oscar's
  `coinvariant_lattice` semantics for an `integer_lattice_with_isometry`.
- Centralizer: `Z_{O(L)}(f)` is a subgroup of the public automorphism group `L.Aut()`.
  Its image in a discriminant automorphism group is the image of a recorded group
  homomorphism, not an untyped generator list.
- Finite quotient filtering: a subgroup specified by determinant, real spinor sign, or
  discriminant-action preimage is the preimage of an explicitly named finite target
  subgroup under a product homomorphism. The filter must expose the homomorphism,
  target image, allowed subgroup image, and lifting condition.

## Backend Routing Contract

| Operation family | Preferred route | Public output |
| --- | --- | --- |
| Invariant lattice of an isometry | Oscar/Hecke `integer_lattice_with_isometry` then `invariant_lattice` | typed subobject with inclusion into `L` |
| Coinvariant lattice of an isometry | Oscar/Hecke `coinvariant_lattice`, with exact semantics recorded | typed subobject or quotient/eigenspace object with maps |
| Centralizer image in discriminant data | Oscar/Hecke `image_centralizer_in_Oq` when hypotheses hold | image subgroup plus homomorphism into a discriminant Aut object |
| Definite centralizer fallback | Sage/GAP definite orthogonal group centralizer only after definite reduction | subgroup of `L.Aut()` after convention normalization |
| Finite quotient action/orbit filtering | GAP finite group actions, intersections, homomorphisms, double cosets | finite group objects, subgroup images, and lifted public group elements |
| Positive-definite or finite matrix-group auxiliary | CARAT only within documented definite/finite domains | backend evidence verified by public group/subgroup containment |

Oscar/Hecke owns the lattice-with-isometry semantics. GAP owns finite group action
algorithms after the target finite group and action are explicit. CARAT must not be
used as an indefinite-form centralizer backend; it may help only when the task has
already reduced to a positive-definite form or a finite matrix-group problem.

## Operation Contracts

### Invariant And Coinvariant Objects

Input: a public isometry `f in L.Aut()`.

Output: subobjects or quotient/eigenspace objects with maps, not basis rows. The
implementation may use Oscar basis matrices as backend data, but the public result must
include the inclusion into `L`, the restricted or descended form data, and verification
that the returned generators satisfy the stated kernel/eigenspace condition.

For involution-specific `ker(f + id_L)` data, the method name and docstring must say
whether the returned object is the `-1` eigenspace subobject or an actual coinvariant
quotient. These are not interchangeable merely because a historical file called one
`coinvariant`.

### Centralizer And Discriminant Image

Input: `L` and `f in L.Aut()`.

Output: a subgroup object of `L.Aut()` or a recorded image subgroup in a discriminant
Aut object. If the backend returns the image of the centralizer in `O(A_L, D_f)`, then
the public object must record:

- the source centralizer group or ambient subgroup whose image is being computed;
- the discriminant object and its Aut parent;
- the homomorphism or representation inducing the image;
- the image generators and image order when the backend provides them;
- the hypotheses, such as evenness, required by `image_centralizer_in_Oq`.

An odd lattice or unsupported theorem domain must not be encoded as `order = -1` in a
public object. That historical sentinel becomes a bridge failure or an unsupported
image result with a typed status.

### Structured Subgroup Constraints

The subgroup constraints in the Dawes and isotropic gamma backends are admitted only as
structured homomorphism data:

- determinant kernel: homomorphism to a two-element group by determinant sign;
- positive real spinor kernel: homomorphism to a two-element group by real spinor norm
  sign, with source-backed domain and convention;
- discriminant preimage: homomorphism from `L.Aut()` to `A_L.Aut()` through the
  induced discriminant action.

The product of these factors is a finite target group. A subgroup is the preimage of a
named allowed subgroup under that product homomorphism. Public filtering must not test
opaque predicates without exposing this finite quotient data.

### Finite Quotient Orbits And Double Cosets

Input: an ambient group action, an ambient orbit/stabilizer computation, and a
structured finite quotient presentation.

Output: orbit representatives, equivalence predicates, or subgroup results whose
finite quotient step can be audited. The contract must expose:

- source group and target finite group;
- homomorphism from source generators to target images;
- subgroup image allowed by the determinant/spinor/discriminant constraints;
- stabilizer image for the object being split;
- double-coset or lifting condition used to refine ambient orbits;
- lifted public group element, when a target representative is lifted.

GAP `DoubleCosets`, `Intersection`, `GroupHomomorphismByImagesNC`,
`PreImagesRepresentative`, `Orbit`, `Stabilizer`, and related finite-action calls are
backend steps only after the source and target group objects are finite and typed.

## Boundary Failures

The bridge must fail or return a typed unsupported result for:

- missing Oscar/Julia/GAP/CARAT backend or environment failure;
- an isometry matrix that is not in the public Aut parent;
- Oscar centralizer-image calls outside their even-lattice or other stated hypotheses;
- finite quotient construction with no determinant, spinor, or discriminant-action
  factor when a subgroup split requires one;
- GAP target image or homomorphism data that does not match source generators;
- a lifted matrix that fails public group containment or fails the stated action.

Do not replace these failures with raw generator-list comparisons, cache hits,
predicate-only subgroup filters, or local matrix searches.

## Non-Preservation Boundaries

- Do not store centralizer output as an untyped dictionary in public code.
- Do not call Julia/Oscar through global user state without an explicit bridge
  contract and environment isolation.
- Do not use finite quotient images as opaque filters with no named quotient map.
- Do not infer subgroup equality from generator lists alone.
- Do not preserve implementation caches as mathematical evidence. Cached orbit
  artifacts may be performance data only after deserialization is revalidated.
- Do not expose Python `dataclass` helper specs as public subgroup semantics; replace
  them with group, homomorphism, image, and preimage objects.

## Acceptance Criteria

- [x] Invariant and coinvariant results are specified as typed subobjects or quotient
  objects with maps.
- [x] Centralizer backend routes record exact domain and finite/definite assumptions.
- [x] Finite quotient filtering exposes the group homomorphism and lifting condition.
- [x] Returned subgroup data is required to be verified by the structured subgroup
  surface.
