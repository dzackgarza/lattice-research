# Sage Wrapper Subcategory Migration Plan

## Goal

The module subtree currently contains subcategories whose main purpose is to wrap Sage
implementation classes. That is the wrong abstraction when the Sage class names a
constructor family or a concrete implementation strategy rather than a mathematical
category.

The target state is:

- every module method from the Sage inventory is mapped to a real mathematical owner;
- constructor entry points route Sage objects into those owners by explicit construction
  case and precise Sage implementation-class matches at the boundary;
- chained axiom subcategories have their immediate supercategories declared before
  constructors depend on them;
- no category spec keeps a Sage-wrapper subcategory solely to expose methods from a Sage
  implementation class;
- `modules/smoketest.sage` asserts mathematical category membership and method behavior,
  not wrapper membership.

## Non-Negotiables

- Do not add explicit provider subclassing inside nested `ParentMethods`,
  `ElementMethods`, `MorphismMethods`, or `SubcategoryMethods`.
- Do not use `hasattr` or broad `try/except` to infer category membership.
- Do not route by generic duck-typing. Constructor routing may use exact Sage classes at
  the interop boundary; ordinary code should use mathematical categories.
- Do not keep a project subcategory unless it names a genuine mathematical category.
- Do not move a method just because a Sage wrapper used to provide it. Each method must
  be mapped from its mathematical meaning.
- Do not delete a wrapper until its methods are either represented on real categories,
  marked interop-only in `modules/docs/MAPPING.md`, or rejected with a documented
  mathematical reason.

## Prerequisites

- Use `modules/docs/SAGE_INVENTORY.md`, `modules/docs/MAPPING.md`, and
  `modules/docs/TRIAGE.md` as the starting sources.
- Read the Sage source and written Sage docs for each class before deciding its mapping.
- Use a commit checkpoint before each pass. Category-spec work uses the repository's
  no-verification commit path because the repo-wide hook is not scoped to this spec
  subtree.

## Efficient Order

The efficient order is mapping first, category graph second, constructors third,
method coverage fourth, deletion last. Doing this in any other order invites the same
failure mode: constructors and smokes depending on wrapper categories before the real
method owners exist.

## Current Execution State

Completed in the current branch:

- The wrapper inventory and mapping table have been created from the Sage inventory.
- `_CombinatorialFreeModules` has been deleted as a project subcategory. Construction
  now routes through `Modules(R).Constructors().CombinatorialFreeModule(...)` and
  refines into the real module categories `Free()`, `WithBasis()`, and
  `WithOrderedGeneratingSet()`.
- `WithBasis()` and `WithOrderedBasis()` are module axioms rather than Sage-wrapper
  categories. `WithOrderedBasis()` is a direct `Modules` axiom with immediate
  supercategories `WithBasis()` and `WithOrderedGeneratingSet()`.
- Standard free-module and basis subobject/quotient routing uses functorial
  construction categories such as `C.Free().FiniteRank().WithOrderedBasis()`,
  `C.WithOrderedBasis().Subobjects()`, and `C.WithOrderedBasis().Quotients()`.
- `FreeQuadraticModule` construction routes to a free finite-rank ordered-basis module
  with quadratic-form structure rather than to a wrapper category as the long-term
  owner.
- Generic basis-owned methods are now represented on `WithBasis()` and
  `WithBasis().HomCategory()`.
- Generic subobject and quotient construction-owner surfaces are represented on the
  module construction categories.
- PID presentation invariant surfaces are represented on
  `FinitelyPresentedModulesOverPID`.

Open blocker:

- `just smoke-file modules/smoketest.sage` currently stops before the module-wrapper
  assertions because finite/countable set structure still declares
  `_an_element_from_iterator` as an abstract method. That is the adjacent sets-spec
  decision recorded in `../../NEEDS_DECISIONS.md`; this migration must not weaken module
  smokes or delete adjacent set-spec methods to make module smokes pass.

Next work starts at the first `[~]` or `[ ]` row in the class todo. A partially
migrated row is not deletable until every inventoried method has a mathematical owner
or an explicit non-mapping decision.

## Phase: Freeze The Wrapper Inventory

Location: `modules/subcategories/`, `modules/__init__.py`,
`modules/docs/SAGE_INVENTORY.md`, `modules/docs/TRIAGE.md`.

Work:

- Build the authoritative candidate list from subcategory classes that either match Sage
  implementation classes in `__contains__` or exist only as constructor-family surfaces.
- Classify each candidate as constructor-only, real mathematical category, or mixed.
- For mixed candidates, split the implementation class evidence from the mathematical
  category name before any code edit.

Acceptance:

- `modules/docs/MAPPING.md` has a migration table covering every candidate in the todo
  list at the end of this file.
- Each row states the mathematical owner, constructor owner, and deletion condition.

Validation:

- `rg "_CombinatorialFreeModules|_FreeModulesWithStandardBasis|_VectorSpaces|_RepresentationModules" modules` finds only expected mapping/todo references until the
  later deletion phase.
- `git diff --check` passes.

Commit boundary:

- Commit only inventory and mapping documentation for this phase.

## Phase: Define The Mathematical Category Graph

Location: existing mathematical subcategories such as `free.py`,
`finitely_generated.py`, `finitely_presented.py`, `over_field.py`,
`over_integral_domain.py`, `over_pid.py`, `quadratic.py`, `bilinear.py`,
`with_forms.py`, `with_ordered_generating_set.py`, construction-category files under
`modules/subcategories/constructions/`, and hom/end/aut files where needed.

Work:

- Define missing immediate supercategories before any constructor depends on them.
- Express chains such as free finite-rank modules over fields through axiom/category
  composition, not by a wrapper class around `FreeModule_ambient_field`.
- Ensure subobject and quotient refinements are construction categories over the ambient
  module category, with ordered-generating-set refinements attached only where that
  structure is stated.
- Ensure bilinear, quadratic, lattice, and torsion-quadratic surfaces are stated as
  form-bearing module categories, not as wrappers around Sage form implementations.
- If a Sage method requires a chained axiom subcategory that does not yet exist, define
  the immediate missing owner first rather than installing the method on a narrower
  implementation wrapper.

Acceptance:

- Every category method owner in `modules/docs/MAPPING.md` resolves to an existing
  category object or to a clearly named missing category entry.
- No nested provider class subclasses another provider class to simulate method
  inheritance.
- For every declared `C <= D` relation, `C.HomCategory() <= D.HomCategory()` follows
  from the category construction rather than from manual class manipulation.
- For every category `C`, `C.EndCategory() <= C.HomCategory()` follows from the generic
  end construction.

Validation:

- Probe or ripgrep confirms no explicit nested provider subclassing was introduced.
- The relevant smoke section reaches category construction without C3 or dynamic-key
  failures for the newly defined surfaces.
- `git diff --check` passes.

Commit boundary:

- Commit by coherent graph cluster: ambient/free/vector, subobjects/quotients,
  form-bearing modules, graded/Ore/representation.

## Phase: Rewrite Constructor Routing

Location: `modules/__init__.py`, constructor-specific helpers, and
`modules/smoketest.sage`.

Work:

- For each Sage constructor, call the Sage constructor once and refine the returned
  parent into the real categories identified in the mapping phase.
- Keep exact Sage implementation-class matches localized to the constructor-routing
  boundary.
- Route by construction case first, class match second, and declared mathematical
  refinements last.
- Remove routing to project wrapper categories as soon as the target mathematical
  categories exist.
- Preserve previously supported call shapes with smoke cases that exercise the old call
  paths through the new explicit routes.

Acceptance:

- Constructor methods return Sage objects refined into real project mathematical
  categories.
- Constructor smokes assert membership in mathematical categories such as
  `Modules(R).Free()`, `Modules(R).WithOrderedGeneratingSet()`,
  `Modules(R).Subobjects()`, `Modules(R).Quotients()`, and form-bearing refinements.
- No constructor helper uses `hasattr`, broad catch-and-retry logic, or membership in a
  soon-to-be-deleted wrapper category.

Validation:

- `just smoke-file modules/smoketest.sage` is the main check.
- If the smoke still fails, the failure must expose a real missing category graph edge
  or mapped method owner, not a hidden wrapper dependency.
- `git diff --check` passes.

Commit boundary:

- Commit constructor routing separately from method-surface moves.

## Phase: Move Method Surfaces To Real Owners

Location: category owners named in `modules/docs/MAPPING.md`; element and morphism
providers under those same owners; hom/end/aut files for morphism-specific methods.

Work:

- For every method available on a wrapper candidate, decide one of:
  - it is a parent method on a real module category;
  - it is an element method on a real element surface;
  - it is a morphism method on the relevant hom/end/aut category;
  - it is a constructor helper;
  - it is Sage interop-only and remains unexposed;
  - it is rejected because it has no mathematical meaning without extra structure.
- Add missing immediate categories before placing methods that require those hypotheses.
- Keep support/order/coordinate methods on basis-bearing or ordered-basis surfaces, not
  on all free modules.
- Keep submodule, quotient, tensor, product, dual, hom, end, and aut methods on their
  construction categories.

Acceptance:

- `modules/docs/MAPPING.md` has no unmapped methods for any class in the final todo
  list.
- Deleted wrapper files do not remove the only representation of any mapped method.
- Methods that require ordered bases, forms, finite rank, PID hypotheses, or field
  hypotheses are not installed on broader categories.

Validation:

- For each migrated class, add or update a smoke statement using a real Sage object and
  the final category owner.
- `just smoke-file modules/smoketest.sage` passes or stops at a documented blocker that
  is not a deleted-wrapper dependency.
- `git diff --check` passes.

Commit boundary:

- Commit one method-owner cluster at a time, after the corresponding smoke statements
  are updated.

## Phase: Delete Wrapper Subcategories

Location: `modules/subcategories/`, `modules/__init__.py`,
`modules/docs/MAPPING.md`, and imports in adjacent files.

Work:

- Delete constructor-only wrapper files after all of their methods have moved or been
  rejected.
- Remove lazy imports, constructor accessors, and smoke references to deleted wrappers.
- Keep only subcategories that name real mathematical categories, even if Sage currently
  implements them with a concrete class.
- For mixed candidates, delete only the implementation-wrapper surface and keep the
  mathematical category under a corrected name and graph.

Acceptance:

- `rg` finds no references to deleted wrapper class names outside migration docs.
- The remaining `modules/subcategories/*.py` files correspond to mathematical
  categories, construction categories, or axiomatic restrictions.
- `modules/smoketest.sage` does not assert membership in wrapper categories.

Validation:

- `just smoke-file modules/smoketest.sage`.
- `rg "CombinatorialFreeModules|FreeModulesWithStandardBasis|VectorSubspacesWithOrderedGeneratingSet|QuotientModulesWithOrderedGeneratingSet" modules` returns only intentional documentation entries after deletion.
- `git diff --check`.

Commit boundary:

- Commit wrapper deletion last, after method coverage is complete.

## Stop Rules

- Stop if a class cannot be classified as constructor-only, real category, or mixed
  from the Sage source and docs.
- Stop if a method needs a mathematical owner that has not been defined yet.
- Stop if a smoke failure is caused by a category graph mismatch. Fix the graph before
  changing constructors.
- Stop if the required next step is production code outside `plans/category_specs`; the
  no-verification path here applies only to this category-spec migration.

## Class Migration Todo

Status markers:

- `[x]` removed or routed in the current branch;
- `[~]` partially migrated: routing, graph, or some method owners have moved, but the
  wrapper is not deletable yet;
- `[ ]` not started;
- `[?]` classify before editing because the name may be a real category even though the
  current file is wrapper-shaped.

| Status | Class | First mapping target | Deletion condition |
| --- | --- | --- | --- |
| [x] | `_CombinatorialFreeModules` | Constructor on `Modules(R)` refined to `Free()`, `WithBasis()`, and `WithOrderedGeneratingSet()` | Deleted in the current branch; keep only mapping docs and smokes. |
| [~] | `_FreeModulesWithStandardBasis` | Free modules with chosen ordered standard basis | Basis, generator, coordinate, and ambient methods moved to free/ordered-basis owners. |
| [~] | `_FiniteRankFreeModules` | `Modules(R).Free().FiniteRank()` | Tensor-calculus constructor routes refine to finite-rank free modules without a wrapper. |
| [ ] | `_FreeModulesOverIntegralDomains` | `Modules(R).Free().OverIntegralDomain()` | Domain-specific methods live on free modules over integral domains. |
| [ ] | `_FreeModulesOverPIDs` | `Modules(R).Free().OverPID()` | PID-specific Smith/Hermite/quotient methods live on the PID refinement. |
| [~] | `_VectorSpaces` | `Modules(K).Free().FiniteRank().OverField()` or the existing field-module surface | Field-specific linear algebra methods have field-category owners. |
| [~] | `_RealDoubleVectorSpaces` | Exact numeric field/vector-space refinement, if mathematically admitted | RDF-specific implementation methods are interop-only or owned by the field/vector-space refinement. |
| [~] | `_ComplexDoubleVectorSpaces` | Exact numeric field/vector-space refinement, if mathematically admitted | CDF-specific implementation methods are interop-only or owned by the field/vector-space refinement. |
| [~] | `_VectorSubspaces` | `Modules(K).Subobjects()` over the vector-space refinement | Subspace methods move to subobject and field-linear owners. |
| [~] | `_VectorSubspacesWithOrderedGeneratingSet` | Vector-space subobjects with ordered generating set | User-basis and coordinate methods move to ordered-generating-set subobject owners. |
| [~] | `_VectorSpaceQuotients` | `Modules(K).Quotients()` over the vector-space refinement | Quotient cover/relation/lift methods move to quotient owners. |
| [~] | `_FreeModuleSubmodules` | `Modules(R).Subobjects()` over free/PID module refinements | Submodule methods move to subobject owners with PID hypotheses where needed. |
| [~] | `_FreeModuleSubmodulesWithOrderedGeneratingSet` | Free-module subobjects with ordered generating set | User-basis methods move to ordered-generating-set subobject owners. |
| [~] | `_SubmodulesWithOrderedGeneratingSet` | Subobjects of modules with ordered generating sets | `SubmoduleWithBasis` implementation evidence is separated from the mathematical owner. |
| [~] | `_FreeModuleQuotients` | `Modules(R).Quotients()` over free module refinements | Free-cover, relation, lift, and quotient-map methods move to quotient owners. |
| [~] | `_QuotientModulesWithOrderedGeneratingSet` | Quotients of modules with ordered generating sets | `QuotientModuleWithBasis` implementation evidence is separated from the mathematical owner. |
| [~] | `_FinitelyGeneratedPIDQuotientModules` | Finitely generated or finitely presented modules over PIDs | FGP quotient methods move to PID finite-presentation owners. |
| [~] | `_FreeQuadraticModules` | Free modules with quadratic form | Keep only if the file is rewritten as a real form-bearing category. |
| [?] | `_IntegerLattices` | Integral lattices as finite-rank free `ZZ`-modules with integral bilinear form | Keep only if rewritten as the lattice/form category, not as a Sage class wrapper. |
| [?] | `_TorsionQuadraticModules` | Finite torsion modules with quadratic form | Keep only if it names the finite quadratic module category rather than Sage's implementation. |
| [ ] | `_FreeGradedModules` | Free graded modules | Graded free methods move to `Graded().Free()` owners. |
| [ ] | `_FinitelyPresentedGradedModules` | Finitely presented graded modules | FP graded methods move to `Graded().FinitelyPresented()` owners. |
| [?] | `_OreModules` | Modules over Ore-polynomial quotient data, if admitted as mathematical structure | Constructor and pseudomorphism data are separated from any real module category owner. |
| [?] | `_RepresentationModules` | Modules with a semigroup/group action | Keep only if rewritten as a representation-module category over the acting object. |
| [?] | `_RingObjectsAsModules` | Constructor or forgetful functor from ring objects to modules | Delete if it is only a ring-object implementation wrapper; keep a functor/category only if mathematically specified. |

## Per-Class Completion Rule

A class row can move to `[x]` only after all of the following are true:

- every inventoried method is mapped in `modules/docs/MAPPING.md` to a real owner or to
  an explicit interop-only or rejected non-mapping;
- every needed narrow category owner exists before the method is moved;
- constructor routing and smokes use real mathematical categories, not wrapper
  membership;
- the wrapper file, lazy import, constructor accessor, and membership smoke are deleted
  if the wrapper was constructor-only;
- `rg` finds the deleted wrapper name only in migration documentation.

For `[~]` rows, the next action is method-owner migration, not deletion.

## Remaining Method Clusters

- Ordered finite-rank coordinate surfaces: `basis_matrix`, `coordinate_vector`,
  `coordinates`, `from_vector`, and `echelonized_basis` need narrow basis/order owners
  before moving.
- Field subobject and quotient surfaces: `linear_dependence`, `subspace`,
  `complement`, `quotient_abstract`, and `lift_map` need field-linear subobject or
  quotient owners.
- PID free and subobject surfaces: `denominator`, `index_in`, Smith/Hermite data,
  `span_of_basis`, `basis_matrix`, and echelon surfaces need PID-refined owners.
- Quotient normal-form and basis surfaces: `free_cover`, `free_relations`, `lift_map`,
  `retract`, quotient-of-quotient structure, and `cokernel_basis_indices` need quotient
  owners with the right basis or PID hypotheses.
- Form and lattice surfaces: determinant, discriminant, Gram data, inner products, and
  lattice reduction need form-bearing and lattice owners before wrapper deletion.
- Graded, Ore, representation, and ring-object bridges are not migrated yet; classify
  them from Sage docs and source before moving methods.
