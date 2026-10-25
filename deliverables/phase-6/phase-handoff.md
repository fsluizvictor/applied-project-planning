# Phase Handoff — Fase 6: Solução SMART e Validação

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 6 |
| **Phase name** | Solução Proposta, Objetivo SMART, Escopo e Validação |
| **Responsible agent** | Solution Specifier |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz — a confirmar |
| **Phase status in PLAN.md** | Aguarda aprovação humana para marcar DONE |

---

## Summary of Work Done

O Solution Specifier descreveu a solução em nível conceitual, detalhou a jornada do usuário, definiu o objetivo SMART (prazo provisório), especificou escopo, premissas, restrições, dependências, requisitos funcionais (RF-01 a RF-10) e não funcionais (RNF-01 a RNF-05), e produziu um plano de validação com protocolo de teste, instrumentos (SUS + escala de ansiedade), critérios de decisão e limitações declaradas. Todos os 6 critérios de aceite passaram.

---

## Deliverables Produced

| File | Location | Description |
|------|----------|-------------|
| `solucao-proposta.md` | `deliverables/phase-6/solucao-proposta.md` | Solução conceitual + jornada do usuário |
| `objetivo-smart.md` | `deliverables/phase-6/objetivo-smart.md` | SMART completo; prazo provisório |
| `escopo-e-requisitos.md` | `deliverables/phase-6/escopo-e-requisitos.md` | Escopo, premissas, restrições, RF, RNF, rastreabilidade |
| `plano-de-validacao.md` | `deliverables/phase-6/plano-de-validacao.md` | Protocolo, instrumentos, critérios de decisão |
| `acceptance-check.md` | `deliverables/phase-6/acceptance-check.md` | 6/6 PASS |
| `agent-report.md` | `deliverables/phase-6/agent-report.md` | Relatório do agente |
| `phase-handoff.md` | `deliverables/phase-6/phase-handoff.md` | Este documento |

---

## Key Findings / Decisions

- **Solução MVP:** simulador de conversação por voz com IA, cenário de entrevista de emprego tech, com F01+F03+F04+F05.
- **Métricas de validação:** SUS ≥ 68, taxa de conclusão ≥ 60%, redução de ansiedade autorrelatada em >50% dos participantes. **Fluência de idioma não é métrica do teste.**
- **Prazo:** não confirmado — elemento T do SMART provisório (D-04).
- **Tecnologia não selecionada** — deve ser avaliada no início do desenvolvimento com ênfase em ASR para sotaque brasileiro.
- **4 restrições de design críticas:** ASR para sotaque (R-C-01), privacidade de áudio (R-C-02), latência (R-C-03), revisão do feedback (R-C-04).

---

## Unresolved Assumptions

| # | Assumption | Flagged in |
|---|-----------|-----------|
| D-03 | Política de dados das APIs de ASR | escopo-e-requisitos.md, R-C-02 |
| D-04 | Prazo real do projeto | objetivo-smart.md, elemento T |
| D-05 | Método de recrutamento de participantes | plano-de-validacao.md, Seção 3 |
| E-01 | Tecnologia ASR/LLM/TTS não selecionada | escopo-e-requisitos.md, Seção 4 |
| B-01 | Cenário prioritário — escolhido como "entrevista", não confirmado primariamente | escopo-mvp.md (Fase 5) |

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| Solução responde ao problema priorizado | PASS |
| Objetivo SMART com critérios mensuráveis | PASS |
| Escopo e exclusões explícitos | PASS |
| Validação testa H-01 com método | PASS |
| Limitações e riscos de IA por voz documentados | PASS |
| Requisitos com rastreabilidade | PASS |

**Overall:** ✅ PASS — aguarda aprovação humana

---

## Instructions for Next Phase Agent (Academic Reviewer — Fase 7)

> **Atenção:** a Fase 7 deve ser executada com **postura crítica e independente**. O revisor não deve presumir que as conclusões das fases anteriores estão corretas — deve auditá-las.

1. Leia **todos** os phase-handoffs das Fases 1 a 6 e os principais entregáveis de cada fase.
2. Compare os entregáveis com os 11 critérios de avaliação da disciplina (listados em `phases/07_revisao_final.md`).
3. Verifique rastreabilidade: o problema das personas leva à justificativa, que leva às hipóteses, que levam ao MVP, que leva ao plano de validação.
4. Identifique: afirmações sem suporte, citações não verificadas, métricas arbitrárias, contradições entre fases, lacunas não declaradas.
5. Verifique especialmente: (a) a distinção entre benefício esperado e resultado demonstrado está mantida ao longo de todos os documentos? (b) As métricas do teste validam H-01 sem confundir usabilidade com aprendizagem de idioma?
6. **Pontos de atenção específicos para auditoria:**
   - Fase 4: HMW statements ausentes — é uma falha relevante para a disciplina?
   - Fase 4: Convenção GUT (G+U+T vs. G×U×T) — qual é a correta para a disciplina?
   - Fase 6: Prazo (elemento T do SMART) provisório — é aceitável ou deve ser confirmado antes da proposta final?
   - Todas as fases: o cenário de viagem (lacuna B-03) foi explicitamente mantido como lacuna — isso é adequado ou deve ser endereçado?
7. Produzir relatório de auditoria **antes** de propor correções.
8. Não inventar informações para preencher lacunas — registrar o que depende do orientador ou de pesquisa futura.
