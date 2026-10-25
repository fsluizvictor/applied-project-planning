# Phase Handoff — Fase 5: Priorização e MVP

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 5 |
| **Phase name** | Priorização de Ideias e MVP |
| **Responsible agent** | Idea Prioritizer |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz — a confirmar |
| **Phase status in PLAN.md** | Aguarda aprovação humana para marcar DONE |

---

## Summary of Work Done

Avaliaram-se 5 alternativas de solução e 12 funcionalidades candidatas. O MVP foi definido com 4 funcionalidades essenciais centradas no cenário de entrevista de emprego em inglês. Tecnologias específicas não foram escolhidas — essa decisão é escopo da Fase 6.

---

## Deliverables Produced

| File | Location | Description |
|------|----------|-------------|
| `priorizacao-ideias.md` | `deliverables/phase-5/priorizacao-ideias.md` | Alternativas, funcionalidades e matriz de priorização |
| `escopo-mvp.md` | `deliverables/phase-5/escopo-mvp.md` | MVP: F01, F03, F04, F05 + rastreabilidade |
| `acceptance-check.md` | `deliverables/phase-5/acceptance-check.md` | 6/6 PASS |
| `agent-report.md` | `deliverables/phase-5/agent-report.md` | Relatório do agente |
| `phase-handoff.md` | `deliverables/phase-5/phase-handoff.md` | Este documento |

---

## Key Findings / Decisions

- **MVP = F01 + F03 + F04 + F05** no cenário de entrevista de emprego.
- **Feedback em tempo real (F08) e avaliação fonética (F09) foram adiados** — alto risco técnico.
- **Nenhuma tecnologia foi escolhida** — a Fase 6 deve avaliar ASR, LLM e TTS compatíveis com os riscos R-01, R-05, R-06.
- **O cenário "entrevista de emprego"** foi selecionado como o mais suportado pela evidência disponível, com a ressalva de que B-01 permanece formalmente em aberto.

---

## Unresolved Assumptions

| # | Assumption | Flagged in |
|---|-----------|-----------|
| B-01 | Situação prática prioritária — escolhida como "entrevista" para o MVP, mas sem confirmação primária | escopo-mvp.md Seção 2 |
| E-01 | Tecnologia de ASR/LLM/TTS não definida | escopo-mvp.md Seção 6 |

---

## Constraints for Next Phase (Fase 6 — Solução SMART e Validação)

- **Descrever a solução em nível conceitual** — sem implementar.
- **Definir objetivo SMART** com elementos concretos; marcar explicitamente como `[ALVO PROVISÓRIO]` qualquer número ou prazo não confirmado.
- **Tratar os 4 riscos altos (R-01, R-04, R-05, R-08) como restrições de design**, documentados no plano de validação.
- **O plano de validação deve testar H-01** — medir usabilidade (SUS), taxa de conclusão e ansiedade autorrelatada. **Fluência de idioma não é métrica do teste inicial.**
- **Separar métricas de usabilidade/aceitação de métricas de aprendizagem** — não confundir os dois tipos no plano de validação.
- **Cronograma:** incluir apenas se houver prazo real conhecido; caso contrário, apresentar etapas sem datas.

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| 5+ ideias/funcionalidades geradas | PASS |
| Priorização com rubrica documentada | PASS |
| Solução vencedora declarada com justificativa | PASS |
| Ideias rejeitadas explicadas | PASS |
| Suposições não resolvidas listadas | PASS |
| acceptance-check.md completo | PASS |

**Overall:** ✅ PASS — aguarda aprovação humana

---

## Instructions for Next Phase Agent (Solution Specifier)

1. Leia este handoff e `deliverables/phase-5/escopo-mvp.md` integralmente.
2. Leia `deliverables/phase-4/hipoteses.md` — a solução deve responder diretamente à H-01.
3. Leia `deliverables/phase-4/registro-de-riscos.md` — os riscos R-01, R-04, R-05, R-08 são restrições de design.
4. Descreva a solução em nível conceitual — não implemente, não escolha tecnologias sem necessidade.
5. O objetivo SMART deve ser específico, mensurável, atingível, relevante e temporal — marque prazos e quantidades como provisórias se não confirmadas.
6. O plano de validação deve testar H-01 com método definido — SUS, escala de ansiedade, tarefas de teste.
7. Separe métricas de usabilidade de métricas de aprendizagem.
