# Daily Work Schedule

Autonomous agents run on this rotation.
Each block is a one-shot session (`ocm one-shot`) dispatched by `task-sched`. The agent
reads AGENTS.md, does the block's work, and exits.
No block exceeds one session.

* * *

## 00:00 – 02:00 Policy enforcement and debris cleanup

- Run the automatic pruning checklist from AGENTS.md (delete .orig, .sage.py, empty
  dirs, banned directories, stale top-level markdown)
- Check for code thrashing: review files changed many times in recent git history — this
  indicates agents undoing each other's work or progress stuck in a cycle
- If thrashing is detected, `remember` the pattern (what files, what cycle) so future
  sessions can break the loop

* * *

## 02:00 – 04:00 Policy improvement

- Read recent git history and agent memories for recurring problems
- If a problem recurs, identify the BEHAVIORAL root cause — what agent behavior produced
  the problem, not what specific file or directory was created
- Draft a policy update to AGENTS.md that prevents the root behavior, not just the
  symptom. A policy that bans a specific directory name is a symptom fix.
  A policy that bans the behavior of preserving broken work in any form is a root fix.
- Policy changes must be committed with a commit message explaining: what recurring
  problem was observed, what root behavior causes it, and how the new policy prevents it

* * *

## 04:00 – 06:00 Literature and references

- Web research for papers and books not already listed in REFERENCES.md
- Ensure all relevant literature references are available locally in machine-parseable
  form (extracted from PDFs) so workers don't repeatedly fetch the same material
- For arXiv papers, prefer LaTeX source over PDF OCR

* * *

## 06:00 – 08:00 Literature leverage check

- Review existing literature to determine if current computation scripts are leveraging
  known theory instead of reinventing it
- Verify known theory with computational examples as a starting point
- Check if any GOAL.md task has a simpler path via a theorem already in the literature

* * *

## 08:00 – 10:00 Computation audit

- For each computation script in `computations/`, verify:
  - Assertions trace to specific GOAL.md claims or literature, not internal consistency
  - Expected values come from the mathematics, not from prior runs
  - Script runs via `just` without errors
- If a script fails: fix it or delete it.
  Do not document the failure.
- If a script's assertions only test internal consistency, rewrite the assertions to
  test GOAL.md claims

* * *

## 10:00 – 12:00 Goal alignment

- Review current work against GOAL.md tasks
- Identify drift: work that doesn't trace to a specific task
- Identify high-value vs low-value work: leveraging existing theory and pushing
  boundaries vs checking boxes with no clear motivation
- If drift is found, `remember` what drifted and why, so future sessions course-correct

* * *

## 12:00 – 14:00 Memory maintenance

- Review and update project memories
- Prune memories that are stale or no longer relevant
- Ensure failed approaches are recorded with: what was tried, why it failed, what to try
  instead
- Ensure operational context (environment quirks, tool gotchas) is captured

* * *

## 14:00 – 16:00 Foundation and refactoring

- Refactoring: centralized constructors in `coble_geometry_foundation.sage`
- Ensure all scripts use foundation library, not ad-hoc constructions
- Ensure no script loads the legacy `coble_geometry.sage`

* * *

## 16:00 – 18:00 Software and tooling

- Investigate and install software packages useful to computation scripts (GAP packages,
  Sage optional packages, CARAT, etc.)
- Ensure justfile recipes are up to date and cover all scripts

* * *

## 18:00 – 20:00 Subagent transcript review

- Use `ocm` to read recent subagent transcripts
- Identify common failures, misinterpretations of instructions, repeated mistakes
- If a failure pattern is found, determine the root behavioral cause and either:
  - Update AGENTS.md with a policy that prevents it
  - `remember` the pattern for future sessions

* * *

## 20:00 – 22:00 Mathematical work

- Advance the highest-priority unverified GOAL.md task
- Use worktrees for any new computation
- Every script must assert GOAL.md claims, not internal consistency

* * *

## 22:00 – 00:00 Lean formalization

- Advance Lean formalizations in `coble_research_lean/`
- Check if target results already exist in Mathlib before proving
- Consolidate any duplicate Lean project directories
