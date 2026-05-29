---
title: Research Code Style Reference
status: active
date: 2026-05-29
---
# Research Code Style Reference

The canonical detailed contribution and code-style reference for the research repo.

## Mathematical Prose

All code must read like mathematical prose and follow either a definition or a theorem,
preferably cited.

## Assertions Over Exceptions

Prefer assertions of mathematical preconditions over exceptions and defensive recovery.

## Glue, Not Math

Delegate nontrivial mathematics to Sage, GAP, Julia, Singular, Lean, or other trusted
exact implementations instead of re-deriving it locally.

## No Try/Except

Mathematically correct code does not raise exceptions.
No `try`/`except`, no `raise`, no error-path handling.

## No Backward Compatibility

Avoid backward-compatibility shims, convenience aliases, and needless indirection.

## Single Source of Truth

Use one source of truth for constructions, semantic membership checks, equality,
validation, and backend boundaries.

## No Internal Renaming

Do not create wrappers that only rename an upstream method without adding repo
semantics.

## No Optional Arguments / No Optional Types

Inputs should be precise and predictable; optional variants should be explicit, not
sentinel-driven.

## Introspection Red Flags

Reject `isinstance`, `hasattr`, `getattr`, `type()`, `issubclass`, `callable()` patterns
unless boundary-justified.

## No `__all__` Exports

Allow importing everything and rely on `_name` conventions for private helpers.

## Semantic Checks Over Manual Implementation

Use Sage's built-in semantic checks such as `ZZ.ideal([...])` and `I.gens()[0]` instead
of manual gcd or determinant calculations.

## Backend Encapsulation

Sage, Julia, GAP, etc.
are calculation engines, not the public API. Public lattice objects must not inherit
from Sage implementation classes.

## TDD-First: Tests Must Have Sources

Tests for nontrivial mathematics must be sourced and must prove mathematical correctness
rather than encoding agent assumptions.

## No Re-Export Files / No Dataclasses

