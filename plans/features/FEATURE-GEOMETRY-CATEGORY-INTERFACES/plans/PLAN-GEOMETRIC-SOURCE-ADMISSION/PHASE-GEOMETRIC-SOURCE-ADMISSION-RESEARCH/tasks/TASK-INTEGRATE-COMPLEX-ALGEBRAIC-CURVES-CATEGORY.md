---
id: TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn: []
title: Research category integration for complex algebraic curves
status: needs-review
priority: high
description: Research and prepare the category-spec integration path for complex algebraic
  curves.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this
  category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors,
  Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation
  cards needed to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for complex algebraic curves

## Summary

Research and prepare the category-spec integration path for complex algebraic curves.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating complex algebraic curves.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Research Result

Status: needs review. Complex algebraic curves are source-grounded as dimension-one complex varieties, with smooth/proper/projective/Riemann-surface surfaces routed to stricter refinements. This card does not authorize implementation.

## Mathematical Definition

Source evidence:

- Stacks Project, Curves, Definition 33.43.1, https://stacks.math.columbia.edu/tag/0A23: a curve over a field `k` is a variety of dimension `1` over `k`.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` records `Varieties(k)` as integral separated finite-type schemes over `k`.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` records complex varieties as varieties over the selected complex base field, keeping analytic and numerical-complex surfaces as bridges/backends.

Project vocabulary:

- `ComplexAlgebraicCurves()` should mean `ComplexVarieties().Dimension(1)` or the repo's equivalent dimension-one refinement.
- `SmoothProjectiveComplexCurves()` should be the owner for compact Riemann-surface and Jacobian-style surfaces.
- `PlaneCurves(CC)`, `ProjectivePlaneCurves(CC)`, `AffineCurves(CC)`, `HyperellipticCurves(CC)`, and `RationalSexticCurves(CC)` are presented/refined curve categories, not replacements for generic curves.
- Singular or reducible plane algebraic sets should remain presented scheme/algebraic-set refinements unless the integral dimension-one variety hypotheses are established.

Boundary decisions:

- A complex algebraic curve is not merely a polynomial equation in two variables; that is a presentation of an affine or projective plane curve.
- `RiemannSurface` surfaces are analytic bridges associated to suitable complex algebraic curves, not the base algebraic curve category.
- `genus()` must distinguish geometric genus, arithmetic genus, and possibly topological genus for the associated compact Riemann surface. Do not collapse these names.
- Normalization returns a normalized curve with a normalization morphism; it is not just a simplified equation or a raw function field.

## Sage Surface Survey

Source evidence:

- Sage curves overview, https://doc.sagemath.org/html/en/reference/curves/index.html, says Sage supports curves in affine and projective ambient spaces, curves over `CC` as Riemann surfaces, and Jacobians of projective curves.
- Sage base curve documentation, https://sagemath.gitlab.io/documentation/html/en/reference/curves/sage/schemes/curves/curve.html, exposes curve surfaces including `genus()` and documents that one genus convention is the genus of the normalization of the projective closure over the algebraic closure of the base field.
- Sage Riemann surface documentation, https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html, provides a `RiemannSurface` model for plane algebraic curves and period/Riemann-matrix computations.
- Sage curve index lists affine curves, projective curves, plane conics, plane quartics, rational/closed points, Riemann surfaces, and Jacobians as separate surfaces.

Inference:

Sage provides strong implementation evidence for presented affine/projective curves and analytic Riemann-surface bridges, but the project should keep the generic curve category scheme/variety-theoretic. Sage genus naming is especially convention-sensitive and must be translated into explicit project surfaces.

## Backend Survey

Source evidence:

- Macaulay2 Varieties package documentation, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/, supplies affine/projective variety infrastructure used by curve computations.
- Macaulay2 PlaneCurveLinearSeries documentation, https://www.macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/PlaneCurveLinearSeries/html/, includes plane-curve linear-series surfaces such as `geometricGenus` and normalization/canonical-model related methods.
- OSCAR projective plane curves documentation, https://docs.oscar-system.org/stable/AlgebraicGeometry/Curves/ProjectivePlaneCurves/, models projective plane curves as reduced projective algebraic sets and exposes `ProjectivePlaneCurve`, `defining_equation`, `degree`, and plane-curve-specific methods.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` routes `Curve.genus()`, `Curve.arithmetic_genus()`, `Curve.normalization()`, plane-curve equation/dual-curve methods, and rational-sextic node methods to Sage, Singular, Macaulay2, and OSCAR backend candidates.

Inference:

Macaulay2, Singular, OSCAR, and Sage are all plausible curve backends, but most support is for presented affine/projective/plane curves. Generic curve methods need exact hypotheses and should route to backend adapters only after the representation is known.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-SCHEMES-CATEGORY` supplies scheme and morphism vocabulary.
- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the integral separated finite-type variety convention.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY` supplies the complex base-field and analytic-bridge boundary.
- `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE` separately owns detailed Riemann-surface API mapping.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` already lists candidate curve, plane-curve, divisor, and rational-sextic method rows.

Inference:

The complex algebraic curve card should stabilize the dimension-one owner and route method names by hypotheses. It should not absorb the Riemann-surface backend card, divisor/sheaf cards, or Coble rational-sextic implementation work.

## Method Ownership Guidance

Admit these as curve-level or curve-refinement surfaces when downstream specs are written:

- `dimension() == 1`: defining refinement from varieties to curves.
- `genus()`: use only after choosing a precise public meaning; for smooth projective complex curves this can match Riemann-surface genus, while singular/nonproper/presented curves need `geometric_genus()` and `arithmetic_genus()` split.
- `arithmetic_genus()`: owned by proper/projective curve or presented projective curve refinements with coherent cohomology/Hilbert polynomial hypotheses.
- `geometric_genus()`: owned by integral curves through normalization; backend support may use Sage/Singular/Macaulay2.
- `normalization()`: owned by integral curves or presented singular-curve refinements; codomain includes the normalized curve and normalization morphism.
- `rational_points(K)` / `complex_points()`: Hom/point surfaces inherited from varieties; enumeration/approximation is backend-specific.
- `riemann_surface()` / `analytic_space()`: bridge from suitable smooth/projective complex curves or presented plane curves to analytic Riemann-surface objects.
- `jacobian()`: owned by smooth projective curves, not arbitrary curves.
- `equation()`, `defining_equation()`, `dual_curve()`: owned by plane-curve refinements.
- `nodes()`, `is_nodal()`: owned by singular plane-curve or rational-sextic refinements with node certificates as finite scheme/point data.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE`: detailed Sage Riemann-surface constructor/method mapping remains there.
- `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES`: curve-family monodromy must use curve/family vocabulary rather than raw polynomial parameter lists.
- `TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY`: families of curves are morphisms whose fibers are curves under explicit hypotheses.
- Coble rational-sextic geometry: rational sextic/node/normalization methods are downstream plane-curve refinements, not generic curve methods.

## Follow-Up Routing

No new card is needed from this curve pass. Existing sibling cards own the remaining specialization work:

- Riemann-surface API mapping belongs to `TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE`.
- Family/monodromy/Picard-Fuchs work belongs to the existing curve-complement and families cards.
- Rational sextic and Coble-specific curve methods remain downstream of Coble geometry cards and plane-curve refinements.

## Acceptance Evidence

- Mathematical convention recorded from Stacks curve definition plus the already-recorded variety and complex-variety cards.
- Sage surfaces surveyed for affine/projective curves, curves over `CC` as Riemann surfaces, and Jacobians.
- Backend surfaces surveyed for Macaulay2 plane-curve linear series, OSCAR projective plane curves, and existing Sage/Singular/Macaulay2 routing rows.
- Local dependencies and downstream cards listed explicitly.
- Follow-up routing records that no new card is needed because existing Riemann-surface, family, monodromy, and Coble cards own specialization.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for complex algebraic curves, recording the dimension-one complex-variety convention and routing genus, normalization, Riemann-surface, Jacobian, plane-curve, and node surfaces to proper refinements.
