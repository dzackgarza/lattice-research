---
id: DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]'
title: Decide module sidedness structure transport and overload surfaces
status: unstarted
chosen: ''
options:
- name: Commutative-first root module surface
  pros:
  - Matches the current category-spec smoke frontier and most Sage module wrapper evidence.
  - Lets tensor, dual, symmetric, exterior, annihilator, and natural-pairing surfaces
    advance with standard commutative-ring signatures.
  - Keeps noncommutative module sidedness out of the root API until left, right, and
    bimodule owners are explicitly named.
  cons:
  - Requires follow-up decisions before admitting noncommutative tensor products,
    duals, annihilators, and transported module structures.
- name: Add left right and bimodule owners now
  pros:
  - Gives noncommutative tensor, dual, annihilator, and natural-pairing surfaces a
    mathematically precise home.
  - Avoids later migration if Ore and representation-module work needs sided module
    vocabulary soon.
  cons:
  - Broadens the current spec phase and may require restructuring existing module,
    algebra, and Ore mapping cards before implementation can continue.
- name: Reject ambiguous overloads from public module API
  pros:
  - Keeps `__mul__` and unqualified `modify_module_structure` from hiding unrelated
    constructions under Python or mutation-shaped names.
  - Forces named methods such as scalar multiplication, tensor product, restriction
    of scalars, extension of scalars, and twist-by-automorphism.
  cons:
  - Requires explicit migration notes for Sage/Python compatibility spellings.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide module sidedness structure transport and overload surfaces

## Summary

The root module ownership spec admits the standard commutative-ring and
integral-domain module surfaces, but several remaining rows depend on conventions that
must not be guessed during implementation:

- noncommutative left/right/bimodule sidedness for tensor products, duals,
  annihilators, and natural pairings;
- torsion conventions over rings with zero-divisors, where "killed by a nonzero
  scalar" need not define the intended torsion submodule without additional
  hypotheses;
- the public type for scalar-action data returned by `module_structure()`;
- whether `modify_module_structure(...)` is a transport, restriction, extension, or
  twisting construction;
- whether overloaded `__mul__` survives as public API or is only Sage/Python interop.

## Source Provenance

- `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- `category_specs/modules/__init__.py`

## Acceptance Criteria

- Decide whether the root module spec is commutative-first or whether left, right, and
  bimodule category owners must be added before implementation.
- Decide whether torsion beyond integral domains is admitted, and if so whether it
  uses regular elements, non-zero-divisors, localization support, or another named
  scalar condition.
- Define the public `ModuleStructure` data type or split it into named scalar-action
  constructions.
- Decide whether `modify_module_structure(...)` is rejected, renamed, or split into
  restriction, extension, transport, and twist constructors.
- Decide whether `__mul__` is public module API or only interop spelling for named
  scalar-multiple and tensor-product surfaces.
- Update `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]` before moving or deleting any
  root module abstract method affected by this decision.

## Dependencies And Boundaries

This decision blocks only module rows whose meaning depends on sidedness, scalar-action
transport, or overloaded Python spelling. It does not block the admitted commutative
base-ring owners for tensor, symmetric, exterior, dual, annihilator, torsion over
integral domains, quotient construction, span, direct sum, or subobject intersection.
