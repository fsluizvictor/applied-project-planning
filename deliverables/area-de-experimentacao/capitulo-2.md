# Instruções de colagem (apagar antes de entregar)

Colar no capítulo 2 do template XP/IGTI, na seção “Área de Experimentação”. Inserir as figuras nos pontos indicados. Os arquivos estão neste diretório e em `deliverables/cronograma-sprints/`.

Não colar chave de API, arquivos `.wav` nem transcrição inventada. A Sprint 3 ainda não ocorreu: deixar a subseção 2.3 apenas com o texto de reserva.

---

## 2. Área de Experimentação

A área de experimentação registra o planejamento, a execução e o resultado das sprints da prova de conceito. O quadro Kanban previsto no escopo foi materializado nas issues do repositório GitHub do artefato (`poc-en-simulator`), uma issue por entrega, com as etiquetas `sprint-1` e `sprint-2`. As Sprints 1 e 2 foram executadas. A Sprint 3 permanece reservada à sessão-piloto, à nota de privacidade e ao DAS na versão 1.

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

Período planejado: 16 a 22 de novembro de 2026. **Esta sprint ainda não foi executada.** Não há registro de sessão-piloto, nota de privacidade fechada, DAS na versão 1 nem publicação em nuvem a anexar.

**2.3.1 Solução.** *A preencher após a execução.*  
Evidências previstas: registro da sessão-piloto (duração, turnos reconhecidos e feedback); nota de privacidade; DAS versão 1. A publicação em nuvem só é evidência se tiver sido feita. Não antecipar números.

**2.3.2 Lições aprendidas / Retrospectiva.** *A preencher após a execução.*
