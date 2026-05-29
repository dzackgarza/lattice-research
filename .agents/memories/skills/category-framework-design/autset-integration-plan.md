---
title: Autset Integration Plan
status: active
date: 2026-05-29
---
# Autset Integration Plan

## Structural Hierarchy

```
Homsets → Endsets (axiom: Endset, extra_super: Monoids)
               → Autsets (axiom: Autset, extra_super: Groups)
```

- Endsets represent endomorphism monoids.
- Autsets represent groups of invertible endomorphisms (automorphism groups).

## Implementation Steps

1. Register the `Autset` axiom in `src/sage/categories/category_with_axiom.py`: Add
   `"Autset"` to `all_axioms` after `"Endset"`.
2. Define Autset Category within Endsets in `src/sage/categories/homsets.py` with proper
   `extra_super_categories`.
3. Add `Autset()` SubcategoryMethod so `SomeCategory().Homsets().Autset()` dispatches
   correctly.
4. Integrate with `Homset.__init__` for automatic dispatch: when `domain is codomain`,
   place the homset in the appropriate endset/autset category.
5. Implement domain-specific `extra_super_categories` for module, ring, and algebra
   categories.
