# Coble Moduli Project - Computational Verification
# Requires: sage, gap, z3 (via uv)

export PYTHONPATH := "."

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
    find . -path './.worktrees' -prune -o -type f -name '*.sage.py' -exec rm -f {} +
    find . -path './.worktrees' -prune -o -type f -name '*.orig' -exec rm -f {} +

# ==============================================================================
# Foundation Library
# ==============================================================================

test:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just _clean
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} test
    just _clean

test-ci:
    #!/usr/bin/env bash
    set -euo pipefail
    cd {{justfile_directory()}}
    just _clean
    just -f /home/dzack/ai/quality-control/justfile -d {{justfile_directory()}} test-ci
