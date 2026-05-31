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
  `my_embedding.is_primitive()`, and `v*w`;
- delegate exact algebra to mature Sage/GAP-style backends;
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
concrete providers, source-grounded definitions, representation splits, or tests that
expose those relations. Engineering-shaped work in this phase is suspicious until it
names the mathematical deficiency it repaired.

## Downstream ordering

The hierarchy implicit in `GOAL.md`: downstream Coble/lattice goals must not be attacked
by ad hoc raw computations.
The first pass is an abstract semantic vocabulary of sets, modules, Hom/End/Aut, modules
with forms, lattices, morphisms, coercions, validation, and backend boundaries.
Do not skip this.
