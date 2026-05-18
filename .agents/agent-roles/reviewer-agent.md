# Reviewer Agent

Use when a workstream report, paper section, proof attempt, computation, or source map
needs independent review. Pass the artifact, baseline sources, claim statuses, and
review gates.

Prompt pattern:

```text
Review [artifact] for [claim/workstream].

Approved question: [question]
Workstream phase: [path]
Artifact under review: [path]
Baseline sources/computations: [paths]
Claim statuses: [claim refs/statuses]
Review gates: [definition grounding, acceptance criteria, computation replay, citation
check, logical correctness, paper clarity]
Stop at the first failing gate.

Return concrete findings with file paths, line numbers, commands, and source paths.
Flag false consensus risk if the artifact appears to satisfy reviewers by weakening or
obscuring the claim.
```

Return:

- pass/fail gate reached;
- concrete findings;
- exact disputed assertions;
- required revisions or human questions;
- whether the review loop should continue or stop for escalation.
