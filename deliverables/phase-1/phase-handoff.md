# Phase Handoff — Fase 1: Planejamento e Análise de Requisitos

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 1 |
| **Phase name** | Planejamento e Análise de Requisitos |
| **Responsible agent** | Requirements Analyst |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz |
| **Phase status in PLAN.md** | ✅ DONE |

---

## Summary of Work Done

O agente de Requisitos leu todos os arquivos internos do projeto e o **PDF de exemplo de proposta aprovada** (`Exemplo - Desafio - Solução.pdf`). Os 11 critérios de avaliação foram mapeados para fases, entregáveis e seções concretas do documento final, com base nos rótulos de `phases/01_planejamento.md` e na estrutura do PDF de exemplo. A rubrica completa com descritores de nível permanece ausente — registrado como lacuna aberta (A-02). Todas as premissas não resolvidas foram documentadas explicitamente.

---

## Deliverables Produced

| Arquivo | Localização | Descrição |
|---------|------------|-----------|
| `requirements.md` | `deliverables/phase-1/requirements.md` | Documento principal: escopo, stakeholders, restrições, mapeamento dos 11 critérios, premissas não resolvidas |
| `source-inventory.md` | `deliverables/phase-1/source-inventory.md` | Inventário de fontes lidas e fontes ausentes |
| `decision-log.md` | `deliverables/phase-1/decision-log.md` | Log de três decisões tomadas nesta fase |
| `agent-report.md` | `deliverables/phase-1/agent-report.md` | Relatório do agente com auto-avaliação |
| `acceptance-check.md` | `deliverables/phase-1/acceptance-check.md` | Verificação de aceite (aguardando aprovação humana) |
| `phase-handoff.md` | `deliverables/phase-1/phase-handoff.md` | Este documento |

---

## Key Findings / Decisions

- O **PDF de exemplo** foi lido integralmente. A estrutura do documento final está definida: `1.1 Desafio` (Análise de Contexto → Personas → Justificativas → Hipóteses com tabela GUT) e `1.2 Solução` (Objetivo SMART → Escopo → Cronograma).
- Os 11 critérios foram mapeados para seções concretas do documento e fases do projeto (ver `requirements.md`, Seção 5.2).
- A **Matriz de Observação** (critério 1.1.8) corresponde à tabela GUT (Gravidade, Urgência, Tendência — escala 1 a 5) integrada na seção de Hipóteses.
- As **personas** exigem figuras visuais (Perfil Comportamental + Mapa de Empatia) — a Fase 3 deve definir como produzi-las em Markdown/PDF (premissa A-09).
- A **rubrica com descritores de nível** continua ausente (A-02) — afeta apenas a Fase 7; não bloqueia as fases intermediárias.
- Nove premissas registradas; A-03 foi fechada com a leitura do PDF de exemplo.
- A estrutura `deliverables/phase-N/` foi adotada em detrimento de `docs/` por consistência com o harness (Decisão 001).
- Os placeholders de critérios em `AGENTS.md` **não foram atualizados** — ação exclusiva do usuário (Decisão 003).

---

## Unresolved Assumptions

| # | Premissa | Flagged em |
|---|----------|------------|
| A-01 | [ASSUMPTION — requires validation]: Prazo de entrega da disciplina desconhecido | `requirements.md`, Seção 7 |
| A-02 | [ASSUMPTION — requires validation]: Rubrica completa com descritores de nível não disponível | `requirements.md`, Seções 5 e 7; `source-inventory.md` |
| A-03 | ~~[ASSUMPTION — requires validation]: PDF de exemplo não localizado~~ | ✅ FECHADA — PDF lido em 25/10/2026 |
| A-04 | [ASSUMPTION — requires validation]: Nome da disciplina, instituição e semestre não informados | `requirements.md`, Seção 7 |
| A-05 | [ASSUMPTION — requires validation]: Trabalho individual ou em grupo não especificado | `requirements.md`, Seção 7 |
| A-06 | [ASSUMPTION — requires validation]: Número mínimo de referências bibliográficas não informado | `requirements.md`, Seção 7 |
| A-07 | [ASSUMPTION — requires validation]: Obrigatoriedade de pesquisa primária não confirmada | `requirements.md`, Seção 7 |
| A-08 | [ASSUMPTION — requires validation]: Área do conhecimento do curso não confirmada pelo usuário | `requirements.md`, Seções 6 e 7 |
| A-09 | [ASSUMPTION — requires validation]: Personas exigem figuras visuais no documento final (Perfil Comportamental + Mapa de Empatia como imagens); formato de entrega em Markdown/PDF a definir | `requirements.md`, Seção 7 |

---

## Constraints for Next Phase (Fase 2 — Context & Research)

- O agente da Fase 2 (Context Researcher) **deve** ler este handoff e `requirements.md` antes de produzir qualquer output.
- Todas as nove premissas acima devem ser **reconhecidas** no início do trabalho da Fase 2 (exceto A-03, fechada).
- As fontes bibliográficas pesquisadas na Fase 2 devem ser **reais e verificáveis** — nenhuma citação inventada.
- A pesquisa deve cobrir o contexto do problema (barreiras à prática de inglês conversacional) e o estado da arte em simuladores de conversação com IA.
- Se a rubrica completa (A-02) for fornecida antes da Fase 2, o Context Researcher deve incorporar seus descritores ao planejamento da pesquisa.
- Não é permitido antecipar personas, ideação ou especificação de solução nesta fase.

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| Escopo documentado sem invenção | PASS |
| Pelo menos 2 grupos de stakeholders | PASS |
| Pelo menos uma restrição por critério | PASS (baseado em rótulos + PDF de exemplo) |
| Premissas não resolvidas presentes | PASS |
| Sem fabricação de fontes | PASS |
| 11 critérios endereçados ou sinalizados | PASS |
| Redigido em português brasileiro | PASS |
| G1–G6 (critérios globais) | PASS |

**Overall:** ✅ PASS — aprovação humana necessária antes de avançar para a Fase 2.

---

## Instructions for Next Phase Agent (Context Researcher)

1. Leia este handoff em sua totalidade antes de iniciar.
2. Leia `deliverables/phase-1/requirements.md` completo, com atenção especial às Seções 5, 6 e 7.
3. Reconheça explicitamente as oito premissas não resolvidas (A-01 a A-08) no início do seu trabalho.
4. Confirme que a Fase 1 está marcada como DONE em `PLAN.md` antes de começar.
5. Limite seu trabalho ao escopo da Fase 2: contexto, pesquisa e fontes.
6. Não conduza ideação, criação de personas ou especificação de solução.
