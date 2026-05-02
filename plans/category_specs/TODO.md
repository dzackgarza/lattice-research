# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Audit Todo

- [ ] Mark overrides explicitly and distinguish them from genuinely new methods
  introduced by a subcategory. A reader should be able to tell whether a method
  refines inherited behavior or first becomes mathematically meaningful at that
  category.
- [ ] Audit every method for highest valid mathematical placement. Place each method
  where implementers primarily think about the corresponding abstraction; for example,
  algebra specs should not restate set-theoretic domain and codomain obligations for
  morphisms.
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
