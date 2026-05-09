# Research Agent Roles

These are repo-local role prompts for co-mathematician-style delegation. The active
chat or harness is the project coordinator. These files define what the coordinator
must pass to delegated agents and what each role must return.

Use these prompts with whatever delegation mechanism is available. If the harness does
not expose named subagents, paste the relevant role contract into the worker prompt.

Every delegated prompt must include:

- approved research question and goal;
- workstream phase path;
- branch type;
- allowed and forbidden files;
- expected report artifact;
- uncertainty policy and stop conditions.

Roles:

- `workstream-coordinator.md`: owns one branch and its report.
- `literature-source-agent.md`: finds exact statements, sources, and hypotheses.
- `experimental-computation-agent.md`: runs bounded computations or simulations.
- `proof-strategy-agent.md`: develops or repairs proof strategies.
- `reviewer-agent.md`: reviews reports, claims, sources, computations, and style.
- `uncertainty-auditor.md`: tracks disputed claims, failed branches, and review stalls.
