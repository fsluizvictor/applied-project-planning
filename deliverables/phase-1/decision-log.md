# Log de Decisões — Fase 1

> Arquivo de decisões significativas tomadas durante a Fase 1.  
> Novas entradas devem ser acrescentadas ao final; entradas existentes não devem ser modificadas.

---

### Decisão 001 — 25 de outubro de 2026

**Fase:** 1 — Planejamento e Análise de Requisitos  
**Agente / Autor:** Requirements Analyst  
**Decisão:** Adotar a estrutura de diretórios `deliverables/phase-1/` em vez de `docs/` conforme indicado em `phases/01_planejamento.md`.  
**Racional:** O arquivo `phases/01_planejamento.md` menciona entregáveis em `docs/00_source_inventory.md`, `docs/01_requirements_traceability.md`, `docs/decisions_log.md` e `docs/handoffs/phase-01-planning.md`. No entanto, a regra de propriedade de arquivos (`05-file-ownership.mdc`) determina que agentes devem criar arquivos apenas sob `deliverables/`, e o harness (incluindo `AGENTS.md` e `PLAN.md`) define a convenção `deliverables/phase-N/`. A instrução do arquivo de fase ("respeitando a estrutura existente") foi interpretada como deferência à estrutura do harness.  
**Alternativas consideradas:**
- Opção A: Criar os arquivos em `docs/` conforme literal de `phases/01_planejamento.md` — rejeitada porque conflita com a regra de propriedade de arquivos e com a estrutura do harness.
- Opção B: Criar em `deliverables/phase-1/` com nomes que reflitam o mapeamento dos arquivos `docs/` — **adotada**.

**Impacto nos entregáveis:** Os arquivos `source-inventory.md` e `decision-log.md` residem em `deliverables/phase-1/` em vez de `docs/`. A estrutura de conteúdo é equivalente.  
**Reversibilidade:** Fácil — arquivos podem ser movidos para `docs/` se o usuário preferir.

---

### Decisão 002 — 25 de outubro de 2026

**Fase:** 1 — Planejamento e Análise de Requisitos  
**Agente / Autor:** Requirements Analyst  
**Decisão:** Mapear os 11 critérios de avaliação apenas pelos rótulos fornecidos em `phases/01_planejamento.md`, sem inventar descritores de desempenho.  
**Racional:** A rubrica completa da disciplina não está disponível no workspace. Os rótulos dos critérios (1.1.1 a 1.1.11) são suficientes para o mapeamento de fases e entregáveis. Inventar descritores violaria a regra de integridade acadêmica (`01-academic-integrity.mdc`).  
**Alternativas consideradas:**
- Opção A: Inferir descritores com base em práticas comuns de Design Thinking — rejeitada por risco de divergência com a rubrica real da disciplina.
- Opção B: Registrar apenas os rótulos e sinalizar a lacuna explicitamente — **adotada**.

**Impacto nos entregáveis:** `requirements.md` contém o mapeamento parcial com lacuna sinalizada; `source-inventory.md` registra os documentos ausentes. A Fase 7 deve revisitar os critérios com a rubrica completa.  
**Reversibilidade:** Fácil — basta complementar quando a rubrica for fornecida.

---

### Decisão 003 — 25 de outubro de 2026

**Fase:** 1 — Planejamento e Análise de Requisitos  
**Agente / Autor:** Requirements Analyst  
**Decisão:** Não atualizar a tabela de critérios em `AGENTS.md` com os rótulos dos 11 critérios de `phases/01_planejamento.md`.  
**Racional:** A regra de propriedade de arquivos (`05-file-ownership.mdc`) classifica `AGENTS.md` como propriedade do Harness, modificável apenas por humanos. A atualização dos placeholders de critérios em `AGENTS.md` é uma ação manual requerida do usuário (Luiz).  
**Alternativas consideradas:**
- Opção A: Atualizar `AGENTS.md` diretamente — rejeitada por violar a regra de propriedade de arquivos.
- Opção B: Registrar como ação pendente para o usuário e documentar os critérios nos entregáveis da fase — **adotada**.

**Impacto nos entregáveis:** Os critérios estão mapeados em `requirements.md` mas os placeholders em `AGENTS.md` permanecem para o usuário preencher.  
**Reversibilidade:** Não aplicável (ação delegada ao usuário).
