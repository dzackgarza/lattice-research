---
id: SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Specify literal method ownership inventory by minimal category
status: in-progress
priority: critical
requirement: Produce source-grounded method ownership spec files that enumerate every
  literal mathematical or software-facing method expected on category-spec objects
  and state the minimal subcategory that introduces each method.
acceptanceCriteria:
- Every admitted method row names the literal surface spelling, minimal owner category,
  mathematical definition or software interop meaning, hypotheses, codomain or return
  object, and source paths.
- Root-set methods, finite-set protocol methods such as `len(X)`, countable/enumerated
  methods, subobject operations, topology/metric methods, algebra/module methods,
  Hom/End/Aut methods, forms/lattice methods, tensor methods, poset methods, and geometry/backend
  methods are all inventoried or explicitly rejected with source provenance.
- External software mappings from Sage, Oscar/Julia, GAP, Singular, Macaulay2, CARAT,
  Indefinite.jl, and related local backend notes are represented as method rows or
  backend-routing rows rather than left in prose.
- Unresolved method-owner conflicts become decision cards with exact sources checked
  and no implementation task is allowed to guess a mathematical owner.
complexity: 95
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify literal method ownership inventory by minimal category

## Summary

Produce one or more trackable spec files that list the literal expected methods on
category-spec objects and record where each method first becomes mathematically valid.
The output is an ownership inventory, not an implementation pass. It exists so later
code and smoke work can ask "which category introduces this method?" without relying on
Sage implementation class names, wrapper inheritance, or generic LLM guesses.

## Required Row Format

Each method row must record:

- literal surface spelling, including Python protocol spelling where relevant;
- object level: category object, parent, element, hom parent, hom element, constructor,
  or backend bridge;
- minimal introducing category or construction owner;
- inherited or refined categories that should receive the method automatically;
- mathematical definition, invariant, or software interop meaning;
- hypotheses required for the method to make sense;
- codomain or return object, including whether it is a scalar, ideal, subobject, set,
  morphism, group, tensor, ring, module, polyhedron, sheaf, or backend payload;
- source paths and source sections reviewed;
- decision status: admitted, rejected, interop-only, deferred, or decision-needed;
- downstream implementation, test, smoke, or audit card if one already exists.

## Seed Method Surfaces

These seed surfaces are not the final inventory. They are the minimum prompts that the
execution tasks must resolve against source files.

- Sets: `__contains__`, `an_element`, `some_elements`, `cardinality`, `is_empty`,
  `is_finite`, `subsets`, `subsets_lattice`, `union`, comparison and subset protocol,
  `free_module`, `free_algebra`, `_sympy_`.
- Countable and enumerated sets: `__iter__`, `rank`, `unrank`, `__getitem__`,
  iterator ranges, `random_element`, `first`, `next`.
- Finite sets and finite enumerated sets: `len(X)` / `__len__`, `list(X)`,
  `tuple(X)`, finite enumeration caches, finite cardinality conversion.
- Set subobjects and image objects: `intersection`, `difference`,
  `symmetric_difference`, `complement`, `ambient`, `lift`, `retract`.
- Topological and metric surfaces: `closure`, `interior`, `boundary_points`,
  `contains`, `is_open`, `is_closed`, `is_connected`, `is_compact`, `metric`,
  `metric_function`, `dist`.
- Posets: `le`, `lt`, `ge`, `gt`, covers, ideals, filters, chains, antichains,
  finite Hasse and interval methods, meet, join, lattice operations, polynomial
  invariants with polynomial codomains.
- Rings and algebras: `zero`, `one`, `characteristic`, `is_unit`, `ideal`,
  quotient/localization/completion routes, matrix-ring methods, algebra
  constructors, `algebra_generators`, `subalgebra`, ideals, radical, center,
  semisimple quotient, product and unit surfaces.
- Modules: `rank`, `dimension`, `basis`, `gens`, `gen`, `ngens`, coordinate and
  support methods, `submodule`, `span`, `quotient_module`, `intersection`,
  `saturation`, `dual`, `tensor`, `hom`, basis-defined morphisms, kernel, image,
  cokernel.
- Tensor components: `tensor_type`, `structure_constants`, `trace`, `contract`,
  symmetry/antisymmetry constructor metadata, dual-object evaluation routing.
- Hom/End/Aut: `domain`, `codomain`, `identity`, `zero`, evaluation, composition,
  `is_endomorphism_set`, `is_invertible`, `is_isomorphism`, `inverse`, `order`.
- Forms and lattices: `form`, form evaluation, `form_degree`, bilinear and quadratic
  evaluation, `is_isotropic`, orthogonal subobjects, `gram_matrix`, determinant,
  discriminant, dual lattice, discriminant group, divisibility as pairing-image
  submodule or ideal, primitive predicates, reflections, root predicates,
  orthogonal and special/stable orthogonal groups.
- Geometry and backend surfaces: varieties, curves, surfaces, divisors, sheaves,
  families, Picard/lattice objects, blowups, singularity resolution, Hilbert and
  Hodge invariants, canonical classes, genus, normalization, monodromy, orbit,
  stabilizer, embedding, isometry, and discriminant-form methods.

## Source Provenance

- `category_specs/*/docs/SAGE_INVENTORY.md`.
- `category_specs/*/docs/MAPPING.md`.
- `category_specs/AGENTS.md` and category-spec skills for grounding requirements.
- `theory/backends/software-capability-map.md`.
- `theory/backends/abstract-to-external-mapping.md`.
- `theory/backends/library-integration.md`.
- `theory/backends/comprehensive-tool-docs.md`.
- `theory/backends/oscar-lattices.md`.
- `theory/backends/gap-orbits.md`.
- `theory/backends/indefinite-jl.md`.
- `theory/backends/carat.md`.
- `theory/backends/vinberg-algorithm.md`.
- `theory/spec_backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`
  and `theory/spec_backups/lattices_written_spec_backup.py` for lattice-source mining
  only, with the warning already recorded in tracker cards: these are source material,
  not current API authority.

## Source Corpus Assignment

The method inventory workstream uses the following corpus map. Each source is assigned
to exactly one first-pass topical task so rows are not discovered ad hoc.

### Category Core

Assigned task: `TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES` for Hom/End/Aut
rows, with Cat construction selectors cross-linked into all topical outputs.

| Source | Scope |
| --- | --- |
| `category_specs/cat/docs/SAGE_INVENTORY.md` | Sage category objects, category order, functors, construction categories, Homsets/Endsets, Autsets, and local Cat files. |
| `category_specs/cat/docs/MAPPING.md` | Project category-object surface, containment, functors, standard constructions, constructor aggregation forwarders, slice/coslice, and Hom/End/Aut category-object routing. |
| `category_specs/homsets/docs/SAGE_INVENTORY.md` | Sage Homsets and Endset surfaces to represent. |
| `category_specs/homsets/docs/MAPPING.md` | Generic `C.HomCategory()`, `C.EndCategory()`, and `C.AutCategory()` ownership rows. |

### Sets And Topology

Assigned task: `TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY`.

| Source | Scope |
| --- | --- |
| `category_specs/sets/docs/SAGE_INVENTORY.md` | Root set, finite set, enumerated set, finite enumerated set, infinite enumerated set, facade set, concrete set wrapper, RealSet, ImageSet, partition, and set-constructor surfaces. |
| `category_specs/sets/docs/MAPPING.md` | Minimal owners for membership, cardinality, finite Python protocols such as `len(X)`, enumeration, subobject operations, image-object `ambient`/`lift`/`retract`, RealSet constructors, partitions, and rejected wrapper state. |
| `category_specs/topological_spaces/docs/SAGE_INVENTORY.md` | Topological, connected, compact, metric, complete metric, RealSet, interval, and numeric interval/ball surfaces. |
| `category_specs/topological_spaces/docs/MAPPING.md` | Topological/metric method owners, RealSet ambient-relative recovery, constructor routing through sets/rings, and topological ring/field recovery boundaries. |

### Rings Algebras And Modules

Assigned task: `TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES`.

| Source | Scope |
| --- | --- |
| `category_specs/rings/docs/SAGE_INVENTORY.md` | Ring category surfaces, construction surfaces, constructors, hom/end/aut routes, quotients, subobjects, matrix rings, p-adic/q-adic and precision families. |
| `category_specs/rings/docs/MAPPING.md` | Ring constructor namespace, matrix ring split, Hom/End/Aut mapping, topological rings, option-bag decisions, and q-adic precision gaps. |
| `category_specs/algebras/docs/SAGE_INVENTORY.md` | Magmatic, associative, unital, commutative, semisimple, with-basis, finite-dimensional algebra surfaces and constructors. |
| `category_specs/algebras/docs/MAPPING.md` | Algebra construction routing, free constructions, multiplication tensor boundary, basis/unit/product rows, subalgebra and ideal rows, radical/center/semisimple quotient rows. |
| `category_specs/modules/docs/SAGE_INVENTORY.md` | Module constructors, Sage category interop, free modules, vector spaces, homsets, subobjects, quotients, torsion/FinitelyPresented/PID modules, graded modules, Ore modules, and ring-side module bridges. |
| `category_specs/modules/docs/MAPPING.md` | Module category graph, method ownership rules, basis/generator boundaries, subobject/quotient/tensor/dual owners, primitive/divisibility boundary, graded/Ore/representation rows. |

### Forms Lattices And Torsion

Assigned task: `TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES`.

| Source | Scope |
| --- | --- |
| `category_specs/forms/docs/SAGE_INVENTORY.md` | Forms-subtree evidence and torsion quadratic form surfaces. |
| `category_specs/forms/docs/MAPPING.md` | Formed module owners, bilinear/quadratic owners, form-preserving morphisms, isometries, divisibility as pairing-image submodule or ideal, and lattice boundary. |
| `category_specs/lattices/docs/SAGE_INVENTORY.md` | Sage free quadratic modules, FGP modules, torsion quadratic modules, integral lattices, quadratic forms, and existing local lattice category surfaces. |
| `category_specs/lattices/docs/MAPPING.md` | Lattice tier table, minimal method placement, construction-category vocabulary, Sage type to spec-category map, forms-vs-lattices boundary, discriminant group and compatibility paths. |
| `theory/spec_backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage` | Mineable late-stage lattice-method source material only; reconcile against current mapping and written spec before admitting rows. |
| `theory/spec_backups/lattices_written_spec_backup.py` | Mineable written lattice-spec source material only; not current API authority and expected to change during lattice implementation. |

### Posets Tensors And Geometry-Facing Surfaces

Assigned task: `TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY`.

| Source | Scope |
| --- | --- |
| `category_specs/posets/docs/SAGE_INVENTORY.md` | Sage poset constructors, finite-poset surface, semilattice and finite-lattice surfaces. |
| `category_specs/posets/docs/MAPPING.md` | Poset hierarchy, root order methods, finite enumeration/Hasse methods, meet/join owners, deferred graph/polytope/polynomial/display surfaces, and slice/coslice structures. |
| `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` | Tensor component objects, tensor type, construction/recovery, component interop, and tensor-calculus surfaces. |
| `category_specs/tensor_algebra_components/docs/MAPPING.md` | Tensor constructor interop, `tensor_type`, `structure_constants`, `trace`, `contract`, symmetry metadata, private component storage, display rejection, and dual/form routing. |
| `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/**` | Geometry-facing feature, plan, phase, task, and spec surfaces that need method-owner/codomain rows before backend implementation. |

### Backend And External Software

Assigned task: `TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING`.

| Source | Scope |
| --- | --- |
| `theory/backends/software-capability-map.md` | Preferred mature systems, routing labels, gap protocol, backend note format, and update triggers. |
| `theory/backends/abstract-to-external-mapping.md` | Method-to-tool rows for varieties, curves, surfaces, divisors, sheaves, families, Picard/lattice objects, branched covers, and lattice-theoretic methods. |
| `theory/backends/library-integration.md` | Existing-library-first routing for current Coble/lattice tasks. |
| `theory/backends/comprehensive-tool-docs.md` | Extracted upstream tool documentation used by old mapping work. |
| `theory/backends/oscar-lattices.md` | Oscar/Hecke lattice and quadratic-form capabilities, including Julia/Oscar routing. |
| `theory/backends/gap-orbits.md` | GAP group-action, orbit, stabilizer, and finite group workflows. |
| `theory/backends/indefinite-jl.md` | Indefinite.jl isometry and orbit backend notes. |
| `theory/backends/carat.md` | CARAT capability audit and positive-definite limitations. |
| `theory/backends/vinberg-algorithm.md` | Vinberg-specific backend and algorithm guidance. |
| `theory/backends/buildings.md` | Buildings.sage capability notes. |
| `theory/backends/indefinite-isometry.md` | Indefinite isometry capability notes not covered by the Julia-specific file. |
| `theory/backends/foliation-lib-reusable-procedures.md` | Candidate reusable procedures for foliation-related backend surfaces. |

## Set Topology And Metric Method Rows

Source task: `TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY`.

These rows cover the first-pass admitted, rejected, or deferred set/topology surfaces.
They are source-grounded in `category_specs/sets/docs/SAGE_INVENTORY.md`,
`category_specs/sets/docs/MAPPING.md`,
`category_specs/topological_spaces/docs/SAGE_INVENTORY.md`, and
`category_specs/topological_spaces/docs/MAPPING.md`.

### Root Set And Construction Selectors

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `C.CartesianProducts()`, `C.Subquotients()`, `C.Quotients()`, `C.Subobjects()`, `C.IsomorphicObjects()` | category object | `Sets()` subcategory methods, inherited by set subcategories | Standard construction-category selectors on set categories. Codomain is the corresponding construction category. | Admitted. Sources: sets inventory section `Sets`; sets mapping rows for construction classes. |
| `C.Topological()` | category object | `Sets()` selector for `TopologicalSpaces()` | Refines a set category to sets with topology; equivalent exposed surface is `TopologicalSpaces()`. | Admitted. Sources: sets inventory section `Sets`; topological mapping `Sets().Topological()`. |
| `C.Metric()` | category object | `Sets()` selector for `TopologicalSpaces().Metric()` | Refines to metric spaces; metric spaces are topological spaces with topology induced by a metric. | Admitted. Sources: sets inventory section `Sets`; topological mapping `Sets().Metric()`. |
| `C.Algebras(base_ring)` | category object | `Sets()` construction selector, but method rows route concrete plain-set algebra calls through modules/algebras | Sage exposes an algebra functor category. Plain-set `S.algebra(R)` is not a public algebra constructor row here. | Admitted as selector only. Sources: sets inventory section `Sets`; sets mapping row for `algebra(R, category=None)`. |
| `C.Finite()`, `C.Infinite()`, `C.Enumerated()`, `C.Facade()` | category object | `Sets()` subcategory methods | Axiomatic/refinement selectors for finite, infinite, enumerated, and facade sets. | Admitted. Source: sets inventory section `Sets`. |

### Root Set Parent Methods

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `x in X` / `X.__contains__(x)` | parent protocol | `Sets().ParentMethods` | Membership predicate for any set object. Codomain is `bool`. | Admitted. Sources: sets inventory `Sets.ParentMethods`; sets mapping `Set_object` row. |
| `X.an_element()` / `_an_element_()` | parent method | `Sets().ParentMethods` | Produce a representative element for tests/examples. Codomain is an element of `X`; existence is implementation-dependent for empty sets. | Admitted. Sources: sets inventory `Sets.ParentMethods`; sets mapping `Set_object` row. |
| `X.some_elements()` | parent method | `Sets().ParentMethods` | Produce finite sample elements for testing. Codomain is a finite Python list of elements, not a mathematical finite subset unless wrapped by a constructor. | Admitted as test/sample surface. Source: sets inventory `Sets.ParentMethods`. |
| `X.cardinality()` | parent method | `Sets().ParentMethods` | Cardinality of a set, finite or infinite. Codomain is a cardinality object such as Sage integer or infinity. | Admitted. Source: sets mapping `Set_object` row. |
| `X.is_empty()` | parent method | `Sets().ParentMethods` | Predicate for empty set. Codomain is `bool`; enumerated sets may compute it by enumeration. | Admitted. Sources: sets mapping `Set_object` row; enumerated inventory. |
| `X.is_finite()` | parent method | `Sets().ParentMethods`; refined constant `True` on `Sets().Finite()` | Predicate for finite set. Codomain is `bool`; finite set axiom makes it constantly true. | Admitted. Sources: sets mapping `Set_object` row; finite-set inventory. |
| `X.subsets(size=None)` | parent method | `Sets().ParentMethods` | Power-set or fixed-cardinality subset construction. Codomain is a set of subsets. | Admitted. Source: sets mapping `Set_object` row. |
| `X.subsets_lattice()` | parent method | `Sets().ParentMethods` | Subset lattice construction of `X`. Codomain is a poset/lattice object; poset operations live in the poset subtree. | Admitted with poset codomain. Source: sets mapping `Set_object` row. |
| `X.union(Y)` | parent method | `Sets().ParentMethods` | Set union of two set objects. Codomain is a set object. | Admitted. Source: sets mapping `Set_object` row. |
| `X == Y`, `X <= Y`, `X < Y`, `X >= Y`, `X > Y`; `issubset`, `issuperset` | parent protocol/method | root set comparison surface | Equality is equality of elements; inequalities are subset/proper-subset and superset/proper-superset relations. Codomain is `bool`. | Admitted. Source: sets mapping `Rich Comparison Mapping Decisions`. |
| `X.free_module(R)` | parent method | `Sets().ParentMethods` method whose constructor owner is `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=X)` | Free `R`-module on the set. Codomain is a module object, not an algebra object. | Admitted with module constructor codomain. Source: sets mapping `Set_object` row. |
| `X.free_algebra(R)` | parent method | `Sets().ParentMethods` method whose constructor owner is `Algebras(R).Constructors().free_algebra_from_set(X)` | Free associative unital `R`-algebra generated by the set. Codomain is an algebra object. | Admitted with algebra constructor codomain. Source: sets mapping `Set_object` row. |
| `X._sympy_()` | parent interop method | `Sets().ParentMethods` where available | Export to SymPy set representation. Codomain is a SymPy object, not project mathematical structure. | Admitted as interop. Source: sets mapping `Set_object` row. |

### Enumerated Countable And Finite Set Methods

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `iter(X)` / `X.__iter__()` | parent protocol | `Sets().Countable()` / enumerated-set surface | Iteration witnesses countability or explicit enumeration, not arbitrary sethood. Codomain is an iterator over elements. | Admitted. Sources: sets mapping `Set_object` row; enumerated inventory. |
| `X.iterator_range(start, stop, step)` | parent method | `Sets().Enumerated()` | Iterate by rank range. Requires rank/unrank-style enumeration. | Admitted. Source: enumerated inventory. |
| `X.unrank_range(start, stop, step)` | parent method | `Sets().Enumerated()` | List elements by rank range. Codomain is a finite list of elements. | Admitted. Source: enumerated inventory. |
| `X[n]` / `X.__getitem__(n)` | parent protocol | `Sets().Enumerated()` | Shorthand for `unrank(n)`; slices route to rank ranges. Codomain is an element or finite list of elements. | Admitted. Source: enumerated inventory. |
| `X.unrank(n)` | parent method | `Sets().Enumerated()` | Return the element of rank `n`. Codomain is an element of `X`. | Admitted. Sources: enumerated inventory; sets mapping `rank`/`unrank` row. |
| `X.rank(e)` | parent method | `Sets().Enumerated()` | Index-of map for enumerated sets; meaningful for infinite countable sets as well. Codomain is a nonnegative integer when defined. | Admitted. Sources: enumerated inventory; sets mapping `rank`/`unrank` row. |
| `X.first()` | parent method | `Sets().Enumerated()` compatibility convenience | First enumerated element. This is derived from enumeration and is not a separate mathematical owner. | Admitted as derived compatibility method. Sources: enumerated inventory; sets mapping `rank`/`unrank` row. |
| `X.next(e)` | parent method | `Sets().Enumerated()` compatibility convenience | Successor in the chosen enumeration. Codomain is an element of `X` when defined. | Admitted as derived compatibility method. Sources: enumerated inventory; sets mapping `rank`/`unrank` row. |
| `X.random_element()` | parent method | `Sets().Enumerated()` computational surface | Random element where the implementation supplies a distribution; infinite enumerated sets may raise. Not a pure mathematical method without distribution data. | Deferred/interoperable. Source: enumerated and infinite-enumerated inventories. |
| `len(X)` / `X.__len__()` | parent protocol | `Sets().Finite().Enumerated()` / finite enumeration protocol | Integer conversion of finite cardinality. This is not a root `Sets()` method. | Admitted only for finite enumeration. Sources: finite-enumerated inventory; sets mapping finite wrapper row. |
| `list(X)` / `tuple(X)` | parent protocol | finite countable/enumerated sets | Python finite enumeration conversions. Do not make Sage `.list()` or `.tuple()` primary project methods. Infinite enumerated sets reject these. | Admitted as finite protocol, rejected as primary method names. Sources: sets mapping finite wrapper row; finite/infinite enumerated inventories. |
| `X._cardinality_from_iterator()`, `_list_from_iterator()`, `_rank_from_iterator(...)`, related cache helpers | parent internals | no public project owner | Implementation support for finite enumerated sets. | Interop/private only. Source: finite-enumerated inventory. |

### Subobject Image And Real-Subset Operations

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `X.intersection(Y)`, `X.difference(Y)`, `X.symmetric_difference(Y)`, `X.complement()` | parent/subobject method | `Sets().Subobjects()` / subsets with common ambient | These operations require a common ambient set. Codomain is a subset/subobject of that ambient. | Admitted under subobject owner. Source: sets mapping `Set_object` row. |
| `ImageSubobject(f, X)` project route | constructor | `Sets().Constructors().ImageSubobject(f: SetMorphism, domain_subset: Subset)` returning `_ImageSets` | Image of a set map on a domain subset, refining through `Sets().Subobjects()` and `Sets().Subquotients()`. | Admitted as named constructor route. Source: sets mapping `Sage ImageSubobject Admission Decision`. |
| `Y.ambient()` on image or real subset | parent/subobject method | `Sets().Subobjects()` / image-subobject refinement | Ambient codomain set containing the subobject. Codomain is a set object. | Admitted. Sources: image admission decision; RealSet inventory. |
| `Y.lift(x)` on image subobject | parent/subquotient method | `Sets().Subquotients()` / image-subobject refinement | Include an image element into the ambient set. Codomain is an ambient element. | Admitted. Source: image admission decision. |
| `Y.retract(x)` on image subobject | parent/subquotient method | `Sets().Subquotients()` / image-subobject refinement | Retract an ambient element to the image when defined. Codomain is an image element or partial-operation failure. | Admitted. Source: image admission decision. |
| `RealSet.interval`, `open`, `closed`, `point`, `open_closed`, `closed_open`, unbounded ray constructors, `real_line` | constructor/static method | `Sets().Constructors()` named real-subset constructors, with topological refinements on result | Construct named real-line subsets. Constructor ownership stays in sets; topology arrives by refinement. | Admitted as named constructor routes. Sources: RealSet inventory; topological mapping constructor decisions. |
| Variadic `RealSet(...)` | constructor | no catch-all project constructor | Sage accepts too many unrelated data shapes. Public project API uses closed named overloads. | Rejected as public catch-all. Sources: RealSet inventory; topological constructor mapping. |
| `RealSet.union`, `intersection`, `complement`, `difference`, `is_disjoint`, `is_subset`, `are_pairwise_disjoint`, `convex_hull` | parent/subobject methods | set/subobject operations with real-line representation | Real-subset operations whose mathematical owner is ordinary set/subobject structure, sometimes with a real-line interval codomain. | Admitted under set/subobject owners. Source: RealSet inventory. |
| `RealSet.n_components()`, `RealSet.get_interval(i)` | parent method | real-line finite-union decomposition surface | Component data of normalized finite unions of intervals. Codomain is a count/internals interval data; keep separate from root topology. | Deferred/real-subset-specific. Source: RealSet inventory. |

### Topological And Metric Methods

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `X.is_open(U)` | parent method | `TopologicalSpaces()` | Openness predicate for subset `U` relative to ambient topological space `X`. Codomain is `bool`. | Admitted. Source: root topological mapping. |
| `X.is_closed(U)` | parent method | `TopologicalSpaces()` | Closedness predicate for subset `U` relative to ambient topological space `X`. Codomain is `bool`. | Admitted. Source: root topological mapping. |
| `X.closure(U)` | parent method | `TopologicalSpaces()` | Smallest closed subset of `X` containing `U`. Codomain is a subset of `X`. | Admitted. Source: root topological mapping. |
| `X.interior(U)` | parent method | `TopologicalSpaces()` | Largest open subset of `X` contained in `U`. Codomain is a subset of `X`. | Admitted. Source: root topological mapping. |
| `X.boundary(U)` | parent method | `TopologicalSpaces()` | Boundary subset determined by closure and interior. Codomain is a subset of `X`. | Admitted. Source: root topological mapping. |
| `X.is_connected()` | parent method | `TopologicalSpaces()` / `TopologicalSpaces().Connected()` axiom fact | Predicate on the whole topological space, not a subset-transform method. Codomain is `bool`. | Admitted. Sources: root topological mapping; topological inventory. |
| `X.is_compact()` | parent method | `TopologicalSpaces()` / `TopologicalSpaces().Compact()` axiom fact | Predicate on the whole topological space. Codomain is `bool`. | Admitted. Sources: root topological mapping; topological inventory. |
| `U.is_open()`, `U.is_closed()`, `U.closure()`, `U.interior()`, `U.boundary()` for `RealSet` | subobject convenience | compatibility route to `U.ambient().<method>(U)` | Sage subset methods migrate to ambient-relative topological methods unless a separate subobject convenience is admitted. | Admitted only as migration/convenience route. Source: root topological mapping. |
| `TopologicalSpaces().Connected()` | category object | `TopologicalSpaces()` subcategory method | Connected topological spaces. | Admitted. Source: topological mapping and inventory. |
| `TopologicalSpaces().Compact()` | category object | `TopologicalSpaces()` subcategory method | Compact topological spaces. | Admitted. Source: topological mapping and inventory. |
| `TopologicalSpaces().Metric().Complete()` | category object | `TopologicalSpaces().Metric()` subcategory method | Complete metric spaces. Completeness is metric, not purely topological. | Admitted. Source: topological mapping and metric inventory. |
| `X.metric()` / Sage `metric_function()` | parent method | `TopologicalSpaces().Metric()` | Return the metric map `d: X x X -> RR` as a set morphism. Not the evaluated distance. | Admitted. Source: metric mapping. |
| `X.dist(x, y)` | parent method | `TopologicalSpaces().Metric()` | Evaluate the metric map on two points. Codomain is a real-valued distance object. | Admitted. Source: metric mapping. |
| `x.dist(y)` | element method | metric-space element convenience | Delegates to `x.parent().dist(x, y)`. Element API does not own metric structure. | Admitted as convenience. Source: metric mapping. |
| `x.abs()` on Sage metric examples | element method | no pure topological owner | Absolute value uses additive/ring structure and zero; route through topological ring/field or normed additive owner when sourced. | Rejected from pure topological root. Source: metric mapping. |
| `TopologicalSpaces().Metric().HomCategory()` | hom category | metric spaces | Short-map homsets: distance-nonincreasing maps, refining continuous maps. | Admitted with enforcement caveat. Source: metric mapping. |
| `TopologicalSpaces().Metric().CartesianProducts().dist(...)` | parent method | metric cartesian products | Sage product metric is maximum of factor distances, separate from product topology. | Admitted. Source: metric mapping. |
| `TopologicalSpaces().Constructors()` for real/complex fields, interval/ball fields, p-adic/q-adic fields | constructor | no pure topological constructor owner | These objects are constructed by rings/fields and recover topology by refinement. | Rejected as pure topological constructors. Source: topological ring and field recovery mapping. |

### Rejected Or Interop-Only Set Surfaces

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `Set(X)` generic wrapping | constructor | no public project owner | Sage generic wrapper accepts arbitrary objects and does not define one mathematical construction. Named cases must be admitted separately. | Rejected. Sources: sets constructor mapping; image admission decision. |
| `Set_object.object()` | parent method | no public project owner | Exposes wrapped Python object implementation state. | Rejected. Source: sets mapping `Set_object` row. |
| `_repr_()`, `_latex_()`, `__hash__()` as category obligations | representation/protocol | no mathematical method owner | Display and hashing are implementation behavior, not set-theoretic structure. | Rejected as method-owner rows. Source: sets mapping `Set_object` row. |
| `set(X)`, `frozenset(X)` on finite wrappers | Python export | no project set object owner | Python hash-set export is not a project set object. | Rejected as category vocabulary. Source: sets mapping `Set_object` row. |
| arbitrary callable conversion inside image-set constructors | constructor plumbing | no public project owner | Sage callable-to-map conversion is interop plumbing; public input is a set morphism. | Rejected. Source: image admission decision. |

## Acceptance Criteria

- [ ] Every admitted method row names the literal surface spelling, minimal owner category, mathematical definition or software interop meaning, hypotheses, codomain or return object, and source paths.
- [ ] Root-set methods, finite-set protocol methods such as `len(X)`, countable/enumerated methods, subobject operations, topology/metric methods, algebra/module methods, Hom/End/Aut methods, forms/lattice methods, tensor methods, poset methods, and geometry/backend methods are all inventoried or explicitly rejected with source provenance.
- [ ] External software mappings from Sage, Oscar/Julia, GAP, Singular, Macaulay2, CARAT, Indefinite.jl, and related local backend notes are represented as method rows or backend-routing rows rather than left in prose.
- [ ] Unresolved method-owner conflicts become decision cards with exact sources checked and no implementation task is allowed to guess a mathematical owner.

## Dependencies And Boundaries

- This spec is owned by `PLAN-CATEGORY-FOUNDATION-KERNEL` and executed through
  `PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP`.
- Do not create implementation cards from a method name until the method row has a
  minimal owner, hypotheses, and codomain.
- Do not treat Sage implementation inheritance as mathematical ownership. The same
  Sage class may witness methods owned by sets, modules, forms, Hom categories, or
  backend interop.
- Do not merge distinct meanings under one method name unless a source-grounded proof
  or decision card states the equivalence hypotheses.
- Backend algorithm rows route through mature software first; use the backend-routing
  labels from `theory/backends/software-capability-map.md`.

## Work Log

- 2026-05-05: Created target spec for the literal method ownership inventory workstream.
- 2026-05-06: Added source corpus assignment by topical inventory task.
- 2026-05-06: Added set, finite/enumerated, subobject, image, RealSet, topological,
  metric, and rejected/interop method rows.
