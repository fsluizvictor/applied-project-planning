# AGENTS.md — Global Project Instructions

## Project Overview

This project produces a **"Desafio e Solução"** academic proposal for an AI-powered English conversation simulator.  
All academic deliverables must be written in **Brazilian Portuguese**.

## Scope of This File

This file provides global behavioral instructions for every agent that operates in this project.  
Do not duplicate these instructions in rules or agent files — refer to this file from there instead.

---

## Mandatory Behaviors (All Agents, All Phases)

1. **Never invent source material.** Do not fabricate interviews, citations, statistics, or project requirements.  
   If information is missing, record an explicit assumption with a flag: `[ASSUMPTION — requires validation]`.

2. **Always read previous deliverables before producing new ones.**  
   Check `PLAN.md` for the phase status and locate the outputs of all upstream phases.

3. **Record unresolved assumptions.** Every agent report must include an "Unresolved Assumptions" section.

4. **Do not claim a phase passed unless its acceptance criteria have been checked.**  
   Fill in `templates/acceptance-check.md` and store it under `deliverables/<phase>/acceptance-check.md`.

5. **Do not claim that independent agents were used unless they were actually invoked in this session.**

6. **Human approval is required before advancing to the next major phase.**  
   At the end of each phase, produce a completed `templates/phase-handoff.md` and stop. Wait for explicit approval.

7. **Follow language standards.** All deliverables → Brazilian Portuguese.  
   Internal harness files (rules, agent definitions, templates) → English.

8. **Follow file ownership rules.** See `.cursor/rules/05-file-ownership.mdc`.

9. **Report limitations honestly.** If you cannot deterministically enforce a constraint, say so explicitly.

---

## Phase Map (summary — see PLAN.md for full detail)

| Phase | Name                        | Status   |
|-------|-----------------------------|----------|
| 0     | Harness Setup               | DONE     |
| 1     | Briefing & Requirements     | READY    |
| 2     | Context & Research          | BLOCKED  |
| 3     | Empathy, Personas, Observation | BLOCKED |
| 4     | Problem Framing             | BLOCKED  |
| 5     | Ideation & Prioritization   | BLOCKED  |
| 6     | Solution Specification      | BLOCKED  |
| 7     | Academic Review             | BLOCKED  |
| 8     | Final Proposal Assembly     | BLOCKED  |

---

## Deliverables Directory Convention

All phase outputs are stored under:
```
deliverables/
  phase-1/
    requirements.md
    acceptance-check.md
    phase-handoff.md
  phase-2/
    ...
```

Do not write deliverables outside this tree unless explicitly instructed.

---

## Eleven Evaluation Criteria

> ⚠️ MANUAL ACTION REQUIRED before Phase 1 begins.  
> Replace the placeholders below with the actual criteria from the academic assessment rubric.

| # | Criterion | Mapped Deliverable |
|---|-----------|-------------------|
| 01 | [CRITÉRIO-01 — preencher] | TBD |
| 02 | [CRITÉRIO-02 — preencher] | TBD |
| 03 | [CRITÉRIO-03 — preencher] | TBD |
| 04 | [CRITÉRIO-04 — preencher] | TBD |
| 05 | [CRITÉRIO-05 — preencher] | TBD |
| 06 | [CRITÉRIO-06 — preencher] | TBD |
| 07 | [CRITÉRIO-07 — preencher] | TBD |
| 08 | [CRITÉRIO-08 — preencher] | TBD |
| 09 | [CRITÉRIO-09 — preencher] | TBD |
| 10 | [CRITÉRIO-10 — preencher] | TBD |
| 11 | [CRITÉRIO-11 — preencher] | TBD |

Once criteria are filled in, update the "Mapped Deliverable" column and cross-reference in `PLAN.md`.

---

## Failed Acceptance Check Protocol

If any acceptance check fails:

1. The phase is **reopened** — its status in `PLAN.md` reverts to `IN PROGRESS`.
2. The responsible agent receives the failed check as input.
3. The agent produces a revised deliverable addressing only the failed criteria.
4. The acceptance check is re-run from scratch.
5. A new `agent-report.md` is filed referencing the failure that triggered the revision.
6. Human approval is still required before the phase is closed again.
