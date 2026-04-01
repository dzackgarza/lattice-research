# Coble Moduli Project - Computational Verification
# Requires: sage, gap, z3 (via uv)

export PYTHONPATH := "."

# Show available recipes
default:
    @just --list

uv-setup:
    @echo "Setting up uv environment..."
    uv sync

# ==============================================================================
# Foundation Library
# ==============================================================================

test-foundation:
    @echo "=== Running Foundation Tests ==="
    sage -c "import os; os.chdir('computations'); load('test_foundation.sage')"


# ==============================================================================
# Run All (Do not exclude heavy computations)
# NOTE: NEVER hard-code running individual tests. All or nothing.
# ==============================================================================

test:
    #!/usr/bin/env bash
    # TODO: run basic quality gates/audits and fail fast
    set -euo pipefail
    echo "=== Running All Tasks ==="
    echo "--- Foundation Tests ---"
    sage -c "import os; os.chdir('computations'); load('test_foundation.sage')"
    # TODO: Glob and run all sage files in the computations dir
    # TODO: Clean up all sage compilation/parsing debris
    echo "=== All Tasks Complete ==="
