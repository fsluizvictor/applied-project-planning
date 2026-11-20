#!/usr/bin/env python3
"""Gera o relatório com o capítulo 2 e os pontos de inserção das evidências.

Parte do backup do capítulo 1 (figuras 1 a 11 já inseridas) e acrescenta a
área de experimentação. Quadros amarelos são capturas novas. Quadros azuis
recebem a mesma imagem de uma figura já numerada.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BACKUP = Path(
    "/home/luiz-victor/Downloads/Relatório_Projeto_Aplicado_Luiz_Victor.backup.docx"
)
OUT = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "Relatorio_Projeto_Aplicado_Sprint_2_evidencias.docx"
)
ASSETS = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "area-de-experimentacao/assets"
)

INK = RGBColor(0x1A, 0x1F, 0x20)
GREEN = RGBColor(0x00, 0xB0, 0x50)
BLUE = RGBColor(0x2A, 0x30, 0xB0)
RED = RGBColor(0xA9, 0x32, 0x26)
AMBER_TEXT = RGBColor(0x6E, 0x4B, 0x00)
NAVY = RGBColor(0x1A, 0x36, 0x5D)

REPO = "https://github.com/fsluizvictor/poc-en-simulator"
C1 = "95a4f57"
C2 = "648013e"


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


def body(doc, text, *, bold=False, italic=False, color=INK) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(p)
    _run(p, text, bold=bold, italic=italic, color=color)


def heading(doc, text, level: int, color=GREEN) -> None:
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        run.font.color.rgb = color


def caption(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(p, after="240", before="80", line="276")
    _run(p, text, bold=True, size=Pt(11))


def item_title(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(p, after="80", before="200", line="360")
    _run(p, text, bold=True)


def picture(doc, path: Path, width_cm: float) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(p, after="40", before="160", line="240")
    p.add_run().add_picture(str(path), width=Cm(width_cm))


def _shade(cell, fill: str) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def _borders(table, color: str) -> None:
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "12")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.append(borders)
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:type"), "pct")
    tblW.set(qn("w:w"), "5000")


def _box(doc, fill: str, border: str, lines: list[tuple[str, bool]]) -> None:
    table = doc.add_table(rows=1, cols=1)
    _borders(table, border)
    cell = table.cell(0, 0)
    _shade(cell, fill)
    for index, (text, is_bold) in enumerate(lines):
        paragraph = cell.paragraphs[0] if index == 0 else cell.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
        _spacing(paragraph, after="60", before="40", line="276")
        color = AMBER_TEXT if fill == "FFF4D6" else NAVY
        _run(paragraph, text, bold=is_bold, color=color, size=Pt(11))
    spacer = doc.add_paragraph()
    _spacing(spacer, after="0", before="0", line="20")


def insert_print(doc, number: int, where: str, show: str, hide: str) -> None:
    _box(
        doc,
        "FFF4D6",
        "B9770E",
        [
            (f"INSERIR PRINT — Figura {number}", True),
            (f"Abrir: {where}", False),
            (f"A imagem precisa mostrar: {show}", False),
            (f"Não mostrar: {hide}", False),
            (
                "Depois de colar a imagem, apague este texto. Mantenha a legenda abaixo.",
                False,
            ),
        ],
    )


def text_field(doc, title: str, hint: str) -> None:
    _box(
        doc,
        "F4F6F7",
        "566573",
        [
            (title, True),
            (hint, False),
        ],
    )


def same_print(doc, number: int) -> None:
    _box(
        doc,
        "D6EAF8",
        "1A5276",
        [
            (f"COLE A MESMA CAPTURA DA FIGURA {number}", True),
            (
                "Não tire outro print. Use a imagem já colocada naquela figura. "
                "Apague este texto depois de colar. Não crie legenda nova.",
                False,
            ),
        ],
    )


def blob(commit: str, path: str) -> str:
    return f"{REPO}/blob/{commit}/{path}"


def replace_cronograma(doc: Document) -> None:
    old = "Nenhuma sprint foi executada."
    new = "O detalhe das três sprints está no capítulo 2."
    for paragraph in doc.paragraphs:
        if old not in paragraph.text:
            continue
        for run in paragraph.runs:
            if old in run.text:
                run.text = run.text.replace(old, new)
                return
        joined = "".join(run.text for run in paragraph.runs)
        if old in joined and paragraph.runs:
            paragraph.runs[0].text = joined.replace(old, new)
            for run in paragraph.runs[1:]:
                run.text = ""
            return
    raise SystemExit("Frase do cronograma não encontrada no backup.")


def instructions(doc: Document) -> None:
    heading(doc, "Instruções de preenchimento — apagar este bloco antes do envio", 1, RED)
    body(
        doc,
        "Este bloco não faz parte do relatório. Apague-o, do título vermelho até a "
        "linha de fim, antes de enviar ao orientador. O capítulo 1 permanece como "
        "está, com as Figuras 1 a 11. Os quadros amarelos são capturas novas. Os "
        "quadros azuis recebem a mesma imagem, sem novo print. Os quadros cinza "
        "são campos de texto: apague a frase de orientação e escreva o valor que "
        "a figura mostrar. As Figuras 28, 29 e 30 já estão coladas. A Sprint 3 "
        "está na seção 2.3, com as quatro entregas e um quadro por evidência. "
        "Não preencha duração nem quantidade de turnos antes de a sessão existir.",
        color=RED,
    )
    body(
        doc,
        "Antes do print do quadro: comente nas issues 1 a 8 com o endereço do arquivo "
        "e feche as issues 5 a 8. As issues 9 a 12 só fecham depois que a figura da "
        "entrega existir. A Figura 12 precisa mostrar as doze entregas em Concluído. "
        "Defina a chave de API no ambiente, execute clear e só então rode o comando: "
        "a captura não pode conter a chave. Na sessão-piloto, conserve a transcrição "
        "que voltar, sem repetir a fala até o texto ficar apresentável.",
        color=RED,
    )
    steps = [
        "Figura 12. Quadro do GitHub Projects de poc-en-simulator, com as entregas 1 a 12 em Concluído. Feche as issues 9 a 12 só depois de a evidência de cada uma existir.",
        f"Figura 13. {REPO}/commit/{C1} — lista de arquivos adicionados da Sprint 1.",
        f"Figura 14. {blob(C1, 'docs/sprint-1/requisitos-do-fluxo.md')} — RF-01 a RF-08 visíveis. O cabeçalho da página precisa mostrar o commit {C1}.",
        f"Figura 15. {blob(C1, 'docs/sprint-1/combinacao-tecnologica.md')} — modelos escolhidos visíveis, no commit {C1}.",
        "Figura 16. Terminal, depois de clear: .venv/bin/python scripts/sprint-1-voice-check.py — frase de abertura, áudio sintetizado e transcrição, mesmo que vazia. Preencha a data na legenda.",
        f"Figura 17. {blob(C1, 'prompts/entrevistador.txt')} — trecho que impede correção durante o turno.",
        f"Figura 18. {blob(C1, 'prompts/feedback.txt')} — pedido dos três blocos e da amostra insuficiente.",
        f"Figura 19. {blob(C1, 'docs/sprint-1/das-parcial.md')} — linha “Versão: 0.1”. Abrir neste commit, não na branch main.",
        f"Figura 20. {REPO}/commit/{C2} — arquivos da interface, da API e a alteração do DAS.",
        f"Figura 21. {blob(C2, 'web/src/App.jsx')} — cenário único e a chamada a /api/sessions.",
        "Figura 22. Navegador em http://127.0.0.1:5173 depois de “Iniciar entrevista”: cenário, fala da entrevistadora e controle de áudio. A tela parada em “A sessão ainda não começou” não serve. Preencha a data na legenda.",
        f"Figura 23. {blob(C2, 'api/app.py')} — as quatro rotas /api/health, /api/sessions, /turns e /end.",
        "Figura 24. Com a API em http://127.0.0.1:8765, terminal depois de clear: curl -s http://127.0.0.1:8765/api/health e, em seguida, .venv/bin/python scripts/sprint-2-first-turn.py. Mostrar ok, key_configured verdadeiro, abertura, transcrição e fala seguinte. Preencha a data na legenda.",
        f"Figura 25. {blob(C2, 'api/feedback.py')} — geração dos três blocos, sem chave.",
        "Figura 26. A mesma tela, depois de “Encerrar sessão”, com os três blocos visíveis. Conservar o texto devolvido, inclusive se a transcrição tiver vindo vazia. Preencha a data na legenda.",
        f"Figura 27. {blob(C2, 'docs/sprint-1/das-parcial.md')} — linha “Versão: 0.2” e o início de um diagrama.",
        "Figura 31. Commit da Sprint 3, depois de publicar os arquivos. Anote o hash na legenda. A lista precisa incluir docs/sprint-3/registro-sessao-piloto.md, docs/sprint-3/nota-de-privacidade.md e o DAS na versão 1.",
        "Figura 32. Tela no meio da sessão-piloto, com mais de uma fala da entrevistadora e a transcrição devolvida, mesmo vazia. A tela inicial, antes de iniciar, não serve. Preencha a data na legenda.",
        f"Figura 33. {REPO}/blob/<commit-da-sprint-3>/docs/sprint-3/registro-sessao-piloto.md — duração, quantidade de turnos reconhecidos, resposta oral e os três blocos. Copie esses valores para o quadro cinza. Não invente transcrição.",
        f"Figura 34. {REPO}/blob/<commit-da-sprint-3>/docs/sprint-3/nota-de-privacidade.md — descarte de áudio e transcrição, voz só de quem executa o teste, e o uso possível pela camada gratuita do provedor.",
        "Figura 35. O mesmo DAS das versões 0.1 e 0.2, agora com a linha “Versão: 1”, os diagramas e o resultado da sessão-piloto no mesmo arquivo.",
        "Figura 36. Uma das duas, a que tiver ocorrido: o endereço publicado aberto no navegador, com o cenário visível; ou o parágrafo que registra que a prova de conceito permanece local. Não deixe este quadro vazio.",
    ]
    for step in steps:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        _spacing(p, after="80", before="40", line="276")
        _run(p, step, color=RED, size=Pt(11))
    body(
        doc,
        "Fim do bloco a apagar. O relatório começa no título seguinte.",
        bold=True,
        color=RED,
    )


def fill(doc: Document) -> None:
    instructions(doc)
    doc.add_page_break()

    heading(doc, "2. Área de Experimentação", 1, BLUE)
    body(
        doc,
        "A área de experimentação registra o planejamento, a execução e o resultado "
        "das sprints da prova de conceito. O quadro previsto no escopo está no "
        "GitHub Projects do repositório poc-en-simulator. A publicação dos arquivos "
        f"ocorreu em 15 de novembro de 2026, no commit {C1} para a Sprint 1 e no "
        f"commit {C2} para a Sprint 2. O commit da Sprint 3 entra na Figura 31, "
        "quando os arquivos dessa sprint forem publicados. A evidência de cada "
        "entrega é a figura correspondente. O endereço do arquivo acompanha a "
        "figura para conferência. As Sprints 1 e 2 foram executadas. A seção 2.3 "
        "deixa prontas as quatro entregas da Sprint 3. Duração, turnos reconhecidos "
        "e endereço de publicação só são escritos a partir da figura colada.",
    )

    heading(doc, "2.1 Sprint 1 — Base do fluxo e escolha da tecnologia", 3)
    body(
        doc,
        "Período: 2 a 8 de novembro de 2026. O teste curto de voz está datado, no "
        "relatório do repositório, de 10 de novembro de 2026. O objetivo desta "
        "sprint foi fechar o que seria construído e escolher uma combinação "
        "gratuita entre as alternativas do escopo, de modo que a sprint seguinte "
        "implementasse o fluxo.",
    )

    heading(doc, "2.1.1 Solução", 4)
    heading(doc, "Evidência do planejamento:", 4)
    body(
        doc,
        "A Sprint 1 foi planejada com quatro entregas. A definição da sprint consta "
        "da Figura 8. O quadro de abertura consta da Figura 11. A Figura 12 registra "
        "o mesmo quadro no envio, com as doze entregas das três sprints na coluna "
        "Concluído.",
    )
    insert_print(
        doc,
        12,
        f"{REPO} — aba Projects",
        "as entregas 1 a 12 na coluna Concluído, com as etiquetas sprint-1, sprint-2 e sprint-3 legíveis.",
        "chave de API e conteúdo de conversa que não esteja no quadro.",
    )
    caption(doc, "Figura 12 — Quadro das três sprints após a conclusão das entregas")

    heading(doc, "Evidência da execução de cada requisito:", 4)
    body(
        doc,
        f"Os quatro artefatos foram publicados no commit {C1}. A Figura 13 mostra "
        "a lista de arquivos adicionados nesse commit. Cada entrega, em seguida, "
        "aparece pelo próprio arquivo, aberto nesse commit.",
    )
    insert_print(
        doc,
        13,
        f"{REPO}/commit/{C1}",
        "a mensagem do commit, a data de 15 de novembro de 2026 e os arquivos "
        "docs/sprint-1, prompts/entrevistador.txt, prompts/feedback.txt e "
        "scripts/sprint-1-voice-check.py.",
        "chave de API.",
    )
    caption(doc, f"Figura 13 — Commit {C1}, arquivos da Sprint 1")

    item_title(doc, "1. Lista de requisitos do fluxo único")
    body(
        doc,
        "O fluxo único foi registrado em docs/sprint-1/requisitos-do-fluxo.md: um "
        "cenário de entrevista de emprego na área de tecnologia, captura de voz, "
        "resposta oral da entrevistadora e retorno ao encerrar, em três blocos. "
        f"A Figura 14 é o arquivo no commit {C1}.",
    )
    insert_print(
        doc,
        14,
        blob(C1, "docs/sprint-1/requisitos-do-fluxo.md"),
        f"o caminho do arquivo, o commit {C1} e os requisitos RF-01 a RF-08. "
        "Se a página não couber em uma tela, usar duas capturas nesta mesma figura, "
        "uma em seguida da outra.",
        "chave de API.",
    )
    caption(doc, f"Figura 14 — Lista de requisitos do fluxo único, commit {C1}")

    item_title(doc, "2. Registro da combinação tecnológica, com teste curto da própria voz")
    body(
        doc,
        "A combinação registrada em docs/sprint-1/combinacao-tecnologica.md foi: "
        "interface em React, na máquina local; API em Python 3.12, no padrão "
        "Backend for Frontend (BFF); reconhecimento gemini-3.5-transcribe em modo "
        "VERBATIM; diálogo e retorno gemini-3.5-flash-lite; síntese "
        "gemini-3.8-flash-lite-tts, voz Kore. A API contínua de áudio, o modo SMART "
        "de transcrição e a variante de síntese de estúdio ficaram de fora. A "
        "Figura 15 é esse registro. A Figura 16 é o terminal do teste curto, no "
        "qual a chave permanece só no ambiente do processo.",
    )
    insert_print(
        doc,
        15,
        blob(C1, "docs/sprint-1/combinacao-tecnologica.md"),
        f"o commit {C1} e os nomes dos modelos de reconhecimento, diálogo e síntese.",
        "chave de API.",
    )
    caption(doc, f"Figura 15 — Combinação tecnológica escolhida, commit {C1}")
    insert_print(
        doc,
        16,
        "Terminal, na raiz de poc-en-simulator, depois de clear",
        "a frase de abertura impressa pelo script, a indicação do áudio sintetizado "
        "e a linha da transcrição, inclusive se vier vazia. Comando: "
        ".venv/bin/python scripts/sprint-1-voice-check.py",
        "a chave GEMINI_API_KEY. Definir a chave, executar clear e só então rodar o script.",
    )
    caption(
        doc,
        "Figura 16 — Terminal do teste curto de voz. Data da captura: _______________",
    )

    item_title(doc, "3. Instruções de sistema do entrevistador e do feedback")
    body(
        doc,
        "Foram escritas duas instruções distintas. A da entrevistadora, em inglês, "
        "impede correção, nota ou comentário pedagógico no meio do turno. A do "
        "retorno, em português brasileiro, pede somente três blocos e manda declarar "
        "amostra insuficiente quando a transcrição for curta ou ininteligível. O "
        "modelo de transcrição não recebe essas instruções. As Figuras 17 e 18 são "
        f"os arquivos no commit {C1}.",
    )
    insert_print(
        doc,
        17,
        blob(C1, "prompts/entrevistador.txt"),
        "o caminho do arquivo e o trecho que impede correção durante a conversa.",
        "chave de API.",
    )
    caption(doc, f"Figura 17 — Instrução de sistema da entrevistadora, commit {C1}")
    insert_print(
        doc,
        18,
        blob(C1, "prompts/feedback.txt"),
        "o pedido de três blocos e a regra de declarar amostra insuficiente.",
        "chave de API.",
    )
    caption(doc, f"Figura 18 — Instrução de sistema do retorno, commit {C1}")

    item_title(doc, "4. Documento de Arquitetura de Software (DAS) parcial")
    body(
        doc,
        "A versão 0.1 do DAS descreve contexto, contêineres em texto, premissas, "
        "restrições e decisões. Os diagramas ficaram para a Sprint 2. A versão não "
        f"afirma que o fluxo já funcionava. A Figura 19 abre o arquivo no commit {C1}, "
        "no qual a linha de versão ainda é 0.1. A versão 0.2, já com diagramas, "
        "pertence à Sprint 2 e não substitui esta figura.",
    )
    insert_print(
        doc,
        19,
        blob(C1, "docs/sprint-1/das-parcial.md"),
        f"o commit {C1} e a linha “Versão: 0.1 — parcial”.",
        "a versão 0.2 da branch main. Abrir o endereço deste commit.",
    )
    caption(doc, f"Figura 19 — DAS parcial, versão 0.1, commit {C1}")

    heading(doc, "Evidência dos resultados:", 4)
    body(
        doc,
        "O resultado de cada entrega é o artefato publicado, reproduzido de novo "
        "nesta seção para leitura independente da execução. O resultado do teste "
        "de voz é o terminal da Figura 16. Transcrição vazia permanece transcrição "
        "vazia: nenhuma frase foi inventada, e este teste não é evidência de "
        "reconhecimento de sotaque brasileiro.",
    )

    item_title(doc, "1. Lista de requisitos")
    body(
        doc,
        "O fluxo único ficou fechado em oito requisitos funcionais, de RF-01 a "
        "RF-08, e nas restrições do mesmo arquivo. Ficaram fora do fluxo a medição "
        "de fluência, a correção durante a conversa, o cadastro, o banco de dados, "
        "o canal bidirecional contínuo e a publicação em nuvem como condição de "
        "conclusão. O documento entregue é a Figura 14.",
    )
    same_print(doc, 14)

    item_title(doc, "2. Combinação tecnológica")
    body(
        doc,
        "A combinação da Sprint 2 ficou escolhida, conforme a Figura 15. No teste "
        "curto, o modelo de diálogo gerou a abertura da entrevistadora e a síntese "
        "gerou áudio reproduzível. A transcrição da resposta veio vazia na execução "
        "de 10 de novembro de 2026, porque a captura de oito segundos não continha "
        "uma frase falada de propósito. A Figura 16 conserva o que o terminal "
        "devolver na captura colada acima e, de novo, abaixo.",
    )
    same_print(doc, 15)
    same_print(doc, 16)

    item_title(doc, "3. Instruções de sistema")
    body(
        doc,
        "As duas instruções passaram a ser a fonte lida pelo teste de voz e, na "
        "Sprint 2, pela API local. O resultado são os arquivos das Figuras 17 e 18.",
    )
    same_print(doc, 17)
    same_print(doc, 18)

    item_title(doc, "4. DAS parcial")
    body(
        doc,
        "O documento descreveu o contexto local, as premissas P-01 a P-04 e as "
        "restrições RC-01 a RC-09. Em 10 de novembro de 2026 o computador expunha "
        "o dispositivo de captura ALC257 Analog. A Figura 19 é a versão 0.1 entregue "
        "nesta sprint.",
    )
    same_print(doc, 19)

    heading(doc, "2.1.2 Lições Aprendidas", 3)
    body(
        doc,
        "1. Lista de requisitos. Fechar o fluxo antes de implementar evitou "
        "acrescentar cenário, cadastro ou banco na sprint seguinte. A lista também "
        "deixou explícito que o turno é uma requisição HTTP local.",
    )
    body(
        doc,
        "2. Combinação tecnológica. A camada gratuita do provedor único atendeu "
        "diálogo e síntese. O SDK oficial não foi caminho suficiente para a síntese: "
        "a chamada REST com responseModalities AUDIO e a voz Kore foi a que devolveu "
        "audio/wav. Essa rota ficou como restrição de implementação da Sprint 2.",
    )
    body(
        doc,
        "3. Teste curto de voz. Uma captura sem frase falada de propósito produz "
        "transcrição vazia. O procedimento da sprint seguinte passou a pedir uma "
        "frase em inglês e a conservar o primeiro resultado, sem repetir a chamada "
        "até aparecer um texto apresentável.",
    )
    body(
        doc,
        "4. DAS parcial. Sem os diagramas, o documento descreveu os contêineres só "
        "em texto. A Sprint 2 incorporou contexto, contêineres e sequência no mesmo "
        "arquivo, em vez de abrir um DAS novo.",
    )

    heading(doc, "2.2 Sprint 2 — Prova de conceito local", 3)
    body(
        doc,
        "Período: 9 a 15 de novembro de 2026. O objetivo desta sprint foi fazer o "
        "fluxo funcionar na máquina local, do cenário de entrevista até o retorno "
        "em três blocos, sem persistir áudio nem transcrição. A implementação foi "
        f"publicada no commit {C2}, também em 15 de novembro de 2026.",
    )

    heading(doc, "2.2.1 Solução", 4)
    heading(doc, "Evidência do planejamento:", 4)
    body(
        doc,
        "A Sprint 2 foi planejada com quatro entregas. A definição da sprint consta "
        "da Figura 9. O quadro de abertura consta da Figura 11, e o quadro após a "
        "conclusão consta da Figura 12. Não se reabriu a Sprint 1 e não se iniciou "
        "a Sprint 3. Não houve publicação em nuvem, banco, cadastro, histórico em "
        "disco, canal bidirecional contínuo, segundo cenário, correção durante a "
        "conversa nem medida de fluência.",
    )

    heading(doc, "Evidência da execução de cada requisito:", 4)
    body(
        doc,
        f"A Figura 20 é o commit {C2}, no qual entraram a interface, a API, o "
        "script do primeiro turno e a atualização do DAS para a versão 0.2. Cada "
        "entrega reúne o arquivo publicado e o registro da execução local.",
    )
    insert_print(
        doc,
        20,
        f"{REPO}/commit/{C2}",
        "a data de 15 de novembro de 2026 e os caminhos web/src/App.jsx, api/app.py, "
        "api/feedback.py, scripts/sprint-2-first-turn.py e docs/sprint-1/das-parcial.md.",
        "chave de API.",
    )
    caption(doc, f"Figura 20 — Commit {C2}, arquivos da Sprint 2")

    item_title(doc, "1. Interface local do cenário de entrevista")
    body(
        doc,
        "A tela em React é servida em http://127.0.0.1:5173. O único cenário é "
        "“Entrevista de emprego — Tecnologia”. Não há seletor de cenário, cadastro "
        "nem segundo fluxo. As chamadas da interface vão só para /api na máquina "
        "local, de modo que a chave do modelo não entra no navegador. A Figura 21 "
        "é o componente publicado. A Figura 22 é a tela depois de “Iniciar "
        "entrevista”, com a fala da entrevistadora e o áudio já devolvidos.",
    )
    insert_print(
        doc,
        21,
        blob(C2, "web/src/App.jsx"),
        f"o commit {C2}, a constante do cenário único e a função que envia POST /api/sessions.",
        "chave de API. Este arquivo não a contém; a captura não deve incluir o terminal ao lado.",
    )
    caption(doc, f"Figura 21 — Componente da interface local, commit {C2}")
    insert_print(
        doc,
        22,
        "Navegador em http://127.0.0.1:5173, depois do clique em Iniciar entrevista",
        "o rótulo do cenário único, a fala da entrevistadora na tela e o controle "
        "de áudio. Os botões de gravar e de encerrar ficam habilitados só depois da abertura.",
        "a tela ainda em “A sessão ainda não começou”. Essa tela não demonstra a execução.",
    )
    caption(
        doc,
        "Figura 22 — Interface local após o início da entrevista. Data da captura: _______________",
    )

    item_title(doc, "2. API local do turno de voz")
    body(
        doc,
        "A API em Python 3.12, no padrão BFF, escuta em http://127.0.0.1:8765. "
        "Cada turno é uma requisição síncrona: o áudio entra; reconhecimento, "
        "diálogo e síntese ocorrem na mesma requisição; texto e áudio da "
        "entrevistadora saem. A chave permanece no ambiente do processo. O "
        "histórico textual fica só em memória. O áudio do usuário é lido, enviado "
        "ao reconhecimento e descartado. A Figura 23 é o código das rotas. A "
        "Figura 24 é o terminal da execução: a consulta de saúde e o primeiro turno.",
    )
    insert_print(
        doc,
        23,
        blob(C2, "api/app.py"),
        "as quatro rotas: GET /api/health, POST /api/sessions, "
        "POST /api/sessions/{session_id}/turns e POST /api/sessions/{session_id}/end.",
        "chave de API e valor de variável de ambiente.",
    )
    caption(doc, f"Figura 23 — Rotas da API local, commit {C2}")
    insert_print(
        doc,
        24,
        "Terminal, com a API já em http://127.0.0.1:8765, depois de clear",
        "a resposta de curl -s http://127.0.0.1:8765/api/health, com ok e "
        "key_configured verdadeiros, e a saída de "
        ".venv/bin/python scripts/sprint-2-first-turn.py, com abertura, transcrição "
        "e fala seguinte. A transcrição vazia, se ocorrer, permanece na figura.",
        "a chave. A resposta de saúde indica apenas se ela está configurada.",
    )
    caption(
        doc,
        "Figura 24 — Terminal da API local e do primeiro turno. Data da captura: _______________",
    )

    item_title(doc, "3. Feedback em três blocos")
    body(
        doc,
        "O encerramento não reutiliza a instrução da entrevistadora. A API apaga "
        "a sessão da memória e chama o modelo com a transcrição acumulada e a "
        "instrução de retorno. A Figura 25 é essa chamada no código. A Figura 26 "
        "é a tela depois de “Encerrar sessão”, com os três blocos devolvidos.",
    )
    insert_print(
        doc,
        25,
        blob(C2, "api/feedback.py"),
        f"o commit {C2} e o trecho que pede os três blocos a partir da transcrição acumulada.",
        "chave de API.",
    )
    caption(doc, f"Figura 25 — Chamada de feedback na API, commit {C2}")
    insert_print(
        doc,
        26,
        "A mesma sessão da Figura 22, depois de Encerrar sessão",
        "os três rótulos na tela: pontos positivos, pontos de melhoria e próximo passo, "
        "com o texto devolvido pelo modelo. Não repetir a sessão para obter um texto "
        "mais apresentável.",
        "chave de API e uma transcrição digitada à mão.",
    )
    caption(
        doc,
        "Figura 26 — Retorno em três blocos na interface. Data da captura: _______________",
    )

    item_title(doc, "4. Diagramas de contexto, contêineres e sequência")
    body(
        doc,
        "Os três diagramas foram incorporados ao DAS parcial já existente, que "
        f"passou à versão 0.2 no commit {C2}. Não se abriu um DAS novo. A "
        "sessão-piloto e a nota de privacidade continuam fora desta versão. A "
        "Figura 27 é o arquivo nessa versão. As figuras legíveis dos diagramas "
        "estão na evidência de resultados.",
    )
    insert_print(
        doc,
        27,
        blob(C2, "docs/sprint-1/das-parcial.md"),
        "a linha “Versão: 0.2 — parcial” e o início de ao menos um bloco mermaid "
        "de contexto, contêineres ou sequência.",
        "a versão 0.1. Abrir o commit da Sprint 2.",
    )
    caption(doc, f"Figura 27 — DAS parcial, versão 0.2, commit {C2}")

    heading(doc, "Evidência dos resultados:", 4)
    body(
        doc,
        "O resultado observável é a prova de conceito em execução na máquina local. "
        "A tela de abertura, o terminal do turno e os três blocos abaixo repetem, "
        "nesta seção, as capturas da execução. Os diagramas estão reproduzidos a "
        "partir do DAS 0.2. Não há banco de dados, fila nem canal bidirecional contínuo.",
    )

    item_title(doc, "1. Interface local")
    body(
        doc,
        "A tela abriu com um único cenário. Depois de “Iniciar entrevista”, a API "
        "devolveu a fala da entrevistadora e o áudio correspondente. O resultado "
        "dessa abertura é a Figura 22. A frase exibida é a que estiver na captura, "
        "sem substituição por um texto mais conveniente.",
    )
    same_print(doc, 22)

    item_title(doc, "2. API local do turno")
    body(
        doc,
        "O resultado da execução local é a Figura 24. A consulta de saúde confirma "
        "a chave configurada sem expô-la. O primeiro turno devolve abertura, "
        "transcrição e fala seguinte. Na execução de 15 de novembro de 2026 a "
        "transcrição veio vazia, diante da frase pedida “I am a software engineer "
        "and I work with Python and web APIs.”, e a entrevistadora pediu que a "
        "pessoa repetisse em uma frase curta. A captura nova conserva o que o "
        "terminal devolver, e este resultado não afirma reconhecimento de sotaque "
        "brasileiro.",
    )
    same_print(doc, 24)

    item_title(doc, "3. Feedback em três blocos")
    body(
        doc,
        "A segunda chamada ao modelo devolve três blocos, não um quarto. Na "
        "execução de 15 de novembro de 2026 o bloco de pontos positivos atribuiu "
        "participação ao candidato sem citar uma frase dita por ele. Esse desvio "
        "é limitação do retorno, não evidência de fala reconhecida. A Figura 26 "
        "mostra os três blocos da captura colada nesta versão.",
    )
    same_print(doc, 26)

    item_title(doc, "4. Diagramas no DAS")
    body(
        doc,
        "Os três diagramas passaram a constar do mesmo documento, na versão 0.2 "
        "registrada pela Figura 27. As Figuras 28 a 30 reproduzem o contexto, os "
        "contêineres e a sequência de um turno.",
    )
    picture(doc, ASSETS / "contexto.png", 15.5)
    caption(doc, "Figura 28 — Diagrama de contexto")
    picture(doc, ASSETS / "conteineres.png", 14.0)
    caption(doc, "Figura 29 — Diagrama de contêineres")
    picture(doc, ASSETS / "sequencia-turno.png", 15.5)
    caption(doc, "Figura 30 — Diagrama de sequência de um turno")

    heading(doc, "2.2.2 Lições Aprendidas", 3)
    body(
        doc,
        "1. Interface local. Uma tela basta para o fluxo. O cenário único precisa "
        "aparecer como rótulo, não como lista de escolha. A reprodução da voz da "
        "entrevistadora depende do clique em “Iniciar entrevista”; o controle de "
        "áudio na tela cobre o caso em que o navegador bloqueia a reprodução automática.",
    )
    body(
        doc,
        "2. API local do turno. Isolar a chave no processo da API atendeu o requisito "
        "de a chave ficar fora do navegador. A porta 8000 não estava livre nesta "
        "máquina; a prova de conceito passou a escutar na porta 8765, em 127.0.0.1. "
        "O reconhecimento devolveu transcrição vazia na execução de 15 de novembro "
        "de 2026, e a captura não foi repetida para obter um texto apresentável. "
        "Sem frase reconhecida, o requisito de transcrição suficiente para o diálogo "
        "continuar permanece sem evidência positiva. A entrevistadora, ainda assim, "
        "manteve o papel e pediu que a pessoa repetisse.",
    )
    body(
        doc,
        "3. Feedback em três blocos. A segunda chamada, com outra instrução, devolveu "
        "os três cabeçalhos. A instrução pede que se declare amostra insuficiente "
        "quando não houver frase do candidato; o modelo, mesmo assim, preencheu "
        "pontos positivos com participação inferida. Para a sessão-piloto da Sprint 3, "
        "esse desvio precisa ser lido como limitação do retorno.",
    )
    body(
        doc,
        "4. Diagramas. Incorporar os três desenhos no DAS parcial evitou um documento "
        "paralelo. A versão continua 0.2: a sessão-piloto de cinco a dez minutos, a "
        "nota de privacidade fechada e o DAS na versão 1 pertencem à Sprint 3. A "
        "publicação em nuvem não foi feita e não é condição para encerrar esta sprint.",
    )

    heading(doc, "2.3 Sprint 3 — Sessão-piloto e fechamento do DAS", 3)
    body(
        doc,
        "Período: 16 a 22 de novembro de 2026. O objetivo desta sprint é verificar "
        "o critério mensurável do objetivo e fechar o documento. A sessão é local "
        "e conduzida por quem executa o teste. São quatro entregas. A publicação "
        "em nuvem só ocorre se as três primeiras estiverem concluídas e ainda "
        "houver tempo; se não houver, o registro de que a prova de conceito "
        "permanece local cumpre a quarta entrega. Essa quarta entrega não bloqueia "
        "o objetivo.",
    )
    body(
        doc,
        "Os quadros desta seção nomeiam o que cada entrega produz. Duração, "
        "quantidade de turnos e texto da transcrição não são antecipados: entram "
        "somente com a figura correspondente.",
    )

    heading(doc, "2.3.1 Solução", 4)
    heading(doc, "Evidência do planejamento:", 4)
    body(
        doc,
        "A Sprint 3 foi planejada com quatro entregas. A definição da sprint consta "
        "da Figura 10. O quadro de abertura consta da Figura 11. O quadro no envio, "
        "com as doze entregas em Concluído, consta da Figura 12. As entregas são "
        "as que seguem.",
    )
    item_title(doc, "1. Registro da sessão-piloto")
    body(
        doc,
        "Uma sessão local, de cinco a dez minutos, com ao menos quatro turnos de "
        "fala reconhecidos, resposta oral da entrevistadora e feedback em três "
        "blocos. O registro informa duração, quantidade de turnos reconhecidos, "
        "resposta oral e os três blocos. O arquivo previsto é "
        "docs/sprint-3/registro-sessao-piloto.md.",
    )
    item_title(doc, "2. Nota de privacidade")
    body(
        doc,
        "Nota de que a aplicação descarta áudio e transcrição ao fim do turno, de "
        "que a sessão-piloto usa apenas a voz de quem executa o teste e de que a "
        "camada gratuita do provedor pode usar o conteúdo enviado para melhoria "
        "dos próprios produtos. O arquivo previsto é "
        "docs/sprint-3/nota-de-privacidade.md.",
    )
    item_title(doc, "3. DAS versão 1")
    body(
        doc,
        "O mesmo DAS das versões 0.1 e 0.2, atualizado para a versão 1, no arquivo "
        "já existente. A versão reúne arquitetura, diagramas, premissas, restrições "
        "e o resultado da sessão-piloto. Não se abre um segundo documento.",
    )
    item_title(doc, "4. Publicação em nuvem, condicionada ao tempo")
    body(
        doc,
        "Se as três entregas anteriores estiverem concluídas e ainda houver tempo, "
        "a interface e a API são publicadas em AWS, Azure ou provedor equivalente, "
        "e o endereço fica registrado. Se não houver tempo, fica registrado que a "
        "prova de conceito permanece local. Uma das duas saídas cumpre a entrega.",
    )

    heading(doc, "Evidência da execução de cada requisito:", 4)
    body(
        doc,
        "A Figura 31 é o commit que publicar os arquivos desta sprint. O hash ainda "
        "não existe neste arquivo: ele é escrito na legenda quando o commit for "
        "criado. Cada entrega, abaixo, tem a captura da execução.",
    )
    insert_print(
        doc,
        31,
        f"{REPO}/commits/main — o commit que adicionar a pasta docs/sprint-3",
        "a data do commit e os caminhos docs/sprint-3/registro-sessao-piloto.md, "
        "docs/sprint-3/nota-de-privacidade.md e o DAS passado à versão 1.",
        "chave de API. Anote o hash curto na legenda, no lugar dos traços.",
    )
    caption(doc, "Figura 31 — Commit ________, arquivos da Sprint 3")

    item_title(doc, "1. Registro da sessão-piloto")
    body(
        doc,
        "A execução é uma única sessão na interface local, em http://127.0.0.1:5173, "
        "com a API em http://127.0.0.1:8765. Quem executa o teste fala as respostas. "
        "A sessão não é repetida para obter uma transcrição mais apresentável. Se "
        "o reconhecimento não completar quatro turnos, a limitação entra no registro "
        "e no DAS, e o critério mensurável do objetivo fica não atingido. A Figura 32 "
        "é a tela durante a sessão. A Figura 33 é o arquivo do registro no commit "
        "da Figura 31.",
    )
    insert_print(
        doc,
        32,
        "Navegador em http://127.0.0.1:5173, no meio da sessão-piloto",
        "mais de uma fala da entrevistadora e a transcrição devolvida para um turno "
        "já enviado, mesmo que vazia. Se os quatro turnos não couberem numa tela, "
        "usar duas capturas nesta mesma figura. O rótulo do cenário único continua visível.",
        "a tela de “A sessão ainda não começou”, chave de API e transcrição digitada à mão.",
    )
    caption(
        doc,
        "Figura 32 — Sessão-piloto em andamento. Data da captura: _______________",
    )
    insert_print(
        doc,
        33,
        f"{REPO}/blob/<hash-da-Figura-31>/docs/sprint-3/registro-sessao-piloto.md",
        "duração em minutos, quantidade de turnos de fala reconhecidos, indicação "
        "de resposta oral da entrevistadora e os três blocos de feedback, com o "
        "texto devolvido pelo modelo.",
        "número que não esteja nesse arquivo e transcrição que o microfone não tenha devolvido.",
    )
    caption(doc, "Figura 33 — Registro da sessão-piloto no repositório")

    item_title(doc, "2. Nota de privacidade")
    body(
        doc,
        "A execução desta entrega é a redação da nota no arquivo previsto, alinhada "
        "ao comportamento já implementado: o áudio do turno é descartado e a "
        "transcrição não é gravada em disco. A Figura 34 é esse arquivo no commit "
        "da Figura 31.",
    )
    insert_print(
        doc,
        34,
        f"{REPO}/blob/<hash-da-Figura-31>/docs/sprint-3/nota-de-privacidade.md",
        "as três afirmações: descarte de áudio e transcrição ao fim do turno; "
        "uso apenas da voz de quem executa o teste; possibilidade de a camada "
        "gratuita do provedor utilizar o conteúdo enviado.",
        "chave de API e áudio da sessão.",
    )
    caption(doc, "Figura 34 — Nota de privacidade da sessão-piloto")

    item_title(doc, "3. DAS versão 1")
    body(
        doc,
        "A execução é a atualização do DAS já existente, não a abertura de outro "
        "arquivo. A versão 1 incorpora os diagramas das Figuras 28 a 30, as "
        "premissas, as restrições e o resultado que a Figura 33 registrar. A "
        "Figura 35 é essa versão no commit da Sprint 3.",
    )
    insert_print(
        doc,
        35,
        "docs/sprint-1/das-parcial.md no commit da Figura 31",
        "a linha “Versão: 1”, um dos diagramas e o trecho que reproduz duração e "
        "turnos da sessão-piloto. Se a página não couber numa tela, usar duas "
        "capturas nesta mesma figura.",
        "a versão 0.1 ou 0.2 no lugar da versão 1. Abrir o commit da Sprint 3.",
    )
    caption(doc, "Figura 35 — DAS na versão 1, com o resultado da sessão-piloto")

    item_title(doc, "4. Publicação em nuvem, condicionada ao tempo")
    body(
        doc,
        "A execução segue uma das duas saídas. Com as três entregas anteriores "
        "concluídas e tempo restante, publicam-se interface e API, e a Figura 36 "
        "mostra o endereço aberto no navegador. Sem tempo, a Figura 36 mostra o "
        "parágrafo, no DAS ou em docs/sprint-3/publicacao.md, que registra a "
        "permanência local. O quadro não fica vazio.",
    )
    insert_print(
        doc,
        36,
        "O endereço publicado, ou o parágrafo que registra a permanência local",
        "uma das duas provas: a página no ar, com o cenário “Entrevista de emprego "
        "— Tecnologia” e o endereço legível na barra; ou a frase explícita de que "
        "a prova de conceito permanece local, com o caminho do arquivo visível.",
        "as duas provas ao mesmo tempo, se apenas uma ocorreu, e qualquer chave de acesso.",
    )
    caption(doc, "Figura 36 — Publicação em nuvem ou registro de permanência local")

    heading(doc, "Evidência dos resultados:", 4)
    body(
        doc,
        "O resultado de cada entrega é o artefato da execução, repetido aqui para "
        "leitura independente. Os campos cinza recebem só o valor que a figura "
        "mostrar. Campo vazio significa que a sessão ainda não foi colada.",
    )

    item_title(doc, "1. Registro da sessão-piloto")
    body(
        doc,
        "O resultado é a sessão da Figura 32 e o registro da Figura 33. Os quatro "
        "campos abaixo são copiados dessa figura. O critério mensurável pede cinco "
        "a dez minutos, quatro turnos de fala reconhecidos, resposta oral e feedback "
        "em três blocos. Se a figura mostrar menos de quatro turnos reconhecidos, "
        "o campo do critério fica “não atingido”, e essa limitação permanece no DAS.",
    )
    text_field(
        doc,
        "Duração da sessão",
        "Copiar da Figura 33. Exemplo de forma, não de valor: 7 minutos.",
    )
    text_field(
        doc,
        "Turnos de fala reconhecidos",
        "Copiar da Figura 33. Contar turno cuja transcrição tenha devolvido texto, não turno com transcrição vazia.",
    )
    text_field(
        doc,
        "Resposta oral da entrevistadora",
        "Copiar da Figura 33: em quantos turnos houve áudio ou texto de resposta da entrevistadora.",
    )
    text_field(
        doc,
        "Critério de quatro turnos reconhecidos",
        "Escrever “atingido” ou “não atingido”, conforme o número do campo anterior.",
    )
    same_print(doc, 32)
    same_print(doc, 33)

    item_title(doc, "2. Nota de privacidade")
    body(
        doc,
        "O resultado é a nota da Figura 34. Ela declara o descarte do áudio e da "
        "transcrição ao fim do turno, o uso exclusivo da voz de quem executa o "
        "teste e a possibilidade de uso do conteúdo pela camada gratuita do provedor.",
    )
    same_print(doc, 34)

    item_title(doc, "3. DAS versão 1")
    body(
        doc,
        "O resultado é um único DAS, na versão 1, com arquitetura, diagramas, "
        "premissas, restrições e o resultado da sessão-piloto. A Figura 35 é esse "
        "documento. As Figuras 28 a 30 continuam a reprodução legível dos diagramas.",
    )
    same_print(doc, 35)

    item_title(doc, "4. Publicação em nuvem, condicionada ao tempo")
    body(
        doc,
        "O resultado é uma das duas saídas da Figura 36. O campo abaixo repete o "
        "que a figura mostrar: o endereço publicado ou a permanência local.",
    )
    text_field(
        doc,
        "Saída da quarta entrega",
        "Copiar da Figura 36. Ou o endereço publicado, ou a frase “a prova de conceito permanece local”.",
    )
    same_print(doc, 36)

    heading(doc, "2.3.2 Lições Aprendidas", 3)
    body(
        doc,
        "Cada lição é escrita depois da execução da entrega correspondente, com o "
        "que a figura mostrou. Não se antecipa conclusão sobre fluência, sobre "
        "reconhecimento de sotaque brasileiro nem sobre a publicação em nuvem.",
    )
    text_field(
        doc,
        "1. Sessão-piloto",
        "Substituir esta frase pelo que a duração e os turnos reconhecidos da Figura 33 mostraram.",
    )
    text_field(
        doc,
        "2. Nota de privacidade",
        "Substituir esta frase pelo que a redação da Figura 34 exigiu em relação ao descarte do áudio e à camada gratuita.",
    )
    text_field(
        doc,
        "3. DAS versão 1",
        "Substituir esta frase pelo que mudou ao reunir, no mesmo arquivo, os diagramas e o resultado da sessão.",
    )
    text_field(
        doc,
        "4. Publicação em nuvem",
        "Substituir esta frase pela saída que a Figura 36 registrou e pelo que limitou ou permitiu essa saída.",
    )


def main() -> None:
    if not BACKUP.exists():
        raise SystemExit(f"Backup não encontrado: {BACKUP}")
    doc = Document(str(BACKUP))
    replace_cronograma(doc)
    fill(doc)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
