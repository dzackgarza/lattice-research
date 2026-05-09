# Uncertainty Auditor

Use when the coordinator needs a branch-independent view of claim status, disputed
lemmas, missing sources, review stalls, or failed explorations. Pass cards, reports,
paper sections, and recent review findings.

Prompt pattern:

```text
Audit uncertainty for [scope].

Approved question: [question]
Scope: [cards/reports/paper sections]
Known claims: [claim refs or labels]
Recent reviews: [paths]
Stop and report if: a claim's stated status is stronger than its evidence.

Return a claim-state table, disputed assertions, missing validations, failed
explorations that should be preserved, and user-escalation candidates.
```

Return:

- claim-state table;
- overstated or underspecified claims;
- stalled review loops and false-consensus risks;
- failed explorations that should be linked into reports or paper;
- next validation or human-steering actions.
