# Algebras Mapping

`Algebras(R)` is the category of algebras over `R`. Algebra-specific methods belong in
this subtree. Ring and module methods are inherited from `rings` and `modules`.

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| Matrix-ring algebra methods | `Algebras(R)` plus matrix-algebra subcategories | A matrix ring is also an algebra over its base ring; algebra methods should not be redeclared in the ring subtree. |
| `FreeAlgebra(R, n, names)` and `algebras.Free(R, n, names)` | `Algebras(R).Constructors().free_algebra_from_set(generators=S)` | This is the true free associative unital `R`-algebra on a set of symbols. Sage's `Sets().example().algebra(R)` is not this construction. |
| Plain-set Sage `S.algebra(R)` and `Sets().Algebras(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`, exposed by `S.free_module(R)` | Sage already constructs the free `R`-module with basis indexed by `S` on this path. The spec routes that Sage source surface to `Modules(R)` and rejects it as evidence for an `Algebras(R)` constructor. |
| `S.algebra(R)` where the selected source category is `Magmas()` | `Algebras(R).Constructors().free_algebra_from_magma(magma=S)` | This names the free functor from magmas to the corresponding category of `R`-algebra objects with bilinear multiplication. |
| `S.algebra(R)` where the selected source category is `Semigroups()` | `Algebras(R).Constructors().free_algebra_from_semigroup(semigroup=S)` | This names the free functor from semigroups to the corresponding associative `R`-algebra objects. |
| `S.algebra(R)` for a Sage monoid `S` | `Algebras(R).Constructors().free_algebra_from_monoid(monoid=S)` | This is the monoid algebra `R[S]`, the free construction relative to the multiplicative-monoid forgetful functor. |
| `G.algebra(R)` for a Sage group `G`; `GroupAlgebra(G, R)` | `Algebras(R).Constructors().free_algebra_from_group(group=G)` | The essential image of the group free functor lands in Hopf algebras over `R`; as an `R`-algebra it is the group algebra `R[G]`. |
| `S.algebra(R, category=...)` for additively written structures | Named free-construction methods for the selected operation, not a generic `category=` argument | Sage's `category` parameter selects whether an operation written additively or multiplicatively supplies the product. The project API must route through the specific category method `S.free_algebra(R)` instead of exposing Sage's ambiguous keyword. |
| `FiniteDimensionalAlgebra(k, table, assume_associative=True, assume_unital=True)` | `Algebras(k).Constructors().from_associative_unital_right_multiplication_table(right_multiplication_matrices=table, basis_names=names)` | Sage's table entries are matrices for right multiplication by basis elements. The project constructor admits only the associative unital case because `Algebras(k)` means associative unital algebras. |
| `FiniteDimensionalAlgebra(k, table)` without both associative and unital assumptions | Mathematically justified non-mapping to `Algebras(k)`; map to magmatic or associative nonunital algebra surfaces when those subtrees exist. | Sage says the default object is a magmatic algebra, not necessarily associative or unital. |
| `AlgebrasWithBasis(R)` | `Algebras(R).WithBasis()` | `WithBasis` is shared module/vector-space vocabulary; the algebra surface adds multiplication-on-basis methods. Bases are families of algebra elements, while `one_basis()` and `product_on_basis()` use basis indices. |
| `CombinatorialFreeModule(R, basis_keys, category=AlgebrasWithBasis(R))` | Future constructor surface for algebras with basis once the multiplication-on-basis data type is fixed. | Sage uses this as infrastructure for algebras with basis, but the constructor alone supplies only the module with basis. A project constructor must also specify `one_basis` and `product_on_basis` using mathematical types. |
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

## Free-Construction Routing

The public method on a source object is `S.free_algebra(R)`. The source category, not a
runtime `category=` keyword, chooses the constructor. The `Sets()` row below is the
project free-algebra method, backed by Sage `FreeAlgebra`; it is not Sage's plain-set
`S.algebra(R)` path.

| Source category for `S` | Public source method | Constructor target |
| --- | --- | --- |
| `Sets()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_set(S)` |
| `Magmas()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_magma(S)` |
| `Semigroups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_semigroup(S)` |
| `Monoids()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_monoid(S)` |
| `Groups()` | `S.free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_group(S)` |

`Groups()` are not an unrelated constructor family: the group construction refines the
monoid construction, and its essential image lies in Hopf algebras over `R`.

For source categories whose operation is written additively, the same pattern applies:
the selected operation must be represented by the source category method, and the target
constructor name must say which source category is being used. Do not expose Sage's
generic `category=` disambiguation as project API.

## Plain-Set Sage Algebra Route

Sage's plain-set `S.algebra(R)` path is a module construction in the project spec:

| Sage source path | Project source spelling | Target constructor |
| --- | --- | --- |
| `S.algebra(R)` for `S in Sets()` with no selected multiplicative/additive structure | `S.free_module(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)` |

This routing preserves the old Sage functionality without admitting the Sage name as
algebra vocabulary. The true free associative algebra on a set of generators uses
`S.free_algebra(R)` and routes to `free_algebra_from_set`.
