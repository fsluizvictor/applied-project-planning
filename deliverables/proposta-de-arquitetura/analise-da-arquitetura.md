# Análise e validação da proposta de arquitetura

**Projeto:** Simulador de Conversação em Inglês com Inteligência Artificial  
**Sprint:** 3 — Sessão-piloto e fechamento do DAS (16 a 22 de novembro de 2026)  
**Data da análise:** 20 de novembro de 2026  
**Material analisado:** `proposta_arquitetura_simulador_entrevistas.md`, `proposta_arquitetura_aws_simulador_entrevistas.md` (duas versões), os seis PNG desta pasta, o DAS parcial v0.2 e o código do repositório `poc-en-simulator`.

---

## 1. Parecer

Os princípios das propostas são sólidos e podem permanecer no projeto final: caminho crítico síncrono, monólito modular, isolamento do provedor por adaptador, controle de tokens, observabilidade de latência e evolução incremental. A arquitetura desenhada nos diagramas, porém, **não pode ser adotada como arquitetura da versão 1 do DAS**, por três motivos verificáveis.

1. **Descreve outro produto.** Os documentos tratam de um chat de texto com LLM. O artefato do projeto é um simulador **por voz**, cujo núcleo é a cascata reconhecimento de fala (*Automatic Speech Recognition* — ASR) → modelo de linguagem (*Large Language Model* — LLM) → síntese de voz (*Text-to-Speech* — TTS). Nenhum diagrama anterior contém ASR nem TTS.
2. **Contradiz o escopo aprovado.** Banco de dados (DynamoDB), cadastro (Cognito), persistência de mensagens e fila (SQS) estão listados como fora do escopo em `docs/sprint-1/requisitos-do-fluxo.md` e violariam RC-02 (orçamento nulo), RC-03 (execução local) e RC-04 (sem armazenamento de áudio ou transcrição).
3. **Não reflete o que foi construído.** O nível C4 de código cita `routes.py`, `handlers.py`, `ports.py` e `repository.py`, que não existem. O código real está em `api/app.py`, `api/sessions.py`, `api/gemini_client.py` e `api/feedback.py`.

A recomendação é fechar o DAS v1 com a arquitetura **como construída e validada na sessão-piloto**, acrescentar uma **visão de implantação AWS proposta** (opcional, como prevê a entrega 4 da Sprint 3) e mover os elementos das propostas anteriores para uma **visão de evolução**, cada um com o gatilho que justificaria sua entrada. Os diagramas novos estão em `diagramas-v2/`, e o rascunho do DAS v1 está em `das-v1-rascunho.md`.

---

## 2. Aderência ao escopo do projeto

| Elemento das propostas | Situação no projeto | Destino recomendado |
|---|---|---|
| Fluxo síncrono no caminho crítico | Igual ao código: um turno é uma requisição | Manter |
| Monólito modular, sem microsserviços | Igual ao código: um processo FastAPI | Manter |
| Adaptador de LLM agnóstico | Parcial: `gemini_client.py` concentra ASR, diálogo e síntese do mesmo fornecedor | Manter como melhoria (portas separadas) |
| Métricas de latência (TTFT, total, por dependência) | Não implementadas; a sessão-piloto não mediu latência por etapa | Manter como melhoria prioritária |
| Controle de tokens e de contexto | Histórico completo enviado a cada turno; sessões de cinco a dez minutos tornam o volume pequeno | Manter como diretriz; sumarização não é necessária na v1 |
| Streaming SSE da resposta | Não se aplica diretamente: a saída é áudio WAV completo | Mover para evolução (streaming por frase) |
| Amazon DynamoDB e persistência de mensagens | Fora do escopo e contrário a RC-04 | Mover para evolução, com consentimento e TTL |
| Amazon Cognito | Fora do escopo (sem cadastro) | Mover para evolução |
| Amazon SQS, worker e DLQ | O retorno em três blocos é uma chamada síncrona no encerramento e funcionou na sessão-piloto | Mover para evolução |
| RAG e base vetorial | Sem corpus próprio | Mover para evolução (as propostas já indicavam isso) |
| AWS WAF | Cobrança mensal fixa, incompatível com RC-02 | Substituir por limite de requisições no API Gateway |
| AWS Secrets Manager | Cobrança por segredo | Substituir por Parameter Store (SecureString, camada padrão) |
| Nível C4 de código | Módulos inexistentes | Remover; usar diagrama dinâmico |

---

## 3. Validação contra arquiteturas de referência

As fontes abaixo são documentação oficial ou repositórios oficiais de amostras. `[FONTE-SECUNDÁRIA]`

| Referência | O que estabelece | Implicação para o projeto |
|---|---|---|
| OpenAI, *Voice agents* (OPENAI, 2026) | Distingue três arquiteturas de voz; a cascata (*chained voice pipeline*) é indicada quando cada etapa precisa ser visível ou substituível; *speech-to-speech* é indicada para menor latência e interrupções naturais | Confirma a decisão da Sprint 1 de usar cascata e de afastar a *Live API*: a transcrição literal precisa ficar visível para o retorno final |
| AWS Samples, *amazon-bedrock-voice-conversation* (AMAZON WEB SERVICES, 2026a) | Implementação de referência da mesma cascata com Amazon Transcribe, Bedrock e Polly, com streaming em quase todas as etapas | O desenho do projeto é o mesmo padrão; o streaming é a otimização seguinte, não um requisito da v1 |
| AWS Samples, *sample-voice-agent-on-aws* (AMAZON WEB SERVICES, 2026b) | Compara cascata e streaming bidirecional; registra que a cascata tem latência maior e permite trocar STT, LLM e TTS de forma independente | Justifica separar no código as portas de ASR, LLM e TTS |
| Microsoft, *Baseline Microsoft Foundry Chat Reference Architecture* (MICROSOFT, 2026) | Arquitetura corporativa de chat com memória persistida, rede privada, *firewall* e WAF | Mostra o que um produto corporativo exige; serve de contraste para justificar por que a prova de conceito não adota esses elementos |
| AWS, *Well-Architected Generative AI Lens* (AMAZON WEB SERVICES, 2025) | Organiza boas práticas de IA generativa nos seis pilares (excelência operacional, segurança, confiabilidade, desempenho, custo, sustentabilidade) | Pode estruturar a seção de atributos de qualidade do DAS |
| OWASP, *Top 10 for LLM Applications 2025* (OWASP, 2025) | LLM01 (*prompt injection*), LLM02 (vazamento de informação sensível) e LLM10 (consumo sem limite) | Base para a seção de segurança: a transcrição é entrada não confiável; publicação exige limite de requisições |
| C4 model, *Notation* e *Diagrams* (BROWN, 2026) | Todo diagrama deve ter título, legenda, tipo e tecnologia de cada elemento e linhas unidirecionais rotuladas; o nível de código é opcional e não recomendado para manutenção manual | Os diagramas anteriores não atendiam a essas regras; os novos atendem |

**Inferência da análise** (não afirmada pelas fontes): a cascata síncrona é adequada à prova de conceito porque o turno é do tipo “aperte para falar” (*push-to-talk*). O próprio guia do OpenAI Agents SDK trata esse caso como entrada de áudio completa, sem necessidade de detecção de atividade de voz.

---

## 4. Limitações técnicas verificadas para a publicação na AWS

Os valores foram conferidos na documentação oficial em 20 de novembro de 2026 e devem ser revistos antes da implantação. `[FONTE-SECUNDÁRIA]`

| Limite | Valor documentado | Impacto no código atual |
|---|---|---|
| Payload síncrono da Lambda (requisição e resposta) | 6 MB cada | `MAX_AUDIO_BYTES` é 8 MB; corpos binários chegam à Lambda em base64, o que reduz o áudio útil para cerca de 4,5 MB `[ASSUMPTION — requires validation]` |
| Streaming de resposta da Lambda | Nativo só em Node.js; Python exige *runtime* personalizado ou Lambda Web Adapter | As propostas sugeriam streaming sem registrar essa restrição |
| Tempo-limite de integração do API Gateway | REST: 29 s por padrão, ampliável em APIs regionais; HTTP API: 30 s, não ampliável | Cada chamada ao Gemini tem `REQUEST_TIMEOUT_SECONDS = 90`; no pior caso o turno ultrapassa o limite |
| Histórico em memória | Instâncias Lambda não compartilham memória | `api/sessions.py` perderia sessões entre instâncias; a API precisa ficar sem estado |
| CloudFront com OAC na frente de uma URL de função Lambda | POST exige o cabeçalho `x-amz-content-sha256` calculado pelo cliente | Inviabiliza na prática o envio multipart; por isso a proposta usa API Gateway HTTP API |
| Concorrência reservada | Exige manter 100 unidades não reservadas; contas novas começam com cota reduzida | Não serve como teto de custo em conta nova; usar limite de requisições do API Gateway |
| Free plan da AWS | Até US$ 200 em créditos, conta encerrada em seis meses ou ao fim dos créditos | Compatível com RC-02, mas a publicação seria temporária |
| Termos da camada gratuita do Gemini | Conteúdo pode ser usado para melhorar produtos e lido por revisores humanos; orientação de não enviar dados pessoais | Publicar para terceiros contrariaria RC-09; a publicação deve ficar restrita a quem executa o teste |

---

## 5. Problemas dos diagramas anteriores

1. **Setas atravessam caixas e rótulos.** No C2 e no C4 de código, várias linhas cruzam textos (“implementado por”, “verifica comportamento”).
2. **Sem legenda, tipo ou tecnologia.** Os elementos não indicam se são pessoa, contêiner ou componente, nem a tecnologia, o que contraria a notação recomendada pelo C4 (BROWN, 2026).
3. **Rótulos de uma palavra.** “API”, “evento” e “mensagem” não descrevem a intenção da relação.
4. **Níveis misturados.** “Serviços transversais” aparece como contêiner no C2, mas não é unidade executável.
5. **Conteúdo divergente do sistema.** Faltam ASR, TTS, instruções de sistema e retorno em três blocos; sobram banco, fila e armazenamento de objetos.
6. **Diagrama AWS denso.** Dezessete setas curvas convergem para poucos pontos, e a leitura do caminho crítico depende do rodapé.

---

## 6. Diagramas novos

| Arquivo | Tipo | Conteúdo |
|---|---|---|
| `diagramas-v2/00-visao-geral.png` | Visão conceitual | Cascata ASR → LLM → TTS no turno e retorno no encerramento |
| `diagramas-v2/01-c1-contexto.png` | C4 nível 1 | Pessoa, simulador e API Gemini; o que está fora do contexto |
| `diagramas-v2/02-c2-conteineres.png` | C4 nível 2 | Interface React, API FastAPI, instruções e provedor, como construídos |
| `diagramas-v2/03-c3-componentes.png` | C4 nível 3 | Módulos reais de `api/` e as quatro funções do cliente do provedor |
| `diagramas-v2/04-dinamico-turno.png` | C4 dinâmico | Sequência numerada de um turno e do encerramento |
| `diagramas-v2/05-implantacao-aws.png` | C4 implantação | Publicação proposta, com os ajustes de código exigidos |
| `diagramas-v2/06-mapa-de-evolucao.png` | Suplementar | Versões 1, 1.1 e 2, com gatilhos de entrada |

Os SVG ficam ao lado dos PNG e são gerados por `diagramas-v2/gerar-diagramas.py`. Para alterar um diagrama, deve-se editar o script e executá-lo novamente.

---

## 7. Pontos de melhoria

### 7.1 No documento (para fechar o DAS v1 nesta sprint)

1. Trocar a arquitetura genérica pela arquitetura de voz como construída, com os diagramas 00 a 04.
2. Registrar as decisões como decisões arquiteturais resumidas (AD), com alternativa descartada e consequência. O rascunho traz oito decisões.
3. Incluir o resultado da sessão-piloto confrontado com o critério da Sprint 3: oito minutos e 22 segundos, quatro turnos reconhecidos, resposta oral e retorno em três blocos.
4. Distinguir, na seção de privacidade, o áudio (descartado ao fim do turno) da transcrição (em memória até o encerramento), como faz a nota de privacidade.
5. Declarar como lacuna a latência por etapa, que não foi medida.
6. Rotular a implantação AWS como proposta não executada e a evolução como fora do escopo.
7. Corrigir o formato de data das propostas (“20/11/2026” → “20 de novembro de 2026”).

### 7.2 Na arquitetura e no código (versão 1.1, sem reabrir a Sprint 2)

| # | Melhoria | Motivo | Esforço estimado |
|---|---|---|---|
| M-01 | Medir a duração de ASR, diálogo, síntese e do turno completo, e registrá-la em log sem conteúdo | R-05 prevê indicador visual acima de oito segundos, mas não há medição | Baixo |
| M-02 | Tempo-limite por etapa, com soma inferior a 30 s | Hoje são 90 s por chamada, o que estoura o API Gateway | Baixo |
| M-03 | Separar portas `SpeechToText`, `DialogueModel` e `TextToSpeech` | Permite trocar cada etapa, que é a vantagem citada pelas referências | Médio |
| M-04 | Retorno determinístico quando não houver fala reconhecida | Na Sprint 2 o modelo inventou pontos positivos com transcrição vazia; a regra deve ficar no código, não só na instrução | Baixo |
| M-05 | Endereço da API e origens de CORS por variável de ambiente | `API_ROOT` e CORS estão fixos em `127.0.0.1` | Baixo |
| M-06 | API sem estado, com histórico enviado pelo navegador (requisito obrigatório só para a publicação) | Lambda não compartilha memória entre instâncias; o requisito original já previa o navegador enviando o histórico | Médio |
| M-07 | Reduzir `MAX_AUDIO_BYTES` para 4 MB | Limite de payload da Lambda | Baixo |
| M-08 | Rótulo de papel e delimitadores na transcrição enviada ao diálogo | Mitigação parcial de LLM01; a fala transcrita é entrada não confiável | Baixo |

### 7.3 Na evolução (fora do escopo)

Streaming por frase (TTS iniciado na primeira frase gerada), camada paga ou provedores AWS (Transcribe, Bedrock e Polly), contas de usuário, histórico com consentimento e avaliação assíncrona. Cada item aparece no diagrama 06 com seu gatilho.

---

## 8. O que fica no projeto final

| Item | Decisão |
|---|---|
| Princípios das propostas (síncrono, monólito modular, adaptador, observabilidade, custo por sessão) | **Fica**, reescrito para voz |
| Diagramas 00 a 04 de `diagramas-v2/` | **Ficam** como arquitetura do DAS v1 |
| Diagrama 05 de implantação AWS | **Fica** como proposta, com rótulo explícito de não implantada |
| Diagrama 06 de evolução | **Fica** como trabalhos futuros |
| Diagramas e textos anteriores com DynamoDB, Cognito, SQS e RAG | **Saem** do DAS; o conteúdo útil já está no diagrama 06 |
| Nível C4 de código | **Sai** |

---

## 9. Lacunas de evidência e suposições

- `[LACUNA DE EVIDÊNCIA — latência por etapa do turno]`: medir com M-01 em uma nova sessão curta, sem alterar o registro da sessão-piloto.
- `[LACUNA DE EVIDÊNCIA — consumo da cota gratuita por sessão]`: conferir o painel de uso do Google AI Studio após uma sessão.
- `[ASSUMPTION — requires validation]`: a redução de cerca de 33% no áudio útil por codificação base64 depende da integração escolhida (HTTP API com Lambda Web Adapter); confirmar com um turno real de aproximadamente 4 MB.
- `[ASSUMPTION — requires validation]`: a classificação da voz e da fala transcrita como dado pessoal, para efeito da LGPD, é inferência da análise e não parecer jurídico.
- As referências técnicas da seção 10 não constam de `deliverables/phase-2/context-report.md`. Para seguir a regra de evidências do projeto, devem ser registradas lá ou auditadas na revisão acadêmica antes de entrar no relatório final.

---

## 10. Referências

AMAZON WEB SERVICES. **Generative AI Lens**: AWS Well-Architected Framework. 2025. Disponível em: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **amazon-bedrock-voice-conversation**. GitHub, 2026a. Disponível em: https://github.com/aws-samples/amazon-bedrock-voice-conversation. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **sample-voice-agent-on-aws**. GitHub, 2026b. Disponível em: https://github.com/aws-samples/sample-voice-agent-on-aws. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Lambda quotas**. AWS Lambda Developer Guide, 2026c. Disponível em: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Response streaming for Lambda functions**. AWS Lambda Developer Guide, 2026d. Disponível em: https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Quotas for configuring and running a REST API in API Gateway**. Amazon API Gateway Developer Guide, 2026e. Disponível em: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-execution-service-limits-table.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Quotas for configuring and running an HTTP API in API Gateway**. Amazon API Gateway Developer Guide, 2026f. Disponível em: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-quotas.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Restrict access to an AWS Lambda function URL origin**. Amazon CloudFront Developer Guide, 2026g. Disponível em: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-lambda.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Configuring reserved concurrency for a function**. AWS Lambda Developer Guide, 2026h. Disponível em: https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **AWS Free Tier**. 2026i. Disponível em: https://aws.amazon.com/free/. Acesso em: 20 nov. 2026.

AMAZON WEB SERVICES. **Response streaming**: AWS Lambda Web Adapter user guide. 2026j. Disponível em: https://aws.github.io/aws-lambda-web-adapter/configuration/response-streaming.html. Acesso em: 20 nov. 2026.

BROWN, Simon. **The C4 model for visualising software architecture**: notation. 2026. Disponível em: https://c4model.com/diagrams/notation. Acesso em: 20 nov. 2026.

GOOGLE. **Gemini API Additional Terms of Service**. Vigência a partir de 23 mar. 2026. Disponível em: https://aistudio.google.com/docs/terms. Acesso em: 20 nov. 2026.

MICROSOFT. **Baseline Microsoft Foundry chat reference architecture**. Azure Architecture Center, 2026. Disponível em: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat. Acesso em: 20 nov. 2026.

OPENAI. **Voice agents**. OpenAI API documentation, 2026. Disponível em: https://developers.openai.com/api/docs/guides/voice-agents. Acesso em: 20 nov. 2026.

OWASP. **OWASP Top 10 for LLM Applications 2025**. OWASP Gen AI Security Project, 2025. Disponível em: https://genai.owasp.org/llm-top-10/. Acesso em: 20 nov. 2026.
