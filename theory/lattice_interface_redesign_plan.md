# Lattice Interface Complete Redesign Plan

This file is the execution plan for the complete lattice redesign. It
supersedes the earlier lightweight plan draft.

## Overview

Current state is not acceptable because the public lattice layer still carries
wrong semantics from an ambient embedded-module model, stale naming, thin
wrapper helpers, and incomplete morphism/group structure. The target state is a
clean semantic hierarchy of public nouns whose implementations delegate exact
computation to Sage and the existing backend code without leaking backend
concepts into the public API.

This is a complete redesign of the lattice interface, not a compatibility
cleanup. The current generated code is retained only as migration source
material. Any concept rejected in the canonical specs must be excised rather
than preserved behind shims or transitional wrappers.

## Canonical Sources

- `theory/spec_backups/lattices_written_spec_backup.py`
- `theory/lattice_redesign_corrections_spec.md`

These two files are the source of truth for architecture, naming, and semantic
requirements. Existing tests, current implementation details, and temporary
adapter code are not source-of-truth artifacts.

## Constraints

- No compatibility shims.
- No legacy import aliases beyond the final intended public export surface.
- No public `native` terminology.
- No public `to_sage`, `from_sage`, or equivalent Sage-object extraction or
  admission on the final public surface.
- No ambient embedding state on public lattice/module nouns.
- No helper wrappers for trivial one-line Sage operations.
- No new public methods that merely expose Sage-native semantics rejected by the
  specs.
- No `raise`, `try` / `except`, or `None`-sentinel control flow in final
  mathematical APIs.
- No hand-rolled public validation in constructors or conversion entry points;
  public-boundary validation must live in pydantic models.
- No optional arguments or optional public field types in the final API unless
  the user explicitly approves them.
- No `Any`, `object`, or similarly broad public type annotations.
- No manual matrix-equation checks duplicated across call sites when semantic
  containment on the relevant noun should own that check.
- No internal renaming of semantically obvious canonical objects.
- No further redesign work should add features to the current flat files except
  insofar as they are being migrated or deleted.
- Existing generated code must be migrated and reused where mathematically sound
  rather than discarded wholesale.

## Preconditions

- The two canonical spec files above remain readable and tracked.
- The current generated lattice code remains available as extraction source
  until its logic has been migrated into the target hierarchy.
- Pydantic is the required public-boundary validation layer for constructor and
  coercion inputs.
- Mathematical preconditions inside proved algorithms remain assertions; object
  shape validation does not.
- The final public nouns must provide the standard method surface required by
  `CONTRIBUTING.md`: `__hash__`, `__repr__`, correct `__eq__`, and LaTeX
  printing hooks.

## Scope

In scope:

- Replacing the current lattice public API hierarchy.
- Replacing the current file layout with a real subdirectory hierarchy.
- Rebuilding morphisms, homspaces, dual/discriminant semantics, and orthogonal
  group semantics to match the written specs.
- Moving backend delegation behind the new semantic layer.
- Deleting rejected concepts and stale names from the public surface.

Out of scope during the redesign:

- Preserving the old API shape merely to keep stale tests passing.
- Expanding unrelated mathematical features.
- Full-suite stabilization before the new hierarchy is in place.

## Target Hierarchy

The public package should end in this form:

- `src/lattices/__init__.py`: final public exports only
- `src/lattices/core/abstract.py`: `BilinearModule`, `QuadraticModule`
- `src/lattices/core/elements.py`: element nouns and shared element behavior
- `src/lattices/core/free.py`: free bilinear-module semantics over general `R`
- `src/lattices/core/torsion.py`: torsion bilinear/quadratic module semantics
- `src/lattices/core/rational.py`: `RationalLattice`, `DualLattice`
- `src/lattices/core/integral.py`: `Lattice`
- `src/lattices/core/discriminant.py`: `DiscriminantForm`,
  `DiscriminantGroup`, discriminant elements
- `src/lattices/morphisms/homspaces.py`: homspace nouns
- `src/lattices/morphisms/lattice.py`: rational/integral lattice morphisms
- `src/lattices/morphisms/discriminant.py`: discriminant morphisms
- `src/lattices/groups/orthogonal.py`: orthogonal-group nouns and subgroup
  semantics
- `src/lattices/validation/presentations.py`: constructor validation only

Backend delegation should end in this form:

- `src/backends/isometry_backend.py`: isometry delegation only
- `src/backends/dawes_orbit_backend.py`: orbit/stabilizer delegation only
- `src/backends/isotropic_gamma_orbit_backend.py`: isotropic-orbit delegation
  only

Flat files such as the current `src/lattices/modules.py`,
`src/lattices/morphisms.py`, `src/lattices/groups.py`, and
`src/lattices/orthogonal.py` are temporary migration waypoints and should be
deleted once their contents have been moved into the target hierarchy.

## Phases

### Phase A: Containment and skeleton

- Create the target subdirectory hierarchy and stub only the intended files.
- Freeze the public noun vocabulary and file ownership.
- Mark current flat lattice files as migration-source files, not destinations.
- Completion:
  - every target file exists,
  - every public noun has a declared home,
  - no new work lands in the wrong file class.
- Verification:
  - file inventory inspection,
  - import graph inspection,
  - diff review confirming no new compatibility shims were added.

### Phase B: Core noun migration

- Move abstract nouns, element semantics, free-module semantics, and
  rational/integral lattice semantics into the target `core/` files.
- Replace hard-coded `ZZ` where the written spec requires general `R`.
- Remove rejected public state:
  `ambient_parent`, `inclusion_matrix`, `projection_lattice`,
  `projection_matrix`, `scaled_element`, `lift_vector`, and any public
  `native`-style methods.
- Remove public Sage leakage:
  `to_sage`, `from_sage`, direct Sage-object constructor admission, and
  analogous passthroughs that let callers bypass the semantic layer.
- Remove optional-argument constructor shapes from the public nouns and split
  the cases into explicit constructors or class methods.
- Completion:
  - public module/lattice nouns are presented only by generators and Gram data,
  - membership is parent-based,
  - no ambient embedding state remains on the public nouns,
  - no public Sage leakage remains on the noun surface.
- Verification:
  - direct inspection of public constructors and fields,
  - import compile of the moved files,
  - spec-review against the canonical sources,
  - grep confirming that public `src/lattices/core/` APIs no longer expose
    `to_sage`, `from_sage`, `ambient_parent`, or `inclusion_matrix`.

### Phase C: Validation and typing pass

- Replace hand-written public validation with explicit pydantic models at the
  public boundary.
- Add complete type annotations on constructors, element conversions, morphism
  constructors, and group entry points.
- Replace `hasattr`/`isinstance` abuse with typed or semantic dispatch.
- Remove `raise`-style validation from public constructors and coercions.
- Remove optional public types and `Any`-typed surfaces from the final lattice
  package.
- Add explicit `@override` markers wherever the codebase/runtime supports them.
- Completion:
  - public constructors and coercions validate through pydantic models,
  - abstract classes have real abstract methods,
  - public methods no longer return `None` for mathematically undefined cases,
  - public mathematical APIs use assertions only for true mathematical domain
    obligations rather than input-shape checking,
  - public signatures avoid `Any` and optional variants.
- Verification:
  - static inspection of signatures,
  - direct inspection of validation ownership in `src/lattices/validation/`,
  - import compile,
  - grep confirming no new `raise`, `try`, or `except` in the public lattice
    layer,
  - grep confirming no `Any`, `object`, `| None`, or `Optional` in the public
    lattice signatures.

### Phase D: Morphisms and homspaces

- Rebuild homspace nouns first, then morphism elements as elements of those
  spaces.
- Implement the missing constructor families and migration of existing matrix
  and generator-image logic.
- Replace the current bogus cokernel logic with actual object construction
  driven by the inclusion or quotient in question.
- Move matrix-isometry checking to the semantic containment boundary of the
  relevant hom-space or orthogonal-group noun instead of repeating matrix
  equations in ad hoc methods.
- Completion:
  - `hom()` returns homspaces,
  - morphisms own `image`, `kernel`, `cokernel`, `is_primitive`, and related
    verbs,
  - `A_L := coker(L -> L^*)` is modeled through the correct construction path,
  - equality on hom spaces and morphisms matches the `CONTRIBUTING.md`
    semantics.
- Verification:
  - API inspection,
  - dedicated spec tests once the hierarchy is stable,
  - review against the morphism block in the written spec backup.

### Phase E: Discriminant and dual semantics

- Rebuild `DualLattice` and discriminant objects without fake projection state.
- Ensure dual-lattice elements, not ad hoc vectors, are the relevant lift
  objects.
- Move lattice invariants such as `delta` and `coparity` to the lattice layer.
- Completion:
  - discriminant class semantics come from the dual/discriminant architecture,
    not from remembered ambient state,
  - discriminant-group API does not own lattice-only invariants.
- Verification:
  - public API inspection,
  - direct comparison against the preserved correction spec.

### Phase F: Orthogonal groups and backend boundary

- Move orthogonal-group nouns into `src/lattices/groups/orthogonal.py`.
- Remove constraint-merge bookkeeping from the public group layer and express
  subgroup semantics through the proper `ConditionSet` boundary.
- Keep backend files delegation-only; they may compute generators/orbits, but
  they must not define the public semantics.
- Completion:
  - `L.orthogonal_group()` is the semantic home,
  - stabilizers live on the orthogonal-group nouns,
  - backend files no longer dictate public API structure.
- Verification:
  - call-site inspection,
  - import compile,
  - spec-check against the orthogonal-group corrections.

### Phase G: Debris deletion

- Delete temporary flat files and any remaining stale names once all migrated
  logic has a final home.
- Delete rejected helper functions and old shim names.
- Delete internal renamings of canonical objects where direct construction is
  the intended name.
- Completion:
  - the repo has exactly one intended public lattice hierarchy,
  - no duplicate or transitional lattice files remain.
- Verification:
  - file inventory,
  - grep for banned names and rejected fields.

## Task-Level Stop Rules

- Stop if a public noun requires ambient embedding state to function.
- Stop if a phase attempts to preserve a rejected name or helper for convenience.
- Stop if backend code begins defining public semantics rather than delegated
  computation.
- Stop if an operation cannot be expressed without inventing a new ad hoc
  helper instead of using an existing Sage or backend primitive.
- Stop if public-object validation is drifting back into ad hoc asserts or
  exception plumbing instead of the pydantic boundary layer.
- Stop if a public API patch introduces optional args/types, `Any`, or public
  Sage-object passthroughs.
- Stop if downstream consumer rewiring begins before the upstream noun/morphism
  interfaces are stable.

## System-Level Validation

- During the architecture migration, use file-layout inspection, import
  compilation, grep checks for banned names, and spec conformance review.
- During validation migration, explicitly grep for `raise`, `try`, `except`,
  `hasattr`, and `None`-sentinel returns in `src/lattices/`.
- During style migration, explicitly grep for `Any`, `object`, `| None`,
  `Optional`, public `to_sage`/`from_sage`, and missing standard methods on the
  public nouns.
- After the hierarchy stabilizes, add or update dedicated spec tests that prove
  the mathematical interface rather than preserve stale implementation details.
- Do not treat the legacy suite as the architecture gate.

## Risks and Rollback

Main risks:

- Carrying over wrong ambient or wrapper semantics into the new hierarchy.
- Splitting files without actually changing the semantic model.
- Letting backend convenience concerns dictate the public API.

Mitigation:

- Treat the canonical spec files as hard gate documents for every phase.
- Use the current generated files only as extraction sources.
- Delete migrated source files as soon as their logic has a stable final home.

Rollback / fallback:

- The rollback point is the current staged flat hierarchy.
- If a migration step corrupts the target hierarchy, restore from the staged
  checkpoint and redo that phase without preserving the rejected abstraction.

## Expected End State

At completion, the lattice subsystem is a clean semantic package with:

- a real subdirectory hierarchy,
- no compatibility cruft,
- no ambient-embedding state on public nouns,
- no public Sage leakage,
- no optional public API surface and no `Any`-typed public signatures,
- typed constructors with pydantic-backed public validation,
- correct homspace/morphism/discriminant semantics,
- backend delegation kept behind the public mathematical layer.
