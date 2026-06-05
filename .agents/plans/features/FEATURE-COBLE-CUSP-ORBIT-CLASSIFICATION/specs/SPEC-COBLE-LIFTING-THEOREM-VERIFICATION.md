---
id: SPEC-COBLE-LIFTING-THEOREM-VERIFICATION
trackerStatus:
  type: spec
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]'
- '[[SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION]]'
- '[[DECISION-TCO-DEFINITION-AND-SIGNATURE]]'
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
title: Verify Nikulin 1.5.2 and Eichler criterion for lattice T_Co
status: unstarted
priority: medium
requirement: The Coble cusp workflow must verify the theorem hypotheses needed to lift discriminant-form isotropic orbits to primitive isotropic vector orbits in T_Co.
acceptanceCriteria:
- A durable theory note records the exact Nikulin and Eichler statements, their hypotheses, and whether they apply to the computed Coble lattice.
- Any orbit-lifting conclusion states the required group, divisibility, discriminant class, and remaining blockers without relying on notation alone.
complexity: 35
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Spec: Verify Nikulin surjectivity and orbit lifting for T_Co

## Summary

The isotropic orbit analysis asks when finite `O(q_T)`-orbits in `A_{T_Co}` determine
orbits of primitive isotropic vectors in `T_Co`.  This is not a single theorem.

The source-backed part now established for the Dolgachev-Kondo standard Coble target is:

```text
N = <2> + E_10(2)
```

Dolgachev-Kondo identify the K3 orthogonal complement `N_X` with this lattice and state
that it is two-elementary of signature `(2,9)` with `q_N=-q_M`.  Nikulin's Theorem
3.6.3 then gives surjectivity

```text
O(N) -> O(q_N).
```

The remaining lifting problem is not this surjectivity statement.  The remaining problem
is to identify the geometrically computed `T_Co=(f^*Pic(S))^\perp` with `N`, compute the
primitive-vector divisibility and finite discriminant-form orbits from that construction,
and state the subgroup of `O(T_Co)` whose primitive-isotropic orbit is being asserted.

For the standard target, the primitive-vector divisibility is also determined:

```text
N = <2> + E_10(2) = 2(<1> + E_10).
```

With the repo convention `E_10=U+E_8(-1)`, the lattice `<1>+E_10` is unimodular.
Therefore a primitive vector `v in N` pairs with `N` in the ideal `2Z`, so
`div_N(v)=2`.  This proves the divisibility claim for the standard target; the project
pipeline may use it for `T_Co` only after the construction or accepted isometry witness
identifies the computed Coble lattice with `N`.

## Hypothesis check

For the standard target `N=<2>+E_10(2)`, the following hypotheses are source-backed:

- rank `11` and signature `(2,9)`;
- even and indefinite;
- two-elementary discriminant group, inherited from the K3 complement statement
  `q_N=-q_M` where `A_M=(Z/2Z)^11`;
- discriminant form `q_N : A_N -> Q/2Z`.

Therefore Nikulin Theorem 3.6.3 applies to the standard target: `O(N)->O(q_N)` is
surjective.

This does not yet prove the desired Coble primitive-isotropic orbit statement.  The
following hypotheses or witness data are still required:

- the project construction of `T_Co=(f^*Pic(S))^\perp <= Lambda_K3`, or an accepted
  isometry witness from that construction to `N`;
- the divisibility of the primitive isotropic vectors under the actual Gram model, which
  is `2` for the standard target `N` and transfers to `T_Co` only through the
  construction/isometry witness;
- the finite orbit structure in `Iso(A_T,q_T)`; for the standard target, exact
  computation in `B/2B` for `N=2(<1>+U+E_8(-1))` gives `528` isotropic classes and
  full-group orbit sizes `[1, 527]` under `O(A_N,q_N)`;
- the subgroup of `O(T_Co)` used in the Coble quotient, e.g. full `O(T_Co)`, stable
  kernel, real-spinor subgroup, stabilizer, or centralizer;
- an Eichler criterion check such as a verified `2U` hypothesis, or a different
  primitive-isotropic orbit theorem/backend for the subgroup actually used.

## Questions

- For the standard target `N=<2>+E_10(2)`, Nikulin surjectivity for
  `O(N)->O(q_N)` is answered yes by Theorem 3.6.3.
- For the geometrically computed project lattice `T_Co`, the same conclusion is
  available only after the construction or isometry witness identifies it with `N`.
- For the standard target `N`, every primitive vector has divisibility `2`, because
  `N=2B` for the unimodular lattice `B=<1>+E_10`.
- For the standard target, `Iso(A_N,q_N)` has `528` elements, including the zero class,
  and full `O(A_N,q_N)` has two orbits on it: the zero class and one orbit of the `527`
  nonzero isotropic classes.
- Surjectivity of the full orthogonal group does not decide stable-kernel,
  real-spinor, stabilizer, centralizer, or Coble arithmetic-subgroup orbits.  Each such
  subgroup requires its own image or orbit theorem.
- The Eichler criterion is not yet verified for the Coble claim.  The card must check
  the required hyperbolic summand hypothesis, or name another theorem/backend for
  primitive isotropic vectors of the computed divisibility.
- A bijection between finite isotropic classes in `A_T` and primitive isotropic lattice
  orbits is not admitted from finite enumeration alone.  It requires the representative
  existence, divisibility, and subgroup/kernel-action statements above.

## Output

A theory note under `theory/foundations/` recording:
- The relevant theorem statements
- The verification (or blocking issues) for T_Co
- The orbit-count prediction and its theoretical basis
- The distinction between full `O(T_Co)` surjectivity and any stable, spinor, stabilizer,
  centralizer, or Coble arithmetic-subgroup orbit claim

## Dependency Status

This is not a human deferral decision.  The full primitive-isotropic orbit conclusion
cannot proceed until the Coble lattice construction/isometry, finite discriminant-form
orbit enumeration, subgroup choice, and active mathematical vocabulary are available
through the repo's typed category/lattice definitions.  Keep this spec `unstarted` under
its declared dependencies rather than asking for human input to bypass the phase order.

The theorem sourcing above is still valid prerequisite information: it answers the
full-orthogonal-group surjectivity question for the standard target, but it does not
discharge the downstream orbit-lifting conclusion.

## Source Evidence

- `theory/references/literature/dolgachev_kondo_2013.md:97-101`: the Coble K3
  orthogonal complement is two-elementary of signature `(2,9)`, has `q_N=-q_M`, and is
  isomorphic to `N=<2>+E(2)`.
- `.agents/plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/decisions/DECISION-TCO-DEFINITION-AND-SIGNATURE.md:40-43`:
  the project convention rewrites the target as `<2>+U(2)+E_8(-2)` using
  `E_10=U+E_8(-1)`.
- `theory/references/literature/nikulin1979integral.md:1595-1597`: for an even
  indefinite two-elementary lattice `S`, the homomorphism `O(S)->O(q_S)` is surjective.
- `theory/foundations/reflective-two-elementary-lattices.md:372-385`: Eichler criterion
  source used only under its stated hyperbolic-summand and subgroup hypotheses.
- `theory/foundations/coble-standard-target-discriminant-form.md`: exact enumeration of
  the standard-target finite discriminant form gives `528` isotropic classes in `A_N`
  and full standard-target orbit sizes `[1, 527]`.
- `theory/computations/coble_standard_target_discriminant_orbits.sage`: exact
  GAP/Sage witness computing `O(A_N,q_N)` as the stabilizer of the four
  `Q(v)=B(v,v) mod 4` fibers in `GL(B/2B)`.

## Non-Evidence

`lean/CobleResearchLean/IsotropicPlanes.lean` is not an implementation witness for the
Coble primitive-plane or lifting claim.  It cites
`computations/task3_2_isotropic_planes.sage`, but a repo-wide search found no file with
that name and the repository has no `computations/` directory.  It also presents
`T_Co` by the diagonal form `diag(2,2,-2,...,-2)`, while the sourced
Dolgachev-Kondo target recorded here is `N=<2>+E_10(2)`.

Therefore that Lean file may be treated only as an unresolved formalization draft until
the missing computation witness is supplied and the lattice presentation is reconciled
with the sourced Coble target.

## Historical Review Log

The review below predates the source evidence recorded above.  It remains a record of
the earlier card state, not the current mathematical status.  The current mathematical
status is: Nikulin full-orthogonal-group surjectivity is sourced for the
Dolgachev-Kondo standard target, standard-target primitive-vector divisibility is `2`,
and full standard-target finite discriminant-form orbits have sizes `[1, 527]`.  The
Coble construction/isometry, subgroup image, and Eichler/backend lattice-lifting
obligations remain unresolved.

### Review 2026-05-07 (6-Gate Spec Review)

**Gates passed:** G1, G2
**Gates not passed:** G3, G4, G5, G6
**Outcome:** DO NOT PROMOTE — research work not executed; two prerequisite specs unreviewed

---

### Gate 1: Card Structure Correctness

| Check | Status | Evidence |
|---|---|---|
| Frontmatter valid YAML | PASS | `id`, `trackerStatus.type: spec`, `parents`, `dependsOn`, `title`, `status`, `priority`, `requirement`, `acceptanceCriteria`, `complexity`, `tags` all present and well-formed |
| `id` matches filename stem | PASS | `SPEC-COBLE-LIFTING-THEOREM-VERIFICATION` matches filename |
| `parents` records containment | PASS | Parent `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` is the owning feature card |
| `dependsOn` records prerequisites | PASS | `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` (provides discriminant-form method surface) and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` (provides orbit-count input) are correctly listed. DAG edges confirmed at `plans/plan-dag.md` lines 849-850 |
| Status reflects actual state | PASS | `needs-human-input` is correct — this is a theorem-verification research card requiring human mathematical investigation of Nikulin and Eichler references |
| Tags present | PASS | `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` tag anchors to owning feature |

**Gate 1 Verdict:** PASS. Card structure follows the planning workspace conventions exactly.

---

### Gate 2: Acceptance Criteria Clarity

| Criterion | Clear? | Measurable? | Assessment |
|---|---|---|---|
| "A durable theory note records the exact Nikulin and Eichler statements, their hypotheses, and whether they apply to the computed Coble lattice" | YES | YES — requires explicit theorem statements with hypothesis verification for T_Co | Well-scoped; T_Co has known properties (rank 11, signature (2,9), 2-elementary discriminant) that make the hypothesis check concrete |
| "Any orbit-lifting conclusion states the required group, divisibility, discriminant class, and remaining blockers without relying on notation alone" | YES | YES — requires explicit group names, numerical divisibility, and blocker enumeration | Critical: forbids hand-waving answers like "the group acts transitively" without specifying which group |

Additional clarity from the spec body:
- The four concrete questions (Nikulin applicability, spinor norm surjectivity, Eichler criterion for divisibility 2, orbit bijection) provide a clear research protocol
- Output destination is explicit: `theory/foundations/`
- The spec identifies exact properties of T_Co to check against theorem hypotheses

**Gate 2 Verdict:** PASS. Acceptance criteria are clear, measurable, and properly scoped. The four research questions form an actionable checklist.

---

### Gate 3: Dependency Resolution

| Dependency | Status | Impact |
|---|---|---|
| `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` | `needs-human-input` (unreviewed) | BLOCKER — this spec specifies the `orthogonal_group()`, `isotropic_orbits()`, and `lift_orbit_to_lattice()` method surfaces on `DiscriminantGroup`. Until these methods exist, the lifting theorem cannot be verified computationally against the concrete Coble discriminant form. The theorem statements themselves can be collected from literature independently, but the *verification against T_Co* requires the computed discriminant form. |
| `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` | `needs-human-input` (reviewed, not passed — G3-G6 not passed) | BLOCKER — this spec provides the orbit-count input needed to check whether the lifting theorem predicts the correct number of primitive isotropic vector orbits. Without knowing how many discriminant-form orbits exist, the lifting conclusion cannot state a specific orbit count. |
| `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` (parent) | `in-progress` | Informational — parent feature is active and this spec is one of its children |
| `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (transitive via feature) | in-progress | The lattice/discriminant-form infrastructure this spec verifies against is still under construction |

DAG edges confirmed at `plans/plan-dag.md`:
```
SPEC_DISCRIMINANT_FORM_ORBIT_SURFACES --> SPEC_COBLE_LIFTING_THEOREM_VERIFICATION  (line 849)
SPEC_COBLE_ISOTROPIC_ORBIT_ENUMERATION --> SPEC_COBLE_LIFTING_THEOREM_VERIFICATION (line 850)
```

Both edges are correct: the lifting theorem verification requires (a) the discriminant-form method surface to be defined so the form can be computed, and (b) the orbit enumeration to be done so the lifting prediction can be checked against actual orbit counts.

**Gate 3 Verdict:** NOT PASSED. Both prerequisite specs are unreviewed/incomplete. The verification cannot proceed against an unspecified method surface and unknown orbit count. This is a genuine dependency block, not a formal one.

---

### Gate 4: Content Quality / Work Completeness

| Deliverable | Present? | Assessment |
|---|---|---|
| Nikulin 1.5.2 statement recording | NO | The spec body mentions "Nikulin 1.5.2 gives conditions under which the map O(L) → O(A_L, q_L) is surjective" but does not state the precise conditions, the theorem's hypotheses, or provide a reference with page/edition. No literature excerpt or translation is recorded. |
| Eichler criterion statement recording | NO | The spec body sketches the Eichler criterion ("for an indefinite lattice of rank ≥ 3, the spinor norm kernel acts transitively on primitive vectors of given divisibility and discriminant class, provided the discriminant class is nonzero") but this is a paraphrase, not a precise statement with hypotheses, domain restrictions, and a verifiable source reference. |
| Hypothesis verification for T_Co | NO | Known properties of T_Co are listed (rank 11, signature (2,9), even, 2-elementary discriminant (Z/2Z)^11), but no verification against Nikulin/Eichler conditions has been performed. The four research questions are posed but unanswered. |
| Spinor norm surjectivity determination | NO | Question posed: "Is the spinor norm surjectivity known for the Coble lattice? Is O(T_Co) → O(A_{T_Co}) surjective, and if not, what is the image?" No computation, literature reference, or determination present. |
| Eichler criterion applicability for divisibility 2 | NO | Question posed: "Does the Eichler criterion apply to vectors of divisibility 2 in T_Co?" No verification present. |
| Orbit bijection conclusion | NO | Question posed: "Are the isotropic orbits in A_{T_Co} in bijection with the O^*(T_Co)-orbits of primitive isotropic vectors with divisibility 2?" No conclusion present; the question itself is well-formed but unanswered. |
| Theory note under `theory/foundations/` | NO | No theory note exists anywhere under the repo. The spec correctly identifies the output destination but no output has been produced. |

The spec body is a well-structured research questionnaire with precisely formulated mathematical questions. The questionnaire has not been answered. The card defines *what* research to do, but no research output exists.

The property list for T_Co (rank 11, signature (2,9), 2-elementary discriminant) is stated without derivation from the geometric construction of the Coble lattice. The spec does not cite a specific source for these lattice invariants (e.g., a computation from the K3 cover or Coble surface construction). The (r, a, δ) Nikulin invariants for T_Co are not stated — this is critical because Nikulin 1.5.2's applicability depends on these invariants.

**Gate 4 Verdict:** NOT PASSED. Research work has not been executed. The card is a valid research spec but contains no research output. None of the four questions are answered. No theory note exists.

---

### Gate 5: Feasibility / Blockers Assessment

| Factor | Assessment |
|---|---|
| Mathematical complexity | High. Nikulin's surjectivity theorem (Prop. 1.5.2) involves spinor norm computations on indefinite lattices, the connecting homomorphism from O(L) to O(A_L, q_L), and delicate conditions on the discriminant form. The Eichler criterion requires understanding of the spinor norm kernel's transitivity on primitive vectors, which depends on the genus of the lattice. For T_Co of signature (2,9), the orthogonal group is an arithmetic group with potentially complicated spinor norm image. |
| Prerequisite dependency | Both `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` must be resolved first. The former defines the method surface for computing the discriminant form; the latter provides the orbit-count baseline to verify against the lifting prediction. |
| Literature accessibility | Nikulin's "Integral symmetric bilinear forms and some of their applications" (Math. USSR Izvestija, 1980) is a standard reference. The Eichler criterion appears in standard lattice-theory texts (e.g., Miranda-Morrison). The mathematical literature is accessible, but the verification requires expert interpretation of Nikulin's conditions for the specific (r,a,δ) invariants of T_Co. |
| Backend requirements | Verifying the lifting theorem computationally requires Sage's `QuadraticForm.automorphism_group()` for the discriminant form and potentially GAP for the orthogonal group structure. These backends are available but the SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES must define the method surface first. |
| Blockers | (1) Both prerequisite specs unreviewed/incomplete. (2) No one has located and excerpted the precise Nikulin 1.5.2 statement with page reference. (3) No one has verified the (r,a,δ) invariants of T_Co against Nikulin's conditions. (4) The Eichler criterion's "discriminant class nonzero" condition has not been checked against the specific isotropic vectors in T_Co. (5) The theory note does not exist. |
| Human input required | YES — this is inherently a research card. Locating and interpreting Nikulin's theorem, computing spinor norm images, and verifying the Eichler criterion against the specific Coble lattice all require expert mathematical work. Automated tools cannot substitute for theorem-verification judgment. |

**Gate 5 Verdict:** NOT PASSED. Genuine blockers exist at multiple levels: dependency, literature verification, and mathematical computation. The card is correctly marked `needs-human-input`.

---

### Gate 6: Readiness for Promotion

| Criterion | Status |
|---|---|
| Acceptance criteria met | NO — no theory note, no theorem statement recording, no hypothesis verification, no orbit-lifting conclusion |
| Dependencies resolved | NO — both `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` are unreviewed/incomplete |
| No blockers from lower gates | NO — Gates 3, 4, 5 all have unresolved issues |
| Card internal consistency | YES — the spec is internally consistent: the four research questions flow logically from the summary through the hypothesis check to the expected output |
| No contradictory claims | N/A — no claims made (research not done) |

**Gate 6 Verdict:** NOT PASSED. The card is not ready for promotion. It is a well-formed research spec awaiting execution.

---

### Overall Assessment

| Gate | Status |
|---|---|
| Gate 1: Card Structure Correctness | PASS |
| Gate 2: Acceptance Criteria Clarity | PASS |
| Gate 3: Dependency Resolution | NOT PASSED — both prerequisite specs unreviewed |
| Gate 4: Content Quality / Work Completeness | NOT PASSED — research not executed; no theory note; no theorem statements recorded |
| Gate 5: Feasibility / Blockers | NOT PASSED — genuine blockers at multiple levels |
| Gate 6: Readiness for Promotion | NOT PASSED |

**Recommendation:** DO NOT PROMOTE. The spec card is well-structured (Gates 1-2 pass) and defines clear, valuable research questions for verifying the Nikulin-Eichler lifting theorem for T_Co. However, the actual research work has not been done. The card's four questions (Nikulin applicability, spinor norm surjectivity, Eichler criterion for divisibility 2, orbit bijection) remain unanswered. Both dependencies (`SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION`) must be resolved before the verification can proceed. No theory note exists under `theory/foundations/`.

**Notable gap beyond the research questions:** The spec's property list for T_Co does not state the Nikulin (r, a, δ) invariants of the Coble lattice. These invariants are essential input to Nikulin 1.5.2's applicability conditions. The spec should either compute or cite a computation of these invariants before the Nikulin hypothesis check can begin.

**Next steps:**
1. Resolve `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` (review/approve) to define the discriminant-form method surface.
2. Resolve `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` (execute the GAP/Sage/Oscar/Burnside survey, record orbit counts).
3. Compute or verify the (r, a, δ) Nikulin invariants for T_Co from the geometric construction.
4. A human researcher must locate the precise Nikulin 1.5.2 statement (with page/edition reference), excerpt it, and verify its hypotheses against the computed T_Co invariants.
5. The same researcher must state the Eichler criterion precisely, verify its conditions for T_Co, and determine whether primitive isotropic vectors of divisibility 2 satisfy the required discriminant-class condition.
6. Produce the orbit-lifting conclusion stating the relevant group (O^*(T_Co) or the spinor norm kernel), the divisibility, the discriminant class, and any remaining blockers.
7. Record all findings in a durable theory note under `theory/foundations/`.
8. After research output is recorded, re-review for promotion.
