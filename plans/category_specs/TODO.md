# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Audit Todo

- [ ] Constructor smoke coverage is complete except for abstract algebra constructor
  families whose source categories do not yet have concrete Sage-backed routing:
  `Algebras(R).Constructors().free_algebra_from_magma`,
  `free_algebra_from_semigroup`, `free_algebra_from_monoid`,
  `free_algebra_from_group`, `free_algebra_from_additive_semigroup`,
  `free_algebra_from_additive_monoid`, `free_algebra_from_additive_group`, and
  `from_multiplication_tensor`. The smoke admits these names but cannot yet assert
  result refinement for them.
- [ ] Scope each remaining variadic Sage surface by reading the docs and source,
  tracing the finite code paths, splitting the surface into named methods or
  constructors, recording the mapping, and stubbing the resulting spec methods.
- [ ] Add an early warning for redundant abstract-method redefinitions, preferably as a
  `just` recipe or script, so specs do not restate inherited obligations.
- [ ] Audit for uniformizing opportunities across category trees where several modules
  express the same mathematical construction with different names or shapes.
- [ ] Add mathematical docstrings whenever a spec introduces a new method. The docstring
  should define the method mathematically rather than merely restating its return type.
