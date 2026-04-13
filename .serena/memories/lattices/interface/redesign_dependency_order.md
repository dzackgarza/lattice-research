# Lattice redesign dependency order

Trigger: planning or resuming the lattice architectural rehaul.

Rule:
- Treat `tests/sage_spec/misc.sage` as an upstream contract, not a downstream cleanup item. The required order is:
  1. foundational ring/module/field semantics,
  2. category-correct general bilinear modules over PID/Dedekind-style bases,
  3. lattice/rational/dual/discriminant specializations,
  4. orthogonal/root/Weyl/Coxeter/Eichler/group surfaces,
  5. general indefinite isometry backend completion.
- Preserve and migrate the current FGP/pydantic/Sage-wrapper machinery where it is sound; do not restart from scratch.
- Before running lattice tests, verify the canonical export surface: `src/lattices/lattices.py` must actually export the public nouns expected by `src/lattices/__init__.py` and the spec tests.
- Sage integration should follow the docs-backed contract: use `Parent` + category, real `Element`/`ElementWrapper` element types, `_Hom_` for custom homset construction, and `_element_constructor_` for parent-side conversion rather than overriding parent `__call__`.

Verify:
- `python -c "import src.lattices"` succeeds.
- The spec files group cleanly by phase: `tests/sage_spec/misc.sage` first, then `tests/lattice_spec/interface_semantics.sage` and `test_lattices_written_feedback_spec.py`, then dual/discriminant/subobject specs, then root/Weyl/Coxeter/Eichler specs, then `todo_general_indefinite_isometry_spec.py`.
- Public lattice code no longer relies on raw Sage-object admission or Sage-private discriminant internals on its external contract.