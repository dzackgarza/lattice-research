---
trackerStatus:
  type: task
title: Audit standard type-package aliases after concrete Cat migration
status: in-review
priority: critical
planId: SPR-CAT-SURFACE-01KQN9
progress: 90
tags:
- category-specs
- implementation
- task
- cat
- types
- audit
- theme-audit-uniformity
---

# Audit standard type-package aliases after concrete Cat migration
Source: pasted backlog 2026-05-02.

Task: audit standard type-package aliases (Set, Matrix, etc.) and ensure they point to the new project types after the concrete Cat migration.

## Grounding

- `category_specs/types.py` is the centralized alias layer: category modules publish
  their standard mathematical type packages locally, and `types.py` chooses
  conventional aliases such as `Ring = RingsObject` and `RModule = ModulesObject`.
- `category_specs/cat/docs/MAPPING.md` says Sage category instances are the objects of
  `Cat()` and that `Cat.ParentMethods` owns the uniform category-object surface.
- `category_specs/cat/__init__.py` re-exports the concrete project wrapper
  `Category` from `cat/base_category_types.py`; that is the post-migration category
  base compatible with Sage category objects.
- `category_specs/modules/__init__.py` records `Matrix` and `vector` as Sage
  primitives in the module alias vocabulary, so the audit must not blindly replace
  `Matrix` with a nonexistent project package.

## Audit Result

- Added the missing `Category` export in `category_specs/types.py`, pointing it to the
  concrete project Cat wrapper base imported as `CatBaseCategory`.
- Left `CategoryObject = SageParent` and `CategoryElement = SageElement` unchanged:
  those aliases are generic object/element support for arbitrary categories, while
  `CatTypes.Object = CatObject` remains the precise object type package for objects of
  `Cat()`.
- Left `Set = SetsObject`, `Ring = RingsObject`, `RModule = ModulesObject`,
  `FormedModule = FormedModulesObject`, `BilinearModule = BilinearModulesObject`,
  `QuadraticModule = QuadraticModulesObject`, `TensorAlgebraComponent =
  TensorAlgebraComponentsObject`, `Poset = PosetsObject`, `TopologicalSpace =
  TopologicalSpacesObject`, and `Lattice = LatticesObject` as project-backed aliases.
- Left `Matrix = SageMatrix`, `MatrixSpace = SageMatrixSpace`, `DiGraph =
  SageDiGraph`, `CartesianProductFunctor = SageCartesianProductFunctor`, generic
  `Morphism = SageMorphism`, and other explicit support aliases Sage-backed because no
  project type package currently owns those support primitives.

## Negative Findings

- Searched: `category_specs/types.py`, `category_specs/cat/docs/MAPPING.md`,
  `category_specs/modules/__init__.py`, `category_specs/cat/__init__.py`,
  `category_specs/cat/base_category_types.py`, `category_specs/homsets/*.py`,
  `rg` import/use scans for `Category`, `CategoryObject`, `Set`, `Matrix`, `Hom`,
  `End`, `Aut`, and a Probe search for standard alias ownership.
- Found: `Set` and the main category-domain aliases already point to project type
  packages; `Matrix` is documented as a Sage primitive; `Category` was imported from
  `types.py` by Cat/homset surfaces but was not exported by `types.py`.
- Conclusion: inference - the only actionable alias mismatch in this audit surface is
  the missing canonical `Category` export; replacing the remaining Sage support
  primitives would invent project ownership not present in the mapped specs.
- Confidence: High.
- Gaps: This audit did not decide future Matrix/MatrixSpace ownership; that belongs to
  a separate matrix-object/category plan if the project later promotes matrices from
  Sage primitives to project-backed objects.

## Verification

- `python -m py_compile category_specs/types.py category_specs/cat/universal_subcategory_methods.py category_specs/cat/base_category_types.py category_specs/homsets/homsets.py category_specs/homsets/endsets.py category_specs/homsets/autsets.py` passed.
- `rg -n "from \\.\\.?types import Category\\b|from category_specs\\.types import Category\\b|\\bCategory = CatBaseCategory\\b|Category as CatBaseCategory" category_specs -g '*.py'` shows the new alias and the two static import consumers.
- `git diff --check` passed.
- `just test` passed Python syntax validation and Sage syntax validation, then failed
  at the existing global mypy gate on missing Sage/pytest stubs and duplicate
  `src.lattices` module naming. This is not a phase-local blocker for this alias
  audit.

## Complexity Justification
- Owner: C54
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Audit standard type-package aliases after concrete Cat migration
- Why this specific score:
  - This is a consistency audit across the naming layer (`Set`, `Matrix`, etc.) after migration. The work is moderate because it is less about introducing new behavior and more about verifying and realigning alias mappings across the project boundary.
- Item-specific evidence:
  - The file explicitly anchors scope to post-migration alias audit, which typically has hidden dependency impacts but a bounded surface if executed as verification-heavy pass.
