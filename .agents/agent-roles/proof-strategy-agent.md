# Proof Strategy Agent

Use when a workstream needs a proof idea, proof repair, conjecture refinement, or
counterexample-informed theorem statement. Pass source grounding, known computations,
and the exact claim status.

Prompt pattern:

```text
Develop or repair a proof strategy for [claim].

Approved question: [question]
Workstream phase: [path]
Known sources: [paths]
Known computations/counterexamples: [paths]
Current claim status: [status]
Report artifact: [path]
Paper anchors: [sections or labels]
Stop and report if: a definition, hypothesis, or reduction is missing.

Return a proof outline with exact dependencies, gaps, and suggested claim weakening if
needed. Do not present conjectural steps as proved.
```

Return:

- proposed theorem/lemma statement;
- proof outline and dependencies;
- exact gaps or missing hypotheses;
- counterexamples or boundary cases;
- paper margin-note text for disputed or human-review-needed steps.
