# Experimental Computation Agent

Use when a workstream needs bounded computation, numerical exploration, simulation, or
counterexample search to build intuition or produce replayable evidence. Pass the exact
question, allowed code/data paths, backend constraints, and validation expectations.

Prompt pattern:

```text
Run a bounded computational exploration for [question].

Approved question: [question]
Workstream phase: [path]
Allowed code/data scope: [paths]
Required backend policy: use mature exact systems first; route through just recipes.
Report artifact: [path]
Paper anchors: [sections or labels]
Stop and report if: a required backend, package, credential, or exact witness is
missing.

Produce replayable artifacts and distinguish intuition, counterexample, exact
computation, and theorem-level evidence.
```

Return:

- commands run through `just` and outputs;
- code/data artifacts produced;
- exact witnesses, counterexamples, or bounds found;
- limitations and unreplayed cases;
- paper/report annotations for computation-dependent claims.
