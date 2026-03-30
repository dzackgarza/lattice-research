# Plan: Verify All Computations Actually Run

**Created**: 2026-03-30 14:30 **Status**: Active

## Context

Refactoring broke load paths in 7 scripts.
Fixed all `load("computations/coble_geometry.sage")` → `load("coble_geometry.sage")`.
Now need to verify ALL computation scripts actually execute successfully, not just trust
documentation.

## Goal

Run every computation script and verify:
1. No runtime errors
2. Output files generated
3. Results match verification note claims

## Phase 1 — Run all task scripts systematically

Execute in computations/ directory:
- [ ] task1_1_sextic.sage
- [ ] task1_1_sextic_example2.sage
- [ ] task1_1_sextic_example3.sage
- [ ] task1_2_gram_matrices.sage
- [ ] task1_2b_discriminant_forms.sage
- [ ] task1_3_embeddings.sage
- [ ] task1_3_embeddings_primitive.sage
- [ ] task1_3_embeddings_fixed.sage
- [ ] task2_1_isotropic_orbits.sage
- [ ] task2_2_orbit_lift.sage
- [ ] task3_1_stabilizer.sage
- [ ] task3_2_isotropic_planes.sage
- [ ] task4_1_coxeter_search.sage
- [ ] task5_1_involution.sage
- [ ] task6_1_monodromy.sage

## Phase 2 — Document failures

For each failure:
- Error message
- Line number
- Root cause
- Whether verification note overclaimed

## Phase 3 — Fix or document

- Fix fixable errors
- Update verification notes if they overclaimed
- Mark scripts as broken if unfixable

## Verification

Success: All scripts run without errors OR failures are documented with updated
verification notes.
