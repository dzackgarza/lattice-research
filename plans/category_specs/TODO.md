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
- [ ] Promote admitted-name variadic-split smoke coverage to concrete regression
  examples when the missing fixtures or implementations exist:
  `Modules(E).Constructors().FPModuleFromCokernelMap` needs a concrete graded-module
  morphism fixture; `Modules(ZZ).Constructors().IntegerLatticeFromOrderElement` needs
  an absolute-order element fixture; `Rings().Constructors().ZqWithPrecisionCaps` and
  `QqWithPrecisionCaps` need a reviewed q-adic lattice-precision path because Sage's
  installed `Zq`/`Qq` factories coerce `prec` to an integer before constructing the
  unramified extension; `Modules(R).Quotients().ParentMethods.quotient_by_*` are
  abstract quotient obligations with no concrete Sage quotient implementation yet
  exposing the split names; `Algebras(R).ParentMethods.subalgebra` and the split ideal
  methods are abstract method names without a concrete finite-dimensional algebra
  fixture implementing them; `Lattices(ZZ).OverIntegers().ParentMethods.short_vectors`
  and `short_vectors_up_to_sign` are abstract lattice obligations without a concrete
  lattice fixture refined far enough to exercise the project method names.
- [ ] Audit for uniformizing opportunities across category trees where several modules
  express the same mathematical construction with different names or shapes.
- [ ] Add mathematical docstrings whenever a spec introduces a new method. The docstring
  should define the method mathematically rather than merely restating its return type.
