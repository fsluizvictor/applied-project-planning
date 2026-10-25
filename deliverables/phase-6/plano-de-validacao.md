# Plano de Validação — Fase 6: Solução SMART e Validação

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA
**Agente responsável:** Solution Specifier
**Data:** 25 de outubro de 2026
**Versão:** 1.0

---

## 1. Objetivo da Validação

Testar a hipótese H-01: um protótipo de simulador de conversação por voz com IA, baseado no cenário de entrevista de emprego em inglês (área de tecnologia), será considerado **útil e utilizável** pelo público-alvo e reduzirá a **ansiedade de fala autorrelatada** em comparação ao estado inicial, em ao menos uma sessão de teste supervisionada.

---

## 2. Separação de Métricas

> **Distinção obrigatória** — não confundir os dois tipos de métrica:

| Tipo | Métricas incluídas neste teste | Métricas NÃO incluídas neste teste |
|------|-------------------------------|-----------------------------------|
| **Usabilidade e Aceitação** | SUS, taxa de conclusão, satisfação, percepção de utilidade, percepção de ansiedade pré/pós | ← Métricas válidas para este protótipo |
| **Aprendizagem de idioma** | Fluência, proficiência oral, ganho de vocabulário | ← Requerem estudo longitudinal com grupos experimental e controle; inviáveis em uma sessão |

---

## 3. Perfil dos Participantes

| Critério | Descrição |
|----------|-----------|
| **Perfil-alvo** | Profissionais ou estudantes de tecnologia da informação, com inglês de nível intermediário, que precisam ou desejam praticar inglês para entrevistas de emprego (correspondência com persona Ana Souza) |
| **Número de participantes** | 5 a 8 `[ALVO PROVISÓRIO — D-02]` — padrão para testes de usabilidade exploratórios (Nielsen, 1994) |
| **Critérios de inclusão** | Inglês intermediário (autorrelato); tem necessidade de praticar para entrevistas em inglês; dispõe de dispositivo com microfone e internet estável |
| **Critérios de exclusão** | Fluência avançada (não representa o público-alvo); sem microfone disponível; impossibilidade de consentir |
| **Recrutamento** | `[ASSUMPTION — requires validation — D-05]` — método de recrutamento a definir com o orientador (ex.: colegas de turma, LinkedIn, redes profissionais) |

---

## 4. Tarefas de Teste

| # | Tarefa | Objetivo |
|---|--------|----------|
| T-01 | Completar o fluxo de seleção de cenário e iniciar a conversa sem assistência do moderador | Medir navegabilidade e clareza da interface (RF-01) |
| T-02 | Conduzir uma simulação de entrevista de emprego de 5 a 10 minutos, respondendo às perguntas da IA por voz | Medir usabilidade do fluxo principal (RF-02 a RF-05) e coletar dados para a escala de ansiedade |
| T-03 | Ler e interpretar o feedback pós-conversa sem assistência | Medir clareza e utilidade percebida do feedback (RF-06) |

---

## 5. Instrumentos de Coleta

### 5.1 Escala de Ansiedade de Fala (pré e pós sessão)

Adaptação de escala Likert de 5 pontos, aplicada **antes** de iniciar a conversa e **depois** de receber o feedback:

| # | Afirmação | Escala |
|---|-----------|--------|
| 1 | "Sinto ansiedade ao ter que falar inglês em uma situação de pressão (ex.: entrevista)." | 1 (Discordo totalmente) → 5 (Concordo totalmente) |
| 2 | "Tenho medo de cometer erros ao falar inglês na frente de outras pessoas." | 1 → 5 |
| 3 | "Neste momento, me sinto confiante para ter uma conversa em inglês." | 5 → 1 (invertida) |

> Forma pós-sessão adiciona: "A sessão com o simulador **reduziu** minha ansiedade em comparação ao início." (1 → 5)

> `[ALVO PROVISÓRIO]`: Esta escala é uma proposta simplificada. O orientador pode recomendar instrumento validado como a FLSAS (Horwitz; Horwitz; Cope, 1986) ou o PSSI (Speaking Self-Confidence Scale). Se instrumentos validados forem exigidos, substituir esta proposta.

---

### 5.2 System Usability Scale (SUS)

O SUS é um questionário de 10 itens de domínio público (Brooke, 1996), com escala Likert de 1 a 5, aplicado **após a sessão**. Pontuação final de 0 a 100:

- **≥ 68:** usabilidade aceitável (benchmark padrão da literatura)
- **≥ 80:** boa usabilidade
- **< 68:** problemas de usabilidade a investigar

Os 10 itens do SUS serão utilizados sem modificação.

---

### 5.3 Questionário de Percepção Pós-Sessão

3 questões abertas aplicadas após o SUS:

1. "O que você achou mais útil nesta experiência?"
2. "O que te incomodou ou dificultou durante a conversa com a IA?"
3. "Você usaria uma ferramenta como esta para praticar inglês? Por quê (não)?"

---

### 5.4 Observação do Moderador

Durante o teste, o moderador registra:
- Momentos de hesitação ou confusão (sem intervir)
- Falhas técnicas (ASR não entende; IA responde de forma incoerente; latência muito alta)
- Comportamentos de abandono ou desistência

---

## 6. Protocolo do Teste

| Etapa | Duração estimada | Descrição |
|-------|-----------------|-----------|
| Apresentação e consentimento | 5 min | Moderador explica o propósito do teste (validar o protótipo, não avaliar o inglês do participante); participante assina/aceita termo de consentimento |
| Escala de ansiedade pré-sessão | 3 min | Participante responde as 3 questões da escala antes de interagir com o protótipo |
| Sessão de teste (Tarefas T-01 a T-03) | 15–25 min | Participante realiza as tarefas; moderador observa sem intervir |
| SUS + Questionário de percepção | 5–10 min | Aplicados logo após a sessão |
| Escala de ansiedade pós-sessão | 3 min | Participante responde novamente as mesmas 3 questões + questão adicional |
| Debriefing opcional | 5 min | Moderador pergunta se o participante tem comentários adicionais |
| **Total por participante** | **~36–51 min** | |

---

## 7. Critérios de Decisão

| Resultado | Interpretação | Próxima ação |
|-----------|--------------|--------------|
| SUS ≥ 68 + Taxa de conclusão ≥ 60% + Maioria relata redução de ansiedade | H-01 suportada — protótipo tem potencial | Iterar com base no feedback; considerar expandir para outros cenários |
| SUS ≥ 68 mas ansiedade não reduz (ou aumenta) | H-01 parcialmente refutada — usabilidade OK, mas abordagem de baixa pressão precisa ser revisada | Revisar design do feedback e da interação antes de nova rodada de testes |
| SUS < 68 | Problema grave de usabilidade — H-01 não pode ser avaliada adequadamente | Corrigir problemas de usabilidade e repetir o teste |
| Falhas técnicas graves em > 50% das sessões (ASR, latência) | Risco R-01/R-05 materializado | Revisar escolha de tecnologia antes de repetir o teste |

---

## 8. Limitações do Plano de Validação

| Limitação | Impacto |
|-----------|---------|
| Amostra pequena (5–8 participantes) | Resultados não são generalizáveis; são evidências exploratórias |
| Sem grupo controle | Impossível isolar o efeito do simulador de outros fatores |
| Ansiedade autorrelatada pode ser afetada por efeito de novidade | Redução de ansiedade pode ser temporária — não implica efeito sustentado |
| Única sessão | Não detecta aprendizagem ou efeitos de longo prazo |
| Recrutamento de conveniência | Pode introduzir viés de seleção |

> Estas limitações não invalidam o teste — são adequadas para um teste exploratório de protótipo. Devem ser declaradas na proposta final para manter a integridade acadêmica.
