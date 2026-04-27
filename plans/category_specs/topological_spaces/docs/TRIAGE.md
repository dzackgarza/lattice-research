# Topological Spaces Triage

## Current Alignment

- `TopologicalSpaces()` is the same target category surface as
  `Sets().Topological()`: a set equipped with a topology is a topological space.
- `TopologicalSpaces().Metric()` is the same metric-space refinement exposed by
  `Sets().Metric()`.
- The subtree does not keep a separate wrapper category around `Sets().Topological()`.
  The axiom-backed category is the public category.

## Outstanding Decisions Needed

- Decide which Sage constructors, if any, belong in
  `TopologicalSpaces().Constructors()`.
- Decide how topological rings, modules, and algebras should inherit from this subtree
  once those category subtrees are reorganized.
