# Phase Handoff — Fase 3: Persona, Empatia e Observação

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 3 |
| **Phase name** | Persona, Empatia e Observação |
| **Responsible agent** | Persona & Empathy Specialist |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz — a confirmar |
| **Phase status in PLAN.md** | Aguarda aprovação humana para marcar DONE |

---

## Summary of Work Done

O agente Persona & Empathy Specialist leu todos os entregáveis das Fases 1 e 2, identificou dois perfis de persona provisórios (Ana Souza e Bruno Lima), construiu mapas de empatia a partir das evidências secundárias disponíveis e organizou uma matriz de observação com 14 linhas cobrindo os temas centrais do context-report.md. Nenhuma pesquisa primária foi conduzida; todas as inferências foram explicitamente identificadas. A suposição B-01 (situação prática prioritária do público-alvo) permanece em aberto.

---

## Deliverables Produced

| File | Location | Description |
|------|----------|-------------|
| `personas.md` | `deliverables/phase-3/personas.md` | Duas personas provisórias com perfil completo, dores, necessidades e situações de uso |
| `empathy-maps.md` | `deliverables/phase-3/empathy-maps.md` | Mapa de empatia completo (Ana Souza) e resumido (Bruno Lima); síntese comparativa |
| `observation-matrix.md` | `deliverables/phase-3/observation-matrix.md` | Matriz com 14 linhas; 10 respondidas, 1 parcial, 3 em aberto |
| `decision-log.md` | `deliverables/phase-3/decision-log.md` | Decisões 007–010 |
| `agent-report.md` | `deliverables/phase-3/agent-report.md` | Relatório do agente com autoavaliação e suposições pendentes |
| `acceptance-check.md` | `deliverables/phase-3/acceptance-check.md` | 6/6 critérios de fase PASS; 6/6 globais PASS |
| `phase-handoff.md` | `deliverables/phase-3/phase-handoff.md` | Este documento |

---

## Key Findings / Decisions

- **Convergência central das duas personas:** ambas compartilham a necessidade de prática conversacional de baixa pressão, em cenários práticos realistas, com feedback imediato. Essa convergência é o fundamento da solução a ser especificada.
- **Barreira dominante é psicológica (ansiedade, medo de errar)**, não puramente linguística — confirmado por múltiplas fontes secundárias. A solução deve abordar isso explicitamente.
- **Ana Souza** (profissional de tecnologia) é a persona principal — maior volume de evidência disponível sobre o perfil; foco em entrevistas de emprego e reuniões internacionais.
- **Bruno Lima** (estudante/iniciante) é a persona secundária — nível de ansiedade mais alto, experiência oral quase nula, representativa do sistema educacional brasileiro.
- **Situação prática prioritária (B-01) ainda não confirmada** — a Fase 4 deve formular hipótese testável que lide com essa incerteza explicitamente.
- **Limitação de ASR para sotaque brasileiro** é risco documentado (JEON; LEE; CORONEL-MOLINA, 2024; VERHELST; BELPAEME, 2025) — deve ser endereçado como restrição de design na Fase 6.
- **Resultados de eficácia de chatbots não são uniformes** (CHEN et al., 2024 não encontrou diferença significativa) — o design da solução não pode assumir eficácia garantida.

---

## Unresolved Assumptions

| # | Assumption | Flagged in |
|---|-----------|-----------|
| B-01 | [ASSUMPTION — requires validation]: Situação prática prioritária para o público-alvo real não confirmada | personas.md Seção 1.2; observation-matrix.md Tema 6 |
| B-02 | [LACUNA DE EVIDÊNCIA]: Relatório primário Pearson não acessado | personas.md; context-report.md |
| B-03 | [LACUNA DE EVIDÊNCIA]: Sem evidência sobre cenário de viagem | observation-matrix.md Tema 6 |
| B-04 | [LACUNA DE EVIDÊNCIA]: Evidência de eficácia de chatbots não vem de contexto brasileiro | observation-matrix.md Tema 4 |
| C-01 | [ASSUMPTION — requires validation]: Qual das duas personas é o público prioritário | personas.md Seção 3 |
| C-02 a C-05 | Traços de perfil inferidos (idade, ocupação, ferramenta, dispositivo) — não validados com dados primários | personas.md Seção 3 |

---

## Constraints for Next Phase (Fase 4 — Justificativa, Hipóteses e Riscos)

- O agente da Fase 4 **deve** ler este handoff e `deliverables/phase-3/personas.md` e `deliverables/phase-3/empathy-maps.md` antes de produzir qualquer output.
- A hipótese principal deve ser formulada de forma **testável e refutável** — não pode ser uma afirmação de que a solução melhora fluência sem teste empírico adequado.
- A **justificativa** deve derivar das dores e necessidades documentadas nas personas (com rastreabilidade às fontes secundárias da Fase 2), não de promessas tecnológicas genéricas sobre IA.
- A **matriz de riscos** deve incluir obrigatoriamente: viés de ASR para sotaque não nativo, heterogeneidade de resultados de chatbots, ansiedade aumentada por contexto avaliativo, custos de API de IA, privacidade de áudio.
- A suposição B-01 deve ser explicitamente endereçada: a hipótese pode cobrir múltiplos cenários, mas deve indicar qual é o cenário de teste primário e por quê.
- **Não avançar para a Fase 5 na mesma sessão** — aguardar aprovação humana da Fase 4.

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| Ao menos 2 personas distintas | PASS |
| Personas fundamentadas em Fase 2 | PASS |
| Mapa de empatia com todos os quadrantes | PASS |
| Matriz de observação com fontes reais | PASS |
| Suposições não resolvidas listadas | PASS |
| acceptance-check.md completo | PASS |

**Overall:** ✅ PASS — aguarda aprovação humana (Luiz) para marcar DONE em PLAN.md

---

## Instructions for Next Phase Agent (Hypothesis & Risk Analyst)

1. Leia este handoff em sua totalidade antes de iniciar.
2. Leia `deliverables/phase-3/personas.md` e `deliverables/phase-3/empathy-maps.md` — especialmente a Síntese Comparativa e as Questões a Validar.
3. Leia `deliverables/phase-3/observation-matrix.md` — atenção especial ao Tema 4 (eficácia de chatbots) e Tema 5 (limitações técnicas).
4. Leia `deliverables/phase-2/context-report.md`, Seções 5.2 e 6 (limitações e lacunas).
5. Reconheça explicitamente as suposições B-01, B-04, C-01 no início do seu trabalho.
6. Confirme que a Fase 3 está marcada DONE em PLAN.md antes de começar (após aprovação humana).
7. Limite seu trabalho ao escopo da Fase 4: justificativa, hipóteses, riscos — não ideie soluções nem especifique MVP.
