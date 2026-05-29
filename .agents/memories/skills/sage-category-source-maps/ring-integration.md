---
title: Sage Ring Construction Entry Points
status: active
date: 2026-05-29
---
# SageMath Ring Construction Entry Points

Structured map of major ring construction entry points in SageMath.

## Base ring singletons

Globally unique instances constructed once at import time: `ZZ` (`IntegerRing_class`),
`QQ` (`RationalField`), `AA` (`AlgebraicRealField`), `QQbar` (`AlgebraicField`), `RR`
(`RealField_class`), `RDF` (`RealDoubleField_class`), `CC` (`ComplexField_class`), `CDF`
(`ComplexDoubleField_class`), `RLF`/`CLF`
(`RealLazyField_class`/`ComplexLazyField_class`), `RBF` (`RealBallField`), `CBF`
(`ComplexBallField`), `RIF` (`RealIntervalField_class`), `CIF`
(`ComplexIntervalField_class`).

## Finite fields

`GF(q)` for prime fields and extension fields, with Conway polynomial support.
`GF(p, n)`, `GF(p^n)`.

## Polynomial rings

`PolynomialRing(R, n, names=...)`, `R['x']`, `R['x,y']`, multivariate, Laurent
polynomial rings `R['x,x^-1']`, power series rings, Puiseux series rings.

## p-adic rings

`Zp(p)`, `Qp(p)`, `Zp(p, prec)`, `Qp(p, prec)`, unramified and eisenstein extensions.
`Zq`, `ZqFP`, `ZqCR`, `ZqFM` for different p-adic implementations.

## Localizations and quotients

`R.localize(S)`, `R.quotient(I)`, `R.quo(I)`, `R.fraction_field()`.

## Completions

`R.completion(p)`, `R.completion(I)` for ideal-adic completions.

## Matrix and group rings

`MatrixRing(R, n)`, `MatrixSpace(R, m, n)`, `GroupRing(G, R)`.
