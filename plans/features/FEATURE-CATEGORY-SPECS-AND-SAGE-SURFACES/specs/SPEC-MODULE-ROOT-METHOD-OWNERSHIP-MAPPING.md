---
id: SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
- '[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]'
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
| `annihilator()` | `Modules(R).OverCommutativeRing().ParentMethods`, with PID finite-presentation algorithms as implementation evidence | `annihilator(self: RModule) -> Ideal` | Ideal `Ann_R(M) = {r in R : r m = 0 for all m in M}` | Commutative scalar ring, or an explicit sided noncommutative convention | Admitted for commutative rings; noncommutative sidedness is blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` |
| `torsion_submodule()` | `Modules(R).OverIntegralDomain().ParentMethods` | `torsion_submodule(self: RModule) -> SubModule` | Submodule `{m in M : exists 0 != r in R with r m = 0}` | Integral domain, so "nonzero scalar" is meaningful and torsion elements form a submodule | Admitted for integral domains; arbitrary-ring torsion conventions are blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` |
| `tensor_algebra()` | `Modules(R).OverCommutativeRing().ParentMethods`, refined by finite-generation/basis algorithms where available | `tensor_algebra(self: RModule) -> Algebra` | `T_R(M) = direct_sum_{n >= 0} M^{tensor n}` | Commutative base ring for the current project module convention; noncommutative versions need bimodule data | Admitted for commutative base rings, with codomain in algebra constructor vocabulary |
| `base_change(...)` | Module objects with specified scalar-extension data | `base_change(self: RModule, morphism: RingMorphism) -> RModule` | `S tensor_R M` as an `S`-module | A ring morphism `R -> S`; the target scalar ring is not recoverable from a bare ring object without the structure map | Admitted as a signature change from `base_change(S: Ring)` to an explicit ring morphism |
| `module_structure()` | `Modules(R).ParentMethods` | `module_structure(self: RModule) -> ModuleStructure` | The scalar action data defining `M` as an `R`-module | Must fix sidedness and the `ModuleStructure` type | Blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` before implementation |
| `modify_module_structure(...)` | A named transport/twist construction, not an unqualified mutator | `modify_module_structure(self: RModule, sigma: ModuleStructure) -> RModule` | Module with transported or replaced scalar action | `sigma` must be a valid action map with stated source and target | Blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; rename/split likely |
| `symmetric_algebra()` | `Modules(R).OverCommutativeRing().ParentMethods` | `symmetric_algebra(self: RModule) -> Algebra` | `Sym_R(M)` | Commutative base ring; implementation may require finite presentation or basis data | Admitted for commutative base rings; codomain in algebra constructor vocabulary |
| `alternating_algebra()` | `Modules(R).OverCommutativeRing().ParentMethods` | `alternating_algebra(self: RModule) -> Algebra` | exterior algebra `Lambda_R(M)` | Commutative base ring; implementation may require finite presentation or basis data | Admitted for commutative base rings; this is the current smoke frontier owner for `alternating_algebra` |
| `dual()` | `Modules(R).OverCommutativeRing().ParentMethods`, refined by finite-free/projective dual-object implementations | `dual(self: RModule) -> DualModule` | `Hom_R(M, R)` | Commutative scalar ring for the current project convention; noncommutative left/right duals need explicit sidedness | Admitted for commutative rings; result lies in `Modules(R).DualObjects()`; noncommutative duals are blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` |
| `determinant_module()` | finite-rank projective modules, with finite-rank free modules as the first implementation owner | `determinant_module(self: RModule) -> RModule` | Top exterior power of `M` | Finite rank and projective/free hypotheses | Admitted on finite-rank projective/free owner, not arbitrary root modules |
| `cardinality()` | Set/cardinality surface inherited by modules as sets | `cardinality(self: RModule) -> Cardinality` | Cardinality of the underlying set of `M` | Depends on set/cardinality framework, not module-specific structure | Prefer inherited set owner |
| `is_isomorphic_to(...)` | `Modules(R).ParentMethods` or Hom/isomorphism vocabulary exposed on modules | `is_isomorphic_to(self: RModule, other: RModule) -> bool` | Boolean predicate for `R`-module isomorphism | Same base ring and module category context | Admitted as module predicate, with Hom/Aut evidence |
| `is_submodule_of(...)` | `Modules(R).Subobjects().ParentMethods` for submodule objects, with an ambient module supplied or already stored | `is_submodule_of(self: SubModule, other: RModule | None = None) -> bool` | Boolean predicate that `self` is included as a submodule of `other`, or of its recorded ambient when `other` is omitted | Requires inclusion or ambient data; abstract isomorphism of modules is not enough | Admitted on subobject/ambient owner, not arbitrary root modules |
| `direct_sum(...)` | `Modules(R).ParentMethods` | `direct_sum(self: RModule, other: RModule) -> RModule` and `direct_sum(self: RModule, modules: Sequence[RModule]) -> RModule` | Direct sum/biproduct module | Compatible base-ring/module category data | Admitted construction method on modules |
| `tensor(...)` | `Modules(R).OverCommutativeRing().ParentMethods`, with sided tensor products split separately when noncommutative owners are admitted | `tensor(self: RModule, other: RModule) -> RModule` and `tensor(self: RModule, modules: Sequence[RModule]) -> RModule` | Tensor product module | Compatible base ring; for noncommutative rings, right/left or bimodule sidedness data | Admitted for commutative base rings; noncommutative tensor products are blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` |
| `intersection(...)` | Submodules of a common ambient module | `intersection(self: SubModule, other: SubModule) -> SubModule` | Intersection submodule | Common ambient module; algorithms may require field/PID/free refinements | Move from arbitrary root only after subobject/ambient owner is admitted |
| `span(...)` / `submodule(...)` | `Modules(R).ParentMethods` on an ambient module `M` | `span(self: RModule, gens: RModuleElement | Sequence[RModuleElement], check: bool = True, already_echelonized: bool = False) -> SubModule` | Submodule of `M` generated by `gens` | Generators are elements of `M`; options are Sage interop/checking data | Admitted construction method on modules |
| `__mul__(...)` | No single mathematical owner for the current overloaded spelling | `__mul__(self: RModule, other: RingElement | RModule) -> RModule` | Either scalar multiple submodule or tensor product | Current spelling conflates two constructions | Blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]`; split into named methods before implementation unless explicitly retained as interop |
| `quotient_module(...)` / `__truediv__` | `Modules(R).ParentMethods` on an ambient module `M` | `quotient_module(self: RModule, submodule: SubModule, check: bool = True) -> QuotientModule` | Quotient module `M/N` | `submodule <= self` | Admitted construction method on modules; quotient-specific methods are additional structure on the output |
| `natural_pairing()` | modules with an admitted dual convention, initially commutative scalar rings | `natural_pairing(self: RModule) -> RModuleForm` | Evaluation pairing `M^* x M -> R` or `M x M^* -> R` according to the dual convention | Dual object and argument order must be fixed; noncommutative sidedness affects codomain and variance | Admitted after the commutative dual convention is fixed in `DualObjects`; noncommutative variants are blocked by `[[DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES]]` |

## Implementation Consequence

The immediate implementation card may add constructor routing needed to reach the next
smoke frontier, but it must not move, delete, or weaken a root method until this spec
row is either admitted or replaced by a linked decision with the same method signature
data.
