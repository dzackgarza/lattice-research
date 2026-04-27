# Rings Sage Inventory

This inventory records Sage ring-category and constructor surfaces that the local
`Rings()` spec must represent. It is source-facing: mappings and implementation status
belong in `MAPPING.md` and `TRIAGE.md`.

## Category Surfaces

| Sage surface | Target vocabulary to inventory |
| --- | --- |
| `sage.categories.rings.Rings` | Root ring parent, element, morphism, homset, endset, and autset surfaces. |
| `sage.categories.commutative_rings.CommutativeRings` | Commutative rings, fields, integral domains, quotient fields, local rings, complete rings, and valuation refinements. |
| `sage.categories.fields.Fields` | Fields, finite fields, number fields, local fields, global fields, algebraically closed fields, and real/complex precision families. |
| `sage.categories.principal_ideal_domains.PrincipalIdealDomains` | PID-specific ideal, gcd, factorization, quotient, and module-construction surfaces. |
| `sage.categories.euclidean_domains.EuclideanDomains` | Euclidean-domain methods, quotient/remainder behavior, and gcd/lcm refinements. |

## Functorial and Construction Surfaces

These surfaces are category-level structure, not named ring constructors. They must be
inventoried before adding or validating scaffolding.

| Sage surface | Source anchor | Ring meaning to inventory |
| --- | --- | --- |
| `Rings().Homsets()` | inherited through `Objects.SubcategoryMethods`; ring morphisms constructed by `Rings.ParentMethods._Hom_` and Sage `RingHomset` classes | Sets of ring homomorphisms preserving addition, multiplication, zero, and one. Sage currently often categorizes ring homsets through lower algebraic supercategories rather than a ring-specific `Rings.Homsets` class. |
| `Rings().Endsets()` | inherited through `Objects.SubcategoryMethods` and generic `Homsets().Endset()` | Endomorphism sets of a ring object; project docs should distinguish endomorphism-set category structure from the constructor `End(R)`. |
| Project `Rings().Autsets()` / `Aut(R)` | project target to audit against Sage generic homset and automorphism constructors | Automorphism sets are bijective ring endomorphisms. They should be documented once in the generic homset/autset hierarchy and specialized for rings. |
| `Rings().CartesianProducts()` | inherited from `Sets.SubcategoryMethods.CartesianProducts()` and Sage cartesian-product functorial machinery | Direct products of rings, with componentwise ring operations; signatures should accept a sequence of ring parents, not untyped variadic placeholders unless Sage requires them. |
| `Rings().Subquotients()` | inherited from `Sets.SubcategoryMethods.Subquotients()` | Constructive ring subquotients with ambient ring, lift, and retract. Quotient rings and subrings are special cases. |
| `Rings().Subobjects()` | inherited from `Sets.SubcategoryMethods.Subobjects()` | Subrings, ideals where the category context asks for ring objects, and other embedded ring objects. Must not be collapsed into set-theoretic subset vocabulary. |
| `Rings().Quotients()` | inherited from `Sets.SubcategoryMethods.Quotients()` plus `Rings.ParentMethods.quotient`/`quotient_ring` | Quotient rings by ideals or congruence data, with the quotient map/retract semantics documented through subquotients. |
| `Rings().IsomorphicObjects()` | inherited from Sage `IsomorphicObjectsCategory` | Ring objects transported along ring isomorphisms; simultaneously subobjects and quotients in Sage's construction hierarchy. |
| `Rings().WithRealizations()` / `Rings().Realizations()` | generic realization category machinery | Ring parents with several concrete realizations or bases. The audited `Rings` category source adds no ring-specific realization parent methods beyond the generic construction surface. |

## Constructor Families

| Sage constructor family | Target constructor surface |
| --- | --- |
| `ZZ`, `QQ`, `AA`, `QQbar`, `RR`, `CC`, `RDF`, `CDF`, `RIF`, `CIF` | `Rings().Constructors()` entry points refining fixed singleton or precision-family categories. |
| `IntegerModRing`, `Zmod`, `Integers` | Integer-modulo ring categories, including finite and quotient-ring structure. |
| `GF`, `FiniteField` | Finite-field categories, including cardinality, characteristic, generator, and Conway/polynomial data where Sage exposes it. |
| `NumberField`, `QuadraticField`, `CyclotomicField` | Number-field categories with quadratic and cyclotomic refinements. |
| `PolynomialRing`, `PowerSeriesRing`, `LaurentSeriesRing`, `PuiseuxSeriesRing` | Ring constructors that also interact with algebra and module categories. |
| `MatrixRing`, `MatrixSpace` when square | Algebra/ring constructors that must inherit algebra and module method surfaces rather than redeclare them locally. |
| `Zp`, `Qp`, `Zq`, `Qq` | Valued, complete, discrete-valuation, and local field/ring categories. |

## Method Surface Still Being Audited

- Ring parent methods in `rings/__init__.py`.
- Ring element methods in `rings/__init__.py`.
- Ring morphism, ideal, homset, endset, and autset methods in `rings/__init__.py` and
  `rings/homsets.py`.
- Ring-family category methods split into mathematical files under
  `rings/subcategories/`, such as `field.py`, `number_field.py`, `finite_field.py`,
  `p_adic_ring.py`, and `polynomial_ring.py`.
- Construction-category methods split under `rings/subcategories/constructions/`.
