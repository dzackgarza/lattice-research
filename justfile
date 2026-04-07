# Coble Moduli Project - Computational Verification
# Requires: sage, gap, z3 (via uv)

export PYTHONPATH := "."
export SAGE_PYTEST := "1"

# Show available recipes
default:
    @just --list

uv-setup:
    @echo "Setting up uv environment..."
    uv sync

[private]
_clean:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    find . -path './.worktrees' -prune -o -type f -name '*.orig' -exec rm -f {} +
    find . -path './.worktrees' -prune -o -type f -name '*.sage.py' -exec rm -f {} +

# ==============================================================================
# Foundation Library
# ==============================================================================

test:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just _clean
    export PYTHONPATH="."
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _normalize
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _no-bypass
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _coverage
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _diff-cover
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _vulture
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _deptry
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _semgrep
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _ast-grep
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _jscpd
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _lizard
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _import-linter
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _codeql
    export PYTHONPATH=".:/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages"
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _slop
    export PYTHONPATH="."
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} _grain
    just _clean

test-ci:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just test
