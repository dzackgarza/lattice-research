# Research repo overview
- Purpose: exact computational and proof-audited research workflow for Coble moduli / lattice-theoretic tasks from GOAL.md.
- Canonical governance: GOAL.md, STATE_MACHINE.md, PROOF_AUDITING.md, AGENTS.md.
- Core output model: task artifacts under tasks/T-XXXX with task.md, scope.yml, assumptions.md, dependencies.md, plan.md, implementation/, proofs/, computations/, audit/, outcomes/, archive/.
- Repo layout emphasizes durable mathematical content only: computations/, coble_research_lean/, notes/, papers/, tasks/, theory/.
- Key environment: Sage at /home/dzack/miniforge3/envs/sage/bin/sage; use uv venv / uv sync, never system packages.
- All computation runs go through justfile. README says scripts should be run through just, not directly.
