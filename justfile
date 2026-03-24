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
