---
id: SPEC-SAGE-MYPY-CATEGORY-OVERRIDE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN]]'
dependsOn: []
title: Acceptance criteria for Sage mypy category override plugin
status: needs-review
priority: high
complexity: 80
acceptanceCriteria:
- 1. A method in C.ParentMethods marked @override is accepted by mypy iff the corresponding
  method name exists in a Sage semantic ancestor method container derived from C.parent_class.mro().
- 2. Same holds for ElementMethods via C.element_class.mro().
- 3. Same holds for MorphismMethods via C.morphism_class.mro().
- 4. No category source file needs to add literal Python bases to ParentMethods, ElementMethods,
  or MorphismMethods.
- 5. No per-category protocol or inherited-method stub inventory is generated.
- 6. New singleton categories automatically participate if Sage's category machinery can instantiate
  them and expose the runtime method-class MRO.
- 7. Parameterized categories are either explicitly configured or explicitly left unresolved;
  no parameter guesses.
- "8. Admission is namespace-agnostic: source fullnames outside `sage.categories.*` are eligible if they resolve to Sage category method containers; the plugin MUST NOT require a `sage.categories.` prefix."
- "9. Third-party or repo-local subtree fixtures under a non-Sage namespace exhibit the same pass/fail override behavior as equivalent fixtures under `sage.categories.*`."
- 10. A debug mode can print the injected static base list for a method container.
- 11. Plugin behavior is deterministic under mypy incremental mode.
- 12. Removing or renaming an ancestor method causes @override failures in semantic descendants
  after rechecking.
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
---
# Acceptance Criteria: Sage Mypy Category Override Plugin

## Source

This spec is derived from the greenfield design document in
`~/ai/quality-control/planning/override-sage-categories.md`, the
user-provided design spec (2026-05-10 session), and the 2026-05-10 follow-up
clarification that this plugin is for any package hand-rolling a Sage category
subtree, not only code filed under upstream `sage.categories.*`.

## Requirements

### Core Override Semantics

A method in `C.ParentMethods` decorated with `@override` (standard
`typing.override`) must pass mypy type-checking if and only if the method
name exists in at least one ancestor method container derived from
`C.parent_class.mro()`.

The same applies to `ElementMethods` via `C.element_class.mro()` and
`MorphismMethods` via `C.morphism_class.mro()`.

This is the central invariant: mypy's static `@override` check must align with
Sage's runtime method resolution.

### No Source-Level Inheritance

No category source file must be required to add literal Python bases to
`ParentMethods`, `ElementMethods`, or `MorphismMethods`. The containment classes
remain "merely containers of operations" as documented by Sage. The plugin
injects ancestry at type-checking time without modifying source trees.

### No Generated Artifacts

No per-category protocol, inherited-method stub inventory, `.pyi`, or
intermediate representation is generated. The plugin operates during semantic
analysis of the original source, not by pre-generating type stubs.

### Singleton Category Participation

Any singleton category (parameter-free, canonical instance — `Groups()`,
`Sets()`, `Rings()`, `Fields()`, etc.) must automatically participate. If
`SageCategory.super_categories()` returns ancestors and the corresponding
`parent_class` / `element_class` / `morphism_class` can be constructed, the
plugin resolves and injects static bases without per-category configuration.

### Parameterized Category Policy

Parameterized categories (`Modules(R)`, `Algebras(R)`, `VectorSpaces(K)`) are
NOT resolved by guessing parameters.

- **Default mode**: singleton-only. Parameterized categories without
  configuration produce no injected bases. Optionally emit a plugin diagnostic.
- **Configured mode**: the plugin accepts a configuration mapping
  parameterized category classes to representative instances, e.g.:
  `Algebras: QQ`. Only bases common across all configured representatives
  (intersection mode) are injected, or a single canonical representative
   per configuration key.

### Namespace-Agnostic Admission

The source module path is NOT part of the semantic contract. A category method
container defined in `my_project.categories.*`, `category_specs.*`, or any
other importable package path must be admissible if the plugin can parse the
method-container fullname, instantiate the corresponding Sage category object,
and project its runtime method-class bases back to source containers.

Prefix checks such as `fullname.startswith("sage.categories.")` are forbidden as
the decisive admission rule. Namespace may be used only as a cheap heuristic if
there is a semantic fallback path that still admits valid third-party Sage
category subtrees.

### Debug Mode

A debug mode (flag or configuration key) enables printing the injected static
base list for any method container. Output format:

```
C.ParentMethods static bases (from Sage):
  A.ParentMethods
  B.ParentMethods
```

This gives independent verification that the plugin is doing what Sage says.

### Incremental Mode Determinism

Plugin behavior must be deterministic under mypy's incremental/daemon mode.
Hook results may be cached; the plugin must not hold global mutable state
across different category classes.

`report_config_data()` must return JSON-encodable data including Sage version,
plugin version, and configured parameterized-category representatives so
mypy can invalidate caches when configuration changes.

### Reactivity to Ancestor Changes

When a method is removed or renamed in an ancestor method container, mypy must
report `@override` failures in all semantic descendant method containers that
declare an override of that method, after rechecking (incremental or fresh).

This is enforced by the `get_additional_deps()` hook: if `C.ParentMethods`
semantically depends on `A.ParentMethods` and `B.ParentMethods`, changing `A`
must invalidate or recheck `C`.

### Homset Categories (Secondary)

For a homset category `C.Homsets`, the plugin must resolve
`C.Homsets().ParentMethods` against `C.Homsets().parent_class.mro()`
and `C.Homsets().ElementMethods` against `C.Homsets().element_class.mro()`.

### Axiom Categories (Secondary)

For axiom-generated categories such as `C.Finite.ParentMethods`, the plugin
must resolve against the axiom category's `parent_class.mro()` without
hardcoding axiom names. Detection: parse nested category classes and ask
Sage whether the nested class participates in the category-with-axiom system.

### Failure Modes

- **Not a Sage method container**: Return None (normal mypy behavior).
- **Wrong namespace but valid Sage category subtree**: Continue semantic
  resolution; do not reject solely because the fullname is outside
  `sage.categories.*`.
- **Sage cannot resolve the category**: Do not inject bases. Emit optional
  plugin note under a Sage-specific error code.
- **Runtime MRO resolves but source container can't be mapped to mypy
  TypeInfo**: Omit that base only if it contributes no source-level method
  container. Otherwise emit diagnostic — override checks may be unsoundly
  incomplete.
- **Parameterized category without configured representative**: No injection.
  Optional diagnostic.
- **Mypy rejects injected MRO**: Report the method-container fullname and the
  Sage-computed source-container bases.

### Sage-Side Integration API

The Sage-side API (`sage.categories.mypy_support`) must expose:

- `method_container_bases(category_cls_fullname, method_path) -> list[str]`:
  returns source-level fullnames of ancestor method containers
- `is_category_method_container(fullname) -> bool`
- `parse_method_container_fullname(fullname) -> CategoryMethodContainer | None`

The mapping must handle: `Groups.parent_class` → `Groups.ParentMethods`,
`Monoids.parent_class` → `Monoids.ParentMethods`, and analogous for
`element_class` ← `ElementMethods`, `morphism_class` ← `MorphismMethods`.

Runtime dynamic classes with no source-level method container are omitted from
the static base list.

## Test Matrix

Minimal tests required:

| Test | Category | Expected |
|------|----------|----------|
| Valid override | B.ParentMethods.@override f, B.super_categories → [A()], A.ParentMethods defines f | PASS |
| Invalid override | B.ParentMethods.@override g, g absent from all ancestors | FAIL |
| Diamond | B→A, C→A, D→[B,C]; B.ParentMethods.f, C.ParentMethods.f, D.ParentMethods.@override f | PASS (Sage-computed order) |
| ElementMethods | B.ElementMethods.@override f, A.ElementMethods defines f | PASS |
| MorphismMethods | B.MorphismMethods.@override f, A.MorphismMethods defines f | PASS |
| Homset | B.Homsets.ParentMethods.@override f | PASS |
| Parameterized no-config | Algebras(QQ).ParentMethods.@override | no injection |
| Parameterized configured | Algebras via configured rep | bases from rep |
| Third-party subtree | `third_party_pkg.demo.C.ParentMethods.@override f` with valid Sage semantic ancestor | PASS |
| Signature mismatch | @override with incompatible signature | FAIL |
| Renamed ancestor | remove f from A.ParentMethods | B.@override f → FAIL |
| Cache invalidation | change A.ParentMethods | B rechecked |
| Config path loads plugin | mypy invocation through repo/QC-style config path | plugin actually active |

## Current Status

Needs review. The 2026-05-10 rewrite removes namespace as the decisive admission
criterion, adds non-Sage fixture coverage alongside the Sage-prefixed matrix,
and wires `sage_mypy_category_plugin.plugin` into the global QC mypy config
path. The spec is back to review-ready pending independent verification of the
new evidence.
