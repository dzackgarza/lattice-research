# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Remaining Implementation Todo

- [ ] Admit pure topological constructors under the top-level constructor surface and
  refine named sets into their tight topological, subset, and subobject categories.
- [ ] Add a foldable-operation decorator for binary operations. It should standardize
  the paired overload pattern `op(x: XElement, y: XElement)` and
  `op(elements: Sequence[XElement])`, and make the sequence overload an explicit fold
  over the binary operation.
- [ ] Separate the forms subtree into its own hierarchy. Bilinear modules, quadratic
  modules, and related formed-module categories should ultimately live there rather
  than as incidental module subcategories.
- [ ] Build a constructor aggregation mechanism that mirrors Sage's mixin logic but
  exposes constructors in one discoverable place. The collector can live outside
  `Sets().Constructors()` and be populated by `Cat` at runtime by iterating over
  registered categories and adding prefixed names, such as
  `Posets().Constructors().from_digraph()` becoming `posets_from_digraph()` on the
  aggregate collector.
- [ ] Uniformize type exports by adding namespace objects such as `LatticeTypes`, with
  standard entries like `LatticeTypes.Category = LatticesCategory`, so callers can use
  one public namespace instead of importing every type alias individually.
- [ ] Ensure main category classes are defined in package `__init__.py` files. The
  initializer should be the readable index into the subtree, with subcategory files
  holding the detailed method surfaces.
- [ ] Standardize construction-category vocabulary. For example, `DualLattices` should
  not introduce a nonstandard verb when the existing categorical construction is
  `C.DualObjects()`.

## Audit Todo

- [ ] Document the axiom chain for each concrete class. For example,
  `NondegenerateSymmetricFiniteRankFreeBilinearModules` should state plainly that it
  represents `BilinearModules().Free().FiniteRank().Nondegenerate()`, or trace the
  chain from `Modules(R)` when that is the clearer source.
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
