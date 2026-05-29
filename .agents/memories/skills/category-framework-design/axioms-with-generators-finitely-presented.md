---
title: Axioms: WithGenerators, FinitelyPresented
status: active
date: 2026-05-29
---
# Axioms: WithGenerators, FinitelyPresented, and Structural Patterns

## WithGenerators axiom

The correct precedent is `FinitelyGeneratedAsMagma`: a dedicated axiom name (not
WithBasis, not FinitelyPresented) that adds a distinguished generating set.
Register in `all_axioms`:

```python
import sage.categories.category_with_axiom as _cwa
_cwa.all_axioms += ("WithGenerators",)
```

The axiom class provides `module_generators()` (distinguished finite generating tuple,
NOT a basis), `gens()` shorthand, and `ngens()`.

## FinitelyPresented modules over PIDs

Uses `FinitelyPresented` axiom with structure theorem semantics: `free_part()`,
`invariant_factors()`, `torsion_part()`, `elementary_divisors()`. Dedekind domain
expansion is prepared for ideal-class and projective-module data but not required yet.

## Homsets as module objects

`Hom_R(M, N)` is itself a finitely generated `R`-module — encoded via
`extra_super_categories` returning `[MyFGModules(R)]`.

## Endsets and Autsets

- Endset: monoid under composition
- Autset: group of units in the endset monoid
- End_R(M) is an R-algebra
- Regular module `R` is rank-1 free: `End_R(R) ≅ R` as R-algebras
