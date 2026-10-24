# Agent Report — [Agent Name] / Phase [N]

> Copy this template to `deliverables/phase-N/agent-report.md` and fill in all sections.

---

## Report Metadata

| Field | Value |
|-------|-------|
| **Agent** | [Agent name from `.cursor/agents/`] |
| **Phase** | [N — Name] |
| **Session date** | [YYYY-MM-DD] |
| **Triggered by** | [Human instruction / Failed acceptance check from Phase N] |
| **Revision number** | [1 = first attempt; 2 = first revision after failure; etc.] |

---

## Inputs Read

List every file read before producing outputs:

- [ ] `AGENTS.md`
- [ ] `PLAN.md`
- [ ] `deliverables/phase-[N-1]/phase-handoff.md`
- [ ] [additional files as applicable]

---

## Summary of Outputs Produced

| File | Brief description |
|------|------------------|
| | |

---

## Decisions Made

| Decision | Rationale | Alternative considered |
|----------|-----------|----------------------|
| | | |

> If a significant decision was made, also log it in `templates/decision-log.md`.

---

## Unresolved Assumptions

| # | Assumption | Where recorded |
|---|-----------|---------------|
| 1 | [ASSUMPTION — requires validation]: | |

---

## Limitations & Honest Disclosures

[List anything the agent could not verify, enforce, or determine. Be explicit.]

- 
- 

---

## Acceptance Check Self-Assessment

| Criterion | Self-assessed result | Notes |
|-----------|---------------------|-------|
| | PASS / FAIL / PARTIAL | |

> Note: Self-assessment does not replace the human-reviewed acceptance check.

---

## Failure Context (if this is a revision)

> Fill this section only if `Revision number > 1`.

| Field | Value |
|-------|-------|
| **Failed check file** | `deliverables/phase-N/acceptance-check.md` (revision [N-1]) |
| **Criteria that failed** | [list] |
| **Changes made in this revision** | [list] |
