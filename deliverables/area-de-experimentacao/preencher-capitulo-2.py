#!/usr/bin/env python3
"""Completa o capítulo 2 do Relatório do Projeto Aplicado no .docx da XP."""

from __future__ import annotations

import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

SRC = Path("/home/luiz-victor/Downloads/Relatório_Projeto_Aplicado_Luiz_Victor.docx")
OUT_DOWNLOADS = SRC
OUT_REPO = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "Relatorio_Projeto_Aplicado_Luiz_Victor.docx"
)
BACKUP = SRC.with_name("Relatório_Projeto_Aplicado_Luiz_Victor.backup.docx")
ASSETS = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/area-de-experimentacao/assets"
)

INK = RGBColor(0x1A, 0x1F, 0x20)
GREEN = RGBColor(0x00, 0xB0, 0x50)
BLUE = RGBColor(0x2A, 0x30, 0xB0)


def _spacing(paragraph, after="240", before="240", line="360") -> None:
    pPr = paragraph._p.get_or_add_pPr()
    spacing = pPr.find(qn("w:spacing"))
    if spacing is None:
        spacing = OxmlElement("w:spacing")
        pPr.append(spacing)
    spacing.set(qn("w:after"), after)
    spacing.set(qn("w:before"), before)
    spacing.set(qn("w:line"), line)
    spacing.set(qn("w:lineRule"), "auto")


def _run(paragraph, text, *, bold=False, italic=False, color=INK, size=None) -> None:
    run = paragraph.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color
    if size is not None:
        run.font.size = size
    rPr = run._r.get_or_add_rPr()
    rtl = OxmlElement("w:rtl")
    rtl.set(qn("w:val"), "0")
    rPr.append(rtl)


def body(doc, text, *, bold=False, italic=False) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(p)
    _run(p, text, bold=bold, italic=italic)


def heading(doc, text, level: int, color=GREEN) -> None:
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        run.font.color.rgb = color


def caption(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(p, after="240", before="120", line="276")
    _run(p, text, italic=False)


def picture(doc, path: Path, width_cm: float = 15.0) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(p, after="80", before="160", line="240")
    p.add_run().add_picture(str(path), width=Cm(width_cm))


def item_title(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(p, after="80", before="200", line="360")
    _run(p, text, bold=True)


def replace_cronograma(doc: Document) -> None:
    old = "Nenhuma sprint foi executada até esta data."
    new = (
        "As Sprints 1 e 2 foram executadas; a Sprint 3 permanece pendente. "
        "O detalhe da execução está no capítulo 2."
    )
    for p in doc.paragraphs:
        if old not in p.text:
            continue
        for run in p.runs:
            if old in run.text:
                run.text = run.text.replace(old, new)
                return
        joined = "".join(run.text for run in p.runs)
        if old in joined and p.runs:
            p.runs[0].text = joined.replace(old, new)
            for run in p.runs[1:]:
                run.text = ""
            return


def fill(doc: Document) -> None:
    doc.add_page_break()

    heading(doc, "2. Área de Experimentação", 1, BLUE)
    body(
        doc,
        "A área de experimentação registra o planejamento, a execução e o resultado "
        "das sprints da prova de conceito. O quadro Kanban previsto no escopo foi "
        "materializado no GitHub Projects do repositório poc-en-simulator, uma issue "
        "por entrega, com as etiquetas sprint-1 e sprint-2, conforme a Figura 11. "
        "As Sprints 1 e 2 foram executadas. A Sprint 3 permanece reservada à "
        "sessão-piloto, à nota de privacidade e ao Documento de Arquitetura de "
        "Software (DAS) na versão 1.",
    )

    # ----- Sprint 1 -----
    heading(doc, "2.1 Sprint 1 — Base do fluxo e escolha da tecnologia", 3)
    body(
        doc,
        "Período: 2 a 8 de novembro de 2026. As entregas foram registradas em "
        "10 de novembro de 2026. O objetivo desta sprint foi fechar o que seria "
        "construído e escolher uma combinação gratuita entre as alternativas do "
        "escopo, de modo que a sprint seguinte implementasse o fluxo em vez de "
        "continuar a pesquisa de ferramentas.",
    )

    heading(doc, "2.1.1 Solução", 4)
    heading(doc, "Evidência do planejamento:", 4)
    body(
        doc,
        "A Sprint 1 foi planejada com quatro entregas, correspondentes às issues 1 a 4 "
        "do repositório. A definição da sprint consta da Figura 8. O quadro de "
        "acompanhamento consta da Figura 11. Issues: "
        "https://github.com/fsluizvictor/poc-en-simulator/issues/1 a /issues/4.",
    )

    heading(doc, "Evidência da execução de cada requisito:", 4)

    item_title(doc, "1. Lista de requisitos do fluxo único")
    body(
        doc,
        "Redigiu-se o fluxo único da prova de conceito: um cenário de entrevista de "
        "emprego na área de tecnologia, captura de voz, resposta oral da "
        "entrevistadora e retorno ao encerrar, em três blocos. O documento fecha oito "
        "requisitos funcionais (RF-01 a RF-08) e seis restrições (RNF-01 a RNF-06). "
        "Ficaram fora do fluxo a medição de fluência, a correção durante a conversa, "
        "o cadastro, o banco de dados, o canal bidirecional contínuo e a publicação "
        "em nuvem como condição de conclusão.",
    )

    item_title(doc, "2. Registro da combinação tecnológica, com teste curto da própria voz")
    body(
        doc,
        "Entre as alternativas do escopo, registrou-se a combinação: interface em "
        "React, na máquina local; API em Python 3.12, no padrão Backend for Frontend "
        "(BFF); reconhecimento gemini-3.5-transcribe em modo VERBATIM; diálogo e "
        "retorno gemini-3.5-flash-lite; síntese gemini-3.8-flash-lite-tts, voz Kore. "
        "Afastaram-se a API contínua de áudio (Live API), o modo SMART de transcrição "
        "e a variante de síntese de estúdio.",
    )
    body(
        doc,
        "Em 10 de novembro de 2026 a chave foi usada só no ambiente do processo. O que "
        "a chave aceitou: o modelo de diálogo gerou a abertura da entrevistadora; a "
        "síntese gerou áudio WAV reproduzível pela chamada REST generateContent; o "
        "reconhecimento aceitou o áudio e, sem fala inteligível, devolveu candidato "
        "vazio. O que falhou, e ficou registrado de propósito: a interface "
        "interactions não encontrou o modelo de síntese; o SDK google-genai 3.1.0 "
        "montou speechConfig de um jeito que a API recusou; a captura de oito segundos "
        "não continha uma resposta falada.",
    )

    item_title(doc, "3. Instruções de sistema do entrevistador e do feedback")
    body(
        doc,
        "Escreveram-se duas instruções distintas. A da entrevistadora, em inglês, "
        "impede correção, nota ou comentário pedagógico no meio do turno. A do "
        "retorno, em português brasileiro, pede somente três blocos e manda declarar "
        "amostra insuficiente quando a transcrição for curta ou ininteligível. O "
        "modelo de transcrição não recebe essas instruções.",
    )

    item_title(doc, "4. Documento de Arquitetura de Software (DAS) parcial")
    body(
        doc,
        "Redigiu-se a versão 0.1 do DAS, com contexto, contêineres previstos em texto, "
        "premissas, restrições e decisões. Os diagramas de contexto, de contêineres e "
        "de sequência ficaram para a Sprint 2. A versão não afirma que o fluxo já "
        "funcionava.",
    )

    heading(doc, "Evidência dos resultados:", 4)

    item_title(doc, "1. Lista de requisitos")
    body(
        doc,
        "O fluxo único ficou fechado. Requisitos funcionais: RF-01 (cenário único), "
        "RF-02 (captura pelo microfone), RF-03 (transcrição suficiente para o diálogo "
        "continuar), RF-04 (fala da entrevistadora sem correção), RF-05 (síntese e "
        "reprodução), RF-06 (retorno em três blocos), RF-07 (histórico só em memória) "
        "e RF-08 (chave fora do navegador).",
    )

    item_title(doc, "2. Combinação tecnológica")
    body(
        doc,
        "A combinação da Sprint 2 ficou escolhida. O teste curto validou diálogo e "
        "síntese. A transcrição veio vazia: o microfone não captou uma frase falada. "
        "Esse teste não é evidência de reconhecimento de sotaque brasileiro.",
    )
    body(
        doc,
        "Abertura gerada: “Hi there, welcome! Could you please introduce yourself and "
        "tell me a bit about your background in software development?” Transcrição da "
        "resposta: [vazia].",
    )

    item_title(doc, "3. Instruções de sistema")
    body(
        doc,
        "As duas instruções canônicas passaram a ser lidas pelo teste de voz e, na "
        "Sprint 2, pela API local.",
    )

    item_title(doc, "4. DAS parcial")
    body(
        doc,
        "O documento descreveu o contexto local, as premissas P-01 a P-04 e as "
        "restrições RC-01 a RC-09. Observação de ambiente em 10 de novembro de 2026: "
        "o computador expunha o dispositivo de captura ALC257 Analog. A transcrição "
        "de uma frase falada de propósito permaneceu pendente.",
    )

    heading(doc, "2.1.2 Lições Aprendidas", 3)
    body(
        doc,
        "1. Lista de requisitos. Fechar o fluxo antes de implementar evitou acrescentar "
        "cenário, cadastro ou banco na sprint seguinte. A lista também deixou explícito "
        "que o turno é uma requisição HTTP local, o que afastou a tentação de usar a "
        "Live API.",
    )
    body(
        doc,
        "2. Combinação tecnológica. A camada gratuita do provedor único atendeu diálogo "
        "e síntese. O SDK oficial não foi caminho suficiente para a síntese: a chamada "
        "REST com responseModalities AUDIO e speechConfig.voiceConfig.voice = Kore foi "
        "a que devolveu audio/wav. Essa rota REST ficou como restrição de implementação "
        "da Sprint 2.",
    )
    body(
        doc,
        "3. Teste curto de voz. Uma captura de oito segundos sem frase falada de "
        "propósito produz transcrição vazia. O procedimento da sprint seguinte passou "
        "a exigir o pedido explícito de uma frase em inglês e a proibição de repetir a "
        "chamada até aparecer um texto apresentável.",
    )
    body(
        doc,
        "4. DAS parcial. Sem os diagramas, o documento descreveu os contêineres só em "
        "texto. A Sprint 2 precisou incorporar contexto, contêineres e sequência no "
        "mesmo arquivo, em vez de abrir um DAS novo.",
    )

    # ----- Sprint 2 -----
    heading(doc, "2.2 Sprint 2 — Prova de conceito local", 3)
    body(
        doc,
        "Período: 9 a 15 de novembro de 2026. As entregas foram implementadas em "
        "15 de novembro de 2026. O objetivo desta sprint foi fazer o fluxo funcionar "
        "na máquina local, do cenário de entrevista até o retorno em três blocos, "
        "sem persistir áudio nem transcrição.",
    )

    heading(doc, "2.2.1 Solução", 4)
    heading(doc, "Evidência do planejamento:", 4)
    body(
        doc,
        "A Sprint 2 foi planejada com quatro entregas, correspondentes às issues 5 a 8. "
        "A definição da sprint consta da Figura 9. O quadro de acompanhamento consta "
        "da Figura 11. Não se reabriu a Sprint 1 e não se iniciou a Sprint 3. Não houve "
        "publicação em nuvem, banco, cadastro, histórico em disco, canal bidirecional "
        "contínuo, segundo cenário, correção durante a conversa nem medida de fluência. "
        "Issues: https://github.com/fsluizvictor/poc-en-simulator/issues/5 a /issues/8.",
    )

    heading(doc, "Evidência da execução de cada requisito:", 4)

    item_title(doc, "1. Interface local do cenário de entrevista")
    body(
        doc,
        "Implementou-se uma tela em React, servida em http://127.0.0.1:5173. O único "
        "cenário exibido é “Entrevista de emprego — Tecnologia”. Não há seletor de "
        "cenário, cadastro nem segundo fluxo. A tela captura o microfone, envia o "
        "áudio à API local, reproduz a voz da entrevistadora e, ao encerrar, mostra "
        "os três blocos. A chave do modelo não entra no navegador: as chamadas da "
        "interface vão só para /api na máquina local.",
    )
    picture(doc, ASSETS / "interface-local.png", 15.0)
    caption(doc, "Figura 12 — Interface local, cenário único")

    item_title(doc, "2. API local do turno de voz")
    body(
        doc,
        "Implementou-se a API em Python 3.12, no padrão BFF, em http://127.0.0.1:8765. "
        "Cada turno é uma requisição síncrona: o áudio entra; reconhecimento, diálogo "
        "e síntese ocorrem na mesma requisição; texto e áudio da entrevistadora saem. "
        "A chave GEMINI_API_KEY permanece no ambiente do processo. O histórico textual "
        "fica só em memória. O áudio do usuário é lido, enviado ao reconhecimento e "
        "descartado; a aplicação não grava arquivo de áudio nem transcrição em disco.",
    )
    body(
        doc,
        "Modelos utilizados, conforme a combinação da Sprint 1: reconhecimento "
        "gemini-3.5-transcribe, modo VERBATIM, idioma sugerido en-US, sem instrução de "
        "sistema; diálogo gemini-3.5-flash-lite, com a instrução da entrevistadora; "
        "síntese gemini-3.8-flash-lite-tts, pela chamada REST generateContent, voz Kore; "
        "retorno gemini-3.5-flash-lite, em uma segunda chamada, só no encerramento. "
        "Rotas: POST /api/sessions (abertura), POST /api/sessions/{id}/turns (áudio do "
        "turno), POST /api/sessions/{id}/end (três blocos) e GET /api/health (indica se "
        "a chave está configurada, sem expô-la).",
    )

    item_title(doc, "3. Feedback em três blocos")
    body(
        doc,
        "O encerramento não reutiliza a instrução da entrevistadora. A API apaga a "
        "sessão da memória e chama o modelo com a transcrição acumulada e a instrução "
        "de retorno. A correção não ocorre no meio da conversa: a entrevistadora, "
        "diante de transcrição vazia, pediu que a pessoa repetisse em uma frase curta, "
        "sem mencionar reconhecimento de fala.",
    )

    item_title(doc, "4. Diagramas de contexto, contêineres e sequência")
    body(
        doc,
        "Os três diagramas foram incorporados ao DAS parcial já existente, que passou "
        "à versão 0.2. Não se abriu um DAS novo. A sessão-piloto e a nota de "
        "privacidade continuam fora desta versão.",
    )

    heading(doc, "Evidência dos resultados:", 4)

    item_title(doc, "1. Interface local")
    body(
        doc,
        "A tela abriu na máquina local com um único cenário, conforme a Figura 12. "
        "Após “Iniciar entrevista”, a API devolveu a fala da entrevistadora e o áudio "
        "correspondente, reproduzido na própria tela (nove segundos na verificação de "
        "15 de novembro de 2026). Os botões “Gravar resposta” e “Encerrar sessão” "
        "ficam habilitados só depois da abertura.",
    )
    body(
        doc,
        "Fala observada na abertura pela interface: “Welcome to the interview, and "
        "thanks for taking the time to chat today. Could you briefly introduce "
        "yourself and share a bit about your experience with software development?”",
    )

    item_title(doc, "2. API local do turno")
    body(
        doc,
        "Em 15 de novembro de 2026, GET /api/health devolveu ok e key_configured "
        "verdadeiros, sem a chave. POST /api/sessions devolveu identificador de "
        "sessão, texto da entrevistadora e áudio audio/wav (309.148 bytes na primeira "
        "abertura verificada). POST /api/sessions/{id}/turns recebeu o áudio da "
        "captura e devolveu texto e áudio. Nenhum arquivo de áudio novo foi gravado "
        "no repositório. A porta 8000 já estava ocupada por outro serviço na máquina; "
        "a API local passou a escutar na porta 8765.",
    )
    body(
        doc,
        "No primeiro turno real pediu-se, em voz alta, a frase em inglês “I am a "
        "software engineer and I work with Python and web APIs.” A captura durou dez "
        "segundos e não foi repetida. Transcrição: [vazia]. Nenhuma frase foi "
        "inventada. Fala seguinte da entrevistadora: “Could you say that again in one "
        "short sentence?” Este resultado não afirma reconhecimento de sotaque "
        "brasileiro e não confirma que a frase pedida tenha sido dita no microfone. "
        "O áudio da pessoa foi apagado ao fim da captura.",
    )

    item_title(doc, "3. Feedback em três blocos")
    body(
        doc,
        "A segunda chamada ao modelo devolveu somente os três blocos pedidos. O texto "
        "abaixo é o que o modelo gerou, conservado como foi devolvido. O primeiro "
        "bloco atribuiu participação ao candidato sem citar uma frase dita por ele; "
        "isso é limitação do modelo, não evidência de fala reconhecida.",
    )
    body(doc, "Pontos positivos:", bold=True)
    body(
        doc,
        "O candidato participou da simulação e respondeu prontamente ao pedido do "
        "entrevistador (“Could you say that again in one short sentence?”).",
    )
    body(doc, "Pontos de melhoria:", bold=True)
    body(
        doc,
        "A amostra fornecida é insuficiente, pois o candidato não deu uma resposta "
        "para a primeira pergunta (“Could you briefly introduce yourself and tell me "
        "a bit about your experience with software development?”), o que impede a "
        "avaliação de estrutura de frases e adequação para uma entrevista de emprego.",
    )
    body(doc, "Próximo passo:", bold=True)
    body(
        doc,
        "Grave novamente uma resposta completa de uma frase para a pergunta de "
        "apresentação e experiência em desenvolvimento de software.",
    )

    item_title(doc, "4. Diagramas no DAS")
    body(
        doc,
        "Os três diagramas passaram a constar do mesmo documento. As Figuras 13 a 15 "
        "reproduzem o contexto, os contêineres e a sequência de um turno. Não há banco "
        "de dados, fila nem canal bidirecional contínuo.",
    )
    picture(doc, ASSETS / "contexto.png", 15.0)
    caption(doc, "Figura 13 — Diagrama de contexto")
    picture(doc, ASSETS / "conteineres.png", 12.5)
    caption(doc, "Figura 14 — Diagrama de contêineres")
    picture(doc, ASSETS / "sequencia-turno.png", 15.8)
    caption(doc, "Figura 15 — Diagrama de sequência de um turno")

    heading(doc, "2.2.2 Lições Aprendidas", 3)
    body(
        doc,
        "1. Interface local. Uma tela basta para o fluxo. O cenário único precisa "
        "aparecer como rótulo, não como lista de escolha: qualquer seletor sugeriria "
        "um segundo cenário que o escopo exclui. A reprodução automática da voz da "
        "entrevistadora depende do clique em “Iniciar entrevista”; o controle de áudio "
        "na tela cobre o caso em que o navegador bloqueia o autoplay.",
    )
    body(
        doc,
        "2. API local do turno. Isolar a chave no processo da API atendeu RF-08. A "
        "porta 8000 não estava livre nesta máquina; a prova de conceito local não exige "
        "porta canônica, desde que interface e API permaneçam em 127.0.0.1. A rota REST "
        "de síntese da Sprint 1 repetiu-se com sucesso. O reconhecimento devolveu "
        "transcrição vazia pela segunda vez; a captura não foi repetida para obter um "
        "texto apresentável. Sem frase reconhecida, o critério RF-03 permanece sem "
        "evidência positiva. A entrevistadora, ainda assim, manteve o papel e pediu "
        "que a pessoa repetisse, o que permite o fluxo continuar mesmo com transcrição "
        "vazia.",
    )
    body(
        doc,
        "3. Feedback em três blocos. A segunda chamada, com outra instrução, devolveu "
        "os três cabeçalhos e não acrescentou um quarto bloco. A instrução pede que se "
        "declare amostra insuficiente quando não houver frase do candidato; o modelo, "
        "mesmo assim, preencheu “pontos positivos” com participação inferida. Para a "
        "sessão-piloto da Sprint 3, esse desvio precisa ser lido como limitação do "
        "retorno, não como avaliação da fala.",
    )
    body(
        doc,
        "4. Diagramas. Incorporar os três desenhos no DAS parcial evitou um documento "
        "paralelo. A versão continua 0.2 e parcial: a sessão-piloto de cinco a dez "
        "minutos, a nota de privacidade fechada e o DAS na versão 1 pertencem à "
        "Sprint 3. A publicação em nuvem não foi feita e não é condição para encerrar "
        "esta sprint.",
    )

    # ----- Sprint 3 -----
    heading(doc, "2.3 Sprint 3 — Sessão-piloto e fechamento do DAS", 3)
    body(
        doc,
        "Período planejado: 16 a 22 de novembro de 2026. Esta sprint ainda não foi "
        "executada. Não há registro de sessão-piloto, nota de privacidade fechada, "
        "DAS na versão 1 nem publicação em nuvem a anexar.",
    )
    heading(doc, "2.3.1 Solução", 4)
    heading(doc, "Evidência do planejamento:", 4)
    body(
        doc,
        "A definição da Sprint 3 consta da Figura 10. O quadro de acompanhamento "
        "consta da Figura 11. As quatro entregas previstas são: registro da "
        "sessão-piloto de cinco a dez minutos, com ao menos quatro turnos de fala "
        "reconhecidos; nota de privacidade; DAS versão 1; publicação em nuvem somente "
        "se as três entregas anteriores estiverem concluídas e ainda houver tempo.",
    )
    heading(doc, "Evidência da execução de cada requisito:", 4)
    body(doc, "A preencher após a execução.", italic=True)
    heading(doc, "Evidência dos resultados:", 4)
    body(
        doc,
        "A preencher após a execução. A publicação em nuvem só é evidência se tiver "
        "sido feita. Não se antecipam números da sessão-piloto.",
        italic=True,
    )
    heading(doc, "2.3.2 Lições Aprendidas", 3)
    body(doc, "A preencher após a execução.", italic=True)


def main() -> None:
    if not BACKUP.exists():
        shutil.copy2(SRC, BACKUP)
    doc = Document(str(SRC))
    replace_cronograma(doc)
    fill(doc)
    OUT_REPO.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT_REPO))
    shutil.copy2(OUT_REPO, OUT_DOWNLOADS)
    print(f"backup: {BACKUP}")
    print(f"salvo: {OUT_DOWNLOADS}")
    print(f"cópia: {OUT_REPO}")


if __name__ == "__main__":
    main()
