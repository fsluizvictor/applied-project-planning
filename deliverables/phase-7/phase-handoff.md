# Phase Handoff — Fase 7: Revisão Acadêmica Independente

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 7 |
| **Phase name** | Revisão Acadêmica Independente |
| **Responsible agent** | Academic Reviewer |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz — a confirmar |
| **Phase status in PLAN.md** | Aguarda aprovação humana para marcar DONE |

---

## Summary of Work Done

O Academic Reviewer auditou todos os 11 critérios de avaliação da disciplina contra os entregáveis das Fases 1–6, verificou a rastreabilidade entre fases, auditou a integridade acadêmica de toda a documentação e identificou 8 problemas (1 crítico, 1 alto corrigido, 4 médios, 1 baixo). O problema crítico (área do conhecimento do curso) requer informação do usuário.

---

## Deliverables Produced

| File | Location | Description |
|------|----------|-------------|
| `relatorio-de-auditoria.md` | `deliverables/phase-7/relatorio-de-auditoria.md` | Auditoria completa por critério + correções aplicadas |
| `acceptance-check.md` | `deliverables/phase-7/acceptance-check.md` | 4/5 PASS; 1 PARTIAL |
| `agent-report.md` | `deliverables/phase-7/agent-report.md` | Relatório do agente |
| `phase-handoff.md` | `deliverables/phase-7/phase-handoff.md` | Este documento |

---

## Key Findings

- **Cadeia de rastreabilidade:** ✅ coerente ao longo de todas as fases.
- **Integridade acadêmica:** ✅ nenhuma evidência, citação ou resultado fabricado em toda a documentação.
- **Critério mais crítico pendente:** área do conhecimento do curso (A-08) — **requer informação do usuário (Luiz).**
- **HMW statements:** adicionados em D-C-01 do relatório de auditoria.
- **Fluência vs. usabilidade:** a distinção está bem mantida em toda a documentação.
- **Formato visual de personas:** depende de decisão do autor na Fase 8.

---

## Ações Obrigatórias do Usuário Antes da Fase 8

| # | Ação | Impacto se não resolvida |
|---|------|------------------------|
| **UA-01** | Informar a **área do conhecimento do curso** (ex.: Engenharia de Software, Tecnologia da Informação, Design Thinking, etc.) | Critério 1.1.4 ficará PARTIAL na proposta final |
| **UA-02** | Confirmar ou fornecer o **prazo real do projeto** (elemento T do SMART) | Objetivo SMART permanecerá com prazo provisório |
| **UA-03** | Confirmar a **convenção GUT** usada pela disciplina (G+U+T ou G×U×T) | Somatórios do registro de riscos e hipóteses podem precisar de recálculo |
| **UA-04** | Decidir sobre o **formato visual das personas** (diagramas/figuras ou tabelas markdown são suficientes?) | Afeta apresentação final |
| **UA-05** | Definir o **método de recrutamento** dos participantes do teste | Plano de validação permanecerá incompleto |

---

## Unresolved Assumptions (todas as fases)

| # | Suposição | Fase de origem |
|---|-----------|---------------|
| A-08 | Área do conhecimento do curso | Fase 1 |
| B-01 | Situação prática prioritária — resolvida como "entrevista" para o MVP | Fase 2 |
| B-02 | Relatório primário Pearson não acessado | Fase 2 |
| B-03 | Sem evidência sobre cenário de viagem | Fase 2 |
| B-04 | Evidência de chatbots não vem de contexto brasileiro | Fase 2 |
| D-01 | Convenção GUT | Fase 4 |
| D-02 | Número de participantes do teste (5–8) | Fase 4 |
| D-04 | Prazo do projeto | Fase 6 |
| D-05 | Método de recrutamento de participantes | Fase 6 |
| E-01 | Tecnologia ASR/LLM/TTS não selecionada | Fase 5 |

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| 11 critérios avaliados com PASS/FAIL/PARTIAL | PASS |
| Cada FAIL/PARTIAL com remediação concreta | PASS |
| Nenhuma validação externa fabricada | PASS |
| Revisão independente de contexto anterior | PARTIAL (limitação declarada) |
| acceptance-check.md completo | PASS |

**Overall:** ⚠️ PASS COM RESSALVA — aguarda aprovação humana

---

## Instructions for Next Phase (Fase 8 — Montagem da Proposta Final)

> A Fase 8 é responsabilidade humana + agente, conforme PLAN.md. As instruções abaixo são para orientar a consolidação.

1. Resolver UA-01 a UA-05 acima antes de iniciar a consolidação.
2. Usar `deliverables/phase-7/relatorio-de-auditoria.md` como guia de quais conteúdos incluir e em que ordem.
3. A estrutura da proposta final deve seguir a numeração do PDF de referência: 1.1 Desafio → 1.1.1 Análise de Contexto → 1.1.2 Personas → 1.1.3 Justificativas → 1.1.4 Hipóteses → 1.2 Solução → 1.2.1 Objetivo SMART → 1.2.2 Escopo → 1.2.3 Cronograma/Validação.
4. Incluir HMW statements (D-C-01) na seção de hipóteses ou como subsecção do desafio.
5. Declarar explicitamente na proposta final todas as limitações metodológicas: ausência de pesquisa primária, evidência de eficácia não específica para o Brasil, prazo provisório (se UA-02 não for resolvida).
6. Não adicionar percentuais de melhoria sem fonte — manter o padrão de rigor estabelecido nas fases anteriores.
7. O arquivo final deve ser salvo em `deliverables/final-proposal/proposta-desafio-e-solucao.md`.
