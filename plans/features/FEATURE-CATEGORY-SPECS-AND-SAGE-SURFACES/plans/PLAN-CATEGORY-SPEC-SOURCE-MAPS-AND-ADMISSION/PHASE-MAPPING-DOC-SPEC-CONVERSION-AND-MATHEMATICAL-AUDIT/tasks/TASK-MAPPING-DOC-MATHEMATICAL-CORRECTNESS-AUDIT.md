---
id: TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[SPEC-MAPPING-ALGEBRAS]]'
- '[[SPEC-MAPPING-CAT]]'
- '[[SPEC-MAPPING-FORMS]]'
- '[[SPEC-MAPPING-HOMSETS]]'
- '[[SPEC-MAPPING-LATTICES]]'
- '[[SPEC-MAPPING-MODULES]]'
- '[[SPEC-MAPPING-POSETS]]'
- '[[SPEC-MAPPING-RINGS]]'
- '[[SPEC-MAPPING-SETS]]'
- '[[SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS]]'
- '[[SPEC-MAPPING-TOPOLOGICAL-SPACES]]'
blocks: []
title: Audit mapping specs for mathematical coherence and well-typed method signatures
status: needs-review
priority: critical
description: Review every tracked mapping spec for mathematically meaningful owners,
  coherent method signatures, inheritance through subcategories, and rejection of
  nonmathematical targets or software-shaped placeholders.
successCriteria:
- Every admitted method row states caller category, complete input data, hypotheses,
  codomain or return object, and source evidence.
- Methods are mapped to the highest category where they are mathematically well-defined.
- Subcategory inheritance is respected; no row treats subcategories as losing methods
  defined on their supercategories.
- Nonmathematical targets, implementation containers, raw option bags, and duck-typed
  helper surfaces are rejected or routed to interop-only status.
- Ambiguities become decision cards before implementation proceeds.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit mapping specs for mathematical coherence and well-typed method signatures

## Summary

Audit the tracked mapping specs as mathematical documents. A row passes only if its
method or constructor is well-defined in ordinary mathematical language and its public
signature is well typed.

## Execution Start

This audit is unblocked by the mapping-completeness pass. The audit must inspect
each tracked mapping spec as a mathematical document, not as a Sage compatibility
check: method owners are caller categories, subcategories inherit supercategory
methods, codomains are return data rather than owners, and nonmathematical targets
are rejected or routed to interop-only status.

## Review Handoff

The concrete mathematical-correctness findings from the delegated audit pass have
been applied to the converted mapping specs and pushed:

- `c1a520d`: corrected ordered-real signature ownership.
- `c84e178`: narrowed lattice-dual and discriminant-group ownership to finite-free
  nondegenerate integral lattice data.
- `fca9feb`: corrected algebra derivations as `R`-linear Leibniz endomorphisms,
  not algebra endomorphisms.
- `eb74c8a`: placed commutative localization above Sage's current integral-domain
  implementation and kept ring/field `free_module` ownership on the caller.
- `ad4fd04`: restricted homset identity to endomorphism objects and made aut-from-end
  construction private glue.
- `ec5806c`: removed cache/export plumbing from set surfaces, restricted finite
  subset lattices, and strengthened metric codomain and axioms.
- `1d737a7`: made tensor coordinate constructors and structure constants
  frame-relative, preserved symmetric/alternating tensor submodules, and changed
  tensor duality to finite-free canonical isomorphism.
- `6553133`: split algebra constructor owners by magmatic/associative/unital laws
  and separated finite-dimensional field algorithms from finite-rank-over-ring
  wiring.
- `c31429a`: split finite-poset Hasse-digraph and relation-digraph constructors and
  removed inherited finite-set enumeration/cardinality from poset ownership.
- `dd507f2`: admitted typed simultaneous tensor contractions without exposing Sage
  positional overloads.

This task is ready for human/spec review. It is not accepted or closed.
