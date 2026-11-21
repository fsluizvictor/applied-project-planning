# Proposta Inicial de Arquitetura AWS --- Simulador de Entrevistas em Inglês

**Tipo de documento:** proposta preliminar para avaliação arquitetural\
**Objetivo:** apresentar uma arquitetura cloud native simples, escalável
e com custo inicial controlado para um simulador de entrevistas em
inglês baseado em LLM.\
**Status:** rascunho para análise; decisões e dimensionamentos ainda
precisam ser validados por testes.

------------------------------------------------------------------------

## 1. Contexto e objetivo

O projeto consiste em uma aplicação que simula entrevistas de emprego em
inglês. O usuário interage com um entrevistador virtual, responde às
perguntas e recebe novas perguntas ou comentários gerados por um modelo
de linguagem.

A POC existente utiliza uma API própria que recebe as mensagens,
encaminha prompts ao Google Gemini por meio de API REST e devolve as
respostas ao cliente.

A arquitetura proposta deve:

-   manter baixa latência percebida durante a conversação;
-   suportar crescimento no número de usuários e entrevistas
    simultâneas;
-   controlar custos de infraestrutura e consumo de tokens;
-   evitar complexidade operacional desnecessária na primeira versão;
-   permitir evolução para avaliação de entrevistas, personalização,
    RAG, voz e múltiplos provedores de LLM.

A recomendação inicial é uma **arquitetura serverless e modular na
AWS**, mantendo o Gemini como provedor de LLM. A AWS hospeda a
aplicação, a API, a persistência e os serviços auxiliares, enquanto o
modelo é consumido externamente.

Não é necessário utilizar Amazon Bedrock obrigatoriamente. Bedrock pode
ser avaliado futuramente como alternativa de integração ou como caminho
para utilizar modelos disponibilizados pela AWS.

## 2. Diretriz arquitetural

A proposta combina:

-   **Monólito modular:** módulos de domínio organizados em uma
    aplicação coesa, evitando a distribuição prematura em vários
    microsserviços.
-   **Serverless:** API Gateway e AWS Lambda para reduzir a necessidade
    de administrar servidores.
-   **Persistência gerenciada:** DynamoDB para sessões, mensagens e
    resultados.
-   **Integração desacoplada com LLM:** Adapter Pattern para isolar a
    aplicação das particularidades do Gemini.
-   **Comunicação síncrona no fluxo de conversa:** o usuário envia uma
    mensagem e recebe a resposta do entrevistador.
-   **Processamento assíncrono para tarefas secundárias:** SQS e Lambda
    podem executar avaliações e geração de relatórios após a entrevista.

A arquitetura deve ser validada por testes de carga, testes de latência
e estimativas de custo. Serverless não significa capacidade ilimitada:
cotas, concorrência, limites do provedor de LLM e limites dos serviços
precisam ser considerados.

## 3. Visão geral da arquitetura

### 3.1 Diagrama lógico

``` mermaid
flowchart TB
    U[Frontend Web ou Mobile]
    CF[Amazon CloudFront]
    S3[Amazon S3 - Frontend estático]
    AUTH[Amazon Cognito]
    APIGW[Amazon API Gateway]
    LAMBDA[AWS Lambda - Interview API]
    ADAPTER[LLM Provider Adapter]
    GEMINI[Google Gemini API]
    DDB[(Amazon DynamoDB)]
    SM[AWS Secrets Manager]
    CW[Amazon CloudWatch]
    SQS[Amazon SQS]
    WORKER[AWS Lambda - Evaluation Worker]
    DLQ[Dead Letter Queue]

    U --> CF
    CF --> S3
    U --> AUTH
    U --> APIGW
    AUTH -. autenticação .-> APIGW
    APIGW --> LAMBDA
    LAMBDA --> DDB
    LAMBDA --> ADAPTER
    ADAPTER --> GEMINI
    LAMBDA --> SM
    LAMBDA --> CW
    LAMBDA --> SQS
    SQS --> WORKER
    SQS --> DLQ
    WORKER --> DDB
    WORKER --> GEMINI
    WORKER --> CW
```

### 3.2 Componentes

  -----------------------------------------------------------------------
  Componente              Responsabilidade        Necessidade inicial
  ----------------------- ----------------------- -----------------------
  Amazon CloudFront       Distribuição do         Recomendado se houver
                          frontend e cache de     frontend web
                          conteúdo estático       

  Amazon S3               Hospedagem dos arquivos Opcional para a POC
                          estáticos e documentos  

  Amazon Cognito          Autenticação e          Necessário quando
                          gerenciamento de        houver contas de
                          usuários                usuário

  Amazon API Gateway      Exposição, roteamento,  Sim
                          autorização e           
                          throttling da API       

  AWS Lambda              Execução da lógica da   Sim
                          aplicação               

  Google Gemini API       Geração de perguntas e  Sim, conforme a POC
                          respostas               

  LLM Provider Adapter    Abstração do provedor   Sim, como módulo de
                          de LLM                  software

  Amazon DynamoDB         Persistência de         Recomendado
                          sessões, mensagens e    
                          avaliações              

  AWS Secrets Manager     Armazenamento seguro da Sim em ambiente AWS
                          chave do Gemini         

  Amazon CloudWatch       Logs, métricas e        Sim
                          alarmes                 

  Amazon SQS              Fila para tarefas       Evolução recomendada
                          secundárias             

  Lambda Evaluation       Processamento de        Evolução
  Worker                  avaliações em segundo   
                          plano                   

  Dead Letter Queue       Armazenamento de        Junto ao SQS
                          mensagens que falharam  
                          repetidamente           
  -----------------------------------------------------------------------

### 3.3 Responsabilidades por camada

**Frontend** - Exibir a entrevista e o histórico de mensagens. - Enviar
respostas do candidato. - Apresentar respostas progressivamente quando
houver streaming. - Consultar o status e o resultado da avaliação.

**Camada de entrada** - Receber requisições HTTPS. - Validar
autenticação e autorização. - Aplicar limites de requisições. -
Direcionar as chamadas aos handlers da aplicação.

**Camada de aplicação** - Gerenciar o ciclo de vida das entrevistas. -
Recuperar e atualizar o contexto da conversa. - Construir prompts. -
Coordenar chamadas ao provedor de LLM. - Persistir mensagens e estado da
sessão.

**Camada de integração com LLM** - Isolar a API específica do Gemini. -
Normalizar entradas e saídas. - Tratar erros, timeouts e limites do
provedor. - Permitir a inclusão de outros provedores no futuro.

**Camada de persistência** - Armazenar sessões, mensagens e
avaliações. - Permitir consultas pelo identificador da sessão. - Manter
os dados necessários para reconstruir o contexto da entrevista.

## 4. Fluxo principal de uma interação

Considere um usuário realizando uma entrevista para uma vaga de
desenvolvedor de software.

1.  O usuário inicia uma entrevista e seleciona informações como cargo,
    nível de experiência e idioma.
2.  O frontend envia a mensagem do candidato para a API.
3.  O API Gateway recebe a requisição, aplica as políticas configuradas
    e encaminha a chamada à Lambda.
4.  A Lambda valida a solicitação e recupera o estado da entrevista no
    DynamoDB.
5.  O gerenciador de contexto seleciona as mensagens relevantes e, se
    necessário, um resumo da conversa.
6.  O módulo de aplicação monta o prompt e chama o LLM Provider Adapter.
7.  O adapter encaminha a solicitação ao Google Gemini.
8.  O Gemini gera a resposta.
9.  A aplicação persiste a mensagem do usuário e a resposta do
    entrevistador.
10. A resposta é devolvida ao frontend.

É importante definir o comportamento de persistência em caso de falha
parcial. Por exemplo, se o Gemini responder, mas a gravação no banco
falhar, a aplicação deve registrar a falha e permitir recuperação ou
repetição controlada, evitando duplicidade de mensagens.

### 4.1 Exemplo de endpoint

``` http
POST /api/v1/interviews/{interview_id}/messages
Content-Type: application/json
Authorization: Bearer <token>
```

Corpo:

``` json
{
  "message": "I have experience with Python and AWS.",
  "language": "en"
}
```

Exemplo simplificado de resposta:

``` json
{
  "interview_id": "12345",
  "message": "Can you explain how you used AWS?",
  "status": "in_progress"
}
```

O contrato real deve incluir identificador da mensagem, timestamps,
tratamento de erros e, se necessário, metadados de consumo de tokens.

### 4.2 Gerenciamento do contexto

Não é recomendável enviar indefinidamente todo o histórico da entrevista
ao modelo. Isso pode elevar o consumo de tokens, o custo e a latência.

Uma estratégia inicial é manter: - uma janela limitada das mensagens
mais recentes; - um resumo contextual atualizado periodicamente; - as
instruções fixas do entrevistador; - os dados relevantes da vaga e do
perfil da entrevista.

O contexto deve preservar informações importantes para a continuidade da
conversa sem incluir todo o conteúdo histórico em cada chamada.

## 5. Protocolos e estratégia de comunicação

A proposta utiliza dois mecanismos principais.

### 5.1 REST sobre HTTPS

REST é adequado para operações tradicionais, como: - criar uma
entrevista; - consultar entrevistas do usuário; - recuperar histórico; -
atualizar configurações; - finalizar uma entrevista; - consultar uma
avaliação.

Exemplos:

``` http
POST   /api/v1/interviews
GET    /api/v1/interviews
GET    /api/v1/interviews/{interview_id}
POST   /api/v1/interviews/{interview_id}/messages
POST   /api/v1/interviews/{interview_id}/finish
GET    /api/v1/interviews/{interview_id}/evaluation
```

### 5.2 Server-Sent Events (SSE) ou HTTP response streaming

Para a conversação, recomenda-se avaliar streaming. Em vez de aguardar a
resposta completa do Gemini, o backend encaminha fragmentos de texto à
medida que são recebidos.

Isso pode reduzir o **Time to First Token (TTFT)** percebido pelo
usuário, isto é, o tempo até o primeiro fragmento da resposta aparecer
na tela.

Exemplo conceitual:

``` text
Gemini -> Backend -> Frontend

Fragmento 1: "Can you"
Fragmento 2: "Can you tell me"
Fragmento 3: "Can you tell me about your experience?"
```

O streaming não reduz necessariamente o tempo total de geração do
modelo. Ele melhora a percepção de velocidade porque o usuário começa a
visualizar a resposta antes da conclusão.

**Ponto de atenção:** é necessário validar o suporte de streaming em
todo o caminho, incluindo API Gateway, Lambda, integração HTTP com o
Gemini e frontend. Devem ser conferidos os limites de duração, tamanho
de resposta, conexões e comportamento de timeout dos serviços
escolhidos. Se a combinação não atender aos requisitos, pode-se avaliar
uma conexão WebSocket ou um serviço de aplicação em containers.

### 5.3 Métricas de latência

Recomenda-se medir separadamente:

-   latência total da requisição;
-   tempo de execução da Lambda;
-   tempo de conexão e resposta do Gemini;
-   TTFT;
-   tempo até a resposta completa;
-   tempo de leitura e gravação no DynamoDB.

Essas medições ajudam a identificar se o gargalo está na aplicação, na
rede, na persistência ou no provedor de LLM.

## 6. Escalabilidade e desempenho

### 6.1 AWS Lambda

Lambda permite executar múltiplas invocações conforme a demanda, sem que
a equipe precise administrar servidores. É uma opção adequada para uma
carga variável e para uma POC que ainda não possui volume previsível.

Entretanto, a capacidade efetiva depende de: - cotas de concorrência da
conta e da região; - limites configurados para a função; - throttling do
API Gateway; - limites de requisição e tokens do Gemini; - duração das
chamadas externas; - capacidade do banco de dados.

É importante configurar alarmes e limites para evitar que um pico de
chamadas gere custos inesperados ou exceda a capacidade do provedor.

### 6.2 DynamoDB

A recomendação inicial é avaliar o DynamoDB em modo On-Demand. Esse modo
evita a necessidade de definir previamente a capacidade de leitura e
escrita para cargas variáveis.

Benefícios: - serviço gerenciado; - escalabilidade sem administração de
servidores de banco; - integração natural com Lambda; - acesso eficiente
por chave; - cobrança baseada no uso do serviço.

A modelagem deve partir dos padrões de consulta. Uma tabela inicial pode
armazenar sessões e outra mensagens, ou pode-se avaliar uma tabela única
com padrão de chave composta. A decisão depende das consultas esperadas
e deve ser documentada.

Exemplo lógico de entidades:

**InterviewSessions**

  Campo             Descrição
  ----------------- -------------------------------
  session_id        Identificador da entrevista
  user_id           Identificador do usuário
  status            Estado da entrevista
  job_position      Cargo ou função simulada
  created_at        Data de criação
  updated_at        Data da última atualização
  context_summary   Resumo contextual da conversa

**InterviewMessages**

  Campo         Descrição
  ------------- --------------------------------------
  message_id    Identificador da mensagem
  session_id    Identificador da entrevista
  role          User ou Assistant
  content       Conteúdo da mensagem
  created_at    Data da mensagem
  tokens_used   Consumo de tokens, quando disponível

A tabela de mensagens deve permitir recuperar as mensagens de uma sessão
em ordem cronológica, evitando varreduras desnecessárias.

### 6.3 Concorrência e proteção do provedor

A aplicação deve implementar: - throttling no API Gateway; - limites por
usuário; - limites de entrevistas simultâneas; - timeout nas chamadas
externas; - retry com backoff exponencial apenas para erros
transitórios; - tratamento específico para respostas de limite de taxa
do Gemini; - controle de concorrência para tarefas de avaliação; -
idempotência para operações que possam ser repetidas.

Não se deve repetir indiscriminadamente uma chamada de geração que já
pode ter sido processada pelo provedor. Uma chave de idempotência e um
estado de processamento ajudam a evitar duplicidade e cobrança
desnecessária.

## 7. Patterns e técnicas arquiteturais

Os patterns abaixo podem enriquecer a solução. Nem todos precisam ser
implementados na primeira versão.

### 7.1 Adapter Pattern --- integração com provedores de LLM

**Recomendação: adotar desde o início.**

A aplicação não deve depender diretamente dos detalhes da API do Gemini
em seus módulos de negócio.

Uma interface conceitual:

``` python
from abc import ABC, abstractmethod

class LLMProvider(ABC):

    @abstractmethod
    def generate_response(self, messages):
        pass
```

Implementações:

``` python
class GeminiProvider(LLMProvider):

    def generate_response(self, messages):
        # Integração com Google Gemini
        pass


class BedrockProvider(LLMProvider):

    def generate_response(self, messages):
        # Integração com Amazon Bedrock
        pass
```

A aplicação depende da abstração, enquanto cada adapter implementa os
detalhes específicos do provedor.

**Benefícios:** - menor acoplamento; - facilidade para substituir o
modelo; - possibilidade de comparar provedores; - testes mais simples
por meio de mocks; - centralização do tratamento de erros e diferenças
de API.

### 7.2 RAG --- Retrieval-Augmented Generation

**Recomendação: avaliar em uma fase posterior.**

RAG permite recuperar informações de uma base externa e incluí-las no
contexto enviado à LLM.

No simulador, uma base de conhecimento poderia conter: - perguntas para
entrevistas técnicas; - critérios de avaliação; - descrições de vagas; -
competências esperadas por nível; - material de apoio para avaliação de
inglês.

Fluxo conceitual:

``` mermaid
flowchart TD
    DOCS[Documentos e materiais] --> S3[Amazon S3]
    S3 --> INGEST[Processamento e chunking]
    INGEST --> EMB[Modelo de embeddings]
    EMB --> VDB[(Base vetorial)]
    Q[Solicitação do usuário] --> RET[Busca semântica]
    VDB --> RET
    RET --> CTX[Contexto recuperado]
    Q --> CTX
    CTX --> LLM[Google Gemini]
    LLM --> RESP[Resposta contextualizada]
```

Possíveis serviços e tecnologias: - Amazon S3 para documentos; - Amazon
Bedrock Knowledge Bases para uma solução gerenciada; - Amazon Aurora
PostgreSQL com pgvector; - Amazon OpenSearch Serverless para busca
vetorial; - serviço de embeddings compatível com a estratégia escolhida.

RAG não é requisito para a primeira versão. Se o simulador utiliza
apenas instruções, parâmetros da entrevista e o histórico recente, uma
chamada direta ao Gemini pode ser suficiente.

RAG passa a agregar valor quando existe uma base de conhecimento
própria, relevante e atualizável, que precisa ser consultada para
fundamentar as perguntas ou avaliações.

### 7.3 Processamento assíncrono com SQS

**Recomendação: adicionar quando existir avaliação pós-entrevista ou
outras tarefas demoradas.**

A conversação deve permanecer síncrona para que o usuário receba retorno
durante a entrevista. Já tarefas secundárias podem ser executadas em
segundo plano.

Exemplos: - avaliação gramatical detalhada; - análise de vocabulário; -
pontuação por competência; - relatório final; - geração de recomendações
de estudo.

Fluxo:

``` mermaid
flowchart TD
    FIN[Entrevista finalizada] --> API[Interview API]
    API --> SQS[Amazon SQS]
    SQS --> WORKER[Lambda Evaluation Worker]
    WORKER --> LLM[Google Gemini]
    LLM --> WORKER
    WORKER --> DB[(DynamoDB)]
    SQS -. falhas repetidas .-> DLQ[Dead Letter Queue]
```

Benefícios: - não aumenta o tempo de resposta da conversação; - permite
processar avaliações independentemente do fluxo interativo; - permite
controlar a concorrência dos workers; - oferece mecanismo de recuperação
para mensagens que falharem.

É necessário considerar que o SQS trabalha com entrega pelo menos uma
vez em cenários comuns. Portanto, o worker deve ser idempotente:
processar a mesma tarefa mais de uma vez não pode criar avaliações
duplicadas ou resultados inconsistentes.

### 7.4 Arquitetura orientada a eventos

A solução pode adotar eventos de domínio para tarefas secundárias, sem
transformar todo o sistema em uma arquitetura distribuída.

Exemplos de eventos: - `InterviewCreated`; - `InterviewFinished`; -
`EvaluationRequested`; - `EvaluationCompleted`.

Para a primeira evolução, SQS é suficiente para uma fila de tarefas.
Amazon EventBridge pode ser considerado se surgir a necessidade de
distribuir eventos para vários consumidores ou integrar outros serviços.

### 7.5 Resiliência: timeout, retry e circuit breaker

As chamadas ao provedor externo devem ter timeout explícito. Retries
devem ser limitados e utilizar backoff exponencial com jitter para
evitar rajadas de novas chamadas.

Um circuit breaker pode ser introduzido se falhas frequentes do provedor
causarem degradação em cascata. Ele interrompe temporariamente chamadas
quando um serviço está indisponível e permite tentativas controladas de
recuperação.

Não é necessário implementar um circuit breaker complexo na POC, mas a
política de falhas deve estar documentada.

## 8. Estratégia de custos

Em aplicações com LLM, o custo do modelo pode representar uma parcela
significativa do custo total. O custo real depende do modelo, volume de
tokens, tamanho do contexto, quantidade de interações e política de
preços vigente.

  Serviço       Estratégia inicial
  ------------- --------------------------------------------------------------
  Lambda        Pagamento por invocação e duração
  API Gateway   Cobrança por requisição e modalidade escolhida
  DynamoDB      On-Demand para carga variável
  S3            Armazenamento de arquivos e documentos
  CloudWatch    Retenção controlada de logs e métricas
  SQS           Utilizar para tarefas que realmente precisam ser assíncronas
  Gemini        Monitorar tokens de entrada e saída

### 8.1 Otimização de tokens

-   Limitar o tamanho das mensagens recebidas.
-   Definir limite de tokens de saída.
-   Manter uma janela controlada do histórico.
-   Resumir conversas longas.
-   Evitar repetir instruções extensas desnecessariamente.
-   Avaliar modelos de menor custo para tarefas simples.
-   Utilizar modelos mais avançados apenas quando os testes demonstrarem
    benefício.

### 8.2 Controle de sessões

-   Definir duração máxima ou regras de encerramento.
-   Expirar sessões abandonadas quando fizer sentido para o produto.
-   Evitar avaliações duplicadas.
-   Limitar entrevistas simultâneas por usuário conforme o plano de uso.

### 8.3 Métrica de custo por entrevista

Uma métrica útil é o custo total de chamadas ao modelo por entrevista:

``` text
Custo da entrevista = soma do custo de cada requisição à LLM
```

O sistema pode registrar tokens de entrada e saída, modelo utilizado,
quantidade de chamadas e identificador da entrevista. Com esses dados, é
possível estimar o custo médio por entrevista e comparar diferentes
modelos.

O custo da infraestrutura AWS também deve ser acompanhado separadamente.
Recomenda-se criar orçamento e alarmes de consumo na AWS e limites de
utilização no provedor de LLM.

## 9. Organização do código e arquitetura interna

A recomendação é começar com um **monólito modular serverless**, e não
com vários microsserviços independentes.

Exemplo de estrutura:

``` text
interview-simulator/
│
├── src/
│   ├── modules/
│   │   ├── interview/
│   │   │   ├── controller.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── conversation/
│   │   │   ├── service.py
│   │   │   └── context_manager.py
│   │   │
│   │   ├── evaluation/
│   │   │   ├── service.py
│   │   │   └── evaluator.py
│   │   │
│   │   └── llm/
│   │       ├── provider.py
│   │       └── gemini_adapter.py
│   │
│   ├── infrastructure/
│   │   ├── dynamodb/
│   │   └── secrets/
│   │
│   └── main.py
│
└── tests/
```

A separação em módulos permite manter responsabilidades claras e
facilita extrair componentes no futuro, caso exista uma necessidade real
de escalabilidade ou implantação independente.

### 9.1 Possível evolução para microsserviços

Se o produto crescer, podem ser extraídos serviços independentes:

  Serviço                Responsabilidade
  ---------------------- ------------------------------------------------
  Interview Service      Gerenciamento do ciclo de vida das entrevistas
  Conversation Service   Gerenciamento das interações e contexto
  AI Gateway Service     Integração com provedores de LLM
  Evaluation Service     Avaliação e relatórios

Essa separação é uma possibilidade futura, não um requisito da primeira
versão. Microsserviços trazem custos de comunicação, implantação,
observabilidade, segurança e consistência de dados.

## 10. Segurança e proteção de dados

Mesmo em uma POC, alguns cuidados devem estar presentes:

-   armazenar a chave do Gemini no Secrets Manager, nunca no frontend ou
    no repositório;
-   utilizar IAM com privilégio mínimo;
-   proteger endpoints com autenticação e autorização;
-   validar tamanho e formato das entradas;
-   limitar requisições por usuário;
-   não registrar tokens, segredos ou dados pessoais desnecessários nos
    logs;
-   definir política de retenção e exclusão das conversas;
-   utilizar HTTPS;
-   avaliar criptografia em repouso e em trânsito;
-   proteger a aplicação contra prompt injection e conteúdo malicioso;
-   não confiar cegamente em instruções ou documentos recuperados por
    RAG;
-   separar dados de usuários e garantir autorização nas consultas por
    sessão.

Também é importante definir quais dados da entrevista serão armazenados,
por quanto tempo e para qual finalidade.

## 11. Observabilidade

A observabilidade deve permitir acompanhar tanto a infraestrutura quanto
a experiência com a LLM.

Métricas recomendadas:

  Métrica                         Objetivo
  ------------------------------- -------------------------------------
  Requisições por minuto          Acompanhar volume
  Taxa de erro da API             Identificar falhas
  Duração da Lambda               Medir processamento interno
  Concorrência da Lambda          Identificar pressão de capacidade
  Latência do Gemini              Medir tempo do provedor
  TTFT                            Medir rapidez do primeiro fragmento
  Latência total                  Medir duração da interação
  Tokens de entrada e saída       Controlar consumo
  Custo por entrevista            Acompanhar custo do produto
  Mensagens na fila               Acompanhar tarefas pendentes
  Idade da mensagem mais antiga   Identificar atraso no processamento

Amazon CloudWatch pode centralizar logs, métricas e alarmes. É
recomendável utilizar identificadores de correlação, como `request_id` e
`interview_id`, para acompanhar uma interação entre os componentes sem
registrar conteúdo sensível desnecessário.

## 12. Comparação: Lambda versus ECS Fargate

A escolha entre Lambda e containers deve permanecer como uma decisão a
validar.

  -----------------------------------------------------------------------
  Critério                AWS Lambda              Amazon ECS Fargate
  ----------------------- ----------------------- -----------------------
  Modelo operacional      Funções sob demanda     Containers gerenciados

  Escalabilidade          Por invocação e         Por tarefas e políticas
                          concorrência            de escala

  Carga variável          Muito adequado          Adequado, mas requer
                                                  configuração

  Execução contínua       Menos adequado          Mais adequado

  Controle do runtime     Mais limitado           Maior controle

  Conexões persistentes   Exige atenção aos       Pode ser mais
                          limites                 apropriado

  Operação inicial        Geralmente mais simples Exige mais configuração

  Custos                  Favorável em carga      Pode ser favorável em
                          esporádica              carga contínua
  -----------------------------------------------------------------------

**Escolha inicial:** Lambda, por simplicidade operacional e adequação à
carga ainda desconhecida.

**Quando reconsiderar:** se houver sessões de voz contínuas, conexões
persistentes, processamento de longa duração, necessidade de controle
maior do runtime ou um perfil de tráfego que torne containers mais
econômicos.

A escolha deve ser sustentada por testes representativos, não apenas por
uma preferência tecnológica.

## 13. Roadmap de evolução

### Fase 1 --- MVP / POC

**Objetivo:** validar a experiência de entrevista.

Componentes: - API Gateway; - Lambda; - Gemini API; - DynamoDB; -
REST; - streaming, se suportado pela combinação de serviços; -
CloudWatch; - Secrets Manager.

Entregas: - criação e encerramento de entrevistas; - envio e recebimento
de mensagens; - persistência do histórico; - controle básico de
contexto; - medição de latência e tokens.

### Fase 2 --- Produto escalável

**Objetivo:** suportar crescimento e novas funcionalidades.

Componentes e capacidades: - Cognito; - CloudFront e S3; - SQS e
Evaluation Worker; - DLQ; - rate limiting; - alarmes e orçamento; -
resumo contextual de conversas; - métricas de custo por entrevista; -
políticas de retenção de dados.

### Fase 3 --- Inteligência e personalização

**Objetivo:** enriquecer a experiência de aprendizagem.

Possíveis evoluções: - RAG; - base vetorial; - avaliação
personalizada; - múltiplos provedores de LLM; - análise histórica de
desempenho; - recomendações de estudo; - integração de voz e
transcrição; - diferentes perfis de entrevistador.

## 14. Decisões arquiteturais consolidadas

  -----------------------------------------------------------------------
  Dimensão                Escolha proposta        Justificativa
  ----------------------- ----------------------- -----------------------
  Cloud provider          AWS                     Ecossistema de serviços
                                                  gerenciados

  Estilo arquitetural     Monólito modular        Simplicidade inicial e
                          serverless              evolução gradual

  Backend                 Python                  Ecossistema de IA e
                                                  integração

  API                     Amazon API Gateway      Exposição e
                                                  gerenciamento

  Compute                 AWS Lambda              Execução sob demanda

  Banco                   DynamoDB                Persistência gerenciada
                                                  e escalável

  LLM                     Google Gemini           Continuidade da POC

  Integração LLM          Adapter Pattern         Desacoplamento do
                                                  provedor

  Comunicação             REST + streaming        Operações tradicionais
                                                  e resposta progressiva

  Mensageria              SQS                     Tarefas secundárias
                                                  assíncronas

  Armazenamento           S3                      Frontend estático e
                                                  documentos

  Autenticação            Cognito                 Gerenciamento de
                                                  usuários

  Observabilidade         CloudWatch              Logs, métricas e
                                                  alarmes

  Segredos                Secrets Manager         Proteção da chave do
                                                  provedor

  Segurança               IAM, Cognito, WAF e     Controle de acesso e
                          validação de entrada    proteção
  -----------------------------------------------------------------------

## 15. Riscos, limitações e pontos a validar

A arquitetura é uma proposta inicial e precisa ser validada em relação
aos seguintes pontos:

1.  **Streaming ponta a ponta:** verificar se a modalidade escolhida do
    API Gateway e Lambda atende ao fluxo de streaming necessário,
    incluindo timeouts e limites.
2.  **Limites do Gemini:** verificar quotas, limites de tokens,
    concorrência, disponibilidade e política de preços do modelo
    selecionado.
3.  **Latência real:** medir o tempo de rede, TTFT e tempo total com
    diferentes tamanhos de contexto.
4.  **Modelagem DynamoDB:** validar os padrões de consulta e a
    estratégia de ordenação e paginação das mensagens.
5.  **Consistência e idempotência:** evitar mensagens duplicadas e
    estados inconsistentes em caso de repetição ou falha parcial.
6.  **Custos:** estimar custo por entrevista com uma quantidade
    representativa de mensagens e tokens.
7.  **Segurança e privacidade:** definir retenção, exclusão e proteção
    dos dados das conversas.
8.  **Carga e concorrência:** testar o comportamento com diferentes
    números de entrevistas simultâneas.
9.  **Fallback do provedor:** definir o comportamento da aplicação
    quando o Gemini estiver indisponível ou limitado.
10. **Voz:** se fizer parte do escopo, avaliar separadamente protocolos,
    serviços de transcrição, síntese e conexões persistentes.

## 16. Referências técnicas para aprofundamento

As referências abaixo são pontos de partida oficiais para validar os
serviços e aprofundar os conceitos. Limites, preços e recursos podem
mudar; devem ser conferidos novamente durante o detalhamento da
arquitetura.

### AWS --- Serverless e API

-   [AWS Lambda --- Developer
    Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
-   [Amazon API Gateway --- Developer
    Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
-   [Amazon API Gateway --- Response
    streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html)
-   [AWS Serverless Application Lens --- Well-Architected
    Framework](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)

### AWS --- Persistência e mensageria

-   [Amazon DynamoDB --- Developer
    Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
-   [DynamoDB --- On-demand capacity
    mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)
-   [Amazon SQS --- Developer
    Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
-   [Amazon SQS --- Dead-letter
    queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

### AWS --- Segurança e observabilidade

-   [Amazon Cognito --- Developer
    Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
-   [AWS Secrets Manager --- User
    Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
-   [Amazon CloudWatch --- User
    Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
-   [AWS Well-Architected
    Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

### AWS --- IA generativa e RAG

-   [Amazon Bedrock --- User
    Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
-   [Knowledge Bases for Amazon
    Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
-   [AWS Prescriptive
    Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/)

### Google --- Gemini

-   [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
-   [Gemini API --- Generate
    content](https://ai.google.dev/gemini-api/docs/text-generation)
-   [Gemini API --- Generate content with
    streaming](https://ai.google.dev/gemini-api/docs/text-generation#generate-a-text-stream)

### Conceitos para pesquisa

  -----------------------------------------------------------------------
  Tema                                Termos de pesquisa
  ----------------------------------- -----------------------------------
  Arquitetura serverless              Serverless Architecture, Function
                                      as a Service

  Integração com LLM                  LLM Gateway, Provider Adapter,
                                      Prompt Management

  Streaming                           Server-Sent Events, HTTP Response
                                      Streaming, Time to First Token

  RAG                                 Embeddings, Chunking, Vector
                                      Search, Retrieval-Augmented
                                      Generation

  Resiliência                         Timeout, Retry, Exponential
                                      Backoff, Circuit Breaker

  Escalabilidade                      Concurrency, Throttling,
                                      Autoscaling

  Custos                              FinOps, Token Cost Optimization,
                                      Cost per Session

  Segurança de IA                     OWASP Top 10 for LLM Applications,
                                      Prompt Injection
  -----------------------------------------------------------------------

## 17. Recomendação final

A arquitetura recomendada para iniciar é:

**AWS Serverless + API Gateway + Lambda + DynamoDB + Google Gemini**,
com streaming no fluxo conversacional quando a integração escolhida
suportar esse recurso adequadamente.

O SQS deve ser introduzido quando houver tarefas secundárias, como
avaliação pós-entrevista e geração de relatórios. RAG deve ser
considerado quando existir uma base de conhecimento própria que
justifique recuperação semântica. Microsserviços e ECS Fargate devem ser
avaliados quando requisitos reais de escala, execução contínua ou
independência de implantação justificarem a complexidade adicional.

Os principais argumentos da proposta são:

1.  baixo custo e baixa operação inicial;
2.  escalabilidade gerenciada para cargas variáveis;
3.  possibilidade de resposta progressiva para melhorar a experiência;
4.  desacoplamento entre aplicação e provedor de LLM;
5.  processamento assíncrono para tarefas que não precisam bloquear a
    conversa;
6.  evolução gradual para personalização, RAG, voz e múltiplos modelos.

A qualidade da arquitetura não depende da quantidade de serviços ou
patterns utilizados. Ela depende da adequação aos requisitos, da clareza
das decisões, da avaliação dos trade-offs e da capacidade de evoluir sem
introduzir complexidade desnecessária.

------------------------------------------------------------------------

## Apêndice --- questões em aberto para a próxima revisão

Antes de transformar esta proposta em um DAS definitivo, recomenda-se
responder:

-   O simulador será apenas texto ou também terá interação por voz?
-   O frontend será web, mobile ou ambos?
-   A entrevista precisa ser transmitida em tempo real ou uma resposta
    progressiva por SSE é suficiente?
-   Qual é o número estimado de usuários simultâneos?
-   Qual é a duração média esperada de uma entrevista?
-   O sistema precisa avaliar o inglês segundo critérios estruturados,
    como gramática, vocabulário, fluência e compreensão?
-   Existe uma base própria de perguntas, vagas e rubricas que
    justifique RAG?
-   O histórico precisa ser mantido por quanto tempo?
-   A aplicação terá diferentes perfis de usuário ou planos de
    utilização?
-   Quais metas de latência e custo por entrevista serão consideradas
    aceitáveis?

As respostas orientarão a escolha definitiva dos serviços, a modelagem
de dados, os requisitos não funcionais e os diagramas C4 e ADRs do
documento de arquitetura.
