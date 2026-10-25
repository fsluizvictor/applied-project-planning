# Justificativa do Projeto — Fase 4

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Curso:** Pós-Graduação em Arquitetura de Software e Soluções com IA
**Agente responsável:** Hypothesis & Risk Analyst
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Declaração do Problema

O domínio da comunicação oral em inglês constitui uma das principais lacunas de competência profissional e educacional do Brasil. A literatura revisada na Fase 2 evidencia que a barreira central à produção oral em inglês não é predominantemente linguística, mas psicológica: ansiedade de fala, medo de cometer erros e baixa autoconfiança situacional — fatores documentados em múltiplas revisões sistemáticas de estudos empíricos com aprendizes de inglês como língua estrangeira (EFL) `[FONTE-SECUNDÁRIA]` (DEWITT; MOOSAVI, 2022; SERAJ; HABIL, 2021; MACINTYRE et al., 1998).

Dados quantitativos confirmam a extensão do problema no contexto nacional: o Brasil ocupa a 75ª posição no Índice de Proficiência em Inglês EF (EF EPI 2025), com pontuação de 482 pontos — abaixo da média global de 488. Entre as quatro habilidades avaliadas, a fala obteve 464 pontos, configurando-se como uma das mais fracas `[FONTE-SECUNDÁRIA]` (EF EDUCATION FIRST, 2025). Pesquisas acadêmicas sobre o ensino público brasileiro reforçam esse padrão: 70% dos alunos do ensino médio e técnico pesquisados nunca realizaram uma prova oral de inglês na escola `[FONTE-SECUNDÁRIA]` (CORRÊA, 2017). Análise de política educacional indica que apenas 3% da população brasileira fala inglês, fenômeno atribuído, entre outros fatores, à priorização da leitura em detrimento da produção oral nos documentos curriculares `[FONTE-SECUNDÁRIA]` (BATISTA, 2020).

Fora do ambiente escolar, a situação não é melhor: dados de pesquisa de mercado indicam que 46% dos respondentes não tiveram oportunidades suficientes de prática de conversação em sala de aula e 50% não encontraram ambientes para praticar fora da escola — embora a metodologia completa dessa pesquisa não tenha sido verificada de forma independente `[FONTE-SECUNDÁRIA com ressalva — lacuna B-02]` (DIRETTRIX, 2024; PORVIR, 2024).

---

## 2. Relevância e Público Afetado

O problema afeta diretamente pessoas que precisam utilizar o inglês em situações práticas do cotidiano profissional ou pessoal — entrevistas de emprego, reuniões internacionais, apresentações e interações cotidianas —, especialmente aquelas cujo percurso escolar não ofereceu prática oral adequada. As personas identificadas na Fase 3 (`deliverables/phase-3/personas.md`) representam dois perfis típicos desse público:

- **Ana Souza** — profissional de tecnologia com inglês intermediário, que enfrenta ansiedade de fala em contexto profissional e carece de prática conversacional acessível e contextualizada.
- **Bruno Lima** — estudante ou recém-formado com experiência oral quase nula, cuja formação escolar não ofereceu prática de conversação.

A combinação de demanda profissional crescente por inglês, baixo nível de proficiência oral nacional e ausência de soluções acessíveis e eficazes para a prática de conversação cria uma lacuna que justifica a investigação de uma solução digital.

---

## 3. Benefícios Esperados versus Resultados Demonstrados

> **Distinção obrigatória:** os benefícios a seguir são **esperados** — derivados de evidências da literatura, não de resultados já obtidos por este projeto. A distinção entre "o que a literatura indica" e "o que este projeto demonstrou" é central para a integridade acadêmica desta proposta.

### 3.1 Benefícios com base na literatura (plausíveis, não garantidos)

| Benefício esperado | Base na literatura | Ressalva |
|-------------------|-------------------|----------|
| Redução da ansiedade de fala após sessões repetidas com simulador de baixa pressão | Intervenções de baixa pressão reduziram ansiedade em ~30% em estudos experimentais (ÖLMEZER-ÖZTÜRK; ÖZTÜRK, 2021; TABUCHI et al., 2024) | Estudos realizados em outros contextos nacionais; aplicabilidade ao público brasileiro é `[INFERÊNCIA]` |
| Aumento da disposição para comunicar (WTC) | Chatbot de IA aumentou WTC em comparação ao grupo controle (FATHI; RAHIMI; DERAKHSHAN, 2024) | Estudo de contexto não brasileiro; resultados não são uniformes (CHEN et al., 2024) |
| Aumento da quantidade de prática oral disponível | A IA pode oferecer prática ilimitada, sem restrição de horário ou parceiro humano | Não é resultado de aprendizagem — é benefício de acesso |
| Aumento de autoconfiança percebida para conversas reais já após uma sessão | Registrado por Tyen; Caines; Buttery (2024) com LLM em contexto de conversação | Autoconfiança percebida ≠ melhoria de fluência mensurável — distinção importante |

### 3.2 O que este projeto NÃO demonstrou (e não pode afirmar sem teste)

- Que o simulador proposto **melhora a fluência** do público-alvo — isso requer avaliação antes-e-depois com instrumento validado.
- Que o simulador é **superior a outras alternativas** (tutoria humana, cursos presenciais, outros chatbots) — isso requer comparação controlada.
- Que o simulador é **viável tecnicamente** no prazo e custo planejados — isso requer prototipagem e teste técnico.

---

## 4. Por Que Vale a Pena Testar uma Solução Digital

A literatura revisada apoia a plausibilidade de um simulador de conversação com IA pelas seguintes razões:

1. **A barreira é de acesso a prática, não apenas de conhecimento** — o problema central (falta de oportunidades de conversação de baixa pressão) é estruturalmente endereçável por uma ferramenta digital disponível sob demanda `[FONTE-SECUNDÁRIA]` (DEWITT; MOOSAVI, 2022; SERAJ; HABIL, 2021).
2. **A IA conversacional demonstrou efeito positivo em contextos similares** — meta-análise de 28 estudos (g = 0,484) e estudos individuais específicos `[FONTE-SECUNDÁRIA]` (WANG et al., 2024; FATHI; RAHIMI; DERAKHSHAN, 2024), com a ressalva de que os resultados não são uniformes (CHEN et al., 2024).
3. **Soluções existentes têm lacunas identificadas** — ferramentas de pronúncia (ELSA Speak) e ferramentas de conversação aberta (Speak, Talkpal) tendem a ser separadas; nenhuma solução comercial revisada resolveu de forma comprovada as limitações de reconhecimento de fala não nativa `[FONTE-SECUNDÁRIA]` (context-report.md, Seção 6).
4. **O custo de um teste controlado é menor do que o custo de não testar** — desenvolver um protótipo de baixa fidelidade para um teste de usabilidade e aceitação é um investimento proporcional ao tamanho do problema e ao valor potencial da solução.

---

## Referências utilizadas neste documento

Fontes completas em `deliverables/phase-2/context-report.md`, Seção 10. Nenhuma fonte nova foi adicionada.

- BATISTA, 2020 | CORRÊA, 2017 | DEWITT; MOOSAVI, 2022 | DIRETTRIX, 2024 | EF EDUCATION FIRST, 2025
- FATHI; RAHIMI; DERAKHSHAN, 2024 | MACINTYRE et al., 1998 | ÖLMEZER-ÖZTÜRK; ÖZTÜRK, 2021
- PORVIR, 2024 | SERAJ; HABIL, 2021 | TABUCHI et al., 2024 | TYEN; CAINES; BUTTERY, 2024
- WANG et al., 2024 | CHEN et al., 2024
