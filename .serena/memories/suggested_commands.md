# Suggested commands
- `just` : list recipes.
- `just uv-setup` : sync project environment.
- `just test-foundation` : run foundation library tests.
- `just test` : current aggregate test entrypoint (still has TODOs for broader gates).
- `git status --short` : inspect noisy worktree before acting.
- `tree -L 1 -a .` : inspect repo roots.
- `npx -y @probelabs/probe search "<query>" /home/dzack/research ext:md -o plain --max-results <N>` : semantic doc/code discovery.
- `npx -y @probelabs/probe extract "<file>#<symbol>" -o plain` : AST-aware extraction when source code is needed.
