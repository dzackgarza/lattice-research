---
name: research-math-boundary
description: Use when working on mathematical shared code boundaries, lattice/module
  foundations, Sage/GAP/Julia/Lean integration, literature-backed computation, or
  exact backend ownership.
---

# Research Math Boundary

This skill is the canonical repo-level authority for mathematical architecture boundaries, trusted base vocabulary, backend ownership, and exact computation routing.

## Canonical source

The source of truth is this skill plus `references/math-boundary.md`.

Read `references/math-boundary.md` before changing shared mathematical code, lattice/module foundations, backend wrappers, tests involving canonical constructors, Lean/Aristotle work, literature extraction, or Sage/GAP/Julia integration.

## Core policy

- Trusted shared code is a semantic mathematical base built from explicit nouns with methods, not a flat bag of helpers.
- If a task cannot be expressed cleanly through the public noun vocabulary, stop and surface a task-boundary failure.
- If a mathematical noun, invariant, or predicate is not definition-grounded in repo
  theory, references, spec backups, Sage docs/source, or an approved decision, stop and
  source it before adding it to the public spec.
- Do not solve missing foundations with ad hoc helpers inside a dependent task.
- Compose upstream exact implementations instead of restating mathematics locally.
- Route mathematical implementation through `research-software-wiring` before writing local algorithms.
- Tests and computations must use canonical constructors and sourced mathematical expectations.

## Load with

- Load `research-code-style` for contribution-style and implementation-level rules.
- Load `research-software-wiring` before mathematical implementation, backend integration, or exact algorithm work.
- Load `research-orchestration` before implementation, self-check, audit, or acceptance work.
- Load `category-spec-style` when the work touches category specs or Sage constructor mapping.
