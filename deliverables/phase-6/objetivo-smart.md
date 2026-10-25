# Objetivo SMART — Fase 6: Solução SMART e Validação

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Curso:** Pós-Graduação em Arquitetura de Software e Soluções com IA
**Agente responsável:** Solution Specifier
**Data:** 25 de outubro de 2026
**Versão:** 1.1 (atualizado com curso — UA-01)

---

## Objetivo SMART

> **Desenvolver e testar um protótipo de simulador de conversação em inglês por voz com IA** — focado no cenário de entrevista de emprego na área de tecnologia —, capaz de ser considerado útil e utilizável pelo público-alvo (S), medido por pontuação SUS ≥ 68, taxa de conclusão de tarefa ≥ 60% e redução de ansiedade autorrelatada em mais da metade dos participantes (M), por meio da implementação de um fluxo de conversação com ASR + LLM + TTS e feedback estruturado pós-conversa, utilizando tecnologias disponíveis publicamente (A), com o propósito de validar se a abordagem de conversação de baixa pressão com IA endereça a barreira central de prática oral identificada nas Fases 2 e 3 (R), **em prazo a confirmar com o orientador** `[ALVO PROVISÓRIO — T]` (T).

---

## Detalhamento dos Elementos SMART

### S — Específico

| Campo | Valor |
|-------|-------|
| **O quê** | Protótipo de simulador de conversação em inglês por voz com IA |
| **Para quem** | Profissionais de tecnologia com inglês intermediário que precisam praticar para entrevistas de emprego (perfil Ana Souza) |
| **Contexto** | Cenário de entrevista de emprego na área de tecnologia — único cenário do MVP |
| **Resultado esperado** | Validar se a ferramenta é percebida como útil, utilizável e redutora de ansiedade em pelo menos uma sessão de teste supervisionada |

---

### M — Mensurável

| Indicador | Valor alvo | Instrumento de coleta | Status do alvo |
|-----------|------------|----------------------|----------------|
| Pontuação SUS (System Usability Scale) | ≥ 68 | Questionário SUS de 10 itens (Brooke, 1996) aplicado pós-sessão | `[ALVO PROVISÓRIO]` — ponto de corte padrão da literatura |
| Taxa de conclusão de tarefa principal sem assistência | ≥ 60% | Observação moderada durante o teste | `[ALVO PROVISÓRIO]` — sem base específica para este tipo de protótipo |
| Mudança na ansiedade autorrelatada (pré vs. pós sessão) | Maioria dos participantes (>50%) relata redução | Escala Likert de 5 pontos customizada ou adaptação da FLSAS — aplicada antes e depois da sessão | `[ALVO PROVISÓRIO]` — baseado em estudos de referência, não no contexto específico deste projeto |
| Percepção de utilidade | Maioria dos participantes relata que usaria a ferramenta para prática | Questão direta no questionário pós-sessão | `[ALVO PROVISÓRIO]` |

> **Separação de métricas:** os indicadores acima são de **usabilidade e aceitação**. Fluência, proficiência ou aprendizagem de idioma **não são métricas deste teste** — uma única sessão não é suficiente para detectar melhoria de fluência de forma confiável e cientificamente válida.

---

### A — Atingível

A viabilidade técnica é **plausível** com base nas seguintes condições:
- Existem APIs de ASR publicamente disponíveis que suportam inglês com razoável qualidade (Whisper OpenAI, Google STT, Azure STT) — a avaliação de desempenho para sotaque brasileiro é etapa obrigatória do desenvolvimento.
- Existem APIs de LLM publicamente disponíveis adequadas para o fluxo de conversação (OpenAI GPT-4o, Google Gemini, Anthropic Claude).
- Existem APIs de TTS publicamente disponíveis (ElevenLabs, Google TTS, OpenAI TTS).
- A interface pode ser construída como aplicação web simples.

> `[ASSUMPTION — requires validation — E-01]`: A viabilidade técnica afirma que essas APIs existem e são acessíveis; não afirma que a combinação específica atingirá a qualidade necessária para o teste sem ajustes. A avaliação técnica é etapa do desenvolvimento do protótipo, não desta fase acadêmica.

---

### R — Relevante

O objetivo é relevante porque:
1. Responde diretamente ao problema central identificado na Fase 2: falta de oportunidades de prática oral de baixa pressão.
2. Testa a hipótese H-01 formulada na Fase 4 com método de coleta definido.
3. O resultado do teste — positivo ou negativo — é valioso: se positivo, justifica investimento em desenvolvimento; se negativo, indica necessidade de redesenho antes de escalar.
4. Está alinhado ao contexto de demanda profissional por inglês documentado pelas evidências secundárias (EF EPI 2025, Pearson 2024).

---

### T — Temporal

> **⚠️ Prazo não confirmado:** nenhum prazo real foi fornecido pelo orientador ou pela disciplina até o momento desta fase. Portanto, não é possível comprometer uma data sem fabricar informação. O prazo é registrado como `[ALVO PROVISÓRIO — requires validation — D-04]`.

**Etapas propostas (sem datas):**

| Etapa | Descrição | Dependência |
|-------|-----------|------------|
| 1 | Definição e teste de tecnologias (ASR, LLM, TTS) — avaliação de desempenho para sotaque brasileiro | Nenhuma |
| 2 | Desenvolvimento do protótipo MVP (F01, F03, F04, F05) | Etapa 1 |
| 3 | Revisão interna do feedback gerado pela IA (prompt engineering + revisão pedagógica) | Etapa 2 |
| 4 | Recrutamento de participantes para o teste (5–8 com perfil Ana Souza) | Etapas 1–2 |
| 5 | Sessão de teste de usabilidade supervisionada | Etapas 2–4 |
| 6 | Análise dos dados e decisão (iterar, pivotar ou escalar) | Etapa 5 |

> Se o orientador ou a disciplina fornecer prazos reais, este documento deve ser atualizado com datas concretas substituindo as etapas genéricas acima.
