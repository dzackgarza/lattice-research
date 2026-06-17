# Execution Roadmap

How this project gets from Sage-backed research to a spec-enforced, provably-correct
lattice DSL — and then to the Coble research results — without drifting into a paperwork
factory.

`GOAL.md` is the mathematical destination (the staged Coble program); this document is
the *execution methodology* and the *order of work*. It does not restate the mathematics
— read `GOAL.md` for that. Read this when planning a workstream, judging whether recent
work was worth it, or onboarding to "how we work and why."

## The corrected pipeline (the one canonical flow)

Every capability the research needs travels exactly this path. No research code is
written ahead of it.

1. **Research need.** A concrete research step (e.g. "compute $\Gamma_{Co}$-orbits of
   isotropic vectors in $T_{Co}$") names a capability it requires.
2. **Spec obligation.** That capability becomes an `@abstractmethod` on the *weakest*
   mathematical category that owns it. The spec declares the contract (operation,
   hypotheses, owner, return object); it never implements, never imports `src/`, never
   carries a `NotImplementedError` body.
3. **Literature test.** A test asserts a *specific value* a cited source guarantees
   (page/theorem/arXiv id in the docstring). It first goes red because the method is
   **missing**, then stays red until the implementation **recovers the cited fact**.
   "Abstractly correct" is not a passing condition; recovering a sourced number is.
4. **Implementation.** Written separately from the spec (impl may import Sage; spec may
   not). Its only job is to make the literature test green.
5. **Expected-failure smoke.** A trivial instantiation of a simple object through a
   category constructor. Current Sage classes satisfy only a fraction of the obligations,
   so most smokes are **supposed to be red**. Each example declares its expected
   disposition:
   - `enforced-and-unmet` → the abstractmethod correctly fires on a correctly-refined
     Sage object that lacks mathematically-required functionality. **This red is a pass.**
   - `graph-broken` / `weakened-spec` / `wrong-category` → a red for the wrong reason.
     **This is a real failure.**
   The harness verifies the *disposition*, not mere green/red. Making an
   `enforced-and-unmet` example green by weakening a spec or bypassing a constructor is
   the cardinal sin.
6. **Promotion gate.** Only after 2–5 hold may the capability be used in research code.
   Research/agent code imports **categories, never Sage directly**; a method reaches the
   research layer only through this gate.

## Why this roadmap exists — the three defects it fixes

Grounded in the 2026-06-17 corpus audit (`reports/2026-06-16-memory-migration-ledger.md`
context; audit findings summarized here):

- **The enforcement engine is inverted.** The smoke-should-fail philosophy lives only as
  human prose; the tooling is binary green/red (`category_specs/justfile` `exit 1`,
  `pipefail`), there are **no `xfail` markers anywhere**, and the *run* obligation tests
  assert source-graph structure (`X is Y.ParentMethods`) with **zero literature
  citations** — while the genuinely cited tests (`tests/variety_spec/*.sage`,
  `tests/fixtures/coble_literature_fixtures.json`) are **not the gate**. Agents feel
  green-at-all-costs pressure and weaken specs to relieve it. This is the engine of the
  thrashing.
- **No import discipline / promotion gate.** `src/**` imports Sage directly throughout;
  nothing forces capabilities through stages 2–5 first, so the DSL is not load-bearing.
- **Process doctrine is scar tissue.** The same anti-drift lesson is restated across 6+
  memories; operational gates (cards, triage, retirement, PR) never re-assert the
  mathematical-object gate, so an agent can satisfy every gate with zero math progress.

## Order of work

Each workstream is a self-limiting state machine with a hard DONE condition. A workstream
is not "done" when its cards are tidy — only when its DONE condition holds.

### WS-4 — This roadmap (current)
DONE when this file is reviewed and adopted as the program-of-record.

### WS-2 — Consolidate the process corpus
Stop the bog before adding new machinery.
- Collapse the 6+ duplicated anti-drift memories into one canonical memory; the rest
  become one-line pointers.
- Embed the single completion gate (ownership theorem / recovery formula /
  missing-category obligation / representation split) **directly into the task-card
  template and the retirement check**, so no gate is satisfiable without naming the math.
- Purge the worst dialect drift from governance docs: "descriptor binding" → "axiom $A$
  refines category $B$"; "surface" → name the actual structure; lead rule-docs with the
  mathematical contract, not the mypy/stub taxonomy.

DONE when: anti-drift doctrine has one canonical owner; the card template's acceptance
field IS the math-object gate; `grep` finds no "descriptor binding"/"frontier"/"surface"
in spec docstrings.

### WS-1 — Fix the engine (prove via one vertical slice)
Per the chosen altitude, do **not** scaffold this broadly. Prove the corrected pipeline
end-to-end on **one** obligation, then generalize.

Proof slice (the first thing built):
- **Need:** the lattice→discriminant surface that the Coble orbits depend on.
- **Spec obligation:** `discriminant_group()` / `discriminant_form` on the integral
  lattice category (already abstract-declared in `category_specs/lattices/`).
- **Literature test:** assert $A_2$ has discriminant group $\mathbb{Z}/3$ with the
  correct $\mathbb{Q}/2\mathbb{Z}$ form value, cited (Conway–Sloane SPLAG / Nikulin
  1979). Red-missing → red-wrong → green-recovers.
- **Expected-failure smoke:** instantiate $A_2$ through the category constructor, tagged
  `enforced-and-unmet`; the harness records its red as the **correct** disposition until
  the implementation lands.
- **Engine artifacts the slice forces into existence:** (a) the expected-failure harness
  that verifies *disposition*; (b) one literature-sourced run test replacing a
  meta-assertion; (c) the import/promotion check, exercised on this one method.

DONE when: the slice's smoke is verified as `enforced-and-unmet` (red-for-the-right-
reason) before impl and flips to satisfied after impl; the literature test gates on a
cited value; the meta-assertion it replaces is deleted; an import-discipline check exists
and passes for this method. Generalize the harness across obligations only after this.

### WS-3 — Coble keystone surfaces
The research payoff. Build these 5 method-families through the corrected pipeline (each
its own slice). The biggest mathematical hole is keystone (1).
1. **Lattice→discriminant lifting** — `O(L)→O(A_L,q_L)` (`stable_subgroup`,
   `discriminant_action`, abstract at `category_specs/lattices/homsets.py`) **+ the
   Nikulin/Eichler lifting theorem** converting finite discriminant-orbit equality into
   primitive isotropic-vector orbit equality. *No named theorem/backend exists today —
   logged unresolved in `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES`. This is the keystone.*
2. **`primitive_embedding` / `primitive_extension` constructors** — absent today (only
   `is_primitive` + gluing exist); needed to build $S_{Co}\subset\Lambda_{K3}$,
   $T_{Co}=S_{Co}^\perp$, and the gluing anti-isometry.
3. **Typed subgroup stabilizer / centralizer** — realize
   $\Gamma_{Co}=\mathrm{Stab}(\tilde h_{Co})\cap Z(\theta)$ as a typed $O(T_{Co})$
   subgroup with verified generators.
4. **Indefinite isotropic-plane orbit binding** — bind the (complete) Indefinite.jl
   `INDEF_FORM_GetOrbit_IsotropicKplane` backend to a Coble-callable spec method.
5. **Morphism-from-generators + matrix extraction** — `hom(images)` / `to_matrix()` as
   the substrate so $\theta$, $\gamma_{Co}$, pullbacks are defined on generators and
   matrices are *extracted*, never hand-written.

DONE when: $\Gamma_{Co}$-orbits of isotropic vectors in $T_{Co}$ are computed through
typed DSL methods (no hand-written matrices), each step backed by a literature test.

## Self-healing audit (kill authority)

On a fixed cadence (every ~N substantive commits, or on context handoff), a high-level
audit runs and is **empowered to halt a workstream**:

- **The value question:** "Did the last batch of commits move at least one literature
  test from red→green, add a real spec obligation, or implement a recovery — or did it
  only rearrange cards, statuses, ledgers, and prose?" If the latter, the batch is drift.
- **The dialect question:** did any engineering jargon re-enter spec docstrings or new
  governance prose?
- **The gate question:** did any `enforced-and-unmet` smoke get turned green by weakening
  a spec rather than implementing the math?
- **Verdict:** `healthy` | `drifting` (course-correct, name the next literature test) |
  `paperclip-factory` (stop the workstream, escalate to the user). The audit reports the
  verdict and the one next mathematical action — not a status matrix.

Detailed per-workstream sub-workflows (state diagrams) are authored **just-in-time when a
workstream starts**, not all upfront — authoring them all now would itself be the bog
this roadmap exists to prevent.
