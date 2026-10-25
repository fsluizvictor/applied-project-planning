Act as a Cursor Harness Engineer.

Your task is to design and create a robust, maintainable harness for an academic Design Thinking project. The project will produce a "Desafio e Solução" proposal for an AI-powered English conversation simulator.

Do not write the final academic proposal in this task. Build the environment that will govern its future production.

### Objectives

1. Inspect the workspace and identify existing files, instructions, and reference materials.
2. Verify the current Cursor-supported formats for project rules and custom subagents using available documentation and existing project conventions.
3. Create a project-level AGENTS.md with global instructions.
4. Create focused `.cursor/rules/*.mdc` files covering:
   - Global operating principles.
   - Academic integrity and research ethics.
   - Evidence management and citations.
   - Brazilian Portuguese writing standards.
   - Phase transitions and acceptance criteria.
   - File ownership and change management.
5. Create specialized agents under `.cursor/agents/` for:
   - Requirements analysis.
   - Context and research.
   - Persona, empathy map, and observation matrix.
   - Hypotheses and risk assessment.
   - Idea prioritization.
   - Solution specification.
   - Independent academic review.
6. Create a root `PLAN.md` with phases, dependencies, deliverables, status, and acceptance criteria.
7. Create templates for phase handoffs, agent reports, decisions, and acceptance checks.
8. Map all eleven academic evaluation criteria to explicit deliverables.
9. Define how failed acceptance checks are reported and how the responsible phase is reopened.
10. Create a clear initial execution instruction that runs Phase 0 only.

### Mandatory constraints

- Do not invent source material, interviews, citations, or project requirements.
- Do not overwrite existing files without inspecting them first.
- Keep rules focused and avoid duplicating the same instructions across files.
- Use valid, currently supported Cursor configuration formats.
- Give every agent a narrow responsibility, clear inputs, explicit outputs, and acceptance criteria.
- Require each phase to read previous deliverables and record unresolved assumptions.
- Do not claim that a phase passed unless its acceptance criteria have been checked.
- Do not claim that independent agents were used unless they were actually invoked.
- Require human approval before moving from one major phase to the next.
- Separate instructions from actual enforcement: use deterministic checks where possible and report limitations where enforcement depends on agent compliance.
- Keep all academic deliverables in Brazilian Portuguese.

### Execution procedure

Step 1: Inspect the workspace and available Cursor configuration.

Step 2: Propose the harness structure and explain any important design decisions.

Step 3: Create the files after checking for conflicts with existing material.

Step 4: Validate file names, frontmatter, references, phase dependencies, and coverage of the eleven evaluation criteria.

Step 5: Produce a harness validation report with passed checks, failed checks, limitations, and remaining manual actions.

Step 6: Stop. Do not start researching or writing the academic proposal.

The final output of this task is a validated harness ready for the separate academic workflow.