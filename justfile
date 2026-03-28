# Coble Moduli Project - Computational Verification
# Requires: sage, gap, z3 (via uv)

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
# Task 3.1: Γ_Co Stabilizer Computation
# ==============================================================================

task3_1:
    @echo "=== Running Task 3.1: Γ_Co Stabilizer Computation ==="
    sage computations/task3_1_stabilizer.sage

task3_1-results:
    @echo "=== Task 3.1 Results ==="
    @cat computations/task3_1_results.txt

task3_1-output:
    @echo "=== Task 3.1 Output ==="
    @cat computations/task3_1_output.txt

# ==============================================================================
# Task 3.2: Isotropic Plane Orbits
# ==============================================================================

task3_2:
    @echo "=== Running Task 3.2: Isotropic Plane Orbits and J⊥/J ==="
    sage computations/task3_2_isotropic_planes.sage

task3_2-results:
    @echo "=== Task 3.2 Results ==="
    @cat computations/task3_2_results.txt

# ==============================================================================
# Task 5.1: Primitive Embedding and True Complement Gate
# ==============================================================================

task5_1-primitive:
    @echo "=== Running Task 5.1 primitive/complement gate ==="
    PYTHONPATH=. sage computations/task5_1_involution.sage | tee computations/task5_1_primitive_output.txt

task5_1-primitive-results:
    @echo "=== Task 5.1 Primitive Results ==="
    @cat computations/task5_1_primitive_results.txt

# Run all tasks
task1_1-all:
    @echo "=== Running Task 1.1 Sextic Suite ==="
    PYTHONPATH=. sage computations/task1_1_sextic.sage
    PYTHONPATH=. sage computations/task1_1_sextic_example2.sage
    PYTHONPATH=. sage computations/task1_1_sextic_example3.sage

run-all:
    @echo "=== Running All Tasks ==="
    PYTHONPATH=. sage computations/task1_1_sextic.sage
    PYTHONPATH=. sage computations/task1_3_embeddings_fixed.sage
    PYTHONPATH=. sage computations/task2_1_isotropic_orbits.sage
    PYTHONPATH=. sage computations/task2_2_orbit_lift.sage
    PYTHONPATH=. sage computations/task3_1_stabilizer.sage
    PYTHONPATH=. sage computations/task3_2_isotropic_planes.sage
    PYTHONPATH=. sage computations/task5_1_involution.sage
    @echo "=== All Tasks Complete ==="
