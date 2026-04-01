# Coble Moduli Project - Computational Verification
# Requires: sage, gap, z3 (via uv)

export PYTHONPATH := "."

# Show available recipes
default:
    @just --list

sage-test:
    @echo "=== SageMath Test ==="
    sage --version
    sage -c "Q = QuadraticForm(ZZ, 3, [1,2,3,4,5,6]); print('Quadratic form created'); print('Signature:', Q.signature())"

z3-test:
    @echo "=== Z3 Test ==="
    uv run python3 -c "import z3; print('Z3 version:', z3.get_version_string()); s = z3.Solver(); s.add(z3.Bool('x')); print('SAT check:', s.check())"

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
# Task 1.1: Sextic Constructions
# ==============================================================================

task1_1:
    @echo "=== Task 1.1: Sextic Construction — PURGED, awaiting rewrite ==="
    @echo "Scripts deleted: zero assertions, undefined utility functions."
    @exit 1

# ==============================================================================
# Task 1.2: Gram Matrices
# ==============================================================================

task1_2:
    @echo "=== Running Task 1.2: Gram Matrices ==="
    sage computations/task1_2_gram_matrices_fixed.sage

task1_2b:
    @echo "=== Running Task 1.2b: Discriminant Forms ==="
    sage computations/task1_2b_discriminant_forms.sage

# ==============================================================================
# Task 1.3: Embeddings
# ==============================================================================

task1_3:
    @echo "=== Task 1.3: Embeddings — PURGED, awaiting rewrite ==="
    @echo "Scripts deleted: zero assertions, wrong API calls."
    @exit 1

# ==============================================================================
# Task 2: Isotropic Orbits
# ==============================================================================

task2_1:
    @echo "=== Running Task 2.1: Isotropic Orbits ==="
    sage computations/task2_1_isotropic_orbits.sage

task2_2:
    @echo "=== Running Task 2.2: Orbit Lift ==="
    sage computations/task2_2_orbit_lift.sage

# ==============================================================================
# Task 3.1: Γ_Co Stabilizer Computation
# ==============================================================================

task3_1:
    @echo "=== Running Task 3.1: Γ_Co Stabilizer Computation ==="
    sage computations/task3_1_stabilizer.sage

# ==============================================================================
# Task 3.2: Isotropic Plane Orbits
# ==============================================================================

task3_2:
    @echo "=== Running Task 3.2: Isotropic Plane Orbits and J⊥/J ==="
    sage computations/task3_2_isotropic_planes_fixed.sage

# ==============================================================================
# Task 4.1: Coxeter Search
# ==============================================================================

task4_1:
    @echo "=== Task 4.1: Coxeter Search — PURGED, awaiting rewrite ==="
    @echo "Script task4_1_coxeter_search.sage was deleted (fabricated diagram)."
    @exit 1

# ==============================================================================
# Task 5.1: Primitive Embedding and True Complement Gate
# ==============================================================================

task5_1-primitive:
    @echo "=== Running Task 5.1 primitive/complement gate ==="
    sage computations/task5_1_involution.sage primitive

task5_1-theta:
    @echo "=== Running Task 5.1 theta verification ==="
    sage computations/task5_1_involution.sage theta

# ==============================================================================
# Task 6.1: Monodromy
# ==============================================================================

task6_1:
    @echo "=== Task 6.1: Monodromy — PURGED, awaiting rewrite ==="
    @echo "Script task6_1_monodromy.sage was deleted (inadequate)."
    @exit 1

# ==============================================================================
# Run All (excludes heavy GAP computation in task3_2)
# ==============================================================================

run-all:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "=== Running All Tasks ==="
    echo "--- Foundation Tests ---"
    sage -c "import os; os.chdir('computations'); load('test_foundation.sage')"
    echo "--- Task 1.2 ---"
    sage computations/task1_2_gram_matrices_fixed.sage
    sage computations/task1_2b_discriminant_forms.sage
    echo "--- Task 2 ---"
    sage computations/task2_1_isotropic_orbits.sage
    sage computations/task2_2_orbit_lift.sage
    echo "--- Task 3.1 ---"
    sage computations/task3_1_stabilizer.sage
    echo "--- Task 5.1 ---"
    sage computations/task5_1_involution.sage primitive
    sage computations/task5_1_involution.sage theta
    echo "=== All Tasks Complete ==="
