---
id: SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Recover exact indefinite form backend bridge contract
status: needs-review
priority: high
requirement: Historical Indefinite and polyhedral_common wrappers must be recovered
  as exact backend bridges with normalized matrix conventions and witness verification.
acceptanceCriteria:
- Indefinite isometry, automorphism group, orbit representative, isotropic subspace
  orbit, and stabilizer calls have documented mathematical domains.
- Backend row-action or right-action matrices are converted to the repo public action
  convention exactly once at the bridge boundary.
- Witnesses and generators are checked as lattice isometries or group elements before
  public methods return them.
- Missing binaries, unsupported signatures, and environment failures stop the backend
  call rather than silently substituting weaker evidence.
complexity: 85
tags:
- FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY
---
# Recover exact indefinite form backend bridge contract

## Source Provenance

- `src.bak/backends/external/README.md`: built binary list and limits.
- `src.bak/backends/external/py_polyhedral/binaries.py`:
  `INDEF_FORM_TestEquivalence`, `INDEF_FORM_AutomorphismGroup`,
  `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`,
  `INDEF_FORM_StabilizerVector`, and `INDEF_FORM_StabilizerIsotropicPlane`.
- `src.bak/backends/isometry_backend.py`: exact obstruction sequence and general
  indefinite witness branch.
- `.agents/memories/theory/backends/software-capability-map.md`: Indefinite.jl
  routing for indefinite forms, Oscar/Hecke routing for lattice invariants, and CARAT
  limitation to positive-definite or finite-matrix-group auxiliary work.
- `.agents/memories/theory-backend-routing.md`: repo method-to-backend routing and
  the warning that direct GAP-in-Sage loading of Indefinite.jl is not a drop-in route.
- `.agents/memories/theory/backends/indefinite-isometry.md`: verified upstream
  Indefinite.jl/GAP/C++ routes and local Julia 1.6.7 isolation requirement.
- `.agents/memories/theory/backends/indefinite-jl.md`: public Indefinite.jl function
  signatures and returned matrix equations.
- `.agents/memories/backend-environment-notes.md`: local `HOME` isolation needed to
  prevent the pinned Indefinite.jl GAP stack from reading the user `~/.gap` tree.

## Contract

The recovered bridge accepts exact presented form data from a public lattice or
formed-module object and calls a documented exact backend. Outputs are raw until the
public layer verifies them: an isometry witness must preserve the form and have the
claimed source/target behavior; group generators must be elements of the appropriate
Aut object; orbit representatives must be typed and verified.

The bridge owns backend conventions. If an upstream binary returns row-action matrices
or uses a right-action convention, the bridge converts them before they enter public
group semantics.

## Definition Grounding

- Mathematical object: a presented integral nondegenerate indefinite symmetric
  bilinear lattice or formed module over `ZZ`, represented to the backend by its exact
  Gram presentation.
- Public convention: matrices entering public Hom/Aut semantics use the repo's
  left-column action convention. A public automorphism generator `g in O(L)` verifies
  `g.T * gram(L) * g == gram(L)`. A public isometry witness `f: L -> M` verifies
  `f.T * gram(L) * f == gram(M)` with source and target recorded by the Hom parent.
- Backend convention: raw Indefinite.jl matrices are documented as satisfying
  `T^T Q1 T = Q2`. The historical `py_polyhedral` wrappers also record row/right-action
  conventions in stabilizer comments. The bridge must normalize whichever convention
  the selected route returns exactly once before public objects see the matrix.
- Completeness claim: a backend call is complete only for the documented exact backend
  domain. A missing binary, unsupported ring, unsupported signature, parse failure,
  Julia/GAP environment collision, or nonzero backend exit is not mathematical
  evidence; it is a bridge failure.

## Backend Routing Contract

The bridge must record the selected exact route for each operation:

| Operation family | Preferred route | Historical local route | Public owner |
| --- | --- | --- | --- |
| Indefinite form isometry | Indefinite.jl `INDEF_FORM_TestEquivalence(Q1, Q2)` | `INDEF_FORM_TestEquivalence` binary via `py_polyhedral` | formed-module Hom parent / lattice `is_isometric_to` |
| Indefinite automorphism generators | Indefinite.jl `INDEF_FORM_AutomorphismGroup(Q)` | `INDEF_FORM_AutomorphismGroup` binary | `L.Aut()` / orthogonal group |
| Norm-level orbit representatives | Indefinite.jl `INDEF_FORM_GetOrbitRepresentative(Q, norm)` | `INDEF_FORM_GetOrbitRepresentative` binary | `L.Aut().orbits(...)` or typed orbit surface |
| Isotropic k-plane and k-flag representatives | Indefinite.jl `INDEF_FORM_GetOrbit_IsotropicKplane` and `INDEF_FORM_GetOrbit_IsotropicKflag` | `INDEF_FORM_GetOrbit_IsotropicKplane` binary with `plane`/`flag` selector | orthogonal-group action on isotropic subobjects or flags |
| Vector and isotropic-subspace stabilizers | bridge-needed exact Indefinite/polyhedral route | `INDEF_FORM_StabilizerVector` and `INDEF_FORM_StabilizerIsotropicPlane` binaries | subgroup objects of `L.Aut()` |

Oscar/Hecke remains the preferred backend for lattice invariants, genera, local
conditions, discriminant groups, primitive embeddings, and centralizer images when the
operation is supported there. CARAT is not an indefinite lattice backend; it may appear
only as a positive-definite or finite-matrix-group auxiliary after the relevant group
is already known to be finite.

## Operation Contracts

### Isometry Witness

Input: two public nondegenerate indefinite integral formed objects `L` and `M` with
exact Gram presentations over `ZZ`.

Output: either no witness, or a public Hom element `f in L.Hom(M)` whose matrix has
been normalized to the public convention and verified by the Hom containment rule. The
backend matrix is not returned directly.

The historical obstruction ladder from `src.bak/backends/isometry_backend.py` is
admitted as early exact evidence, not as a proof substitute. Rank, signature,
determinant, discriminant group, discriminant-form isometry, rational isometry, local
isometry, and genus checks may reject early when source-backed and exact. If they do
not reject, the general indefinite branch must return and verify a witness before a
positive isometry result is accepted, except for a separately source-grounded theorem
branch such as the even indefinite 2-elementary Nikulin classification.

### Automorphism Generators

Input: a public nondegenerate indefinite integral formed object `L`.

Output: generators of a subgroup object of `L.Aut()` or the orthogonal group object.
Each raw generator must be normalized and checked for integrality, invertibility, parent
rank, and form preservation before it is admitted. A list of matrices is backend data
until every matrix is an element of the public Aut parent.

### Norm Orbit Representatives

Input: a public indefinite integral lattice `L` and an exact norm value in the form
codomain.

Output: typed elements of `L` or typed rational/metric-dual elements when the operation
is explicitly over an extended object. Each representative must be parent-constructed,
must have the requested norm, and must be accompanied by the backend route's
completeness claim. Exhaustive finite-window enumeration is not a replacement for the
backend orbit theorem.

### Isotropic Subspaces And Flags

Input: a public indefinite integral lattice `L`, an integer `k`, and optionally typed
subobjects or flags when testing equivalence or stabilizers.

Output: isotropic subobjects or flags with inclusion data, not row matrices. The bridge
must verify rank `k`, isotropy of the restricted form, and parent containment. For flag
operations, the nested inclusions are part of the object being stabilized or represented.

### Stabilizers

Input: a public group action by `L.Aut()` on an element, subobject, line, plane, or flag.

Output: a subgroup object with generators admitted through `L.Aut()` and verified to
fix the element pointwise or stabilize the subobject/flag setwise exactly as the public
method name states. Pointwise and setwise stabilizers are distinct surfaces; the bridge
must not blur them because a wrapper accepts a `plane`/`flag` string.

## Boundary Failures

The bridge must fail loudly at the boundary for:

- missing binary or missing Julia package;
- Julia/GAP environment collision, including the known user `~/.gap/pkg/JuliaInterface`
  conflict unless the subprocess isolates `HOME`;
- unsupported base ring, non-integral input, degenerate input where the backend
  requires nondegeneracy, or a signature outside the backend domain;
- parser failure, malformed matrix shape, rational entries where integral witnesses
  are required, or a matrix that fails public containment verification;
- backend nonzero exit, timeout, or stderr/error report.

These failures are not reasons to silently substitute Sage definite algorithms,
finite-window search, random search, or local bespoke matrix enumeration.

## Non-Preservation Boundaries

- Do not expose `run_and_check`, temporary files, or Python-literal parser details as
  part of the public contract.
- Do not make `M G M^T = G` and `G^T M G = M` both appear at call sites; normalize the
  convention at the bridge.
- Do not replace exact witness calls with finite-window enumeration.
- Do not mark an operation supported merely because a wrapper name exists; the binary
  or upstream package must be available and verified.
- Do not preserve `assert`-only validation from `py_polyhedral`; implementation work
  should raise typed backend errors and then verify public containment separately.

## Acceptance Criteria

- [x] Each backend operation records its domain, output, and completeness claim.
- [x] The spec requires raw output conversion to be centralized and tested against the
  public convention during implementation.
- [x] The spec requires public methods to verify returned witness/generator data before
  exposing it.
- [x] The spec requires unsupported or unavailable backend states to fail loudly at the
  bridge boundary.
