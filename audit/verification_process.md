# Canonical Verification Process

**Purpose**: Prevent assigning impossible tasks by mandating research and scoping phases
before delegation.

## The Correct Verification Loop

Every verification task must follow this structure:

### Phase 1: Research

**Question**: What techniques exist?
What makes this hard?
What's known in literature?

**Actions**:
- Search literature for standard techniques
- Identify what experts do for similar problems
- Understand theoretical foundations
- Document what's known vs unknown

**Output**: Research summary with citations to relevant techniques

**Pivot trigger**: If literature reveals fundamental complexity, adapt scope

### Phase 2: Scope

**Question**: Is this computationally verifiable?
What prerequisites? What bounds are justified?

**Actions**:
- Identify prerequisites (finiteness arguments, bounds, invariants)
- Determine if computational verification is feasible
- Understand what would constitute valid evidence vs proof
- Identify gaps between claim and verifiable subclaims

**Output**: Scoping document stating what CAN be verified and what prerequisites are
needed

**Pivot trigger**: If prerequisites are missing or task is impossible, pivot to
achievable subtask

### Phase 3: Method

**Question**: What approach has mathematical justification?

**Actions**:
- Choose technique with theoretical backing
- Justify any bounds or search spaces
- Identify acceptance criteria
- Document expected computational cost

**Output**: Method specification with justification

**Pivot trigger**: If no justified method exists, pivot to evidence-gathering or
literature search

### Phase 4: Plan

**Question**: How do we break this into delegable subtasks?

**Actions**:
- Decompose into concrete subtasks
- Define clear acceptance criteria for each
- Identify dependencies
- Allocate to appropriate subagent types

**Output**: Structured plan with subtasks and acceptance criteria

### Phase 5: Delegate

**Question**: Execute with proper technique

**Actions**:
- Delegate to appropriate subagent (Prover for mathematical verification)
- Provide clear context and acceptance criteria
- Include method justification in prompt

**Output**: Subagent results

### Phase 6: Audit

**Question**: Do results meet acceptance criteria?

**Actions**:
- Review subagent transcript and outputs
- Check against acceptance criteria
- Verify mathematical correctness (not just execution success)
- Identify any gaps or errors

**Output**: Audit report with pass/fail determination

### Phase 7: Pivot (if needed)

**Question**: What did we learn?
How should we adapt?

**Actions**:
- If complexity discovered: revise scope, add prerequisites
- If method failed: try alternative approach
- If claim false: document counterexample
- If evidence insufficient: gather more data

**Output**: Updated plan or new research direction

**Key principle**: Pivots are EXPECTED and NORMAL when complexity is discovered.
They are not failures.

## Anti-Patterns (DO NOT DO)

❌ **Skip research phase**: "Verify this claim" → delegate immediately ❌ **Assume
feasibility**: Treat all claims as equally verifiable ❌ **Ignore prerequisites**: Assign
tasks without checking if foundations exist ❌ **Treat pivots as failures**: Rigidly
stick to original plan when complexity discovered ❌ **Confuse evidence with proof**:
Computational results are evidence, not always proof

## Examples

### Good: Task 2.1 Isotropic Orbits

1. **Research**: Nikulin's theory of discriminant groups, orbit classification
2. **Scope**: Finite discriminant group (2048 elements), computationally enumerable
3. **Method**: Exhaustive enumeration + orbit computation via group action
4. **Plan**: Enumerate A_T, compute q_T, find orbits under O(q_T)
5. **Delegate**: To Prover with clear acceptance criteria
6. **Audit**: Verified 2 orbits (1 zero + 527 nonzero)
7. **Result**: ✓ PASSED

### Bad: Task 3.2 Primitive Isotropic Planes (original attempt)

1. ~~**Research**: SKIPPED~~
2. ~~**Scope**: SKIPPED~~
3. ~~**Method**: SKIPPED~~
4. **Plan**: "Verify there are 15 primitive isotropic planes"
5. **Delegate**: Assigned impossible task (enumerate infinite lattice without bounds)
6. **Audit**: Discovered task was impossible
7. **Outcome**: Planning failure, not execution failure

### Good: Task 3.2 Primitive Isotropic Planes (corrected)

1. **Research**: Study literature techniques for enumerating primitive isotropic planes
2. **Scope**: Understand finiteness argument, identify proper bounds
3. **Method**: Identify justified enumeration technique
4. **Plan**: Break into research → finiteness → enumeration subtasks
5. **Delegate**: With proper prerequisites
6. **Audit**: Verify against acceptance criteria
7. **Pivot**: If needed based on research findings

## Usage

When creating any verification plan, explicitly include all 7 phases.
Document pivots as they occur.
Treat complexity discovery as valuable information, not failure.

Reference this document in all verification plans to ensure process compliance.
