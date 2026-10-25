# Hipóteses — Fase 4: Justificativa, Hipóteses e Riscos

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Hypothesis & Risk Analyst
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## Nota Metodológica

As hipóteses a seguir seguem o padrão da tabela GUT (Gravidade, Urgência, Tendência) adotado no PDF de referência do projeto (`Exemplo - Desafio - Solução.pdf`), conforme identificado na Fase 7. Cada hipótese descreve uma observação (problema constatado) e a solução candidata, avaliada nos critérios GUT de 1 a 5.

### Escala GUT utilizada

| Pontuação | Gravidade (G) | Urgência (U) | Tendência (T) |
|-----------|---------------|--------------|---------------|
| 5 | Extremamente grave — impede o progresso ou causa dano severo | Precisa de ação imediata (dias) | Piora rapidamente se não tratado |
| 4 | Muito grave — impacto significativo | Precisa de ação em semanas | Piora progressivamente |
| 3 | Grave — impacto moderado | Pode esperar algumas semanas | Tende a se manter se não tratado |
| 2 | Pouco grave — impacto limitado | Pode esperar meses | Melhora sozinho se ignorado |
| 1 | Sem gravidade relevante | Sem urgência | Sem tendência de piora |

**Fórmula:** Somatório = G + U + T (1–15 pontos)
**Classificação de risco:** Baixo: 3–6 | Médio: 7–10 | Alto: 11–15

> **Nota de transparência:** Esta convenção GUT foi adotada por analogia ao exemplo de referência da disciplina. Caso a disciplina especifique outra fórmula (ex.: G × U × T), este documento deve ser atualizado — registrado como `[ASSUMPTION — requires validation]` (D-01).

---

## Hipótese Principal (H-01)

### Observação
Pessoas que precisam utilizar inglês em situações práticas (entrevistas de emprego, reuniões profissionais, interações cotidianas) carecem de oportunidades acessíveis, flexíveis e de baixa pressão para praticar a produção oral, o que perpetua a ansiedade de fala e a baixa disposição para comunicar (WTC).

### Descrição da Hipótese
Um protótipo de simulador de conversação por voz com IA, baseado em situações práticas do cotidiano profissional (pelo menos o cenário de entrevista de emprego em inglês), será considerado **útil e utilizável** pelo público-alvo — representado pela persona Ana Souza — em pelo menos uma sessão de teste supervisionada, e reduzirá a ansiedade de fala autorrelatada em comparação ao estado inicial.

> **Condição de refutação:** A hipótese é refutada se, após a sessão de teste, a maioria dos participantes (>50%) indicar que a ferramenta não é útil ou utilizável, ou se a ansiedade autorrelatada não diminuir (ou aumentar).

### Critérios de Avaliação (GUT)

| Observação | G | U | T | Somatório | Grau de Risco |
|-----------|---|---|---|-----------|---------------|
| Falta de oportunidades de prática oral de baixa pressão e acessível | 5 | 4 | 5 | 14 | **Alto** |

**Justificativa dos valores:**
- **G=5:** A ausência de prática oral perpetua diretamente a barreira documentada: ansiedade de fala, baixo WTC e baixa proficiência — impacto severo sobre mobilidade profissional e educacional.
- **U=4:** O mercado de trabalho exige inglês de forma crescente e imediata; quanto mais cedo a prática for incorporada, maior o benefício acumulado.
- **T=5:** Sem intervenção, a tendência é de agravamento: o sistema escolar não corrigiu o problema (BATISTA, 2020) e o mercado de trabalho exige cada vez mais proficiência (PEARSON, 2024 apud DIRETTRIX, 2024).

### Método de Teste

| Campo | Descrição |
|-------|-----------|
| **Instrumento** | Sessão de teste de usabilidade estruturada + escala de ansiedade autorrelatada (ex.: adaptação da FLSAS — Foreign Language Speaking Anxiety Scale, ou escala Likert de 5 pontos customizada) |
| **Participantes** | 5 a 8 participantes com perfil similar à persona Ana Souza (profissional de tecnologia, inglês intermediário, necessidade de uso em contexto profissional) — número `[ASSUMPTION — requires validation — D-02]` |
| **Tarefas de teste** | (1) Selecionar cenário de entrevista de emprego; (2) conduzir simulação de 5–10 minutos; (3) receber feedback da IA; (4) responder questionário de usabilidade (SUS ou similar) e escala de ansiedade |
| **Indicadores** | Taxa de conclusão de tarefa; pontuação de usabilidade (SUS ≥ 68 = aceitável `[ASSUMPTION — requires validation]`); mudança na ansiedade autorrelatada (pré vs. pós) |
| **Regra de interpretação** | A hipótese é suportada se: ≥60% dos participantes completa a tarefa sem assistência; SUS ≥ 68; e a maioria (>50%) relata redução de ansiedade. A hipótese é refutada se qualquer desses três critérios falhar de forma consistente. |
| **Separação de métricas** | Usabilidade e aceitação são métricas válidas para este teste. **Fluência e aprendizagem de idioma NÃO serão medidas** — uma única sessão não é suficiente para detectar melhoria de fluência de forma confiável. |

---

## Hipótese Secundária (H-02)

### Observação
Aprendizes com baixa experiência de conversação oral formal (perfil Bruno Lima) evitam praticar fala em ambientes que percebem como avaliativos ou de alta pressão.

### Descrição da Hipótese
Um ambiente de simulação com IA, percebido como não avaliativo e sem julgamento humano, aumentará a disposição do público-alvo de perfil Bruno Lima para iniciar a prática oral, em comparação à percepção atual de prática com humanos ou em sala de aula.

> **Condição de refutação:** A hipótese é refutada se os participantes com perfil Bruno Lima indicarem que a interação com a IA gera tanta ou mais ansiedade do que a prática com humanos (resultado plausível dado que chatbots em contexto avaliativo podem aumentar ansiedade — KOÇ; SAVAŞ, 2024).

### Critérios de Avaliação (GUT)

| Observação | G | U | T | Somatório | Grau de Risco |
|-----------|---|---|---|-----------|---------------|
| Evitação de prática oral por percepção de alta pressão em contextos humanos | 4 | 3 | 4 | 11 | **Alto** |

**Justificativa dos valores:**
- **G=4:** Afeta diretamente o grupo com menor proficiência oral — aqueles que mais se beneficiariam de prática.
- **U=3:** Menos urgente que H-01 porque este perfil ainda tem tempo de formação; porém, o padrão de evitação, se cristalizado, torna-se mais difícil de reverter.
- **T=4:** Sem intervenção, a evitação tende a persistir ou aumentar — o perfil escolar brasileiro não oferece mecanismos de reversão (CORRÊA, 2017).

### Método de Teste

| Campo | Descrição |
|-------|-----------|
| **Instrumento** | Questionário de percepção de pressão (escala Likert, pré e pós interação com protótipo) comparado à percepção de prática com humanos |
| **Participantes** | 3 a 5 participantes com perfil Bruno Lima (estudante ou recém-formado, pouca/nenhuma experiência oral formal) `[ASSUMPTION — requires validation — D-02]` |
| **Indicador** | Diferença entre pontuação de ansiedade percebida "com IA" vs. "com humano nativo" |
| **Regra de interpretação** | H-02 é suportada se a maioria dos participantes relata menor pressão percebida com IA do que em situações com humanos |

---

## Hipótese Terciária (H-03)

### Observação
Ferramentas existentes de prática oral (ELSA Speak, Speak, Talkpal) não atendem ao público que precisa de simulações de situações práticas contextualizadas com feedback integrado de conversação e pronúncia.

### Descrição da Hipótese
Uma solução que combine simulação de conversa em cenário prático, resposta oral da IA e feedback integrado após a conversa será percebida pelo público-alvo como mais relevante para suas necessidades do que as alternativas que utilizam atualmente.

> **Condição de refutação:** H-03 é refutada se a maioria dos participantes já utilizar e se sentir satisfeita com as alternativas disponíveis, ou se a solução proposta não se diferenciar de forma perceptível das alternativas existentes.

### Critérios de Avaliação (GUT)

| Observação | G | U | T | Somatório | Grau de Risco |
|-----------|---|---|---|-----------|---------------|
| Lacuna de ferramentas que combinam conversação contextualizada + feedback integrado | 4 | 4 | 4 | 12 | **Alto** |

---

## Resumo das Hipóteses

| Hipótese | Observação | G | U | T | Somatório | Risco | Prioridade |
|----------|-----------|---|---|---|-----------|-------|------------|
| H-01 | Falta de prática oral acessível e de baixa pressão | 5 | 4 | 5 | 14 | Alto | Alta |
| H-02 | Evitação de prática por percepção de alta pressão | 4 | 3 | 4 | 11 | Alto | Média |
| H-03 | Lacuna de ferramentas com conversação + feedback integrado | 4 | 4 | 4 | 12 | Alto | Média |

**A hipótese H-01 é a hipótese principal do projeto.** As hipóteses H-02 e H-03 são secundárias — informam o design da solução, mas não definem o critério de sucesso do protótipo.

---

## Alvos Numéricos Provisórios

> Os valores abaixo são **provisórios** e requerem confirmação antes do início dos testes. Estão sinalizados como `[ALVO PROVISÓRIO — requires validation]`.

| Indicador | Alvo provisório | Justificativa |
|-----------|----------------|---------------|
| SUS (System Usability Scale) | ≥ 68 | Ponto de corte padrão da literatura de usabilidade |
| Taxa de conclusão de tarefa sem assistência | ≥ 60% | `[ALVO PROVISÓRIO]` — sem base empírica específica para este tipo de protótipo |
| Redução de ansiedade autorrelatada (pré vs. pós) | Maioria (>50%) relata redução | `[ALVO PROVISÓRIO]` — baseado em estudos de ÖLMEZER-ÖZTÜRK; ÖZTÜRK (2021), mas não diretamente transferível |
| Número de participantes no teste | 5–8 | `[ALVO PROVISÓRIO]` — padrão para testes de usabilidade exploratórios (Nielsen, 1994); a ser confirmado |
