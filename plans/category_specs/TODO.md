# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Audit Todo

- [ ] Finish the method-placement audit outside the foundational pass, and resolve
  these scoped leftovers:
  - `sets/subcategories/real_set.py`: decide whether `ambient`, `lift`, `retract`,
    `union`, `intersection`, `complement`, `difference`, `symmetric_difference`, and
    `is_subset` need real-interval-normalized methods or should route entirely through
    `Sets()` and `Sets().Subobjects()`.
  - `sets/homsets.py` and `topological_spaces/homsets.py`: decide whether
    `SetEndCategory.ParentMethods.base_set`,
    `TopologicalSpaceEndCategory.ParentMethods.base_space`, and
    `MetricSpaceEndCategory.ParentMethods.base_space` are useful mathematical aliases
    or redundant with the generic `End_C(A)` domain.
  - `topological_spaces/homsets.py`: decide whether `_ContinuousMaps.preimage` is a
    topological subspace operation or duplicate set-map inverse-image vocabulary.
  - `cat/`, `sets/`, and `topological_spaces/` slice/coslice construction files:
    decide whether `structure_domain` and `structure_codomain` should be universal
    construction vocabulary.
- [ ] Spot-check every public method for mathematical well-definedness and nontrivial
  content. If a method is meaningful only on a different object, move it to that
  owner or expose it through the relevant morphism. For example,
  `discriminant_class()` is nontrivial for dual-lattice elements via
  `L^* -> L^*/L`, but it is always zero on elements of `L`.
- [ ] Check that smoke tests exercise all constructors, that every constructor refines
  its result, and that constructor refinement targets the tightest subcategories
  possible, including derived cases such as a finite-rank free module over a finite
  ring being finite.
- [ ] Check that refinement smokes surface the gap between current Sage implementations
  and the mathematical spec, rather than trying to make current Sage objects pass.
- [ ] Audit for variadic specs that slipped in and create an inventory of remaining
  variadic signatures.
- [ ] Scope each remaining variadic Sage surface by reading the docs and source,
  tracing the finite code paths, splitting the surface into named methods or
  constructors, recording the mapping, and stubbing the resulting spec methods.
- [ ] Add an early warning for redundant abstract-method redefinitions, preferably as a
  `just` recipe or script, so specs do not restate inherited obligations.
- [ ] Audit for uniformizing opportunities across category trees where several modules
  express the same mathematical construction with different names or shapes.
- [ ] Add mathematical docstrings whenever a spec introduces a new method. The docstring
  should define the method mathematically, e.g. explaining what
  `discriminant_class()` means rather than merely restating its return type.
