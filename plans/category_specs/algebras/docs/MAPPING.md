# Algebras Mapping

`Algebras(R)` is the category of algebras over `R`. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A matrix ring is also an algebra over its base ring; algebra methods should not be redeclared in the ring subtree. |
| `AlgebrasWithBasis(R)` | A future `Algebras(R).WithBasis()` subcategory | Basis-dependent methods require a separate mathematical restriction. |
| `subalgebra`, `center`, `radical`, derivation and Hochschild methods | Algebra parent method surface | These methods depend on algebra structure, not merely ring or module structure. |
| Topological algebras | `Algebras(R)` plus `topological_spaces` | Topological-space methods belong to the topological-space subtree and should be inherited. |
