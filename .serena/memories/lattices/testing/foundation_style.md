# Lattice foundation testing style

Use family-based mathematical specification tests, not wrapper smoke tests.

Rules:
- Group tests by lattice family or theorem (`A_n`, `B_n`, `C_n`, `D_n`, `E_n`, `F_4`, `G_2`, standard indefinite models, minimal routing tests).
- Assert exact theory-backed invariants: Gram matrix, determinant, parity, signature, scale, simple-root norms, simple-root divisibilities, isotropy, and exact discriminant-form isometry classes.
- Use only semantic foundation constructors in tests (`Lattice.*`, `rescale`, `DiscriminantGroup.from_invariants_and_gram`, etc.). If the vocabulary is missing, add it to `src/` instead of inventing test-local constructions.
- Routing tests against Sage should be narrow boundary tests only; do not spend the suite proving Sage works.
- Avoid weak assertions like cardinality-only or prime-power-only checks when the exact discriminant form is known.
- Avoid iterator trivia like `next(iter(L.gens()))` when the exact generator set is known.
- Prefer direct mathematical equalities (`== 1`) over QC-noise style (`is_one()`) in assertions.

Semantic guidance exposed by this work:
- `scale()` is the ideal `<beta(L,L)>` in `ZZ`.
- Form multiplication belongs under `twist(...)` / `rescale(...)`, not `scale(...)`.
- `discriminant_class()` is trivial on integral lattice elements of `L`; the nontrivial semantic operation belongs on dual/rational lattice elements, suggesting a future `DualLattice` layer.
- Do not introduce custom mathematical algorithms when Sage/GAP/Julia already own the computation; the repo should compose exact backend computations into a semantic interface.
