---
id: SPEC-MAPPING-RINGS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track rings mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/rings/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  ring, ideal, quotient, localization, topological, and constructor signatures.
acceptanceCriteria:
- Source paths category_specs/rings/docs/MAPPING.md and category_specs/rings/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 85
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Rings Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/rings/docs/MAPPING.md`.

Source inventory: `category_specs/rings/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Converted Mapping Content

This file records the forward target mapping from Sage ring surfaces into the local
category-spec hierarchy. It is not a history of deleted files.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Rings().NamedRings()` | `Rings().Constructors()` | Constructors are entry points into Sage objects, not mathematical subcategories. The target surface is an inner `Constructors` class on `Rings`. |
| Root shortcuts such as `Rings().ZZ()` | `Rings().Constructors().ZZ()` | Constructor shortcuts do not belong on the category root. The category root documents mathematics; `Constructors()` owns Sage entry points. |
| `RationalField()` / `QQ` | `Rings().Constructors().QQ()` | The rational field is a fixed object constructor with no Sage option bag on the public project surface. Rational elements are constructed by the returned field object, not by extra rational-field constructor options. |
| Parameterized families such as `RealField(prec)` and `Zp(p)` | Constructor methods returning objects refined into precision, valuation, or local-field subcategories | The parameterized family is not a one-object category; fixed objects such as `RR` and `CC` may have singleton refinements. |

Constructor signatures must follow Sage's documented input shapes. `PowerSeriesRing`,
`LaurentSeriesRing`, `PuiseuxSeriesRing`, and `MatrixRing` expose their structured
parameters directly. `PolynomialRing` exposes Sage's finite variable-specification
casework as overloads: `name`, `n` with `name`, `names`, `n` with `names`, single-count
`var_array`, and the names-external `n` form. Sage's higher-dimensional `var_array`
shape accepts an unbounded positional dimension list such as
`PolynomialRing(ZZ, 2, 3, 4, var_array='m')`; this pass does not admit that shape
because the public spec has no mathematical finite-indexing vocabulary for it yet. The
implementation may delegate to Sage's variadic factory, but the spec surface is closed
to the documented parameters: `base_ring`, `n`, `name`, `names`, `var_array`, `sparse`,
`order`, and `implementation`.

The remaining variadic ring factories are split as follows:

| Sage surface | Project surface | Decision |
| --- | --- | --- |
| `NumberField(polynomial, name=None, check=True, names=None, embedding=None, latex_name=None, assume_disc_small=False, maximize_at_primes=None, structure=None, *, latex_names=None)` | `NumberField(polynomial, name=None, check=True, names=None, embedding=None, latex_name=None, assume_disc_small=False, maximize_at_primes=None, structure=None, *, latex_names=None)` | Single defining-polynomial route. Each admitted Sage option is named explicitly; sequence-valued tower metadata is not accepted here. |
| `NumberField(polynomials, names, check=True, embeddings=None, latex_names=None, assume_disc_small=False, maximize_at_primes=None, structures=None)` | `NumberFieldTower(polynomials, names, check=True, embeddings=None, latex_names=None, assume_disc_small=False, maximize_at_primes=None, structures=None)` | Tower construction is a separate mathematical case with sequence metadata attached to the tower. |
| `Zp(p, prec=n, type=...)` / `Qp(p, prec=n, type=...)` | `Zp(p, prec=n, type=...)` / `Qp(p, prec=n, type=...)` | Scalar precision cap route. |
| `Zp(p, prec=(relative_cap, absolute_cap), type='lattice-*')` and `Qp` analogue | `ZpWithPrecisionCaps(...)` / `QpWithPrecisionCaps(...)` | Pair precision data is meaningful only for lattice precision, so it is named explicitly. |
| `Zp(p, prec=(default_prec, halting_prec, secure), type='relaxed')` and `Qp` analogue | `ZpRelaxed(...)` / `QpRelaxed(...)` | Relaxed arithmetic has default, halting, and security data; it is not a generic precision tuple. |
| `Zq(q, ...)` / `Qq(q, ...)` with integer prime power | `Zq(q, ...)` / `Qq(q, ...)` | Cardinality route. |
| `Zq((p, n), ...)` / `Qq((p, n), ...)` | `ZqFromPrimePower(p, degree=n, ...)` / `QqFromPrimePower(...)` | Prime-power pair route. |
| `Zq([(p, n)], ...)` / `Qq([(p, n)], ...)` | `ZqFromPrimePowerFactorization(factorization=...)` / `QqFromPrimePowerFactorization(...)` | Factorization route. |
| `Zq(..., prec=(relative_cap, absolute_cap), type='lattice-*')` and `Qq` analogue | Deferred admitted names `ZqWithPrecisionCaps(...)` / `QqWithPrecisionCaps(...)` | The split is mathematically meaningful, but installed Sage does not expose a working unramified extension parent for lattice precision caps. |
| `PowerSeriesRing(R, name, default_prec=...)` | `PowerSeriesRing(base_ring=R, name=..., default_prec=...)` | Univariate power-series route. Sage's deprecated positional precision route maps to the named `default_prec`. |
| `PowerSeriesRing(R, names=...)` or comma-separated/list names | `MultivariatePowerSeriesRing(base_ring=R, names=..., num_gens=...)` | Multivariate named-generator route. |
| `PowerSeriesRing(R, n, prefix, ...)` | `MultivariatePowerSeriesRingWithGeneratorPrefix(base_ring=R, prefix=..., num_gens=n, ...)` | Prefix-plus-count route. |
| `LaurentSeriesRing(PowerSeriesRing(...))` | `LaurentSeriesRingFromPowerSeriesRing(power_series_ring)` | Underlying power-series-ring route. |
| `PuiseuxSeriesRing(LaurentSeriesRing(...))` | `PuiseuxSeriesRingFromLaurentSeriesRing(laurent_series_ring)` | Underlying Laurent-series-ring route. |
| `MatrixRing(R, n, sparse=False, implementation=None)` | `Rings().Constructors().MatrixRing(base_ring=R, n=n, sparse=False, implementation=None)` | The constructor entry point stays in `rings` because it builds the ambient square-matrix parent itself. Refinement into algebra and module categories happens on the returned parent rather than by relocating the constructor. |
| `MatrixSpace.matrix(x=None, **kwds)` | `zero_matrix()`, `matrix_from_matrix(matrix, *, coerce=True)`, `matrix_from_entries(entries, *, coerce=True)`, `matrix_from_rows(rows, *, coerce=True)`, `scalar_matrix(scalar, *, coerce=True)` | The no-argument, matrix, flat-entry, row-entry, and scalar cases are separate element constructors. Sage's option bag is not public; the only admitted keyword on data-bearing routes is the named `coerce` flag. |

Number-field methods with optional `v` are also split. `discriminant()` is the field
discriminant, while `trace_pairing_discriminant(elements)` is the determinant of the
trace pairing on supplied elements. `integral_basis()`, `ring_of_integers()`, and
`maximal_order()` are the full-order routes; the `v=p` and `v=[p_i]` Sage paths are
named `*_at_prime` and `*_at_primes`.

## Signature Typing Decisions

Ring dimensions, generator indices, generator counts, precisions, p-adic print bounds,
orders, degrees, and multiplicities are Sage integer quantities. The spec uses
`Integer` from `types.py` instead of accepting both native Python `int` and
`Integer`. Constructor bodies may still pass these values to Sage's factories, but the
category-spec surface is mathematically typed.

Matrix-ring diagonal construction takes a sequence of ring elements. The previous
`Any` surface hid the mathematical input: diagonal entries form an ordered finite
family in the base ring.

Boolean-controlled return-shape methods use literal overloads when Sage documents a
closed finite split. For `galois_closure(map=False)` the return object is the Galois
closure field; for `galois_closure(map=True)` it is the pair consisting of that field
and the embedding of the source field into it. For algebraic `nth_root(all=False)` and
`sqrt(all=False)` the return object is one root; with `all=True` Sage returns the
finite list of all roots. Non-literal boolean callers keep the union return shape.

Precision-family identities are exact Sage identity facts, not informal equality:
`RR is RealField(53)`, `CC is ComplexField(53)`,
`RIF is RealIntervalField(53)`, and `CIF is ComplexIntervalField(53)` are true.
`RDF is RealField(53)`, `CDF is ComplexField(53)`, `RR is RDF`, and `CC is CDF`
are false. Thus `RR`, `CC`, `RIF`, and `CIF` may have fixed-object refinements,
while `RealField(...)`, `ComplexField(...)`, and related precision families remain
multi-object parameterized subcategories.

Sage p-adic `change(...)` calls split into mathematical operations. Precision changes
map to `change_precision(precision, precision_type=None)` on `Rings().Approximate()`.
Changing `type='capped-abs'` supplies the optional `precision_type`. Changing
`p=17` maps to `change_prime(17)` on p-adic rings and fields. Switching
`field=True` maps to `fraction_field()`. Print-mode changes are display interop and
use the private convenience method `_change_print_mode(print_mode)`.

## Subcategory Layout

| Current source surface | Target file organization | Rationale |
| --- | --- | --- |
| Ring family category surface | `subcategories/<mathematical_name>.py` or nested directories | Files should correspond to mathematical subcategories: `field.py`, `finite.py`, `integral_domain.py`, `valuation/`, `number_fields/`, and so on. |
| Approximate ring surface | `subcategories/approximate.py` | Precision control is common to real/complex precision families and p-adic rings/fields. The shared mathematical method is `change_precision`, not Sage's raw `change(...)` option bag. |
| Construction-category surface | `subcategories/constructions/<notion>.py` | Constructions such as subobjects, quotients, rings under, rings over, characteristic, and Krull dimension are attachable categorical constructions and are split by notion. |
| Matrix ring/algebra surface | `algebras` plus ring refinement | Matrix rings are algebras over their base ring and modules over that base. Algebraic methods belong in `algebras`; ring methods belong in `rings`; module methods belong in `modules`. |

## Square Matrix Parent Split

The square matrix parent split is fixed by the current mapping docs plus Sage's public
behavior:

- Sage documents `MatrixSpace(R, n, n)` as the parent of `n x n` matrices over `R`,
  places square matrix spaces in an algebra-with-basis category, and still treats the
  same parent as a ring object (`is_Ring(MatrixSpace(QQ, 2))` is true).
- The same Sage inventory pass records rectangular `MatrixSpace(R, m, n)` in module
  territory and square `MatrixSpace(R, n, n)` in algebra territory, so the split is
  by public structure, not by constructor namespace.

The project owner rule is therefore:

| Surface on a square matrix parent over `R` | Owner | Codomain consequence |
| --- | --- | --- |
| Constructor entry point | `Rings().Constructors().MatrixRing(base_ring, n, sparse=False, implementation=None)` | Returns the ambient square matrix parent itself. |
| Ring operations: multiplication, unit, ideals, quotient-ring structure, ring predicates | `rings` | The codomain stays the same square matrix parent viewed in `Rings()`. |
| Algebra operations over the base ring `R`: algebra generators, center, radical, algebra ideals, finite-dimensional algebra structure | `algebras` | The codomain stays the same parent viewed in `Algebras(R)` or a matrix-algebra refinement below it. |
| Free finite-rank module operations over `R`: rank, basis, coordinate conversion, submodule/quotient/module hom structure | `modules` | The codomain stays the same parent viewed in `Modules(R).Free().FiniteRank()`. |

Migration consequence: keep `MatrixRing` and square `MatrixSpace` constructor routing in
`rings`, move only algebra-specific method surfaces to `algebras`, and keep free-module
structure in `modules`. Do not weaken the matrix smoke by replacing simultaneous
refinement checks with a single-owner shortcut.

## Construction-Category Mapping

| Sage surface | Target surface | Rationale |
| --- | --- | --- |
| `Rings().Homsets()` | `Rings().HomCategory()` in `rings/homsets.py` and top-level `homsets/` | Ring morphisms are structure-preserving maps. The ring-specific file declares ring-homomorphism vocabulary; the top-level hom category hierarchy owns generic hom/end/aut behavior. |
| `Rings().Endsets()` | `Rings().EndCategory()` plus generic end-category wiring | Endomorphism objects are `End(R) = Hom(R, R)`. The ring subtree specifies ring endomorphism methods without duplicating generic end-category logic. |
| Sage/project automorphism surfaces | `Rings().AutCategory()` with ring specialization | A ring automorphism object is the bijective part of `End(R)`. The target exposes this explicitly because `Aut` appears in Sage ring objects even when category-level wiring is inherited. |
| `Rings().CartesianProducts()` | `subcategories/constructions/cartesian_products.py` | A product of rings is a ring with componentwise operations. Signatures should use sequence vocabulary for the factors unless Sage source proves a different mathematical input shape. |
| `Rings().Subquotients()` | `subcategories/constructions/subquotients.py` | Quotients and subobjects share the ambient/lift/retract construction. Ring documentation must keep this parent construction visible instead of jumping directly to quotient rings. |
| `Rings().Subobjects()` | `subcategories/constructions/subobjects.py` | Ring subobjects are subrings in ring categories, not arbitrary subsets. Ideals belong to their own ring-side vocabulary when they are not themselves ring objects. |
| `Rings().Quotients()` | `subcategories/constructions/quotients.py` | Quotient rings are rings modulo ideals or congruences and should refine the subquotient surface. |
| `Rings().IsomorphicObjects()` | `subcategories/constructions/isomorphic_objects.py` | Transport of ring structure along an isomorphism is both subobject-like and quotient-like in Sage's construction hierarchy. |
| `Rings().WithRealizations()` / `Rings().Realizations()` | `subcategories/constructions/with_realizations.py` and `realizations.py` using the generic realization method surface | Realization categories are categorical structure for parents with several concrete models, not constructor namespaces. The audited `Rings` category source contributes no additional ring-only realization methods. |

`Rings().RingsOver(R)` and `Rings().RingsUnder(R)` own the ring-specific
`structure_ring()` and ring morphism `structure_map()` methods. Their old local
`structure_domain()` and `structure_codomain()` methods now map to the Cat-owned
universal structure-morphism surface through `structure_morphism().domain()` and
`structure_morphism().codomain()`.

## Deferred Q-Adic Lattice Precision

`ZpWithPrecisionCaps` and `QpWithPrecisionCaps` are concrete because Sage's `Zp` and
`Qp` base constructors canonicalize lattice precision pairs. The corresponding
unramified extension names `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` are retained
as admitted split names, but their bodies assert the installed Sage gap instead of
passing through to a broken constructor path.

- Searched: `rings/docs/MAPPING.md`, `rings/docs/SAGE_INVENTORY.md`,
  `rings/smoketest.sage`, `rings/__init__.py`, Sage
  `sage/rings/padics/factory.py` around `get_key_base`, `Zq`, `Qq`, and
  `pAdicExtension_class`, Sage `sage/rings/padics/padic_extension_leaves.py`,
  Sage `sage/rings/padics/generic_nodes.py`, and Sage
  `sage/rings/padics/local_generic.py`. Runtime probes covered direct Sage
  `Zq(25, prec=4, type="lattice-cap", names="a")`,
  `Zq(25, prec=(4, 8), type="lattice-cap", names="a")`,
  `Qq(25, prec=4, type="lattice-cap", names="a")`,
  `Qq(25, prec=(4, 8), type="lattice-cap", names="a")`, the analogous
  `lattice-float` pair routes, `check=False` factorization routes, and explicit
  `Zp(..., type="lattice-cap").extension(...)` /
  `Qp(..., type="lattice-cap").extension(...)` routes.
- Found: Sage `Zp`/`Qp` base constructors canonicalize lattice precision pairs through
  `get_key_base`, and `pAdicLatticeGeneric` stores separate relative and absolute
  caps. Installed Sage `Zq`/`Qq` extension constructors document q-adic `prec` as an
  integer cap and coerce non-`Integer` precision with `prec = Integer(prec)` before
  calling `ExtensionFactory`. Direct q-adic pair precision fails with `TypeError:
  unable to coerce <class 'tuple'> to an integer`. Scalar lattice-cap q-adic routes
  and explicit lattice-base extension routes fail before returning a usable extension
  parent. The installed `ext_table` has unramified extension leaves for
  capped-relative, capped-absolute, fixed-modulus, and floating-point bases, but no
  lattice extension leaf keyed by `pAdicRingLattice` or `pAdicFieldLattice`.
- Conclusion: inference -- no real installed Sage construction path currently realizes
  unramified q-adic extensions with split lattice relative/absolute precision caps.
  These names remain deferred frontiers until Sage exposes an extension-specific
  lattice-precision route or an upstream fix.
- Confidence: High.
- Gaps: upstream Sage issue trackers, unreleased Sage branches, and Sage developer
  discussion were not searched in this pass; the conclusion is limited to the installed
  Sage source, installed written docs, and direct local runtime probes.

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

Canonical public-surface anchors already exist in the spec tree:

- `category_specs/rings/subcategories/topological.py` fixes the algebraic owner for the
  ring-side category edge as `Rings().Topological()`.
- `category_specs/topological_spaces/__init__.py` fixes the topological owner for
  `is_open`, `is_closed`, `closure`, `interior`, `boundary`, `is_connected`, and
  `is_compact` as `TopologicalSpaces().ParentMethods`.

The recovery rule for topology-bearing rings and fields is therefore inheritance/join,
not constructor duplication:

| Candidate object family | Constructor owner | Topological owner recovered after refinement | Algebraic owner preserved after refinement | Migration consequence |
| --- | --- | --- | --- | --- |
| `RealField(...)`, `ComplexField(...)`, `RR`, `CC` | `Rings().Constructors()` or field refinements below it | `TopologicalSpaces()` and, when source-backed, `TopologicalSpaces().Metric()` and `TopologicalSpaces().Metric().Complete()` | `Rings()` / `Fields()` and the relevant precision-field subcategories | A field constructor still returns a field object; topological predicates arrive through category refinement, not through a topological-space constructor. |
| `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, `ComplexBallField` | `Rings().Constructors()` or field refinements below it | `TopologicalSpaces()` only through the topological ring/field path documented here | Interval/ball field subcategories in `rings` | Interval and ball objects remain algebraic/numerical fields. Their topology-bearing methods are inherited; they are never admitted as pure `TopologicalSpaces().Constructors()` outputs. |
| `Zp(...)`, `Qp(...)`, `Zq(...)`, `Qq(...)` and named split precision routes | `Rings().Constructors()` or field refinements below it | `TopologicalSpaces()` through `Rings().Topological()` / field refinements | p-adic and q-adic ring/field subcategories | Local-field constructors keep valuation and precision ownership in `rings`; topological recovery adds predicates and transforms without changing constructor namespace. |
| Matrix, power-series, Laurent-series, and Puiseux-series ring families when Sage/refinement marks them topological | `Rings().Constructors()` and the relevant ring family route | `TopologicalSpaces()` through the topological ring subcategory | Ring-family and algebra/module owners already recorded in this mapping | Any topological behavior augments the existing ring/algebra/module split; it does not relocate ownership into `topological_spaces`. |

Topological methods imported into a topological ring or field keep the codomain
contracts fixed in `topological_spaces`: `is_open` and `is_closed` return `bool`,
while `closure`, `interior`, and `boundary` return subsets of the same ambient
topological object. Ring-local files should not restate or shadow those signatures.

Rejected routes for this card:

- adding `TopologicalSpaces().Constructors()` entries for rings, fields, interval
  fields, or ball fields;
- copying `is_open`, `is_closed`, `closure`, `interior`, `boundary`, `is_connected`,
  or `is_compact` into a ring-only `ParentMethods` block as second owners;
- changing a ring or field constructor so that it returns a pure topological-space
  object detached from its algebraic category.
