# Subgraph orbits under Aut(G)

**Problem:** Given graph G with automorphism group Aut(G), enumerate subgraphs up to isomorphism (orbits under Aut(G) action).

**Key insight:** This is the quotient of the subgraph poset by Aut(G).

---

## GAP: GRAPE package

### Complete subgraphs with orbit representatives

```gap
LoadPackage("grape");

gamma := Graph(...);  # Your graph with gamma.group ≤ Aut(gamma)

# Maximal complete subgraphs (one per orbit)
cliques := CompleteSubgraphs(gamma, -1, 0);
# alls=0: one representative per Aut(gamma)-orbit

# All complete subgraphs of size k (one per orbit)
cliques_k := CompleteSubgraphs(gamma, k, 0);

# All complete subgraphs of size k (full orbit data)
cliques_k_full := CompleteSubgraphs(gamma, k, 2);
# Returns record with:
#   .reps: orbit representatives
#   .sizes: orbit sizes
#   .stabs: stabilizer orders
```

### Vertex-weighted complete subgraphs

```gap
# Vertex weights
wts := [1, 2, 1, 3, 2, ...];

# Complete subgraphs with total vertex weight = k
cliques_weighted := CompleteSubgraphsOfGivenSize(gamma, k, 0, false, true, wts);
# alls=0: orbit reps
# maxi=false: not just maximal
# col=true: use coloring optimization
# wts: vertex weights
```

### Independent sets (via complement)

```gap
# Independent sets = cliques in complement
gamma_complement := ComplementGraph(gamma);
indsets := CompleteSubgraphs(gamma_complement, k, 0);
```

---

## General subgraph orbits

### Method: Canonical labeling + hashing

```gap
LoadPackage("grape");
LoadPackage("digraphs");

gamma := Graph(...);
aut := AutomorphismGroup(gamma);
verts := Vertices(gamma);
n := Length(verts);

# Enumerate k-vertex subgraphs by orbit
k := 4;
orbit_reps := [];
seen_canons := [];

for subset in Combinations(verts, k) do
    # Compute canonical form of induced subgraph
    sub := InducedSubgraph(gamma, subset);
    adj := AdjacencyMatrix(sub);
    dig := Digraph(adj);
    canon := BlissCanonicalLabelling(dig);
    
    # Check if we've seen this isomorphism type
    if not canon in seen_canons then
        Add(seen_canons, canon);
        Add(orbit_reps, subset);
    fi;
od;

# orbit_reps: one representative per isomorphism class
Length(orbit_reps);  # Number of non-isomorphic k-vertex subgraphs
```

### Method: Orbits under explicit group action

```gap
# If you have explicit Aut(gamma) generators
aut := AutomorphismGroup(gamma);

# All k-subsets
subsets := Combinations(verts, k);

# Orbits under Aut(gamma)
orbits := Orbits(aut, subsets, OnSets);

# Representatives
reps := List(orbits, o -> o[1]);

# Orbit sizes
sizes := List(orbits, Length);

# Total count (with multiplicity)
Sum(sizes);  # = Binomial(n, k)
```

---

## Quotient poset structure

The quotient poset P/Aut(G) has:
- **Elements:** Orbits [H] of subgraphs H ⊆ G
- **Order:** [H] ≤ [K] iff ∃g ∈ Aut(G) with H ⊆ g·K

### Computing cover relations

```gap
# For each pair of orbit reps, check if one embeds in orbit of other
IsSubgraphOfOrbit := function(gamma, aut, S1, S2)
    # Does S1 embed into some g·S2 for g ∈ aut?
    for g in aut do
        S2_image := OnSets(S2, g);
        if IsSubset(S2_image, S1) then
            return true;
        fi;
    od;
    return false;
end;

# Cover relations in quotient poset
covers := [];
for i in [1..Length(reps)] do
    for j in [1..Length(reps)] do
        if Length(reps[i]) = Length(reps[j]) - 1 then
            if IsSubgraphOfOrbit(gamma, aut, reps[i], reps[j]) then
                Add(covers, [i, j]);
            fi;
        fi;
    od;
od;
```

---

## Efficient enumeration by isomorphism type

### Using nauty directly (via GRAPE)

```gap
LoadPackage("grape");

# GRAPE uses nauty internally for canonical labeling
# Set information records for orbit computation

gamma := Graph(...);

# Compute complete subgraphs with full orbit info
result := CompleteSubgraphs(gamma, k, 2);

# Access orbit data
reps := result.representatives;  # Orbit reps
sizes := result.orbit_sizes;     # Size of each orbit
stabs := result.stabilizer_sizes; # Stabilizer order

# Verify orbit-stabilizer: |orbit| × |stab| = |Aut(gamma)|
for i in [1..Length(reps)] do
    Print("Orbit ", i, ": size ", sizes[i], 
          ", stab size ", stabs[i], "\n");
od;
```

### Using bliss canonical forms (Digraphs package)

```gap
LoadPackage("digraphs");

# For each subgraph, compute canonical form
# Two subgraphs are in same orbit iff same canonical form

CanonicalForm := function(gamma, subset)
    sub := InducedSubgraph(gamma, subset);
    adj := AdjacencyMatrix(sub);
    dig := Digraph(adj);
    return BlissCanonicalLabelling(dig);
end;

# Group subgraphs by canonical form
canon_to_reps := [];
for subset in Combinations(verts, k) do
    canon := CanonicalForm(gamma, subset);
    if not canon in canon_to_reps then
        canon_to_reps[canon] := [subset];
    else
        Add(canon_to_reps[canon], subset);
    fi;
od;

# Each entry: list of subsets in same orbit
orbit_lists := Values(canon_to_reps);
Length(orbit_lists);  # Number of orbits
```

---

## Complete example: Petersen graph 4-vertex subgraphs

```gap
LoadPackage("grape");
LoadPackage("digraphs");

# Petersen graph
gamma := PetersenGraph();
aut := AutomorphismGroup(gamma);
verts := Vertices(gamma);

k := 4;
subsets := Combinations(verts, k);
Print("Total subsets: ", Length(subsets), "\n");  # 210

# Compute orbits
orbits := Orbits(aut, subsets, OnSets);
Print("Number of orbits: ", Length(orbits), "\n");  # e.g., 6

# Display orbit structure
for i in [1..Length(orbits)] do
    rep := orbits[i][1];
    sub := InducedSubgraph(gamma, rep);
    
    # Compute invariants
    deg_seq := SortedList(List(rep, v -> VertexDegree(gamma, v)));
    edges := Size(Edges(sub));
    
    Print("Orbit ", i, ": size ", Length(orbits[i]), 
          ", rep: ", rep,
          ", deg seq: ", deg_seq,
          ", edges: ", edges, "\n");
od;

# Classify by isomorphism type (canonical form)
canon_types := [];
for orbit in orbits do
    rep := orbit[1];
    sub := InducedSubgraph(gamma, rep);
    adj := AdjacencyMatrix(sub);
    dig := Digraph(adj);
    canon := BlissCanonicalLabelling(dig);
    
    if not canon in canon_types then
        Add(canon_types, canon);
    fi;
od;
Print("Isomorphism types: ", Length(canon_types), "\n");
```

---

## Summary

| Function | Purpose |
|----------|---------|
| `CompleteSubgraphs(gamma, k, 0)` | k-cliques, one per orbit |
| `CompleteSubgraphs(gamma, k, 2)` | k-cliques with full orbit data |
| `CompleteSubgraphsOfGivenSize(..., wts)` | Weighted cliques |
| `Orbits(aut, subsets, OnSets)` | General subgraph orbits |
| `BlissCanonicalLabelling(dig)` | Canonical form for isomorphism test |
| `RepresentativeAction(aut, S1, S2, OnSets)` | Test if S1, S2 in same orbit |

**Workflow:**
1. For cliques: `CompleteSubgraphs(gamma, k, 0)` gives orbit reps directly
2. For general subgraphs: `Orbits(aut, Combinations(verts, k), OnSets)`
3. For isomorphism classification: `BlissCanonicalLabelling`
4. Quotient poset: orbit reps with inclusion check via `RepresentativeAction`
