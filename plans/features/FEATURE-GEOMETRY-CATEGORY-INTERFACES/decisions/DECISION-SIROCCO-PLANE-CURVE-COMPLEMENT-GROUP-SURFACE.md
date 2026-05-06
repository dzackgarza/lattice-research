---
id: DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE
trackerStatus:
  type: decision
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING]]'
title: Choose Sirocco-backed plane-curve complement group surface
status: unstarted
chosen: ''
options:
- name: Complement object owns the group
  pros:
  - Keeps the mathematical object as the complement, not the defining curve alone.
  - Can separate affine and projective complements by construction.
  cons:
  - Requires complement-object vocabulary before implementation work.
- name: Plane curve forwards to complement
  pros:
  - Matches Sage's existing `C.fundamental_group()` user-facing route.
  - Gives a convenient interop spelling after the complement owner exists.
  cons:
  - Can hide that the computed group is attached to the complement and presentation choices.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Choose Sirocco-backed plane-curve complement group surface

## Summary

Decide the public mathematical surface for using Sage's Sirocco-backed
Zariski-Van Kampen route after the geometry category vocabulary exists.

## Source Provenance

- `[[TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS]]`
- `[[SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING]]`
- Upstream SIROCCO2 repository: <https://github.com/miguelmarco/sirocco2>
- Sage Zariski-Van Kampen documentation:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html>
- Sage projective plane curve `fundamental_group()` documentation:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/projective_curve.html>
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/zariski_vankampen.py`

## Context

The Sirocco research pass admitted backend evidence but did not admit an
implementation. Sage exposes finite presentations of affine and projective
plane-curve complement groups through Zariski-Van Kampen computations that use
Sirocco for certified strand following.

The remaining choices are mathematical surface decisions, not implementation
details.

## Decision Questions

- Should the public owner be `C.complement().fundamental_group()` with
  `C.fundamental_group()` as an interop forwarder, or should the plane curve own
  the public method directly?
- Should braid monodromy be a typed intermediate mathematical object, or remain
  backend-only evidence hidden below the complement-group method?
- How should finite presentations record meridians, arrangement factors,
  vertical components, simplification, and comparison/equivalence policy?
- Should affine and projective complements be distinct complement objects, or
  variants selected by construction data on one complement type?

## Acceptance Criteria

- [ ] The chosen owner names the caller object, required projection or complement
      data, hypotheses on the plane curve and coefficient field, and the return
      object.
- [ ] The decision records whether braid monodromy is public typed vocabulary or
      backend-only evidence.
- [ ] The decision records how presentation generators, meridians, arrangement
      labels, vertical components, simplification, and comparison policy are typed
      or deferred.
- [ ] The decision records whether affine and projective complements are separate
      objects or variants of one construction.
- [ ] The decision updates or links the geometry category spec that will own the
      chosen method surface.

## Dependencies And Boundaries

- This decision depends on the Sirocco backend mapping spec, but it does not
  authorize an implementation.
- Do not add a raw Sirocco wrapper as the public surface.
- Do not treat a finitely presented group returned by Sage as canonical group
  equality or isomorphism evidence without a separate presentation/comparison
  policy.

## Work Log

- 2026-05-06: Created from Gate 2 review of the Sirocco research task, which found
  that concrete follow-up choices were left as inline prose in the backend mapping
  spec instead of tracked as a card.
