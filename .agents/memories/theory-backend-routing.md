# Theory Backend Routing

Trigger: before mathematical implementation work, backend wiring, exact algorithm work, or tests that encode mathematical computation.

Start with `theory/backends/software-capability-map.md`. Its invariant is that repo code should not implement mathematical algorithms locally when a mature open-source exact system already provides the operation.

Required reading order from the theory docs:

1. `theory/backends/software-capability-map.md`
2. `theory/backends/library-integration.md`
3. `theory/backends/abstract-to-external-mapping.md`
4. The specific backend note for the selected tool
5. `research-source-acquisition` if the source or theorem basis is uncertain

Preferred routing from the current theory docs:

- SageMath for orchestration and Sage category machinery.
- GAP for finite groups, group actions, orbits, and stabilizers.
- Singular through Sage or direct bridge for Groebner, singularities, local algebra, and normalization.
- Macaulay2 for algebraic geometry, sheaves, divisors, Hilbert polynomials, and blowups after current support is verified.
- Oscar/Hecke/Nemo/AbstractAlgebra for lattices, quadratic forms, number theory, discriminant groups, primitive embeddings, and exact algebra.
- Indefinite.jl for indefinite lattice isometry and orbit computations.
- CARAT only for positive-definite forms and finite matrix-group auxiliary work.
- PARI/GP, FLINT, Arb, Nemo, and Sage wrappers for exact arithmetic kernels.
- polymake, Normaliz, Sage wrappers, and Oscar integration candidates for polyhedra, cones, toric and combinatorial geometry after audit.

Gap protocol: if an implementation reaches an undocumented operation, stop. Do not add an ad hoc helper. Create or update a backend-gap research card with the exact operation, objects, candidate software, sources checked, and why the current path is blocked.

Verification: a plan/card/backend note should use the routing statuses from the map: `preferred-backend`, `bridge-needed`, `candidate-backend`, `true-gap`, or `out-of-scope`.
