---
trackerStatus:
  itemId: res_01KQN9J3XB7KP0D1WRYSN000NJ
  title: Implement and validate the Dawes orbit backend plan for structured subgroup
    orbit computations
  type: research-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - category-specs
  - research-backend
  - research-work
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Implement and validate the Dawes orbit backend plan for structured subgroup orbit computations

## Summary

The Dawes backend plan targets subgroup-aware non-isotropic vector orbit equivalence
using existing lattice/group nouns and a private backend.

## Source Provenance

- `theory/dawes_orbit_backend_plan.md`
- Original migrated line: `Implement and validate the Dawes orbit backend plan for structured subgroup orbit computations from theory/dawes_orbit_backend_plan.md`

## Context

- Public methods include special_orthogonal_subgroup, plus_subgroup, special_plus_subgroup, preimage_of_discriminant_subgroup, find_vector_isometry, and vectors_are_equivalent.
- The backend uses Dutour-Sikiric binaries when decisive and Dawes algorithms only for subgroup-sensitive branches.
- The implementation should stay in src/research/dawes_orbit_backend.py with thin hooks on existing orthogonal-group nouns.
- The condition-set model remains the OSOT for subgroup membership.

## Acceptance Criteria

- [ ] The research result cites the exact sources searched and separates source evidence from inference.
- [ ] Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence, Gaps.
- [ ] Any admitted design consequence is linked to a spec-work or design-decision item rather than buried in prose.
- [ ] Validate subgroup-sensitive vector equivalence against exact fixtures.
- [ ] Do not introduce a second public group hierarchy.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

