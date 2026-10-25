# Priorização de Ideias — Fase 5: Priorização e MVP

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Idea Prioritizer
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Premissa de Entrada

A Fase 4 estabeleceu a hipótese principal (H-01): um protótipo de simulador de conversação por voz com IA para entrevistas de emprego será considerado útil, utilizável e reduzirá a ansiedade autorrelatada do público-alvo (persona Ana Souza) em uma sessão de teste. O critério central de priorização desta fase é: **quais funcionalidades são necessárias e suficientes para testar H-01?**

---

## 2. Alternativas de Solução Consideradas

Antes de priorizar funcionalidades dentro da solução escolhida, avaliaram-se alternativas de abordagem que também poderiam endereçar o problema identificado.

| # | Alternativa | Descrição | Critérios positivos | Critérios negativos |
|---|------------|-----------|--------------------|--------------------|
| A1 | **Simulador de conversação por voz com IA** *(solução candidata principal)* | Protótipo digital de voz com IA generativa, baseado em cenários práticos, com feedback integrado | Alta escalabilidade; sem restrição de horário; compatível com H-01; evidência de plausibilidade na literatura (WANG et al., 2024) | Riscos técnicos altos (ASR, latência, feedback); depende de API de IA |
| A2 | **Aplicativo de conversação por texto com IA** | Chat por texto com IA em cenários práticos, sem componente de voz | Menor risco técnico (sem ASR); menor custo; menor latência | Não pratica a **produção oral** — não testa H-01; desalinhado com a dor central das personas |
| A3 | **Plataforma de tutoria humana sob demanda** | Conecta usuário com tutores humanos para conversação | Alta qualidade de feedback humano | Custo elevado (lacuna identificada em Cambly, WIFITALENTS, 2026); escalabilidade limitada; inviável como protótipo acadêmico |
| A4 | **Grupos de conversação online mediados por IA** | Sessões em grupo com facilitação de IA | Interação humana combinada com IA | Complexidade técnica e logística elevada para um protótipo; fora do escopo acadêmico |
| A5 | **Material de autoestudo com roteiros de prática oral** (sem IA) | Cartões, scripts e exercícios gravados | Baixo custo e risco | Sem feedback adaptativo; sem interatividade; não aborda a barreira da ansiedade de forma dinâmica |

**Decisão:** A alternativa A1 (simulador de conversação por voz com IA) é selecionada por ser a única que endereça diretamente a hipótese principal (prática oral + feedback imediato + baixa pressão) e por ter base de plausibilidade na literatura. As alternativas A2–A5 foram descartadas pelas razões listadas.

---

## 3. Funcionalidades Candidatas

As funcionalidades abaixo foram geradas a partir das necessidades das personas (Fase 3) e dos requisitos implícitos da hipótese H-01 (Fase 4).

| ID | Funcionalidade | Descrição |
|----|---------------|-----------|
| F01 | Seleção de cenário prático | Usuário escolhe o cenário antes de iniciar (ex.: entrevista de emprego, reunião, interação cotidiana) |
| F02 | Configuração de nível de inglês | Usuário indica seu nível (básico, intermediário, avançado) para adaptar a dificuldade da IA |
| F03 | Conversa por voz (captura de áudio) | Usuário fala; o sistema converte fala em texto (ASR) e envia para a IA |
| F04 | Resposta oral da IA (síntese de voz) | A IA responde por voz (TTS), simulando um interlocutor real |
| F05 | Feedback após a conversa | Ao final da sessão, a IA apresenta resumo com pontos positivos e áreas de melhoria |
| F06 | Transcrição da conversa | O sistema exibe o texto da conversa para revisão posterior |
| F07 | Histórico de sessões | Usuário acessa sessões anteriores e acompanha progresso ao longo do tempo |
| F08 | Feedback em tempo real (durante a conversa) | A IA corrige ou sugere melhorias enquanto a conversa ocorre |
| F09 | Avaliação de pronúncia | Análise fonética detalhada da pronúncia do usuário |
| F10 | Perfil de usuário e progresso | Cadastro, histórico de pontuações, metas e gamificação |
| F11 | Múltiplos idiomas ou sotaques da IA | IA pode responder em sotaque americano, britânico, australiano, etc. |
| F12 | Modo de texto (fallback sem voz) | Alternativa por texto para conexões lentas ou sem microfone |

---

## 4. Critérios de Priorização

Cada funcionalidade é avaliada em três critérios, cada um com escala de 1 a 5:

| Critério | Descrição | Peso |
|----------|-----------|------|
| **Impacto para testar H-01** | Sem essa funcionalidade, é possível testar se o protótipo é útil, utilizável e reduz ansiedade? | 3 (maior peso) |
| **Impacto para o usuário** | O quanto a funcionalidade resolve uma dor central das personas? | 2 |
| **Esforço / Risco técnico** | Quão difícil é implementar? Quais riscos altos (R-01, R-05, R-08) estão envolvidos? Nota invertida: 5 = baixo esforço/risco | 1 |

**Pontuação ponderada** = (Impacto H-01 × 3) + (Impacto usuário × 2) + (Esforço/Risco × 1)

> **Nota de transparência:** os valores atribuídos são julgamentos analíticos fundamentados nas necessidades das personas e nos riscos da Fase 4 — não são medições objetivas. Estão sinalizados como `[JULGAMENTO — requires validation]` onde a subjetividade é alta.

---

## 5. Matriz de Priorização

| ID | Funcionalidade | Impacto H-01 (×3) | Impacto Usuário (×2) | Esforço/Risco (×1) | Pontuação | Classificação |
|----|---------------|-------------------|----------------------|--------------------|-----------|---------------|
| F01 | Seleção de cenário prático | 5 | 5 | 4 | 29 | **Essencial** |
| F03 | Conversa por voz (ASR) | 5 | 5 | 2 | 27 | **Essencial** ⚠️ risco R-01 |
| F04 | Resposta oral da IA (TTS) | 5 | 5 | 3 | 28 | **Essencial** ⚠️ risco R-05 |
| F05 | Feedback após a conversa | 5 | 5 | 3 | 28 | **Essencial** ⚠️ risco R-08 |
| F02 | Configuração de nível de inglês | 3 | 4 | 5 | 22 | **Desejável** |
| F06 | Transcrição da conversa | 3 | 4 | 4 | 21 | **Desejável** |
| F12 | Modo de texto (fallback) | 2 | 3 | 4 | 16 | **Desejável** *(contingência para R-01)* |
| F08 | Feedback em tempo real | 2 | 4 | 2 | 15 | **Fora do escopo v1** ⚠️ alto risco/esforço |
| F09 | Avaliação de pronúncia | 2 | 3 | 1 | 14 | **Fora do escopo v1** ⚠️ risco R-01 elevado |
| F07 | Histórico de sessões | 1 | 3 | 3 | 12 | **Fora do escopo v1** |
| F10 | Perfil de usuário e progresso | 1 | 3 | 2 | 11 | **Fora do escopo v1** |
| F11 | Múltiplos sotaques da IA | 1 | 2 | 2 | 9 | **Fora do escopo v1** |

---

## 6. Justificativa das Classificações

### Essenciais (MVP)
- **F01 (Seleção de cenário):** sem cenário definido, a IA não tem contexto para simular uma situação prática — a hipótese H-01 não pode ser testada. Baixo risco técnico.
- **F03 (Conversa por voz / ASR):** é o componente central da proposta de valor. Sem captura de voz, o produto não pratica produção oral. Risco alto (R-01 — ASR para sotaque brasileiro), mas incontornável — deve ser testado.
- **F04 (Resposta oral da IA / TTS):** sem resposta em voz, a simulação não é conversacional — perde o componente de baixa pressão que distingue o produto de um chat de texto. Risco médio (R-05 — latência).
- **F05 (Feedback pós-conversa):** é a diferença entre uma "conversa qualquer com IA" e um "simulador de aprendizado". Sem feedback, a hipótese de redução de ansiedade e percepção de utilidade perde o componente de valor central. Risco alto (R-08 — qualidade do feedback), mas essencial para o teste.

### Desejáveis (a incluir se o esforço permitir)
- **F02 (Nível de inglês):** permite adaptar a dificuldade — importante para não frustrar o perfil Bruno Lima com diálogos muito avançados. Baixo risco técnico.
- **F06 (Transcrição):** facilita a revisão posterior; aumenta o valor percebido do feedback. Baixo risco técnico.
- **F12 (Fallback de texto):** mitiga o risco R-01 (ASR com falhas) — oferece uma saída quando o reconhecimento de voz falha. Aumenta a robustez do protótipo.

### Fora do escopo da versão 1
- **F08 (Feedback em tempo real):** interrompe o fluxo conversacional; alto esforço técnico; pode aumentar a ansiedade (risco R-03). Adiado.
- **F09 (Avaliação de pronúncia):** exige sistema especializado de análise fonética além do ASR padrão; risco R-01 agravado. Adiado.
- **F07, F10, F11:** funcionalidades de suporte e personalização — relevantes para produto em escala, mas não para testar H-01 com um protótipo.

---

## 7. Alternativas Descartadas — Registro

| Funcionalidade | Razão do descarte |
|---------------|------------------|
| Tutoria humana (A3) | Custo e viabilidade inviáveis para protótipo acadêmico |
| Grupos de conversação (A4) | Complexidade logística e técnica acima do escopo |
| Autoestudo sem IA (A5) | Não aborda o problema da produção oral interativa |
| Feedback em tempo real (F08) | Alto risco de ruptura do fluxo conversacional + esforço elevado |
| Avaliação fonética (F09) | Requer sistema especializado além do ASR padrão; alto risco R-01 |
