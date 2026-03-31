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

gap-test:
    @echo "=== GAP Test ==="
    gap -q scripts/gap_test.g

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
    @echo "=== Running Task 1.1: Sextic Construction ==="
    sage computations/task1_1_sextic.sage

task1_1-all:
    @echo "=== Running Task 1.1 Sextic Suite ==="
    sage computations/task1_1_sextic.sage
    sage computations/task1_1_sextic_example2.sage
    sage computations/task1_1_sextic_example3.sage

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
    @echo "=== Running Task 1.3: Embeddings (fixed) ==="
    sage computations/task1_3_embeddings_fixed.sage

task1_3-primitive:
    @echo "=== Running Task 1.3: Embeddings (primitive) ==="
    sage computations/task1_3_embeddings_primitive.sage

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

task3_1-results:
    @echo "=== Task 3.1 Results ==="
    @cat computations/task3_1_results.txt

# ==============================================================================
# Task 3.2: Isotropic Plane Orbits
# ==============================================================================

task3_2:
    @echo "=== Running Task 3.2: Isotropic Plane Orbits and J⊥/J ==="
    sage computations/task3_2_isotropic_planes_fixed.sage

task3_2-results:
    @echo "=== Task 3.2 Results ==="
    @cat computations/task3_2_results.txt

# ==============================================================================
# Task 4.1: Coxeter Search
# ==============================================================================

task4_1:
    @echo "=== Running Task 4.1: Coxeter Search ==="
    sage computations/task4_1_coxeter_search.sage

# ==============================================================================
# Task 5.1: Primitive Embedding and True Complement Gate
# ==============================================================================

task5_1-primitive:
    @echo "=== Running Task 5.1 primitive/complement gate ==="
    sage computations/task5_1_involution.sage primitive | tee computations/task5_1_primitive_output.txt

task5_1-primitive-results:
    @echo "=== Task 5.1 Primitive Results ==="
    @cat computations/task5_1_primitive_results.txt

task5_1-theta:
    @echo "=== Running Task 5.1 theta verification ==="
    sage computations/task5_1_involution.sage theta | tee computations/task5_1_theta_output.txt

task5_1-theta-results:
    @echo "=== Task 5.1 Theta Results ==="
    @cat computations/task5_1_theta_results.txt

# ==============================================================================
# Task 6.1: Monodromy
# ==============================================================================

task6_1:
    @echo "=== Running Task 6.1: Monodromy ==="
    sage computations/task6_1_monodromy.sage

# ==============================================================================
# Compare Stabilizers
# ==============================================================================

compare-stabilizers:
    @echo "=== Running Stabilizer Comparison ==="
    sage computations/compare_stabilizers.sage

# ==============================================================================
# Run All (excludes heavy GAP computation in task3_2)
# ==============================================================================

run-all:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "=== Running All Tasks ==="
    echo "--- Foundation Tests ---"
    sage -c "import os; os.chdir('computations'); load('test_foundation.sage')"
    echo "--- Task 1.1 ---"
    sage computations/task1_1_sextic.sage
    sage computations/task1_1_sextic_example2.sage
    sage computations/task1_1_sextic_example3.sage
    echo "--- Task 1.2 ---"
    sage computations/task1_2_gram_matrices_fixed.sage
    sage computations/task1_2b_discriminant_forms.sage
    echo "--- Task 1.3 ---"
    sage computations/task1_3_embeddings_fixed.sage
    sage computations/task1_3_embeddings_primitive.sage
    echo "--- Task 2 ---"
    sage computations/task2_1_isotropic_orbits.sage
    sage computations/task2_2_orbit_lift.sage
    echo "--- Task 3.1 ---"
    sage computations/task3_1_stabilizer.sage
    echo "--- Task 4.1 ---"
    sage computations/task4_1_coxeter_search.sage
    echo "--- Task 5.1 ---"
    sage computations/task5_1_involution.sage primitive
    sage computations/task5_1_involution.sage theta
    echo "--- Task 6.1 ---"
    sage computations/task6_1_monodromy.sage
    echo "--- Compare Stabilizers ---"
    sage computations/compare_stabilizers.sage
    echo "=== All Tasks Complete ==="
