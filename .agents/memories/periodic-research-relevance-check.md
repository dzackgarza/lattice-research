---
title: Periodic Research Relevance Check
status: active
---
# Stop periodically and check whether the current work still advances research

Trigger this check:

- after 2-3 artifact edits;
- after 2-3 card/plan/status updates;
- after a correction from the user;
- after more than one round of classification without source changes;
- before detailed engineering work that does not directly expose mathematical
  vocabulary;
- whenever the agent feels tempted to create a plan, handoff, decision card, or memory
  instead of reading/fixing source.

Answer concretely:

1. What mathematical object, operation, theorem, construction, or interface is this work
   advancing?
2. What source file, proof note, spec method, backend bridge, or research computation
   will change?
3. Is this engineering necessary to make future mathematics safe, or is it process work
   shaped like progress?
4. Does this prevent a known failure mode such as raw matrix hacking, oracle-like
   computations, or ungrounded claims?
5. If this session stopped now, what would be closer to a publishable mathematical
   result?

If the answers are vague, stop artifact work.
Read the source/math, fix the source-level issue, or retire the artifact.
