# Algebras Sage Inventory

This inventory records Sage algebra surfaces that the local `Algebras(R)` spec must
represent.

## Category Surfaces

| Sage surface | Target vocabulary to inventory |
| --- | --- |
| `sage.categories.algebras.Algebras` | Root algebra parent, element, morphism, homset, and constructor surfaces. |
| `sage.categories.algebras_with_basis.AlgebrasWithBasis` | Basis-dependent algebra operations, structure constants, and module-with-basis inheritance. |
| Matrix algebras and square matrix spaces | Algebra objects inheriting ring and module surfaces without redeclaring them in `rings`. |
| Polynomial, quotient, and finite-dimensional algebras | Algebra constructors and subcategories once their Sage surfaces are inventoried. |

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
