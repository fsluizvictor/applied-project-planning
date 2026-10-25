# Relatório de Contexto — Fase 2: Análise de Contexto e Pesquisa

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com Inteligência Artificial (IA)
**Agente responsável:** Context Researcher
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Propósito e Escopo

Este relatório sintetiza evidências externas, reais e verificáveis, sobre o contexto do problema de prática oral em língua inglesa, sobre soluções já existentes no mercado e sobre o que a literatura acadêmica indica a respeito do uso de inteligência artificial (IA) em simuladores de conversação. Nenhuma entrevista, questionário ou observação primária foi realizada nesta fase — essa limitação está declarada na Seção 10.

Conforme a regra `01-academic-integrity.mdc` e o arquivo `.cursor/agents/context-researcher.md`, este documento não cria personas, não define hipóteses com pontuação de risco e não propõe soluções definitivas. Essas atividades permanecem no escopo das Fases 3 e 4.

---

## 2. Premissas Reconhecidas da Fase 1

O Context Researcher leu integralmente `deliverables/phase-1/phase-handoff.md` e `deliverables/phase-1/requirements.md` e reconhece explicitamente as premissas não resolvidas abertas (A-01, A-02, A-04 a A-09), conforme exigido pelo handoff. Em particular:

- **A-07** (obrigatoriedade de pesquisa primária) permanece aberta. Como nenhuma indicação em contrário foi fornecida, esta fase trata a pesquisa primária como **não realizada e não obrigatória por ora**, mas propõe um roteiro de validação (Seção 7) para que a Fase 3 ou uma iteração futura possa executá-la com usuários reais.
- **A-08** (área do conhecimento do curso) permanece aberta. Este relatório não tenta resolvê-la; apenas organiza evidências que, de qualquer forma, seriam relevantes independentemente da área do curso.
- **A-06** (número mínimo de referências bibliográficas) permanece aberta. Esta fase reuniu dezoito fontes externas verificáveis (Seção 9), número considerado razoável na ausência de um mínimo formal exigido pela disciplina.

---

## 3. Contexto do Problema

### 3.1 Barreiras psicológicas, ambientais e linguísticas à produção oral em língua estrangeira

A literatura em ensino de inglês como língua estrangeira (English as a Foreign Language — EFL) converge em um achado central: a maior barreira ao desenvolvimento da fala não é predominantemente linguística, mas psicológica. Uma revisão sistemática de dezenove estudos empíricos publicados entre 2018 e 2022 identificou que os problemas psicológicos — especialmente ansiedade, medo de cometer erros, falta de motivação e baixa autoconfiança — foram apontados como barreira mais frequente à fala entre aprendizes de EFL, seguidos por problemas ambientais (temas de conversação, métodos de ensino, falta de prática) e linguísticos (vocabulário, pronúncia, gramática) [FONTE-SECUNDÁRIA] (DEWITT; MOOSAVI, 2022).

De forma convergente, outra revisão sistemática da literatura aponta a ansiedade e a timidez como fatores centrais, resultantes sobretudo da falta de prática dentro e fora da sala de aula, de vocabulário insuficiente e do medo de crítica [FONTE-SECUNDÁRIA] (SERAJ; HABIL, 2021). Estudos experimentais mostram que intervenções de baixa pressão — aulas de conversação individuais on-line, apresentações com retroalimentação (*feedback*) escalonada e trocas de tipo *eTandem* — reduzem a ansiedade de fala e melhoram o desempenho oral, com uma intervenção de catorze semanas registrando redução de aproximadamente 30% na ansiedade de fala em língua estrangeira (Foreign Language Speaking Anxiety Scale — FLSAS) [FONTE-SECUNDÁRIA] (ÖLMEZER-ÖZTÜRK; ÖZTÜRK, 2021); resultado semelhante foi observado em um estudo de caso com aulas de conversação on-line individualizadas [FONTE-SECUNDÁRIA] (TABUCHI et al., 2024).

Um arcabouço teórico relevante para compreender por que alguns aprendizes evitam falar, mesmo quando possuem competência linguística suficiente, é o modelo de **disposição para comunicar** (*Willingness to Communicate* — WTC), que descreve a decisão de iniciar comunicação em uma segunda língua como um processo volitivo, influenciado por autoconfiança situacional, ansiedade e oportunidade [FONTE-SECUNDÁRIA] (MACINTYRE et al., 1998). Este modelo é citado nesta fase como referencial teórico, não como evidência empírica sobre o público-alvo deste projeto — distinção importante, já que nenhuma pesquisa primária com usuários reais foi conduzida.

### 3.2 O Contexto Brasileiro

Especificamente no Brasil, o índice *EF English Proficiency Index* (EF EPI) 2025, calculado a partir de mais de dois milhões de participantes do teste EF SET em 2024, posiciona o Brasil na septuagésima quinta colocação global, com pontuação geral de 482 (pontuação média global: 488). Entre as quatro habilidades avaliadas, a fala obteve a menor pontuação relativa entre as habilidades produtivas e receptivas mais fracas do país: leitura 516, compreensão auditiva 468, fala 464 e escrita 442. O próprio relatório destaca que a fala é a habilidade mais fraca na maioria dos países avaliados, raramente priorizada pelos sistemas escolares devido à dificuldade de avaliação individual em larga escala [FONTE-SECUNDÁRIA] (EF EDUCATION FIRST, 2025).

Pesquisas acadêmicas sobre o ensino de inglês nas escolas públicas brasileiras corroboram esse padrão a partir de dados de campo. Um estudo com estudantes de Letras da Universidade Federal de Juiz de Fora e com alunos do ensino médio/técnico do Centro Federal de Educação Tecnológica de Minas Gerais (CEFET/MG) constatou que, entre os respondentes do primeiro ano, apenas 34% já haviam tido algum professor que usasse o inglês com frequência em sala e 70% nunca haviam realizado prova oral na escola [FONTE-SECUNDÁRIA] (CORRÊA, 2017). Em análise de política educacional, outro estudo aponta que, apesar de o inglês ser disciplina obrigatória do quinto ao décimo segundo ano da educação básica, estima-se que apenas 3% da população brasileira fale o idioma, fenômeno atribuído em parte a lacunas nos documentos de política curricular, que não especificam as condições necessárias para um ensino efetivo e acabam favorecendo a leitura em detrimento da produção oral, entre outros fatores como turmas numerosas e recursos escassos [FONTE-SECUNDÁRIA] (BATISTA, 2020).

Uma pesquisa de mercado conduzida pela empresa multinacional de educação Pearson em 2024, com mil respondentes em cada um de cinco países (Arábia Saudita, Brasil, Estados Unidos, Itália e Japão), relatada por veículos jornalísticos especializados em educação, indica que 85% dos respondentes consideram o inglês vital para o sucesso profissional, mas 54% afirmam que a educação formal não os capacitou adequadamente; apenas 25% se sentem confiantes nas quatro habilidades linguísticas, sendo fala e escrita as mais deficientes. Quanto à prática oral especificamente, 46% dos respondentes relataram não ter tido oportunidades suficientes de treino de conversação em sala de aula e 50% afirmaram não ter encontrado ambientes para praticar fora da escola [FONTE-SECUNDÁRIA] (DIRETTRIX, 2024; PORVIR, 2024). Esta fase **não teve acesso ao relatório primário da Pearson**, apenas a reportagens jornalísticas que o descrevem; portanto, a metodologia completa (margem de erro, critérios de amostragem) não pôde ser verificada de forma independente. Esta limitação está sinalizada como `[LACUNA DE EVIDÊNCIA — relatório primário da pesquisa Pearson não acessado diretamente]`.

### 3.3 Manifestação do Problema em Diferentes Situações Práticas

O brief inicial do projeto (`phases/02_contexto_problema.md`) solicita que o problema seja investigado em situações práticas distintas — viagens, entrevistas de emprego, estudo e trabalho, interações cotidianas —, sem presumir que todas pertençam ao mesmo público. As evidências reunidas nesta fase permitem as seguintes observações, cada uma claramente delimitada quanto ao tipo de situação a que se refere:

| Situação | O que a evidência mostra | Tipo de evidência |
|---|---|---|
| Entrevistas de emprego / mercado de trabalho | Ferramentas comerciais já oferecem módulos específicos de "Interview Coach" e "Workplace Coach", indicando demanda de mercado percebida por fornecedores de produtos de IA para esse cenário específico [FONTE-SECUNDÁRIA] (ELSA SPEAK, 2026). A pesquisa Pearson (2024) relaciona proficiência em inglês a vantagem profissional percebida (85% dos respondentes) | [FONTE-SECUNDÁRIA] |
| Estudo formal (escola/curso de idiomas) | A maior parte da evidência acadêmica reunida refere-se a este contexto: sala de aula de EFL, cursos universitários e programas de verão (Seções 3.1 e 3.2) | [FONTE-SECUNDÁRIA] |
| Trabalho / reuniões / apresentações | Produtos comerciais (ELSA Speak) incluem módulos de "Meeting Coach" e "Presentation Coach"; a pesquisa Pearson também associa o domínio do inglês a competitividade profissional frente à tecnologia (40% dos respondentes) | [FONTE-SECUNDÁRIA] |
| Viagens | **Nenhuma fonte acadêmica ou de mercado específica sobre viagens foi localizada nesta fase.** | `[LACUNA DE EVIDÊNCIA — prática oral em contexto de viagem]` |
| Interações cotidianas informais | A literatura sobre WTC (MACINTYRE et al., 1998) é o referencial teórico mais próximo, mas trata de disposição para comunicar de forma geral, não de cenários cotidianos específicos | [FONTE-SECUNDÁRIA] (referencial teórico) |

> `[ASSUMPTION — requires validation]`: Não há evidência nesta fase de que um único público-alvo enfrente simultaneamente todos os cenários acima. O requirements.md (Fase 1) já assume um "público-alvo inicial: pessoas que precisam do inglês em situações práticas" de forma genérica; esta fase não encontrou dados que confirmem ou refutem qual situação é prioritária para esse público. Esta é uma pergunta central para a pesquisa de validação proposta na Seção 7.

---

## 4. Soluções Existentes

Diversas ferramentas comerciais já oferecem prática de conversação em inglês assistida por IA ou por humanos. O quadro abaixo resume as soluções identificadas, com base em páginas oficiais de produto e comparativos especializados — fontes secundárias de natureza comercial, não acadêmica, cujas afirmações de eficácia não foram verificadas de forma independente por esta fase:

| Ferramenta | Modalidade principal | Característica distintiva | Limitação relatada |
|---|---|---|---|
| ELSA Speak | IA + reconhecimento de fala | Análise fonética detalhada; módulos para entrevistas, reuniões e apresentações | Foco em pronúncia; menos robusta como ferramenta de conversação aberta [FONTE-SECUNDÁRIA] (HELLOTALK, 2026) |
| Speak | IA conversacional | Conversação simulada com retroalimentação de fala | Sem camada gratuita relevante; previsibilidade das respostas de IA [FONTE-SECUNDÁRIA] (HELLOTALK, 2026) |
| Talkpal | IA conversacional multilíngue | Chat, chamadas e simulações de papéis (*role-play*) em mais de 130 idiomas | Análise de pronúncia mais limitada que concorrentes especializados [FONTE-SECUNDÁRIA] (TALKPAL, 2026) |
| Cambly | Tutoria humana ao vivo | Conversação sob demanda com falantes nativos, sem agendamento | Custo elevado para uso diário; variação na qualificação dos tutores [FONTE-SECUNDÁRIA] (WIFITALENTS, 2026) |

Nenhuma das fontes de mercado consultadas publica dados de eficácia pedagógica auditados de forma independente; suas afirmações de "resultados comprovados" são material promocional e não foram tratadas como evidência científica nesta síntese. A literatura acadêmica revisada na Seção 5 é a base usada para avaliar a eficácia real de abordagens baseadas em IA.

---

## 5. Papel da IA em Simuladores de Conversação: Eficácia e Limitações

### 5.1 Evidências de eficácia

Uma meta-análise de setenta tamanhos de efeito extraídos de vinte e oito estudos encontrou efeito geral positivo do uso de chatbots sobre o desempenho em aprendizagem de idiomas (g = 0,484) em comparação a condições sem chatbot, com a eficácia variando conforme nível educacional, nível de proficiência do aprendiz, design de interface e capacidade de interação do sistema [FONTE-SECUNDÁRIA] (WANG et al., 2024).

Estudos experimentais específicos sobre fala corroboram esse padrão com achados mais granulares:

- Um experimento controlado com sessenta e cinco aprendizes de EFL (33 no grupo de IA, 32 no grupo de controle com interação face a face) encontrou melhoria significativamente maior em fluência, coerência, léxico, precisão gramatical, pronúncia e disposição para comunicar (WTC) no grupo que usou um chatbot de IA, em comparação ao grupo de interação convencional entre pares [FONTE-SECUNDÁRIA] (FATHI; RAHIMI; DERAKHSHAN, 2024).
- Um estudo com oitenta e cinco aprendizes do ensino fundamental, em interações individuais e em pares com um chatbot generativo durante um programa de verão de três semanas, encontrou desempenho de fala pós-teste significativamente superior ao de um grupo de controle com instrução convencional, sem diferença significativa entre as condições individual e em pares [FONTE-SECUNDÁRIA] (TAI; CHEN, 2024).
- Um estudo com agente de IA generativa em atividades de simulação de papéis (*role-play*) com cinquenta e três estudantes universitários chineses, por outro lado, **não** encontrou vantagem significativa do grupo experimental sobre o grupo de controle com interação humana, indicando que os resultados de eficácia não são uniformes entre contextos [FONTE-SECUNDÁRIA] (CHEN et al., 2024).
- Um estudo de usuário com cento e sessenta aprendizes de inglês interagindo com um chatbot baseado em modelo de linguagem de grande escala (*Large Language Model* — LLM) encontrou aumento de autoconfiança percebida para conversas reais já após uma única sessão (mais da metade dos participantes), mas achados de aprendizagem mensurável limitados no curto prazo, com participantes prevendo benefícios maiores caso tivessem mais oportunidades de uso [FONTE-SECUNDÁRIA] (TYEN; CAINES; BUTTERY, 2024).

### 5.2 Limitações e riscos documentados

A literatura também documenta limitações técnicas e pedagógicas relevantes para o desenho de qualquer simulador de conversação com IA:

- **Reconhecimento de fala não nativa**: sistemas de reconhecimento automático de fala (*Automatic Speech Recognition* — ASR) têm desempenho degradado para falantes não nativos e para aprendizes de proficiência limitada; um estudo mediu taxa de erro de palavras (*word-error rate*) de 32,8% para fala em francês como segunda língua, embora modelos de linguagem de grande escala tenham demonstrado capacidade de compensar parcialmente esses erros ao manter a coerência conversacional [FONTE-SECUNDÁRIA] (VERHELST; BELPAEME, 2025).
- **Viés sociolinguístico**: sistemas de reconhecimento de fala são treinados majoritariamente em dados de falantes nativos, o que gera "viés preditivo" contra variedades não nativas do inglês; isso pode pressionar aprendizes a tentar imitar parâmetros estreitos de pronúncia "padrão", em contradição com tendências atuais de valorização de variedades diversas do inglês no ensino [FONTE-SECUNDÁRIA] (JEON; LEE; CORONEL-MOLINA, 2024).
- **Coerência conversacional limitada e falta de retroalimentação corretiva explícita**: uma meta-síntese sistemática de estudos publicados entre 2010 e 2024 identificou como problemas mais frequentemente relatados a baixa inteligibilidade de enunciados do aprendiz (por falhas de reconhecimento de fala), o caráter pouco natural da interação humano-chatbot e a ausência de retroalimentação corretiva explícita; alguns estudos analisados relataram aumento de ansiedade após interação com chatbots, atribuído ao contexto educacional avaliativo e à falta de empatia e raciocínio complexo dos sistemas [FONTE-SECUNDÁRIA] (KOÇ; SAVAŞ, 2024).
- **Limitações técnicas e pedagógicas consolidadas**: uma revisão sistemática de trinta estudos empíricos (2018–2025) sintetiza esses riscos — erros de reconhecimento de fala sensíveis a sotaque, manutenção limitada de contexto e de competência pragmática ao longo de diálogos extensos, qualidade variável de retroalimentação, desalinhamento curricular e despreparo docente para integrar a ferramenta — e recomenda que chatbots sejam usados como prática suplementar e supervisionada, não como substituto da interação humana [FONTE-SECUNDÁRIA] (KHAN; HUSSAIN, 2026).

> **Síntese integradora**: a literatura converge para a conclusão de que a IA conversacional pode aumentar a quantidade de prática disponível e reduzir a ansiedade inicial de falar, mas não substitui integralmente a interação humana, especialmente quanto à retroalimentação pedagógica corretiva, à competência pragmática e à equidade no reconhecimento de diferentes variedades de pronúncia. Isso é relevante para o desenho da solução deste projeto: qualquer simulador de conversação proposto nas Fases 5 e 6 deve tratar essas limitações como restrições de design, não como detalhes menores.

> **Nota de integridade acadêmica**: durante a pesquisa, foi localizado um artigo revisado por pares sobre emoções do aprendiz e chatbots de IA (XIAO; ZHANG; HE, *Heliyon*) que **foi formalmente retratado** pelo periódico (retratação publicada em 27 de janeiro de 2025). Em conformidade com a regra `01-academic-integrity.mdc`, esse artigo **não foi utilizado como evidência** neste relatório e é mencionado aqui apenas para registrar que a pesquisa o identificou e o descartou deliberadamente.

---

## 6. Lacunas Identificadas (Onde Soluções Existentes Falham ou Há Oportunidade)

Com base nas Seções 4 e 5, as seguintes lacunas foram identificadas nas soluções existentes, estritamente a partir da evidência reunida:

1. Ferramentas especializadas em pronúncia (ex.: ELSA Speak) e ferramentas de conversação aberta (ex.: Speak, Talkpal) tendem a ser oferecidas de forma separada; a literatura (Seção 5.2) sugere que a combinação de retroalimentação fonética com conversação contextualizada e prática supervisionada é pouco explorada nas soluções comerciais revisadas [FONTE-SECUNDÁRIA].
2. Todas as ferramentas de IA revisadas carregam as limitações documentadas na Seção 5.2 (viés de reconhecimento de fala não nativa, falta de retroalimentação corretiva robusta); nenhuma fonte consultada indica que algum produto comercial tenha resolvido esses problemas de forma comprovada e auditada de modo independente.
3. `[LACUNA DE EVIDÊNCIA]`: não foi localizada nesta fase nenhuma fonte, acadêmica ou de mercado, que avalie especificamente o uso de simuladores de IA para o cenário de **viagem**.
4. `[LACUNA DE EVIDÊNCIA]`: não foi localizada evidência brasileira (nacional) específica sobre o uso de simuladores de conversação com IA — toda a evidência sobre eficácia de chatbots (Seção 5.1) é de outros contextos nacionais (China, Irã, Reino Unido/Cambridge, etc.); a aplicabilidade ao público brasileiro é, portanto, uma inferência, não um achado direto.
5. `[LACUNA DE EVIDÊNCIA]`: não há, nas fontes consultadas, comparação direta de custo-benefício entre tutoria humana sob demanda (Cambly) e simuladores de IA para o público e orçamento relevantes a este projeto.

---

## 7. Perguntas de Pesquisa e Roteiro de Validação

Em atendimento à tarefa 6 do brief da Fase 2 (`phases/02_contexto_problema.md`), esta seção define perguntas de pesquisa e um roteiro curto de entrevista para validar o problema com usuários reais. **Nenhuma dessas perguntas foi aplicada nesta fase** — nenhuma entrevista foi conduzida, e nenhum dado de resposta é apresentado em lugar algum deste relatório.

### 7.1 Perguntas de pesquisa

1. Em quais situações específicas (estudo, trabalho, entrevistas, viagem, interações cotidianas) o público-alvo relata maior necessidade e maior dificuldade de produção oral em inglês?
2. O que impede, na prática, que esse público pratique conversação com a frequência que julga necessária (falta de parceiros de conversação, custo, horário, vergonha, ansiedade, outro)?
3. Que experiências prévias esse público teve com ferramentas de IA para prática de idiomas (se alguma) e o que funcionou ou não funcionou?
4. Que tipo de retroalimentação (corretiva, de pronúncia, de fluência) esse público considera mais valiosa ao praticar conversação?
5. Esse público prefere, confia ou se sente mais confortável praticando com um sistema de IA, com um humano, ou com uma combinação dos dois — e por quê?

### 7.2 Roteiro curto de entrevista (sugestão para validação futura)

> Este roteiro é uma proposta para uso em uma eventual pesquisa primária futura (Fase 3 ou posterior), não um instrumento já aplicado.

1. "Em que situações do seu dia a dia, trabalho ou estudo você precisa ou gostaria de falar inglês?"
2. "Com que frequência você pratica conversação em inglês atualmente? Com quem ou o quê?"
3. "O que mais dificulta essa prática para você hoje?"
4. "Você já usou algum aplicativo ou ferramenta de IA para praticar inglês falado? Como foi a experiência?"
5. "O que faria você se sentir mais confiante para falar inglês em uma situação real?"
6. "Se existisse uma ferramenta ideal para isso, o que ela precisaria ter — e o que ela definitivamente não deveria fazer?"

---

## 8. Desafio Preliminar Centrado no Usuário

Em atendimento à tarefa 7 do brief da Fase 2, apresenta-se abaixo uma formulação **preliminar** de desafio, construída estritamente a partir da evidência reunida nesta fase. Esta formulação **não constitui a definição final do problema** — essa definição formal, incluindo *insights*, declarações "Como Podemos..." (*How Might We* — HMW) e hipóteses com classificação de risco, é escopo da Fase 4 (Problem Framing), conforme `PLAN.md`.

> **Desafio preliminar**: Como permitir que pessoas que precisam usar o inglês em situações práticas do cotidiano pessoal ou profissional pratiquem a produção oral com a frequência e o apoio necessários para reduzir a ansiedade de fala e aumentar sua disposição para comunicar, dado que a literatura indica que a principal barreira é a falta de oportunidades de prática de baixa pressão, e não exclusivamente a falta de conhecimento linguístico?

Esta formulação evita presumir a IA como solução exclusiva: a literatura revisada (Seção 3.1) mostra que intervenções de baixa pressão sem IA — aulas on-line individuais, *eTandem*, sessões com retroalimentação escalonada — também reduzem ansiedade e aumentam prática. A IA é uma via possível entre outras, e sua inclusão como solução deve ser justificada, não assumida, nas Fases 4 a 6.

---

## 9. Área do Conhecimento do Curso

Conforme reconhecido na Seção 2, a premissa **A-08** (área do conhecimento do curso) permanece aberta e não é resolvida nesta fase — sua resolução depende de informação a ser fornecida pelo usuário, conforme já registrado em `requirements.md`. Esta pesquisa de contexto foi conduzida de forma a ser relevante independentemente da área curricular declarada (Design Thinking, tecnologia da informação ou inovação/empreendedorismo), já que trata de evidência sobre o problema do usuário, não sobre uma tecnologia ou metodologia específica de curso.

---

## 10. Referências Bibliográficas (ABNT NBR 6023)

BATISTA, Fernanda C. A. English language teaching in Brazil: a gap in policy, problems in practice. **English Language Teaching**, v. 13, n. 8, p. 135-144, 2020. DOI: https://doi.org/10.5539/elt.v13n8p135.

CHEN, Angxuan et al. Investigating the effect of role-play activity with GenAI agent on EFL students' speaking performance. **Journal of Educational Computing Research**, 2024. DOI: https://doi.org/10.1177/07356331241299058.

CORRÊA, Tamires Huguenin. "To be or not to be"? Uma análise da prática da oralidade nas aulas de língua inglesa das escolas públicas do estado de Minas Gerais: realidade ou utopia? **PERcursos Linguísticos**, Vitória, v. 7, n. 14, p. 295-313, 2017. Disponível em: https://periodicos.ufes.br/percursos/article/view/15625. Acesso em: 25 out. 2026.

DEWITT, Dorothy; MOOSAVI, Zeynab. A systematic review of the issues and challenges in developing EFL learners' speaking skills. **JIIE**, Kuala Lumpur: Universiti Malaya, 2022. Disponível em: https://ejournal.um.edu.my/index.php/JIIE/article/download/41116/15403/101578. Acesso em: 25 out. 2026.

DIRETTRIX. Alunos saem do ensino médio sem inglês adequado para o mercado de trabalho. 9 abr. 2024. Disponível em: https://www.direttrix.com.br/noticias/alunos-saem-do-ensino-medio-sem-ingles-adequado-para-o-mercado-de-trabalho/. Acesso em: 25 out. 2026.

EF EDUCATION FIRST. **EF English Proficiency Index 2025**. Zurique: EF Education First, 2025. Disponível em: https://www.ef.com.br/assetscdn/cefcom-epi-site/reports/2025/ef-epi-2025-brazilian-portuguese.pdf. Acesso em: 25 out. 2026.

ELSA SPEAK. **The world's best way to improve your English speaking**. 2026. Disponível em: https://elsaspeak.com/en. Acesso em: 25 out. 2026.

FATHI, Jalil; RAHIMI, Masoud; DERAKHSHAN, Ali. Improving EFL learners' speaking skills and willingness to communicate via artificial intelligence-mediated interactions. **System**, v. 121, 103254, 2024. DOI: https://doi.org/10.1016/j.system.2024.103254.

HELLOTALK. Best English speaking apps in 2026 (tested). 2026. Disponível em: https://www.hellotalk.com/blog/best-english-speaking-apps-2026. Acesso em: 25 out. 2026.

JEON, Jaeho; LEE, Seongyong; CORONEL-MOLINA, Serafín M. Rethinking AI: bias in speech-recognition chatbots for ELT. **ELT Journal**, 2024. DOI: https://doi.org/10.1093/elt/ccae035.

KHAN, Hashim; HUSSAIN, Irfan. Using AI chatbots as speaking partners: benefits, limitations, and learner perceptions. **International Journal of Research and Innovation in Social Science**, v. 10, n. 3, p. 3375-3386, 2026. DOI: https://doi.org/10.47772/IJRISS.2026.100300254.

KOÇ, Fatma Şeyma; SAVAŞ, Perihan. The use of artificially intelligent chatbots in English language learning: a systematic meta-synthesis study of articles published between 2010 and 2024. **ReCALL**, Cambridge University Press, 2024.

MACINTYRE, Peter D. et al. Conceptualizing willingness to communicate in a L2: a situational model of L2 confidence and affiliation. **The Modern Language Journal**, v. 82, n. 4, p. 545-562, 1998. DOI: https://doi.org/10.1111/j.1540-4781.1998.tb05543.x.

ÖLMEZER-ÖZTÜRK, Elçin; ÖZTÜRK, Gökhan. Reducing speaking anxiety in EFL classrooms: an explanatory mixed-methods study. **Porta Linguarum**, n. 36, p. 249-261, jun. 2021. DOI: https://doi.org/10.30827/portalin.v0i36.18018.

PORVIR. Alunos saem do ensino médio sem inglês adequado para o mercado de trabalho. 8 abr. 2024. Disponível em: https://porvir.org/ensino-medio-sem-ingles-adequado/. Acesso em: 25 out. 2026.

SERAJ, Prodhan Mahbub Ibna; HABIL, Hadina. A systematic overview of issues for developing EFL learners' oral English communication skills. **Journal of Language and Education**, v. 7, n. 1, 2021. DOI: https://doi.org/10.17323/jle.2021.10737.

TABUCHI, Kanako et al. A case study on reducing language anxiety and enhancing speaking skills through online conversation lessons. **Technology in Language Teaching & Learning**, v. 6, n. 3, 2024. DOI: https://doi.org/10.29140/tltl.v6n3.1497.

TAI, Tzu-Yu; CHEN, Howard Hao-Jan. Improving elementary EFL speaking skills with generative AI chatbots: exploring individual and paired interactions. **Computers & Education**, v. 220, 105112, 2024. DOI: https://doi.org/10.1016/j.compedu.2024.105112.

TALKPAL. **The fun and effective way to learn a language with AI**. 2026. Disponível em: https://talkpal.ai/. Acesso em: 25 out. 2026.

TYEN, Gladys; CAINES, Andrew; BUTTERY, Paula J. LLM chatbots as a language practice tool: a user study. **Linköping Electronic Conference Proceedings**, 2024. DOI: https://doi.org/10.3384/ecp211018.

VERHELST, Eva; BELPAEME, Tony. Large language models cover for speech recognition mistakes: evaluating conversational AI for second language learners. In: **ACM/IEEE International Conference on Human-Robot Interaction (HRI)**, 2025. DOI: https://doi.org/10.1109/hri61500.2025.10974188.

WANG, Feifei et al. Does chatting with chatbots improve language learning performance? A meta-analysis of chatbot-assisted language learning. **Review of Educational Research**, 2024. DOI: https://doi.org/10.3102/00346543241255621.

WIFITALENTS. English speaking practice software: expert picks 2026. 2026. Disponível em: https://wifitalents.com/best/english-speaking-practice-software/. Acesso em: 25 out. 2026.

> Nota de integridade acadêmica: o artigo de XIAO, Yuehai; ZHANG, Tianyu; HE, Jingyi ("The promises and challenges of AI-based chatbots in language education through the lens of learner emotions") foi localizado durante a pesquisa, porém **foi retratado** pelo periódico (ver retratação em *Heliyon*, 2025) e **não consta** como referência válida deste relatório, em conformidade com a regra `01-academic-integrity.mdc`.

---

## 11. Premissas Não Resolvidas e Lacunas de Evidência (Consolidado)

| # | Item | Tipo | Impacto | Fase de resolução sugerida |
|---|------|------|---------|----------------------------|
| B-01 | Não há evidência sobre qual situação prática (viagem, entrevista, estudo, trabalho, cotidiano) é prioritária para o público-alvo real deste projeto | `[ASSUMPTION — requires validation]` | Afeta definição de persona e escopo da solução | Fase 3 (pesquisa com usuários, se realizada) ou Fase 4 |
| B-02 | Relatório primário da pesquisa Pearson (2024) não foi acessado diretamente; apenas reportagens que o descrevem | `[LACUNA DE EVIDÊNCIA]` | Impede verificação independente de metodologia e margem de erro | Pode ser resolvida obtendo o relatório original junto à Pearson, se necessário |
| B-03 | Nenhuma fonte sobre uso de IA conversacional especificamente em contexto de viagem | `[LACUNA DE EVIDÊNCIA]` | Limita afirmações sobre esse cenário específico | Pesquisa adicional direcionada, se o cenário de viagem for priorizado |
| B-04 | Toda a evidência de eficácia de chatbots de IA (Seção 5.1) vem de contextos nacionais distintos do brasileiro | `[LACUNA DE EVIDÊNCIA]` | Generalização para o público brasileiro é inferência, não achado direto | Fase 4 deve tratar como suposição a ser testada, não como fato estabelecido |
| B-05 | Nenhuma pesquisa primária (entrevista, questionário, observação) foi conduzida nesta fase | Limitação declarada | Toda validação de problema com usuários reais permanece pendente | Roteiro proposto na Seção 7; execução depende de decisão humana sobre obrigatoriedade (A-07) |
| B-06 | Afirmações de eficácia das ferramentas comerciais (Seção 4) não foram verificadas de forma independente — são material de marketing dos próprios fornecedores | `[DADO-NÃO-VERIFICADO]` | Essas ferramentas devem ser tratadas como referência de mercado, não como evidência científica de eficácia | Não bloqueia fases futuras, desde que a distinção seja mantida |

---

## 12. Limitações Desta Pesquisa (Honestidade de Processo)

- Esta pesquisa foi conduzida inteiramente por meio de busca na internet (ferramenta de busca disponível na sessão), sem acesso a bases de dados acadêmicas pagas (ex.: Scopus, Web of Science) além do que está indexado publicamente. Não é possível garantir que esta seja a cobertura mais completa da literatura disponível sobre o tema.
- Nem todos os artigos citados foram lidos em sua versão de texto completo com acesso irrestrito; alguns foram acessados por meio de resumos, páginas de editora ou repositórios de metadados (ex.: OUCI, ScienceOpen). Nesses casos, a citação reflete apenas o que foi efetivamente verificado, não o conteúdo integral do artigo.
- A pesquisa priorizou fontes em inglês e português; não foram buscadas fontes em outros idiomas.
- Esta fase não tem meios determinísticos de garantir que o humano revisor concorde com a classificação de evidência atribuída a cada fonte; a classificação (`[FONTE-SECUNDÁRIA]`, `[DADO-NÃO-VERIFICADO]`, `[ASSUMPTION]`, `[LACUNA DE EVIDÊNCIA]`) é um julgamento do agente, sujeito a revisão humana, conforme a limitação de aplicação já reconhecida na regra `01-academic-integrity.mdc`.
