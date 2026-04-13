# Lattice redesign source of truth

Trigger: working on `src/lattices/lattices.py`, lattice interface redesign, or lattice spec tests.

Rule:
- Treat `src/lattices/lattices.py` as the canonical written spec.
- Protect that file by adding new dedicated spec tests derived from its semantic comments/TODO clusters, not by rewriting the old lattice test suite first.
- Import the renamed module directly in new spec tests (`src.lattices.lattices`); do not preserve or add compatibility shims for `coble_geometry_foundation` during this rewrite.
- Existing tests are secondary and may be migrated only after the new spec surface exists.

Verify:
- New spec tests live in `tests/lattice_spec/` and target `src.lattices.lattices` directly.
- The redesign plan groups work by semantic boundaries from the written spec (hierarchy, promotion, dual/discriminant semantics, morphisms, subobjects, groups/backends).