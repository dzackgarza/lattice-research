---
id: SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
title: Recover geometry nouns, morphisms, divisors, and Picard group surface
status: needs-review
priority: medium
requirement: Historical geometry nouns must be recovered as source-admitted category
  interfaces with backend ownership for schemes, varieties, morphisms, divisors, and
  Picard groups.
acceptanceCriteria:
- Variety, subvariety, morphism, curve, surface, divisor, line bundle, Picard group,
  blowup, and cover nouns have explicit owners and source grounding.
- Divisor pullback, pushforward, intersection, linear equivalence, Cartier/Q-Cartier/Weil
  predicates, and Picard group intersection matrices have backend routes.
- Blowups record centers, exceptional divisors, and induced Picard-group changes as
  maps and generators.
- Geometry specs do not assume Coble-specific outputs before the construction supplies
  them.
complexity: 80
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover geometry nouns, morphisms, divisors, and Picard group surface

## Source Provenance

- `src.bak/varieties/varieties.py`: `Variety`, `Subvariety`, `VarietyMorphism`,
  `Curve`, `Surface`, `Divisor`, `LineBundle`, `PicardGroup`, `Blowup`, and
  `BranchedCover` abstract surfaces.
- `.agents/memories/theory-backend-routing.md` and
  `.agents/memories/theory/backends/software-capability-map.md`: Macaulay2, Singular,
  Sage, Oscar/Hecke, and commutative-algebra backend ownership for geometry methods.
- `.agents/memories/theory/backends/abstract-to-external-mapping.md`: historical method
  to backend route table for varieties, curves, surfaces, divisors, Picard groups,
  covers, sheaves, and families.
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-SCHEMES-CATEGORY.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-VARIETIES-CATEGORY.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY.md`

## Contract

The recovered geometry layer must provide nouns and morphisms that make algebraic
geometry computations readable as geometry. Pullbacks, pushforwards, exceptional
divisors, Picard groups, intersection forms, canonical classes, Hilbert polynomials,
Hodge numbers, and singularity operations are methods on the relevant objects or maps,
with backend ownership recorded before implementation.

Blowups must expose the center, exceptional divisor data, induced divisor/Picard maps,
and any changes in intersection pairing as typed constructions. These are prerequisites
for later Coble work but are not themselves Coble claims.

## Owner Surface

The historical abstract classes are source material, not public API authority. The
recovered owners are mathematical category refinements:

| Noun or method family | Owner | Backend route | Notes |
| --- | --- | --- | --- |
| `Scheme`, `Spec(R)`, `Proj(S)`, `Hom(X,Y)`, points as `Spec(K)->X` | `Schemes()` and affine/projective/presented refinements | Sage schemes, Macaulay2 `Spec`/`Proj`, OSCAR schemes | A scheme is not a raw ideal or zero locus; presentations are constructors. |
| `Variety` | `Varieties(k)` as integral separated finite-type schemes over `k` | Sage presented schemes, Macaulay2/Oscar affine and projective varieties after hypothesis checks | Reducible or nonreduced algebraic sets stay under named scheme/presented refinements. |
| `Subvariety`, `singular_locus`, `smooth_locus`, `defining_ideal`, `equations` | embedded/presented scheme or variety refinements | Sage algebraic subschemes, Singular, Macaulay2 | `defining_ideal()` and equations are presentation data, not methods on all varieties. |
| `VarietyMorphism`, fibers, pullback/pushforward hooks | scheme/variety Hom surfaces | Sage scheme morphisms, backend-specific adapters | Points and rational points should route through Hom surfaces, not raw coordinate lists. |
| `Curve`, `Surface` | dimension-one and dimension-two variety refinements | Sage/Macaulay2/OSCAR under presentation hypotheses | They inherit broad invariants and add dimension-specific formulas or refinements. |
| `Divisor` | divisor objects over appropriate normal/smooth/presented scheme or variety refinements | Macaulay2 Divisor, Sage divisor surfaces where available, Singular for curve divisor computations | Weil, Cartier, and `Q`-Cartier predicates are separate surfaces. |
| `LineBundle`, `CoherentSheaf`, cohomology | sheaf category over a scheme/variety | Macaulay2 `HH`, `chi`, tangent/cotangent sheaves; Sage where available | Divisor-to-sheaf maps must be explicit. |
| `PicardGroup` | Picard group object of a scheme/variety | Sage Picard surfaces where available; Macaulay2/Oscar candidates | Picard group is not the Picard lattice. |
| Picard lattice/intersection form | smooth proper/projective surface refinements with admitted intersection pairing | Oscar/Hecke integer-lattice route after divisor basis and pairing are known | The divisor generators and maps producing the lattice must remain recoverable. |
| `blowup(center)` | scheme/noetherian or presented-scheme construction with surface-preserving refinements | Macaulay2 Schubert2 `blowup(i)`, Sage/Singular candidates | The blowup object owns center, exceptional divisor, and induced Picard maps. |
| branch/ramification cover data | finite morphism/branched-cover refinement | Sage weighted/projective constructors, Macaulay2/Singular support as audited | Cover claims must include branch divisor, ramification divisor, and canonical formulas. |

## Invariant Ownership

Global invariants such as arithmetic genus, geometric genus, Hodge numbers, Kodaira
dimension, holomorphic Euler characteristic, Hilbert polynomial, and canonical class
must be owned by the broadest source-backed scheme or variety refinement satisfying the
definition's hypotheses. Curves and surfaces may inherit these methods, add
dimension-specific formulas, and supply backend routes, but they do not own the names
merely because low-dimensional software exposes them prominently.

In particular, arithmetic genus and geometric genus are not curve-exclusive. Any
surface or higher-dimensional variety card that exposes these methods must state the
exact convention and hypotheses. Method docstrings should use the global category
diagnostic flag when a low-dimensional compatibility spelling could make users think a
curve-only formula or surface-only formula is being applied outside its hypothesis.

## Backend Routes

Implementation cards consuming this spec must record one of the software-wiring
statuses from `research-software-wiring`: `preferred-backend`, `bridge-needed`,
`candidate-backend`, `true-gap`, or `out-of-scope`.

Initial routing:

- Singular owns curve singularities, normalization, Brill-Noether/Riemann-Roch spaces,
  and polynomial solving for nodes or singular loci.
- Macaulay2 owns blowups, exceptional divisors, canonical divisors/bundles, Hilbert
  polynomials, tangent/cotangent sheaves, sheaf cohomology, and much divisor/intersection
  theory.
- Sage owns scheme orchestration, scheme morphisms, presented schemes, ambient spaces,
  and bridges into Singular or other exact backends.
- Oscar/Hecke owns integer-lattice outputs after geometry has produced the Picard
  group, divisor basis, and intersection pairing.
- No local bespoke geometry algorithm is admitted by this recovery card.

## Coble Boundary

Coble/K3 cards may depend on this geometry noun surface, but they must not shortcut it.
A later Coble construction must exhibit the rational sextic, nodes, blowup morphism,
exceptional divisors, Picard generators, cover map, branch and ramification data, and
Picard pullback before comparing a resulting lattice to a standard presentation.

## Non-Preservation Boundaries

- Do not preserve abstract methods as if they define accepted behavior without source
  and backend admission.
- Do not express Picard groups only as raw lattices; the divisor generators and maps
  that produce the lattice must be recoverable.
- Do not collapse Weil, Cartier, and `Q`-Cartier predicates.
- Do not assume a single backend owns all geometry operations.
- Do not move broad invariants such as genus, Hodge numbers, Kodaira dimension, Euler
  characteristics, or canonical data down to curves or surfaces when the source
  hypotheses are broader.
- Do not implement Picard lattices as raw matrices detached from divisor generators,
  intersection pairings, and the map from the surface to the Picard object.

## Acceptance Criteria

- [x] Each recovered noun has owner, definition source, and backend route.
- [x] Divisor and Picard operations are maps and objects, not detached matrices.
- [x] Blowup-induced Picard behavior is specified in a reusable form.
- [x] Coble-specific specs can depend on this surface without restating it.
