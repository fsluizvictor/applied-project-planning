# Phase Handoff — Fase 4: Justificativa, Hipóteses e Riscos

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 4 |
| **Phase name** | Justificativa, Hipóteses e Riscos |
| **Responsible agent** | Hypothesis & Risk Analyst |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz — a confirmar |
| **Phase status in PLAN.md** | Aguarda aprovação humana para marcar DONE |

---

## Summary of Work Done

O agente Hypothesis & Risk Analyst leu todos os entregáveis das Fases 1 a 3, construiu a justificativa do projeto com rastreabilidade explícita às fontes da Fase 2, formulou três hipóteses testáveis e refutáveis (sendo H-01 a hipótese principal), e produziu um registro de oito riscos com scoring GUT, mitigação e risco residual. Um critério de aceite ficou PARTIAL (HMW statements ausentes) — não bloqueia o avanço se aprovado pelo revisor humano.

---

## Deliverables Produced

| File | Location | Description |
|------|----------|-------------|
| `justificativa.md` | `deliverables/phase-4/justificativa.md` | Justificativa com separação explícita entre benefícios esperados e resultados demonstrados |
| `hipoteses.md` | `deliverables/phase-4/hipoteses.md` | H-01 (principal), H-02 e H-03 com GUT, método de teste e condição de refutação |
| `registro-de-riscos.md` | `deliverables/phase-4/registro-de-riscos.md` | 8 riscos; 4 altos: R-01 (ASR), R-04 (privacidade), R-05 (latência), R-08 (feedback de IA) |
| `acceptance-check.md` | `deliverables/phase-4/acceptance-check.md` | 5/6 PASS, 1 PARTIAL |
| `agent-report.md` | `deliverables/phase-4/agent-report.md` | Relatório do agente |
| `phase-handoff.md` | `deliverables/phase-4/phase-handoff.md` | Este documento |

---

## Key Findings / Decisions

- **Hipótese principal (H-01):** um protótipo de simulador de conversação por voz com IA para entrevistas de emprego será considerado útil, utilizável e reduzirá a ansiedade autorrelatada em pelo menos uma sessão de teste com o perfil Ana Souza.
- **Critério de sucesso:** SUS ≥ 68, taxa de conclusão ≥ 60%, maioria relata redução de ansiedade — todos **provisórios**, precisam ser confirmados.
- **4 riscos de classificação Alta** que devem ser tratados como restrições de design na Fase 6: ASR para sotaque brasileiro (R-01), privacidade de áudio (R-04), latência (R-05), qualidade pedagógica do feedback (R-08).
- **Fluência não é métrica do protótipo** — claramente documentado para não ser confundido na Fase 7.
- **HMW statements ausentes** — podem ser adicionadas antes da Fase 7 se necessário.

---

## Unresolved Assumptions

| # | Assumption | Flagged in |
|---|-----------|-----------|
| D-01 | [ASSUMPTION]: Convenção GUT (G+U+T vs. G×U×T) a confirmar | hipoteses.md, registro-de-riscos.md |
| D-02 | [ASSUMPTION]: Número de participantes do teste (5–8) provisório | hipoteses.md, Seção H-01 |
| B-01 (herdada) | Situação prática prioritária não confirmada | Resolvida parcialmente: H-01 foca em entrevista de emprego, mas B-01 permanece formalmente aberta |
| B-04 (herdada) | Evidência de eficácia não é do contexto brasileiro | registro-de-riscos.md, R-02 |

---

## Constraints for Next Phase (Fase 5 — Priorização e MVP)

- **A Fase 5 deve decidir explicitamente qual cenário entra no MVP** — dado que B-01 permanece aberta e H-01 aponta entrevista de emprego como cenário de teste primário, mas isso não está formalmente confirmado.
- **Os 4 riscos altos (R-01, R-04, R-05, R-08) devem ser considerados** ao avaliar o esforço e a viabilidade de cada funcionalidade candidata — funcionalidades que dependem de ASR intensivo ou feedback complexo têm risco técnico elevado.
- **A distinção entre funcionalidades essenciais para testar H-01 e funcionalidades desejáveis** deve ser o critério de corte do MVP.
- **Não avançar para a Fase 6 na mesma sessão** — aguardar aprovação humana da Fase 5.

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| Ao menos 3 insights derivados da Fase 3 | PASS |
| Ao menos 2 HMW statements | PARTIAL (ausentes) |
| Ao menos 3 hipóteses testáveis | PASS |
| Registro de riscos com GUT | PASS |
| Suposições não resolvidas listadas | PASS |
| acceptance-check.md completo | PASS |

**Overall:** ⚠️ PARTIAL — aguarda decisão do revisor humano sobre HMW statements

---

## Instructions for Next Phase Agent (Idea Prioritizer)

1. Leia este handoff e `deliverables/phase-4/hipoteses.md` integralmente — especialmente H-01 e os critérios de sucesso.
2. Leia `deliverables/phase-4/registro-de-riscos.md` — os 4 riscos altos são restrições de design que afetam diretamente a viabilidade de funcionalidades.
3. Leia `deliverables/phase-3/personas.md` — a síntese comparativa das personas é o ponto de partida para geração de funcionalidades candidatas.
4. O critério central de priorização é: **quais funcionalidades são estritamente necessárias para testar a hipótese H-01?**
5. Não selecione tecnologias específicas prematuramente.
6. Documente explicitamente as funcionalidades descartadas e o porquê.
7. Confirme que a Fase 4 está DONE em PLAN.md antes de começar.
