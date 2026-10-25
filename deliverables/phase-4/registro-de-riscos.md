# Registro de Riscos — Fase 4: Justificativa, Hipóteses e Riscos

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Hypothesis & Risk Analyst
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## Metodologia

Esta matriz utiliza a escala GUT (Gravidade × Urgência × Tendência) de 1 a 5 por critério, com somatório de 3 a 15 pontos, conforme convenção adotada no documento de referência da disciplina.

| Pontuação | Gravidade (G) | Urgência (U) | Tendência (T) |
|-----------|---------------|--------------|---------------|
| 5 | Inviabiliza o projeto ou causa dano acadêmico severo | Ação necessária em dias | Piora rapidamente se ignorado |
| 4 | Impacto significativo — requer mitigação | Ação em semanas | Piora progressivamente |
| 3 | Impacto moderado — controlável | Pode aguardar algumas semanas | Persiste se ignorado |
| 2 | Impacto baixo — facilmente contornável | Pode aguardar meses | Tende a se resolver sozinho |
| 1 | Impacto negligenciável | Sem urgência | Sem tendência de piora |

**Classificação:** Baixo: 3–6 | Médio: 7–10 | Alto: 11–15

---

## Matriz de Riscos

### R-01 — Reconhecimento de fala enviesado contra sotaque brasileiro

| Campo | Detalhe |
|-------|---------|
| **Descrição** | Sistemas de ASR (Automatic Speech Recognition) são treinados predominantemente em dados de falantes nativos; apresentam taxa de erro elevada para falantes não nativos (WER de 32,8% documentado para L2 em outro idioma) e viés contra variedades não nativas do inglês |
| **Fontes** | `[FONTE-SECUNDÁRIA]` VERHELST; BELPAEME, 2025; JEON; LEE; CORONEL-MOLINA, 2024 |
| **G** | 5 — Se o sistema não entende o usuário, a experiência central do produto falha completamente |
| **U** | 4 — Deve ser avaliado no início do desenvolvimento do protótipo |
| **T** | 3 — A qualidade dos modelos de ASR está melhorando, mas o viés para sotaques específicos persiste |
| **Somatório** | **12 — Alto** |
| **Mitigação** | Testar o protótipo especificamente com usuários falantes de português brasileiro antes de definir a tecnologia de ASR; avaliar múltiplos modelos (ex.: Whisper, Google STT, Azure STT) para sotaque brasileiro; documentar a limitação no protótipo |
| **Responsável** | Equipe técnica (Fase de prototipagem) |
| **Risco residual** | Médio — melhorias em ASR reduzem o risco, mas não o eliminam; pode ser necessário aceitar limitação de ASR como restrição do protótipo v1 |

---

### R-02 — Heterogeneidade dos resultados de eficácia de chatbots

| Campo | Detalhe |
|-------|---------|
| **Descrição** | A literatura mostra que os resultados de eficácia de chatbots para fala não são uniformes: enquanto Wang et al. (2024) reportam efeito positivo médio (g = 0,484), Chen et al. (2024) não encontraram diferença significativa em estudo controlado |
| **Fontes** | `[FONTE-SECUNDÁRIA]` WANG et al., 2024; CHEN et al., 2024; KOÇ; SAVAŞ, 2024 |
| **G** | 4 — Pode comprometer a validade da proposta se a hipótese não for confirmada no teste |
| **U** | 3 — Relevante para o design do teste, não para a fase atual |
| **T** | 3 — A heterogeneidade de resultados é esperada em tecnologias emergentes |
| **Somatório** | **10 — Médio** |
| **Mitigação** | Formular a hipótese principal como testável e refutável (H-01 já está assim formulada); não afirmar eficácia antes do teste; o teste de validação do protótipo é a mitigação principal |
| **Responsável** | Agente Hypothesis & Risk Analyst (Fase 4); Academic Reviewer (Fase 7) |
| **Risco residual** | Médio — o risco é inerente à natureza do protótipo; não é eliminável sem teste empírico |

---

### R-03 — Ansiedade aumentada pelo contexto avaliativo da IA

| Campo | Detalhe |
|-------|---------|
| **Descrição** | Alguns estudos documentaram aumento de ansiedade em aprendizes após interação com chatbots em contexto educacional avaliativo; a falta de empatia e raciocínio complexo dos sistemas pode criar experiência frustrante ou intimidadora |
| **Fontes** | `[FONTE-SECUNDÁRIA]` KOÇ; SAVAŞ, 2024 |
| **G** | 4 — Contraproducente: se a ferramenta aumenta ansiedade, a hipótese H-02 é refutada e a proposta precisa ser redesenhada |
| **U** | 3 — Relevante para o design da interação e para o teste de validação |
| **T** | 3 — Persiste enquanto o design não abordar explicitamente a percepção de pressão |
| **Somatório** | **10 — Médio** |
| **Mitigação** | Design explicitamente não avaliativo: feedback encorajador antes do corretivo; introdução da ferramenta como ambiente de prática, não de avaliação; medir ansiedade pré e pós no teste para detectar o risco |
| **Responsável** | Solution Specifier (Fase 6) |
| **Risco residual** | Médio — dependente de decisões de design de UX e de fluxo de feedback |

---

### R-04 — Privacidade e retenção de áudios

| Campo | Detalhe |
|-------|---------|
| **Descrição** | O simulador captura áudio do usuário para processamento via ASR. A retenção, armazenamento e eventual treinamento de modelos com esses dados levanta questões de privacidade e conformidade com a LGPD (Lei Geral de Proteção de Dados) |
| **Fontes** | `[INFERÊNCIA]` — risco derivado da natureza técnica do produto; regulamentação LGPD é fato público |
| **G** | 4 — Violação de privacidade pode inviabilizar o produto ou gerar responsabilidade legal |
| **U** | 3 — Relevante para o protótipo, mas crítico para uma versão produção |
| **T** | 4 — A consciência sobre privacidade de dados aumenta progressivamente; risco cresce se ignorado |
| **Somatório** | **11 — Alto** |
| **Mitigação** | No protótipo: não reter áudios além da sessão; exigir consentimento explícito do usuário antes de iniciar; documentar no termo de consentimento do teste de usabilidade o que é capturado e por quanto tempo |
| **Responsável** | Solution Specifier (Fase 6); equipe técnica |
| **Risco residual** | Baixo para o protótipo de teste (se implementado corretamente), Médio a Alto para produto em escala |

---

### R-05 — Latência e qualidade da resposta da IA

| Campo | Detalhe |
|-------|---------|
| **Descrição** | Simulações de conversação por voz dependem de pipeline com ASR → LLM → TTS (text-to-speech); latências altas (>3–5 segundos) rompem o fluxo conversacional e degradam a experiência de uso |
| **Fontes** | `[INFERÊNCIA]` — característica técnica de pipelines de IA de voz; sem fonte acadêmica específica disponível |
| **G** | 4 — Latência alta pode tornar a conversa inviável e inviabilizar o teste da hipótese principal |
| **U** | 4 — Precisa ser avaliada na fase de desenvolvimento do protótipo |
| **T** | 3 — Latência de LLMs está diminuindo com o tempo, mas permanece relevante para casos de uso de voz em tempo real |
| **Somatório** | **11 — Alto** |
| **Mitigação** | Avaliar múltiplas opções de LLM e TTS com benchmarks de latência antes de fixar a tecnologia; considerar pré-processamento de respostas comuns para cenários fixos; documentar limitação de latência como restrição do protótipo v1 |
| **Responsável** | Solution Specifier (Fase 6); equipe técnica |
| **Risco residual** | Médio — reduzível com escolha adequada de tecnologia e arquitetura |

---

### R-06 — Custos de API de IA (viabilidade econômica do protótipo)

| Campo | Detalhe |
|-------|---------|
| **Descrição** | O uso de APIs de LLM (ex.: OpenAI GPT-4, Google Gemini, Anthropic Claude) e ASR pode gerar custos recorrentes por sessão; para um produto de baixo custo ou gratuito, o modelo de negócio deve ser validado |
| **Fontes** | `[INFERÊNCIA]` — estrutura de precificação de APIs é pública; custo elevado documentado como barreira em produtos similares (WIFITALENTS, 2026) `[FONTE-SECUNDÁRIA]` |
| **G** | 3 — Para o protótipo de teste, o custo é controlável; torna-se crítico na escala |
| **U** | 3 — Não urgente para o escopo atual de proposta acadêmica |
| **T** | 3 — Custos de LLM estão caindo, mas permanecem relevantes para casos de uso intensivo |
| **Somatório** | **9 — Médio** |
| **Mitigação** | Para o protótipo: limitar o número de sessões e a duração de cada sessão; usar modelos de custo-benefício favorável (ex.: GPT-4o mini, Gemini Flash) para o teste inicial; documentar custos estimados por sessão |
| **Responsável** | Solution Specifier (Fase 6) |
| **Risco residual** | Baixo para o protótipo; Médio para produto em escala |

---

### R-07 — Acessibilidade e acesso a dispositivos

| Campo | Detalhe |
|-------|---------|
| **Descrição** | O simulador requer microfone e conexão de internet de qualidade suficiente; usuários com dispositivos de baixa qualidade ou conexão instável podem ter experiência degradada |
| **Fontes** | `[INFERÊNCIA]` — requisito técnico de produtos de voz; sem dado específico sobre infraestrutura do público-alvo deste projeto |
| **G** | 3 — Afeta acessibilidade, especialmente para o perfil Bruno Lima |
| **U** | 2 — Pode ser endereçado na fase de especificação do protótipo |
| **T** | 3 — Acesso a smartphones com microfone é crescente no Brasil, mas conexão de qualidade ainda é irregular |
| **Somatório** | **8 — Médio** |
| **Mitigação** | Especificar requisitos mínimos de hardware e conectividade claramente; considerar modo de texto como fallback para conexões instáveis |
| **Responsável** | Solution Specifier (Fase 6) |
| **Risco residual** | Médio |

---

### R-08 — Coerência e qualidade pedagógica do feedback da IA

| Campo | Detalhe |
|-------|---------|
| **Descrição** | LLMs podem gerar feedback inconsistente, superficial ou pedagogicamente inadequado; feedback corretivo explícito é documentado como lacuna em chatbots atuais |
| **Fontes** | `[FONTE-SECUNDÁRIA]` KOÇ; SAVAŞ, 2024; KHAN; HUSSAIN, 2026 |
| **G** | 4 — Feedback de baixa qualidade reduz o valor pedagógico da ferramenta e pode reforçar erros |
| **U** | 3 — Relevante para o design do protótipo |
| **T** | 4 — Sem design explícito do feedback, o risco tende a materializar-se |
| **Somatório** | **11 — Alto** |
| **Mitigação** | Definir explicitamente o prompt de sistema da IA para guiar o tipo e o tom do feedback; testar amostras de feedback em múltiplos cenários antes do teste com usuários; incluir revisão pedagógica do feedback no plano de validação |
| **Responsável** | Solution Specifier (Fase 6) |
| **Risco residual** | Médio — dependente da qualidade do design do prompt |

---

## Resumo Consolidado dos Riscos

| Risco | Descrição resumida | G | U | T | Somatório | Classificação |
|-------|-------------------|---|---|---|-----------|---------------|
| R-01 | ASR enviesado para sotaque brasileiro | 5 | 4 | 3 | 12 | **Alto** |
| R-02 | Heterogeneidade de resultados de eficácia | 4 | 3 | 3 | 10 | **Médio** |
| R-03 | Ansiedade aumentada por contexto avaliativo | 4 | 3 | 3 | 10 | **Médio** |
| R-04 | Privacidade e retenção de áudios | 4 | 3 | 4 | 11 | **Alto** |
| R-05 | Latência e qualidade da resposta de IA | 4 | 4 | 3 | 11 | **Alto** |
| R-06 | Custos de API de IA | 3 | 3 | 3 | 9 | **Médio** |
| R-07 | Acessibilidade e acesso a dispositivos | 3 | 2 | 3 | 8 | **Médio** |
| R-08 | Qualidade pedagógica do feedback de IA | 4 | 3 | 4 | 11 | **Alto** |

**Riscos de classificação Alta (≥11):** R-01, R-04, R-05, R-08 — devem ser tratados como restrições de design na Fase 6.
