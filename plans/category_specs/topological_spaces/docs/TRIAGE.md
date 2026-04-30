# Topological Spaces Triage

## Current Alignment

- `TopologicalSpaces()` is the same target category surface as
  `Sets().Topological()`: a set equipped with a topology is a topological space.
- `TopologicalSpaces().Metric()` is the same metric-space refinement exposed by
  `Sets().Metric()`.
- The subtree does not keep a separate wrapper category around `Sets().Topological()`.
  The axiom-backed category is the public category.

## Current Smoke Frontier

`topological_spaces/smoketest.sage` currently reaches the deliberate constructor
sentinel:

- `TopologicalSpaces().Constructors() has admitted constructor cases` fails because no
  concrete topological-space constructor has been admitted yet.

The Sage warning about `Sets.Topological` not being a `CategoryWithAxiom` is also still
visible during smoke runs and belongs to the centralized topological inheritance
decision in `NEEDS_DECISIONS.md`.
