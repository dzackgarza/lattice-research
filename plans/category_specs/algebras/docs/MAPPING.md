# Algebras Mapping

`Algebras(R)` is the category of algebras over `R`. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A matrix ring is also an algebra over its base ring; algebra methods should not be redeclared in the ring subtree. |
| `AlgebrasWithBasis(R)` | `Algebras(R).WithBasis()` | Basis-dependent methods require a separate mathematical restriction; bases are families of algebra elements, while `one_basis()` and `product_on_basis()` use basis indices. |
| `FiniteDimensionalAlgebrasWithBasis(R)` | `Algebras(R).FiniteDimensional().WithBasis()` | This is the finite-dimensional algebra-with-basis intersection where Sage implements radical, center, idempotent lifting, Peirce decomposition, and semisimple quotients. |
| `SemisimpleAlgebras(R)` | `Algebras(R).Semisimple()` | Semisimplicity is an algebraic restriction expressible as a local axiom. |
| `CommutativeAlgebras(R)` | `Algebras(R).Commutative()` | Commutative multiplication is an algebraic restriction, not merely a ring shortcut. |
| `subalgebra`, `center`, `radical`, derivation and Hochschild methods | Algebra parent method surface | These methods depend on algebra structure, not merely ring or module structure. |
| Quotients, subobjects, Cartesian products, tensor products, duals | `Algebras(R).<Construction>()` | These are construction categories attachable to arbitrary algebra subcategories by `category_of(self)`. |
| Topological algebras | `Algebras(R)` plus `topological_spaces` | Topological-space methods belong to the topological-space subtree and should be inherited. |
