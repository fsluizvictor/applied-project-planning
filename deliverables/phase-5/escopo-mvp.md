# Escopo do MVP — Fase 5: Priorização e MVP

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Idea Prioritizer
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Definição do MVP

O Produto Mínimo Viável (MVP) deste projeto é um **protótipo de simulador de conversação por voz com IA**, de baixa fidelidade, cujo propósito exclusivo é **validar a hipótese H-01**: testar se o público-alvo considera a ferramenta útil e utilizável e se a experiência de conversação de baixa pressão reduz a ansiedade de fala autorrelatada.

> **O protótipo NÃO é um produto completo.** Não visa cobrir todas as situações práticas, todos os perfis de usuário ou todas as funcionalidades identificadas na Fase 5. Seu escopo é deliberadamente estreito para ser construído e testado rapidamente.

---

## 2. Funcionalidades Incluídas no MVP

| ID | Funcionalidade | Por que é essencial no MVP |
|----|---------------|---------------------------|
| F01 | Seleção de cenário prático | Define o contexto da simulação; sem isso, a IA não tem base para gerar o diálogo; cenário inicial: **entrevista de emprego em inglês** |
| F03 | Conversa por voz (captura de áudio / ASR) | Componente central — sem voz, não há prática de produção oral |
| F04 | Resposta oral da IA (TTS) | Torna a interação conversacional e de baixa pressão — simulação de interlocutor real |
| F05 | Feedback pós-conversa | Diferencial do produto; necessário para testar a percepção de utilidade |

**Cenário do MVP:** entrevista de emprego em inglês na área de tecnologia — selecionado porque:
- É o cenário com maior volume de evidência indireta (módulo "Interview Coach" de ferramentas existentes; pesquisa Pearson sobre inglês e empregabilidade)
- É o cenário central da persona principal (Ana Souza)
- Tem escopo conversacional bem definido — mais fácil de projetar e avaliar do que conversas abertas

> `[ASSUMPTION — requires validation]`: O cenário de entrevista de emprego é a escolha mais suportada pela evidência disponível, mas B-01 permanece em aberto. Se uma pesquisa primária revelar outro cenário como prioritário, este escopo deve ser revisado.

---

## 3. Funcionalidades Desejáveis (v1.1 ou após validação)

| ID | Funcionalidade | Condição para inclusão |
|----|---------------|----------------------|
| F02 | Configuração de nível de inglês | Incluir se o perfil Bruno Lima (iniciante) for recrutado para o teste — sem adaptação de dificuldade, o teste pode ser inviável para esse perfil |
| F06 | Transcrição da conversa | Incluir se o tempo de desenvolvimento permitir — aumenta valor do feedback |
| F12 | Modo de texto (fallback) | Incluir se testes técnicos de ASR indicarem alta taxa de erro com o público-alvo |

---

## 4. Funcionalidades Excluídas do MVP

| ID | Funcionalidade | Razão |
|----|---------------|-------|
| F08 | Feedback em tempo real | Interrompe o fluxo; alto esforço; risco de aumentar ansiedade |
| F09 | Avaliação de pronúncia | Exige sistema especializado; alto risco R-01 |
| F07 | Histórico de sessões | Irrelevante para teste de uma sessão |
| F10 | Perfil de usuário e progresso | Fora do escopo de um protótipo de teste |
| F11 | Múltiplos sotaques da IA | Complexidade sem impacto no teste da hipótese principal |

---

## 5. Por Que Este Escopo é Suficiente para Testar H-01

A hipótese H-01 requer:
1. ✅ Uma sessão de conversação em cenário prático → coberta por F01 + F03 + F04
2. ✅ Feedback ao final → coberto por F05
3. ✅ Medição de usabilidade → realizada com questionário pós-sessão (SUS ou similar)
4. ✅ Medição de ansiedade autorrelatada → realizada com escala pré e pós sessão

As funcionalidades desejáveis e excluídas não são necessárias para testar H-01 — apenas para melhorar a experiência ou cobrir casos de uso mais amplos.

---

## 6. Dependências Técnicas do MVP

| Componente | Dependência | Risco associado | Decisão de implementação |
|------------|-------------|-----------------|------------------------|
| ASR (reconhecimento de fala) | Serviço ou modelo de STT | R-01 (alto) — viés para sotaque | Avaliar múltiplos modelos antes de fixar; não comprometido nesta fase |
| LLM (geração de resposta) | API de LLM ou modelo local | R-05 (latência), R-06 (custo) | Avaliar opções de custo-benefício (GPT-4o mini, Gemini Flash, etc.) — não comprometido nesta fase |
| TTS (síntese de voz) | Serviço de text-to-speech | R-05 (latência) | Idem LLM — não comprometido nesta fase |
| Interface de usuário | Web ou mobile | R-07 (acessibilidade) | Interface web simples é suficiente para o protótipo |

> **Nota:** nenhuma tecnologia específica foi selecionada nesta fase. A Fase 6 (Solution Specifier) deve avaliar opções e documentar a decisão — conforme a restrição do brief da Fase 5 ("Não escolha tecnologias sem necessidade").

---

## 7. Alinhamento MVP ↔ Hipóteses ↔ Personas

| Elemento do MVP | Hipótese que testa | Persona atendida |
|----------------|-------------------|-----------------|
| Cenário de entrevista de emprego | H-01 (utilidade e usabilidade percebidas) | Ana Souza (principal) |
| Conversa por voz (sem julgamento humano) | H-01 (redução de ansiedade) + H-02 (menor pressão que com humano) | Ambas |
| Feedback pós-conversa | H-01 (utilidade) + H-03 (lacuna de ferramentas existentes) | Ana Souza (principal) |

---

## 8. Rastreabilidade: Problema → Necessidade → Funcionalidade

| Dor / Necessidade (Fase 3) | Funcionalidade do MVP |
|---------------------------|----------------------|
| Falta de oportunidades de prática oral de baixa pressão | F01 + F03 + F04 — simulação de conversação disponível sob demanda |
| Ausência de feedback corretivo imediato | F05 — feedback estruturado pós-conversa |
| Ansiedade em contexto com julgamento humano | F04 — IA como interlocutor não humano, sem consequência real |
| Necessidade de cenário profissional realista | F01 — seleção de cenário prático (entrevista de emprego) |
