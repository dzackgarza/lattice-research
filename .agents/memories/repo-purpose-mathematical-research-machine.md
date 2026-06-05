---
title: Repo Purpose — Mathematical Research Machine
status: active
---
# The repo exists to advance mathematical research

This is not fundamentally an engineering project.
The engineering exists only to build a reliable mathematical language in which research
claims can be stated, checked, transferred, and written.

The purpose is to make future lattice/Coble work read like mathematics:

- construct named lattices and related objects;
- map generators and define symbolic morphisms;
- use standard vocabulary such as `f.cokernel()`, `L.discriminant_group()`,
  `my_embedding.is_primitive()`, and `v*w` only when the operation has recorded exact
  support or an explicit deferred-algorithm status;
- delegate exact algebra to mature Sage/GAP-style backends and name the backend or Sage
  surface that makes an operation feasible;
- produce code whose narrative can be transferred directly into a proof, computation
  note, or paper.

The repo is not trying to maximize completed cards, green checkboxes, ledgers, reports,
or process artifacts.

Every session must ask:

> What mathematical object, operation, claim, interface, or proof path is now closer
> because of this work?

If the answer is only "a card is clearer," "a ledger is updated," "a plan is more
detailed," or "handoff context improved," presume no mathematical progress has occurred.

During category-spec work, most legitimate progress should look mathematical on its
face: category edges, method owners, constructors, morphisms, abstract obligations,
concrete implementations, source-grounded definitions, feasibility classifications,
representation splits, or tests that expose those relations. Engineering-shaped work in
this phase is suspicious until it names the mathematical deficiency it repaired.

Engineering is acceptable only as minimal enabling infrastructure for that research
language.
Prefer mature existing mechanisms over local invention: Sage should own Sage category
construction, Python should own Python abstract-method semantics, and exact algebra
should be delegated to mature mathematical backends whenever possible.
When this repo must bridge those systems, the bridge should be narrow, owned, and
quarantined so ordinary mathematical specs remain readable without expertise in Sage or
Python internals.

The alignment check for a proposed implementation is:

- Does this make a mathematical object, operation, interface, or proof path available?
- Does it reuse the simplest existing mechanism that already solves the non-research
  problem?
- Is any unavoidable machinery confined to the smallest interop layer the repo owns?
- Does it avoid creating a parallel local system that future research code must trust?

For `category_specs`, the central object is the mathematical specification, not runtime
enforcement. But the current phase is not abstract API design: it is
inventory-to-spec translation. A spec-level operation is admitted only when it is
Sage-backed, backend-backed by a named exact package, locally implementable as a
bounded thin extension over available exact ingredients, or explicitly marked as a
deferred research algorithm. Refinement declares that an implementation is regarded as
an object of a category; it does not prove that implementation satisfies the category.
Current Sage objects may be partial relative to project specs, but missing support must
remain visible as a feasibility classification rather than being hidden behind a
mathematically nameable method.

Do not turn this repo into a mechanism that hides or preempts the gap: no generated
failure bodies, refinement-time satisfaction checks, cache priming, source-shape tests,
or QC-passing substitutes for category contracts.

## Downstream ordering

The hierarchy implicit in `GOAL.md`: downstream Coble/lattice goals must not be attacked
by ad hoc raw computations.
The first pass is a Sage-grounded, feasibility-classified semantic vocabulary of sets,
modules, Hom/End/Aut, modules with forms, lattices, morphisms, coercions, validation,
and backend boundaries. Hom/End/Aut vocabulary may name mathematical objects without
promising generic computation; for example, `is_isometry(f)` is certification, while a
generic `Aut(L)` computation is a global algorithmic claim requiring separate
ownership.
Do not skip this.
