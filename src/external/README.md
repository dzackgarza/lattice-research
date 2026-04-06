# src/external

Vendored third-party binaries used by the research codebase.
This directory is excluded from repo quality-control checks.

## bin/ — polyhedral_common indefinite-form binaries

The `bin/` directory contains compiled C++ binaries from
[MathieuDutSik/polyhedral_common](https://github.com/MathieuDutSik/polyhedral_common),
specifically the `src_indefinite` subdirectory.  These implement exact
integral equivalence and automorphism-group algorithms for indefinite
quadratic forms over **Z**.

Binaries present:

| Binary | Purpose |
|---|---|
| `INDEF_FORM_TestEquivalence` | Test whether two indefinite forms are integrally equivalent; returns witness matrix |
| `INDEF_FORM_AutomorphismGroup` | Compute generators of the automorphism group |
| `INDEF_FORM_GetOrbitRepresentative` | Orbit representatives of vectors of a given norm |
| `INDEF_FORM_GetOrbit_IsotropicKplane` | Orbits of isotropic k-planes / k-flags |

These binaries are called directly by `src/research/isometry_backend.py`
(general indefinite branch) via subprocess with the `PYTHON` output mode,
which writes results as Python literals.

---

## Rebuilding the binaries

The binaries are statically linked against GMP/GMP++ and Boost.serialization,
and dynamically linked against libnauty.  To rebuild from source:

### 1. Prerequisites

```sh
sudo apt-get install -y \
    g++ make cmake \
    libeigen3-dev \
    libboost-serialization-dev \
    libgmp-dev libgmpxx4ldbl
```

### 2. Clone polyhedral_common

```sh
git clone --recursive https://github.com/MathieuDutSik/polyhedral_common
cd polyhedral_common
```

### 3. Build Mathieu's nauty fork (required version)

The `src_indefinite` code requires nauty ≤ 2.8.9 (API incompatibility with 2.9+).

```sh
git clone --depth=1 --branch 2.8.9 https://github.com/MathieuDutSik/nauty /tmp/nauty-mathieu
cd /tmp/nauty-mathieu
CC=/usr/bin/gcc ./configure --prefix=/tmp/nauty-install
make -j4
make install
```

### 4. Build the indefinite binaries

```sh
cd polyhedral_common/src_indefinite
make \
    GMP_INCDIR=/usr/include/x86_64-linux-gnu \
    GMP_CXX_LINK="-lgmp -lgmpxx" \
    BOOST_INCDIR=/usr/include \
    BOOST_LINK="-lboost_serialization" \
    EIGEN_PATH=/usr/include/eigen3 \
    NAUTY_INCLUDE="-I/tmp/nauty-install/include" \
    NAUTY_LINK="/tmp/nauty-install/lib/libnauty.a" \
    INDEF_FORM_TestEquivalence \
    INDEF_FORM_AutomorphismGroup \
    INDEF_FORM_GetOrbitRepresentative \
    INDEF_FORM_GetOrbit_IsotropicKplane
```

### 5. Copy into repo

```sh
cp INDEF_FORM_TestEquivalence \
   INDEF_FORM_AutomorphismGroup \
   INDEF_FORM_GetOrbitRepresentative \
   INDEF_FORM_GetOrbit_IsotropicKplane \
   /path/to/research/src/external/bin/
```

### Notes

- The `CMakeLists.txt` in polyhedral_common requires MPI (for parallel
  variants), which is not needed for the indefinite binaries.  Use `make`
  directly in `src_indefinite/` as shown above to avoid that dependency.
- On systems where the conda/miniforge gcc appears before the system gcc on
  `PATH`, pass `CC=/usr/bin/gcc CXX=/usr/bin/g++` to all build steps.
- Compilation takes ~30 minutes on a single core (heavy C++20 template
  instantiation).  Use `make -j$(nproc)` if you have cores to spare.
