---
id: TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn: []
title: Research category integration for toric varieties with lattice categories
status: needs-review
priority: high
description: Research and prepare the category-spec integration path for toric varieties,
  explicitly including integration with the lattice category.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this
  category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors,
  Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation
  cards needed to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for toric varieties with lattice categories

## Summary

Research and prepare the category-spec integration path for toric varieties, explicitly including integration with the lattice category.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating toric varieties, explicitly including integration with the lattice category.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Dependencies And Boundaries

This is a research/planning card, not an implementation card. Do not write category code or specs until the vocabulary, ownership boundaries, and dependencies are clear or an approved plan delegates that work.

## Research Result

Status: needs review. Toric varieties are source-grounded as normal varieties
associated to rational polyhedral fans in a finite-rank free abelian group. The
toric "lattice" involved here is character/cocharacter free `ZZ`-module data, not the
repo's symmetric-bilinear `Lattice` endpoint. This card does not authorize
implementation.

## Mathematical Definition

Source evidence:

- `TASK-INTEGRATE-VARIETIES-CATEGORY` records `Varieties(k)` as integral separated finite-type schemes over `k`.
- Sage toric lattice documentation, https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/toric_lattice.html, records toric lattices as objects isomorphic to `ZZ^n`, with paired dual lattices conventionally named `N` and `M`, designed to prevent mixing elements from incompatible lattices.
- Sage toric variety documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/variety.html, constructs `ToricVariety(fan, ...)` from a rational polyhedral fan and exposes the fan as structural data.
- Sage fan morphism documentation, https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/fan_morphism.html, defines fan morphisms as lattice morphisms compatible with specified fans and notes induced morphisms between associated toric varieties.
- OSCAR normal toric variety documentation, https://docs.oscar-system.org/v1/AlgebraicGeometry/ToricVarieties/NormalToricVarieties/, distinguishes affine normal toric varieties associated to cones from normal toric varieties associated to polyhedral fans, citing Cox-Little-Schenck notation `U_sigma` and `X_Sigma`.
- OSCAR toric morphism documentation, https://docs.oscar-system.org/v1.4/AlgebraicGeometry/ToricVarieties/ToricMorphisms/, states that compatible `ZZ`-linear maps of fan lattices induce exactly the toric morphisms.
- `SPEC-MAPPING-MODULES.md` and `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` admit `Modules(ZZ).Free().FiniteRank()` as the ordinary free-module owner and reserve `Lattices(ZZ)` for integral nondegenerate symmetric finite-rank free bilinear modules.

Project vocabulary:

- `ToricLattices()` should be a toric refinement of `Modules(ZZ).Free().FiniteRank()` or a named character/cocharacter lattice pair surface, not a refinement of the repo's formed `Lattices(ZZ)`.
- `CharacterLattice()` and `CocharacterLattice()` should be dual finite-rank free `ZZ`-modules with the natural pairing `M x N -> ZZ`.
- `RationalPolyhedralFans(N)` should own cones, rays, faces, subdivisions, smoothness/simplicial/completeness predicates, and fan morphism compatibility.
- `NormalToricVarieties(k)` should be varieties over `k` constructed from fans in a cocharacter lattice, with fan and torus data retained as structure.
- `AffineNormalToricVarieties(k)` are cone-owned affine refinements; projective, complete, smooth, simplicial, orbifold, Fano, and CPR-Fano toric varieties are stricter refinements.

Boundary decisions:

- Do not identify toric lattices with Coble/Nikulin/formed lattices. The toric object is a free abelian group, usually with a dual, not a finite-rank free module equipped with a symmetric bilinear form.
- Do not attach toric fan methods to all varieties. The fan is extra toric structure; only toric refinements own `fan()`, `rays()`, `cones()`, `orbit_closure(...)`, fan subdivision, and toric resolution surfaces.
- Do not treat a lattice polytope, normal fan, cone, or fan as the same object as the toric variety. These are constructor or structural inputs with their own polyhedral owners.
- Toric morphisms are not arbitrary scheme morphisms: the toric-refinement owner is compatible lattice/fan morphism data, with the induced scheme morphism as codomain evidence.
- Picard, class-group, Cartier/Weil divisor, and invariant-divisor methods should inherit broad variety/divisor/Picard owners where possible and add toric combinatorial routes only on toric refinements.

## Sage Surface Survey

Source evidence:

- Sage `ToricLattice(rank, name, dual_name, ...)` constructs named dual free abelian lattices and prevents accidental mixing of elements from different toric lattices.
- Sage `ToricVariety(fan, coordinate_names=None, base_ring=..., base_field=...)` constructs toric varieties from rational polyhedral fans and a field-like base.
- Sage toric varieties expose `fan()`, `orbit_closure(cone)`, `embedding_morphism()`, `rational_class_group()`, `resolve(...)`, `resolve_to_orbifold()`, `is_smooth()`, and `is_orbifold()`.
- Sage fan morphisms expose domain/codomain fans, compatibility checks, dominance, fibration, and injectivity predicates for lattice maps between fans.

Inference:

Sage is strong implementation evidence for toric lattices, fans, toric varieties, orbit closures, class groups, and fan-subdivision resolution routes. The project should translate this into mathematical owners rather than copying Sage's constructor shapes as the public spec.

## Backend Survey

Source evidence:

- OSCAR `NormalToricVariety` and `AffineNormalToricVariety` provide fan/cone constructors, famous toric varieties, affine open coverings, Q-Gorenstein checks, character lattices, class groups, Picard-group maps, and torus-invariant divisor groups.
- OSCAR toric morphisms construct morphisms from mapping matrices or finite-generated abelian group homomorphisms when the lattice map is compatible with the fans.
- `.agents/memories/theory/backends/software-capability-map.md` lists polymake, Normaliz, Sage wrappers, and Oscar candidates for cones, Hilbert bases, lattice-point enumeration, toric and polyhedral work.
- Polymake toric documentation, https://polymake.org/doku.php/user_guide/tutorials/apps_fulton, provides a toric/fan-oriented backend route for polyhedral and toric computations.

Inference:

Sage and OSCAR are preferred candidates for toric varieties and toric morphisms. Polymake/Normaliz remain candidate backends for polyhedral fan/cone/lattice-point kernels. No local toric or polyhedral algorithm should be implemented before a backend audit picks the exact route.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the variety substrate.
- `TASK-INTEGRATE-POLYTOPES-CATEGORY` and `TASK-INTEGRATE-POLYHEDRA-2D-POLYTOPES-CATEGORY` still need to admit polytope/polyhedron/fan-related vocabulary.
- `SPEC-MAPPING-MODULES.md` supplies finite-rank free module ownership for the toric lattice/free-abelian-group layer.
- `SPEC-MAPPING-LATTICES.md` and the ModulesWithForms roadmap reserve the repo `Lattice` endpoint for formed modules with symmetric bilinear data.
- `theory/references/literature/aegs_2023.md` contains downstream Coble/K3 references where toric surfaces, polytopes, and altered lattices appear as source material, but those are downstream geometry claims rather than generic toric API authority.

Inference:

The toric card should stabilize the free-module/fan/toric-variety boundary now and leave detailed polytope/fan constructors to polyhedral source-admission cards. It should explicitly prevent the word "lattice" from routing toric data into the formed-lattice roadmap.

## Method Ownership Guidance

Admit these as toric-level or toric-refinement surfaces when downstream specs are written:

- `character_lattice()` and `cocharacter_lattice()`: owned by toric varieties or torus/fan data; codomains are finite-rank free `ZZ`-modules with dual pairing.
- `fan()`: owned by normal toric varieties, returning a rational polyhedral fan in the cocharacter lattice.
- `rays()`, `cones()`, `maximal_cones()`, `faces()`, `subdivide(...)`, and `normal_fan(...)`: owned by fan/polyhedral refinements, not by all varieties.
- `torus()`, `dense_torus()`, and `torus_action()`: owned by toric varieties with algebraic torus codomain.
- `orbit_closure(cone)`: owned by toric varieties with fan cone input; codomain is a toric subvariety plus embedding morphism where exposed.
- `toric_morphism(lattice_map, codomain)`: owned by compatible fan/lattice morphism data; codomain is a toric morphism/scheme morphism.
- `resolve_by_fan_subdivision(...)` or toric `resolve(...)`: owned by toric varieties via fan subdivisions; generic `resolve_singularities()` remains a broader singular-variety surface with characteristic/backend hypotheses.
- `is_smooth()`, `is_complete()`, `is_projective()`, `is_simplicial()`, `is_q_gorenstein()`, `is_fano()`: toric refinements may provide combinatorial decision routes, but the underlying mathematical property owners remain the relevant variety/divisor/singularity categories.
- `class_group()`, `picard_group()`, torus-invariant Weil/Cartier divisor groups, and maps among them: toric refinements of broad divisor/Picard surfaces with combinatorial backends.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- Polytope/polyhedron source-admission cards must admit cones/fans/lattice polytopes before toric constructor specs harden.
- Coble/K3 toric-surface references must state whether the object is a toric variety, fan, polytope, or altered free abelian lattice.
- Backend-routing work should prefer Sage/OSCAR for toric varieties and morphisms, with polymake/Normaliz for fan/cone kernels after audit.
- Lattice/ModulesWithForms implementation work is not a blocker for toric source admission because toric lattices use ordinary finite-rank free `ZZ`-module structure, not symmetric bilinear forms.

## Follow-Up Routing

No new card is needed from this toric source-admission pass.

- Polyhedral constructor details remain in the existing polytope/polyhedron source-admission cards.
- Backend implementation routing remains future work after source specs decide the exact toric object surfaces.
- If downstream implementation needs a public `ToricLattice` type, it should be specced as a finite-rank free `ZZ`-module/dual-pair refinement, not under `Lattices(ZZ)`.

## Acceptance Evidence

- Mathematical convention recorded from Sage toric lattice/fan/toric variety docs, OSCAR toric variety and morphism docs, and local module/lattice ownership specs.
- Sage surfaces surveyed for toric lattices, fans, toric varieties, orbit closures, class groups, and fan-subdivision resolution.
- Backend surfaces surveyed for OSCAR toric varieties/morphisms and polymake/Normaliz polyhedral routing.
- Local dependency on free-module categories and explicit non-dependency on formed lattice implementation recorded.
- Follow-up routing records that no new card is needed because existing polytope/polyhedron and backend-routing cards own specialization.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for toric varieties with lattice categories, routing toric lattices to finite-rank free `ZZ`-module/dual-pair vocabulary and toric varieties to fan-owned normal variety refinements.
