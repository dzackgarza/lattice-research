# Algebras Sage Inventory

This inventory records Sage algebra surfaces that the local `Algebras(R)` spec must
represent.

## Category Surfaces

| Sage surface | Target vocabulary to inventory |
| --- | --- |
| `sage.categories.algebras.Algebras` | Root algebra parent, element, morphism, homset, and constructor surfaces. |
| `sage.categories.algebras_with_basis.AlgebrasWithBasis` | Basis-dependent algebra operations, structure constants, and module-with-basis inheritance. |
| `sage.categories.commutative_algebras.CommutativeAlgebras` | Commutative algebra restriction. |
| `sage.categories.finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis` | Finite-dimensional basis-dependent radical, center, idempotent-lift, Peirce, and semisimple-quotient methods. |
| `sage.categories.semisimple_algebras.SemisimpleAlgebras` | Semisimple algebra restriction and semisimple quotient targets. |
| Matrix algebras and square matrix spaces | Algebra objects inheriting ring and module surfaces without redeclaring them in `rings`. |
| Polynomial, quotient, and finite-dimensional algebras | Algebra constructors and subcategories once their Sage surfaces are inventoried. |
| Sage algebra construction categories | Subobjects, quotients, Cartesian products, tensor products, and dual objects under `subcategories/constructions/`. |

## Method Surface From Current Spec

- `base_ring`
- `change_ring`
- `center`
- `center_basis`
- `radical`
- `radical_basis`
- `subalgebra`
- `derivations_basis`
- `hochschild_complex`
- `has_standard_involution`
- `idempotent_lift`
- `peirce_decomposition`
- `semisimple_quotient`

## Local Vocabulary Decisions

- `basis()` returns an `AlgebraBasis`, a Sage family of algebra elements.
- `one_basis()` and `product_on_basis()` use `AlgebraBasisIndex`, since Sage basis
  multiplication is indexed by the basis keys.
- `algebra_generators()` returns an `AlgebraElementFamily`, not a generic set family.
- `WithBasis`, `FiniteDimensional`, `Commutative`, and `Semisimple` use the shared
  axiom names registered in `axioms.py`; this subtree contributes only the
  algebra-specific method surfaces for those restrictions.
