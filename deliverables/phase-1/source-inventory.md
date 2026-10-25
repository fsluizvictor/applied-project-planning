# Inventário de Fontes — Fase 1

**Projeto:** Desafio e Solução — Simulador de Conversação em Inglês com IA  
**Fase:** 1 — Planejamento e Análise de Requisitos  
**Data:** 25 de outubro de 2026

---

## Propósito

Este documento registra todas as fontes inspecionadas durante a Fase 1, distinguindo entre fontes efetivamente acessadas e fontes esperadas mas não encontradas. Nenhuma fonte não consultada será apresentada como consultada (ver regra `01-academic-integrity.mdc`).

---

## Fontes do Harness (Arquivos Internos do Projeto)

| # | Arquivo | Localização | Status | Conteúdo relevante encontrado |
|---|---------|------------|--------|-------------------------------|
| F-01 | `AGENTS.md` | Raiz do projeto | ✅ Acessado e lido | Instruções globais, visão do projeto, 11 critérios (como placeholders), mapa de fases |
| F-02 | `PLAN.md` | Raiz do projeto | ✅ Acessado e lido | Status das fases, critérios de aceite por fase, dependências |
| F-03 | `harness.md` | Raiz do projeto | ✅ Acessado e lido | Brief original do projeto; confirma escopo e restrições do harness |
| F-04 | `phases/01_planejamento.md` | `phases/` | ✅ Acessado e lido | Instruções desta fase; lista os 11 critérios com rótulos; define entregáveis esperados |
| F-05 | `.cursor/agents/requirements-analyst.md` | `.cursor/agents/` | ✅ Acessado e lido | Responsabilidades do agente, outputs esperados, critérios de aceite da fase |
| F-06 | `templates/acceptance-check.md` | `templates/` | ✅ Acessado e lido | Template para verificação de aceite |
| F-07 | `templates/phase-handoff.md` | `templates/` | ✅ Acessado e lido | Template para handoff entre fases |
| F-08 | `templates/agent-report.md` | `templates/` | ✅ Acessado e lido | Template para relatório do agente |
| F-09 | `templates/decision-log.md` | `templates/` | ✅ Acessado e lido | Template para log de decisões |
| F-10 | `README.md` | Raiz do projeto | ✅ Acessado | Conteúdo mínimo (apenas título); sem informações adicionais |
| F-11 | `.cursor/rules/*.mdc` | `.cursor/rules/` | ✅ Aplicados como contexto | Seis arquivos de regras aplicadas automaticamente ao agente |

---

## Fontes Esperadas Mas Não Encontradas

| # | Fonte esperada | Por que era esperada | Impacto da ausência |
|---|---------------|---------------------|---------------------|
| M-01 | PDF de instruções da disciplina | `phases/01_planejamento.md` instrui "localize e leia as instruções da disciplina e o PDF de exemplo" | Os critérios de avaliação são conhecidos apenas pelos rótulos; descritores de desempenho desconhecidos |
| M-02 | PDF de exemplo de proposta aprovada | `phases/01_planejamento.md` instrui leitura de um PDF de exemplo | Sem referência de formato, estilo e extensão esperados |
| M-03 | Rubrica completa de avaliação | Necessária para mapear descritores dos 11 critérios | Mapeamento de critérios é parcial — baseado apenas nos rótulos |
| M-04 | Informações da disciplina (nome, instituição, semestre) | Contextualização acadêmica básica | Contextualização incompleta da proposta |

> **Ação requerida:** O usuário (Luiz) deve fornecer os documentos M-01 a M-04 antes que a proposta possa ser finalizada com segurança. Esses documentos podem ser adicionados ao workspace em qualquer momento antes da Fase 7.

---

## Fontes Bibliográficas Externas

Nenhuma fonte bibliográfica externa foi consultada na Fase 1. A pesquisa bibliográfica é escopo da **Fase 2** (Context Researcher).

---

## Registro de Integridade

- Nenhuma fonte foi citada sem ter sido efetivamente acessada.
- Nenhuma informação foi inferida de fontes não disponíveis sem sinalização explícita de `[ASSUMPTION]` ou `[LACUNA DE EVIDÊNCIA]`.
