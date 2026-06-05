---
title: Current Goal Handoff
---
# Handoff

## Current Phase

Category-spec vocabulary. The live goal is to define the mathematical language needed
by the later Coble/K3 lattice program: typed modules, formed modules, lattices,
Hom/End/Aut objects, morphisms, discriminant forms, metric duals, embeddings,
orthogonal complements, subgroup objects, and witness data grounded in Sage/source
evidence.

Downstream Coble subgroup, cusp, and orbit computations are not the next action unless
they expose a missing foundational definition. Existing Coble theory notes may be used
as research needs; they are not the active work item.

## Next Mathematical Obligation

Classify the remaining lattice/module Hom and morphism operations in
`SPEC-MAPPING-LATTICES` from the Sage method cluster:

```text
FreeModuleHomspace,
FreeModuleMorphism,
MatrixMorphism,
FGP_Homset,
FGP_Morphism,
generic Homset/End constructors.
```

The statement to settle is:

```text
For objects in the correct category C satisfying hypotheses H,
the Sage method m realizes a morphism operation O,
with codomain or return object Y,
using witness data W.
```

The research need is that later Coble code must express maps such as
`f^*Pic(S) -> H^2(X,Z)`, inclusions `L -> L^#`, embeddings of lattices with forms,
orthogonal projections/complements, discriminant descent, and certified isometries as
typed morphisms rather than raw matrices.

## Source Evidence To Read

- `category_specs/lattices/docs/SAGE_INVENTORY.md`, especially the Hom/morphism blocks
  for `FreeModuleHomspace`, `FreeModuleMorphism`, `MatrixMorphism`,
  `FGP_Homset`, and `FGP_Morphism`.
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`,
  especially `Lattices Homset Mirroring Audit`.
- Sage installed source named by those rows:
  `sage/modules/free_module_homspace.py`,
  `sage/modules/free_module_morphism.py`,
  `sage/modules/matrix_morphism.py`,
  `sage/modules/fg_pid/fgp_morphism.py`,
  `sage/modules/fg_pid/fgp_module.py`,
  `sage/categories/homset.py`,
  and `sage/categories/homsets.py`.

## Success Condition For The Next Unit

`SPEC-MAPPING-LATTICES` states or corrects the theorem-shaped rows for:

- `Hom_R(M,N)` construction from generator images, matrices, or callable-on-generators
  data under finite-free or finitely-presented hypotheses;
- morphism evaluation, composition, zero morphisms, additive Hom structure, and scalar
  Hom structure at their correct category owners;
- matrix representation only after finite free presentations or chosen bases;
- kernel, image, inverse image, cokernel, and lift/preimage representative at the
  module or formed-module tier where the operation is actually defined;
- `End(X)=Hom(X,X)` and `Aut_C(X)=End_C(X)^\times` without implying generators or
  presentations unless a stronger group refinement supplies witnesses;
- lattice-specific refinements only for form-preserving morphisms, isometry
  certification, discriminant action, and the subgroup objects of `O(L)`.

If a Sage method is display, call-protocol, cache, comparison, orientation, or backend
residue, record that as residue only after the mathematical operation is named or shown
absent.

## Non-Goals

- Do not continue Coble primitive-isotropic, Heegner-line, or arithmetic-subgroup orbit
  proofs as the next action.
- Do not treat finite discriminant-form orbit computations as a substitute for
  foundational Hom/morphism vocabulary.
- Do not answer with routes, phases, plans, or status summaries before naming the
  mathematical operation, category, hypotheses, return object, and source evidence.
- Do not use this handoff as a changelog. Git history and the mapping spec carry past
  work.
