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

## Ring Algebra And Module Method Rows

Source task: `TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES`.

These rows cover the first-pass admitted, rejected, or deferred ring, algebra, and
module surfaces. They are source-grounded in
`category_specs/rings/docs/SAGE_INVENTORY.md`,
`category_specs/rings/docs/MAPPING.md`,
`category_specs/algebras/docs/SAGE_INVENTORY.md`,
`category_specs/algebras/docs/MAPPING.md`,
`category_specs/modules/docs/SAGE_INVENTORY.md`, and
`category_specs/modules/docs/MAPPING.md`.

### Rings And Ring Constructions

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `zero()`, `one()` | parent | `Rings()` | Additive and multiplicative identities of a ring object. Codomain is the same ring's element type. | Admitted. Sources: rings inventory root ring surfaces; rings mapping square-matrix split. |
| `characteristic()` | parent | `Rings()` | Ring characteristic as a Sage integer quantity. Codomain is `Integer`. | Admitted. Sources: rings inventory category surfaces; algebra inventory records inherited algebra characteristic. |
| `is_unit()` and unit predicates | element | `Rings().ElementMethods` | Predicate that an element is invertible for ring multiplication. Codomain is `bool`; unit-group realizations remain ring-family refinements. | Admitted. Sources: rings task seed; rings inventory additional source areas. |
| `ideal(generators)`, `principal_ideal(generator)` | parent / ideal constructor | ring ideal surface under `Rings()` | Constructs a ring ideal from generators; side data belongs only where noncommutative ideal owners are explicitly named. Codomain is an ideal object over the ring. | Admitted with named routes. Sources: rings inventory `Ring Category Methods`; rings mapping construction categories. |
| `Ideal.gens()`, `gen(i)`, `ngens()`, `gens_reduced()` | ideal parent | ring ideal object | Returns ideal generators or reduced generators. Codomain is a finite tuple/family of ring elements. | Admitted. Source: modules inventory `Ideals As Module-Like Objects`. |
| `Ideal.ring()`, `base_ring()`, `apply_morphism(f)`, `reduce(x)` | ideal parent | ring ideal object | Ambient ring access, scalar base access, functorial image, and reduction modulo the ideal. Codomains are ring object, base ring, ideal/image object, and ring element. | Admitted. Source: modules inventory `Ideals As Module-Like Objects`. |
| `Ideal.norm()`, `absolute_norm()` | ideal parent | number-field or order ideal refinements | Norm invariants for number-field/order ideals. Codomain is a scalar integer where defined. | Admitted only on source-backed ideal refinements. Source: modules inventory number-field ideal rows. |
| `free_resolution()`, `graded_free_resolution()` on ideals | ideal parent | principal or graded ideal refinements | Free-resolution construction when Sage source supports it. Codomain is a module complex/resolution object. | Deferred outside supported hypotheses; generic implementation is principal-only. Source: modules inventory ideal caveats. |
| `quotient(I)`, `quo(I)`, `quotient_ring(I)` | parent | `Rings().Quotients()` | Quotient ring by an ideal or congruence datum; codomain is a quotient ring with quotient map/retract inherited from subquotients. | Admitted. Sources: rings inventory construction surfaces; rings mapping construction-category mapping. |
| `R / I` / `__truediv__` for rings | Python protocol | no public ring method owner | Sage rejects quotient syntax and directs callers to `quotient(I)`. | Rejected as public category vocabulary. Source: modules inventory `Ring Category Methods`. |
| `Rings().HomCategory()`, `EndCategory()`, `AutCategory()` | category object | ring-specialized Hom/End/Aut category | Ring homomorphisms, endomorphisms, and automorphisms preserving ring structure. Generic Hom/End/Aut rows are owned by the category-core task; ring rows add the ring-specific preservation contract. | Admitted. Sources: rings inventory construction surfaces; rings mapping construction-category mapping. |
| `CartesianProducts()`, `Subquotients()`, `Subobjects()`, `Quotients()`, `IsomorphicObjects()`, `WithRealizations()`, `Realizations()` | category object | `Rings()` construction categories | Product, subquotient, subring, quotient, transported-structure, and realization categories for rings. | Admitted. Sources: rings inventory functorial surfaces; rings mapping construction-category mapping. |
| `Rings().Constructors().ZZ()`, `QQ()`, fixed precision singleton constructors | constructor | `Rings().Constructors()` or field refinements below it | Fixed ring/field objects such as `ZZ`, `QQ`, `RR`, `CC`, `RIF`, and `CIF`. Codomain is the constructed ring refined into its algebraic and possible topological categories. | Admitted. Sources: rings inventory constructor families; rings mapping constructor namespace. |
| `PolynomialRing(...)` overload family | constructor | `Rings().Constructors()` | Polynomial-ring constructor with closed finite variable-shape overloads: `name`, `n` with `name`, `names`, `n` with `names`, single-count `var_array`, and names-external `n`. | Admitted only for documented closed shapes. Source: rings mapping constructor namespace. |
| higher-dimensional `var_array` positional shapes | constructor plumbing | no public project owner yet | Sage accepts unbounded dimension lists, but the project has no mathematical finite-indexing vocabulary for this input family. | Deferred/rejected for this inventory pass. Source: rings mapping constructor namespace. |
| `NumberField(...)`, `NumberFieldTower(...)` | constructor | number-field constructor refinements under `Rings().Constructors()` | Single defining-polynomial and tower construction routes with explicit Sage option names. Codomain is a number field or tower object. | Admitted with split names. Source: rings mapping constructor namespace. |
| `discriminant()`, `trace_pairing_discriminant(elements)`, `integral_basis()`, `ring_of_integers()`, `maximal_order()` | number-field parent | number-field and order refinements | Field discriminant, trace-pairing discriminant on supplied elements, and full-order construction/access. Codomains are scalar discriminant, basis/order objects. | Admitted with optional-prime variants split into named routes. Source: rings mapping number-field methods. |
| `Zp(...)`, `Qp(...)`, `ZpWithPrecisionCaps(...)`, `QpWithPrecisionCaps(...)`, `ZpRelaxed(...)`, `QpRelaxed(...)` | constructor | p-adic ring/field constructor refinements | Scalar, pair precision-cap, and relaxed-precision routes are distinct local-field constructors. | Admitted. Source: rings mapping constructor namespace. |
| `Zq(...)`, `Qq(...)`, `ZqFromPrimePower(...)`, `QqFromPrimePower(...)`, `ZqFromPrimePowerFactorization(...)`, `QqFromPrimePowerFactorization(...)` | constructor | q-adic ring/field constructor refinements | Unramified-extension constructors split by cardinality, prime-power pair, and factorization input. | Admitted for scalar precision routes. Source: rings mapping constructor namespace. |
| `ZqWithPrecisionCaps(...)`, `QqWithPrecisionCaps(...)` | constructor | q-adic constructor frontier | Split lattice precision-cap names are mathematically meaningful but not supported by installed Sage construction paths. | Deferred admitted names with Sage-gap implementation behavior. Source: rings mapping `Deferred Q-Adic Lattice Precision`. |
| `change_precision(precision, precision_type=None)`, `change_prime(p)`, `fraction_field()` | parent | `Rings().Approximate()` and p-adic/local-field refinements | Precision change, base-prime change, and passage to fraction field. Codomains are changed precision ring/field, changed-prime ring/field, and fraction field. | Admitted. Source: rings mapping signature decisions. |
| `_change_print_mode(print_mode)` and print-option changes | private/interoperability | no public category owner | Display-mode change is Sage print interop, not ring mathematics. | Interop-only/private. Source: rings mapping signature decisions. |
| `PowerSeriesRing(...)`, `MultivariatePowerSeriesRing(...)`, `LaurentSeriesRingFromPowerSeriesRing(...)`, `PuiseuxSeriesRingFromLaurentSeriesRing(...)` | constructor | `Rings().Constructors()` and series refinements | Series-ring construction split by univariate, multivariate, prefix-count, and underlying-series input routes. | Admitted with named routes. Source: rings mapping constructor namespace. |
| `MatrixRing(base_ring=R, n=n, sparse=False, implementation=None)` | constructor | `Rings().Constructors()` | Constructs the ambient square matrix parent. The returned parent also refines into `Algebras(R)` and `Modules(R).Free().FiniteRank()`. | Admitted. Sources: rings mapping matrix split; modules mapping square matrix recovery. |
| `matrix_from_matrix(matrix)`, `matrix_from_entries(entries)`, `matrix_from_rows(rows)`, `scalar_matrix(scalar)`, `diagonal_matrix(entries)`, `identity_matrix()`, `zero_matrix()` | parent / element constructor | square matrix parent under ring/algebra/module refinements | Element constructors for matrix parents; entries live in the base ring and ordered rows/entries are explicit finite data. | Admitted with named routes. Sources: rings mapping `MatrixSpace.matrix`; probe evidence from `rings/matrix_algebras.py`. |
| `row_space()`, `column_space()`, `from_vector(vector, order=None, coerce=True)` | parent | matrix parent as `Modules(R).Free().FiniteRank()` | Derived row/column free modules and coordinate-vector-to-matrix conversion. | Admitted under module owner, not ring owner. Sources: modules inventory matrix-space row; modules mapping square matrix recovery. |
| topological ring and field methods `is_open`, `is_closed`, `closure`, `interior`, `boundary`, `is_connected`, `is_compact` | inherited parent | `TopologicalSpaces()` through topological ring/field refinement | Topology-bearing rings inherit topological-space surfaces without duplicating method ownership in `rings`. | Admitted as inherited only. Source: rings mapping `Topological Rings`. |

### Algebras And Algebra Constructions

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `MagmaticAlgebras(R)` | category object | `MagmaticAlgebras(R)` | `R`-modules with bilinear multiplication; not necessarily associative or unital. | Admitted. Sources: algebras inventory category surfaces; algebras mapping opening definition. |
| `AssociativeAlgebras(R)` | category object | `MagmaticAlgebras(R).Associative()` / `AssociativeAlgebras(R)` | Associative `R`-algebras, not necessarily unital. | Admitted. Sources: algebras inventory; algebras mapping. |
| `Algebras(R)` | category object | associative unital algebra endpoint | Associative unital `R`-algebras. Ring and module methods are inherited; algebra-specific methods stay here. | Admitted. Sources: algebras inventory; algebras mapping. |
| multiplication `x * y` | element | `MagmaticAlgebras(R).ElementMethods` | Bilinear product on the underlying `R`-module. Codomain is an algebra element. | Admitted. Source: algebras mapping definitions and product-on-basis row. |
| `one()` | parent | `Algebras(R)` | Algebra unit element. Codomain is an algebra element. | Admitted. Sources: algebras inventory `AlgebrasWithBasis` inherited methods; algebras mapping `one_basis` row. |
| `characteristic()`, `has_standard_involution()` | parent | `Algebras(R).ParentMethods` | Characteristic inherited from base/ring behavior and standard-involution predicate. Codomains are `Integer` and `bool`. | Admitted. Source: algebras inventory method surfaces. |
| `basis()` on an algebra with a distinguished basis | parent | `Algebras(R).WithBasis()` | Distinguished algebra basis. Codomain is basis data, inherited from module `WithBasis` but refined by algebra structure. | Admitted. Source: algebras mapping basis row. |
| `one_basis()` | parent | no public algebra invariant owner | Sage basis index of the unit when the unit is a basis vector; project exposes `one()` and constructor unit data instead. | Interop-only. Source: algebras mapping `one_basis()` row. |
| `product_on_basis(i, j)` | parent/interoperability | no public method beyond element multiplication | Sage basis-index multiplication hook. Public algebra surface is `e_i * e_j`; construction supplies the multiplication tensor. | Interop-only. Source: algebras mapping `product_on_basis` row. |
| `algebra_generators()` | parent | `Algebras(R)` with generator-family refinement | Family of algebra elements generating the algebra. Codomain is an `AlgebraElementFamily`. | Admitted. Sources: algebras inventory method surfaces; algebras mapping. |
| `S.free_algebra(R)` for sets, magmas, semigroups, monoids, groups, additive semigroups, additive monoids, and additive groups | source parent method | source category method plus `Algebras(R).Constructors()` target | Free algebra construction selected by the source category, not by a runtime `category=` keyword. Codomain refines to magmatic, associative, or unital algebra as appropriate. | Admitted with named constructor targets. Source: algebras mapping `Free-Construction Routing`. |
| `S.algebra(R, category=...)` | Sage constructor plumbing | no public category-method owner | Sage's ambiguous runtime `category=` disambiguation is split into source-category methods and named constructors. | Rejected as public API. Source: algebras mapping free-construction routing. |
| plain-set `S.algebra(R)` | source parent method | `Sets().free_module(R)` / `Modules(R).Constructors().CombinatorialFreeModule` | Sage constructs a free module with basis indexed by `S`, not a project algebra constructor. | Rejected as algebra vocabulary and rerouted to modules. Source: algebras mapping plain-set route. |
| `Algebras(R).Constructors().from_multiplication_tensor(multiplication=mu)` | constructor | `Algebras(R).Constructors()` | Canonical finite-rank algebra constructor from a tensor `mu in T_R(M)[1,2]`; codomain is a magmatic/associative/unital algebra refinement according to verified laws. | Admitted. Source: algebras mapping `Multiplication Tensor Constructor`. |
| `FiniteDimensionalAlgebra(k, table, ...)` table/list/matrix input shapes | constructor input plumbing | `TensorAlgebraComponents(R).Constructors()` before algebra construction | Tables and matrices are interop inputs for constructing the multiplication tensor, not algebra constructor parameters. | Rerouted. Source: algebras mapping multiplication tensor boundary. |
| `subalgebra(generators)` | parent | `Algebras(R).Subobjects()` / subalgebra owner | Generated subalgebra. Codomain is an algebra subobject. | Admitted. Source: algebras inventory finite-dimensional methods; algebras mapping. |
| `left_ideal(generators)`, `right_ideal(generators)`, `two_sided_ideal(generators)` | parent | algebra ideal owner under `Algebras(R).Ideals(A)` | Algebra ideals as module subobjects with side predicates. Codomain is an `AlgebraIdeal`. | Admitted. Source: algebras mapping `ideal_submodule` split. |
| `principal_left_ideal(generator)`, `principal_right_ideal(generator)`, `principal_two_sided_ideal(generator)` | parent | algebra principal-ideal refinements | One-generator case of the corresponding named algebra ideal construction. | Admitted. Source: algebras mapping `principal_ideal` split. |
| `ideal_submodule(gens, side=...)`, `principal_ideal(a, side=...)` | Sage compatibility | no side-string public owner | Sage side strings are split into named methods; category and option bags are implementation routing. | Rejected as public spelling. Source: algebras mapping ideal rows. |
| `center()`, `radical()`, `semisimple_quotient()` | parent | finite-dimensional algebra with basis / semisimple refinements where required | Center algebra, Jacobson radical ideal, and semisimple quotient. Codomains are algebra, algebra ideal, and quotient algebra. | Admitted. Sources: algebras inventory finite-dimensional methods; algebras mapping. |
| `center_basis()`, `radical_basis()`, `annihilator_basis(...)` | parent | no public method beyond returned algebra/ideal objects | Sage returns implementation bases; public methods return the center, radical, or annihilator ideal object. | Interop-only/rerouted. Source: algebras mapping basis rows. |
| `derivations()` | parent | algebra derivation surface | Module or Lie algebra of derivations of the algebra. Codomain is the derivation module/algebra object. | Admitted. Source: algebras mapping derivation row. |
| `hochschild_complex(M)` | parent | `Algebras(R).WithBasis()` | Hochschild complex with coefficients in `M`. Codomain is a chain complex. | Admitted on source-backed with-basis algebra surface. Source: algebras inventory method surfaces. |
| `orthogonal_idempotents_central_mod_radical()`, `idempotent_lift(x)`, `is_identity_decomposition_into_orthogonal_idempotents(idempotents)` | parent | finite-dimensional algebra with basis | Idempotent decomposition and lifting operations modulo the radical. Codomains are families of idempotents or `bool`. | Admitted with finite-dimensional hypotheses. Source: algebras inventory finite-dimensional methods. |
| `peirce_summand(ei, ej)`, `peirce_decomposition(idempotents=None, check=True)` | parent | finite-dimensional algebra with basis | Peirce summands/decomposition attached to idempotents. Codomain is summand/decomposition data as algebra/module subobjects. | Admitted. Source: algebras inventory finite-dimensional methods. |
| `cartan_invariants_matrix()`, `isotypic_projective_modules(side='left')` | parent | finite-dimensional algebra with basis / representation-theoretic refinement | Cartan invariants and isotypic projective module data. Codomain is a matrix or finite family of modules. | Admitted with finite-dimensional hypotheses. Source: algebras inventory method surfaces. |
| `is_commutative()` | parent | `Algebras(R)` predicate and `Algebras(R).Commutative()` refinement | Predicate that multiplication is commutative; successful proof/refinement places object in commutative algebras. | Admitted. Source: algebras inventory finite-dimensional methods and commutative category row. |
| `__invert__()` on algebra-with-basis elements | element protocol | algebra element unit/inverse surface where defined | Sage implements inversion for scalar multiples of the basis unit. Public owner is the element inverse/unit surface, not the with-basis implementation class. | Admitted only under unit hypotheses; source: algebras inventory method surfaces. |
| `Algebras(R).TensorProducts()`, `CartesianProducts()`, `Quotients()` | category object | algebra construction categories | Algebra tensor products, products, and quotients; extra supercategories are implementation/category wiring, not separate public methods. | Admitted. Sources: algebras inventory method surfaces; algebras mapping construction rows. |

### Modules, Bases, Subobjects, Quotients, Tensor Products, And Duals

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `Modules(R).Constructors().FreeModule(rank)`, `VectorSpace(dimension)`, `CombinatorialFreeModule(basis_keys)` | constructor | `Modules(R).Constructors()` with free/finite-rank/basis refinements | Free-module, vector-space, and basis-key free-module constructors. Codomain is a module refined by free, finite-rank, over-field, with-basis, or ordered-generating-set hypotheses. | Admitted with split constructor names. Sources: modules inventory constructor entry points; modules mapping constructor namespace. |
| `FreeModuleWithoutBasis`, `VectorSpaceWithoutBasis`, inner-product row/entry constructors, `FreeQuadraticModuleFromRows`, `FreeQuadraticModuleFromEntries` | constructor | module constructor or forms-owned constructor depending on supplied form | Sage constructor shapes are named explicitly; inner-product/form data routes to formed-module owners. | Admitted or routed to forms. Source: modules mapping constructor namespace. |
| `span(gens, base_ring=None)`, `submodule(generators)`, `submodule_with_basis(generators)` | parent / construction | `Modules(R).Subobjects()` with free/field/PID/basis refinements | Generated submodule or subspace. Codomain is a submodule object; PID/field/echelon hypotheses determine algorithms and ordered-basis structure. | Admitted. Sources: modules inventory standard free modules; modules mapping method rules. |
| `rank()` | parent | `Modules(R).Free()` | Basis cardinality for a free module. Codomain is `Integer` or cardinality data where infinite-basis refinements exist. | Admitted. Source: modules mapping rank boundary. |
| `dimension()` | parent | finite-rank free modules or field-vector refinements | Finite basis cardinality/dimension alias where a finite-rank or vector-space hypothesis is present. | Admitted only with finite-rank hypotheses. Sources: modules mapping method rules; modules inventory `ModulesWithBasis`. |
| `basis()`, `basis().keys()`, `monomial(i)`, `term(i, coeff)`, `linear_combination_of_basis(terms)` | parent / element constructor | `Modules(R).WithBasis()` | Chosen basis data, basis-index access, basis element construction, and finite basis-term linear combinations. | Admitted. Source: modules mapping combinatorial free module method surface. |
| `gens()`, `gen(i)`, `ngens()` | parent | `Modules(R).WithOrderedGeneratingSet()` | Ordered generator access. If the generators are known to be a basis, inherited/refined owner is `WithOrderedBasis()`. | Admitted. Source: modules mapping method ownership rules. |
| `set_order(order)`, `get_order()`, `get_order_key()`, `_order_key(x)` | parent/private helper | `Modules(R).WithOrderedBasis()` for public order data | Public surface is ordered basis/term order. Sage order-key helpers remain interop-local. | Admitted public order data; private helpers interop-only. Source: modules mapping combinatorial rows. |
| `from_vector(vector, order=..., coerce=...)`, `coordinate_vector(x)`, `coordinates(x)`, `basis_matrix()` | parent | `Modules(R).WithOrderedBasis()` | Coordinate conversion between module elements and coordinate vectors relative to an ordered basis. Codomains are elements, coordinate vectors, or basis matrices. | Admitted with ordered-basis hypotheses. Sources: modules mapping method rules; modules inventory free-module methods. |
| element `monomial_coefficients()`, `__getitem__`, `coefficient()`, `items()`, `support()`, `support_of_term()`, `monomials()`, `terms()`, `coefficients()` | element | basis-bearing module element surface | Coordinate and support data of an element in a chosen basis. Codomain is finite support/key/coefficient data in the base ring. | Admitted with basis hypotheses. Sources: modules inventory `ModulesWithBasis`; modules mapping method rules. |
| element `__len__()`, `length()` | element | basis-bearing module element support surface | Size of finite support, not module dimension. Codomain is `Integer`. | Admitted only with chosen basis/sparse-support semantics. Source: modules mapping method ownership rules. |
| leading/trailing term methods, `map_coefficients`, `map_support`, `map_support_skip_none`, `map_item` | element | ordered-basis or sparse-support interop owner | Term-order-dependent element operations. Public admission requires ordered-basis semantics; implementation traversal helpers are interop-local. | Deferred/admitted only in ordered-basis cases. Source: modules mapping method rules. |
| `zero()`, module addition, scalar multiplication | parent / element | `Modules(R)` | Additive identity and `R`-module operations. Codomain is a module element. | Admitted. Sources: modules inventory Sage category interop; modules mapping method rules. |
| parent `sum(...)`, `linear_combination(...)`, `random_element(...)` | parent helper | no root module obligation unless extra structure is specified | Aggregation and sampling are computational helpers unless the public spec states finite-linear-combination vocabulary or a probability distribution. | Rejected/deferred as general category methods. Source: modules mapping method rules. |
| `change_ring(S)` | parent | module base-change surface | Base change returning an object in `Modules(S)` with compatible refinements where valid. | Admitted. Sources: modules inventory free modules; modules mapping combinatorial rows. |
| `direct_sum(...)`, `CartesianProducts()` | parent / category object | `Modules(R).CartesianProducts()` | Direct products/sums with componentwise module structure and common base-ring bookkeeping. | Admitted. Sources: modules inventory construction categories; modules mapping construction-category mapping. |
| `intersection(other)`, `saturation(...)`, `denominator()`, `index_in(other)` | parent/subobject | `Modules(R).Free().OverIntegralDomain()` or `OverPID()` and subobject refinements | Operations requiring domain/PID linear algebra. Codomains are submodules or scalar/index data. | Admitted with base-ring hypotheses. Source: modules mapping method ownership rules. |
| `ambient()`, `ambient_module()`, `ambient_vector_space()`, `lift(x)`, `retract(x)`, `reduce(x)`, `echelon_coordinate_vector(x)`, `echelonized_basis()`, `echelonized_basis_matrix()`, `has_user_basis()` | subobject parent | `Modules(R).Subobjects()` with basis/ordered-basis/PID/field refinements | Subobject ambient access, inclusion/retraction/reduction, and basis/echelon witnesses. | Admitted with construction hypotheses. Sources: modules inventory submodule methods; modules mapping required owners. |
| `quotient_module(submodule)`, `quotient_by_submodule`, `quotient_by_generators`, `quotient_by_relation_matrix`, `quotient_by_relation_rows`, `__truediv__` on modules | parent / construction | `Modules(R).Quotients()` | Quotient module construction by submodule, generators, relation matrix, or relation rows. Codomain is a quotient module refining subquotient structure. | Admitted with named public routes; Sage slash is compatibility syntax only. Source: modules mapping constructor namespace and method rules. |
| `cover()` / `V`, `relations()` / `W`, `free_cover()`, `free_relations()`, `quotient_map()`, `lift_map()`, `lift(x)`, `cokernel_basis_indices()` | quotient parent | `Modules(R).Quotients()` / `Subquotients()` with basis or PID refinements | Quotient presentation data, maps, lifts, and normal-form basis indices. | Admitted with quotient/basis hypotheses. Sources: modules inventory quotient methods; modules mapping basis-coordinate audit. |
| `invariant_factors()`, `invariants()`, `smith_form_gens()`, `smith_form_gen(i)`, `linear_combination_of_smith_form_gens(...)`, `free_part()`, `torsion_part()`, `annihilator()` | parent | `FinitelyPresentedModulesOverPID` and torsion/finite refinements | Smith-form and elementary-divisor data for finitely presented PID modules. Codomains are finite tuples, elements, submodules, or annihilator ideals. | Admitted with PID finite-presentation hypotheses. Sources: modules inventory FGP modules; modules mapping method rules. |
| element `additive_order()`, parent `cardinality()`, `is_finite()`, `list()`, `__iter__()` | element/parent | finite torsion or finite FGP module refinements | Finite-module enumeration and element order. Codomains are `Integer`, cardinality, finite list/iterator. | Admitted only for finite quotient hypotheses. Source: modules inventory FGP module caveats. |
| `hom(...)`, `_Hom_`, `module_morphism(...)`, `from_basis_map(f)`, `on_basis()` | hom parent / morphism | `Modules(R).HomCategory()` with `WithBasis().HomCategory()` refinements | Constructs or reads `R`-linear morphisms, especially basis-defined maps. Codomain is a module morphism or basis-index function. | Admitted. Sources: modules inventory Homsets; modules mapping hom-category decision. |
| hom element `matrix()`, evaluation `f(x)`, `kernel()`, `image()`, `cokernel()`, `coimage()`, `inverse_image(...)`, `lift(...)`, `is_injective()`, `is_surjective()`, `is_identity()`, `is_bijective()`, `inverse()` | morphism element | `Modules(R).HomCategory().ElementMethods` with free/PID/Ore/graded refinements | Linear-map evaluation and exactness constructions. Matrix access requires a presentation/basis. Codomains are elements, submodules, quotient modules, booleans, or morphisms. | Admitted with presentation hypotheses. Sources: modules inventory homsets; modules mapping construction categories. |
| `dual()` | parent | `Modules(R).DualObjects()` routed through `Modules(R).HomCategory()` | Linear dual `M^* = Hom_R(M, R)`. Codomain is a dual module that is also a Hom object. | Admitted. Source: modules mapping `Dual Objects As Hom Objects`. |
| morphism `dual()` | hom element | `Modules(R).HomCategory().ElementMethods` | Dual morphism `f^*: B^* -> A^*` for `f: A -> B`. | Admitted. Source: modules mapping dual-object consequences. |
| `tensor(...)`, `tensor_module(...)`, `tensor_factors()`, tensor-power construction methods | parent/category | `Modules(R).TensorProducts()` | Tensor product construction and factor access. Codomain is a tensor product module or factor tuple. | Admitted. Sources: modules inventory construction categories; modules mapping method rules. |
| `linear_form()`, `alternating_form()`, `symmetric_power(...)`, `exterior_power(...)`, `dual_symmetric_power(...)` | parent / construction | finite-rank free modules, tensor-component, dual-object, symmetric/exterior construction owners | Form and tensor-power constructors on finite-rank free modules. Codomains are dual/tensor/form objects. | Admitted where finite-rank hypotheses hold; detailed form rows belong to the forms/lattice task. Sources: modules inventory finite-rank tensor modules; modules mapping tensor component duals. |
| `degree`, `generator_degrees()`, `generator(i)`, `generators()`, `connectivity()`, `is_trivial()`, `has_relations()`, `relations()`, `suspension()`, `minimal_presentation()`, `resolution()`, `vector_presentation()` | graded parent/element | `Modules(A).Graded().Free()` or `Modules(A).Graded().FinitelyPresented()` | Graded generator, relation, presentation, suspension, connectivity, resolution, and vector-presentation data. | Admitted with graded algebra/PID hypotheses. Sources: modules inventory graded modules; modules mapping method rules. |
| `ore_ring()`, `twisting_morphism()`, `twisting_derivation()`, `pseudohom()`, `matrix()`, `multiplication_map()`, `identity_morphism()`, `injection_morphism()`, `projection_morphism()`, `morphism_restriction()`, `morphism_corestriction()`, `morphism_quotient()`, `morphism_modulo()` | Ore parent / morphism | Ore-algebra or semilinear-operator module owner | Ore-module structural data and morphism operations. Codomains are Ore rings, maps, matrices, morphisms, submodules, or quotients. | Admitted with Ore owner decision boundary. Source: modules inventory Ore modules; modules mapping retained-category rows. |
| `semigroup()`, `semigroup_algebra()`, `side()`, `representation_matrix(g)`, `character()`, `brauer_character()`, `invariant_module()`, `twisted_invariant_module()`, `is_irreducible()`, `subrepresentation()`, `quotient_representation()`, `composition_series()`, `composition_factors()` | representation parent | `Modules(R).WithAction(S, side)` and representation-module refinements | Module with specified semigroup/group/monoid action and side. Codomains are action data, matrices, characters, sub/quotient representations, or finite series data. | Admitted with source hypotheses. Source: modules inventory representation modules; modules mapping method rules. |
| representation `exterior_power(...)`, `symmetric_power(...)`, `schur_functor(...)`, tensor representation constructors | representation parent | representation module plus tensor/exterior/symmetric/Schur construction owners | Functorial constructions preserving representation data. | Admitted with representation hypotheses. Source: modules inventory representation modules. |
| `structure_ring()`, `structure_map()`, `module_generators()` | parent | ring-object-as-module or object-over/under module surface | Forgetful module structure supplied by a ring or algebra object. Ring operations remain in `rings`. | Admitted. Source: modules mapping required category owners and method rules. |
| `is_primitive()` on a module element | element / submodule predicate | cyclic-submodule inclusion primitive predicate | Routed through `v.span().inclusion().is_primitive()`, not through coordinate gcd or unit-divisibility. Codomain is `bool`. | Admitted only through primitive morphism/submodule notion. Source: modules mapping rank/divisibility boundary. |
| `divisibility()` from coordinate gcds or chosen generators | element | no module owner | This is not a source-grounded module definition and must not be conflated with formed-element divisibility. | Rejected. Source: modules mapping rank/divisibility boundary. |
| `_element_constructor_`, `_convert_map_from_`, `_coerce_map_from_`, `_from_dict`, `_repr_`, `_latex_`, `_sympy_`, `_magma_init_`, `_macaulay2_`, display and dense/sparse conversion hooks | implementation/interoperability | no public mathematical category owner unless a separate row states an invariant | Sage parent internals, coercion, display, representation, or backend bridge plumbing. | Interop-only/rejected as method-owner evidence. Source: modules mapping combinatorial and method ownership rules. |
| `is_exact()` on combinatorial free modules | parent | no module-category predicate owner in this inventory | Exact-arithmetic capability predicate, not module structure. | Deferred to exact-computation policy if admitted. Source: modules mapping combinatorial rows. |

## Hom Forms And Lattice Method Rows

Source task: `TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES`.

These rows cover the first-pass admitted, rejected, or deferred Hom/End/Aut, forms,
torsion-form, and lattice surfaces. They are source-grounded in
`category_specs/homsets/docs/SAGE_INVENTORY.md`,
`category_specs/homsets/docs/MAPPING.md`,
`category_specs/forms/docs/SAGE_INVENTORY.md`,
`category_specs/forms/docs/MAPPING.md`,
`category_specs/lattices/docs/SAGE_INVENTORY.md`,
`category_specs/lattices/docs/MAPPING.md`,
`category_specs/modules/docs/MAPPING.md`, and
`theory/foundations/bilinear-forms-duals-morphisms.md`.

### Generic Hom End And Aut Categories

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `C.HomCategory().Of(A, B)` | category object / hom parent constructor | `C.HomCategory()` | Hom object `Hom_C(A, B)` for objects `A, B in C`. Codomain is a hom parent whose elements are morphisms in `C`. | Admitted. Sources: homsets mapping project extension surface; homsets Sage inventory. |
| `domain()`, `codomain()` | hom parent | `C.HomCategory().Of(A, B)` | The source and target objects of the hom object. Codomain is an object of `C`. | Admitted. Source: homsets mapping project extension surface. |
| `identity()` | end/aut parent | `C.EndCategory().Of(A)` and `C.AutCategory().Of(A)` | Identity endomorphism or automorphism of `A`. | Admitted. Source: homsets mapping project extension surface. |
| morphism evaluation `f(x)` / `__call__` | hom element | `C.HomCategory().ElementMethods` | Evaluation of a morphism on an element of its domain. Codomain is an element of the codomain object. | Admitted. Sources: homsets mapping; bilinear forms foundations use morphism evaluation before matrix presentations. |
| morphism composition | hom element | `C.HomCategory().ElementMethods` | Composition of compatible morphisms. Codomain is a morphism in the appropriate hom object. | Admitted. Source: homsets mapping project extension surface. |
| `C.EndCategory().Of(A)` | category object / end parent constructor | `C.EndCategory()` | Endomorphism object `End_C(A) = Hom_C(A, A)`. | Admitted. Source: homsets mapping. |
| `is_endomorphism_set()` | hom parent / Sage interop | `HomCategory().EndCategory()` | Boolean Sage witness that a hom object is an end object. | Admitted as interop witness, not as a separate mathematical owner. Source: homsets Sage inventory. |
| `C.AutCategory().Of(A)` | category object / aut parent constructor | `C.AutCategory()` | Automorphism object `Aut_C(A)`, the invertible part of `End_C(A)`. | Admitted. Source: homsets mapping. |
| `end_category()` | aut parent | `C.AutCategory().Of(A)` | Returns the underlying endomorphism object from which the automorphism object is cut out. | Admitted. Source: homsets mapping. |
| `is_invertible()`, `is_isomorphism()`, `inverse()`, `order()` | aut element | `C.AutCategory().ElementMethods` | Invertibility/isomorphism predicates, inverse automorphism, and element order. Codomains are `bool`, automorphism, and order/integer data. | Admitted. Source: homsets mapping project extension surface. |
| `AutCategory.from_end_category` | construction helper | generic aut construction in `homsets/autsets.py` | Builds the public aut object from an end object through a private condition-subset bridge. | Admitted as construction route; raw condition object stays private. Source: homsets mapping. |
| `condition_set()` on aut objects | implementation detail | no public owner | Raw Sage `ConditionSet` bridge used to cut out invertible endomorphisms. | Rejected as public API. Source: homsets mapping. |
| local duplicate `EndCategory()` / `AutCategory()` selectors on hom construction classes | category selector | inherited `Cat` universal selectors | Universal category selectors own end/aut navigation; local duplicates are not separate method surfaces. | Rejected as local owner. Source: homsets mapping selector ownership. |

### Module Hom Specialization And Formed-Module Morphisms

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `zero()` on `Hom_R(M, N)` | hom parent | `Modules(R).HomCategory()` | Zero `R`-linear morphism. | Admitted. Sources: modules Sage inventory Homsets; modules mapping Hom-category extra-structure decision. |
| `base_ring()` on `Hom_R(M, N)` | hom parent | `Modules(R).HomCategory()` | Base ring of the module-hom object. Codomain is `R`. | Admitted. Source: modules Sage inventory Homsets. |
| `End_R(M)` as an algebra | end parent | `Modules(R).EndCategory()` | Module endomorphisms carry `R`-algebra structure in addition to generic end-category structure. | Admitted. Source: modules mapping Hom-category extra-structure decision. |
| form-preserving Hom containment | hom parent containment | `C.HomCategory().Of(M, N)` for `C <= FormedModules(R)` | A plain module morphism belongs to the formed-module Hom object exactly when it preserves the attached form data. | Admitted. Sources: forms mapping form-preserving morphisms; lattice-redesign category ABC morphism semantics. |
| `is_isometry()` on a formed-module morphism | hom element compatibility query | `C.HomCategory().Of(M, N)` for `C <= FormedModules(R)` | Isomorphism inside an already form-preserving Hom object. Codomain is `bool`. | Admitted as compatibility query, not a separate preservation owner. Source: forms mapping. |
| `orthogonal_group()` | parent | `C.AutCategory().Of(M)` for `C <= FormedModules(R)` | Orthogonal group `O(M, form) = Aut_C(M)`, the automorphism object in the relevant formed-module category. | Admitted. Sources: forms mapping; lattices mapping note (5); modules mapping construction-category mapping. |
| standalone `is_form_preserving()` as a public owner | morphism predicate | no public owner | Form preservation is Hom-object containment, not a separate mathematical surface. | Rejected. Source: forms mapping. |
| matrix equation `g^T G g = G` as owner of isometry | presentation-level check | no semantic owner | Matrix equations are implementation witnesses after presentations/bases are fixed. | Rejected as method owner. Sources: forms mapping; bilinear forms foundations. |

### Formed Modules Bilinear Quadratic And Symmetric Rows

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `Modules(R).WithForms()` / `FormedModules(R)` | category object | `forms.subcategories.with_forms.FormedModulesCategory` | Modules equipped with attached semilinear form data. `Modules(R).WithForms()` is the Sage-compatible route; forms owns the class and method surface. | Admitted. Sources: forms mapping ownership; lattice-redesign category ABC. |
| `form()` | parent | `FormedModules(R)` | Attached form object/data. Codomain is the form object with tensor source, codomain module, and scalar action. | Admitted. Source: lattices mapping method placement table. |
| `form_degree()` | parent | `FormedModules(R)` | Tensor degree/type of the attached form data. Codomain is degree/type data. | Admitted. Source: lattices mapping method placement table. |
| `twist(s)` | parent | `FormedModules(R)` | Same underlying module with form scaled by scalar `s`. | Admitted. Sources: forms mapping; lattices mapping method placement table. |
| bilinear evaluation `b(v, w)` | parent/element operation | `FormedModules(R).Bilinear()` | Bilinear form evaluation. Codomain is the form codomain module `S`. | Admitted. Source: lattices mapping method placement table. |
| `self_product(v)`, element `norm(v)` | element | `FormedModules(R).Bilinear().ElementMethods` | `b(v, v)`. `self_product` is generic; `norm` is Sage/lattice terminology for the same value. | Admitted with alias note. Source: lattices mapping note (7). |
| `is_isotropic(v)` | element/parent | `FormedModules(R).Bilinear()` | Predicate `b(v, v) = 0`. Codomain is `bool`. | Admitted. Source: lattices mapping method placement table. |
| `perp(v)` | element | `FormedModules(R).Bilinear().ElementMethods` | Orthogonal subobject `{w in M : b(v,w)=0}`. | Admitted. Source: lattices mapping method placement table. |
| `orthogonal_submodule_to(S)` | parent | `FormedModules(R).Bilinear()` | Orthogonal submodule to a submodule/subobject `S`. | Admitted. Source: lattices mapping note (4). |
| quadratic evaluation `q(v)` | parent/element operation | `FormedModules(R).Quadratic()` | Quadratic-form evaluation. Codomain is the quadratic-form codomain module. | Admitted. Source: lattices mapping method placement table. |
| `is_symmetric()`, `is_alternating()`, `is_nondegenerate()`, `is_definite()`, `is_indefinite()`, `is_integral()`, `is_rational()` | parent predicate | forms-owned bilinear axiom refinements | Witness/refinement predicates for formed-module axioms. Codomain is `bool`; successful checks refine the category. | Admitted. Sources: forms mapping ownership; lattices mapping method placement table. |
| `divisibility(v)` | element | `forms.subcategories.symmetric.SymmetricBilinearModulesCategory.ElementMethods` | Pairing-image submodule `<b(v,w) : w in M> <= S`; in the scalar-valued case `S = R`, this is an ideal of `R`. | Admitted. Sources: forms mapping symmetric divisibility; lattices mapping note (9); modules mapping divisibility boundary. |
| coordinate-gcd or chosen-generator `divisibility(v)` | element | no module/lattice owner | Coordinate gcds and principal generators are representations under extra hypotheses, not the invariant definition. | Rejected. Sources: forms mapping; modules mapping rank/divisibility boundary. |
| `orthogonal_complement(S)` | parent | `FormedModules(R).Bilinear().Symmetric()` | Symmetric left/right orthogonal complement of subobject `S`. Codomain is a submodule/subobject. | Admitted. Source: lattices mapping note (4). |
| `is_even()` | parent | `FormedModules(R).Bilinear().Integral()` | Evenness predicate for integral bilinear forms. Codomain is `bool`. | Admitted. Sources: lattices mapping method placement table; Nikulin source listed in task provenance. |
| `is_unimodular()` | parent | `FormedModules(R).Bilinear().Symmetric().Nondegenerate().Integral()` over an integral domain | Predicate `L = L^*` or determinant/unit condition when presented. | Admitted. Source: lattices mapping method placement table. |

### Free Bilinear And Torsion Form Rows

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `gram_matrix()` | parent | `forms.subcategories.free_bilinear.FreeBilinearModulesCategory` | Gram matrix of the bilinear form in the chosen free basis. Codomain is a matrix over the form/base ring. | Admitted. Sources: forms mapping; lattices Sage inventory Tier 0; lattices mapping note (1). |
| `inner_product_matrix()` | parent / Sage compatibility | free bilinear presentation surface, with `gram_matrix()` canonical | Sage source name for the stored form matrix. In public lattice semantics, avoid treating this as an inner product on indefinite forms. | Interop/admitted only as presentation alias if required. Sources: lattices Sage inventory Tier 0; lattice interface style guide. |
| `determinant()`, `discriminant()` | parent | `FreeBilinearModulesCategory` | Determinant of the Gram matrix and signed discriminant `(-1)^r det`. Codomain is a scalar. | Admitted. Sources: lattices Sage inventory Tier 0; lattices mapping method placement table. |
| `rank()` | parent | `Modules(R).Free()` | Rank of the underlying free module, inherited by free bilinear modules. | Admitted via module owner. Source: lattices mapping method placement table. |
| `signature_pair()`, `signature()` | parent | free symmetric bilinear modules over ordered integral-domain/fraction-field hypotheses; concrete `ZZ` algorithm at lattice refinement | Signature pair and signature after suitable base change. Codomains are `(Integer, Integer)` and `Integer`. | Admitted with algorithm caveat. Source: lattices mapping note (2); lattices Sage inventory Tier 3. |
| `direct_sum(other)` | parent | `FreeBilinearModulesCategory` | Orthogonal direct sum of formed modules. Codomain is a free bilinear formed module. | Admitted. Sources: lattices mapping; lattices Sage inventory Tier 3. |
| `tensor_product(other)` | parent | `FreeBilinearModulesCategory` | Tensor product with induced form. Codomain is a free bilinear formed module. | Admitted. Sources: lattices mapping; lattices Sage inventory Tier 3. |
| `base_change_to(ring)`, `rational_span()` | parent | free bilinear / free over integral domain owner | Base-change of the formed module and rational span `L tensor_R Frac(R)`. | Admitted. Sources: lattices mapping; bilinear forms foundations. |
| `gram_matrix_bilinear()`, `gram_matrix_quadratic()` | parent | torsion bilinear/quadratic formed-module owner | Torsion Gram matrices with quotient-valued codomains such as `Q/mZ` or `Q/nZ`. | Admitted. Sources: lattices Sage inventory Tier 2; lattices mapping note (6). |
| `value_module()`, `value_module_qf()` | parent | torsion bilinear/quadratic formed-module owner | Quotient-value modules for bilinear and quadratic torsion forms. | Admitted. Sources: lattices Sage inventory Tier 2; lattices mapping method placement table. |
| `primary_part(m)`, `normal_form()`, `brown_invariant()` | parent | torsion formed-module refinements | Primary part, canonical normal form, and Brown invariant. | Admitted. Source: lattices Sage inventory Tier 2. |
| `additive_order(v)`, element `lift(v)` | torsion element | torsion formed-module element methods | Additive order and lift to a covering/dual object where defined. | Admitted with torsion hypotheses. Source: lattices Sage inventory Tier 2 and FGP element rows. |
| `all_submodules()` on torsion forms | parent | torsion finite module/form owner | Enumerates all submodules. | Admitted only with finite torsion hypotheses; can be expensive but source-backed. Source: lattices Sage inventory Tier 2. |

### Lattices Discriminant Objects And Algorithmic Rows

| Literal surface | Object level | Minimal owner | Meaning, codomain, and hypotheses | Status and source |
| --- | --- | --- | --- | --- |
| `Lattices(R)` | category object | `lattices.LatticesCategory` endpoint over forms-owned chain | Named endpoint for integral, nondegenerate, symmetric, finite-rank free bilinear modules. | Admitted. Sources: forms mapping boundary; lattices mapping hierarchy overview; lattice-redesign category ABC. |
| `dual_lattice()` | parent | `Bilinear().Integral()` over integral-domain/fraction-field hypotheses, inherited by lattices | Dual formed object `L^* = {v in L_K : beta(v,L) subset R}`. | Admitted. Sources: lattices mapping note (3); bilinear forms foundations. |
| `discriminant_group()` | parent | same dual/discriminant formed-module owner, inherited by lattices | Finite torsion formed module `L^*/L` with discriminant form data. | Admitted. Sources: lattices Sage inventory Tier 3; lattices mapping note (3). |
| `inclusion_morphism()` | parent | `Bilinear().Integral()` over integral-domain/fraction-field hypotheses | Morphism `L -> L^*` induced by the bilinear form/adjoint map. | Admitted. Sources: lattices mapping note (3); bilinear forms foundations. |
| `Lattices(R).DualObjects()` | construction category | lattice dual-object construction | Canonical dual construction category; objects are dual lattices/formed dual objects. | Admitted. Source: lattices mapping construction-category vocabulary. |
| `Lattices(R).DualLattices()` | construction alias | compatibility alias only | Old lattice-specific spelling of `DualObjects()`. | Interop-only. Source: lattices mapping construction vocabulary. |
| `discriminant_class(x)` | dual element | `Lattices(R).DualObjects().ElementMethods` | Quotient class of a dual element in `L^*/L`. | Admitted. Source: lattices mapping note (8). |
| `discriminant_class()` on ordinary lattice elements | element | no nontrivial ordinary-element owner | Ordinary elements map to zero after inclusion `L -> L^*`; the nontrivial map is on dual elements. | Rejected as separate owner. Source: lattices mapping compatibility paths. |
| `is_primitive(M)` / element `is_primitive(v)` | subobject/element | free module over integral domain; element case via cyclic-submodule inclusion | Primitive submodule predicate; element predicate routes through `v.span().inclusion().is_primitive()`. | Admitted with owner split. Sources: lattices mapping method placement table; modules mapping divisibility boundary. |
| `sublattice(basis)` | parent | free bilinear modules over PID | Sublattice spanned by a basis/generating family under PID hypotheses. | Admitted. Source: lattices Sage inventory Tier 3; lattices mapping. |
| `overlattice(gens)`, `maximal_overlattice(p)` | parent | free symmetric nondegenerate integral formed modules; `OverZZ` for maximal algorithm | Finite-index same-rational-span overlattice constructions. | Admitted with algorithm/backing caveats. Sources: lattices mapping; lattices Sage inventory Tier 3. |
| `genus()`, `nikulin_invariants()` | parent | `Lattices(ZZ)` / `OverZZ + Free + Symmetric + Nondegenerate` | Local-global genus and discriminant invariants. | Admitted as lattice-specific algorithmic surface. Sources: lattices mapping method placement table; backend rows route Oscar/Hecke where relevant. |
| `is_isometric_to(other)`, rational/local isometry tests | parent/hom query | `OverZZ + Free + Symmetric + Nondegenerate` plus formed-module Hom/Aut semantics | Predicate for existence of a lattice isometry; codomain is `bool` plus future witness surface when admitted. | Admitted with backend routing. Sources: lattices mapping; backend inventory rows for Indefinite.jl/Oscar/CARAT. |
| `reflection(v)` | element | free symmetric nondegenerate formed-module element owner | Reflection `s_v(w) = w - 2b(v,w)/b(v,v) v`, with integrality of output a separate check. Codomain is an automorphism/rational automorphism witness. | Admitted. Source: lattices mapping method placement table. |
| `is_root(v)` | element | free symmetric integral formed-module element owner | Predicate `b(v,v) in {-2, 2}` in the current source-backed root convention. | Admitted. Source: lattices mapping method placement table. |
| `minimum()`, `maximum()`, `LLL()`, `short_vectors(n)`, `short_vectors_up_to_sign(n)`, `enumerate_short_vectors()`, `enumerate_close_vectors(target)` | parent | `Lattices(ZZ)` / `OverZZ + Free + Symmetric` algorithm surface | Reduction and vector-enumeration algorithms. Codomains are scalar extrema, reduced lattice/basis data, or iterators/families of lattice elements. | Admitted only as algorithmic rows with backend/package caveats; not evidence for positive-definite-only semantics. Sources: lattices Sage inventory Tier 3; lattices mapping method placement table. |
| `orthogonal_group()` / `automorphisms()` on lattices | parent | `C.AutCategory().Of(L)` for the relevant formed/lattice category `C` | Lattice orthogonal group as categorical automorphisms preserving the form. Sage `automorphisms()` is an alias. | Admitted, with `automorphisms()` interop alias. Sources: forms mapping; lattices Sage inventory Tier 3; lattices mapping note (5). |
| `special_orthogonal_group()`, `stable_orthogonal_group()` | aut parent | `Lattices(R).AutCategory().ParentMethods` | Determinant-one and stable/orientation-positive subgroup selectors on the lattice aut object. | Admitted only on aut parent with determinant/orientation realization prerequisites. Source: lattices mapping compatibility paths. |
| lattice-object `L.special_orthogonal_group()`, `L.stable_orthogonal_group()` | parent | no lattice-object owner | Former object calls route through `L.orthogonal_group().special_orthogonal_group()` and `L.orthogonal_group().stable_orthogonal_group()`. | Rejected as owner. Source: lattices mapping compatibility paths. |
| `quadratic_form()` | parent | free symmetric formed-module presentation conversion | Converts a free symmetric bilinear presentation to a quadratic-form object/presentation. | Admitted as conversion, not a separate owner for the underlying object. Sources: lattices Sage inventory Tier 3 and Tier 4; lattices mapping. |
| public Sage escape hatches such as `sage_lattice()`, `inner_product_matrix()` as lattice identity, ambient/inclusion/projection matrix state | implementation detail | no public lattice owner | Internal Sage/Julia objects and ambient-vector-space state are calculation engines or presentation data, not public semantics. | Rejected. Sources: lattice-redesign interface style guide and corrections spec. |

## Backend And External Software Method Rows

Source task: `TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING`.

These rows translate `theory/backends/abstract-to-external-mapping.md` through the
routing statuses in `theory/backends/software-capability-map.md`. A backend row never
approves bespoke local mathematics. It says which semantic project object should own the
method and which mature external system should be audited or wired.

### Algebraic Geometry And Sheaf Backends

| Source surface | Project owner and codomain | Backend route and status | Source and consequence |
| --- | --- | --- | --- |
| `Variety.blowup(center)` | `Varieties().ParentMethods`; codomain is a variety or blowup object over the same base context with exceptional divisor data. | Macaulay2 Schubert2 `blowup(i)`; `bridge-needed`. | Source: `abstract-to-external-mapping.md`. Wire Macaulay2 rather than implementing blowups locally. |
| `Variety.resolve_singularities()` | singular variety surface; codomain is a resolution morphism or resolved variety once the geometry interface fixes that object. | Singular `resbin.lib`; `candidate-backend`. | Source: abstract map. Requires support audit before implementation. |
| `Variety.picard_group()` | variety/surface Picard-group surface; codomain is a Picard group object, with lattice realization only after source-backed construction. | Sage `PicardGroup` or Oscar integer lattices; `candidate-backend`. | Source: abstract map. Do not postulate Picard lattices as inputs. |
| `Variety.kodaira_dimension()` | proper variety surface; codomain is an integer dimension or `-infinity` sentinel as specified by geometry docs. | Macaulay2 sheaf cohomology plus Sage interpolation; `bridge-needed`. | Source: abstract map with Stacks Tag 0BJ8 reference. Needs exact hypotheses for properness and canonical powers. |
| `Variety.hilbert_polynomial()` | projective variety or graded coordinate object; codomain is a polynomial. | Macaulay2 `hilbertPolynomial`; `bridge-needed`. | Source: abstract map. Polynomial arithmetic belongs to the returned polynomial ring. |
| `Variety.hodge_number(p, q)` | smooth/proper variety surface after geometry specs fix hypotheses; codomain is an integer. | Macaulay2 sheaf cohomology through `HH^i(cotangentSheaf(p, X))`; `candidate-backend`. | Source: abstract map. Requires geometry owner and package support audit. |
| `Variety.holomorphic_euler_characteristic()` | coherent-sheaf/variety invariant surface; codomain is an integer. | Macaulay2 sheaf cohomology; `bridge-needed`. | Source: abstract map. Formula row is definition-level; backend computes dimensions. |
| `Variety.canonical_class()` | variety/divisor surface; codomain is a divisor or canonical class object. | Macaulay2 `canonicalDivisor(X)`; `bridge-needed`. | Source: abstract map and Macaulay2 docs link in that file. |
| `Surface.birational_involution()` | surface-specific automorphism/birational-map surface; codomain is a birational self-map object. | Sage Enriques functionality; `candidate-backend`. | Source: abstract map. Needs geometry category owner before implementation. |
| `Blowup.exceptional_divisor()` | blowup object surface; codomain is a divisor object. | Macaulay2 Schubert2 `exceptionalDivisor`; `bridge-needed`. | Source: abstract map. |
| `CobleSurface.from_singular_sextic()` | constructor/factory route under the future Coble surface category; codomain is a Coble surface object with provenance. | Singular for nodes plus Sage blowup; `candidate-backend`. | Source: abstract map. This is downstream of category/lattice substrate and not current implementation permission. |

### Curve Plane-Curve And Divisor Backends

| Source surface | Project owner and codomain | Backend route and status | Source and consequence |
| --- | --- | --- | --- |
| `Curve.genus()` | curve invariant surface; codomain is an integer. | Singular `brnoeth.lib: Adj_div` or Macaulay2 `geometricGenus`; `bridge-needed`. | Source: abstract map. |
| `Curve.arithmetic_genus()` | curve invariant surface; codomain is an integer. | Singular `brnoeth.lib: Adj_div`; `bridge-needed`. | Source: abstract map. |
| `Curve.normalization()` | curve construction surface; codomain is a normalized curve plus normalization map when the geometry owner admits it. | Sage `normalize()` or Singular `normalize`; `candidate-backend`. | Source: abstract map. |
| `PlaneCurve.equation()` | plane-curve object surface; codomain is the defining polynomial in its coordinate ring. | Sage direct access; `preferred-backend`. | Source: abstract map. This is object data access, not an algorithmic kernel. |
| `PlaneCurve.dual_curve()` | plane-curve construction surface; codomain is a plane curve in the dual projective plane. | Sage `dual`; `candidate-backend`. | Source: abstract map. Needs current Sage support audit before wiring. |
| `RationalSextic.is_nodal()` | rational-sextic predicate; codomain is `bool`, with node certificates in a separate witness surface if needed. | Singular `solve.lib`; `bridge-needed`. | Source: abstract map. |
| `RationalSextic.nodes()` | rational-sextic singularity surface; codomain is a finite set of node points with scheme/field data. | Singular `solve.lib`; `bridge-needed`. | Source: abstract map. |
| `RationalSextic.normalization()` | rational-sextic curve construction surface; codomain is a normalization map/object. | Sage `normalize()`; `candidate-backend`. | Source: abstract map. |
| `Divisor.riemann_roch_space_dimension()` | divisor/coherent-sheaf surface; codomain is an integer dimension. | Singular `brnoeth.lib: BrillNoether` or Macaulay2; `candidate-backend`. | Source: abstract map. |
| `Divisor.is_ample()` | divisor positivity predicate; codomain is `bool` plus optional certificate surface. | Macaulay2 `isVeryAmple` or Nakai-Moishezon style test; `candidate-backend`. | Source: abstract map. Requires exact positivity owner and hypotheses. |
| `Divisor.is_nef()` | divisor positivity predicate; codomain is `bool` plus optional curve-intersection witnesses. | Intersection-theory route; `candidate-backend`. | Source: abstract map. Needs backend research before implementation. |
| `Divisor.self_intersection()` | divisor intersection surface; codomain is a scalar/intersection number. | Macaulay2 intersection theory; `bridge-needed`. | Source: abstract map. |
| `Divisor.intersection(other)` | divisor-pairing surface; codomain is scalar, cycle, or intersection object as geometry spec decides. | Macaulay2 intersection theory; `bridge-needed`. | Source: abstract map. |

### Picard Lattice Cover Sheaf And Family Backends

| Source surface | Project owner and codomain | Backend route and status | Source and consequence |
| --- | --- | --- | --- |
| `PicardGroup.intersection_matrix()` | Picard group with intersection pairing; codomain is a Gram/intersection matrix or formed module row after the lattice owner is fixed. | Oscar `gram_matrix`; `bridge-needed`. | Source: abstract map. |
| `PicardeLattice.underlying_picard_group()` | source surface is malformed or typo-like; intended owner appears to be a Picard-lattice wrapper returning a Picard group. | Direct mapping; `candidate-backend`. | Source: abstract map. Public spelling blocked by `DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES`. |
| `DoubleCover.total_space()` | double-cover object surface; codomain is the total space object. | Sage weighted projective-space construction; `candidate-backend`. | Source: abstract map. |
| `K3DoubleCover.cover_surface()` | K3 double-cover surface; codomain is the covered/base surface. | Sage K3 surface constructor; `candidate-backend`. | Source: abstract map. |
| `EnriquesQuotient.k3_cover()` | Enriques quotient surface; codomain is the K3 cover object. | Sage Enriques/K3 route; `candidate-backend`. | Source: abstract map. |
| `CoherentSheaf.h0()`, `CoherentSheaf.h1()` | coherent-sheaf cohomology surface; codomain is an integer dimension. | Macaulay2 `dim HH^0(F)` and `dim HH^1(F)`; `bridge-needed`. | Source: abstract map. |
| `CoherentSheaf.euler_characteristic()` | coherent-sheaf invariant surface; codomain is an integer. | Macaulay2 `chi(F)`; `bridge-needed`. | Source: abstract map. |
| `CoherentSheaf.rank()` | coherent-sheaf invariant surface; codomain is rank where defined. | Macaulay2 `rank(F)`; `bridge-needed`. | Source: abstract map. |
| `FamilyOfVarieties.specialization()` | family surface; codomain is a specialized fiber/object. | Sage degeneration handling; `candidate-backend`. | Source: abstract map. Needs current Sage capability audit. |
| `FamilyOfVarieties.monodromy()` | family/local-system surface; codomain is monodromy representation or operator data. | Sage monodromy; `candidate-backend`. | Source: abstract map. |

### Lattice And Group-Action Backends

| Source surface | Project owner and codomain | Backend route and status | Source and consequence |
| --- | --- | --- | --- |
| `CobleSurface.coble_lattice()` | downstream Coble surface method; codomain is a lattice or formed module constructed from geometry. | Oscar integer lattices; `candidate-backend`. | Source: abstract map. Not current-phase implementation permission. |
| `Lattice.discriminant_group()` | lattice/discriminant construction surface; codomain is a finite discriminant group with form when applicable. | Oscar `discriminant_group(L)`; `bridge-needed`. | Sources: abstract map and `software-capability-map.md`. |
| `Lattice.primitive_embedding()` | lattice embedding surface; codomain is embedding data or candidate embedding objects. | Oscar `primitive_embeddings(L, M)`; `bridge-needed`. | Sources: abstract map and library-integration note. |
| `Lattice.automorphism_group()` | formed-module/lattice `AutCategory` surface; codomain is the automorphism group in the relevant category. | CARAT `Aut_grp` for positive definite forms; Indefinite.jl `automorphism_group` for indefinite forms; `candidate-backend`. | Sources: abstract map, `carat.md`, `indefinite-jl.md`. Do not force CARAT onto indefinite input. |
| `Lattice.isometry_test()` | isometry predicate between formed modules/lattices; codomain is `bool` plus optional isometry witness. | Indefinite.jl `test_equivalence`; `bridge-needed`. | Sources: abstract map and `indefinite-jl.md`. |
| `Lattice.orbit_representatives()` | orthogonal-group or subgroup action surface; codomain is representatives with stabilizer/certificate data when needed. | Indefinite.jl `get_orbit_representative`; `candidate-backend`. | Sources: abstract map, `indefinite-jl.md`, orbit backend notes. |
| `Lattice.vinberg_sh姚()` | malformed source surface; intended Vinberg/chamber/root method not admitted under this literal spelling. | Vinberg algorithm through Oscar/Vinberg backend candidates; `candidate-backend`. | Sources: abstract map and `vinberg-algorithm.md`. Public spelling blocked by `DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES`; bespoke implementation is not approved. |
| `GroupAction.orbit(x)` / orbit enumeration rows | group-action surface attached to finite group actions, graph automorphism actions, or orthogonal subgroup actions. | GAP `Orbit`, `OrbitsDomain`, GRAPE/Digraphs where relevant; `bridge-needed`. | Sources: `software-capability-map.md` and `gap-orbits.md`. Prefer GAP over custom orbit enumeration. |
| `GroupAction.stabilizer(x)` | group-action surface; codomain is subgroup or stabilizer object. | GAP `Stabilizer`; `bridge-needed`. | Sources: `software-capability-map.md` and `gap-orbits.md`. |
| centralizer/finite-image subgroup operations | automorphism-group or subgroup-action surface; codomain is subgroup or finite quotient data. | GAP, Oscar, or backend-specific finite quotient route; `candidate-backend`. | Sources: `gap-orbits.md`, `library-integration.md`, orbit/building backend notes. |

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
- 2026-05-06: Added backend and external software routing rows for the abstract method
  map, including malformed-source follow-up routing.
- 2026-05-06: Added ring, algebra, and module method rows covering constructor,
  basis/generator, ideal, quotient, tensor, dual, Hom, PID, graded, Ore, representation,
  matrix, and rejected interop surfaces.
- 2026-05-06: Added Hom/End/Aut, module-hom, formed-module, bilinear/quadratic,
  symmetric divisibility, free/torsion form, lattice, discriminant-object, orthogonal
  group, and lattice-algorithm ownership rows.
