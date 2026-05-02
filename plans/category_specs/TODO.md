# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Audit Todo

- [ ] Continue the override/provenance audit outside the high-confidence formed-module
  and lattice pass already started. Remaining judgment areas outside this pass:
  `algebras/`, `modules/`, `posets/`, and `rings/`; constructor helper classes
  outside `cat/`, `homsets/`, `sets/`, `tensor_algebra_components/`, and
  `topological_spaces/`; foldable binary operations with overload stubs outside the
  scoped pass; and abstract method families whose mathematical owner is not locally
  obvious from the docstring.
  Scoped leftovers from this pass are exact set-subcategory provenance families:
  `sets/subcategories/cartesian_product.py::_CartesianProductSets` category hooks,
  `ParentMethods`, and `ElementMethods`;
  `sets/subcategories/countable.py::_CountableSets`,
  `_FiniteCountableSets`, and `_InfiniteCountableSets` category hooks and
  enumeration/cardinality/random-element methods;
  `sets/subcategories/disjoint_union.py::_DisjointUnionEnumeratedSets`;
  `sets/subcategories/enumerated_from_iterator.py::_EnumeratedSetsFromIterator`;
  `sets/subcategories/facade.py::_FacadeSets`;
  `sets/subcategories/family.py::_FamilySets`;
  `sets/subcategories/finite.py::_FiniteSets`;
  `sets/subcategories/finite_enumerated_set.py::_FiniteEnumeratedSetObjects`;
  `sets/subcategories/finite_set_maps.py::_FiniteSetMapsSets`;
  `sets/subcategories/graded.py::_GradedSets.super_categories`;
  `sets/subcategories/group_actions.py::_GSets.__init__` and
  `_GSets.super_categories`;
  `sets/subcategories/image.py::_ImageSets`;
  `sets/subcategories/infinite.py::_InfiniteSets`;
  `sets/subcategories/integer_range.py::_IntegerRangeSets`;
  `sets/subcategories/non_negative_integers.py::_NonNegativeIntegersSets`;
  `sets/subcategories/partitioned.py::_PartitionedSets.super_categories`;
  `sets/subcategories/positive_integers.py::_PositiveIntegersSets`;
  `sets/subcategories/primes.py::_PrimesSets`;
  `sets/subcategories/real_set.py::_RealSets.ParentMethods` real-subset operations;
  `sets/subcategories/recursively_enumerated.py::_RecursivelyEnumeratedSets`;
  `sets/subcategories/totally_ordered.py::_TotallyOrdered`;
  `sets/subcategories/totally_ordered_finite.py::_TotallyOrderedFiniteSets`; and
  `sets/subcategories/uncountable.py::_UncountableSets`.
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
