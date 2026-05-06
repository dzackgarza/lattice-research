---
id: SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track tensor algebra components mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/tensor_algebra_components/docs/MAPPING.md into
  a tracked spec surface and audit it for Sage-source completeness, mathematical correctness,
  and well-typed tensor component, contraction, trace, dual, and display signatures.
acceptanceCriteria:
- Source paths category_specs/tensor_algebra_components/docs/MAPPING.md and category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Tensor Algebra Components Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/tensor_algebra_components/docs/MAPPING.md`.

Source inventory: `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`.
- Sage written documentation pages named by the local inventory:
  - `reference/tensor_free_modules/sage/tensor/modules/free_module_tensor.html`
  - `reference/tensor_free_modules/sage/tensor/modules/tensor_with_indices.html`
  - `reference/tensor_free_modules/sage/tensor/modules/finite_rank_free_module.html`
- Installed Sage source files checked for this tensor-component pass:
  - `sage/tensor/modules/finite_rank_free_module.py`
  - `sage/tensor/modules/tensor_free_module.py`
  - `sage/tensor/modules/free_module_tensor.py`
  - `sage/tensor/modules/tensor_with_indices.py`
  - `sage/tensor/modules/comp.py`
  - `sage/tensor/modules/free_module_basis.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the tensor core
  method reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Tensor Core Inventory

The tensor inventory is intentionally narrow and names the tensor-free-module surface
needed for the project `TensorAlgebraComponents` subtree. This pass checked that each
inventoried surface has a mapping consequence:

- `TensorFreeModule` and `M.tensor_module(k,l)` map to tensor component parent objects
  in `TensorAlgebraComponents(R)`, with inherited finite-rank free module structure
  when the base module has finite rank;
- `FreeModuleTensor` and `M.tensor((k,l), ...)` map to `Tensor` elements, not parent
  categories;
- `base_module()`, `tensor_type()`, and Sage `tensor_rank()` are represented by the
  structural base-module link, the public `(k,l)` tensor type, and derived total order
  `sum(tensor_type())`;
- component assignment, `Components`, `comp`, `set_comp`, `display`, and
  `display_comp` are recorded as coordinate or display interop, not public
  mathematical objects;
- matrix, module-element matrix, list-of-matrices, and multidimensional-list inputs
  are routed through named tensor constructors rather than a catch-all component
  surface;
- `trace` and `contract` are admitted as closed tensor-element operations with
  explicit opposite-variance slot hypotheses and codomains;
- `TensorWithIndices` and string-index syntax are explicitly rejected as public API,
  with migration through named symmetry metadata, `trace`, or `contract`.

Negative missing-surface finding for the narrow tensor inventory:

- Searched: `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`,
  installed Sage tensor sources `finite_rank_free_module.py`,
  `tensor_free_module.py`, `free_module_tensor.py`, `tensor_with_indices.py`,
  `comp.py`, and `free_module_basis.py`, plus the converted tensor mapping rows above.
- Found: every surface named in the local tensor inventory has a corresponding
  admitted, derived, interop-only, or rejected mapping row in this spec.
- Conclusion: inference -- this pass found no unmapped surface inside the intentionally
  narrow tensor-free-module inventory.
- Confidence: Medium.
- Gaps: Sage tensor docs outside the three inventory URLs, unreleased Sage branches,
  and broader tensor-calculus APIs not named by this subtree inventory remain outside
  this narrow reconciliation pass.

## Converted Mapping Content

This file maps the narrow Sage tensor-free-module surface into the project
`tensor_algebra_components` subtree.

| Sage surface | Project surface | Rationale |
| --- | --- | --- |
| `TensorFreeModule` / `M.tensor_module(k,l)` | `TensorAlgebraComponents(R)` object, with parent categories `Modules(R).TensorProducts()` and `Modules(R).Free().FiniteRank()` | The object is the graded piece `T_R(M)[k,l]`, hence a finite-rank free module when `M` is finite-rank free. |
| `FreeModuleTensor` / `M.tensor((k,l), ...)` | `Tensor` element | A tensor is an element of some component module `T_R(M)[k,l]`; its parent recovers that module. |
| `base_module()` | `base_module() -> RModule` on component parents and tensor elements | This is the structural link from `T_R(M)[k,l]` back to `M`. |
| `tensor_type()` | `tensor_type() -> tuple[Integer, Integer]` | This is the unique public tuple-valued tensor type `(k,l)`, with `k` contravariant and `l` covariant slots. Ordinary rank is inherited from the finite-rank free module structure. |
| Sage `tensor_rank()` as total tensor order `k + l` | `sum(tensor_type())` when the total tensor order is needed | The project does not expose a second tensor-type/rank method. The tuple is `tensor_type()`; total order is a derived integer. |
| Module `rank()` / `dimension()` on tensor component parents | inherited from `Modules(R).Free().FiniteRank()` | The tensor component is a finite-rank free module, so ordinary module rank comes from that supercategory. It is not tensor type data. |
| `t[:]`, `t.set_comp(basis)[:]`, indexed component assignment | Named interop constructors on `TensorAlgebraComponents(R).Constructors()` with an explicit ordered basis or generating frame | Component arrays are coordinate inputs for constructing tensor elements, not public tensor objects. The old catch-all `from_components(...)` surface is private helper code only; public callers use the named matrix, module-element matrix, multidimensional-list, or list-of-matrices route with the frame that makes the coordinates meaningful. |
| Matrix over `R` | `TensorAlgebraComponents(R).Constructors().from_matrix(base_module=M, frame=e, entries=B)` | A scalar-valued bilinear form `M \otimes_R M -> R` is a covariant `(0,2)` tensor. The matrix is coordinate data relative to `e`; it is not intrinsic tensor data without that frame. |
| Matrix of module elements `Sequence[Sequence[RModuleElement]]` | `TensorAlgebraComponents(R).Constructors().from_module_element_matrix(base_module=M, frame=e, entries=products)` | A multiplication table with entries in `M` is the bilinear map `M \otimes_R M -> M`, hence a structure tensor in `M \otimes_R M^* \otimes_R M^*` of type `(1,2)`. The table is interpreted relative to the ordered input frame `e`. |
| Multiplication tensor structure constants | `Tensor.structure_constants(frame=e)` | A tensor of type `(1,2)` determines coordinate structure constants only after choosing an ordered basis or generating frame of its base module. Algebra constructors may read this basis-relative tensor surface instead of accepting Sage table/list shapes directly. |
| Lists of matrices for component data | `TensorAlgebraComponents(R).Constructors().from_matrices(base_module=M, frame=e, entries=matrices)` | This is an admitted interop shape for old table-like data relative to `e`. The return value is a tensor element. |
| Multidimensional lists for component data | `TensorAlgebraComponents(R).Constructors().from_multidimensional_list(base_module=M, frame=e, entries=data)` | This is an admitted interop shape for coordinate data relative to `e`. The return value is a tensor element. |
| Catch-all component data | no public constructor; private `_from_components(...)` helper only | Shape unions are implementation-local. Public callers use the named constructor matching the data they hold. |

## Deferred Tensor Surface Freeze

The old triage file at `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`
listed symmetry/antisymmetry subtrees, storage, contraction, trace, display, and
index notation as deferred. This section freezes those decisions before any tensor API
expansion.

| Sage/deferred surface | Frozen project decision | Owner and codomain consequence |
| --- | --- | --- |
| `sym=` / `antisym=` on `M.tensor(...)` and `M.tensor_module(...)` | Admitted as constructor metadata selecting symmetric or alternating tensor-component refinements. Symmetry and antisymmetry are mathematical submodule conditions on tensor slots, not standalone storage containers. | Owner: `TensorAlgebraComponents(R).Symmetric(slot_blocks)` and `.Alternating(slot_blocks)` refinements, with constructor methods accepting the Sage position data as named metadata. Hypotheses: `tensor_type() == (p,q)` and Sage position numbering on the `p+q` tensor arguments. Codomain: a tensor element or component parent in the corresponding refined submodule. Migration consequence: old code that treated symmetry data as its own public container is retired, but the mathematical symmetric/alternating submodule structure is preserved. |
| `Components`, `comp(...)`, `set_comp(...)`, `add_comp(...)`, `[:]`, indexed basis assignment | Remains private coordinate interop and storage. The admitted public routes are the named tensor constructors and `Tensor.structure_constants(frame=e)` for type `(1,2)` product tensors. | Owner: no new public owner beyond constructor interop. Codomain consequence: no typed finite collection return is admitted for general tensor storage. Migration consequence: old component-container workflows must convert coordinate data at the boundary into a `Tensor`; they do not persist as public tensor objects. |
| `t.trace(pos1, pos2)` | Admitted as public tensor-element method `trace(contravariant_position, covariant_position)`. | Owner: `Tensor` elements. Hypotheses: if `tensor_type() == (p,q)`, then `p >= 1`, `q >= 1`, and the selected positions have opposite variance inside the same tensor. Codomain: `RingElement` when `(p,q) == (1,1)`, otherwise a tensor in `T_R(M)[p-1,q-1]` on the same base module. Migration consequence: internal Einstein-style self-contraction is represented by this named method, not by index-notation strings. |
| `t.contract(...)` with Sage defaulted position conventions | Admit closed typed spellings: `contract(left_position, other, right_position)` for one contraction and `contract_many(pairs, other)` for a finite sequence of simultaneous contraction pairs. The Sage defaulted overloads such as `a.contract(b)` and `a.contract(b, 0)` are not project API. | Owner: `Tensor` elements. Hypotheses: `self` and `other` lie over the same base module; each pair chooses one contravariant and one covariant position across the two tensors; chosen positions are distinct. Codomain: `RingElement` exactly when the remaining tensor type is `(0,0)`; otherwise a tensor in the corresponding tensor component on the same base module. Migration consequence: old Sage positional shorthands and Einstein-product syntax must be rewritten to explicit contraction calls, but genuine simultaneous contractions remain admitted. |
| `t.display(...)` and `t.display_comp(...)` | Rejected as public category-spec methods in this subtree. They are basis-dependent rendering support, not mathematical tensor structure. | Owner: nonpublic Sage rendering/interchange layer only. Codomain consequence: no new project return object is introduced. Migration consequence: display-driven workflows stay in Sage interop or UI/debug code and are not part of the tensor mathematical API. |
| `TensorWithIndices(...)`, `t['...']`, repeated-index Einstein notation, bracket/parenthesis symmetrization syntax | Rejected as public tensor API. Sage explicitly documents `TensorWithIndices` as a technical class for notation-driven operations. | Owner: nonpublic interop only. Codomain consequence: no project method or object is named after index strings. Migration consequence: old index-notation usages must be translated into named constructor metadata (`sym=` / `antisym=`), `trace(...)`, or explicit `contract(...)`; unsupported notation-only shortcuts are retired. |

## Dual Objects And Forms

The dual-object surface of this subtree owns integral forms and remains inside the
tensor-component category:

```text
T_R(M)[p,q]^* \simeq T_R(M)[q,p]
```

For finite-rank free `M`, the displayed relation is a canonical isomorphism using the
finite-dual tensor-Hom adjunction and the standard `M** \simeq M` identification; it
is not definitional equality of parents. The same dual component is naturally
interpretable as `Hom_R(T_R(M)[p,q], R)`.
`Modules(R).HomCategory().Forms().Integral()` records that evaluation interpretation,
but it does not own the tensor component. If the original component has
`tensor_type() == (p,q)`, the dual component has `tensor_type() == (q,p)`.

The forms subtree owns formed modules: attaching such a tensor as form data to a module
places the result in `FormedModules(R).Bilinear()` or another forms-owned refinement.

| Sage/form surface | Project resurfacing |
| --- | --- |
| `Hom_R(T_R(M)[p,q], R)` as a form parent | `TensorAlgebraComponents(R).DualObjects()` with extra supercategory `Modules(R).HomCategory().Forms().Integral()` |
| Evaluating a form on a tensor | inherited hom/morphism evaluation from `Modules(R).HomCategory().Forms()` |

## Algebra Constructor Use

An algebra multiplication on a finite-rank free module `M` should be validated as a
`Tensor` with `tensor_type() == (1, 2)` and `base_module() is M`. Constructor
interop may accept multiplication tables as `Sequence[Sequence[RModuleElement]]` or
legacy lists of matrices, but those shapes belong here. `Algebras(R).Constructors()`
receives only the tensor element after this subtree has converted the shape into
canonical tensor data. Its only public extraction surface is
`Tensor.structure_constants(frame=e)`, which recovers the coordinate structure
constants encoded by the tensor relative to the chosen ordered frame `e`.
