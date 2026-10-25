# Log de Decisões — Fase 2

> Continuação da numeração iniciada em `deliverables/phase-1/decision-log.md` (Decisões 001–003).
> Novas entradas devem ser acrescentadas ao final; entradas existentes não devem ser modificadas.

---

### Decisão 004 — 25 de outubro de 2026

**Fase:** 2 — Análise de Contexto e Pesquisa
**Agente / Autor:** Context Researcher
**Decisão:** Incluir, dentro de `context-report.md`, uma seção de perguntas de pesquisa e um roteiro curto de entrevista para validação futura (tarefa 6 de `phases/02_contexto_problema.md`), em vez de criar um arquivo separado `docs/05_user_research_plan.md`.
**Racional:** O agente oficial desta fase (`.cursor/agents/context-researcher.md`) não lista um arquivo de plano de pesquisa entre seus quatro entregáveis obrigatórios. Entretanto, o brief original da fase solicita explicitamente essa entrega. A solução adotada preserva o conteúdo solicitado sem violar a convenção de diretórios já estabelecida na Decisão 001 (Fase 1).
**Alternativas consideradas:**
- Opção A: Criar `docs/05_user_research_plan.md` conforme o brief literal — rejeitada por repetir o conflito já resolvido na Decisão 001.
- Opção B: Omitir completamente o roteiro de pesquisa — rejeitada por descumprir a tarefa 6 do brief sem necessidade.
- Opção C: Incluir o conteúdo como seção dentro de `context-report.md` — **adotada**.

**Impacto nos entregáveis:** `context-report.md`, Seção 7, contém as perguntas de pesquisa e o roteiro de entrevista.
**Reversibilidade:** Fácil — o conteúdo pode ser extraído para um arquivo dedicado em fase futura, se necessário.

---

### Decisão 005 — 25 de outubro de 2026

**Fase:** 2 — Análise de Contexto e Pesquisa
**Agente / Autor:** Context Researcher
**Decisão:** Formular um "desafio preliminar centrado no usuário" (tarefa 7 do brief original) dentro de `context-report.md`, explicitamente rotulado como não definitivo e sujeito a revisão formal na Fase 4.
**Racional:** `PLAN.md` atribui a definição formal do problema (insights, declarações "Como Podemos...", hipóteses com classificação de risco) à Fase 4 (agente `hypothesis-risk`). Omitir completamente a tarefa 7 descumpriria o brief original sem necessidade; apresentá-la como definição final violaria o escopo estreito da Fase 2 e a regra `04-phase-transitions.mdc` ("não avance para fases posteriores").
**Alternativas consideradas:**
- Opção A: Omitir a formulação do desafio — rejeitada por descumprir a tarefa 7 sem necessidade.
- Opção B: Apresentar o desafio como definição final do problema — rejeitada por antecipar o escopo da Fase 4.
- Opção C: Apresentar uma formulação preliminar, claramente rotulada como tal, fundamentada apenas na evidência já reunida — **adotada**.

**Impacto nos entregáveis:** `context-report.md`, Seção 8.
**Reversibilidade:** Fácil — a Fase 4 pode substituir, refinar ou descartar essa formulação preliminar livremente.

---

### Decisão 006 — 25 de outubro de 2026

**Fase:** 2 — Análise de Contexto e Pesquisa
**Agente / Autor:** Context Researcher
**Decisão:** Excluir das referências o artigo de Xiao, Zhang e He ("The promises and challenges of AI-based chatbots in language education through the lens of learner emotions"), inicialmente localizado em busca sobre limitações de IA, por ter sido formalmente retratado pelo periódico (retratação publicada em *Heliyon*, 27 de janeiro de 2025).
**Racional:** A regra `01-academic-integrity.mdc` exige que nenhuma citação cujo conteúdo não possa ser considerado confiável seja apresentada como evidência válida. Um artigo retratado não atende a esse padrão, independentemente de seu conteúdo específico.
**Alternativas considerads:**
- Opção A: Citar o artigo com uma ressalva de retratação no corpo do texto — rejeitada por risco de uso indevido da citação por leitores que não notem a ressalva.
- Opção B: Excluir completamente o artigo das referências e registrar apenas que ele foi identificado e descartado — **adotada**.

**Impacto nos entregáveis:** `context-report.md`, Seção 5.2 (nota de integridade acadêmica) e Seção 10 (nota ao final das referências).
**Reversibilidade:** Não aplicável — decisão de integridade acadêmica, não deve ser revertida.

---

<!-- Append new entries below this line -->
