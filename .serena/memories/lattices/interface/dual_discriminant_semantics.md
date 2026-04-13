# Dual/discriminant interface semantics

When working in `src/lattices/`, treat discriminant lifts and submodules semantically rather than through raw vectors.

- Trigger: editing `Lattice`, `DualLattice`, `DiscriminantGroup`, or backend code that touches discriminant lifts, spans, or orthogonal complements.
- Rule: `DiscriminantGroupElement.lift()` should mean a lift to the dual lattice as a mathematical object. If backend interop needs the raw Sage representative vector, expose that explicitly as `lift_vector()` rather than overloading the semantic method.
- Rule: do not assume a lattice/module basis matrix is square. Genuine embedded submodules, such as isotropic lines in `U`, have rectangular basis matrices. Coordinate extraction must solve against the transposed basis matrix rather than using `.inverse()`.
- Rule: spans and orthogonal complements should return the most specific correct noun. If the result is degenerate, keep it in `FreeBilinearModule` rather than forcing it into `Lattice`.
- Rule: use Sage linear algebra and native exact objects for these constructions; do not add custom search/enumeration algorithms to fake missing generality.
- Verify: `Lattice.U().span([e])` yields a `FreeBilinearModule`-level object, and a discriminant generator of a nontrivial lattice lifts to a `DualLattice` element whose `ambient_vector()` is available for explicit interop.