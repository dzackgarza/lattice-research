# GOAL_EXPANSION: Task Backlog and Prerequisites

## Source: GOAL_INGEST memory (mem_1ylxxqvfCNs)

## Expanded Goal Items

### G1 - Coble Curves and Picard Lattices

#### G1.1: Explicit Sextic Equation

- **Mathematical question**: Given 10 points in P^2 in general position for a Coble
  configuration, find the sextic F(x,y,z) vanishing to order 2 at each point
- **Prerequisites**: Specific point configuration (Steiner sextic or equivalent)
- **Ambiguity**: Needs concrete coordinate choice for the 10 points
- **Deliverable**: Explicit polynomial F(x,y,z) + K3 cover equation w^2 = F
- **Risk**: Medium - requires solving overdetermined system

#### G1.2: Gram Matrices and Invariants

- **Mathematical question**: Verify S_Co ≅ <2> ⊕ <-2>^10 and compute T_Co = S_Co^⊥ in
  Λ_K3
- **Prerequisites**: coble_geometry_foundation.sage constructors
- **Status**: T-0001 exists with implementation scripts, but foundation library missing
- **Deliverable**: Verified (r,a,δ) invariants, discriminant forms, genus check
- **Risk**: Low - straightforward exact computation

#### G1.3: Primitive Embedding Matrices

- **Mathematical question**: Find explicit integer matrices for T_Co → T_En → T_dP →
  Λ_K3
- **Prerequisites**: G1.2 (Gram matrices), lattice embedding algorithms
- **Deliverable**: Explicit embedding matrices with primitivity certificates
- **Risk**: Medium - requires Nikulin embedding theory implementation
- **ADDENDUM**: This is exactly what Oscar.jl `primitive_embeddings` does.
  See `/home/dzack/research/theory/oscar_lattices.md` → "Primitive embeddings and
  extensions". Do NOT implement Nikulin theory from scratch.

### G2 - Isotropic Orbit Enumeration

#### G2.1: Orbit Enumeration in A_T

- **Mathematical question**: Enumerate isotropic vectors in (Z/2Z)^11 under O(q_T)
- **Prerequisites**: G1.2 (discriminant form q_T)
- **Deliverable**: Orbit representatives and orbit sizes
- **Risk**: Low - finite group computation
- **ADDENDUM**: This is exactly what GAP `Orbit`/`Orbits` does.
  See `/home/dzack/research/theory/gap_orbits.md`. Do NOT write custom orbit code.

#### G2.2: Orbit Lifting to T_Co

- **Mathematical question**: Lift isotropic orbits from A_T to T_Co, verify unique
  O*(T)-orbit for div=2
- **Prerequisites**: G2.1, Sterk's lifting theorems
- **Deliverable**: Verification of unique orbit
- **Risk**: Medium - requires Sterk's technique implementation
- **ADDENDUM**: Oscar.jl `image_centralizer_in_Oq` computes the image of the centralizer
  in O(D_L), which is the lifting obstruction.
  See `/home/dzack/research/theory/oscar_lattices.md` → "Lattices with isometry".

### G3 - Uniqueness of 1-Cusps

#### G3.1: Γ_Co Generators

- **Mathematical question**: Compute Stab_O(T_En)(h_Co) ∩ Z_O(T_En)(θ) explicitly
- **Prerequisites**: G1.3 (embedding T_Co → T_En), G5.1 (θ matrix)
- **Ambiguity**: "Minimal set of generators" for infinite group needs definition
- **Deliverable**: Matrix generators for Γ_Co
- **Risk**: High - infinite group computation
- **ADDENDUM**: Oscar.jl `invariant_lattice` and `coinvariant_lattice` compute the
  fixed/coinvariant sublattices under an isometry.
  See `/home/dzack/research/theory/oscar_lattices.md` → "Kernel sublattices".

#### G3.2: Isotropic Plane Orbits

- **Mathematical question**: Enumerate O(T_Co)-orbits of isotropic planes J, compute
  J^⊥/J
- **Prerequisites**: G1.2, G2 (orbit machinery)
- **Deliverable**: Verification that J^⊥/J ≅ A_1^⊕7 for all orbits
- **Risk**: High - requires plane orbit enumeration
- **ADDENDUM**: buildings.sage `building()` computes exactly this—orbits of isotropic
  planes for O(2,n) subgroups.
  See `/home/dzack/research/theory/buildings.md`. Local copy: `buildings.sage`.

### G4 - Coxeter Parabolics

#### G4.1: Subdiagram Search

- **Mathematical question**: Find all maximal parabolic subdiagrams in 10×10 Gram matrix
- **Prerequisites**: G1.2 (S_Co root system)
- **Deliverable**: Complete list of maximal parabolics, verification of unique B̃_7(2)
- **Risk**: Medium - combinatorial search
- **ADDENDUM**: Oscar.jl `vinberg_algorithm` computes the fundamental chamber and simple
  roots for hyperbolic lattices.
  See `/home/dzack/research/theory/oscar_lattices.md` → "Vinberg's algorithm".

### G5 - Involution Matrix

#### G5.1: θ Construction

- **Mathematical question**: Construct 22×22 matrix θ on Λ_K3 with Λ_K3^θ ≅ T_Co,
  Λ_K3^-θ ≅ S_Co
- **Prerequisites**: G1.3 (embedding into Λ_K3)
- **Deliverable**: Explicit θ matrix, eigenspace invariants
- **Risk**: Medium - requires involution construction
- **ADDENDUM**: Oscar.jl `equivariant_primitive_extensions` constructs lattices with
  isometry from (L⁺, +id) ⊕ (L⁻, -id).
  See `/home/dzack/research/theory/oscar_lattices.md` → "Primitive embeddings and
  extensions".

### G6 - Monodromy Invariants

#### G6.1: Surgery Vector Mapping

- **Mathematical question**: Map h_Co to surgery vector ℓ, verify slc stability of B(ℓ)
- **Prerequisites**: G1 (h_Co), G5 (θ action), AEGS23 construction
- **Ambiguity**: slc stability criterion not locally formalized
- **Deliverable**: Mapping + stability verification
- **Risk**: High - depends on external AEGS23 construction
- **ADDENDUM**: Oscar.jl `admissible_equivariant_primitive_extensions` handles
  p-admissible triples and double coset representatives.
  See `/home/dzack/research/theory/oscar_lattices.md` → "Primitive embeddings and
  extensions".

## Task Backlog (Ordered by Prerequisites)

| Priority | Task | Depends On | Type | Risk |
| --- | --- | --- | --- | --- |
| 1 | T-0001: G1.2 Gram matrices | Foundation library | Computation | Low |
| 2 | T-0002: G1.1 Sextic equation | None (but needs point config) | Computation | Medium |
| 3 | T-0003: G1.3 Embedding matrices | T-0001 | Computation | Medium |
| 4 | T-0004: G2.1 Orbit enumeration | T-0001 | Computation | Low |
| 5 | T-0005: G4.1 Coxeter search | T-0001 | Computation | Medium |
| 6 | T-0006: G5.1 θ matrix | T-0003 | Computation | Medium |
| 7 | T-0007: G2.2 Orbit lifting | T-0004 | Computation | Medium |
| 8 | T-0008: G3.1 Γ_Co generators | T-0003, T-0006 | Computation | High |
| 9 | T-0009: G3.2 Plane orbits | T-0007, T-0008 | Computation | High |
| 10 | T-0010: G6.1 Surgery vector | T-0003, T-0006, T-0008 | Conjecture | High |

## Hidden Prerequisites Discovered

1. **coble_geometry_foundation.sage**: Referenced by T-0001 scripts but missing from
   computations/
   - Must be created or located before T-0001 can run
   - Contains S_Co_lattice(), T_Co_lattice(), hyperbolic_plane(), E8_lattice()

2. **Point configuration for G1.1**: No explicit coordinates for 10 nodes
   - Steiner sextic mentioned but not constructed
   - Needs either literature coordinates or explicit construction

3. **slc stability criterion for G6.1**: References AEGS23 B(λ) construction
   - Not locally formalized
   - May require literature review and formalization

## Natural Extensions Identified

1. **CARAT integration**: For finite positive-definite lattice automorphism groups
   - Relevant for G3.1 (Γ_Co generators)
   - CARAT source already present in carat/

2. **Vinberg's algorithm**: For Coxeter diagram computation
   - Present in computations/vinbergs_algorithm/
   - May support G4.1

## Computational Tool Routing

All remaining tasks use specialized tools rather than hand-rolled Sage implementations:

| Task | Goal | Tool | Key Function | Notes |
| --- | --- | --- | --- | --- |
| T-0004 | G2.1 Orbits | GAP | `Orbit`/`Orbits` | Finite group action on (Z/2Z)^11 |
| T-0005 | G4.1 Coxeter | Oscar.jl | `vinberg_algorithm` | Fundamental chamber + simple roots |
| T-0006 | G5.1 θ matrix | Oscar.jl | `equivariant_primitive_extensions` | Lattice with isometry from (L⁺,L⁻) |
| T-0007 | G2.2 Lifting | Oscar.jl | `image_centralizer_in_Oq` | Centralizer image in O(D_L) |
| T-0008 | G3.1 Γ_Co | Oscar.jl | `invariant_lattice`/`coinvariant_lattice` | Fixed/coinvariant under isometry |
| T-0009 | G3.2 Planes | buildings.sage | `building()` | Orbits of isotropic planes for O(2,n) |
| T-0010 | G6.1 Surgery | Oscar.jl | `admissible_equivariant_primitive_extensions` | p-admissible triples |

**Environment notes:**
- Oscar.jl: `~/.julia/juliaup/julia-1.12.5+0.x64.linux.gnu/bin/julia`. Precompilation
  slow (100s+).
- GAP: available via `sage -sh` environment.
- buildings.sage: local copy at `computations/buildings.sage`, theory at
  `theory/buildings.md`.
- G1.3 (T-0003) was completed with Sage kernel method; Oscar.jl `primitive_embeddings`
  is superior but not worth re-doing.

## Computational Tool Routing

All remaining tasks use specialized tools rather than hand-rolled Sage implementations:

| Task | Goal | Tool | Key Function | Notes |
| --- | --- | --- | --- | --- |
| T-0004 | G2.1 Orbits | GAP | `Orbit`/`Orbits` | Finite group action on (Z/2Z)^11 |
| T-0005 | G4.1 Coxeter | Oscar.jl | `vinberg_algorithm` | Fundamental chamber + simple roots |
| T-0006 | G5.1 θ matrix | Oscar.jl | `equivariant_primitive_extensions` | Lattice with isometry from (L⁺,L⁻) |
| T-0007 | G2.2 Lifting | Oscar.jl | `image_centralizer_in_Oq` | Centralizer image in O(D_L) |
| T-0008 | G3.1 Γ_Co | Oscar.jl | `invariant_lattice`/`coinvariant_lattice` | Fixed/coinvariant under isometry |
| T-0009 | G3.2 Planes | buildings.sage | `building()` | Orbits of isotropic planes for O(2,n) |
| T-0010 | G6.1 Surgery | Oscar.jl | `admissible_equivariant_primitive_extensions` | p-admissible triples |

**Environment notes:**
- Oscar.jl: `~/.julia/juliaup/julia-1.12.5+0.x64.linux.gnu/bin/julia`. Precompilation
  slow (100s+).
- GAP: available via `sage -sh` environment.
- buildings.sage: local copy at `computations/buildings.sage`, theory at
  `theory/buildings.md`.
- G1.3 (T-0003) was completed with Sage kernel method; Oscar.jl `primitive_embeddings`
  is superior but not worth re-doing.

## Risk Assessment

- **Low risk**: G1.2, G2.1, G4.1 (finite exact computations)
- **Medium risk**: G1.1, G1.3, G2.2, G5.1 (require nontrivial constructions)
- **High risk**: G3.1, G3.2, G6.1 (infinite groups, external dependencies)
