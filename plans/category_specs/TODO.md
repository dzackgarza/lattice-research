# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`. Completed items leave this file; git history is
the archive.

## Audit Todo

- [ ] Continue the public-method well-definedness audit on these exact remaining
  surfaces:
  - `homsets/homsets.py`: decide whether `HomCategory.SubcategoryMethods.EndCategory`
    and `AutCategory`, plus the corresponding construction methods, are legitimate
    hom-category navigation or should be only the inherited universal selectors.
  - `homsets/endsets.py`: decide whether `EndCategory.SubcategoryMethods.AutCategory`
    and `EndCategoryOf.SubcategoryMethods.AutCategory` are legitimate end-category
    navigation or duplicated universal selectors.
  - `modules/subcategories/with_basis.py`: audit `linear_combination_of_basis`,
    `cokernel_basis_indices`, `HomCategory.ParentMethods.from_basis_map`, and
    `HomCategory.ElementMethods.on_basis` for basis-coordinate interop leakage versus
    genuine basis-bearing module structure.
  - `lattices/subcategories/over_dedekind.py`: decide whether
    `special_orthogonal_group()` and `stable_orthogonal_group()` belong on lattice
    objects or should be exposed through `Lattices(R).AutCategory()` refinements.
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
  should define the method mathematically rather than merely restating its return type.
