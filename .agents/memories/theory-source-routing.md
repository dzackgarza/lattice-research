# Theory Source Routing

Trigger: before using anything under `theory/` as mathematical authority, adding background prose, adding expected values, or turning a theory note into implementation work.

The directory routing is defined by `theory/index.md`:

- `theory/references/` is the source-authority layer: citation index, BibTeX, claim map, and extracted literature.
- `theory/foundations/` is durable mathematical vocabulary and background used across tasks.
- `theory/algorithms/` explains mathematical algorithms and orbit/computation methods independent of one backend.
- `theory/backends/` records external-tool capabilities, integration boundaries, backend-specific algorithms, and the existing-software-first map.
- `theory/moduli/` owns Coble/K3/Enriques moduli claims and period-domain background.
- `theory/external/` is vendored or externally sourced theory/tooling material retained for reference.
- `theory/spec_backups/` preserves source material that still needs explicit human-directed migration before rewrite or deletion.

Rule: identify the role of the theory file before citing it. Algorithm and backend notes tell future work how to compute; they do not replace literature-backed source claims.

For standard claims, start with `theory/references/index.md` and `theory/references/claim-map.md`. If a computation supports a standard fact, state that it is supporting evidence or an exact worked example, not the primary source.

Verification: a new theory-backed claim should cite the relevant reference entry or explain why a source-mining card is needed.
