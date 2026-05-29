---
title: ModulesWithForms Category ABC Contracts
status: active
date: 2026-05-29
---
# ModulesWithForms Category: ABC Contracts

Authoritative specification of the category-level contract for the lattice redesign.
This file supersedes the earlier `BilinearModules`-first framing.

## Foundation

`Modules(R)` patches Sage's `Modules(R)` surface for finitely presented PID-module
structure independent of forms.
`Modules(R).WithForm()` is the form-bearing refinement, implemented by
`ModulesWithForms(R)`.

`ModuleBaseRings` targets commutative PIDs: `ZZ`, `Zp(p)`, `QQ`, `RR`, `CC`, `QQbar`,
finite fields `GF(p^n)`.

Installation: `ring._refine_category_(ModuleBaseRings())` at import time.
Overrides in `ModuleBaseRings.ParentMethods` drive the enriched surface: `r * R`,
`R / I`, `R^n`, localize, completion, fraction_field.

## Presented Object Identity

A free bilinear module is `(M, beta, B)` where `B` is the selected generating set.
Changing generators changes the presented object.
This is the central divergence from Sage's ambient-vector-space convention.

Named cases: `R`-lattice = free finitely generated bilinear `R`-module with
nondegeneracy/integrality predicates.
`Lattice` means integral `ZZ` case.

## Form Codomains

Codomain strata: `Integral` (S=R), `Rational` (S=Frac(R)), discriminant quotient
codomains (K/R, K/2R, QQ/ZZ, QQ/2ZZ).

## Core ABCs

`ModuleForm`: ambient_module, domain, codomain, tensor_degree,
scalar_action_endomorphism, evaluate, gram_matrix. `BilinearForm` and `QuadraticForm`
refine it.

## Parent and Element Methods

`ModulesWithForms.ParentMethods`: form(), gens(), zero(), base_ring(), free_part(),
torsion_part(), Hom(), dual(), span(), cardinality(), End().

`ModulesWithForms.ElementMethods`: parent(), add, neg, scalar multiplication, equality,
hash, to_vector, span().

Uniform diagonal syntax: `v.q()` is allowed everywhere.
In Bilinear(), means `b(v,v)`. In Quadratic(), means quadratic evaluation.

## Axiom Hierarchy

`Bilinear()`, `Quadratic()`, `Free()`, `Torsion()`, `NonDegenerate()`, `Integral()`,
`Rational()`, `TensorProducts()`, `CartesianProducts()`, `DualObjects()`, `Homsets()`.

Downstream: `Lattices(R)` = Bilinear().Free().NonDegenerate().Integral().
`DiscriminantBilinearForms(R)` = Bilinear().Torsion() with quotient-valued codomain.

## Cokernels and Discriminant Descent

Generic construction: build kernel/image/cokernel in PID module sense, determine if form
data descends, construct descended form, promote.
`L -> L^# -> A_L = coker(L -> L^#)`.

## Sage Wiring Notes

Follow pattern of `sage.categories.modules.Modules`. `_Hom_` is internal hook; public
contract is `M.Hom(N)`. Elements must be genuine Sage `Element` or `ElementWrapper`
instances. Public lattice objects must not inherit from Sage lattice implementation
classes.
