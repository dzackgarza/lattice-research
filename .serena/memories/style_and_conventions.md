# Style and conventions
- Read docs before code; local governing docs outrank guesses.
- Use Read -> Checkpoint -> Edit -> Verify workflow for edits; noisy repo, never revert others' changes.
- All tests/builds/verification should route through justfile.
- Computation scripts prove claims with assertions tied to GOAL.md, literature, or independent computation; print statements are not proof.
- Preferred exact math tooling: foundation library for lattice construction, GAP for finite group actions, mature backends over ad hoc algorithms.
- State machine requires isolated worktrees/branches, bounded scope from scope.yml, non-author self-check, independent adversarial audit, and complete acceptance bundles before downstream trust.
- Repo forbids process debris; broken work is fixed or deleted, not documented and preserved.
