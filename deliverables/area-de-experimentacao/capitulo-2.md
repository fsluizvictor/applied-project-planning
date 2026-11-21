# Instruções de colagem (apagar antes de entregar)

Colar no capítulo 2 do template XP/IGTI, na seção “Área de Experimentação”. Inserir as figuras nos pontos indicados. Os arquivos estão neste diretório e em `deliverables/cronograma-sprints/`.

Não colar chave de API, arquivos `.wav` nem transcrição inventada. As entregas 1, 2 e 3 da Sprint 3 estão registradas. A publicação em nuvem não foi realizada: não inventá-la.

---

## 2. Área de Experimentação

A área de experimentação registra o planejamento, a execução e o resultado das sprints da prova de conceito. O quadro Kanban previsto no escopo foi materializado nas issues do repositório GitHub do artefato (`poc-en-simulator`), uma issue por entrega, com as etiquetas `sprint-1` e `sprint-2`. As Sprints 1 e 2 foram executadas. Na Sprint 3, as entregas 1, 2 e 3 (sessão-piloto, nota de privacidade e DAS na versão 1) foram concluídas em 20 de novembro de 2026. A publicação em nuvem não foi realizada. A prova de conceito permanece local.

---

### 2.1 Sprint 1 — Base do fluxo e escolha da tecnologia

Período: 2 a 8 de novembro de 2026. As entregas foram registradas em 10 de novembro de 2026. O objetivo desta sprint foi fechar o que seria construído e escolher uma combinação gratuita entre as alternativas do escopo, de modo que a sprint seguinte implementasse o fluxo em vez de continuar a pesquisa de ferramentas.

#### 2.1.1 Solução

**Evidência do planejamento**

A Sprint 1 foi planejada com quatro entregas, correspondentes às issues 1 a 4 do repositório. A figura 6 reproduz o cartão de planejamento da sprint.

**Figura 6 — Definição da Sprint 1**

*(inserir `deliverables/cronograma-sprints/sprint-1.png`)*

Issues de planejamento: [issue 1](https://github.com/fsluizvictor/poc-en-simulator/issues/1), [issue 2](https://github.com/fsluizvictor/poc-en-simulator/issues/2), [issue 3](https://github.com/fsluizvictor/poc-en-simulator/issues/3) e [issue 4](https://github.com/fsluizvictor/poc-en-simulator/issues/4). *(Opcional: inserir captura da lista de issues com a etiqueta `sprint-1`.)*

**Evidência da execução de cada requisito**

1. **Lista de requisitos do fluxo único**

Redigiu-se o fluxo único da prova de conceito: um cenário de entrevista de emprego na área de tecnologia, captura de voz, resposta oral da entrevistadora e retorno ao encerrar, em três blocos. O documento fecha oito requisitos funcionais (RF-01 a RF-08) e seis restrições (RNF-01 a RNF-06). Ficaram fora do fluxo a medição de fluência, a correção durante a conversa, o cadastro, o banco de dados, o canal bidirecional contínuo e a publicação em nuvem como condição de conclusão.

Arquivo: `docs/sprint-1/requisitos-do-fluxo.md`.

2. **Registro da combinação tecnológica, com teste curto da própria voz**

Entre as alternativas do escopo, registrou-se a combinação: interface em React, na máquina local; API em Python 3.12, no padrão *Backend for Frontend* (BFF); reconhecimento `gemini-3.5-transcribe` em modo `VERBATIM`; diálogo e retorno `gemini-3.5-flash-lite`; síntese `gemini-3.8-flash-lite-tts`, voz `Kore`. Afastaram-se a *Live API*, o modo `SMART` de transcrição e a variante de síntese de estúdio.

Em 10 de novembro de 2026 a chave foi usada só no ambiente do processo. O que a chave aceitou: o modelo de diálogo gerou a abertura da entrevistadora; a síntese gerou WAV reproduzível pela chamada REST `generateContent`; o reconhecimento aceitou o áudio e, sem fala inteligível, devolveu candidato vazio. O que falhou, e ficou registrado de propósito: a interface `interactions` não encontrou o modelo de síntese; o SDK `google-genai` 3.1.0 montou `speechConfig` de um jeito que a API recusou; a captura de oito segundos não continha uma resposta falada.

Arquivos: `docs/sprint-1/combinacao-tecnologica.md` e `docs/sprint-1/resultado-teste-voz.md`.

3. **Instruções de sistema do entrevistador e do feedback**

Escreveram-se duas instruções distintas. A da entrevistadora, em inglês, impede correção, nota ou comentário pedagógico no meio do turno. A do retorno, em português brasileiro, pede somente três blocos e manda declarar amostra insuficiente quando a transcrição for curta ou ininteligível. O modelo de transcrição não recebe essas instruções.

Arquivos: `prompts/entrevistador.txt`, `prompts/feedback.txt` e `docs/sprint-1/instrucoes-de-sistema.md`.

4. **Documento de Arquitetura de Software (DAS) parcial**

Redigiu-se a versão 0.1 do DAS, com contexto, contêineres previstos em texto, premissas, restrições e decisões. Os diagramas de contexto, de contêineres e de sequência ficaram para a Sprint 2. A versão não afirma que o fluxo já funcionava.

Arquivo: `docs/sprint-1/das-parcial.md` (versão 0.1, anterior à atualização da Sprint 2).

**Evidência dos resultados**

1. **Lista de requisitos**

O fluxo único ficou fechado. Requisitos funcionais: RF-01 (cenário único), RF-02 (captura pelo microfone), RF-03 (transcrição suficiente para o diálogo continuar), RF-04 (fala da entrevistadora sem correção), RF-05 (síntese e reprodução), RF-06 (retorno em três blocos), RF-07 (histórico só em memória) e RF-08 (chave fora do navegador).

2. **Combinação tecnológica**

A combinação da Sprint 2 ficou escolhida. O teste curto validou diálogo e síntese. A transcrição veio vazia: o microfone não captou uma frase falada. Esse teste **não** é evidência de reconhecimento de sotaque brasileiro.

Abertura gerada: “Hi there, welcome! Could you please introduce yourself and tell me a bit about your background in software development?”

Transcrição da resposta: [vazia].

3. **Instruções de sistema**

As duas instruções canônicas passaram a ser lidas pelo teste de voz e, na Sprint 2, pela API local.

4. **DAS parcial**

O documento descreveu o contexto local, as premissas P-01 a P-04 e as restrições RC-01 a RC-09. Observação de ambiente em 10 de novembro de 2026: o computador expunha o dispositivo de captura ALC257 Analog. A transcrição de uma frase falada de propósito permaneceu pendente.

#### 2.1.2 Lições aprendidas (retrospectiva)

1. **Lista de requisitos.** Fechar o fluxo antes de implementar evitou acrescentar cenário, cadastro ou banco na sprint seguinte. A lista também deixou explícito que o turno é uma requisição HTTP local, o que afastou a tentação de usar a *Live API*.

2. **Combinação tecnológica.** A camada gratuita do provedor único atendeu diálogo e síntese. O SDK oficial não foi caminho suficiente para a síntese: a chamada REST com `responseModalities AUDIO` e `speechConfig.voiceConfig.voice = Kore` foi a que devolveu `audio/wav`. Essa rota REST ficou como restrição de implementação da Sprint 2.

3. **Teste curto de voz.** Uma captura de oito segundos sem frase falada de propósito produz transcrição vazia. O procedimento da sprint seguinte passou a exigir o pedido explícito de uma frase em inglês e a proibição de repetir a chamada até aparecer um texto apresentável.

4. **DAS parcial.** Sem os diagramas, o documento descreveu os contêineres só em texto. A Sprint 2 precisou incorporar contexto, contêineres e sequência no mesmo arquivo, em vez de abrir um DAS novo.

---

### 2.2 Sprint 2 — Prova de conceito local

Período: 9 a 15 de novembro de 2026. As entregas foram implementadas em 15 de novembro de 2026. O objetivo desta sprint foi fazer o fluxo funcionar na máquina local, do cenário de entrevista até o retorno em três blocos, sem persistir áudio nem transcrição.

#### 2.2.1 Solução

**Evidência do planejamento**

A Sprint 2 foi planejada com quatro entregas, correspondentes às issues 5 a 8. Não se reabriu a Sprint 1 e não se iniciou a Sprint 3. Não houve publicação em nuvem, banco, cadastro, histórico em disco, canal bidirecional contínuo, segundo cenário, correção durante a conversa nem medida de fluência.

**Figura 7 — Definição da Sprint 2**

*(inserir `deliverables/cronograma-sprints/sprint-2.png`)*

Issues de planejamento: [issue 5](https://github.com/fsluizvictor/poc-en-simulator/issues/5), [issue 6](https://github.com/fsluizvictor/poc-en-simulator/issues/6), [issue 7](https://github.com/fsluizvictor/poc-en-simulator/issues/7) e [issue 8](https://github.com/fsluizvictor/poc-en-simulator/issues/8). *(Opcional: inserir captura da lista de issues com a etiqueta `sprint-2`.)*

**Evidência da execução de cada requisito**

1. **Interface local do cenário de entrevista** *(issue 5)*

Implementou-se uma tela em React, servida em `http://127.0.0.1:5173`. O único cenário exibido é “Entrevista de emprego — Tecnologia”. Não há seletor de cenário, cadastro nem segundo fluxo. A tela captura o microfone, envia o áudio à API local, reproduz a voz da entrevistadora e, ao encerrar, mostra os três blocos. A chave do modelo não entra no navegador: as chamadas do *front-end* vão só para `/api` na máquina local.

**Figura 8 — Interface local, cenário único**

*(inserir `deliverables/area-de-experimentacao/assets/interface-local.png`)*

2. **API local do turno de voz** *(issue 6)*

Implementou-se a API em Python 3.12, no padrão BFF, em `http://127.0.0.1:8765`. Cada turno é uma requisição síncrona: o áudio entra; reconhecimento, diálogo e síntese ocorrem na mesma requisição; texto e áudio da entrevistadora saem. A chave `GEMINI_API_KEY` permanece no ambiente do processo. O histórico textual fica só em memória. O áudio do usuário é lido, enviado ao reconhecimento e descartado; a aplicação não grava `.wav` nem transcrição em disco.

Modelos utilizados, conforme a combinação da Sprint 1:

| Papel | Modelo | Observação |
|-------|--------|------------|
| Reconhecimento | `gemini-3.5-transcribe` | Modo `VERBATIM`, idioma sugerido `en-US`. Sem instrução de sistema. |
| Diálogo | `gemini-3.5-flash-lite` | Instrução `prompts/entrevistador.txt`. |
| Síntese | `gemini-3.8-flash-lite-tts` | REST `generateContent`, voz Kore. |
| Retorno | `gemini-3.5-flash-lite` | Segunda chamada, só no encerramento, com `prompts/feedback.txt`. |

Rotas: `POST /api/sessions` (abertura), `POST /api/sessions/{id}/turns` (áudio do turno), `POST /api/sessions/{id}/end` (três blocos) e `GET /api/health` (indica se a chave está configurada, sem expô-la).

3. **Feedback em três blocos** *(issue 7)*

O encerramento não reutiliza a instrução da entrevistadora. A API apaga a sessão da memória e chama o modelo com a transcrição acumulada e `prompts/feedback.txt`. A correção não ocorre no meio da conversa: a entrevistadora, diante de transcrição vazia, pediu que a pessoa repetisse em uma frase curta, sem mencionar reconhecimento de fala.

4. **Diagramas de contexto, contêineres e sequência** *(issue 8)*

Os três diagramas foram incorporados ao DAS parcial já existente (`docs/sprint-1/das-parcial.md`), que passou à versão 0.2. Não se abriu um DAS novo. A sessão-piloto e a nota de privacidade continuam fora desta versão.

**Evidência dos resultados**

1. **Interface local**

A tela abriu na máquina local com um único cenário. Após “Iniciar entrevista”, a API devolveu a fala da entrevistadora e o áudio correspondente, reproduzido na própria tela (nove segundos na verificação de 15 de novembro de 2026). Os botões “Gravar resposta” e “Encerrar sessão” ficam habilitados só depois da abertura.

Fala observada na abertura pela interface: “Welcome to the interview, and thanks for taking the time to chat today. Could you briefly introduce yourself and share a bit about your experience with software development?”

2. **API local do turno**

Em 15 de novembro de 2026, `GET /api/health` devolveu `{"ok": true, "key_configured": true}` sem a chave. `POST /api/sessions` devolveu identificador de sessão, texto da entrevistadora e áudio `audio/wav` (309.148 bytes na primeira abertura verificada). `POST /api/sessions/{id}/turns` recebeu o WAV da captura e devolveu texto e áudio. Nenhum arquivo `.wav` novo foi gravado no repositório. A porta 8000 já estava ocupada por outro serviço na máquina; a API local passou a escutar na porta 8765.

No primeiro turno real pediu-se, em voz alta, a frase em inglês “I am a software engineer and I work with Python and web APIs.” A captura durou dez segundos e **não foi repetida**.

- Transcrição: [vazia]. Nenhuma frase foi inventada.
- Fala seguinte da entrevistadora: “Could you say that again in one short sentence?”
- Este resultado **não** afirma reconhecimento de sotaque brasileiro e **não** confirma que a frase pedida tenha sido dita no microfone.

O registro completo está em `docs/sprint-2/resultado-primeiro-turno.md`. O áudio da pessoa foi apagado ao fim do script.

3. **Feedback em três blocos**

A segunda chamada ao modelo devolveu somente os três blocos pedidos. O texto abaixo é o que o modelo gerou, conservado como foi devolvido. O primeiro bloco atribuiu participação ao candidato sem citar uma frase dita por ele; isso é limitação do modelo, não evidência de fala reconhecida.

Pontos positivos:

- O candidato participou da simulação e respondeu prontamente ao pedido do entrevistador (“Could you say that again in one short sentence?”).

Pontos de melhoria:

- A amostra fornecida é insuficiente, pois o candidato não deu uma resposta para a primeira pergunta (“Could you briefly introduce yourself and tell me a bit about your experience with software development?”), o que impede a avaliação de estrutura de frases e adequação para uma entrevista de emprego.

Próximo passo:

- Grave novamente uma resposta completa de uma frase para a pergunta de apresentação e experiência em desenvolvimento de software.

4. **Diagramas no DAS**

Os três diagramas passaram a constar do mesmo documento. As figuras 9 a 11 reproduzem o contexto, os contêineres e a sequência de um turno.

**Figura 9 — Diagrama de contexto**

*(inserir `deliverables/area-de-experimentacao/assets/contexto.png`)*

**Figura 10 — Diagrama de contêineres**

*(inserir `deliverables/area-de-experimentacao/assets/conteineres.png`)*

**Figura 11 — Diagrama de sequência de um turno**

*(inserir `deliverables/area-de-experimentacao/assets/sequencia-turno.png`)*

O documento canônico permanece `docs/sprint-1/das-parcial.md`. Não há banco de dados, fila nem canal bidirecional contínuo.

#### 2.2.2 Lições aprendidas (retrospectiva)

1. **Interface local.** Uma tela basta para o fluxo. O cenário único precisa aparecer como rótulo, não como lista de escolha: qualquer seletor sugeriria um segundo cenário que o escopo exclui. A reprodução automática da voz da entrevistadora depende do clique em “Iniciar entrevista”; o controle de áudio na tela cobre o caso em que o navegador bloqueia o autoplay.

2. **API local do turno.** Isolar a chave no processo da API atendeu RF-08. A porta 8000 não estava livre nesta máquina; a prova de conceito local não exige porta canônica, desde que interface e API permaneçam em `127.0.0.1`. A rota REST de síntese da Sprint 1 repetiu-se com sucesso (áudio WAV na abertura). O reconhecimento devolveu transcrição vazia pela segunda vez; a captura não foi repetida para obter um texto apresentável. Sem frase reconhecida, o critério RF-03 (transcrição suficiente para o diálogo continuar) permanece sem evidência positiva. A entrevistadora, ainda assim, manteve o papel e pediu que a pessoa repetisse, o que permite o fluxo continuar mesmo com transcrição vazia.

3. **Feedback em três blocos.** A segunda chamada, com outra instrução, devolveu os três cabeçalhos e não acrescentou um quarto bloco. A instrução pede que se declare amostra insuficiente quando não houver frase do candidato; o modelo, mesmo assim, preencheu “pontos positivos” com participação inferida. Para a sessão-piloto da Sprint 3, esse desvio precisa ser lido como limitação do retorno, não como avaliação da fala.

4. **Diagramas.** Incorporar os três desenhos no DAS parcial evitou um documento paralelo. A versão continua 0.2 e parcial: a sessão-piloto de cinco a dez minutos, a nota de privacidade fechada e o DAS na versão 1 pertencem à Sprint 3. A publicação em nuvem não foi feita e não é condição para encerrar esta sprint.

---

### 2.3 Sprint 3 — Sessão-piloto e fechamento do DAS

Período: 16 a 22 de novembro de 2026. As entregas 1, 2 e 3 foram executadas em 20 de novembro de 2026. A entrega 4, publicação em nuvem, não foi realizada. A prova de conceito permanece local.

#### 2.3.1 Solução

**Evidência do planejamento**

A Sprint 3 foi planejada com quatro entregas. A figura 12 reproduz o cartão de planejamento da sprint. As três primeiras têm evidência de execução. A quarta não foi executada.

**Figura 12 — Definição da Sprint 3**

*(inserir `deliverables/cronograma-sprints/sprint-3.png`)*

**Evidência da execução de cada requisito**

1. **Registro da sessão-piloto**

A sessão ocorreu na interface local, em `http://127.0.0.1:5173`, no cenário “Entrevista de emprego — Tecnologia”. O início foi o clique em “Start interview”. O encerramento foi o clique em “End interview”. O relógio local marcou 21:11:25 com a tela em “Starting”, durante o pedido da abertura, e 21:19:47 com a tela em “Processing”, depois do clique de encerramento. A duração medida foi de oito minutos e 22 segundos. A rota de encerramento respondeu 200.

Antes da sessão oficial, o diagnóstico usou uma única captura. O modelo `gemini-3.5-transcribe` devolveu a frase no campo `candidates[].content.parts[].text`, que é o campo já lido pelo extrator em `api/gemini_client.py`. A transcrição extraída foi “I am a software engineer and I work with Python and web”. O extrator não foi alterado e não houve segunda captura de diagnóstico. Essa captura não entra na contagem dos quatro turnos.

A sessão oficial teve quatro turnos com transcrição não vazia. Cada turno devolveu a fala seguinte da entrevistadora com áudio. Nenhuma chamada HTTP dessa sessão falhou. Uma abertura anterior, encerrada sem resposta falada, não entra neste registro. O áudio da pessoa foi apagado ao fim de cada turno e não está no repositório.

Arquivo: `docs/sprint-3/registro-sessao-piloto.md`, no repositório `poc-en-simulator`.

2. **Nota de privacidade**

A nota foi redigida em 20 de novembro de 2026, a partir da leitura do código. Nenhum arquivo de aplicação foi alterado. O critério da sprint confirma-se para o áudio da pessoa: em `api/app.py`, o corpo do turno segue ao reconhecimento e, na linha seguinte, `audio_bytes = b""`. `api/sessions.py` guarda apenas `role` e `text`.

A transcrição não segue o mesmo intervalo. O texto entra em `session.history` e permanece na memória do processo até `POST /api/sessions/{id}/end`. Nessa rota a sessão sai do dicionário e `history.clear()` é chamado. A transcrição não é gravada em disco e não some ao fim de cada turno. Se o encerramento não for chamado, o histórico permanece no processo.

No navegador, `web/src/hooks/useInterview.js` acumula as falas em `messages` e, depois do encerramento, guarda os três blocos em `feedback`. Esse estado dura enquanto a página estiver aberta. Não há `localStorage`, `sessionStorage` nem IndexedDB. O áudio do microfone não fica em estado depois do envio. O áudio reproduzido é o da entrevistadora, em blob URL.

Acima de 1 MB, o parser de formulário do Starlette pode usar arquivo temporário de spool. `await audio.close()` ocorre antes do reconhecimento, e o fechamento destrói esse temporário. Não é um `.wav` gravado pela aplicação. O limite do turno continua 8 MB, em `MAX_AUDIO_BYTES`.

A página de preços do provedor foi reaberta nesta data. Na camada gratuita, o conteúdo enviado pode ser usado para melhoria dos produtos (GOOGLE, 2026a). Nos três modelos usados, a coluna gratuita de “Used to improve our products” está como Yes. A aplicação não controla essa retenção. Por isso a sessão usa somente a voz de quem executa o teste. A nota não afirma conformidade certificada com a Lei Geral de Proteção de Dados (LGPD) nem que o provedor apague o conteúdo.

A suíte local, sem chamada ao provedor, executou cinco testes em 0,188 s, com resultado OK. Dois deles cobrem a ausência de áudio no histórico e a remoção da sessão no encerramento.

Arquivo: `docs/sprint-3/nota-de-privacidade.md`, no repositório `poc-en-simulator`.

3. **DAS versão 1**

Redigido em 20 de novembro de 2026, a partir da versão 0.2, do código, do registro da sessão-piloto e da nota de privacidade. O documento descreve a arquitetura como construída e validada nessa sessão: reconhecimento, diálogo e síntese em cascata, interface em React e API local em Python 3.12. Reúne os requisitos RF-01 a RF-08, as restrições RC-01 a RC-09, as premissas P-01 a P-04, oito decisões arquiteturais e o resultado da sessão. A publicação em nuvem e a visão de produto mínimo viável constam do mesmo documento, rotuladas como proposta não implantada e como evolução fora da versão 1. A latência de cada etapa do turno não foi medida; essa lacuna está declarada. O arquivo parcial do repositório, `docs/sprint-1/das-parcial.md`, permanece na versão 0.2. A versão 1 está nos entregáveis, em `deliverables/proposta-de-arquitetura/das-v1-simulador-entrevista.docx`.

4. **Publicação em nuvem**

Não realizada. A prova de conceito permanece local, em `http://127.0.0.1:5173`, com a API em `http://127.0.0.1:8765`. O DAS versão 1 descreve uma implantação proposta na AWS e lista os ajustes de código que ela exigiria. Nenhum serviço foi implantado. Essa publicação não é condição para concluir o objetivo.

**Evidência dos resultados**

1. **Sessão-piloto**

A abertura, devolvida com áudio, foi: “Hi, thanks for joining me today. Could you briefly introduce yourself and tell me a bit about your experience with software development?”

Os quatro turnos abaixo reproduzem a transcrição e a fala seguinte como a interface as mostrou. A abertura não entra na contagem.

Turno 1. Transcrição: “I am a software engineer and I have about five years of experience. At the moment I worked with closure.” Fala seguinte: “That sounds interesting. Could you tell me about a recent project you worked on using Clojure?”

Turno 2. Transcrição: “Of course, I explain my experience saying about my of my current company. Well, my current company is a financial company.” Fala seguinte: “Thanks for sharing that. What did your role involve on that project at the financial company?”

Turno 3. Transcrição: “Of course, my current job is about the director on app of this company.” Fala seguinte: “Could you tell me about a specific technical difficulty or challenge you ran into while working on that app?”

Turno 4. Transcrição: “Of course, my principal problem that I worked direct in my company is involve involve latency and other metrics about the.” Fala seguinte: “How did you go about investigating and resolving that latency issue?”

A figura 13 é a captura da tela ao encerrar. Nela aparecem o cenário, o estado “Session ended”, a última pergunta da entrevistadora, o último trecho reconhecido e os blocos de retorno visíveis nessa captura.

**Figura 13 — Tela ao encerrar a sessão-piloto**

*(inserir `deliverables/area-de-experimentacao/assets/sessao-piloto-encerrada.png`)*

O retorno em três blocos é o texto que a tela mostrou depois de “End interview”, conservado como foi devolvido.

Pontos positivos:

- Você demonstrou cordialidade e disposição para responder às perguntas ao usar frases como “Of course, I explain my experience...” e “Of course, my current job is about...”.
- Você manteve o foco no contexto profissional ao mencionar o seu tempo de experiência (“I am a software engineer and I have about five years of experience”) e o setor da empresa (“a financial company”).

Pontos de melhoria:

- Houve repetições e hesitações na estrutura das frases que dificultam a clareza, como em “my principal problem that I worked direct in my company is involve involve latency and other metrics about the”.
- A formulação das respostas em alguns momentos soou truncada ou incompleta, por exemplo, “about the director on app of this company”, o que prejudica a fluidez esperada em uma entrevista de emprego.

Próximo passo:

- Pratique responder a uma pergunta de entrevista por vez, escrevendo primeiro um rascunho de frase curta e direta (por exemplo, focando em um problema técnico e sua solução) e, em seguida, treinando a fala em voz alta sem repetir palavras.

Este resultado não afirma ganho de fluência, não trata a transcrição como prova geral de reconhecimento de sotaque brasileiro e não inclui amostra externa.

2. **Nota de privacidade**

O resultado é a distinção registrada na nota. O áudio da pessoa é descartado ao fim do turno. A transcrição permanece só em memória até o encerramento. O navegador mostra o texto enquanto a página está aberta e não o grava. O provedor, na camada gratuita, pode usar o conteúdo enviado para melhoria dos próprios produtos. Nenhum código foi alterado para produzir essa nota.

3. **DAS versão 1**

O resultado é o documento de fechamento, versão 1, de 20 de novembro de 2026. Os requisitos RF-01 a RF-08 constam como atendidos na sessão-piloto. As figuras da visão geral, dos componentes da API e da implantação proposta estão no relatório, nas figuras 17 a 19. A implantação proposta não foi executada.

4. **Publicação em nuvem**

Sem implantação. A saída registrada é a permanência local da prova de conceito.

#### 2.3.2 Lições aprendidas (retrospectiva)

1. **Reconhecimento.** O extrator não era a causa das transcrições vazias de 10 e de 15 de novembro de 2026. No diagnóstico de 20 de novembro de 2026, o provedor devolveu texto no campo que o código já lia. Na sessão oficial, os quatro turnos trouxeram transcrição não vazia, dentro de oito minutos e 22 segundos. O requisito RF-03 passa a ter evidência positiva nesta sessão. As hesitações permaneceram no texto (“involve involve”, “about the director on app”), o que é compatível com o modo literal escolhido na Sprint 1. Isso não autoriza afirmar acurácia para sotaque brasileiro fora desta sessão.

2. **Diálogo.** A entrevistadora manteve o papel e fez a pergunta seguinte a partir do texto reconhecido, inclusive quando a frase veio truncada. No turno 1, a transcrição traz “closure” e a fala seguinte pergunta sobre “Clojure”. O registro conserva as duas formas. Não se corrige uma pela outra.

3. **Retorno em três blocos.** Desta vez os blocos citam trechos da transcrição da própria sessão. Em 15 de novembro de 2026, com transcrição vazia, o bloco de pontos positivos tinha atribuído participação sem citar uma frase dita. A diferença fica registrada como comportamento observado do modelo, não como validação pedagógica do retorno.

4. **Privacidade.** A frase “áudio e transcrição não permanecem armazenados após o turno” vale, na leitura do código, para o áudio da pessoa. A transcrição fica na memória do processo até o encerramento, porque o turno seguinte e os três blocos dependem dela. Acima de 1 MB, o spool temporário do parser não foi tratado como gravação da aplicação: ele é fechado antes do reconhecimento. A coluna gratuita “Used to improve our products” igual a Yes, reaberta em 20 de novembro de 2026, mantém a restrição de usar apenas a voz de quem executa o teste. A nota não certifica conformidade com a LGPD.

5. **DAS versão 1.** O fechamento descreveu a arquitetura como construída na sessão-piloto. A proposta anterior de chat de texto, com banco, fila e cadastro, ficou na visão de evolução, fora da versão 1. A latência de cada etapa do turno não foi medida e permanece como lacuna declarada.

6. **Publicação em nuvem.** Não foi executada. O objetivo não depende dela. A topologia proposta ficou no DAS, com o rótulo de não implantada. Ela exigiria ajustes que a versão local não tem: API sem estado, limite de áudio menor e tempos-limite por etapa.
