# Posets Triage

The promoted subtree now owns the order-theoretic surface separately from
ordinary sets. The current hierarchy distinguishes finite posets, finite
meet-semilattices, finite join-semilattices, and finite order-theoretic
lattices.

## Current Blockers

The Sage `Poset(...)`, `MeetSemilattice(...)`, `JoinSemilattice(...)`, and
`LatticePoset(...)` constructors are variadic compatibility surfaces. They need named
project constructor paths and closed overload cases before implementation.

## Concrete Future NEEDS_DECISIONS Items

- Choose the named constructor API for the documented `Poset(...)` input cases:
  elements plus relations, elements plus order predicate, elements plus cover
  predicate, upper-cover dictionary, upper-cover list, acyclic `DiGraph`, and
  existing-poset refinement.
- Choose whether aggregate `meet(x, y=None)` and `join(x, y=None)` become
  explicit overloads, separate finite-fold methods, or stay as Sage
  compatibility-only behavior.
- Choose project type names for lattice congruences before admitting
  `congruence`, `quotient`, and `congruences_lattice` stubs.
- Decide ownership for graph, plotting, TikZ, polytope, order-complex,
  incidence-algebra, Möbius-algebra, and polynomial invariant surfaces.
- Decide how certificate-returning Sage predicates should appear in project
  signatures without `certificate` boolean overload ambiguity.

## Evidence Gaps

- Searched: local Sage category filenames under
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories`.
- Found: `posets.py`, `finite_posets.py`, `lattice_posets.py`, and
  `finite_lattice_posets.py`; no semilattice category module filename appeared
  in that directory.
- Conclusion: I believe Sage has concrete finite semilattice classes but no
  separate documented Sage semilattice category module in this installation.
- Confidence: Medium.
- Gaps: I did not complete an import-level Sage category introspection because
  local Sage imports failed before reaching poset category modules.

- Searched: `/home/dzack/miniforge3/envs/sage/bin/sage -python` import of
  `sage.combinat.posets.posets` and `sage.combinat.posets.lattices`.
- Found: import failed during Sage category initialization with
  `ImportError: cannot import name Category`.
- Conclusion: I believe the local Sage interpreter is not reliable for source
  introspection from this working directory/session.
- Confidence: Medium.
- Gaps: I did not debug the Sage environment because the task could proceed
  from published Sage documentation and local source paths.
