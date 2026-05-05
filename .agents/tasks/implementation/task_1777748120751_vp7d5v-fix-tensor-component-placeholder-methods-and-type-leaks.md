---
trackerStatus:
  type: task
title: Fix tensor-component placeholder methods and type leaks
status: in-review
priority: critical
planId: SPR-ALG-TENSOR-01KQN9
progress: 90
tags:
- category-specs
- implementation
- task
- tensors
- types
- theme-audit-uniformity
---

# Fix tensor-component placeholder methods and type leaks
Source: pasted backlog 2026-05-02.

Task: fix tensor-component placeholder methods that incorrectly return self or return None, add missing @final markers, and excise Sage option bags from the public surface.

## Complexity Justification
- Owner: C69
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Fix tensor-component placeholder methods and type leaks
- Why this specific score:
  - The task spans tensor-component behavior, return-type correctness, and constructor-surface hygiene simultaneously. Placeholder return fixes (`self`/`None`) can silently affect call contracts, so this carries higher impact than pure signature cleanup and justifies a high band.
- Item-specific evidence:
  - It names concrete risk vectors (`type leaks`, `@final` markers, `Sage option bags`) rather than a single-file rename, so validation must cover both runtime and typing expectations.

## Grounding

- `category_specs/tensor_algebra_components/docs/MAPPING.md` owns the public tensor-component surface: component parents and tensor elements expose `base_module()` and `tensor_type()`, component data stays constructor interop/private storage, `Tensor.structure_constants()` is the sole public product-tensor extraction surface, and `sym=` / `antisym=` are admitted only as constructor metadata.
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` records the Sage source vocabulary for `TensorFreeModule`, `FreeModuleTensor`, `tensor_type()`, component arrays, trace, and contraction.
- `.agents/tasks/spec/spec_01KQN9YGCB7YYAXVHWHQWGV281-freeze-tensor-symmetry-antisymmetry-storage-contraction-trace-display-an.md` freezes symmetry, component storage, trace, contraction, display, and index-notation decisions.
- `.agents/tasks/spec/spec_01KQN9J3WRAX3KGTBPA4Y1T1SC-expand-tensoralgebracomponents-beyond-the-minimal-tensor-constructor-sur.md` records that implementation follow-up is concrete method/constructor surface cleanup, not more owner-planning.

## Result

- Replaced the concrete `lift_from_product(...)` placeholder in `TensorAlgebraComponents.ParentMethods` with an abstract requirement. Tensor components still refine `Modules(R).TensorProducts()`, whose parent methods require pure-product lifting, but this subtree no longer ships a fake concrete implementation.
- Changed `Tensor.structure_constants()` to return `tuple[Matrix, ...]` instead of a raw Sage `self[:]` slice surface.
- Changed constructor-internal module-element coordinate extraction to return `tuple[RingElement, ...]` instead of a raw Sage slice surface before building multiplication tensors.
- Added the missing return annotation on `TensorAlgebraComponents.Constructors()`.
- Kept `sym=` and `antisym=` on `tensor(...)` and `component_module(...)` because the mapping admits them as constructor metadata. Kept `name=` and `latex_name=` because they are Sage tensor labels used by the current smoke surface rather than public mathematical option bags.

## Negative Finding

- Searched: current `category_specs/tensor_algebra_components/__init__.py`; `category_specs/tensor_algebra_components/docs/MAPPING.md`; `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`; tensor spec cards `spec_01KQN9YGCB7YYAXVHWHQWGV281` and `spec_01KQN9J3WRAX3KGTBPA4Y1T1SC`; repository search for `return self`, `return None`, `assert False`, `*args`, `**kwargs`, `kwargs`, `kwds`, `structure_constants`, and tensor constructor option names.
- Found: no current tensor-component method literally returning `self` or `None`; no public `*args` / `**kwargs` / `kwds` option bag in this subtree. The live placeholder was the concrete `assert False` body on `lift_from_product(...)`, and the live type leaks were raw Sage slice returns from `structure_constants()` and `_module_element_coordinates(...)`.
- Conclusion: inference - the pasted backlog phrase about `return self` / `return None` is stale for the current tensor-component file, but the card still named a real implementation defect: an ungrounded concrete placeholder and raw Sage component-slice leakage.
- Confidence: High for the current tensor-component file and docs searched; Medium for all historical migrated sources because deleted pre-migration plans were sampled through the currently referenced docs rather than exhaustively replayed.
- Gaps: no exhaustive audit of Sage's full tensor implementation internals was performed because this card targets the project public category-spec surface, not Sage source replacement.

## Verification

- `python -m py_compile category_specs/tensor_algebra_components/__init__.py`
- `git diff --check`
- `just check-abstract-redefinitions` from `category_specs/`
- `just smoke-file tensor_algebra_components/smoketest.sage` from `category_specs/` still fails on the pre-existing tensor constructor-refinement `__richcmp__` frontier tracked by `.agents/tasks/implementation/impl_01KQN9J3X47WFCYHM2CK8G1677-fix-tensoralgebracomponents-constructor-refinement-richcmp-failures-from.md`; every failed smoke assertion reports `AssertionError: Not implemented method: __richcmp__`.
