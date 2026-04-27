# cat subtree

This subtree owns the category of categories, written `Cat()`.

Rules:

- `Cat()` is intentionally barebones. Do not build a deep subcategory hierarchy here.
- Every project category and subcategory is an object of `Cat()`.
- Every project category class must inherit from the registered re-exported bases in
  `category_specs.cat` (`Category`, `Category_singleton`, `CategoryWithAxiom`,
  `Homsets`, `HomsetsCategory`, etc.), not directly from `sage.categories.*`.
- `base_category_types.py` is the only Sage category-base touch point. It explicitly
  lists Sage base category classes the tree subclasses. Do not add arbitrary Sage
  category objects there merely because a spec names them as supercategories.
- If a Sage category base has no registered re-export here, add that re-export in
  `cat/base_category_types.py` first; do not use the raw Sage base as a superclass in
  another subtree.
- `Cat` uniformizes category-object constructions. If every category should expose an
  operation, define it on `Cat.ParentMethods` and let registration adapt it into
  Sage's category-object method path.
- Maintain the required subtree documentation before extending code:
  - `docs/SAGE_INVENTORY.md` records Sage classes, methods, signatures, and source paths.
  - `docs/MAPPING.md` records the mathematical mapping from Sage's category/functor
    machinery to the project surface.
  - `docs/TRIAGE.md` records current blockers and validation scope.
- Category-object method rules live here first. Other subtrees should eventually reuse
  the `Cat.ParentMethods` surface instead of hand-writing duplicate category-object
  operations.
- Category objects expose private hooks for containment:
  - `_sage_super_categories()`
  - `_sage_object_classes()`
  - `_sage_morphism_classes()`
- For any category `C`, `X in C` can mean object membership or morphism membership.
  For `C = Cat()`, membership is category-object membership only; functors live in
  `A.Hom(B)`, `A.End()`, and `A.Aut()`.
- `leq` and `geq` are readable shorthands for Sage's subcategory relation.
- `Hom`, `End`, and `Aut` are category-object methods in `Cat.ParentMethods`.
- Standard regressive constructions (`Subobjects`, `Quotients`, `Subquotients`,
  `ObjectsOver`, `ObjectsUnder`, `CartesianProducts`, `Homsets`, `Endsets`,
  `Autsets`) are declared here as shared category-object boilerplate.
- Sage functors and construction functors are morphism-like objects in this subtree.
  Document Sage's functor machinery here before adding wrappers elsewhere.
- `Cat().Constructors()` is intentionally empty until a real category-object
  constructor entry point is needed.
- Nontrivial algorithms belong under `implementations/`; trivial Sage wiring stays
  on the category surface.
