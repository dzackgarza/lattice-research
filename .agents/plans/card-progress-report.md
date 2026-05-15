# Planning Progress Report

## Overall

- Total cards: **312**
- Completed cards: **250**
- Overall progress: `[###################-----]  80.1%`
- Active feature trees: **13**
- Completed feature trees: **7**

## Counts By Type

| Type | Total | Completed | In Progress | Needs Review | Needs Human Input | Blocked |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| decision | 22 | 22 | 0 | 0 | 0 | 0 |
| feature | 20 | 7 | 4 | 1 | 0 | 0 |
| phase | 27 | 18 | 2 | 3 | 0 | 0 |
| plan | 12 | 7 | 3 | 2 | 0 | 0 |
| spec | 60 | 57 | 0 | 1 | 0 | 0 |
| task | 171 | 139 | 0 | 11 | 3 | 0 |

## Co-Mathematician Workflow

### Workstream Phases

- None recorded.

### Task Activity Types

- `implementation`: **19**
- `source-mining`: **10**
- `validation`: **3**

## Feature Rollup

| Feature | Progress | Done/Total | In Progress | Needs Review | Needs Human Input | Blocked |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Geometry category interfaces | `[################] 100.0%` | 28/28 | 0 | 0 | 0 | 0 |
| Historical discriminant and morphism recovery | `[################] 100.0%` | 3/3 | 0 | 0 | 0 | 0 |
| Historical geometry and Coble vocabulary recovery | `[################] 100.0%` | 4/4 | 0 | 0 | 0 | 0 |
| Historical indefinite backend bridge recovery | `[################] 100.0%` | 3/3 | 0 | 0 | 0 | 0 |
| Historical lattice presentation method recovery | `[################] 100.0%` | 3/3 | 0 | 0 | 0 | 0 |
| Historical orthogonal group and orbit recovery | `[################] 100.0%` | 3/3 | 0 | 0 | 0 | 0 |
| Historical Vinberg and Coxeter recovery | `[################] 100.0%` | 5/5 | 0 | 0 | 0 | 0 |
| Modules with forms and lattices | `[###############-]  96.4%` | 53/55 | 2 | 0 | 0 | 0 |
| Category specs and Sage surface admission | `[###############-]  91.2%` | 145/159 | 5 | 0 | 0 | 0 |
| Coble cusp orbit classification | `[####------------]  25.0%` | 1/4 | 1 | 0 | 0 | 0 |
| Zero QC warnings — repo-wide QC gate | `[##--------------]  10.5%` | 2/19 | 1 | 1 | 3 | 0 |
| Coble arithmetic group generators | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Coble Coxeter parabolic classification | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Coble geometric lattice foundation | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Coble K3 folding involution | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Coble moduli comparison | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Coble stable model slc verification | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Mypy plugin for Sage category method override checking | `[----------------]   0.0%` | 0/18 | 0 | 17 | 0 | 0 |
| Sage-backed categorical implementation layer | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |
| Universal categorical algorithms | `[----------------]   0.0%` | 0/1 | 0 | 0 | 0 | 0 |

## High-Priority DAG Frontier

- `feature` `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`: Category specs and Sage surface admission (`critical`, `in-progress`)
- `feature` `FEATURE-QC-WARNINGS-ZERO`: Zero QC warnings — repo-wide QC gate (`critical`, `in-progress`)
- `phase` `PHASE-QC-BASIC-TYPING-HYGIENE`: Basic mypy typing hygiene (`critical`, `revision-required`)
- `phase` `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT`: Mapping doc spec conversion and mathematical audit (`critical`, `in-progress`)
- `plan` `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`: Category spec source maps and admission (`critical`, `in-progress`)
- `plan` `PLAN-QC-MYPY-FOUNDATION-ORDER`: QC mypy foundation dependency order (`critical`, `needs-review`)
- `task` `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY`: Fix basic mypy missing-type hygiene (`critical`, `needs-human-input`)
- `task` `TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES`: Ground category-spec callable constructor types (`critical`, `needs-human-input`)
- `task` `TASK-QC-RATIONAL-FIELD-PARENT-SURFACE-TYPING`: Ground rational-field parent-method typing (`critical`, `needs-human-input`)
- `feature` `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`: Mypy plugin for Sage category method override checking (`high`, `needs-review`)
- `phase` `PHASE-SAGE-SIDE-API`: Sage introspection API (`high`, `needs-review`)
- `plan` `PLAN-MYPY-PLUGIN-IMPLEMENTATION`: Mypy plugin implementation plan (`high`, `needs-review`)
- `spec` `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: Acceptance criteria for Sage mypy category override plugin (`high`, `needs-review`)
- `task` `TASK-MYPY-PARSER`: Implement parse_method_container_fullname and is_sage_method_container (`high`, `needs-review`)

## High-Priority DAG-Gated Items

- `feature` `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`: gated by `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`, `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`, `FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS`, `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER`, `FEATURE-QC-WARNINGS-ZERO` (`critical`, `unstarted`)
- `feature` `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`: gated by `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`, `FEATURE-QC-WARNINGS-ZERO` (`critical`, `in-progress`)
- `feature` `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER`: gated by `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`, `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`, `FEATURE-QC-WARNINGS-ZERO` (`critical`, `unstarted`)
- `feature` `FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS`: gated by `FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER`, `FEATURE-QC-WARNINGS-ZERO` (`critical`, `unstarted`)
- `phase` `PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`: gated by `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`, `PHASE-QC-BASIC-TYPING-HYGIENE` (`critical`, `unstarted`)
- `plan` `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`: gated by `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` (`critical`, `in-progress`)
- `plan` `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP`: gated by `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`, `FEATURE-QC-WARNINGS-ZERO` (`critical`, `in-progress`)
- `task` `TASK-AUDIT-MODULES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES`: gated by `PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT` (`critical`, `unstarted`)
- `task` `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`: gated by `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`, `PHASE-QC-BASIC-TYPING-HYGIENE`, `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY` (`critical`, `unstarted`)
- `task` `TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME`: gated by `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` (`critical`, `unstarted`)
- `task` `TASK-QC-PLUGIN-METHOD-CONTAINER-SELF-SURFACES`: gated by `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`, `PHASE-QC-BASIC-TYPING-HYGIENE`, `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` (`critical`, `unstarted`)
- `task` `TASK-QC-PLUGIN-CATEGORY-PROMOTION-RETURNS`: gated by `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`, `PHASE-QC-BASIC-TYPING-HYGIENE`, `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` (`critical`, `unstarted`)
- `feature` `FEATURE-COBLE-ARITHMETIC-GROUP-GENERATORS`: gated by `FEATURE-COBLE-K3-FOLDING-INVOLUTION`, `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`, `FEATURE-QC-WARNINGS-ZERO` (`high`, `unstarted`)
- `feature` `FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION`: gated by `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`, `FEATURE-QC-WARNINGS-ZERO` (`high`, `unstarted`)
- `feature` `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION`: gated by `FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION`, `FEATURE-QC-WARNINGS-ZERO` (`high`, `in-progress`)

## Blocked Items

- None.

## Most Recently Completed

- 2026-05-15 `spec` `SPEC-MAPPING-RINGS`: Track rings mapping spec (commit `5c13e1c`: docs(qc): separate mypy foundation routing)
- 2026-05-15 `decision` `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`: Mypy error triage — code gaps vs plugin gaps across all remaining error groups (commit `5c13e1c`: docs(qc): separate mypy foundation routing)
- 2026-05-15 `decision` `DECISION-01KQN9J3XCYW748M5V0K2SGJGK-DECIDE-WHETHER-EQUIVALENCE-RELATIONS-AND-SET-PARTITIONS-NEED-A-FIRST-CLA`: Decide whether equivalence relations and set partitions need a first-class set subtree or remain centralized Sage-backed type aliases (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-01KQN9YGCTP85RXF1F56D8S08X-DECIDE-WHETHER-PARTITIONED-SET-COMBINATORIAL-SUBCLASSES-SUCH-AS-NONCROSS`: Decide whether partitioned-set combinatorial subclasses such as noncrossing and atomic become axiomatic subcategories in the current set-partition pass or a later pass (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-01KQN9YGCVRR84SHX4DR1K284C-DECIDE-WHETHER-TENSOR-SYMMETRY-ANTISYMMETRY-AND-CONTRACTION-NEED-ADMITTE`: Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees before full tensor-calculus method mapping (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING`: Decide how partition element methods override Sage list-returning methods (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-20260505-REALSET-SAGE-TOPOLOGICAL-AXIOM-WARNING`: Decide how to handle Sage RealSet inherited Sets.Topological axiom warning (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER`: Decide algebra standard-involution method owner (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES`: Decide public names for malformed backend-mapping source surfaces (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER`: Decide Picard group and Picard lattice method ownership (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-CELLULAR-ALGEBRA-OWNER`: Route Cellular algebra subcategory to Algebras(R).FiniteDimensional().WithBasis().Cellular() (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-DEC-PHASE-01-PLAN-APPROVAL-AND-FIRST-EXECUTION-LANE`: Decide whether to approve the phase-01 plan tree and first execution lane (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION`: Decide HomCategory semantic base and Sage homset mirroring route (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES`: Decide module sidedness structure transport and overload surfaces (commit `582e200`: chore: relocate planning workspace under agents)
- 2026-05-15 `decision` `DECISION-NIKULIN-INVARIANTS-DISCRIMINANT-FORM-RESEARCH-GAP`: Nikulin invariants discriminant-form research gap (commit `582e200`: chore: relocate planning workspace under agents)

## Notes

- Completion status is inferred from the local tracker schema labels such as `Done`, `Complete`, `Implemented`, and `Decided`.
- Recently completed items are cards currently in a completed status, sorted by the most recent git commit touching that card file.
- Completed feature trees may live under `.agents/plans/features/completed/`; this report includes them in totals.
- High-priority DAG frontier items exclude cards with incomplete direct or transitive `dependsOn` prerequisites. Gated items are shown only by their unmet prerequisite frontier.
