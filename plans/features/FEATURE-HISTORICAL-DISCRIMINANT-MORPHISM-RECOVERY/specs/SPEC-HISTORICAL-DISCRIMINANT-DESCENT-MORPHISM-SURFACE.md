---
id: SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE]]'
title: Recover kernels, images, cokernels, and discriminant descent through morphisms
status: unstarted
priority: high
requirement: Historical morphism operations must be recovered through category-correct
  Hom objects, with cokernels returning the mathematically correct formed-module quotient.
acceptanceCriteria:
- Morphisms are elements of Hom spaces and form preservation is Hom containment.
- Kernel, image, cokernel, lift, injective, surjective, bijective, identity, and primitive
  predicates have mathematically typed return objects.
- The discriminant form arises from the cokernel of the dual inclusion with descended
  coefficient data.
- Lattice promotion from a morphism result happens only when the returned object is
  free, integral, and nondegenerate under explicit hypotheses.
complexity: 80
tags:
- FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY
---
# Recover kernels, images, cokernels, and discriminant descent through morphisms

## Source Provenance

- `src.bak/lattices/morphisms/lattice.py`: image, kernel, cokernel, lift, primitive,
  injective, and promotion hooks.
- `src.bak/lattices/morphisms/discriminant.py`: discriminant-group morphism kernel,
  image, cokernel, injective, surjective, bijective, isomorphism, and identity
  predicates.
- `src.bak/lattices/morphisms/homspaces.py`: Hom-space construction stubs and evidence
  that the old layer was incomplete.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: current Hom,
  cokernel, and discriminant descent rules.

## Contract

Recovered morphism work must start from Hom objects. A matrix or generator-image table
constructs a candidate morphism only through the parent Hom space, where domain,
codomain, generator conventions, and form-preservation checks are centralized.

Kernel, image, and cokernel return actual category objects with the appropriate
descended form data. For discriminant descent, the quotient is not merely an
underlying-module quotient: the form and coefficient codomain must descend through the
specified morphism under the hypotheses recorded in the with-form category spec.

Primitive embedding and quotient tests are properties of the morphism and its cokernel.
They must not be restated as standalone helper assertions over raw matrices.

## Non-Preservation Boundaries

- Do not preserve `pass`-only homspace subclasses as if the surface were implemented.
- Do not define cokernel as an orthogonal complement.
- Do not promote a quotient to `DiscriminantGroup` by recognizing a particular class
  pair without constructing the actual dual inclusion and quotient map.
- Do not make morphisms own operations such as `perp` or containment; those belong to
  subobjects, Hom spaces, or formed-module parents as appropriate.

## Acceptance Criteria

- [ ] Matrix and image constructors route through Hom-space parents.
- [ ] Kernels, images, cokernels, and lifts return typed mathematical objects.
- [ ] Discriminant descent is specified as a cokernel with descended form data.
- [ ] Primitive embedding checks use the morphism/cokernel contract and produce
  reviewable evidence.
