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
status: unstarted
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
- IWE `theory-backend-routing`: Oscar, GAP, CARAT, and Indefinite backend ownership.

## Contract

Centralizer and finite quotient computations are backend services for structured
subgroups. Invariant and coinvariant outputs must be promoted to typed subobjects with
maps, not raw row bases. Discriminant-action images and finite quotient homomorphisms
must be explicit enough that an orbit/stabilizer result can be audited as a group
action computation.

CARAT remains an auxiliary for positive-definite forms and finite matrix groups. GAP
finite group calls are appropriate only after the acting set, action, and finite group
object have been constructed.

## Non-Preservation Boundaries

- Do not store centralizer output as an untyped dictionary in public code.
- Do not call Julia/Oscar through global user state without an explicit bridge
  contract and environment isolation.
- Do not use finite quotient images as opaque filters with no named quotient map.
- Do not infer subgroup equality from generator lists alone.

## Acceptance Criteria

- [ ] Invariant and coinvariant results are typed subobjects with maps.
- [ ] Centralizer backend routes record exact domain and finite/definite assumptions.
- [ ] Finite quotient filtering exposes the group homomorphism and lifting condition.
- [ ] Returned subgroup data is verified by the structured subgroup surface.
