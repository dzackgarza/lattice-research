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

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/rings/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/rings.py`
  - `sage/categories/rngs.py`
  - `sage/categories/semirings.py`
  - `sage/categories/domains.py`
  - `sage/categories/commutative_rings.py`
  - `sage/categories/fields.py`
  - `sage/categories/integral_domains.py`
  - `sage/categories/principal_ideal_domains.py`
  - `sage/categories/euclidean_domains.py`
  - `sage/categories/finite_fields.py`
  - `sage/categories/quotient_fields.py`
  - `sage/rings/ideal.py`
  - `sage/rings/polynomial/polynomial_ring_constructor.py`
  - `sage/rings/number_field/number_field.py`
  - `sage/rings/power_series_ring.py`
  - `sage/rings/laurent_series_ring.py`
  - `sage/rings/puiseux_series_ring.py`
  - `sage/rings/padics/factory.py`
  - `sage/rings/finite_rings/finite_field_constructor.py`
  - `sage/rings/finite_rings/integer_mod_ring.py`
  - `sage/matrix/matrix_space.py`
- Source access method: installed source and docstrings were read directly; method
  listings were cross-checked from the Python AST of the installed category files.
- Completeness status: this pass reconciles the source corpus above into the mapping
  rows below. Remaining gaps are explicit negative findings or decision/frontier rows
  in this spec; no separate file is edited by this task.

## Sage Source Reconciliation

This reconciliation is normative for the Rings mapping until the implementation specs
split these rows into concrete category files.

| Source surface | Highest mathematical owner | Mapping decision |
| --- | --- | --- |
| `Semirings` category axiom surface | strict supercategory of `Rings()` | Ring specs inherit semiring addition/multiplication/distributivity data; no ring method is duplicated here. |
| `Rngs.ParentMethods.ideal_monoid`, `principal_ideal`, `zero_ideal` | `Rngs()` / nonunital ring-side ideal vocabulary | Ideal construction starts before unital rings. `Rings()` must preserve these obligations and may refine unit-ideal and quotient behavior, but must not move zero/principal ideals downward to commutative rings only. |
| `Rngs.ParentMethods._ideal_class_` and commutative/PID overrides | private Sage ideal-class interop | Not public project API. It witnesses that ideals must stay constructible for noncommutative, commutative, and PID rings through the public ideal constructors. |
| `Domains` and `IntegralDomains` containment/predicate methods | `Rings().NoZeroDivisors()` and `Rings().Commutative().NoZeroDivisors()` | `Domains` is the noncommutative no-zero-divisor owner; `IntegralDomains` is the commutative specialization. Field and finite-domain shortcuts are implementation evidence, not owner changes. |
| `Rings.MorphismMethods.is_injective` | `Rings().HomCategory().MorphismMethods` | Ring-homomorphism injectivity belongs on ring morphisms. Field-domain, characteristic, kernel, cardinality, and fraction-field cases are implementation criteria for that morphism predicate. |
| `Rings.MorphismMethods.extend_to_fraction_field` | ring morphisms between integral domains, with field codomains by identity | The source morphism must be injective when extension is nontrivial. Codomain is a morphism between fraction fields. |
| `Rings.MorphismMethods._is_nonzero` | private ring-hom compatibility helper | Keep as interop evidence only. Public zero/nonzero morphism predicates belong to generic Hom/End surfaces and ring morphism refinements. |
| `Rings.ParentMethods.is_ring`, `is_commutative`, `is_integral_domain`, `is_field`, `is_zero` | ring object predicates, refined by subcategory overrides | These are predicates on ring objects. Lower categories may return trivial values, but the method owner remains the highest category where the question is meaningful. |
| `Rings.ParentMethods.is_subring` | ring-object relation / subobject vocabulary | The mathematical content is injectivity of the canonical map from one ring into another. Public mapping should phrase this through subring/subobject and structure-morphism surfaces. |
| `Rings.ParentMethods.zeta`, `zeta_order` and `FiniteFields.ParentMethods.zeta`, `zeta_order` | finite-field roots-of-unity surface, with a broader roots-of-unity decision needed for arbitrary rings | Finite fields own the constructive root-of-unity implementation. The generic Sage ring-level methods are too broad to admit without a `RootsOfUnity` or torsion-unit owner. |
| `Rings.ParentMethods.localization` and `IntegralDomains.ParentMethods.localization` | commutative-ring localization at a multiplicative set, with Sage's integral-domain implementation as evidence | Localization is not domain-only mathematics: for a commutative ring `R` and multiplicative set `S`, the public target is `S^{-1}R` with the universal map `R -> S^{-1}R`. Sage's checked generic method rejects non-domains and its implemented constructor lives on `IntegralDomains`, so non-domain commutative localization is an implementation gap rather than a reason to weaken the spec. Noncommutative/Ore localization remains a separate owner decision. |
| `Rings.ParentMethods.bracket` / `__getitem__` | constructor dispatcher, not a public variadic method | Split into explicit constructor routes: polynomial rings, power series rings, Ore polynomial rings, algebraic extensions/number fields, and number-field orders. The raw `R[...]` dispatcher remains Sage interop. |
| `Rings.ParentMethods._Hom_` | `Rings().HomCategory().Of(domain, codomain)` | Sage homset construction evidence maps to explicit ring hom category construction, not a root method on `Rings()`. |
| `Rings.ParentMethods._mul_`, `__pow__`, `__truediv__` | categorical construction glue | Products, free powers, and quotients must route through product/module/quotient constructors with typed inputs; raw Python operator overloads are interop syntax. |
| `Rings.ParentMethods.nilradical`, `unit_ideal`, `ideal`, `quotient`, `quo`, `quotient_ring` | ring ideal and quotient-ring surface | Preserve the full ideal interface: ideal generators, side for noncommutative ideals, coercion, quotient names, quotient map/retract data, and quotient-ring refinement. `quo` is an alias; `quotient` and `quotient_ring` map to the same quotient-ring constructor family. |
| `Rings.ParentMethods.characteristic` | ring invariant | Characteristic is a ring-object invariant returning a Sage integer. Tests for additive order are implementation evidence. |
| `Rings.ParentMethods.free_module` and `Fields.ParentMethods.vector_space` | finite-free-over-base presentation of the caller ring/field | The caller owner remains the ring or field object equipped with a finite-free structure over `base`; the codomain data are `V in Modules(base).Free().FiniteRank()` and mutually inverse `base`-linear maps `V <-> R`. Do not move the method owner to the constructed module category merely because `V` is returned. |
| `Rings.ParentMethods.random_element`, `_random_nonzero_element` | runtime sampling interop | Not a mathematical spec obligation. Keep only as Sage compatibility evidence unless a separate probabilistic/sampling category is admitted. |
| `Rings.ParentMethods.epsilon` | approximate/topological ring precision surface | Exact rings return zero only as implementation fallback. Public ownership is `Rings().Approximate()` or a topology/precision refinement, not all rings. |
| `Rings.ElementMethods.is_unit`, `inverse_of_unit` | ring element/unit surface | Unit predicate and inverse-of-unit belong on elements of unital rings. Field elements override by nonzero criterion. |
| `Rings.ElementMethods._divide_if_possible` | private divisibility helper | Do not expose under this name. Public divisibility belongs to commutative/PID/Euclidean or quotient-field surfaces according to hypotheses. |
| `CommutativeRings.ParentMethods.krull_dimension` | commutative ring invariant | Krull dimension first becomes meaningful for commutative rings. Field and PID values are subcategory overrides. |
| `CommutativeRings.ParentMethods.over` | rings-over / ring-extension construction | Maps to `Rings().RingsOver(base)` and structure-morphism vocabulary. `gen/gens/name/names` are constructor data for the extension object, not separate categories. |
| `CommutativeRings.ParentMethods.frobenius_endomorphism` | positive-characteristic commutative ring endomorphism | Caller is a commutative ring; input is a nonnegative Sage integer power; codomain is an endomorphism of the same ring. |
| `CommutativeRings.ParentMethods.derivation_module`, `derivation` | derivation module over a commutative ring | The returned object is a module of derivations into a codomain algebra or along a twisting morphism. Ring mapping must point to module/hom ownership rather than a raw callable helper. |
| `CommutativeRings.ParentMethods._pseudo_fraction_field` | private coercion interop | Not public project API. It is evidence that fraction-field and division-parent behavior must be mapped explicitly. |
| `CommutativeRings.Finite.ParentMethods.cyclotomic_cosets` | finite commutative rings | Caller is a finite commutative ring; input is an invertible element and optional selected elements; return is a finite ordered list of finite orbits. |
| `Fields.ParentMethods.algebraic_closure`, `an_embedding`, `prime_subfield`, `is_perfect` | fields | These are field-level constructions or predicates. `an_embedding(K)` returns a ring morphism into a field of the same characteristic when one exists. |
| `Fields.ParentMethods.divides`, `ideal`, `fraction_field`, `integral_closure` | fields as trivial integral domains/PIDs | Field overrides preserve inherited divisibility, ideal, fraction-field, and integral-closure obligations with trivial codomains. They are not grounds for deleting the inherited surfaces. |
| `Fields.ParentMethods._gcd_univariate_polynomial`, `_xgcd_univariate_polynomial`, `_squarefree_decomposition_univariate_polynomial` | private polynomial-algorithm hooks over fields | Public obligations belong to polynomial rings over fields and factorization/squarefree surfaces; the private hooks are implementation evidence. |
| `Fields.ElementMethods.euclidean_degree`, `quo_rem`, `gcd`, `lcm`, `xgcd`, `factor`, `inverse_of_unit` | field elements as Euclidean/PID/UFD elements | Field element arithmetic refines inherited Euclidean and factorization surfaces. GCD/LCM are unit-normalized and need field-specific codomain notes. |
| `PrincipalIdealDomains.ParentMethods.gcd`, `content`, `class_group` | PIDs | `gcd` and `content` are PID methods with ring-element inputs. `class_group()` is the trivial class group for PIDs and must not be generalized to arbitrary integral domains without a separate owner. |
| `EuclideanDomains.ParentMethods.gcd_free_basis` and `ElementMethods.euclidean_degree`, `quo_rem`, `gcd` | Euclidean domains | Quotient-with-remainder and Euclidean degree are the defining constructive data. `gcd` may be implemented by Euclidean algorithm here, with PID/UFD consequences inherited upward. |
| `FiniteFields.ParentMethods.is_perfect`, `zeta`, `zeta_order` | finite fields | Finite fields are perfect and have constructive multiplicative roots of unity. `_element_of_factored_order` is private algorithm evidence for `zeta(n)`. |
| `QuotientFields.ElementMethods.numerator`, `denominator`, `gcd`, `lcm`, `xgcd`, `factor`, `partial_fraction_decomposition`, `derivative`, `_derivative` | quotient-field elements, with rational-function refinements where polynomial hypotheses are required | Numerator and denominator are abstract quotient-field element data. Partial fractions and derivatives require denominator factorization or polynomial/rational-function structure and should be guarded by those hypotheses in the final spec. |
| `PolynomialRing` constructor | `Rings().Constructors().PolynomialRing(...)` split into explicit overloads | The installed source confirms the finite documented cases: one name, names, count plus names, and finite `var_array` shapes. Higher-dimensional `var_array` remains excluded until finite-indexing vocabulary exists. |
| `NumberField` constructor | `Rings().Constructors().NumberField(...)` and `NumberFieldTower(...)` | The installed source confirms a single-polynomial route and a list/tuple polynomial tower route; `implementation` and `prec` are compatibility keywords ignored unless nontrivial values are supplied. |
| `PowerSeriesRing`, `LaurentSeriesRing`, `PuiseuxSeriesRing` constructors | named power/Laurent/Puiseux series constructors | Univariate, multivariate, and underlying-ring routes remain split. Laurent and Puiseux constructors can accept already-built underlying series rings; those are named constructor paths, not arbitrary variadic admission. |
| `MatrixSpace` / square matrix parent | ring constructor plus algebra/module refinement | Square matrix spaces are algebras and rings; rectangular matrix spaces are module homspaces. Matrix element construction remains split into named element constructors. |
| `Zp`, `Qp`, `Zq`, `Qq` | p-adic and q-adic ring/field constructors | Scalar precision, lattice precision pairs, relaxed precision triples, print controls, and unramified-extension data stay named. Print controls are display interop; precision and valuation data are mathematical. |
| `FiniteField` / `GF` and `IntegerModRing` | finite field and integer-modulo constructors | `GF` admits prime-power order, name/prefix, modulus, implementation, proof/check data, and display representation. `IntegerModRing` is a quotient-ring constructor for `ZZ/nZZ`, with field refinement only when the modulus is prime. |

## Interop, Display, Runtime, And Private Helper Classification

| Class | Sage surfaces | Mapping consequence |
| --- | --- | --- |
| Private test helpers | `_test_*`, `_contains_helper`, `_call_`, factory `create_key*`, factory `create_object` | Do not admit as public methods. They provide source evidence for invariants and constructor casework. |
| Private implementation hooks | `_ideal_class_`, `_pseudo_fraction_field`, `_element_of_factored_order`, `_gcd_univariate_polynomial`, `_xgcd_univariate_polynomial`, `_squarefree_decomposition_univariate_polynomial`, `_derivative` | Keep private. Public mapping must name the mathematical surface they support: ideals, fraction fields, roots of unity, polynomial gcd/squarefree, or derivations. |
| Display interop | p-adic `print_mode`, `print_pos`, `print_sep`, `print_alphabet`, `print_max_*`, `show_prec`, Sage `_repr_`, `_latex_`, `_magma_init_`, `_polymake_init_` | Not mathematical category data except where display choices affect Sage identity/equality. Public constructors may accept named display options only as interop/display options; category methods do not own them. |
| Runtime/sampling | `random_element`, `_random_nonzero_element`, proof/check flags, implementation selectors, element caches | Not ideal-interface obligations. Keep as constructor or runtime interop parameters when preserving Sage behavior requires them. |
| Syntax dispatchers | `R.__getitem__`, operator overloads, `quo` alias, `MatrixSpace.matrix(x=None, **kwds)` | Do not expose as catch-all methods. Split into named constructors and overloads with typed mathematical input data. |

## Formal Negative Findings

- Searched: `category_specs/rings/docs/SAGE_INVENTORY.md`; installed Sage
  `sage/categories/rings.py`, `rngs.py`, `semirings.py`, `domains.py`,
  `commutative_rings.py`, `fields.py`, `integral_domains.py`,
  `principal_ideal_domains.py`, `euclidean_domains.py`, `finite_fields.py`, and
  `quotient_fields.py`; AST method listing for those files.
- Found: the local inventory names category files and constructor families, but it does
  not enumerate the method-level Sage surfaces listed in the reconciliation table
  above.
- Conclusion: inference -- the local inventory is a source-area inventory, not a
  complete method inventory; this spec now carries the method-level reconciliation for
  Rings until the inventory is expanded.
- Confidence: High.
- Gaps: Cython-only methods on concrete ring element classes and external optional
  backend methods were not exhaustively enumerated in this pass.

- Searched: installed Sage `sage/categories/rings.py`, `sage/categories/rngs.py`,
  `sage/categories/semirings.py`, `sage/categories/domains.py`, and generic Hom/End
  category surfaces referenced by the Rings inventory.
- Found: Sage exposes ring homsets and endsets through generic category/Homset
  machinery and concrete ring morphism classes; no separate installed
  `Rings().Autsets()` category class or ring-specific `Autsets` method surface was
  found in those sources.
- Conclusion: inference -- project `Rings().AutCategory()` must be local top-level
  Hom/End/Aut wiring with ring specialization, not a direct wrapper of a Sage
  ring-autset category.
- Confidence: High.
- Gaps: concrete ring-family automorphism methods outside the checked category files
  were not exhaustively listed; those remain family-specific method evidence.

- Searched: installed Sage `sage/categories/semirings.py` and
  `sage/categories/domains.py`.
- Found: `Semirings` contributes the category axiom declaration and examples but no
  nested `ParentMethods`, `ElementMethods`, or `MorphismMethods`; `Domains` contributes
  only the no-zero-divisor category edge and `_test_zero_divisors`.
- Conclusion: inference -- there are no additional semiring- or domain-local public
  method surfaces to map into the Rings spec from those two category files beyond the
  inherited category structure and the domain predicate/test evidence.
- Confidence: High.
- Gaps: semiring implementations outside `sage/categories/semirings.py` were not part
  of the Rings inventory and were not exhaustively searched.

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
  `Qp(..., type="lattice-cap").extension(...)` routes. Upstream follow-up searched
  Sage 10.8 p-adics docs for `factory`, `generic_nodes`, and `padic_base_leaves`;
  Sage `develop` raw source for `factory.py`, `padic_extension_leaves.py`,
  `padic_base_leaves.py`, and `generic_nodes.py`; GitHub issue/PR searches for
  `Zq Qq lattice-cap`, `pAdicLatticeGeneric unramified extension`, `lattice precision
  q-adic`, `pAdicRingLattice pAdicFieldLattice extension`, and `PrecisionLattice`;
  issues `#23505`, `#24809`, `#25915`, `#28466`, `#30692`, and pull request `#34993`;
  the stale `sagetrac-mirror` branch for `#25915`; and PR `#34993` branch
  `roed314/sage:general-extensions`.
- Found: Sage `Zp`/`Qp` base constructors canonicalize lattice precision pairs through
  `get_key_base`, and `pAdicLatticeGeneric` stores separate relative and absolute
  caps. Installed Sage `Zq`/`Qq` extension constructors document q-adic `prec` as an
  integer cap and coerce non-`Integer` precision with `prec = Integer(prec)` before
  calling `ExtensionFactory`. Direct q-adic pair precision fails with `TypeError:
  unable to coerce <class 'tuple'> to an integer`. Scalar lattice-cap q-adic routes
  and explicit lattice-base extension routes fail before returning a usable extension
  parent. The installed and `develop` `ext_table` entries have unramified extension
  leaves for capped-relative, capped-absolute, fixed-modulus, and floating-point bases,
  but no lattice extension leaf keyed by `pAdicRingLattice` or `pAdicFieldLattice`.
  Issue `#23505` is the merged base p-adic lattice-precision ticket; open issues
  `#24809` and `#30692` show remaining lattice-precision performance/API gaps. Open
  issue `#25915` targets unramified extensions of arbitrary p-adic fields, and open
  issue `#28466` / draft PR `#34993` target general p-adic extensions, but the searched
  branches still do not add lattice extension leaves or a q-adic split-cap constructor.
- Conclusion: inference -- no real installed or searched upstream Sage construction
  path currently realizes unramified q-adic extensions with split lattice
  relative/absolute precision caps. These names remain deferred frontiers until Sage
  exposes an extension-specific lattice-precision route or an upstream fix.
- Confidence: High.
- Gaps: GitHub issue comments could not be loaded through `gh issue view --comments`
  because GitHub's classic-project GraphQL field failed, so the upstream audit used
  issue bodies, search results, labels, source branches, and PR metadata. Private
  branches and developer discussions outside public Sage GitHub/Sage docs were not
  searched.

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
