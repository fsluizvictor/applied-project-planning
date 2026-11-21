# Instruções de colagem (apagar antes de entregar)

Este arquivo condensa o material das fases 1 a 7 no padrão do PDF `Exemplo - Desafio - Solução.pdf` e do template XP/IGTI ([documento Google](https://docs.google.com/document/d/1XC7fvK35z4bkLZuxRvoaBk2zEMpBvyAU/edit)). Não é possível editar o Google Docs a partir desta sessão: copiar cada seção para o campo correspondente do template.

**Preencher no template:** nome do aluno, orientador, cidade, data e o texto de conclusão de curso.

**Inserir como figuras (já existem no repositório):**

| Figura | Arquivo |
|--------|---------|
| Figura 1 — Perfil Comportamental Ana Souza | `deliverables/phase-3/assets/persona-ana-souza-perfil.jpg` |
| Figura 2 — Mapa de Empatia Ana Souza | `deliverables/phase-3/assets/persona-ana-souza-empatia.jpg` |
| Figura 3 — Perfil Comportamental Bruno Lima | `deliverables/phase-3/assets/persona-bruno-lima-perfil.jpg` |
| Figura 4 — Mapa de Empatia Bruno Lima | `deliverables/phase-3/assets/persona-bruno-lima-empatia.jpg` |
| Figura 5 — Proposta de Valor | montar no canvas visual do template a partir da subseção 1.1.3 |
| Figura 6 — Definição da Sprint 1 | `deliverables/cronograma-sprints/sprint-1.png` |
| Figura 7 — Definição da Sprint 2 | `deliverables/cronograma-sprints/sprint-2.png` |
| Figura 8 — Interface local | `deliverables/area-de-experimentacao/assets/interface-local.png` |
| Figura 9 — Diagrama de contexto | `deliverables/area-de-experimentacao/assets/contexto.png` |
| Figura 10 — Diagrama de contêineres | `deliverables/area-de-experimentacao/assets/conteineres.png` |
| Figura 11 — Diagrama de sequência de um turno | `deliverables/area-de-experimentacao/assets/sequencia-turno.png` |
| Figura 12 — Definição da Sprint 3 | `deliverables/cronograma-sprints/sprint-3.png` |
| Figura 13 — Tela ao encerrar a sessão-piloto | `deliverables/area-de-experimentacao/assets/sessao-piloto-encerrada.png` |
| CANVAS do Projeto Aplicado | montar no canvas visual do template a partir da seção 1 |

**Capítulo 2:** as Sprints 1 e 2 foram executadas. Na Sprint 3, a sessão-piloto, a nota de privacidade e o DAS na versão 1 foram concluídos em 20 de novembro de 2026. A publicação em nuvem não foi realizada. O texto está em `deliverables/area-de-experimentacao/capitulo-2.md` e no relatório.

---

# Relatório do Projeto Aplicado

**Título:** Simulador de Conversação em Inglês com Inteligência Artificial  
**Curso:** Pós-Graduação em Arquitetura de Software e Soluções com IA  
**Área do conhecimento:** Tecnologia da Informação — Arquitetura de Software  
**Aluno:** [Nome do Aluno]  
**Orientador(a):** [Nome]  
**Cidade / Data:** [Cidade], [data]

Relatório de Projeto Aplicado desenvolvido para fins de conclusão da Pós-Graduação em Arquitetura de Software e Soluções com IA.

---

## 1. CANVAS do Projeto Aplicado

Inserir a figura do CANVAS do template e preencher os blocos com o resumo abaixo.

| Bloco | Conteúdo condensado |
|-------|---------------------|
| **Título / Versão** | Simulador de Conversação em Inglês com IA — v1 (proposta acadêmica) |
| **Análise de Contexto** | A barreira central à fala em inglês é psicológica (ansiedade, medo de errar, baixa disposição para comunicar), agravada pela falta de prática oral no percurso escolar brasileiro. O Brasil ocupa a 75ª posição no EF EPI 2025; a fala pontua 464. |
| **Personas** | Ana Souza (principal): profissional de tecnologia, inglês intermediário, ansiedade em entrevistas. Bruno Lima (secundária): estudante ou recém-formado, prática oral quase nula. |
| **Benefícios e Justificativas** | Prática oral sob demanda, sem julgamento humano; feedback estruturado após a conversa; validação de usabilidade e de redução de ansiedade autorrelatada. Benefícios são esperados com base na literatura, não demonstrados por este projeto. |
| **Hipóteses** | H-01 (principal, GUT 14): o protótipo será útil, utilizável e reduzirá ansiedade. H-02 (11) e H-03 (12) são secundárias. |
| **Objetivo SMART** | Desenvolver e testar um protótipo de voz (entrevista de emprego em tecnologia), medido por SUS ≥ 68, conclusão de tarefa ≥ 60% e redução de ansiedade na maioria dos participantes, em prazo a confirmar com o orientador. |
| **Premissas e Restrições** | Dispositivo com microfone e internet; APIs de ASR, LLM e TTS acessíveis; áudios não retidos além da sessão; ASR avaliado para sotaque brasileiro; o protótipo não afirma melhorar fluência. |
| **Backlog** | Essenciais: F01 seleção de cenário, F03 conversa por voz, F04 resposta oral da IA, F05 feedback pós-conversa. |
| **Área de experimentação** | Sprints 1 e 2 executadas. Em 20 de novembro de 2026 a sessão-piloto durou oito minutos e 22 segundos, com quatro turnos reconhecidos. A nota de privacidade confirma o descarte do áudio da pessoa ao fim do turno; a transcrição fica em memória até o encerramento. O DAS versão 1 foi fechado na mesma data. A publicação em nuvem não foi realizada. |

---

## 1.1 Desafio

**Desafio:** como permitir que profissionais de tecnologia que precisam usar o inglês em entrevistas de emprego pratiquem a produção oral com frequência e apoio suficientes para reduzir a ansiedade de fala e aumentar a disposição para comunicar (*Willingness to Communicate* — WTC), dado que a literatura indica que a barreira principal é a falta de prática de baixa pressão, e não exclusivamente a falta de conhecimento linguístico?

**Declarações “Como Podemos…” (How Might We):**

- **HMW-01:** como oferecer a profissionais de tecnologia com inglês intermediário uma experiência de prática oral de baixa pressão, disponível sob demanda, que simule entrevistas de emprego e forneça feedback imediato?
- **HMW-02:** como reduzir a ansiedade de fala de pessoas que sabem inglês, mas travam ao falar, usando inteligência artificial (IA) como interlocutor não avaliativo, sem substituir a interação humana de alta qualidade?
- **HMW-03:** como tornar o ciclo prática–feedback–melhoria acessível e recorrente para pessoas cujo percurso escolar não ofereceu prática oral adequada?

A IA é uma via possível entre outras. Intervenções de baixa pressão sem IA também reduzem ansiedade (ÖLMEZER-ÖZTÜRK; ÖZTÜRK, 2021; TABUCHI *et al.*, 2024). A escolha do simulador digital é justificada nas seções 1.1.3 e 1.2, não assumida *a priori*.

---

### 1.1.1 Análise de Contexto

O domínio da comunicação oral em inglês permanece uma das principais lacunas de competência profissional e educacional no Brasil. A literatura em ensino de inglês como língua estrangeira (*English as a Foreign Language* — EFL) converge para um achado central: a maior barreira à fala não é predominantemente linguística, e sim psicológica. Revisão sistemática de dezenove estudos empíricos (2018–2022) identificou ansiedade, medo de errar, falta de motivação e baixa autoconfiança como a barreira mais frequente, seguida de problemas ambientais (métodos de ensino, falta de prática) e linguísticos (vocabulário, pronúncia, gramática) (DEWITT; MOOSAVI, 2022). Outra revisão aponta ansiedade e timidez como fatores centrais, associados à falta de prática, ao vocabulário insuficiente e ao medo de crítica (SERAJ; HABIL, 2021).

O modelo de disposição para comunicar (WTC) descreve a decisão de iniciar comunicação em uma segunda língua como processo volitivo, influenciado por autoconfiança situacional, ansiedade e oportunidade (MACINTYRE *et al.*, 1998). Esse modelo é utilizado como referencial teórico, não como evidência empírica coletada junto ao público-alvo deste projeto.

No Brasil, o *EF English Proficiency Index* (EF EPI) 2025, calculado a partir de mais de dois milhões de participantes do teste EF SET em 2024, posiciona o país na 75ª colocação global, com 482 pontos (média global: 488). Entre as quatro habilidades, a fala obteve 464 pontos, uma das mais fracas (leitura 516; compreensão auditiva 468; escrita 442) (EF EDUCATION FIRST, 2025). Estudo de campo com alunos do ensino médio e técnico constatou que 70% dos respondentes do primeiro ano nunca haviam realizado prova oral de inglês na escola (CORRÊA, 2017). Análise de política educacional estima que apenas 3% da população brasileira fala inglês, fenômeno atribuído, entre outros fatores, à priorização da leitura em detrimento da produção oral nos documentos curriculares (BATISTA, 2020).

Pesquisa de mercado da Pearson (2024), relatada por veículos especializados, indica que 85% dos respondentes consideram o inglês vital para o sucesso profissional, 54% afirmam que a educação formal não os capacitou adequadamente, 46% não tiveram treino suficiente de conversação em sala e 50% não encontraram ambientes para praticar fora da escola (DIRETTRIX, 2024; PORVIR, 2024). O relatório primário da Pearson não foi acessado; a metodologia completa não pôde ser verificada de forma independente.

O problema manifesta-se em situações distintas. Ferramentas comerciais já oferecem módulos de *Interview Coach*, *Meeting Coach* e *Presentation Coach*, o que indica demanda percebida para entrevistas e reuniões (ELSA SPEAK, 2026). Não foi localizada evidência específica sobre o cenário de viagem. Não há confirmação primária de qual situação é prioritária para o público-alvo real; o MVP adota entrevista de emprego na área de tecnologia como recorte provisório, por ser o cenário com maior volume de evidência indireta e o mais alinhado à persona principal.

**Soluções existentes.** ELSA Speak concentra-se em análise fonética; Speak e Talkpal oferecem conversação simulada; Cambly oferece tutoria humana ao vivo, com custo elevado para uso diário (HELLOTALK, 2026; TALKPAL, 2026; WIFITALENTS, 2026). Afirmações comerciais de eficácia não foram tratadas como evidência científica. Ferramentas de pronúncia e de conversação aberta tendem a ser oferecidas de forma separada; nenhuma fonte consultada demonstra, de modo auditado, a superação do viés de reconhecimento de fala não nativa.

**Papel da IA.** Meta-análise de 28 estudos encontrou efeito positivo de chatbots sobre a aprendizagem de idiomas (g = 0,484) (WANG *et al.*, 2024). Experimento controlado com 65 aprendizes relatou ganho maior em fluência, coerência, léxico, gramática, pronúncia e WTC no grupo com chatbot (FATHI; RAHIMI; DERAKHSHAN, 2024). Outro estudo, com 53 universitários chineses, **não** encontrou vantagem significativa do agente de IA sobre a interação humana (CHEN *et al.*, 2024). Estudo com 160 aprendizes registrou aumento de autoconfiança percebida já após uma sessão, com ganhos de aprendizagem mensurável limitados no curto prazo (TYEN; CAINES; BUTTERY, 2024). Toda essa evidência de eficácia vem de contextos não brasileiros; a aplicabilidade ao público nacional é inferência, não achado direto.

**Limitações técnicas documentadas.** Sistemas de reconhecimento automático de fala (*Automatic Speech Recognition* — ASR) apresentam taxa de erro elevada para falantes não nativos e viés contra variedades não nativas do inglês (VERHELST; BELPAEME, 2025; JEON; LEE; CORONEL-MOLINA, 2024). Meta-síntese identificou baixa inteligibilidade, interação pouco natural, ausência de retroalimentação corretiva explícita e, em alguns casos, aumento de ansiedade em contexto avaliativo (KOÇ; SAVAŞ, 2024). Revisão de 30 estudos recomenda chatbots como prática suplementar e supervisionada, não como substituto da interação humana (KHAN; HUSSAIN, 2026).

**Síntese.** A IA conversacional pode aumentar a quantidade de prática disponível e reduzir a ansiedade inicial, mas não substitui a interação humana. Qualquer simulador proposto deve tratar ASR, latência, privacidade e qualidade do feedback como restrições de desenho.

**Limitação metodológica desta análise.** Não foi conduzida pesquisa primária (entrevista, questionário ou observação). As evidências são secundárias. Um artigo retratado (XIAO; ZHANG; HE, *Heliyon*, 2025) foi localizado e descartado.

**Pontos urgentes a endereçar:**

- falta de oportunidades de prática oral de baixa pressão e acessíveis;
- ansiedade de fala e baixa WTC em situações profissionais, sobretudo entrevistas;
- lacuna entre ferramentas de pronúncia e ferramentas de conversação contextualizada com feedback integrado;
- viés de ASR contra sotaque não nativo, inclusive o brasileiro.

**Impactos esperados com a investigação da solução** (não demonstrados por este projeto):

- aumento do acesso a prática oral sob demanda;
- ambiente não avaliativo para ensaiar entrevistas;
- feedback estruturado após a conversa;
- decisão fundamentada de iterar, pivotar ou abandonar a abordagem após teste de usabilidade.

---

### 1.1.2 Personas

As duas personas são **provisórias**, inferidas de evidências secundárias. Nenhuma entrevista com usuários reais foi realizada. Nomes são fictícios. Não há citações diretas de usuários.

#### 1.1.2.1 Ana Souza *(persona principal)*

**Figura 1 — Perfil Comportamental Ana Souza**

*(inserir `persona-ana-souza-perfil.jpg`)*

**Figura 2 — Mapa de Empatia Ana Souza**

*(inserir `persona-ana-souza-empatia.jpg`)*

Ana Souza, entre 26 e 32 anos, é analista de sistemas ou desenvolvedora. Lê e compreende inglês de forma razoável, mas fala com hesitação. Precisa do idioma em reuniões internacionais e em entrevistas de emprego em empresas de tecnologia. Pratica fala de forma esporádica. Dores centrais: ansiedade ao falar, medo de errar diante de colegas ou entrevistadores, falta de prática estruturada e ausência de feedback corretivo após práticas informais. Necessita de simulações realistas de trabalho, ambiente de baixa pressão e flexibilidade de horário.

**Mapa de empatia (síntese).** Vê vagas exigindo fluência e colegas que se comunicam em inglês com aparente facilidade. Ouve pressão por “melhorar o inglês” e feedbacks vagos após entrevistas. Pensa e sente que “sabe inglês” para leitura, mas “trava” ao falar. Fala e faz: evita turnos orais, consome conteúdo passivo e raramente pratica fala. Dores de alta intensidade: ansiedade de fala e falta de prática acessível. Ganhos desejados: cenário profissional realista, interlocutor sem julgamento e feedback claro.

#### 1.1.2.2 Bruno Lima *(persona secundária)*

**Figura 3 — Perfil Comportamental Bruno Lima**

*(inserir `persona-bruno-lima-perfil.jpg`)*

**Figura 4 — Mapa de Empatia Bruno Lima**

*(inserir `persona-bruno-lima-empatia.jpg`)*

Bruno Lima, entre 19 e 24 anos, é estudante ou recém-formado em tecnologia. Tem inglês básico a intermediário inferior e experiência oral formal quase nula — padrão compatível com a ausência de provas orais na escola (CORRÊA, 2017). Dores: desconforto acentuado com situações orais, vocabulário insuficiente para contexto profissional e vergonha de errar. Necessita de início gradual, feedback encorajador e construção de confiança antes de situações reais.

**Convergência.** Ambas as personas compartilham a necessidade de prática conversacional de baixa pressão, em cenário prático, com feedback. Essa convergência fundamenta o MVP. Ana Souza é a persona do teste; Bruno Lima informa o risco de dificuldade excessiva e a eventual necessidade de adaptar o nível (funcionalidade desejável F02).

---

### 1.1.3 Justificativas

A implementação de um protótipo de simulador de conversação por voz justifica-se pelos fatores abaixo. Os benefícios são **esperados** com base na literatura; este projeto ainda não os demonstrou.

**Barreira de acesso à prática, não apenas de conhecimento.** A ausência de conversação de baixa pressão é estruturalmente endereçável por ferramenta digital disponível sob demanda (DEWITT; MOOSAVI, 2022; SERAJ; HABIL, 2021).

**Demanda profissional e déficit nacional de fala.** O EF EPI 2025 e os estudos sobre o ensino público documentam baixa proficiência oral. A pesquisa Pearson associa o inglês a vantagem profissional percebida, com ressalva metodológica já declarada.

**Plausibilidade da IA conversacional, com heterogeneidade.** Há efeito médio positivo em meta-análise (WANG *et al.*, 2024) e ganhos em estudo controlado (FATHI; RAHIMI; DERAKHSHAN, 2024), mas resultados não são uniformes (CHEN *et al.*, 2024). Vale testar, não afirmar eficácia prévia.

**Lacuna das ferramentas existentes.** Pronúncia e conversação contextualizada com feedback integrado tendem a estar separadas. Tutoria humana ao vivo tem custo elevado para uso frequente (WIFITALENTS, 2026).

**Custo de testar versus custo de não testar.** Um protótipo de baixa fidelidade, com teste de usabilidade e aceitação, é investimento proporcional ao tamanho do problema.

**O que este projeto não afirma:** melhoria de fluência; superioridade a tutoria humana ou a outros aplicativos; viabilidade técnica já comprovada no prazo e no custo. Essas afirmações exigiriam teste empírico ainda não realizado.

**Proposta de valor (preencher a Figura 5 no canvas visual):**

| Lado do cliente (Ana Souza) | Lado da solução |
|-----------------------------|-----------------|
| **Tarefas:** ensaiar entrevistas em inglês; reduzir o “travamento” oral; receber orientação após a prática | **Produtos e serviços:** simulador de voz com IA no cenário de entrevista de emprego em tecnologia; feedback estruturado pós-conversa |
| **Dores:** ansiedade, falta de parceiro, custo de tutor, apps que não treinam fala real | **Analgésicos:** interlocutor disponível sem julgamento; correção apenas ao final (não interrompe o fluxo); fallback de texto se o ASR falhar |
| **Ganhos:** confiança situacional, prática recorrente, clareza sobre o que melhorar | **Criadores de ganho:** cenário profissional realista; resumo com pontos positivos, áreas de melhoria e próximo passo |

Ajuste da proposta em relação a alternativas: não compete com curso completo de idiomas nem com tutor nativo; posiciona-se como prática suplementar de baixa pressão para um cenário específico.

---

### 1.1.4 Hipóteses

As hipóteses seguem a matriz GUT (Gravidade, Urgência, Tendência), escala de 1 a 5. Somatório = G + U + T (3 a 15). Classificação de risco: baixo 3–6; médio 7–10; alto 11–15. Caso a disciplina adote a fórmula multiplicativa G × U × T, os valores individuais de G, U e T permanecem os mesmos e o somatório deve ser recalculado.

| Observação | Descrição da hipótese | G | U | T | Soma | Priorização | Grau de risco |
|------------|----------------------|---|---|---|------|-------------|---------------|
| Falta de oportunidades de prática oral acessível e de baixa pressão | **H-01.** Um protótipo de simulador de conversação por voz com IA, no cenário de entrevista de emprego em tecnologia, será considerado útil e utilizável pela persona Ana Souza em ao menos uma sessão supervisionada e reduzirá a ansiedade de fala autorrelatada | 5 | 4 | 5 | 14 | Alta | Alto |
| Evitação da prática oral por percepção de alta pressão em contextos humanos | **H-02.** Ambiente de simulação com IA, percebido como não avaliativo, aumentará a disposição do perfil Bruno Lima para iniciar a prática, em comparação à prática com humanos ou em sala de aula | 4 | 3 | 4 | 11 | Média | Alto |
| Lacuna de ferramentas que unam conversação contextualizada e feedback integrado | **H-03.** Solução que combine cenário prático, resposta oral da IA e feedback ao final será percebida como mais relevante do que as alternativas atualmente usadas | 4 | 4 | 4 | 12 | Média | Alto |

**H-01 é a hipótese principal.** É refutada se, após o teste, a maioria dos participantes (>50%) indicar que a ferramenta não é útil ou utilizável, ou se a ansiedade autorrelatada não diminuir (ou aumentar). Fluência e aprendizagem de idioma **não** serão medidas em uma única sessão.

**Matriz de observação → hipótese (síntese).**

| Tema observado | Resultado da fonte | Status | Hipótese alimentada |
|----------------|-------------------|--------|---------------------|
| Barreiras à fala em EFL | Barreira mais frequente: psicológica (DEWITT; MOOSAVI, 2022; SERAJ; HABIL, 2021) | Respondido para EFL em geral; parcial para o Brasil | H-01, H-02 |
| Proficiência oral no Brasil | 75ª posição no EF EPI; fala 464 (EF EDUCATION FIRST, 2025) | Respondido | H-01 |
| Prática oral na escola | 70% nunca fizeram prova oral (CORRÊA, 2017) | Respondido para a amostra; generalização limitada | H-02 |
| Prática fora da escola | 46% sem treino em sala; 50% sem ambiente externo (Pearson *apud* DIRETTRIX, 2024) | Parcial — relatório primário não acessado | H-01 |
| Eficácia de chatbots | Efeito médio positivo (WANG *et al.*, 2024); resultado nulo em CHEN *et al.* (2024) | Respondido fora do Brasil | H-01, H-03 |
| Limitações de ASR | WER elevado e viés contra variedade não nativa | Respondido | restrições de desenho |
| Situação prática prioritária | Sem dado primário | Em aberto | recorte provisório do MVP |
| Eficácia no público brasileiro | Sem dado | Em aberto | H-01 deve ser testada, não assumida |

**Grau de risco do projeto (além da coluna GUT das hipóteses).**

| ID | Risco | G | U | T | Soma | Classe | Mitigação |
|----|-------|---|---|---|------|--------|-----------|
| R-01 | ASR enviesado contra sotaque brasileiro | 5 | 4 | 3 | 12 | Alto | Avaliar Whisper, Google STT e Azure STT com falantes brasileiros antes de fixar a tecnologia |
| R-04 | Privacidade e retenção de áudios (LGPD) | 4 | 3 | 4 | 11 | Alto | Não reter áudio além da sessão; consentimento informado |
| R-05 | Latência do pipeline ASR → LLM → TTS | 4 | 4 | 3 | 11 | Alto | Comparar APIs; indicador visual acima de oito segundos |
| R-08 | Feedback pedagogicamente frágil | 4 | 3 | 4 | 11 | Alto | Prompt explícito; revisão amostral antes do teste |
| R-02 | Heterogeneidade de eficácia na literatura | 4 | 3 | 3 | 10 | Médio | Hipótese refutável; não afirmar resultado prévio |
| R-03 | IA em contexto avaliativo pode aumentar ansiedade | 4 | 3 | 3 | 10 | Médio | Tom não avaliativo; correção só ao final |
| R-06 | Custo de APIs | 3 | 3 | 3 | 9 | Médio | Sessões curtas; modelos de menor custo no teste |
| R-07 | Microfone e conexão instável | 3 | 2 | 3 | 8 | Médio | Requisitos mínimos; fallback de texto |

**Priorização de ideias.** Cinco alternativas foram comparadas. A1 (simulador de voz com IA) foi selecionada por endereçar prática oral, baixa pressão e feedback. Descartadas: A2 chat só texto (não pratica fala); A3 tutoria humana (custo e escala); A4 grupos mediados (complexidade); A5 autoestudo sem IA (sem interação). Doze funcionalidades foram pontuadas por impacto em H-01 (peso 3), impacto no usuário (peso 2) e esforço/risco invertido (peso 1). **MVP:** F01, F03, F04 e F05. Desejáveis: F02, F06, F12. Fora da v1: F07 a F11 (histórico, perfil, sotaques, feedback em tempo real, avaliação fonética).

---

## 1.2 Solução

A solução proposta é um **protótipo de simulador de conversação em inglês por voz, com apoio de IA**, voltado a profissionais de tecnologia que precisam ensaiar entrevistas de emprego. O artefato serve para validar se a abordagem é útil, utilizável e redutora de ansiedade — não é produto comercial nem curso de idiomas.

O fluxo principal (persona Ana Souza): acesso via web, sem cadastro no teste; escolha do cenário “Entrevista de Emprego — Tecnologia”; a IA assume o papel de entrevistador e fala a primeira pergunta; o usuário responde por voz; ASR converte a fala em texto; um modelo de linguagem de grande porte (*Large Language Model* — LLM) gera a continuação **sem corrigir durante o diálogo**; síntese de voz (*Text-to-Speech* — TTS) devolve a fala da IA; após cinco a dez minutos, o usuário finaliza e recebe feedback em três blocos (pontos positivos, áreas de melhoria, próximo passo); em seguida responde SUS e escala de ansiedade.

A solução alinha-se à área do curso ao especificar arquitetura de sistema conversacional: componentes ASR, LLM e TTS, restrições de latência, privacidade, fallback e critérios de validação. Nenhuma marca de API é obrigatória; a escolha ocorre na Sprint 1, após teste com sotaque brasileiro.

**O protótipo é** artefato de validação de H-01. **Não é** produto em escala, ferramenta completa de fluência nem prova de aprendizagem de idioma.

---

### 1.2.1 Objetivo SMART

Desenvolver e testar um protótipo de simulador de conversação em inglês por voz com IA, focado no cenário de entrevista de emprego na área de tecnologia **(S — específico)**; medido por pontuação SUS ≥ 68, taxa de conclusão da tarefa principal sem assistência ≥ 60% e redução de ansiedade autorrelatada em mais da metade dos participantes **(M — mensurável)**; por meio de fluxo ASR + LLM + TTS e feedback estruturado pós-conversa, com tecnologias publicamente disponíveis **(A — atingível)**; a fim de verificar se a conversação de baixa pressão endereça a barreira de prática oral identificada na análise de contexto e nas personas **(R — relevante)**; em prazo a confirmar com o orientador **(T — temporal, provisório)**.

Alvos numéricos são provisórios (ponto de corte SUS da literatura; demais sem base específica deste protótipo). Métricas de fluência ficam fora do teste.

**Etapas propostas (sem datas até confirmação do orientador):** (1) avaliar ASR, LLM e TTS para sotaque brasileiro; (2) implementar o MVP; (3) revisar amostralmente o feedback da IA; (4) recrutar cinco a oito participantes com perfil Ana Souza; (5) sessão supervisionada; (6) analisar e decidir se itera, pivota ou escala.

---

### 1.2.2 Escopo do Projeto (Premissas e Restrições)

Texto para colar no documento:

Dentro do escopo: o Documento de Arquitetura de Software (DAS) e uma prova de conceito web com um único fluxo — cenário de entrevista de emprego em tecnologia, captura de voz, resposta oral da inteligência artificial e feedback ao final em três blocos (pontos positivos, pontos de melhoria e próximo passo).

Fora do escopo: medição de fluência, correção durante a conversa, cadastro ou histórico de sessões, banco de dados, conversa contínua por canal bidirecional, outros cenários, produto comercial e teste formal de usabilidade com amostra externa.

Premissas:

A sessão-piloto dispõe de microfone funcional, de internet estável e de um computador capaz de executar a interface e a API localmente.

Permanece acessível, durante as três sprints, uma oferta gratuita de reconhecimento de fala, modelo de linguagem e síntese de voz, a exemplo da API Gemini ou de oferta equivalente de outro fornecedor.

Cinco a dez minutos bastam para percorrer o fluxo.

A sessão é uma simulação, distinta de uma entrevista real.

Caso as premissas não sejam verdadeiras, haverá os seguintes impactos:

Sem microfone ou rede, o fluxo de voz não é demonstrado.

Se o serviço gratuito não reconhecer a fala a ponto de o diálogo continuar, a sessão-piloto não completa os quatro turnos e a limitação fica registrada no DAS.

Se o fluxo não couber em dez minutos, o critério mensurável do objetivo não se completa.

Se a sessão for conduzida como entrevista real, o ensaio deixa de ser prática de baixa pressão.

Restrições:

O prazo é de 21 dias corridos, em três sprints de sete dias.

O orçamento é nulo: somente camada gratuita e ferramentas sem custo.

A prova de conceito é executada localmente. A publicação em nuvem, na Amazon Web Services (AWS), no Microsoft Azure ou em provedor equivalente, entra somente se o fluxo de voz já estiver concluído e ainda houver tempo na sprint.

Em observância à Lei Geral de Proteção de Dados (LGPD), a aplicação não grava áudio nem transcrição em disco. O áudio da pessoa é descartado ao fim do turno. A transcrição permanece apenas em memória até o encerramento da sessão. Essa descrição é o que o código faz; não é certificação de conformidade. Em camadas gratuitas, o provedor pode usar o conteúdo enviado para melhoria dos próprios produtos, como ocorre na API Gemini (GOOGLE, 2026). Por isso, a sessão-piloto utiliza apenas a voz de quem executa o teste.

Há um único cenário.

A correção ocorre somente ao final da conversa.

A entrega não inclui afirmação de ganho de fluência.

Recursos e requisitos técnicos:

O que segue é uma base de tecnologias para orientar o escopo. A combinação definitiva fica para a sprint, conforme acesso gratuito e tempo de desenvolvimento. A prova de conceito é construída e executada localmente. O DAS pode descrever a mesma solução publicada em nuvem. Essa publicação não é condição para concluir o objetivo.

Interface: aplicação web executada na máquina local, em React, Vue ou Angular.

Orquestração: API desenvolvida no projeto, no padrão Backend for Frontend (BFF) ou equivalente, de modo que a chave de acesso ao modelo permaneça fora do navegador.

Protocolo: requisição e resposta em ambiente local, por HTTP ou protocolo equivalente. A cada turno, o navegador envia o áudio capturado e o histórico da conversa, mantido em memória durante a sessão. A API devolve o texto da entrevistadora e o áudio correspondente.

Modelo e voz: um provedor em camada gratuita reúne reconhecimento de fala, diálogo e síntese, a exemplo da API Gemini ou de oferta equivalente. O reconhecimento converte a fala em texto. O modelo de diálogo recebe a instrução de sistema — papel de entrevistador, sem correção durante a fala — mais o histórico, e devolve a próxima fala. A síntese converte essa fala em áudio. Ao encerrar a sessão, uma segunda chamada ao modelo, com outra instrução, gera os três blocos de feedback.

Nuvem: AWS, Microsoft Azure ou provedor equivalente, citados no DAS como destino possível da interface e da API. O serviço de publicação só é escolhido se houver tempo após o fluxo local.

O desenho previsto é uma orquestração síncrona por turno: reconhecimento, modelo e síntese ocorrem em sequência dentro da mesma requisição. A diagramação do modelo C4, o diagrama de sequência desse turno e o quadro Kanban, em Trello, Planner ou ferramenta equivalente, registram a arquitetura e as sprints. O aluno atua como arquiteto da solução.

Competências e habilidades técnicas:

Interface web em React, Vue ou Angular. API local que isola a chave do modelo. Integração com provedor de reconhecimento, diálogo e síntese. Descrição da publicação em nuvem no DAS. Modelo C4 e diagrama de sequência do turno. Elaboração das instruções de sistema do entrevistador e do feedback. Tratamento de dados de voz.

---

### 1.2.3 Cronograma de Ações Planejadas (Backlog de Produto)

Texto para colar no documento:

O projeto está dividido em três sprints de sete dias corridos, de 2 a 22 de novembro de 2026. As Sprints 1 e 2 foram executadas. Na Sprint 3, a sessão-piloto, a nota de privacidade e o DAS versão 1 foram concluídos em 20 de novembro de 2026. A publicação em nuvem não foi realizada. A prova de conceito permanece local. Essa publicação não é condição para concluir o objetivo.

Cada sprint produz quatro entregas. O quadro Kanban, em Trello, Planner ou ferramenta equivalente, registra o andamento nas colunas Backlog do Projeto, Backlog da Sprint, A Fazer, Em Andamento e Concluído.

Sprint 1 (2 a 8 de novembro de 2026) — Base do fluxo e escolha da tecnologia

O objetivo desta sprint é fechar o que será construído e escolher uma combinação gratuita entre as alternativas do escopo. A sprint seguinte implementa o fluxo, em vez de continuar a pesquisa de ferramentas.

Entregas:

1. Lista de requisitos do fluxo único: cenário de entrevista em tecnologia, captura de voz, resposta oral e feedback em três blocos.

2. Registro da combinação escolhida entre as alternativas do escopo (interface e provedor de reconhecimento, diálogo e síntese), com um teste curto da própria voz.

3. Instruções de sistema do entrevistador e do feedback.

4. Documento de Arquitetura de Software (DAS) parcial, com contexto, premissas e restrições.

Sprint 2 (9 a 15 de novembro de 2026) — Prova de conceito local

O objetivo desta sprint é fazer o fluxo funcionar na máquina local, do cenário ao feedback, sem persistir áudio nem transcrição.

Entregas:

1. Interface local com o cenário de entrevista de emprego em tecnologia.

2. API local do turno: reconhecimento, resposta do modelo e síntese, com histórico apenas em memória.

3. Feedback ao encerrar, em três blocos: pontos positivos, pontos de melhoria e próximo passo.

4. Diagramas de contexto, de contêineres e de sequência do turno, incorporados ao DAS.

Sprint 3 (16 a 22 de novembro de 2026) — Sessão-piloto e fechamento do DAS

O objetivo desta sprint é verificar o critério do objetivo e fechar o documento. A sessão é local e conduzida por quem executa o teste.

Entregas:

1. Registro da sessão-piloto de cinco a dez minutos, com ao menos quatro turnos de fala reconhecidos, resposta oral e feedback em três blocos. Entrega registrada em 20 de novembro de 2026: duração de oito minutos e 22 segundos (21:11:25 a 21:19:47) e quatro turnos com transcrição não vazia. O registro está em `docs/sprint-3/registro-sessao-piloto.md`, no repositório da prova de conceito.

2. Nota de privacidade: áudio e transcrição não permanecem armazenados após o turno. Entrega registrada em 20 de novembro de 2026, em `docs/sprint-3/nota-de-privacidade.md`. A leitura confirma o descarte do áudio da pessoa ao fim do turno. A transcrição não é gravada em disco e permanece na memória da API até o encerramento da sessão. Nenhum código foi alterado. A página de preços do Gemini foi reaberta nessa data: na camada gratuita, os três modelos usados têm “Used to improve our products” como Yes.

3. DAS versão 1, reunindo arquitetura, diagramas, premissas, restrições e o resultado da sessão-piloto. Entrega concluída em 20 de novembro de 2026. O documento descreve a arquitetura como construída. A publicação proposta na AWS está no mesmo documento e não foi implantada. O arquivo está em `deliverables/proposta-de-arquitetura/das-v1-simulador-entrevista.docx`. O parcial do repositório, `docs/sprint-1/das-parcial.md`, permanece na versão 0.2.

4. Publicação em nuvem, somente se as três entregas anteriores estiverem concluídas e ainda houver tempo. Não realizada. A prova de conceito permanece local.

O print do quadro na abertura de cada sprint, as capturas da execução e a retrospectiva de meia a uma lauda entram na área de experimentação, depois que a sprint ocorrer.

---

## 2. Área de Experimentação

Texto completo para colar, com os pontos de inserção das figuras 6 a 13: `deliverables/area-de-experimentacao/capitulo-2.md`.

Síntese: a Sprint 1 fechou requisitos, combinação (React, Python 3.12 BFF, Gemini gratuito), instruções e DAS 0.1. O teste de 10 de novembro de 2026 validou diálogo e síntese; a transcrição veio vazia. A Sprint 2 implementou a tela local, a API do turno, o retorno em três blocos e os diagramas no DAS 0.2. Em 15 de novembro de 2026 o primeiro turno real também devolveu transcrição vazia; a captura não foi repetida. Em 20 de novembro de 2026 a sessão-piloto da Sprint 3 durou oito minutos e 22 segundos, com quatro turnos reconhecidos e retorno em três blocos. No mesmo dia, a nota de privacidade registrou o descarte do áudio da pessoa e a permanência da transcrição em memória até o encerramento, e o DAS versão 1 foi fechado com a arquitetura como construída. A publicação em nuvem não foi realizada.

---

## 3. Considerações Finais

O texto abaixo incorpora a sessão-piloto, a nota de privacidade e o DAS na versão 1, todos de 20 de novembro de 2026. A publicação em nuvem não foi realizada.

### 3.1 Resultados

O resultado do Projeto Aplicado, até 21 de novembro de 2026, é a especificação fundamentada do desafio e da solução, a prova de conceito local e o DAS na versão 1. A tela abre com o cenário único, a API local devolve texto e áudio da entrevistadora, e o encerramento gera os três blocos. Os testes de 10 e de 15 de novembro de 2026 devolveram transcrição vazia. Em 20 de novembro de 2026, a sessão-piloto percorreu o fluxo em oito minutos e 22 segundos, com quatro turnos de transcrição não vazia, resposta oral e retorno em três blocos. A nota de privacidade do mesmo dia confirma que o áudio da pessoa é descartado ao fim do turno e que a transcrição permanece apenas em memória até o encerramento. Na camada gratuita, o provedor pode usar o conteúdo enviado para melhoria dos próprios produtos. O DAS na versão 1 registra a arquitetura como construída e deixa a implantação proposta na AWS identificada como não implantada. O projeto não afirma ganho de fluência, reconhecimento de sotaque brasileiro fora dessa sessão, nem conformidade certificada com a Lei Geral de Proteção de Dados (LGPD).

Pontos positivos do processo: rastreabilidade problema → persona → hipótese → backlog → métricas; recusa de percentuais sem fonte; descarte de artigo retratado.

Dificuldades: ausência de pesquisa primária; evidência de chatbots oriunda de outros países; prazo SMART ainda não confirmado; convenção GUT (soma versus produto) a confirmar com o orientador.

### 3.2 Contribuições

A contribuição atual é um recorte de arquitetura de solução com IA conversacional aplicado a um problema educacional e profissional documentado: prática oral de inglês em entrevista de emprego, com restrições explícitas de ASR, latência, privacidade e qualidade pedagógica do feedback. O trabalho posiciona o protótipo como instrumento de teste, não como produto acabado.

### 3.3 Próximos passos

1. Confirmar com o orientador o prazo (elemento T), a fórmula GUT e se o teste com usuários será executado nesta edição do curso.  
2. A publicação em nuvem não foi executada. A prova de conceito permanece local, e a topologia proposta está no DAS versão 1, identificada como não implantada. Ela não é condição para concluir o objetivo. O prazo da sprint segue até 22 de novembro de 2026.  
3. Se H-01 for suportada, avaliar um segundo cenário (reunião) e a adaptação de nível (F02).  
4. Se H-01 for refutada, redesenhar interação ou tecnologia antes de qualquer expansão.  
5. Pesquisa primária futura: situar qual cenário o público prioriza e se o sotaque brasileiro é reconhecido de forma aceitável.

---

## Referências

BATISTA, Fernanda C. A. English language teaching in Brazil: a gap in policy, problems in practice. **English Language Teaching**, v. 13, n. 8, p. 135-144, 2020. DOI: https://doi.org/10.5539/elt.v13n8p135.

CHEN, Angxuan *et al.* Investigating the effect of role-play activity with GenAI agent on EFL students’ speaking performance. **Journal of Educational Computing Research**, 2024. DOI: https://doi.org/10.1177/07356331241299058.

CORRÊA, Tamires Huguenin. “To be or not to be”? Uma análise da prática da oralidade nas aulas de língua inglesa das escolas públicas do estado de Minas Gerais: realidade ou utopia? **PERcursos Linguísticos**, Vitória, v. 7, n. 14, p. 295-313, 2017. Disponível em: https://periodicos.ufes.br/percursos/article/view/15625. Acesso em: 25 out. 2026.

DEWITT, Dorothy; MOOSAVI, Zeynab. A systematic review of the issues and challenges in developing EFL learners’ speaking skills. **JIIE**, Kuala Lumpur: Universiti Malaya, 2022. Disponível em: https://ejournal.um.edu.my/index.php/JIIE/article/download/41116/15403/101578. Acesso em: 25 out. 2026.

DIRETTRIX. Alunos saem do ensino médio sem inglês adequado para o mercado de trabalho. 9 abr. 2024. Disponível em: https://www.direttrix.com.br/noticias/alunos-saem-do-ensino-medio-sem-ingles-adequado-para-o-mercado-de-trabalho/. Acesso em: 25 out. 2026.

EF EDUCATION FIRST. **EF English Proficiency Index 2025**. Zurique: EF Education First, 2025. Disponível em: https://www.ef.com.br/assetscdn/cefcom-epi-site/reports/2025/ef-epi-2025-brazilian-portuguese.pdf. Acesso em: 25 out. 2026.

ELSA SPEAK. **The world’s best way to improve your English speaking**. 2026. Disponível em: https://elsaspeak.com/en. Acesso em: 25 out. 2026.

FATHI, Jalil; RAHIMI, Masoud; DERAKHSHAN, Ali. Improving EFL learners’ speaking skills and willingness to communicate via artificial intelligence-mediated interactions. **System**, v. 121, 103254, 2024. DOI: https://doi.org/10.1016/j.system.2024.103254.

GOOGLE. **Gemini API**: pricing. 2026. Disponível em: https://ai.google.dev/gemini-api/docs/pricing. Acesso em: 20 nov. 2026.

HELLOTALK. Best English speaking apps in 2026 (tested). 2026. Disponível em: https://www.hellotalk.com/blog/best-english-speaking-apps-2026. Acesso em: 25 out. 2026.

JEON, Jaeho; LEE, Seongyong; CORONEL-MOLINA, Serafín M. Rethinking AI: bias in speech-recognition chatbots for ELT. **ELT Journal**, 2024. DOI: https://doi.org/10.1093/elt/ccae035.

KHAN, Hashim; HUSSAIN, Irfan. Using AI chatbots as speaking partners: benefits, limitations, and learner perceptions. **International Journal of Research and Innovation in Social Science**, v. 10, n. 3, p. 3375-3386, 2026. DOI: https://doi.org/10.47772/IJRISS.2026.100300254.

KOÇ, Fatma Şeyma; SAVAŞ, Perihan. The use of artificially intelligent chatbots in English language learning: a systematic meta-synthesis study of articles published between 2010 and 2024. **ReCALL**, Cambridge University Press, 2024.

MACINTYRE, Peter D. *et al.* Conceptualizing willingness to communicate in a L2: a situational model of L2 confidence and affiliation. **The Modern Language Journal**, v. 82, n. 4, p. 545-562, 1998. DOI: https://doi.org/10.1111/j.1540-4781.1998.tb05543.x.

ÖLMEZER-ÖZTÜRK, Elçin; ÖZTÜRK, Gökhan. Reducing speaking anxiety in EFL classrooms: an explanatory mixed-methods study. **Porta Linguarum**, n. 36, p. 249-261, jun. 2021. DOI: https://doi.org/10.30827/portalin.v0i36.18018.

PORVIR. Alunos saem do ensino médio sem inglês adequado para o mercado de trabalho. 8 abr. 2024. Disponível em: https://porvir.org/ensino-medio-sem-ingles-adequado/. Acesso em: 25 out. 2026.

SERAJ, Prodhan Mahbub Ibna; HABIL, Hadina. A systematic overview of issues for developing EFL learners’ oral English communication skills. **Journal of Language and Education**, v. 7, n. 1, 2021. DOI: https://doi.org/10.17323/jle.2021.10737.

TABUCHI, Kanako *et al.* A case study on reducing language anxiety and enhancing speaking skills through online conversation lessons. **Technology in Language Teaching & Learning**, v. 6, n. 3, 2024. DOI: https://doi.org/10.29140/tltl.v6n3.1497.

TALKPAL. **The fun and effective way to learn a language with AI**. 2026. Disponível em: https://talkpal.ai/. Acesso em: 25 out. 2026.

TYEN, Gladys; CAINES, Andrew; BUTTERY, Paula J. LLM chatbots as a language practice tool: a user study. **Linköping Electronic Conference Proceedings**, 2024. DOI: https://doi.org/10.3384/ecp211018.

VERHELST, Eva; BELPAEME, Tony. Large language models cover for speech recognition mistakes: evaluating conversational AI for second language learners. In: **ACM/IEEE International Conference on Human-Robot Interaction (HRI)**, 2025. DOI: https://doi.org/10.1109/hri61500.2025.10974188.

WANG, Feifei *et al.* Does chatting with chatbots improve language learning performance? A meta-analysis of chatbot-assisted language learning. **Review of Educational Research**, 2024. DOI: https://doi.org/10.3102/00346543241255621.

WIFITALENTS. English speaking practice software: expert picks 2026. 2026. Disponível em: https://wifitalents.com/best/english-speaking-practice-software/. Acesso em: 25 out. 2026.

O artigo de XIAO, Yuehai; ZHANG, Tianyu; HE, Jingyi, sobre chatbots e emoções do aprendiz, foi retratado por *Heliyon* em 2025 e **não** é referência deste relatório.
