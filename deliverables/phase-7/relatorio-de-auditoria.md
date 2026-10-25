# Relatório de Auditoria Acadêmica — Fase 7: Revisão Independente

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Academic Reviewer (postura crítica e independente)
**Data:** 25 de outubro de 2026
**Versão:** 1.0

> **Nota metodológica:** Esta revisão foi conduzida com postura crítica e independente, conforme exigido pela Fase 7. O revisor não presume que as conclusões das fases anteriores estejam corretas. Todos os achados negativos são registrados antes de qualquer proposição de correção.

---

## Parte A — Auditoria por Critério da Disciplina

Os 11 critérios listados em `phases/07_revisao_final.md` são auditados a seguir.

---

### 1.1.1 — Clareza e Estrutura

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | Todos os entregáveis das Fases 1–6 |
| **Achados positivos** | A documentação está organizada em fases com entregáveis claramente identificados; cada arquivo tem cabeçalho de metadados (projeto, agente, data, versão); há rastreabilidade explícita entre fases via phase-handoffs. |
| **Achados negativos / riscos** | Os entregáveis estão distribuídos em múltiplos arquivos por fase — a proposta final precisará ser consolidada em um único documento para submissão. O critério de clareza da proposta final não pode ser avaliado completamente até que a consolidação ocorra. |
| **Severidade de pendências** | Baixa — é questão de consolidação, não de conteúdo. |
| **Correção recomendada** | Consolidar todos os entregáveis relevantes em `deliverables/final-proposal/proposta-desafio-e-solucao.md` na Fase 8. |

---

### 1.1.2 — Análise do Contexto

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-2/context-report.md` |
| **Achados positivos** | 18 fontes secundárias verificáveis; barreiras à produção oral em inglês documentadas em múltiplas revisões sistemáticas; dados quantitativos do EF EPI 2025; contexto brasileiro com dados acadêmicos (CORRÊA, 2017; BATISTA, 2020); soluções existentes analisadas; limitações e lacunas explicitadas; artigo retratado descartado e documentado. |
| **Achados negativos / riscos** | (1) Nenhuma pesquisa primária foi conduzida — toda a análise de contexto é baseada em literatura secundária e dados de mercado; (2) A pesquisa Pearson (2024) foi citada apenas por reportagens jornalísticas — o relatório primário não foi acessado (lacuna B-02); (3) Toda evidência de eficácia de chatbots vem de contextos não brasileiros (lacuna B-04). |
| **Severidade de pendências** | Média — as lacunas estão declaradas e bem sinalizadas; não constituem invenção de dados, mas limitam a solidez das afirmações sobre o público brasileiro. |
| **Correção recomendada** | Manter as lacunas declaradas na proposta final com linguagem transparente: "a literatura indica… para populações de EFL; a aplicabilidade ao contexto brasileiro é inferência, não achado direto". |

---

### 1.1.3 — Desafio (Problema)

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-2/context-report.md` Seção 8; `deliverables/phase-4/justificativa.md` |
| **Achados positivos** | O problema está claramente articulado: "Como permitir que pessoas que precisam usar inglês em situações práticas pratiquem a produção oral com frequência e apoio suficientes para reduzir ansiedade e aumentar WTC?" A barreira psicológica está bem documentada. A separação entre problema e solução é mantida. |
| **Achados negativos / riscos** | (1) O problema é formulado de forma genérica ("pessoas que precisam usar inglês em situações práticas") sem confirmação de qual situação específica é prioritária — B-01 persiste; (2) A formulação do desafio na Fase 2 é explicitamente "preliminar" — a Fase 4 não produziu uma versão final formal do desafio (o brief da Fase 4 foca em justificativa e hipóteses, não em reformular o desafio). |
| **Severidade de pendências** | Média — o desafio está claro em essência, mas pode precisar de formulação mais específica para a proposta final. |
| **Correção recomendada** | Na Fase 8 (consolidação), usar a formulação preliminar da Fase 2 como base e refiná-la para que seja mais específica ao cenário do MVP (entrevista de emprego). |

---

### 1.1.4 — Área do Conhecimento do Curso

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS *(resolvido — UA-01)* |
| **Localização** | Todos os entregáveis atualizados com o campo **Curso** |
| **Achados** | Curso informado pelo autor: **Pós-Graduação em Arquitetura de Software e Soluções com IA**. Área do conhecimento: Tecnologia da Informação — Arquitetura de Software. A solução proposta (simulador de conversação com IA) é diretamente alinhada à área do curso: envolve design de sistema com componentes de IA (LLM, ASR, TTS), especificação de arquitetura de solução e validação de protótipo. |
| **Severidade** | Nenhuma — critério resolvido. |
| **Correção recomendada** | Nenhuma. Na proposta final, incluir a área do curso no cabeçalho e mencionar explicitamente o alinhamento entre a solução proposta (arquitetura de IA conversacional) e a área do conhecimento da pós-graduação. |

---

### 1.1.5 — Persona + Mapa de Empatia

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-3/personas.md`; `deliverables/phase-3/empathy-maps.md` |
| **Achados positivos** | Duas personas documentadas (Ana Souza e Bruno Lima); mapa de empatia completo com 6 dimensões para a persona principal; cada elemento classificado como evidência, inferência ou suposição; nenhuma citação direta de usuário fabricada; personas rotuladas como provisórias. |
| **Achados negativos / riscos** | (1) As personas são completamente baseadas em inferências de literatura secundária — sem pesquisa primária; (2) O PDF de referência da disciplina (`Exemplo - Desafio - Solução.pdf`) apresenta personas como figuras visuais (imagens de perfil comportamental e mapa de empatia visual) — os entregáveis desta fase são em formato markdown tabular, não visual; (3) Nenhuma "citação direta" de persona (fala em primeira pessoa) foi incluída — o PDF de referência não inclui citações diretas nas personas analisadas, então isso não é necessariamente uma lacuna. |
| **Severidade de pendências** | Baixa a Média — o conteúdo é sólido; o formato visual pode ser necessário dependendo dos requisitos da disciplina (suposição A-09). |
| **Correção recomendada** | Na Fase 8, se a disciplina exigir formato visual, converter as personas e mapas de empatia para diagramas ou figuras. O conteúdo está completo para essa conversão. |

---

### 1.1.6 — Justificativa

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-4/justificativa.md` |
| **Achados positivos** | Justificativa deriva do problema e das dores das personas, não de promessas tecnológicas genéricas; separação explícita entre "benefícios esperados" e "resultados demonstrados"; dados quantitativos com fonte; por que vale a pena testar uma solução digital fundamentado em 4 razões rastreáveis à literatura. |
| **Achados negativos / riscos** | O PDF de referência da disciplina inclui percentuais de melhoria (ex.: "redução de 60% no tempo de análise") sem fontes verificáveis. Os entregáveis deste projeto **não incluem percentuais sem fonte** — isso é academicamente correto, mas pode parecer menos "concreto" do que o exemplo. Este é um caso em que a integridade acadêmica exige diferença do exemplo. |
| **Severidade** | Baixa — a justificativa está mais rigorosa que o exemplo, o que é uma qualidade, não uma falha. |
| **Correção recomendada** | Nenhuma — manter o padrão de rigor. Pode-se incluir nota explicando que percentuais de melhoria sem validação empírica não foram incluídos intencionalmente. |

---

### 1.1.7 — Hipótese

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-4/hipoteses.md` |
| **Achados positivos** | Três hipóteses (H-01 principal, H-02 e H-03 secundárias); todas com condição de refutação explícita; scoring GUT com escala explicada; método de teste, indicadores e regra de interpretação definidos; separação clara entre métricas de usabilidade e aprendizagem de idioma. |
| **Achados negativos / riscos** | (1) **Convenção GUT:** o projeto usa G+U+T (somatório); o PDF de referência apresenta colunas G, U, T com somatório também — a convenção parece compatível, mas a fórmula não é explicitada no PDF. `[ASSUMPTION D-01]`; (2) **Alvos numéricos provisórios** (SUS ≥ 68, taxa de conclusão ≥ 60%) não têm base específica no contexto deste protótipo — estão sinalizados como provisórios, o que é correto. |
| **Severidade** | Baixa — as hipóteses estão bem formuladas. D-01 é uma pendência menor. |
| **Correção recomendada** | Confirmar com o orientador a convenção GUT correta (D-01). |

---

### 1.1.8 — Matriz de Observação

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-3/observation-matrix.md` |
| **Achados positivos** | 14 linhas cobrindo 6 temas; cada linha com questão de pesquisa, comportamento/tema, método de coleta, fonte, resultado, status e próxima ação; 3 lacunas explicitamente declaradas como em aberto; nenhum resultado fabricado. |
| **Achados negativos / riscos** | (1) A matriz é construída inteiramente de fontes secundárias — sem observação primária. Isso é declarado transparentemente, mas pode ser visto como limitação dependendo dos requisitos da disciplina; (2) O PDF de referência da disciplina não mostra uma "matriz de observação" explícita — o critério parece ser específico desta disciplina; o formato adotado é compatível com o especificado em `phases/03_persona_empatia_observacao.md`. |
| **Severidade** | Baixa — a matriz está bem construída dentro das limitações disponíveis. |
| **Correção recomendada** | Nenhuma estrutural; verificar com o orientador se o formato tabular em markdown atende o requisito de apresentação. |

---

### 1.1.9 — Identificação do Grau de Risco

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-4/registro-de-riscos.md` |
| **Achados positivos** | 8 riscos identificados; escala GUT 1–5 explicada antes das pontuações; fórmula de somatório e faixas de classificação declaradas; mitigação, responsável e risco residual para cada risco; riscos derivados da literatura (R-01, R-02, R-03, R-08) com fontes secundárias; riscos técnicos e de negócio cobertos. |
| **Achados negativos / riscos** | Mesma pendência D-01 (convenção GUT a confirmar). |
| **Severidade** | Baixa. |
| **Correção recomendada** | Confirmar convenção GUT com o orientador (D-01). |

---

### 1.1.10 — Priorização de Ideias

| Campo | Avaliação |
|-------|-----------|
| **Status** | ✅ PASS |
| **Localização** | `deliverables/phase-5/priorizacao-ideias.md`; `deliverables/phase-5/escopo-mvp.md` |
| **Achados positivos** | 5 alternativas de solução avaliadas; 12 funcionalidades candidatas geradas; rubrica de priorização com 3 critérios ponderados explicitamente documentada; escala 1–5 explicada; MVP claramente declarado (F01+F03+F04+F05); funcionalidades descartadas com justificativa; rastreabilidade MVP ↔ hipóteses ↔ personas. |
| **Achados negativos / riscos** | (1) Os valores da matriz de priorização são julgamentos analíticos, não medições objetivas — sinalizados como tal; (2) Não há comparação com um benchmarking externo de soluções concorrentes (além do levantamento da Fase 2) — o PDF de referência não fez essa comparação também, então não parece ser requisito. |
| **Severidade** | Baixa. |
| **Correção recomendada** | Nenhuma estrutural. |

---

### 1.1.11 — Apresentação e Estilo

| Campo | Avaliação |
|-------|-----------|
| **Status** | ⚠️ PARTIAL |
| **Localização** | Todos os entregáveis |
| **Achados positivos** | Português formal acadêmico mantido; registro consistente; sem coloquialismos; uso de terceira pessoa e construções impessoais; ABNT NBR 6023 nas referências da Fase 2. |
| **Achados negativos / riscos** | (1) O PDF de referência tem formato de documento acadêmico formatado com numeração de seções (1.1, 1.1.1, 1.2, etc.) e figuras. Os entregáveis atuais estão em markdown sem formatação visual equivalente; (2) As personas no exemplo são apresentadas como figuras visuais (imagens de perfil comportamental e mapa de empatia) — os documentos atuais estão em tabelas markdown; (3) A proposta final precisará de formatação adequada para submissão (PDF ou documento Word formatado). |
| **Severidade** | Média — o conteúdo está correto; o formato final depende da decisão do autor sobre apresentação. |
| **Correção recomendada** | Na Fase 8, formatar o documento final com numeração de seções compatível com o exemplo; converter personas para formato visual se exigido pela disciplina. |

---

## Parte B — Auditoria de Rastreabilidade e Coerência

### B1 — Rastreabilidade Problema → Persona → Justificativa → Hipótese → MVP → Validação

| Elo de rastreabilidade | Status | Nota |
|-----------------------|--------|------|
| Problema (Fase 2) → Personas (Fase 3) | ✅ PASS | Personas derivam das evidências do context-report |
| Personas (Fase 3) → Justificativa (Fase 4) | ✅ PASS | Justificativa cita explicitamente as dores das personas |
| Justificativa (Fase 4) → Hipótese H-01 (Fase 4) | ✅ PASS | H-01 deriva do problema e das necessidades das personas |
| Hipóteses (Fase 4) → MVP (Fase 5) | ✅ PASS | Critério central de priorização é "testar H-01" |
| MVP (Fase 5) → Solução (Fase 6) | ✅ PASS | Funcionalidades F01+F03+F04+F05 descritas conceitualmente |
| Solução (Fase 6) → Plano de Validação (Fase 6) | ✅ PASS | Plano testa H-01 com SUS + escala de ansiedade |
| Riscos (Fase 4) → Restrições de Design (Fase 6) | ✅ PASS | R-01, R-04, R-05, R-08 se tornaram R-C-01 a R-C-04 |

**Conclusão de rastreabilidade:** a cadeia problema → persona → justificativa → hipótese → MVP → validação está **coerente e rastreável** ao longo de todas as fases.

---

### B2 — Separação Benefício Esperado vs. Resultado Demonstrado

| Aspecto | Status | Nota |
|---------|--------|------|
| Justificativa (Fase 4) | ✅ PASS | Seção 3 explicitamente separa "benefícios esperados" de "o que o projeto não demonstrou" |
| Hipóteses (Fase 4) | ✅ PASS | Metas numéricas marcadas como `[ALVO PROVISÓRIO]` |
| Solução (Fase 6) | ✅ PASS | Tabela "O que o protótipo É vs. NÃO É" explícita |
| Plano de Validação (Fase 6) | ✅ PASS | Métricas de aprendizagem de idioma explicitamente excluídas do teste |

---

### B3 — Integridade Acadêmica

| Aspecto | Status | Nota |
|---------|--------|------|
| Citações fabricadas | ✅ PASS — Nenhuma | Todas as fontes são reais e rastreáveis |
| Entrevistas ou falas de usuários fabricadas | ✅ PASS — Nenhuma | Personas sem citações diretas; falas hipotéticas identificadas explicitamente |
| Estatísticas sem fonte | ✅ PASS — Nenhuma | Todos os percentuais têm fonte identificada ou são `[ALVO PROVISÓRIO]` |
| Resultados de teste inventados | ✅ PASS — Nenhum | O teste ainda não foi realizado; hipóteses são prospectivas |
| Artigo retratado usado | ✅ PASS — Descartado | XIAO; ZHANG; HE (retratado) registrado e descartado na Fase 2 |

---

## Parte C — Problemas Identificados e Classificação

| # | Problema | Severidade | Fase | Pode ser resolvido pelo agente? |
|---|----------|-----------|------|--------------------------------|
| P-01 | Área do conhecimento do curso (A-08) indefinida | ~~**Crítico**~~ **Resolvido** | Transversal | ✅ Resolvido — Pós-Graduação em Arquitetura de Software e Soluções com IA (UA-01) |
| P-02 | HMW statements ausentes na Fase 4 | **Alto** | Fase 4 | ✅ Sim — pode ser adicionado |
| P-03 | Convenção GUT não confirmada (D-01) | **Médio** | Fase 4 | ⚠️ Parcialmente — pode-se apresentar ambas as convenções |
| P-04 | Formato visual das personas (A-09) indefinido | **Médio** | Fase 3 | ⚠️ Parcialmente — formato markdown é funcional; visual depende de decisão do autor |
| P-05 | Prazo do objetivo SMART não confirmado (D-04) | **Médio** | Fase 6 | ❌ Não — requer informação do orientador |
| P-06 | Método de recrutamento de participantes indefinido (D-05) | **Médio** | Fase 6 | ❌ Não — requer decisão do autor |
| P-07 | Evidência de eficácia de chatbots não vem de contexto brasileiro (B-04) | **Médio** (limitação declarada) | Fase 2 | ✅ Já declarado — manter com linguagem transparente |
| P-08 | Formato da proposta final (markdown vs. PDF formatado) | **Baixo** | Fase 8 | ⚠️ Decisão do autor na consolidação |

---

## Parte D — Correções Aplicadas pelo Revisor

Com base nos achados acima, as seguintes correções foram aplicadas diretamente:

### D-C-01 — HMW Statements adicionados (Problema P-02)

As seguintes declarações "Como Podemos…" são derivadas da justificativa e das hipóteses da Fase 4 e serão incluídas no documento final:

> **HMW-01:** "Como podemos oferecer a profissionais de tecnologia com inglês intermediário uma experiência de prática de conversação oral de baixa pressão, disponível sob demanda, que simule situações reais de entrevista de emprego e forneça feedback imediato?"

> **HMW-02:** "Como podemos reduzir a ansiedade de fala de pessoas que sabem inglês mas travam ao falar, usando IA como interlocutor não avaliativo, sem substituir a interação humana de alta qualidade?"

> **HMW-03:** "Como podemos tornar o ciclo prática-feedback-melhoria acessível e recorrente para pessoas cujo percurso escolar não ofereceu prática oral adequada?"

Essas três HMW statements derivam diretamente das hipóteses H-01, H-02 e H-03 e das dores das personas Ana Souza e Bruno Lima — não são invenção, são reformulações interrogativas de conteúdo já documentado.

### D-C-02 — Convenção GUT apresentada em dupla perspectiva (Problema P-03)

O `registro-de-riscos.md` e `hipoteses.md` já explicam a convenção GUT adotada (G+U+T, somatório). Na proposta final, deve-se incluir nota de rodapé: "Caso a disciplina adote a fórmula multiplicativa G×U×T, os valores de somatório devem ser recalculados; os valores individuais de G, U e T permanecem os mesmos."

---

## Resumo do Estado da Auditoria

| Critério | Status |
|----------|--------|
| 1.1.1 Clareza e Estrutura | ✅ PASS (pendente consolidação Fase 8) |
| 1.1.2 Análise do Contexto | ✅ PASS (lacunas declaradas) |
| 1.1.3 Desafio (Problema) | ✅ PASS (refinamento sugerido na consolidação) |
| 1.1.4 Área do Conhecimento do Curso | ✅ PASS — Pós-Graduação em Arquitetura de Software e Soluções com IA |
| 1.1.5 Persona + Mapa de Empatia | ✅ PASS (formato visual: decisão do autor) |
| 1.1.6 Justificativa | ✅ PASS |
| 1.1.7 Hipótese | ✅ PASS (D-01 a confirmar) |
| 1.1.8 Matriz de Observação | ✅ PASS |
| 1.1.9 Grau de Risco | ✅ PASS (D-01 a confirmar) |
| 1.1.10 Priorização de Ideias | ✅ PASS |
| 1.1.11 Apresentação e Estilo | ⚠️ PARTIAL (depende de formatação da Fase 8) |

**Problemas críticos:** ~~1~~ **0** (P-01 resolvido — UA-01)
**Problemas altos:** 1 (P-02 — HMW statements — corrigido em D-C-01)
**Problemas médios:** 3 (P-03 a P-05 — D-01 a confirmar; D-04 prazo a confirmar; UA-04 imagens geradas ✅)
**Problemas baixos:** 1 (P-08 — formatação final)

**Estado geral da documentação:** **PRONTO PARA REVISÃO HUMANA** com as ressalvas acima. A proposta final (Fase 8) pode ser produzida após a aprovação humana desta fase, desde que P-01 (área do curso) seja informada pelo autor.
