# Topological Spaces Triage

## Current Alignment

- `TopologicalSpaces()` owns the topological-space method surface.
- `TopologicalSpaces().Metric()` owns metric-space methods.
- `Sets().Topological()` and `Sets().Metric()` remain navigation aliases into this
  topological-space hierarchy.

## Outstanding Decisions Needed

- Decide which Sage constructors, if any, belong in
  `TopologicalSpaces().Constructors()`.
- Decide how topological rings, modules, and algebras should inherit from this subtree
  once those category subtrees are reorganized.
