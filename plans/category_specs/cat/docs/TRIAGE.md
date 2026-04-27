# Cat Triage

Source for this pass: `cat/docs/SAGE_INVENTORY.md`, `cat/docs/MAPPING.md`, and the
local smoke surface `cat/smoketest.sage`.

The `cat` subtree is intentionally barebones, but it now has the required
documentation spine and a Sage-grounded method surface.

## Current Alignment

- `Cat()` declares Sage/project category objects as objects of the category of
  categories.
- `Cat()` treats Sage `Functor` and `ConstructionFunctor` instances as
  morphism-like objects for uniform containment.
- `Cat.ParentMethods` owns the uniform containment hooks:
  `_sage_super_categories`, `_sage_object_classes`, `_sage_morphism_classes`, and
  `__contains__`.
- `leq`, `geq`, `<=`, and `>=` are shorthands for Sage's `is_subcategory` order.
- Standard construction navigation is declared for `Subobjects`, `Quotients`,
  `Subquotients`, `ObjectsOver`, `ObjectsUnder`, `CartesianProducts`, `Homsets`,
  `Endsets`, and `Autsets`.
- `Cat().Constructors()` is present as an explicitly empty constructor namespace.
- Nontrivial implementation code is not present; `cat/implementations/AGENTS.md`
  documents that this is currently spec-only.

## Corrections From The First Scaffold

- The original inventory only listed Sage modules. It now records concrete Sage
  classes, method signatures, source files, and source lines for category,
  functor, construction-functor, construction-category, and homset machinery.
- `Cat().__contains__` no longer bypasses the uniform containment hooks. It now
  delegates to the same subcategory/object/morphism check used by
  `Cat.ParentMethods`.
- The smoke surface now uses the subtree `smoke_case` pattern and covers the empty
  constructor namespace, functor containment, slice/coslice construction, and
  standard construction methods.
- The implementation directory is tracked and explicitly marked as empty for now.

## Remaining Design Work

- Existing top-level categories have not yet been refactored to inherit or copy the
  `Cat.ParentMethods` containment mixin. That is a follow-up refactor, not part of
  the stub.
- `CatHomsets` is a direct local wrapper. It does not yet inherit from the
  repository's `HomsetsOf` class.
- Natural transformations are not modeled. The current morphism surface is Sage
  functors and construction functors only.
- The list of `_sage_morphism_classes()` is intentionally conservative:
  `Functor` and `ConstructionFunctor`. Additional Sage functor subclasses should be
  added only when a concrete method surface needs them.

## Source Note: `CatHomsets` And Generic `HomsetsOf`

- Searched: local `category_specs/homsets/__init__.py`,
  `sage/categories/homsets.py`, and the first `CatHomsets` smoke attempt.
- Found: the generic project `HomsetsOf` owns `Endset` and `Autset` axiom classes
  whose base-category wiring currently assumes `HomsetsOf`; direct subclassing for
  `CatHomsets` produced an axiom/base-class mismatch during `Endset` construction.
- Conclusion: inference -- keep `CatHomsets` as a direct category wrapper until
  generic homsets can accept category-specific element surfaces without breaking
  `Endset` and `Autset` registration.
- Confidence: Medium.
- Gaps: I have not done a full redesign of the top-level `homsets/` subtree in this
  pass.

## Validation Scope

Run `sage cat/smoketest.sage` after layout and documentation edits are complete.
This smoke is structural only; it does not prove that existing project categories
already use the new containment mixin.
