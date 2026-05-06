---
id: DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide public names for malformed backend-mapping source surfaces
status: unstarted
options:
- name: Preserve malformed source spellings as public methods
  pros:
  - Literal migration from the old abstract map is mechanically complete.
  cons:
  - Corrupt names would poison the public API and downstream spec rows.
- name: Reject malformed spellings and rename through source-grounded owners
  pros:
  - Keeps public method names mathematical and reviewable.
  - Separates backend availability from source-file typo cleanup.
  cons:
  - Requires a small follow-up decision before implementation cards can use these rows.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide public names for malformed backend-mapping source surfaces

## Summary

`theory/backends/abstract-to-external-mapping.md` contains two source surfaces that
should not be normalized silently:

- `PicardeLattice.underlying_picard_group()`
- `Lattice.vinberg_sh姚()`

The backend inventory records rows for both surfaces so the source map is complete, but
it does not admit those literal spellings as public project API.

## Source Provenance

- `theory/backends/abstract-to-external-mapping.md`
- `theory/backends/software-capability-map.md`
- `theory/backends/vinberg-algorithm.md`
- `category_specs/lattices/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`

## Context

The issue is not backend availability alone. Oscar/Hecke, Indefinite.jl, CARAT, GAP,
and Vinberg-specific notes all provide plausible backend routes for nearby
mathematical operations. The blocker is public method naming and owner placement:
malformed spellings must not be promoted into category specs or implementation tasks.

## Acceptance Criteria

- [ ] The decision states the replacement public surface or rejection for
  `PicardeLattice.underlying_picard_group()`.
- [ ] The decision states the replacement public surface or rejection for
  `Lattice.vinberg_sh姚()`.
- [ ] The chosen names cite the lattice/forms mapping docs or create the missing
  source-mining card if the current docs are insufficient.
- [ ] Any implementation card that depends on these methods links to this decision
  rather than relying on the malformed source spelling.

## Dependencies And Boundaries

- Do not implement either malformed method name.
- Do not treat this decision as approval for a local Vinberg implementation.
- Keep the backend rows in the method inventory as source-map coverage, but keep the
  public API blocked until this decision is resolved.

## Work Log

- 2026-05-06: Created while translating backend method rows for the literal method
  ownership inventory.
