---
id: SPEC-HISTORICAL-LATTICE-CONSTRUCTORS-INVARIANTS-AND-COMPARISONS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]'
title: Recover lattice constructors, invariants, and comparison predicates
status: unstarted
priority: high
requirement: Standard constructors, invariants, and comparison predicates from historical
  lattice code must be recovered with source-grounded mathematical owners and theorem
  hypotheses.
acceptanceCriteria:
- Named standard-lattice constructors are admitted through the approved constructor
  layer and remain available for later research reuse.
- Coble-specific derived lattice constructors are not used as evidence in the feature
  that proves the Coble lattice presentation.
- Rank, determinant, signature, scale, evenness, genus, local genus, rational isometry,
  and integral isometry are methods on the appropriate lattice noun.
- Nikulin-style invariants are lattice invariants with explicit domain hypotheses
  and warnings or rejection outside those hypotheses.
- Comparison predicates either return exact booleans with sourced criteria or return
  witness-bearing morphisms when the claim is existential.
complexity: 75
tags:
- FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY
---
# Recover lattice constructors, invariants, and comparison predicates

## Source Provenance

- `src.bak/lattices/core/integral.py`: `Z`, `U`, `A`, `D`, `E`, `I`, `II`,
  `from_string`, `scale`, `is_even`, `genus`, `local_genus_symbol`,
  `is_rationally_isometric_to`, `is_locally_isometric_to`,
  `is_in_same_genus_as`, `is_isometric_to`, and `nikulin_invariants`.
- `src.bak/lattices/core/rational.py`: rational Gram construction, integral
  promotion, signature, and negative root Gram construction.
- `theory/backends/software-capability-map.md` and IWE `theory-backend-routing`:
  backend ownership for isometry, genus, local invariants, and exact lattice kernels.

## Contract

The constructor surface must recover common lattice families and operations only after
the current constructor admission layer says where they live. Examples include rank-one
lattices, hyperbolic planes, root lattices, odd and even unimodular lattices, K3
lattices, Mathieu-related lattices where source-grounded, twists, direct sums, and
parseable expression syntax if that syntax is approved as public.

The invariant surface must be method-owned by the lattice noun. Immediate invariants
such as rank, determinant, signature, scale, and evenness are computed directly from
the presentation. Genus, local equivalence, rational equivalence, and integral isometry
must route to mature exact backends or theorem-backed classification branches.

Nikulin-style data such as `(r, a, delta)` are invariants of the lattice under explicit
hypotheses. They must not be presented as discriminant-group-local facts and must not
be used outside their theorem-backed domain as if classification still applies.

## Standard Library Versus Derived Research Objects

Standard lattice constructors are a desired library surface. They let later research
use canonical sourced objects instead of constructing ad hoc isometric presentations
such as `I_{1,10}(2)`, `\langle -2 \rangle \oplus U(2) \oplus E_8(2)`, or a
handwritten Gram matrix when the intended object is already canonical.

Derived project objects are separate. The feature that proves a Coble lattice is
isometric to a standard presentation must construct the object geometrically, then
verify the isometry. It may use standard constructors as comparison targets only after
the constructed lattice exists. Once accepted, a canonical sourced `T_Co` surface is
desirable for downstream research so later agents do not re-invent equivalent
presentations.

## Non-Preservation Boundaries

- Do not preserve `coble_picard` or `coble_transcendental` as proof shortcuts that
  bypass the Coble construction.
- Do not present a self-computed invariant match as an isometry without the theorem,
  hypotheses, or witness required for that branch.
- Do not hide backend failure by falling back to weaker sampled or bounded checks.
- Do not duplicate simple Sage or Oscar constructors behind trivial helper aliases
  unless the alias is the approved project vocabulary.

## Acceptance Criteria

- [ ] Every recovered standard constructor has an owner category and source grounding.
- [ ] Derived project constructors such as a future canonical `T_Co` record the proof
  artifact or decision that authorizes their downstream use.
- [ ] Every recovered invariant records whether it is immediate, theorem-backed, or
  backend-computed.
- [ ] Integral isometry and classification predicates state the exact branch used and
  the evidence needed to accept the result.
- [ ] Coble derivation code is forced to construct the geometric input before invoking
  lattice comparisons.
- [ ] Downstream post-derivation Coble research is directed to use the canonical
  sourced `T_Co` rather than ad hoc isometric presentations or raw Gram matrices.
