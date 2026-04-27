# Rings Mapping

This file records the forward target mapping from Sage ring surfaces into the local
category-spec hierarchy. It is not a history of deleted files.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Rings().NamedRings()` | `Rings().Constructors()` | Constructors are entry points into Sage objects, not mathematical subcategories. The target surface is an inner `Constructors` class on `Rings`. |
| Root shortcuts such as `Rings().ZZ()` | `Rings().Constructors().ZZ()` | Constructor shortcuts do not belong on the category root. The category root documents mathematics; `Constructors()` owns Sage entry points. |
| Parameterized families such as `RealField(prec)` and `Zp(p)` | Constructor methods returning objects refined into precision, valuation, or local-field subcategories | The parameterized family is not a one-object category; fixed objects such as `RR` and `CC` may have singleton refinements. |

## Subcategory Layout

| Current source surface | Target file organization | Rationale |
| --- | --- | --- |
| Ring family category surface | `subcategories/<mathematical_name>.py` or nested directories | Files should correspond to mathematical subcategories: `field.py`, `finite.py`, `integral_domain.py`, `valuation/`, `number_fields/`, and so on. |
| Construction-category surface | `subcategories/constructions/<notion>.py` | Constructions such as subobjects, quotients, rings under, rings over, characteristic, and Krull dimension are attachable categorical constructions and are split by notion. |
| Matrix ring/algebra surface | `algebras` plus ring refinement | Matrix rings are algebras over their base ring and modules over that base. Algebraic methods belong in `algebras`; ring methods belong in `rings`; module methods belong in `modules`. |

## Construction-Category Mapping

| Sage surface | Target surface | Rationale |
| --- | --- | --- |
| `Rings().Homsets()` | `rings/homsets.py` and top-level `homsets/` | Ring morphisms are structure-preserving maps. The ring-specific file declares ring-homomorphism vocabulary; the top-level homset hierarchy owns generic hom/end/aut set behavior. |
| `Rings().Endsets()` | `rings/homsets.py` plus generic `Endsets` | Endomorphism sets are homsets with equal domain and codomain. The ring subtree should specify ring endomorphism methods without duplicating generic endset category logic. |
| Project `Rings().Autsets()` | generic `Autsets` with ring specialization | A ring automorphism set is the bijective part of `End(R)`. The target should expose this explicitly because `Aut` appears in Sage ring objects even when category-level wiring is inherited. |
| `Rings().CartesianProducts()` | `subcategories/constructions/cartesian_products.py` | A product of rings is a ring with componentwise operations. Signatures should use sequence vocabulary for the factors unless Sage source proves a different mathematical input shape. |
| `Rings().Subquotients()` | `subcategories/constructions/subquotients.py` | Quotients and subobjects share the ambient/lift/retract construction. Ring documentation must keep this parent construction visible instead of jumping directly to quotient rings. |
| `Rings().Subobjects()` | `subcategories/constructions/subobjects.py` | Ring subobjects are subrings in ring categories, not arbitrary subsets. Ideals belong to their own ring-side vocabulary when they are not themselves ring objects. |
| `Rings().Quotients()` | `subcategories/constructions/quotients.py` | Quotient rings are rings modulo ideals or congruences and should refine the subquotient surface. |
| `Rings().IsomorphicObjects()` | `subcategories/constructions/isomorphic_objects.py` | Transport of ring structure along an isomorphism is both subobject-like and quotient-like in Sage's construction hierarchy. |
| `Rings().WithRealizations()` / `Rings().Realizations()` | `subcategories/constructions/with_realizations.py` and `realizations.py` using the generic realization method surface | Realization categories are categorical structure for parents with several concrete models, not constructor namespaces. The audited `Rings` category source contributes no additional ring-only realization methods. |

## Axiom vs. Implementation Decision

Use direct implementation categories only for genuinely computable implementation
targets, such as a concrete finite-field family or a future finitely generated free
module implementation over a PID. Use `with_axiom` restrictions for mathematical
adjectives that must attach to arbitrary ring subcategories, such as `Commutative`,
`Finite`, `Reduced`, or `Topological`.

## Topological Rings

Topological ring structure must inherit from the `topological_spaces` subtree for the
topological-space surface and from `rings` for ring operations. It should not duplicate
topological-space methods inside a ring-only file.
