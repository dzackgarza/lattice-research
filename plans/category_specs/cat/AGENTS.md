# cat subtree

This subtree owns the category of categories, written `Cat()`.

Rules:

- `Cat()` is intentionally barebones. Do not build a deep subcategory hierarchy here.
- Every project category and subcategory is an object of `Cat()`.
- Maintain the required subtree documentation before extending code:
  - `docs/SAGE_INVENTORY.md` records Sage classes, methods, signatures, and source paths.
  - `docs/MAPPING.md` records the mathematical mapping from Sage's category/functor
    machinery to the project surface.
  - `docs/TRIAGE.md` records current blockers and validation scope.
- Category-object containment rules live here first. Other subtrees should eventually
  reuse the `Cat.ParentMethods` mixins instead of hand-writing `__contains__`.
- Category objects expose private hooks for containment:
  - `_sage_super_categories()`
  - `_sage_object_classes()`
  - `_sage_morphism_classes()`
- Uniform containment checks test, in order, whether the candidate is a subcategory,
  an object, or a morphism in the category.
- `leq` and `geq` are readable shorthands for Sage's subcategory relation.
- Standard regressive constructions (`Subobjects`, `Quotients`, `Subquotients`,
  `ObjectsOver`, `ObjectsUnder`, `CartesianProducts`, `Homsets`, `Endsets`,
  `Autsets`) are declared here as shared category-object boilerplate.
- Sage functors and construction functors are morphism-like objects in this subtree.
  Document Sage's functor machinery here before adding wrappers elsewhere.
- `Cat().Constructors()` is intentionally empty until a real category-object
  constructor entry point is needed.
- Nontrivial algorithms belong under `implementations/`; trivial Sage wiring stays
  on the category surface.
