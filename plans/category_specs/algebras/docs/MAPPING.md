# Algebras Mapping

`Algebras(R)` is the category of algebras over `R`. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A matrix ring is also an algebra over its base ring; algebra methods should not be redeclared in the ring subtree. |
| `AlgebrasWithBasis(R)` | `Algebras(R).WithBasis()` | `WithBasis` is shared module/vector-space vocabulary; the algebra surface adds multiplication-on-basis methods. Bases are families of algebra elements, while `one_basis()` and `product_on_basis()` use basis indices. |
| `FiniteDimensionalAlgebrasWithBasis(R)` | `Algebras(R).FiniteDimensional().WithBasis()` | `FiniteDimensional` is shared vector-space vocabulary. This intersection is where Sage implements radical, center, idempotent lifting, Peirce decomposition, and semisimple quotients for algebras with basis. |
| `SemisimpleAlgebras(R)` | `Algebras(R).Semisimple()` | Semisimplicity uses the shared `Semisimple` axiom; algebra subcategories supply the algebra-specific method surface. |
| `CommutativeAlgebras(R)` | `Algebras(R).Commutative()` | Commutativity uses the shared `Commutative` axiom; this algebra surface records algebra-specific consequences without redefining the axiom. |
| `subalgebra`, `center`, `radical`, derivation and Hochschild methods | Algebra parent method surface | These methods depend on algebra structure, not merely ring or module structure. |
| Quotients, subobjects, Cartesian products, tensor products, duals | `Algebras(R).<Construction>()` | These are construction categories attachable to arbitrary algebra subcategories by `category_of(self)`. |
| Topological algebras | `Algebras(R)` plus `topological_spaces` | Topological-space methods belong to the topological-space subtree and should be inherited. |
