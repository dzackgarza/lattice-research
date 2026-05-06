---
id: SPEC-HISTORICAL-COXETER-FUNDAMENTAL-DOMAIN-OUTPUT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT]]'
title: Recover Coxeter diagram and fundamental chamber output contracts
status: needs-review
priority: medium
requirement: Vinberg/Coxeter recovery must specify exact output objects for reflection
  groups, Coxeter diagrams, chamber inequalities, and finite-volume evidence.
acceptanceCriteria:
- Simple roots, reflection morphisms, Coxeter matrix or diagram, Gram data, and chamber
  inequalities are separate typed outputs with shared provenance.
- Fundamental chamber claims include verification that the reported inequalities define
  the chamber for the generated reflection group under stated hypotheses.
- Finite-volume or parabolic-subdiagram claims are exact combinatorial or polyhedral
  checks, not diagram eyeballing.
- Outputs are reusable by downstream Coble Coxeter and cusp-classification features.
complexity: 80
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Recover Coxeter diagram and fundamental chamber output contracts

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md`:
  status flag records whether found roots form a finite-volume diagram, while `das`
  is an internal Coxeter-diagram continuation object.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/quad_forms.jl`
  and `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/vinbergs_algo.jl`:
  Gram coefficients, Coxeter coefficients, diagram extension, finite-volume check, and
  sanity checks for roots, acute angles, chamber side, and distance ordering.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/infinite_order_symmetry.jl`:
  graph automorphism work uses root Gram colors, not an unweighted graph alone.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/README.md`
  and `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/vinal.py`:
  CoxIter route, dual-cone/polycone route, finite and ideal vertex extraction, and
  root printing.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/docs/vin-alg-pseudocode-old.txt`:
  fundamental polyhedron and fundamental cone narrative.
- `src.bak/backends/external/vinbergs_algorithm/references/AlVin/mainpage.dox`:
  AlVin outputs root vectors, CoxIter graph files, finite-volume/invariant data, and
  explicit nontermination/nonreflectivity distinction.
- `src.bak/backends/external/vinbergs_algorithm/references/sterk-peters_symmetric-quadratic-forms.md`
- `theory/foundations/reflective-two-elementary-lattices.md`: Coxeter diagram,
  parabolic diagram, Lanner subgraph, fundamental polyhedron, root, reflection, and
  reflection-group definitions; Sterk-Peters example records maximal parabolic
  subdiagrams and dashed-edge finite-volume checks.
- `.agents/memories/theory-graph-monodromy-hodge-methods.md`: Coxeter diagrams with
  labels and edge multiplicities require colored graph automorphism.
- `plans/features/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION.md`
- `plans/features/FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY/specs/SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT.md`

## Contract

The recovered output surface must separate the mathematical objects involved:
simple roots are lattice elements, reflections are automorphisms of the lattice,
the Coxeter diagram records pairwise reflection data, and the chamber is a polyhedral
object or inequality system in the appropriate hyperbolic cone.

Downstream code must be able to ask for parabolic subdiagrams, finite-volume status,
incidence data, or chamber faces without reconstructing the meaning of a raw root list.

## Output Objects

The output of a complete Vinberg chamber computation is not a graph. It is a linked
collection of exact mathematical objects with shared provenance:

- `simple_roots`: ordered lattice elements from the parent lattice `L`;
- `reflections`: the corresponding elements of `L.Aut()`;
- `root_gram_matrix`: the exact matrix `b(r_i, r_j)`;
- `coxeter_matrix`: pairwise Coxeter exponents or infinity/dashed-edge markers derived
  from the root Gram data under the stated sign convention;
- `coxeter_diagram`: a colored, labeled graph whose vertex colors include root norm or
  root type when relevant and whose edge labels distinguish no edge, finite Coxeter
  angle, affine/tangent, and disjoint/skew hyperplanes;
- `chamber_inequalities`: inequalities such as `b(x, r_i) >= 0` or the chosen equivalent
  convention, with the cone component and sign convention recorded;
- `chamber`: a typed hyperbolic/polyhedral chamber object or an exact inequality system
  tied to the parent lattice and cone;
- `faces`: facet objects linked to roots and reflections;
- `vertices`: finite and ideal vertices when a backend computes them, with ideal
  vertices represented as isotropic lines or sublattices, not loose coordinate rows;
- `finite_volume_certificate`: the exact check or backend certificate supporting
  finite volume;
- `parabolic_subdiagrams`: typed subdiagram data with affine type, rank, connected
  components, and inclusion/maximality data;
- `lanner_subdiagrams`: Lanner obstruction data when used by the termination criterion;
- `symmetry_group`: diagram symmetries only after preserving vertex and edge colors,
  root Gram data, and the map back to lattice isometries.

Partial Vinberg searches may return the same shape with `completeness_status =
partial-prefix` or `shell-complete`, but the chamber and finite-volume certificate must
then be absent or explicitly marked unavailable. A partial prefix can be a fixture,
debug artifact, or continuation state; it is not a fundamental domain.

Docstrings for these surfaces must mention the global diagnostic flag for surprise
logging. When enabled, the implementation should warn if a diagram is returned without
a chamber certificate, if finite-volume status is unknown, if graph symmetries are being
computed on colored data rather than an unweighted graph, if a partial prefix is
returned, or if ideal vertices are represented through isotropic subobjects rather than
ordinary finite vertices.

## Verification Contract

A chamber-complete result must verify the following obligations:

- every simple root satisfies the sourced root predicate for `L`;
- every reflection is admitted through `L.Aut()`;
- pairwise root inner products satisfy the simple-root acute-angle convention used by
  the chamber side;
- each chamber inequality is oriented so the control vector lies on the chosen side;
- the root ordering is compatible with the Vinberg distance/shell data supplied by the
  algorithm contract;
- the inequalities define the claimed chamber for the generated reflection group under
  the backend theorem or certificate;
- finite-volume claims are backed by CoxIter, Vinberg's Lanner/parabolic criterion, an
  exact polyhedral check, or a named backend certificate;
- nonreflective or nonterminating outputs are distinguished from "not enough roots were
  computed".

For the Sterk-Peters rank-19 example, fixture extraction should preserve the sourced
root list, distance levels, dashed-edge data, maximal parabolic subdiagram types, the
rank-2 hyperbolic span condition for dashed-line vertices, and the negative-definite
complement check. These are expected fixture obligations, not generic defaults for all
hyperbolic lattices.

## Downstream Reuse

The Coble Coxeter/parabolic-classification feature should consume the typed Coxeter
output directly. It should not parse pictures, free-text labels, or backend output
files. In particular:

- cusp and boundary classifications consume ideal vertices as isotropic line or plane
  subobjects;
- parabolic classification consumes typed affine subdiagrams and inclusion data;
- graph-monodromy or symmetry steps consume colored Coxeter diagrams and the induced
  lattice isometries;
- fixture data records exact source paths, theorem hypotheses, root norms,
  inner-products, and diagram conventions.

## Non-Preservation Boundaries

- Do not store Coxeter data only as a drawn graph or list of labels.
- Do not treat a Gram matrix of roots as the whole chamber object.
- Do not conflate a root enumeration prefix with a verified fundamental domain.
- Do not make Coble-specific parabolic classification depend on unsourced diagram
  conventions.
- Do not compute diagram symmetries from an unweighted graph when vertex/edge colors,
  root norms, or dashed/affine labels carry mathematical data.
- Do not collapse finite vertices, ideal vertices, isotropic lines, and isotropic planes
  into one coordinate-list output.
- Do not treat AlVin or CoxIter graph files as public API; they are backend artifacts to
  parse into typed objects if the bridge is admitted.
- Do not use a finite-volume status flag without retaining the certificate source and
  hypotheses that make the flag meaningful.

## Acceptance Criteria

- [x] Simple roots, reflections, diagrams, and chambers are distinct linked outputs.
- [x] Finite-volume and parabolic claims have exact checks.
- [x] The output can feed downstream Coble Coxeter/parabolic feature specs.
- [x] Known reference examples can be represented as fixtures with sourced expected
  structure.
