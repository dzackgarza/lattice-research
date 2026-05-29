---
title: Homsets — the Structural Core
status: active
date: 2026-05-29
---
# Homsets — the Structural Core

Key structural relationships:

- `Hom_R(M, N)` is itself a finitely generated R-module
- `End_R(M)` is an R-algebra
- `Autset` nested inside `Endset`, which is nested inside `Homsets`

## Dual modules

`M^* = Hom_R(M, R)` is a rank-n free module with the dual basis.
The dual of a morphism `f: M -> N` is `f^*: N^* -> M^*`. Double dual is naturally
isomorphic to M for free modules.

## Endset algebra structure

The endomorphism ring `End_R(M)` carries composition as multiplication, pointwise
addition, and scalar action from `R`. The category encoding:
`Endset.extra_super_categories()` returns `[Algebras(R)]`, making `End_R(M)` a Sage
`Algebras(R)` object with the right parents.

## Rank semantics

`rank(M)` = dimension of `M ⊗_R K` over `K = Frac(R)`. For torsion modules `rank=0`, for
free modules equals the number of generators.
For mixed modules, rank of the free part only.

## Homsets class skeleton

```python
class Homsets(HomsetsCategory):
    def extra_super_categories(self):
        return [MyFGModules(self.base_category().base_ring())]

    class ParentMethods:
        @cached_method
        def base_ring(self):
            return self.domain().base_ring()

        @cached_method
        def zero(self):
            return self.domain().hom(
                [self.codomain().zero()] * self.domain().ngens(),
                self.codomain())

    class Endset(CategoryWithAxiom_over_base_ring):
        def extra_super_categories(self):
            from sage.categories.algebras import Algebras
            return [Algebras(self.base_category().base_ring())]
```
