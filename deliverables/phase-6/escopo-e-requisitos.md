# Escopo e Requisitos — Fase 6: Solução SMART e Validação

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Solution Specifier
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Escopo

### 1.1 Dentro do Escopo (MVP)

- Simulação de conversação em inglês por voz no cenário de entrevista de emprego (área de tecnologia)
- Captura de voz do usuário via microfone (ASR)
- Resposta oral da IA em inglês (LLM + TTS)
- Feedback estruturado pós-conversa (pontos positivos, áreas de melhoria, próximo passo)
- Interface web simples para condução do teste de usabilidade
- Coleta de dados do teste: questionário SUS + escala de ansiedade pré/pós sessão + termo de consentimento

### 1.2 Fora do Escopo (versão 1)

- Avaliação fonética detalhada de pronúncia (F09)
- Feedback em tempo real durante a conversa (F08)
- Histórico de sessões e perfil do usuário (F07, F10)
- Múltiplos cenários além de entrevista de emprego
- Múltiplos sotaques ou vozes de IA (F11)
- Gamificação ou sistema de pontuação
- Integração com sistemas de gerenciamento de aprendizagem (LMS)
- Desenvolvimento de produto comercial em escala

---

## 2. Premissas

| # | Premissa | Risco se falsa |
|---|----------|----------------|
| P-01 | O público-alvo do teste tem acesso a dispositivo com microfone funcional e conexão de internet estável | Requisito mínimo — se falso, o teste não pode ser realizado com esse participante; mitigação: selecionar participantes que atendam ao requisito |
| P-02 | As APIs de ASR, LLM e TTS escolhidas são acessíveis e têm desempenho aceitável para o cenário do teste | Se falso, o protótipo pode não funcionar adequadamente — risco R-01 e R-05 |
| P-03 | A duração da sessão de teste (5–10 minutos de conversa + 5–10 minutos de questionários) é aceitável para os participantes | Se falsa, a taxa de completude do teste pode ser baixa |
| P-04 | Nenhuma entrevista real de emprego é simulada como consequência real — os participantes entendem que é uma simulação de teste | Fundamental para o consentimento informado e para a validade do teste |

---

## 3. Restrições

| # | Restrição | Origem |
|---|-----------|--------|
| R-C-01 | ASR deve ser avaliado para desempenho com sotaque brasileiro antes de ser fixado | Risco R-01 — JEON; LEE; CORONEL-MOLINA, 2024; VERHELST; BELPAEME, 2025 |
| R-C-02 | Áudios dos usuários não podem ser retidos além da sessão de teste sem consentimento explícito adicional | LGPD; Risco R-04 |
| R-C-03 | Latência alvo: resposta da IA em < 5 segundos `[ALVO PROVISÓRIO]` — se não atingível, documentar como limitação do protótipo | Risco R-05 |
| R-C-04 | O feedback da IA deve ser revisado por amostragem antes do teste com usuários — não pode ser enviado a participantes sem validação mínima do conteúdo | Risco R-08 — qualidade pedagógica |
| R-C-05 | A solução não afirma melhorar a fluência do usuário — apenas oferece prática e feedback | Integridade acadêmica — regra 01-academic-integrity.mdc |
| R-C-06 | Nenhuma tecnologia específica é obrigatória — a escolha deve ser fundamentada em avaliação técnica | Princípio de não comprometer tecnologia prematuramente (Fase 5) |

---

## 4. Dependências

| Dependência | Tipo | Impacto se não resolvida |
|-------------|------|-------------------------|
| Escolha de API de ASR compatível com sotaque brasileiro | Técnica | Protótipo pode não funcionar adequadamente — R-01 |
| Escolha de LLM para geração de diálogo | Técnica | Sem isso, o protótipo não pode ser construído |
| Escolha de TTS com latência aceitável | Técnica | Latência alta inviabiliza a experiência conversacional — R-05 |
| Recrutamento de 5–8 participantes com perfil Ana Souza | Logística | Sem participantes, H-01 não pode ser testada |
| Definição do prazo com o orientador | Acadêmica | Objetivo SMART permanece com elemento T provisório — D-04 |

---

## 5. Requisitos Funcionais (RF)

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | O sistema deve apresentar ao usuário ao menos um cenário de conversação antes de iniciar | Essencial |
| RF-02 | O sistema deve capturar o áudio do usuário via microfone do dispositivo | Essencial |
| RF-03 | O sistema deve converter o áudio em texto com acurácia suficiente para continuar o diálogo | Essencial |
| RF-04 | O sistema deve enviar o texto do usuário e o histórico do diálogo para a IA e receber uma resposta | Essencial |
| RF-05 | O sistema deve sintetizar a resposta da IA em voz e reproduzi-la ao usuário | Essencial |
| RF-06 | O sistema deve exibir uma tela de feedback estruturado ao final da sessão | Essencial |
| RF-07 | O sistema deve apresentar termo de consentimento informado antes de iniciar qualquer sessão | Essencial |
| RF-08 | O sistema deve coletar o questionário SUS e a escala de ansiedade pré/pós sessão | Essencial (para o teste) |
| RF-09 | O sistema deve exibir indicador visual de processamento enquanto aguarda resposta da IA | Desejável |
| RF-10 | O sistema deve oferecer modo de texto como fallback quando o ASR falhar de forma grave | Desejável |

---

## 6. Requisitos Não Funcionais (RNF)

| ID | Requisito | Valor alvo | Status |
|----|-----------|------------|--------|
| RNF-01 | Latência da resposta da IA | < 5 segundos | `[ALVO PROVISÓRIO]` |
| RNF-02 | Compatibilidade de navegador | Chrome e Firefox modernos (versões atuais) | Essencial para o teste |
| RNF-03 | Proteção de dados | Nenhum áudio ou transcrição retido além da sessão sem consentimento adicional | Essencial — LGPD |
| RNF-04 | Disponibilidade durante o teste | 99% durante o período do teste presencial | Essencial |
| RNF-05 | Acessibilidade básica | Contraste adequado; botões com rótulos; sem dependência de cor como único indicador | Desejável |

---

## 7. Rastreabilidade: Requisitos → Funcionalidades → Hipóteses

| Requisito | Funcionalidade (Fase 5) | Hipótese testada |
|-----------|------------------------|-----------------|
| RF-01 | F01 — Seleção de cenário | H-01 |
| RF-02, RF-03 | F03 — Conversa por voz (ASR) | H-01 |
| RF-04, RF-05 | F04 — Resposta oral da IA (TTS) | H-01, H-02 |
| RF-06 | F05 — Feedback pós-conversa | H-01, H-03 |
| RF-07, RF-08 | Instrumentos de teste | H-01 |
| RF-10 | F12 — Modo de texto (fallback) | Mitigação R-01 |
