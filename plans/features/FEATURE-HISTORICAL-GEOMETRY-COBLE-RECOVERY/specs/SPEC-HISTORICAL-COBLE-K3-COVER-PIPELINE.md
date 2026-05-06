---
id: SPEC-HISTORICAL-COBLE-K3-COVER-PIPELINE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE]]'
- '[[SPEC-HISTORICAL-LATTICE-CONSTRUCTORS-INVARIANTS-AND-COMPARISONS]]'
title: Recover Coble surface and K3 double-cover construction pipeline
status: unstarted
priority: high
requirement: Historical Coble and K3 vocabulary must be recovered as a construction
  pipeline that derives Picard and pullback lattice data instead of naming expected
  lattice outputs.
acceptanceCriteria:
- A Coble surface is constructed from a rational sextic and the blowup at its nodes,
  with exceptional divisors and Picard generators recorded.
- The K3 double cover is constructed from a branch divisor or sextic with ramification
  data and canonical-class checks.
- Picard pullback along the cover produces a lattice through divisor pullback and
  intersection pairing, not by postulating the target presentation.
- Any standard presentation appears only as a comparison target after the geometric
  lattice has been constructed.
complexity: 90
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover Coble surface and K3 double-cover construction pipeline

## Source Provenance

- `src.bak/varieties/varieties.py`: `CobleSurface`, `K3Surface`, `BranchedCover`,
  `EnriquesSurface`, `PicardGroup`, `Divisor`, and `Blowup` surfaces.
- `GOAL.md`: staged Coble construction obligations.
- `theory/foundations/coble-task-background.md`: current source-backed Coble
  construction argument and tracker routing.

## Contract

The recovered Coble API must express the actual construction chain. Start with a
rational sextic curve, construct its nodes, blow up the plane at those nodes, construct
the Coble surface, compute its Picard group from the blowup, construct the relevant
double cover and ramification data, compute the pullback of Picard classes, and only
then compare the resulting lattice to a standard presentation.

The K3 claim is a geometric invariant computation: the canonical class, irregularity,
geometric genus, singularity resolution context, and cover formulas must be expressed
through geometry nouns and maps. Lattice data are downstream outputs of this pipeline.

This proof pipeline is separate from the eventual standard lattice library. During this
derivation, the code may compare the constructed lattice to a standard presentation
such as `I_{1,10}(2)` or an isometric decomposition only as a target of an explicit
isometry verification. After the proof is accepted, downstream Coble research should
use the canonical sourced `T_Co` object rather than constructing an isometric
presentation or supplying a raw Gram matrix.

## Non-Preservation Boundaries

- Do not use `coble_lattice()` as a black box returning an expected lattice without
  the construction evidence.
- Do not treat the Picard lattice statement as input data for the Coble construction.
- Do not call the cover "K3" unless the invariants and hypotheses that prove it are
  recorded or computed.
- Do not conflate the Coble-side Picard lattice with its K3 pullback or orthogonal
  complement.

## Acceptance Criteria

- [ ] The surface, blowup, cover, Picard, pullback, and lattice objects are linked by
  explicit maps.
- [ ] The K3 double-cover claim has invariant checks or sourced formulas.
- [ ] Standard lattice presentations appear as verification targets, not premises.
- [ ] The accepted result defines the provenance needed for downstream code to use a
  canonical `T_Co` instead of ad hoc isometric presentations.
- [ ] The pipeline can feed downstream Coble moduli and lattice-complement features.
