# Algebras Mapping

`Algebras(R)` is the category of algebras over `R`. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A matrix ring is also an algebra over its base ring; algebra methods should not be redeclared in the ring subtree. |
| `AlgebrasWithBasis(R)` | `Algebras(R).WithBasis()` | `WithBasis` is shared module/vector-space vocabulary; the algebra surface adds multiplication-on-basis methods. Bases are families of algebra elements, while `one_basis()` and `product_on_basis()` use basis indices. |
| `basis()` | `AlgebraBasis` | A basis of an algebra is a Sage family of algebra elements, not a Python-native collection. |
| `one_basis()` and `product_on_basis()` | `AlgebraBasisIndex` | Sage basis multiplication is indexed by basis keys, so the spec names the mathematical index type. |
| `algebra_generators()` | `AlgebraElementFamily` | Algebra generators form a family of algebra elements, not a generic set family. |
| `FiniteDimensionalAlgebrasWithBasis(R)` | `Algebras(R).FiniteDimensional().WithBasis()` | `FiniteDimensional` is shared vector-space vocabulary. This intersection is where Sage implements radical, center, idempotent lifting, Peirce decomposition, and semisimple quotients for algebras with basis. |
| `SemisimpleAlgebras(R)` | `Algebras(R).Semisimple()` | Semisimplicity uses the shared `Semisimple` axiom; algebra subcategories supply the algebra-specific method surface. |
| `CommutativeAlgebras(R)` | `Algebras(R).Commutative()` | Commutativity uses the shared `Commutative` axiom; this algebra surface records algebra-specific consequences without redefining the axiom. |
| `WithBasis`, `FiniteDimensional`, `Commutative`, `Semisimple` | shared axiom names from `axioms.py` | The algebra subtree contributes algebra-specific method surfaces for these restrictions instead of defining separate algebra-only axiom names. |
| `subalgebra`, `center`, `radical`, derivation and Hochschild methods | Algebra parent method surface | These methods depend on algebra structure, not merely ring or module structure. |
| Quotients, subobjects, Cartesian products, tensor products, duals | `Algebras(R).<Construction>()` | These are construction categories attachable to arbitrary algebra subcategories by `category_of(self)`. |
| Topological algebras | `Algebras(R)` plus `topological_spaces` | Topological-space methods belong to the topological-space subtree and should be inherited. |
