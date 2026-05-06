---
id: SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE]]'
title: Recover kernels, images, cokernels, and discriminant descent through morphisms
status: needs-review
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
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  morphism-owned verbs, Hom-space construction, and rejection of morphism `perp` or
  containment shortcuts.
- `.agents/memories/bilinear-form-category-semantics.md`: coefficient-module
  cokernel semantics and the discriminant descent diagram using `L -> L^#`.

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

## Recovered Hom-Space Surface

Every formed-module morphism is an element of a declared Hom parent:

- `M.Hom(N)` is the parent of morphisms from `M` to `N`.
- `Hom.from_images(images)` constructs the morphism determined by the fixed domain
  generators and the listed codomain elements.
- `Hom.from_dict({g_i: h_i})` constructs a morphism from named generator images.
- `Hom.from_callable(f)` is admitted only as a thin constructor that evaluates `f` on
  the domain generators and delegates to `from_dict`.
- `Hom.from_matrix(A)` constructs a candidate morphism from a matrix relative to the
  selected presentations, then validates it through Hom containment.

The Hom parent owns domain/codomain checks, selected-generator conventions, module
linearity, and form preservation. Matrix equations such as `A^T Q_N A = Q_M` are
localized implementation checks inside Hom containment or Aut containment; they are not
public substitutes for the morphism object.

The old `BilinearModuleHomSpace.__contains__` is recoverable only as the containment
site. It must not be copied as a broad `isinstance`/duck-type pattern. Candidate inputs
must be routed through explicit constructors and real category membership.

## Recovered Morphism Element Surface

A formed-module morphism element owns:

- `domain()` and `codomain()`;
- `__call__(x)` for `x` in the domain, returning a codomain element;
- `images()` as the tuple of images of the domain generators;
- `to_matrix()` as presentation readback after the morphism exists;
- additive operations in the Hom object when the Hom parent has additive module
  structure;
- `inverse()` only when the morphism is an isomorphism, returning an element of the
  reverse Hom parent.

`is_isometry()` is not a freestanding matrix predicate. In a formed Hom parent whose
containment already enforces form preservation, an isomorphism is an isometry. In an
Aut parent, membership is the isometry check.

## Recovered Kernel, Image, And Cokernel Surface

The returned objects must be actual category objects:

- `f.kernel()` is a subobject of `domain(f)` with the restricted form.
- `f.image()` is a subobject of `codomain(f)` with inclusion into the codomain and the
  restricted form.
- `f.cokernel()` is the quotient `codomain(f) / image(f)` with projection morphism,
  lift data where mathematically available, and descended form data when the descent
  hypotheses hold.
- `f.lift(y)` is a partial inverse along the projection/image data, not a raw Sage lift
  escape hatch.

The cokernel descent gate is:

- construct the underlying finitely generated PID-module cokernel;
- compute the coefficient-module quotient needed by the form;
- verify that cross-terms from the image vanish in the quotient codomain;
- construct the descended bilinear or quadratic form on the cokernel;
- promote the result into the richest correct category, such as `Free()`, `Torsion()`,
  `Integral()`, `Rational()`, `NonDegenerate()`, or `DiscriminantGroups()`.

Promotion is therefore a consequence of the constructed object and hypotheses. It must
not be implemented as "if the codomain is a `DualLattice` class, return a
`DiscriminantGroup`".

## Discriminant Descent Contract

For a lattice `L`, discriminant descent is the special case of the generic cokernel
machine applied to the metric inclusion:

```text
i: L -> L^#
A_L := coker(i)
```

The descended bilinear form has codomain `K/R`, and any descended quadratic refinement
has codomain `K/2R`. The resulting object must carry:

- the source lattice `L`;
- the metric dual `L^#`;
- the inclusion `i`;
- the projection `L^# -> A_L`;
- the quotient-valued form data.

The map `L^# -> Hom_R(L,R)` induced by `x |-> beta(x, -)` is separate transport data.
It is not what makes `L^#` a dual object, and it must not replace the metric-cokernel
definition of `A_L`.

## Recovered Predicate Surface

Morphism predicates are derived from the returned objects:

- `f.is_injective()` means `f.kernel()` is the zero object in the domain category.
- `f.is_surjective()` means `f.cokernel()` is the zero object in the codomain category.
- `f.is_bijective()` is injective and surjective.
- `f.is_isomorphism()` is categorical isomorphism, and in a formed Hom parent it is the
  relevant isometry condition when form preservation is already contained.
- `f.is_identity()` requires equal domain/codomain and equality on generators.
- `f.is_primitive()` for an inclusion means the cokernel is torsion-free; this belongs
  to the morphism/inclusion surface, not to a coordinate helper.

## Non-Preservation Boundaries

- Do not preserve `pass`-only homspace subclasses as if the surface were implemented.
- Do not define cokernel as an orthogonal complement.
- Do not promote a quotient to `DiscriminantGroup` by recognizing a particular class
  pair without constructing the actual dual inclusion and quotient map.
- Do not make morphisms own operations such as `perp` or containment; those belong to
  subobjects, Hom spaces, or formed-module parents as appropriate.

## Acceptance Criteria

- [x] Matrix and image constructors route through Hom-space parents.
- [x] Kernels, images, cokernels, and lifts return typed mathematical objects.
- [x] Discriminant descent is specified as a cokernel with descended form data.
- [x] Primitive embedding checks use the morphism/cokernel contract and produce
  reviewable evidence.
