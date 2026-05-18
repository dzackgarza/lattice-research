# Literature And Source Agent

Use when a workstream needs exact literature, Sage/source, theorem, definition, or
hypothesis grounding. Pass the claim or term, candidate sources, search scope, and
report path.

Prompt pattern:

```text
Find source grounding for [claim/definition/term].

Approved question: [question]
Workstream phase: [path]
Candidate sources: [paths/URLs/arXiv IDs/Sage modules]
Search scope: [local theory, Sage docs/source, references, web, arXiv]
Report artifact: [path]
Stop and report if: exact hypotheses or owner category cannot be found.

Return exact statements, hypotheses, source paths, and gaps. Use the five-field
negative-finding format for anything not found. Do not infer a theorem from nearby
terminology.
```

Return:

- exact source paths or URLs;
- theorem/definition statements in paraphrase or short compliant excerpts;
- hypotheses and applicability notes;
- unresolved gaps with confidence and remaining search space;
- suggested paper margin notes for source-backed or missing-source claims.
