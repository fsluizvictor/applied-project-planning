# Requisitos do Projeto — Fase 1: Planejamento e Análise

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA  
**Responsável:** Requirements Analyst (Fase 1)  
**Data:** 25 de outubro de 2026  
**Versão:** 1.0

---

## 1. Descrição do Projeto

Proposta de um protótipo de simulador de conversação em inglês por voz, com apoio de inteligência artificial (IA), voltado a pessoas que precisam utilizar o inglês em situações práticas do cotidiano profissional ou pessoal. O produto do projeto é uma **proposta acadêmica** no formato "Desafio e Solução", produzida segundo os critérios avaliativos da disciplina.

> [ASSUMPTION — requires validation]: O nome exato da disciplina, a instituição de ensino e o semestre letivo não foram informados no brief. Registrado como lacuna.

---

## 2. Escopo do Projeto

### 2.1 Dentro do Escopo

- Elaboração de proposta acadêmica completa no formato "Desafio e Solução"
- Análise de contexto e pesquisa bibliográfica (Fase 2)
- Desenvolvimento de personas e mapas de empatia (Fase 3)
- Definição do problema central, hipóteses e riscos (Fase 4)
- Ideação e priorização de soluções (Fase 5)
- Especificação da solução proposta, incluindo descrição do protótipo de IA (Fase 6)
- Revisão acadêmica e montagem da proposta final (Fases 7–8)
- Cobertura dos 11 critérios de avaliação da rubrica da disciplina

### 2.2 Fora do Escopo

- Desenvolvimento e implementação técnica do software
- Condução de entrevistas ou pesquisa primária nesta fase (Fase 1)
- Validação empírica com usuários reais
- Comprometimento com cronograma de lançamento do produto
- Análise financeira ou de mercado aprofundada

---

## 3. Partes Interessadas (Stakeholders)

| # | Grupo | Papel | Interesse principal |
|---|-------|-------|-------------------|
| 1 | **Usuários-alvo** | Beneficiários da solução proposta | Praticar inglês conversacional em situações reais (entrevistas de emprego, reuniões, viagens) |
| 2 | **Professores avaliadores** | Avaliadores da proposta acadêmica | Verificar o cumprimento dos 11 critérios da rubrica com rigor acadêmico |
| 3 | **Autores / equipe acadêmica** | Produtores da proposta | Entregar proposta aprovada dentro dos padrões exigidos |
| 4 | **Comunidade acadêmica** | Leitores secundários | Reprodutibilidade e integridade do raciocínio apresentado |

> [ASSUMPTION — requires validation]: Não foi confirmado se o projeto é individual ou em grupo. Registrado como lacuna.

---

## 4. Restrições

### 4.1 Acadêmicas

- A proposta deve ser estruturada segundo os 11 critérios de avaliação (ver Seção 5).
- Todas as afirmações empíricas devem ter fonte verificável; é proibido fabricar dados ou citações.
- A revisão acadêmica (Fase 7) deve ser conduzida de forma independente, sem reutilizar contexto de sessões anteriores.

### 4.2 De Idioma

- Todos os entregáveis acadêmicos devem ser redigidos em **português brasileiro**, no registro formal acadêmico.
- Arquivos de harness (regras, definições de agentes, templates) são mantidos em inglês.

### 4.3 Técnicas

- O protótipo deve ser descrito como **prova de conceito**, sem comprometimento de implementação.
- O componente de IA deve ter escopo, papel e limitações claramente declarados.

### 4.4 Éticas

- Proibido fabricar entrevistas, resultados de pesquisa, citações ou estatísticas.
- Premissas não verificadas devem ser sinalizadas com `[ASSUMPTION — requires validation]`.
- Lacunas de evidência devem ser registradas com `[LACUNA DE EVIDÊNCIA]`.

### 4.5 De Prazo

> [ASSUMPTION — requires validation]: O prazo de entrega da disciplina não foi informado no brief. A estrutura de fases do projeto implica entregas sequenciais com aprovação humana entre cada fase.

### 4.6 De Processo

- Cada fase exige aprovação humana explícita antes de avançar para a próxima.
- Agentes não devem iniciar a próxima fase na mesma sessão em que recebem aprovação.

---

## 5. Mapeamento dos 11 Critérios de Avaliação

Os critérios a seguir foram extraídos diretamente de `phases/01_planejamento.md`. Não foi localizado no workspace um documento PDF ou rubrica detalhada da disciplina com descritores de nível de desempenho.

> [LACUNA DE EVIDÊNCIA — rubrica completa]: O documento original da disciplina com descritores detalhados de cada critério não está disponível no workspace. Os critérios abaixo são identificados pelos rótulos; os descritores precisam ser obtidos com o docente ou no portal da disciplina antes da Fase 7.

| # | Critério | Fase responsável | Entregável principal | Restrição / Observação |
|---|----------|-----------------|---------------------|------------------------|
| 1.1.1 | Clareza e Estrutura | Todas (transversal) | `proposta-desafio-e-solucao.md` (Fase 8) | Documento deve ter estrutura coerente, seções bem delimitadas e linguagem clara |
| 1.1.2 | Análise do Contexto | Fase 2 | `context-report.md` | Toda afirmação deve ser rastreável a fontes reais |
| 1.1.3 | Desafio (Problema) | Fase 4 | `insights.md`, `hmw-statements.md` | O problema deve emergir da pesquisa, não ser pressuposto |
| 1.1.4 | Área do Conhecimento do Curso | Fase 1 e Fase 6 | `requirements.md`, `solution-spec.md` | Deve ficar claro como o projeto se relaciona com a área de conhecimento da disciplina |
| 1.1.5 | Persona + Mapa de Empatia | Fase 3 | `personas.md`, `empathy-maps.md` | Mínimo de duas personas; mapa com quatro quadrantes |
| 1.1.6 | Justificativa | Fase 4 | `hypotheses.md` | Justificativa deve ser fundamentada em dados da Fase 2 |
| 1.1.7 | Hipótese | Fase 4 | `hypotheses.md` | Mínimo de três hipóteses testáveis |
| 1.1.8 | Matriz de Observação | Fase 3 | `observation-matrix.md` | Populada a partir de fontes secundárias reais |
| 1.1.9 | Identificação do Grau de Risco | Fase 4 | `risk-register.md` | Escala de probabilidade × impacto documentada |
| 1.1.10 | Priorização de Ideias | Fase 5 | `prioritization-matrix.md` | Rubrica de pontuação documentada (impacto × viabilidade ou equivalente) |
| 1.1.11 | Apresentação e Estilo | Fase 8 (transversal) | `proposta-desafio-e-solucao.md` | Normas ABNT, registro formal, ausência de coloquialismos |

> [ASSUMPTION — requires validation]: Os descritores de nível de desempenho de cada critério (ex.: o que distingue nota máxima de nota parcial) não estão disponíveis. O mapeamento acima reflete a interpretação do agente com base nos rótulos.

---

## 6. Área do Conhecimento do Curso

> [ASSUMPTION — requires validation]: A área do conhecimento do curso não foi especificada no brief. Com base no contexto do projeto ("Inovação, Design e Tecnologia" — IDT, referenciado em `phases/01_planejamento.md`), presume-se que a disciplina situa-se na interseção de **design de produto**, **tecnologia da informação** e **empreendedorismo/inovação**.

A proposta deve demonstrar conexão explícita com os fundamentos da área, incluindo:
- Metodologia de Design Thinking (empatia, definição, ideação, prototipagem, teste)
- Aplicação de IA como ferramenta tecnológica de suporte ao aprendizado
- Análise de problema centrada no usuário

---

## 7. Premissas Não Resolvidas

| # | Premissa | Impacto se não validada | Fase em que deve ser resolvida |
|---|----------|------------------------|-------------------------------|
| A-01 | Prazo de entrega da disciplina desconhecido | Impossível planejar cronograma realista | Fase 1 (obter do usuário) |
| A-02 | Rubrica completa com descritores de nível não disponível | Critérios mapeados apenas pelos rótulos; risco de não atender ao que é efetivamente cobrado | Fase 1 (antes de avançar) |
| A-03 | PDF de instruções e exemplo da disciplina não localizado no workspace | Estrutura da proposta pode divergir do formato esperado | Fase 1 (antes de avançar) |
| A-04 | Nome da disciplina, instituição e semestre não informados | Contextualização acadêmica incompleta | Fase 1 |
| A-05 | Trabalho individual ou em grupo não especificado | Afeta escopo de pesquisa primária e responsabilidades | Fase 1 |
| A-06 | Número mínimo de referências bibliográficas não informado | Fase 2 pode ser insuficiente | Fase 2 |
| A-07 | Obrigatoriedade de pesquisa primária (entrevistas, observação in loco) não confirmada | Fases 3 e 8 podem ser reprovadas se primária for obrigatória | Fase 2 |
| A-08 | Área do conhecimento do curso não confirmada pelo usuário | Critério 1.1.4 pode ser mapeado incorretamente | Fase 1 |

---

## 8. Fontes Inspecionadas Nesta Fase

| # | Arquivo | Status |
|---|---------|--------|
| 1 | `AGENTS.md` | ✅ Lido |
| 2 | `PLAN.md` | ✅ Lido |
| 3 | `phases/01_planejamento.md` | ✅ Lido |
| 4 | `harness.md` | ✅ Lido |
| 5 | `.cursor/agents/requirements-analyst.md` | ✅ Lido |
| 6 | `templates/acceptance-check.md` | ✅ Lido |
| 7 | `templates/phase-handoff.md` | ✅ Lido |
| 8 | `templates/agent-report.md` | ✅ Lido |
| 9 | `templates/decision-log.md` | ✅ Lido |
| 10 | `README.md` | ✅ Lido (conteúdo mínimo) |
| 11 | PDF de instruções da disciplina | ❌ Não localizado no workspace |
| 12 | Rubrica completa de avaliação | ❌ Não localizada no workspace |
