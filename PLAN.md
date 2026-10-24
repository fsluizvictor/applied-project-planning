# PLAN.md — Project Phase Plan

**Project:** Desafio e Solução — AI-powered English Conversation Simulator  
**Language:** Deliverables in Brazilian Portuguese; harness files in English  
**Last updated:** (update manually each time a phase status changes)

---

## Phase Dependency Graph

```
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4
                                                    │
                                                    ▼
                                      Phase 5 ──► Phase 6 ──► Phase 7 ──► Phase 8
```

Each arrow represents a **hard dependency**: a phase may not begin until all upstream phases are `DONE`.

---

## Phase Details

---

### Phase 0 — Harness Setup

| Field | Value |
|-------|-------|
| **Status** | ✅ DONE |
| **Responsible** | Harness Engineer (this session) |
| **Inputs** | `harness.md` |
| **Outputs** | `AGENTS.md`, `PLAN.md`, `.cursor/rules/*.mdc`, `.cursor/agents/*.md`, `templates/*.md` |
| **Human approval required** | No (harness creation, not academic work) |

**Acceptance Criteria:**
- [x] `AGENTS.md` exists and contains global instructions
- [x] Six `.mdc` rule files exist with correct frontmatter
- [x] Seven agent files exist under `.cursor/agents/`
- [x] Four template files exist under `templates/`
- [x] `PLAN.md` exists with all phases mapped
- [x] Eleven evaluation criteria are present (as placeholders — must be filled before Phase 1)
- [x] Failed acceptance check protocol is defined

---

### Phase 1 — Briefing & Requirements

| Field | Value |
|-------|-------|
| **Status** | 🟡 READY |
| **Responsible Agent** | `requirements-analyst` |
| **Inputs** | `AGENTS.md`, `PLAN.md`, project brief (provided by human) |
| **Outputs** | `deliverables/phase-1/requirements.md`, `deliverables/phase-1/acceptance-check.md`, `deliverables/phase-1/phase-handoff.md` |
| **Human approval required** | ✅ Yes — before Phase 2 begins |

**Acceptance Criteria:**
- [ ] Project scope is documented without invented content
- [ ] Target users / stakeholders identified
- [ ] At least one constraint per evaluation criterion is recorded
- [ ] Unresolved assumptions listed explicitly
- [ ] No fabricated interviews or citations
- [ ] Eleven evaluation criteria are mapped (or flagged if still TBD)
- [ ] `acceptance-check.md` completed and signed by human

---

### Phase 2 — Context & Research

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 1 DONE) |
| **Responsible Agent** | `context-researcher` |
| **Inputs** | `deliverables/phase-1/phase-handoff.md` |
| **Outputs** | `deliverables/phase-2/context-report.md`, `deliverables/phase-2/acceptance-check.md`, `deliverables/phase-2/phase-handoff.md` |
| **Human approval required** | ✅ Yes |

**Acceptance Criteria:**
- [ ] All cited sources are real and verifiable
- [ ] No invented statistics or findings
- [ ] Gaps and limitations of available research are documented
- [ ] Unresolved assumptions listed
- [ ] `acceptance-check.md` completed

---

### Phase 3 — Empathy, Personas & Observation Matrix

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 2 DONE) |
| **Responsible Agent** | `persona-empathy` |
| **Inputs** | `deliverables/phase-2/phase-handoff.md` |
| **Outputs** | `deliverables/phase-3/personas.md`, `deliverables/phase-3/empathy-maps.md`, `deliverables/phase-3/observation-matrix.md`, `deliverables/phase-3/acceptance-check.md`, `deliverables/phase-3/phase-handoff.md` |
| **Human approval required** | ✅ Yes |

**Acceptance Criteria:**
- [ ] At least 2 distinct personas documented
- [ ] Each persona grounded in research from Phase 2 (no invention)
- [ ] Empathy map has all four quadrants: Thinks/Feels, Sees, Says/Does, Hears
- [ ] Observation matrix populated from real secondary sources
- [ ] Unresolved assumptions listed
- [ ] `acceptance-check.md` completed

---

### Phase 4 — Problem Framing

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 3 DONE) |
| **Responsible Agent** | `hypothesis-risk` |
| **Inputs** | `deliverables/phase-3/phase-handoff.md` |
| **Outputs** | `deliverables/phase-4/insights.md`, `deliverables/phase-4/hmw-statements.md`, `deliverables/phase-4/hypotheses.md`, `deliverables/phase-4/risk-register.md`, `deliverables/phase-4/acceptance-check.md`, `deliverables/phase-4/phase-handoff.md` |
| **Human approval required** | ✅ Yes |

**Acceptance Criteria:**
- [ ] At least 3 insights derived from Phase 3 data
- [ ] At least 2 HMW (How Might We) statements
- [ ] At least 3 hypotheses formulated with testable form
- [ ] Risk register has likelihood × impact scoring
- [ ] Unresolved assumptions listed
- [ ] `acceptance-check.md` completed

---

### Phase 5 — Ideation & Prioritization

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 4 DONE) |
| **Responsible Agent** | `idea-prioritizer` |
| **Inputs** | `deliverables/phase-4/phase-handoff.md` |
| **Outputs** | `deliverables/phase-5/idea-bank.md`, `deliverables/phase-5/prioritization-matrix.md`, `deliverables/phase-5/selected-idea.md`, `deliverables/phase-5/acceptance-check.md`, `deliverables/phase-5/phase-handoff.md` |
| **Human approval required** | ✅ Yes |

**Acceptance Criteria:**
- [ ] At least 5 distinct ideas generated
- [ ] Prioritization uses a documented scoring rubric (impact × feasibility or equivalent)
- [ ] Winning idea clearly stated with rationale
- [ ] Rejected ideas briefly explained
- [ ] Unresolved assumptions listed
- [ ] `acceptance-check.md` completed

---

### Phase 6 — Solution Specification

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 5 DONE) |
| **Responsible Agent** | `solution-specifier` |
| **Inputs** | `deliverables/phase-5/phase-handoff.md` |
| **Outputs** | `deliverables/phase-6/solution-spec.md`, `deliverables/phase-6/prototype-description.md`, `deliverables/phase-6/acceptance-check.md`, `deliverables/phase-6/phase-handoff.md` |
| **Human approval required** | ✅ Yes |

**Acceptance Criteria:**
- [ ] Solution specification addresses each evaluation criterion
- [ ] Prototype description is concrete (not aspirational)
- [ ] AI component clearly described (scope, role, limitations)
- [ ] Feasibility argued from Phase 2 research (no invention)
- [ ] Unresolved assumptions listed
- [ ] `acceptance-check.md` completed

---

### Phase 7 — Academic Review

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 6 DONE) |
| **Responsible Agent** | `academic-reviewer` (invoked independently — fresh context) |
| **Inputs** | All `phase-handoff.md` files from Phases 1–6 + all main deliverables |
| **Outputs** | `deliverables/phase-7/review-report.md`, `deliverables/phase-7/acceptance-check.md` |
| **Human approval required** | ✅ Yes — this is the final gate before assembly |

**Acceptance Criteria:**
- [ ] All eleven evaluation criteria explicitly assessed (PASS / FAIL / PARTIAL)
- [ ] Each FAIL or PARTIAL includes a concrete remediation note
- [ ] No fabricated external validation cited
- [ ] Review conducted with no reliance on prior agent session context
- [ ] `acceptance-check.md` completed

---

### Phase 8 — Final Proposal Assembly

| Field | Value |
|-------|-------|
| **Status** | 🔴 BLOCKED (awaits Phase 7 DONE + human approval) |
| **Responsible** | Human + any agent as directed |
| **Inputs** | All prior deliverables; `deliverables/phase-7/review-report.md` |
| **Outputs** | `deliverables/final-proposal/proposta-desafio-e-solucao.md` (or PDF) |
| **Human approval required** | ✅ Yes — final sign-off |

**Acceptance Criteria:**
- [ ] All eleven evaluation criteria covered
- [ ] Written entirely in Brazilian Portuguese
- [ ] All sources cited are real
- [ ] No invented interview data or statistics
- [ ] Consistent with all phase deliverables

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ DONE | Phase complete, acceptance check passed, human approved |
| 🟡 READY | All dependencies met, can be started |
| 🔵 IN PROGRESS | Currently being worked on |
| 🔴 BLOCKED | Upstream dependency not yet DONE |
| ❌ FAILED | Acceptance check failed — phase reopened |
