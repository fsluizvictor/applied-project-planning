# Phase Handoff — Fase 2: Análise de Contexto e Pesquisa

---

## Handoff Metadata

| Field | Value |
|-------|-------|
| **Phase number** | 2 |
| **Phase name** | Análise de Contexto e Pesquisa |
| **Responsible agent** | Context Researcher |
| **Date completed** | 2026-10-25 |
| **Human who approved** | Luiz |
| **Phase status in PLAN.md** | ✅ DONE |

---

## Summary of Work Done

O Context Researcher leu todos os entregáveis da Fase 1 e o brief original (`phases/02_contexto_problema.md`) e conduziu pesquisa bibliográfica real via busca na web, reunindo dezoito fontes verificáveis sobre barreiras à produção oral em inglês, o contexto brasileiro, soluções comerciais existentes e a eficácia e as limitações de chatbots de IA em prática de conversação. Produziu-se um relatório de contexto completo, incluindo perguntas de pesquisa, roteiro de entrevista para validação futura e um desafio preliminar centrado no usuário — este último explicitamente não definitivo. Nenhuma pesquisa primária foi conduzida; todas as lacunas correspondentes foram sinalizadas.

---

## Deliverables Produced

| File | Location | Description |
|------|----------|-------------|
| `context-report.md` | `deliverables/phase-2/context-report.md` | Relatório principal de contexto, pesquisa e lacunas |
| `agent-report.md` | `deliverables/phase-2/agent-report.md` | Relatório do agente com autoavaliação |
| `decision-log.md` | `deliverables/phase-2/decision-log.md` | Decisões 004–006 (continuação da Fase 1) |
| `acceptance-check.md` | `deliverables/phase-2/acceptance-check.md` | Verificação de aceite (8 PASS, 1 PARTIAL); aguardando aprovação humana |
| `phase-handoff.md` | `deliverables/phase-2/phase-handoff.md` | Este documento |

---

## Key Findings / Decisions

- A barreira mais documentada à produção oral em inglês, segundo a literatura revisada, é predominantemente **psicológica e ambiental** (ansiedade, falta de oportunidades de prática), não exclusivamente linguística.
- No Brasil, dados do EF EPI 2025 e de estudos acadêmicos locais confirmam que a fala é a habilidade mais fraca e a menos praticada em sala de aula.
- A literatura sobre chatbots de IA mostra efeito positivo médio sobre desempenho em fala (meta-análise: g = 0,484), mas com limitações técnicas relevantes: reconhecimento de fala enviesado contra sotaques não nativos, coerência conversacional limitada e retroalimentação corretiva insuficiente.
- Nenhuma fonte foi localizada sobre uso de simuladores de IA especificamente no cenário de viagem; essa é uma lacuna explícita.
- Um artigo originalmente localizado foi descartado por ter sido formalmente retratado pelo periódico (Decisão 006) — a próxima fase que realizar busca bibliográfica adicional deve continuar verificando esse tipo de status.
- A relação entre público-alvo e situação prática prioritária (viagem vs. entrevista vs. trabalho vs. cotidiano) **não está confirmada por nenhuma evidência** — permanece suposição aberta (B-01), responsável pelo único critério de aceite com resultado PARTIAL nesta fase.

---

## Unresolved Assumptions

| # | Assumption | Flagged in |
|---|-----------|-----------|
| B-01 | [ASSUMPTION — requires validation]: Situação prática prioritária para o público-alvo real não confirmada | `context-report.md`, Seções 3.3 e 11 |
| B-02 | [LACUNA DE EVIDÊNCIA]: Relatório primário da pesquisa Pearson (2024) não acessado diretamente | `context-report.md`, Seções 3.2 e 11 |
| B-03 | [LACUNA DE EVIDÊNCIA]: Nenhuma fonte sobre IA conversacional em contexto de viagem | `context-report.md`, Seções 3.3 e 11 |
| B-04 | [LACUNA DE EVIDÊNCIA]: Evidência de eficácia de chatbots vem de contextos nacionais distintos do Brasil | `context-report.md`, Seções 5.1 e 11 |
| B-05 | Nenhuma pesquisa primária foi conduzida nesta fase | `context-report.md`, Seções 7 e 12 |
| B-06 | [DADO-NÃO-VERIFICADO]: Afirmações de eficácia de ferramentas comerciais não verificadas de forma independente | `context-report.md`, Seções 4 e 11 |
| — | Premissas herdadas da Fase 1 (A-01, A-02, A-04 a A-09) permanecem abertas | `deliverables/phase-1/requirements.md`, Seção 7 |

---

## Constraints for Next Phase (Fase 3 — Persona, Empatia e Observação)

- O agente da Fase 3 (`persona-empathy`) **deve** ler este handoff e `context-report.md` completo antes de produzir qualquer output.
- Nenhuma persona pode ser apresentada como baseada em pesquisa primária real — toda a base disponível até aqui é literatura secundária. Se personas forem criadas com traços inferidos, isso deve ser sinalizado como `[ASSUMPTION]`, conforme a regra `01-academic-integrity.mdc` e o próprio `.cursor/agents/persona-empathy.md`.
- A suposição B-01 (situação prática prioritária) deve ser explicitamente tratada pela Fase 3: ou a persona cobre múltiplas situações de forma sinalizada como hipotética, ou a Fase 3 recomenda que essa lacuna seja resolvida antes de prosseguir.
- A Matriz de Observação (ver Seção 5.1 de `deliverables/phase-1/requirements.md`, que a associa à tabela GUT) deve ser construída a partir das fontes secundárias já reunidas em `context-report.md`, Seção 10, não de novas fontes inventadas.
- A premissa A-09 (formato das figuras de persona e mapa de empatia) permanece aberta e deve ser resolvida nesta fase, conforme já indicado no handoff da Fase 1.

---

## Acceptance Check Result

| Critério | Resultado |
|----------|-----------|
| Fontes reais e verificáveis | PASS |
| Mínimo de cinco fontes | PASS |
| Tags de evidência consistentes | PASS |
| Lacunas documentadas | PASS |
| Limitações reconhecidas | PASS |
| Nenhum dado inventado | PASS |
| Contexto identifica público, situações, necessidades, lacunas | PARTIAL |
| Problema descrito sem confundir com solução | PASS |
| Roteiro de pesquisa permite validar o problema | PASS |
| G1–G6 (critérios globais) | PASS |

**Overall:** ✅ APROVADO por Luiz em 25/10/2026, com um critério PARTIAL (critério 7) aceito como lacuna documentada (B-01), não como falha. A Fase 2 está marcada `DONE` em `PLAN.md`. A Fase 3 não deve começar nesta mesma sessão — aguarda nova instrução explícita.

---

## Instructions for Next Phase Agent (Persona & Empathy Specialist)

1. Leia este handoff em sua totalidade antes de iniciar.
2. Leia `deliverables/phase-2/context-report.md` completo, com atenção especial às Seções 3.3, 6, 7, 8 e 11.
3. Reconheça explicitamente as suposições B-01 a B-06 no início do seu trabalho.
4. Confirme que a Fase 2 está marcada como DONE em `PLAN.md` (após aprovação humana) antes de começar.
5. Limite seu trabalho ao escopo da Fase 3: personas, mapas de empatia e matriz de observação, com base em evidência secundária já reunida — não conduza ideação nem especificação de solução.
6. Não trate o "desafio preliminar" da Seção 8 de `context-report.md` como definição final — ele será formalizado na Fase 4.
