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
