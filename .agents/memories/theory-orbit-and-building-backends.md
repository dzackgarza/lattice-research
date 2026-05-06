# Theory Orbit And Building Backends

Trigger: working on vector orbits, isotropic line/plane/flag orbits, Tits buildings, cusp enumeration, Dawes algorithms, or subgroup-sensitive orthogonal-group computations.

Use these owner notes:

- `theory/algorithms/dawes-nonisotropic-vector-orbits.md` for Dawes Algorithms 2.1-2.3.
- `theory/algorithms/dawes-orbit-backend.md` for the repo plan around non-isotropic vector orbit backend wiring.
- `theory/algorithms/isotropic-gamma-orbit-backend.md` for isotropic line/plane/flag orbits under structured subgroups.
- `theory/algorithms/buildings.md` and `theory/backends/buildings.md` for Tits building and Baily-Borel boundary computations.
- `theory/backends/indefinite-jl.md` and `theory/backends/indefinite-isometry.md` for indefinite-form backend routes.
- `theory/backends/carat.md` for positive-definite and finite matrix-group auxiliary work only.

Rules from the theory docs:

- Dawes Algorithm 2.1 handles non-isotropic vectors with definite perpendicular complement for arbitrary `Gamma`.
- Dawes Algorithms 2.2 and 2.3 handle a narrower indefinite-complement case under explicit discriminant-form and surjectivity hypotheses.
- Do not use the Dawes non-isotropic backend for Sterk-style isotropic cusp claims.
- For isotropic subgroup orbits, use ambient Dutour-Sikiric or buildings-style orbit/stabilizer data plus finite quotient or double-coset splitting. Do not require infinite subgroup generators merely to compute `Gamma`-orbits.
- Do not create a new public `Gamma` noun for these backends; keep public API centered on existing lattice orthogonal group/subgroup nouns.
- CARAT `Aut_grp` and `Isometry` require positive-definite form input. Do not use them for indefinite forms.
- CARAT `Orbit` should be bounded with `-L` when an orbit may be infinite, and `Normalizer` should be preceded by a finiteness check.

Stop conditions from the isotropic plan: stop and split prerequisite work if the subgroup quotient image cannot be computed, if ambient matrices cannot be recovered from quotient words, if the subgroup is only an opaque condition set with no finite-image data, or if the task needs a new shared mathematical noun not covered by the base.

Verification: isotropic Enriques degree-2 work should reproduce the `5` zero-cusps and `9` one-cusps from the Dutour-Sikiric/Hulek Case 1 table before claiming the backend route is correct.
