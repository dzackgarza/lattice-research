---
id: SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
title: Specify root module method ownership by explicit mathematical signatures
status: in-progress
priority: critical
requirement: Record the root `Modules(R)` method surface as explicit project method
  signatures with caller category, inputs, hypotheses, return type, source evidence,
  and decision status before any implementation moves or smoke-driven edits.
acceptanceCriteria:
- Every root module method row states the project method location, complete signature,
  return type, hypotheses, and status in ordinary mathematical language.
- Construction methods distinguish caller location from output type without treating
  construction/result categories as disjoint from `Modules(R)`.
- Ambiguous surfaces are marked decision-needed with the missing mathematical question,
  not implemented or deleted.
- '`category_specs/modules/docs/MAPPING.md`, `category_specs/modules/docs/SAGE_INVENTORY.md`,
  and the current `category_specs/modules/__init__.py` root abstract surface are cited
  as source material.'
- No root abstract method is deleted, weakened, or moved before the replacement project
  method signature is admitted here or in a linked decision.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify root module method ownership by explicit mathematical signatures

## Summary

This spec is the tracked owner for the root `Modules(R)` method mapping. It replaces
software-routing prose with project method signatures. Each row maps a current Sage or
project surface to a project method by saying where the method is defined, what data it
takes, what it returns, and under which hypotheses the statement is mathematically
coherent.

The category where the output object lives is part of the return type. It is not by
itself the method owner. If a method is defined on all modules, it is inherited by
every subcategory of `Modules(R)`.

## Source Provenance

- `category_specs/modules/__init__.py`, `_RModObjects`
- `category_specs/modules/docs/MAPPING.md`, especially module constructor, construction,
  and method ownership sections
- `category_specs/modules/docs/SAGE_INVENTORY.md`, especially Sage `Modules`,
  `ModulesWithBasis`, free-module, submodule, quotient, tensor, and dual surfaces
- Triggering task:
  `[[TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS]]`

## Signature Mapping

| Surface | Defined on | Project signature | Returns | Hypotheses | Status |
| --- | --- | --- | --- | --- | --- |
| `annihilator()` | `Modules(R).ParentMethods` when scalar annihilators form the admitted ideal object | `annihilator(self: RModule) -> Ideal` | Ideal of scalars annihilating `M` | Need the sided/noncommutative convention for `Ann_R(M)`; commutative-ring case is coherent | Decision-needed before implementation beyond commutative/PID evidence |
| `torsion_submodule()` | A torsion-admitting module category, not arbitrary `Modules(R)` until the scalar condition is defined | `torsion_submodule(self: RModule) -> SubModule` | Submodule of elements killed by admissible nonzero scalars | Requires an integral domain or another sourced torsion convention | Decision-needed for arbitrary rings; do not delete root obligation until replacement owner is admitted |
| `tensor_algebra()` | Module objects satisfying the tensor-algebra hypotheses | `tensor_algebra(self: RModule) -> Algebra` | `T_R(M)` | Requires the base-ring and sidedness hypotheses under which tensor algebra is defined | Decision-needed for codomain/type alias before implementation |
| `base_change(...)` | Module objects with specified scalar-extension data | `base_change(self: RModule, morphism: RingMorphism) -> RModule` | `M tensor_R S` as an `S`-module | A ring morphism `R -> S`; current `base_change(S: Ring)` signature is under-specified | Split/signature-change needed |
| `module_structure()` | `Modules(R).ParentMethods` | `module_structure(self: RModule) -> ModuleStructure` | The scalar action data defining `M` as an `R`-module | Must fix sidedness and the `ModuleStructure` type | Admitted after type grounding |
| `modify_module_structure(...)` | A named transport/twist construction, not an unqualified mutator | `modify_module_structure(self: RModule, sigma: ModuleStructure) -> RModule` | Module with transported or replaced scalar action | `sigma` must be a valid action map with stated source and target | Decision-needed; rename/split likely |
| `symmetric_algebra()` | Module objects satisfying the symmetric-algebra hypotheses | `symmetric_algebra(self: RModule) -> Algebra` | `Sym_R(M)` | Needs commutative/base-ring hypotheses and codomain owner | Decision-needed before implementation |
| `alternating_algebra()` | Module objects satisfying the exterior-algebra hypotheses | `alternating_algebra(self: RModule) -> Algebra` | `Lambda_R(M)` | Needs commutative/base-ring hypotheses and codomain owner | Decision-needed before implementation |
| `dual()` | Module objects for which the chosen dual is defined | `dual(self: RModule) -> DualModule` | `Hom_R(M, R)` with correct sidedness | Sidedness and dual-object convention must be explicit | Admitted after sidedness review; result lies in dual-object surface |
| `determinant_module()` | Finite-rank free/projective module category | `determinant_module(self: RModule) -> RModule` | Top exterior power of `M` | Finite rank and projective/free hypotheses | Move only after finite-rank/projective owner is admitted |
| `cardinality()` | Set/cardinality surface inherited by modules as sets | `cardinality(self: RModule) -> Cardinality` | Cardinality of the underlying set of `M` | Depends on set/cardinality framework, not module-specific structure | Prefer inherited set owner |
| `is_isomorphic_to(...)` | `Modules(R).ParentMethods` or Hom/isomorphism vocabulary exposed on modules | `is_isomorphic_to(self: RModule, other: RModule) -> bool` | Boolean predicate for `R`-module isomorphism | Same base ring and module category context | Admitted as module predicate, with Hom/Aut evidence |
| `is_submodule_of(...)` | Ambient-bearing subobject context | `is_submodule_of(self: RModule, other: RModule) -> bool` | Boolean predicate that `self` is a specified submodule of `other` | Requires an ambient/inclusion relation, not just abstract isomorphism | Decision-needed for exact caller category |
| `direct_sum(...)` | `Modules(R).ParentMethods` | `direct_sum(self: RModule, other: RModule) -> RModule` and `direct_sum(self: RModule, modules: Sequence[RModule]) -> RModule` | Direct sum/biproduct module | Compatible base-ring/module category data | Admitted construction method on modules |
| `tensor(...)` | Module objects with compatible tensor-product data | `tensor(self: RModule, other: RModule) -> RModule` and `tensor(self: RModule, modules: Sequence[RModule]) -> RModule` | Tensor product module | Compatible base ring and sidedness | Admitted after sidedness review; output carries tensor-product construction data |
| `intersection(...)` | Submodules of a common ambient module | `intersection(self: SubModule, other: SubModule) -> SubModule` | Intersection submodule | Common ambient module; algorithms may require field/PID/free refinements | Move from arbitrary root only after subobject/ambient owner is admitted |
| `span(...)` / `submodule(...)` | `Modules(R).ParentMethods` on an ambient module `M` | `span(self: RModule, gens: RModuleElement | Sequence[RModuleElement], check: bool = True, already_echelonized: bool = False) -> SubModule` | Submodule of `M` generated by `gens` | Generators are elements of `M`; options are Sage interop/checking data | Admitted construction method on modules |
| `__mul__(...)` | No single mathematical owner for the current overloaded spelling | `__mul__(self: RModule, other: RingElement | RModule) -> RModule` | Either scalar multiple submodule or tensor product | Current spelling conflates two constructions | Split into named methods before implementation |
| `quotient_module(...)` / `__truediv__` | `Modules(R).ParentMethods` on an ambient module `M` | `quotient_module(self: RModule, submodule: SubModule, check: bool = True) -> QuotientModule` | Quotient module `M/N` | `submodule <= self` | Admitted construction method on modules; quotient-specific methods are additional structure on the output |
| `natural_pairing()` | Module objects with an admitted dual convention | `natural_pairing(self: RModule) -> RModuleForm` | Evaluation pairing between `M` and `M^*` | Correct sidedness and form codomain must be fixed | Decision-needed for dual/form ownership |

## Implementation Consequence

The immediate implementation card may add constructor routing needed to reach the next
smoke frontier, but it must not move, delete, or weaken a root method until this spec
row is either admitted or replaced by a linked decision with the same method signature
data.
