---
id: SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Specify literal method ownership inventory by minimal category
status: unstarted
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
