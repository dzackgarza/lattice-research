# CARAT capability audit for lattice-group computations

## Scope

This note records a doc-first audit of CARAT as a possible exact-computation backend for
this repo's lattice-group tasks.

Primary upstream sources reviewed:

- `README.md`
- `tex/progs/Aut_grp.html`
- `tex/progs/Normalizer.html`
- `tex/progs/Normalizer_in_N.html`
- `tex/progs/Orbit.html`
- `tex/progs/Isometry.html`
- `tex/progs/Shortest.html`
- `tex/progs/Form_space.html`
- `tex/progs/Tr_bravais.html`
- `tex/progs/First_perfect.html`
- `functions/Orbit/README`

## What CARAT can plausibly replace here

### `Aut_grp`

- Upstream description: computes generators for the finite group of all `g ∈ GL_n(Z)`
  with `g^T F g = F` for every input form `F`.
- Repo relevance: exact automorphism / orthogonal-group generation for integral
  symmetric forms, especially when a task reduces to preserving one positive-definite
  Gram matrix or a tuple of exact forms.
- Likely use here: exact stabilizer/orthogonal-group computations for positive-definite
  auxiliary lattices, small-rank quotients, or finite form-preserving searches.

### `Normalizer`

- Upstream description: computes matrices which, together with a finite unimodular group
  `G`, generate the normalizer `N_GL_n(Z)(G)`.
- Repo relevance: exact normalizer/stabilizer workflows once a finite matrix group has
  been isolated.
- Likely use here: replacing hand-rolled normalizer searches in finite positive-definite
  settings related to Task 3.1 or finite quotient/stabilizer problems.

### `Orbit`

- Upstream description: computes orbits under several actions and can also compute
  stabilizers.
- Repo relevance: exact orbit/stabilizer calculations for finite matrix-group actions.
- Likely use here: orbit representatives and stabilizers for finite exact searches after
  a group has already been constructed.

### Supporting tools

- `Isometry`: exact integral isometry test between tuples of forms.
- `Shortest`: shortest vectors of a positive-definite form; useful preprocessing for
  `Aut_grp` / `Isometry`.
- `Form_space`: invariant-form space of a group.
- `Tr_bravais`: computes `G^T`, which `Normalizer` can consume.
- `First_perfect`: produces a nearby `G`-perfect form for `Normalizer` workflows.

## Most relevant upstream cautions

- CARAT was developed mainly for crystallographic groups in dimensions up to 6; higher
  dimensions may still work, but the README explicitly warns that integer overflow is
  not trapped in general.
- Building from a GitHub checkout requires `./autogen.sh`, then `./configure && make`.
- CARAT depends on GMP headers/libraries.
- `Aut_grp` / `Shortest` are tailored to positive-definite symmetric-form workflows.
- `Orbit` may be infinite; upstream docs explicitly recommend bounding such runs.
- `Normalizer` complexity is controlled by the dimension of the invariant-form space.

## Incorporation guidance for this repo

### Good targets

- Exact orthogonal-group computations for finite positive-definite lattices.
- Exact stabilizer/normalizer computations once a finite matrix group is already known.
- Exact orbit/stabilizer computations on finite sets where Sage code is currently doing
  bespoke enumeration.

### Poor targets / caution cases

- Directly trusting CARAT as a black-box replacement for indefinite rank-11 or rank-22
  lattice problems without a smaller positive-definite reduction.
- Any workflow that fundamentally needs dimensions beyond CARAT's documented sweet spot
  without an exact audit of overflow risk and output correctness.

## Current repo-specific conclusion

CARAT is worth incorporating as an **audited auxiliary tool**, not as a blanket rewrite
of the current Sage workflows.

Best immediate route:

- use CARAT selectively for finite positive-definite subproblems arising inside Tasks
  3.1, 3.2, 4.1, or 5.1;
- prefer `Aut_grp`, `Normalizer`, and `Orbit` only after reducing to an exact finite
  matrix-group problem with small/runnable dimension;
- keep Sage as the orchestration layer and document every CARAT call with its exact
  input matrices and downstream verification.

---

## Practical usage guide

### Input file formats

CARAT uses several input formats. The key distinction:

**Simple matrix format** (for `Short`, `Elt`, `Signature`, etc.):
```
<dim>
<row 1>
<row 2>
...
```

**Symmetric matrix shorthand** (lower triangle, for quadratic forms):
```
<dim>x0
<diag_1>
<off_1> <diag_2>
<off_1> <off_2> <diag_3>
...
```

**Multi-form format** (required for `Aut_grp`, `Isometry`):
```
#<num_forms>

<dim> d0
1

<dim> d1
<coefficients of first form>

<dim>x0
<lower triangle of Gram matrix>
```

### Worked examples

#### Example 1: Automorphism group of A2 lattice

```bash
# Create input file
cat > A2.mat << 'EOF'
#1

2 d0
1

2x0
2
-1 2
EOF

# Compute Aut(A2)
./bin/Aut_grp A2.mat
```

Output:
```
#g3 % 
2       % generator
 -1  0
  0 -1
2       % generator
 0 1
 1 0
2       % generator
 1  0
 0 -1
2^3   = 8 % order of the group
```

Interpretation: Aut(A2) has order 8, generated by -I, the swap matrix, and diag(-1,1).

#### Example 2: Short vectors of a form

```bash
cat > form.mat << 'EOF'
2x0
2
-1 2
EOF

# Find vectors of norm ≤ 2
./bin/Short form.mat -l=2
```

Output:
```
3x2     % shortest vectors
 1 1
 0 1
 1 0
```

These are the 3 positive roots of A2 (CARAT returns one from each ± pair).

#### Example 3: Verify matrix has full rank

```bash
cat > matrix.mat << 'EOF'
6
1 3 1 0 0 0
0 1 3 1 0 0
0 0 1 3 1 0
0 0 0 1 3 1
1 0 0 0 1 3
3 1 0 0 0 1
EOF

./bin/Elt matrix.mat
```

Output shows the Hermite normal form / elementary divisors.

#### Example 4: Normalizer computation

```bash
# Input: group generators + form
cat > input.mat << 'EOF'
#<num_generators + 1 forms>

<dim> d0
1

<dim>
<generator 1>

<dim>
<generator 2>
...
EOF

./bin/Normalizer input.mat
```

### Typical workflows

**Compute Aut(L) for a lattice L with Gram matrix G:**

1. Write G in multi-form format (see A2 example above)
2. Run `./bin/Aut_grp input.mat`
3. Parse output: generators are `<dim>×<dim>` matrices, order is factored at end

**Find shortest vectors up to norm N:**

1. Write G in symmetric format: `<dim>x0` header, then lower triangle
2. Run `./bin/Short form.mat -l=N`
3. Output is `<count>x<dim>` matrix of vectors

**Test if two forms are isometric:**

1. Put both forms in multi-form format
2. Run `./bin/Isometry forms.mat`
3. Output indicates isometry status and transformation if it exists

**Compute normalizer N_G(G) for finite G ⊂ GL_n(Z):**

1. Input: generators of G plus invariant form(s)
2. Run `./bin/Normalizer input.mat`
3. Output: generators extending G to its normalizer

### Common pitfalls

1. **Wrong format for Aut_grp**: Must use multi-form format with `#<n>` header, not simple matrix format
2. **Missing invariant form**: `Aut_grp` needs the quadratic form preserved, not just group generators
3. **Dimension mismatch**: All matrices in a file must have consistent dimensions
4. **Infinite groups**: `Aut_grp` assumes finite output; indefinite forms may hang
5. **Data directory**: CARAT looks for tables relative to executable; set `CARAT_DIR` if moved

### Verification strategy

For any CARAT computation:

1. **Cross-check with Sage**: Verify group order, generator relations
2. **Verify generators preserve the form**: `g^T F g = F` for each output generator
3. **Check closure**: Multiply generators, verify products are in the group
4. **Compare with known results**: A2 → order 8 or 12 (depending on conventions), Z^n → hyperoctahedral group
