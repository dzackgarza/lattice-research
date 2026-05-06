---
id: DECISION-VINBERG-WRAPPING-STRATEGY
trackerStatus:
  type: decision
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn: []
title: Decide Vinberg algorithm source strategy — wrap, adapt, or reimplement
status: in-progress
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Vinberg Algorithm Source Strategy

## Summary

Vinberg's algorithm is a well-known and relatively simple algorithm for computing
the fundamental polytope and Coxeter diagram of a reflective hyperbolic lattice.
At least four implementations exist:

1. **VinbergsAlgorithmNF.jl**: Julia implementation with number field support,
   PID algebraic integers. Uses Hecke.jl. Fast (Bugaenko 8D <10 min).

2. **AlVin C++**: Supports ℚ, ℚ(√d), ℚ(cos(2π/7)). Optimized.

3. **vinal Python/Sage**: Sage implementation using direct quadratic Diophantine
   solving. Easiest to adapt to the repo's vocabulary.

4. **polyhedral_common edgewalk** (`LORENTZ_RunEdgewalkAlgorithm`): C++,
   vendored at `src/external/dutsik_polyhedral/polyhedral_common`, with Python
   wrapper bridge at `src.bak/backends/external/py_polyhedral/`. No number field
   support. Already has a `lorentzian_reflective_edgewalk` export in the wrapper.

## Decision Required

The project needs a single Vinberg-like function that fits into the category
spec vocabulary: given a hyperbolic lattice object `L` (with Gram matrix,
generators, and a control vector or canonical default), produce a list of
simple root vectors and the Coxeter matrix.

## Requirement

Choose whether the implementation should wrap one or more reference implementations,
adapt their algorithms into the repo's vocabulary, or write a new implementation based
on their approach. The resulting implementation work must accept a hyperbolic lattice
with a control vector and return simple roots, Coxeter matrix data, and fundamental
polytope data.

Candidates differ in:
- **Input format**: Can they consume our lattice objects, or do they need raw
  Gram matrices?
- **Signature**: Do they handle signature (1, n) for the full n we need (up to
  10-19)?
- **Number fields**: Are ℚ(√d) or cyclotomic fields needed for the Coble case?
- **Integration**: Subprocess wrapper vs Python import vs direct port.
- **Maintenance**: How much effort to keep working across Sage version changes?

## Acceptance Criteria

- The decision records the evaluation of each candidate (VinbergsAlgorithmNF.jl, AlVin
  C++, vinal Python/Sage, polyhedral_common edgewalk) against the project's needs:
  input format, signature range, number field support, parallelizability, and
  maintainability.
- The decision identifies which source or sources to use and at what level: subprocess
  wrapper, Python bridge, port to Sage, or another explicit route.
- The resulting feature card allocates the implementation work.

## Outcome

Once decided, create or update the feature card for the Vinberg wrapping/adaptation
implementation. The existing survey at
`.agents/memories/theory/backends/vinberg-algorithm.md` documents all four
implementations with enough detail to support this decision.
