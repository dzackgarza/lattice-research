# Workstream Coordinator

Use when a single approved goal needs one linear branch of research. Pass the approved
question, selected goal, workstream phase path, branch type, report path, paper anchors,
allowed files, forbidden shortcuts, and stop conditions.

Prompt pattern:

```text
Coordinate exactly this workstream: [goal].

Approved question: [question]
Branch type: [prove/disprove/literature/theory/computation/implementation/formalization/synthesis/audit/exploration]
Workstream phase: [path]
Report artifact: [path]
Paper anchors: [sections or labels]
Allowed scope: [paths]
Forbidden actions: [actions]
Stop and report if: [conditions]

Produce incremental report updates with claim status, provenance, uncertainty, failed
paths, and next escalation point. Do not mark the workstream complete until the report
has passed the required review.
```

Return:

- report path and sections updated;
- claims advanced and their current status;
- sources/computations/proofs consulted;
- failed explorations preserved;
- unresolved uncertainty and escalation needs.
