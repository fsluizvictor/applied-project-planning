# Solução Proposta — Fase 6: Solução SMART e Validação

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Solution Specifier
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Descrição da Solução

A solução proposta é um **protótipo de simulador de conversação em inglês por voz, com suporte de inteligência artificial (IA)**, voltado a pessoas que precisam utilizar o inglês em situações práticas do cotidiano profissional. O protótipo é um artefato de validação — seu propósito é testar se a abordagem é útil, utilizável e reduz a ansiedade de fala do público-alvo, antes de qualquer decisão de desenvolvimento em escala.

A solução responde diretamente ao problema identificado nas Fases 2 e 3: a principal barreira à produção oral em inglês é psicológica (ansiedade, medo de errar, baixa autoconfiança), agravada pela falta de oportunidades de prática de baixa pressão e acessíveis. Um simulador baseado em IA oferece um interlocutor disponível sob demanda, sem julgamento humano, com feedback estruturado — características que, segundo a literatura revisada, têm potencial de reduzir a ansiedade de fala (ÖLMEZER-ÖZTÜRK; ÖZTÜRK, 2021; FATHI; RAHIMI; DERAKHSHAN, 2024) `[FONTE-SECUNDÁRIA]`.

---

## 2. Jornada do Usuário

### 2.1 Fluxo principal (persona Ana Souza)

```
1. ENTRADA
   Usuário acessa o protótipo via interface web
   └── Sem cadastro necessário no protótipo de teste

2. SELEÇÃO DE CENÁRIO
   Usuário escolhe: "Entrevista de Emprego em Inglês (Área de Tecnologia)"
   └── Versão futura: outros cenários disponíveis (reuniões, cotidiano)

3. CONFIGURAÇÃO (opcional no MVP)
   Usuário indica nível de inglês: Básico / Intermediário / Avançado
   └── A IA adapta vocabulário e complexidade das perguntas

4. INÍCIO DA SIMULAÇÃO
   IA apresenta-se como entrevistador fictício e faz a primeira pergunta em inglês (voz)
   └── Ex.: "Tell me a little bit about yourself and your experience with software development."

5. RESPOSTA DO USUÁRIO
   Usuário responde em inglês por voz (microfone)
   └── Sistema converte fala em texto via ASR
   └── Texto enviado à IA junto com histórico do diálogo

6. RESPOSTA DA IA
   IA processa a resposta e responde por voz (TTS), dando continuidade ao diálogo
   └── Latência alvo: < 5 segundos (restrição de design)
   └── A IA NÃO corrige durante a conversa — mantém o fluxo natural

7. CONVERSA (ciclos 4–6, duração estimada: 5–10 minutos)
   Usuário e IA alternam turnos até o encerramento do cenário

8. ENCERRAMENTO
   Usuário encerra a sessão (botão "Finalizar")

9. FEEDBACK PÓS-CONVERSA
   Sistema exibe tela de feedback estruturado:
   - Resumo do que foi dito (transcrição resumida)
   - Pontos positivos (ex.: vocabulário relevante utilizado, clareza nas respostas)
   - Áreas de melhoria (ex.: estrutura das frases, escolha de tempo verbal)
   - Sugestão de próxima prática
   └── Feedback é gerado pela IA com base no histórico completo da conversa

10. AVALIAÇÃO DO USUÁRIO (coleta de dados para o teste)
    Usuário responde escala de ansiedade pós-sessão + questionário SUS
```

---

## 3. Especificação Conceitual do Comportamento Esperado

| Componente | Comportamento esperado | Restrição / Limitação |
|------------|----------------------|----------------------|
| **Seleção de cenário** | Interface simples com cartões de cenário; no MVP apenas "Entrevista de Emprego — Tecnologia" | Cenários adicionais: fora do escopo v1 |
| **IA (LLM)** | Mantém papel de entrevistador durante toda a sessão; faz perguntas realistas de entrevista de emprego tech; não corrige o usuário durante a conversa | Não simula emoções humanas complexas; pode ter incoerências em conversas muito longas (limitação de contexto de LLMs) |
| **ASR (reconhecimento de fala)** | Converte voz do usuário em texto com acurácia suficiente para continuar o diálogo | Taxa de erro elevada para sotaque brasileiro documentada (R-01); o sistema deve ter tolerância a erros de reconhecimento — responder de forma coerente mesmo com transcrição imperfeita |
| **TTS (síntese de voz)** | Resposta da IA em voz natural em inglês; latência < 5 segundos `[ALVO PROVISÓRIO — requires validation]` | Voz sintética pode romper a imersão; é limitação conhecida do protótipo |
| **Feedback pós-conversa** | Estruturado em 3 seções: pontos positivos, áreas de melhoria, próximos passos; tom encorajador antes do corretivo; baseado na transcrição completa da conversa | Qualidade do feedback depende do prompt de sistema e da qualidade do LLM escolhido (risco R-08) |
| **Interface** | Web, responsiva para desktop e mobile; sem cadastro necessário para o teste | Requisitos mínimos: microfone funcional, conexão de internet estável |

---

## 4. O Protótipo NÃO É Um Produto Completo

| O que o protótipo É | O que o protótipo NÃO É |
|--------------------|------------------------|
| Um artefato de validação da hipótese H-01 | Um produto pronto para uso em escala |
| Uma experiência de conversação de baixa fidelidade em um cenário | Uma ferramenta completa de aprendizado de idiomas |
| Um teste de aceitação e usabilidade | Uma prova de que a solução melhora a fluência do usuário |
| Um ponto de partida para iteração | Uma solução definitiva para o problema de prática oral |

---

## 5. Considerações de Privacidade, Consentimento e Acessibilidade

| Tema | Tratamento no protótipo |
|------|------------------------|
| **Áudios do usuário** | Não retidos além da sessão; processados em memória e descartados ao encerrar | 
| **Consentimento** | Termo de consentimento informado obrigatório antes do início do teste: informa o que é capturado, por quanto tempo e para qual finalidade |
| **LGPD** | O protótipo de teste não retém dados pessoais além do necessário para a sessão; nenhum dado é compartilhado com terceiros `[ASSUMPTION — requires validation D-03: depende da API de ASR escolhida]` |
| **Acessibilidade** | Interface em português e inglês; botões com rótulos claros; modo de texto como fallback (F12) se ASR falhar | 
| **Erros de reconhecimento de fala** | O sistema exibe a transcrição ao usuário e oferece opção de redigitar manualmente se a transcrição estiver muito incorreta |
| **Respostas inadequadas da IA** | O prompt de sistema deve instruir explicitamente a IA a permanecer no papel de entrevistador; evitar respostas fora do contexto; recusar solicitações que fujam ao cenário |
| **Latência** | Se a resposta da IA demorar mais de 8 segundos, o sistema exibe indicador visual de "processando" para evitar que o usuário acredite que houve erro |
