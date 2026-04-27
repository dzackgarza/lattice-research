# Algebras Triage

## Current Alignment

- `Algebras(R)` exists as a top-level category over a base ring.
- Algebra-specific parent methods are centralized in `algebras/__init__.py`.

## Outstanding Decisions Needed

- Decide the first concrete constructor entries for `Algebras(R).Constructors()`.
- Decide whether `AlgebrasWithBasis(R)` should be modeled as `Algebras(R).WithBasis()`
  or as a more specific module-with-basis intersection category.
- Decide how matrix algebras should be split between `rings`, `modules`, and `algebras`
  without duplicating inherited method surfaces.
