# Plan: Refactor Stabilizer and Orbit Utilities

**Created**: 2026-03-30 13:47 **Status**: Active **SCHEDULE.md slot**: 15:00-16:00
(Refactoring: computing stabilizers, computing orbits, canonical Gram matrices)

## Context

After removing duplicate lattice definitions (49 lines), several utility functions
remain scattered across computation scripts:
- `reflection_matrix` appears in both `coble_geometry.sage` and
  `task3_1_stabilizer.sage`
- Stabilizer computation utilities in `task3_1_stabilizer.sage`
- Orbit computation utilities in `task2_2_orbit_lift.sage`
- Isotropic plane utilities in `task3_2_isotropic_planes.sage`

## Goal

Consolidate reusable stabilizer/orbit/reflection utilities into `coble_geometry.sage` or
a new `lattice_utilities.sage` module.

## Tasks

1. Audit which functions are truly reusable vs task-specific
2. Move reusable functions to central module
3. Update scripts to import from central module
4. Verify all affected scripts still run correctly
5. Commit changes

## Verification

- All computation scripts run without errors
- No duplicate utility functions remain
- Output files match previous results

## Notes

- Focus on functions used in multiple scripts or that provide general lattice/group
  utilities
- Task-specific functions (e.g., specific to one computation) should stay in their
  scripts
- Delegate this work to avoid token-heavy reconnaissance
