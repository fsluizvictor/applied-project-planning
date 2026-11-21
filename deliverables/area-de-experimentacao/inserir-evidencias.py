#!/usr/bin/env python3
"""Insere os prints de planejamento, execução e resultado de cada entrega."""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.text.paragraph import Paragraph

DOC = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "Relatorio_Projeto_Aplicado_Luiz_Victor.docx"
)
EV = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "area-de-experimentacao/evidencias"
)
INK = RGBColor(0x1A, 0x1F, 0x20)
GREEN = RGBColor(0x00, 0xB0, 0x50)


def _spacing(paragraph, after="200", before="160", line="360") -> None:
    pPr = paragraph._p.get_or_add_pPr()
    spacing = pPr.find(qn("w:spacing"))
    if spacing is None:
        spacing = OxmlElement("w:spacing")
        pPr.append(spacing)
    spacing.set(qn("w:after"), after)
    spacing.set(qn("w:before"), before)
    spacing.set(qn("w:line"), line)
    spacing.set(qn("w:lineRule"), "auto")


def _run(paragraph, text, *, bold=False, color=INK, size=None) -> None:
    run = paragraph.add_run(text)
    run.bold = bold
    run.font.color.rgb = color
    if size is not None:
        run.font.size = size


def insert_before(anchor) -> Paragraph:
    element = OxmlElement("w:p")
    anchor._p.addprevious(element)
    return Paragraph(element, anchor._parent)


def render(paragraph, kind, payload) -> None:
    if kind == "break":
        run = paragraph.add_run()
        run.add_break(WD_BREAK.PAGE)
        return
    if kind == "h3":
        paragraph.style = "Heading 3"
        _run(paragraph, payload, bold=True, color=GREEN)
        return
    if kind == "h4":
        paragraph.style = "Heading 4"
        _run(paragraph, payload, bold=True, color=GREEN)
        return
    if kind == "title":
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        _spacing(paragraph, after="60", before="200")
        _run(paragraph, payload, bold=True)
        return
    if kind == "body":
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        _spacing(paragraph)
        _run(paragraph, payload)
        return
    if kind == "caption":
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _spacing(paragraph, after="200", before="60", line="276")
        _run(paragraph, payload, bold=True, size=Pt(11))
        return
    if kind == "picture":
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _spacing(paragraph, after="40", before="80", line="240")
        paragraph.add_run().add_picture(str(payload), width=Cm(15.5))
        return
    raise SystemExit(kind)


def shot(name: str) -> Path:
    path = EV / name
    if not path.exists():
        raise SystemExit(f"Print ausente: {path}")
    return path


def main() -> None:
    blocks: list[tuple] = [
        ("break", None),
        ("h3", "2.4 Evidências por entrega"),
        (
            "body",
            "Esta seção reúne, para cada entrega, o print do planejamento e o print "
            "do artefato publicado. O planejamento é a issue do repositório "
            "poc-en-simulator. A execução é o arquivo no commit em que a entrega "
            "foi publicada. Quando o resultado é outro arquivo, ou uma tela, ele "
            "aparece em seguida. As Figuras 8 a 11 continuam a ser o planejamento "
            "das três sprints e o quadro. As Figuras 12 a 19 continuam nos pontos "
            "em que já foram citadas.",
        ),
        (
            "body",
            "Não há print de terminal das execuções de 10 e de 15 de novembro de "
            "2026. O que o terminal devolveu está escrito nos arquivos de resultado, "
            "e esses arquivos é que foram fotografados. A tela da Sprint 2 depois "
            "de “Iniciar entrevista” também não foi arquivada. A Figura 12 mostra "
            "a interface antes do início. As issues 11 e 12 seguem abertas: a "
            "versão 1 do DAS não foi publicada nesse repositório, e a publicação "
            "em nuvem não foi feita.",
        ),
        ("h4", "2.4.1 Sprint 1 — commit 95a4f57"),
        ("title", "Entrega 1 — Lista de requisitos do fluxo único"),
        (
            "body",
            "O planejamento é a issue 1, fechada, com a etiqueta sprint-1. A "
            "execução e o resultado são o mesmo arquivo, requisitos-do-fluxo.md, "
            "nesse commit. A Figura 21 mostra o fluxo único e o início dos "
            "requisitos RF-01 a RF-08.",
        ),
        ("caption", "Figura 20 — Planejamento da entrega 1, issue 1"),
        ("picture", shot("issue-1.png")),
        ("caption", "Figura 21 — Resultado da entrega 1, requisitos do fluxo, commit 95a4f57"),
        ("picture", shot("s1-requisitos.png")),
        ("title", "Entrega 2 — Combinação tecnológica e teste curto de voz"),
        (
            "body",
            "O planejamento é a issue 2. A execução é o registro da combinação. "
            "O resultado do teste de 10 de novembro de 2026 está em "
            "resultado-teste-voz.md: a abertura foi gerada e a transcrição veio "
            "vazia. Não se reexecutou o teste para produzir um print de terminal.",
        ),
        ("caption", "Figura 22 — Planejamento da entrega 2, issue 2"),
        ("picture", shot("issue-2.png")),
        ("caption", "Figura 23 — Combinação tecnológica, commit 95a4f57"),
        ("picture", shot("s1-combinacao.png")),
        ("caption", "Figura 24 — Resultado do teste curto de voz, transcrição vazia"),
        ("picture", shot("s1-teste-voz.png")),
        ("title", "Entrega 3 — Instruções de sistema"),
        (
            "body",
            "O planejamento é a issue 3. A execução e o resultado são os dois "
            "arquivos de instrução do mesmo commit. A da entrevistadora impede "
            "correção durante o turno. A do retorno pede somente três blocos.",
        ),
        ("caption", "Figura 25 — Planejamento da entrega 3, issue 3"),
        ("picture", shot("issue-3.png")),
        ("caption", "Figura 26 — Instrução da entrevistadora, commit 95a4f57"),
        ("picture", shot("s1-prompt-entrevistador.png")),
        ("caption", "Figura 27 — Instrução do retorno em três blocos, commit 95a4f57"),
        ("picture", shot("s1-prompt-feedback.png")),
        ("title", "Entrega 4 — DAS parcial, versão 0.1"),
        (
            "body",
            "O planejamento é a issue 4. O resultado é o mesmo arquivo que a "
            "Sprint 2 depois atualizou. Neste commit a linha de versão é 0.1, e "
            "o texto diz que os diagramas ficam para a sprint seguinte.",
        ),
        ("caption", "Figura 28 — Planejamento da entrega 4, issue 4"),
        ("picture", shot("issue-4.png")),
        ("caption", "Figura 29 — DAS parcial, versão 0.1, commit 95a4f57"),
        ("picture", shot("s1-das-01.png")),
        ("h4", "2.4.2 Sprint 2 — commit 648013e"),
        ("title", "Entrega 5 — Interface local do cenário de entrevista"),
        (
            "body",
            "O planejamento é a issue 5. A execução é App.jsx nesse commit: a "
            "constante do cenário único é “Entrevista de emprego — Tecnologia” e "
            "a abertura chama /api/sessions. A tela depois de “Iniciar entrevista” "
            "não foi arquivada. A Figura 12 mostra a interface antes do início, "
            "com o mesmo rótulo de cenário.",
        ),
        ("caption", "Figura 30 — Planejamento da entrega 5, issue 5"),
        ("picture", shot("issue-5.png")),
        ("caption", "Figura 31 — Interface local, cenário único, commit 648013e"),
        ("picture", shot("s2-app-jsx.png")),
        ("title", "Entrega 6 — API local do turno de voz"),
        (
            "body",
            "O planejamento é a issue 6. A execução é api/app.py no mesmo commit, "
            "com as rotas de saúde, de abertura e de turno. O resultado do "
            "primeiro turno real, em 15 de novembro de 2026, está em "
            "resultado-primeiro-turno.md. A transcrição registrada é vazia. Não "
            "há print do terminal dessa execução.",
        ),
        ("caption", "Figura 32 — Planejamento da entrega 6, issue 6"),
        ("picture", shot("issue-6.png")),
        ("caption", "Figura 33 — Rotas da API local, commit 648013e"),
        ("picture", shot("s2-api.png")),
        ("caption", "Figura 34 — Resultado do primeiro turno, transcrição vazia"),
        ("picture", shot("s2-primeiro-turno.png")),
        ("title", "Entrega 7 — Feedback em três blocos"),
        (
            "body",
            "O planejamento é a issue 7. A execução é api/feedback.py, que separa "
            "somente os três blocos e não inventa bloco ausente. O texto que o "
            "modelo devolveu em 15 de novembro de 2026 está no mesmo registro da "
            "Figura 34.",
        ),
        ("caption", "Figura 35 — Planejamento da entrega 7, issue 7"),
        ("picture", shot("issue-7.png")),
        ("caption", "Figura 36 — Separação dos três blocos de retorno, commit 648013e"),
        ("picture", shot("s2-feedback.png")),
        ("title", "Entrega 8 — Diagramas no DAS"),
        (
            "body",
            "O planejamento é a issue 8. A execução atualizou o DAS já existente "
            "para a versão 0.2, no mesmo arquivo, em 15 de novembro de 2026. Os "
            "desenhos legíveis são as Figuras 13 a 15.",
        ),
        ("caption", "Figura 37 — Planejamento da entrega 8, issue 8"),
        ("picture", shot("issue-8.png")),
        ("caption", "Figura 38 — DAS parcial, versão 0.2, commit 648013e"),
        ("picture", shot("s2-das-02.png")),
        ("h4", "2.4.3 Sprint 3"),
        ("title", "Entrega 9 — Registro da sessão-piloto"),
        (
            "body",
            "O planejamento é a issue 9, fechada. A tela ao encerrar é a Figura 16. "
            "O registro escrito está no commit f1466c0. Esse arquivo ainda diz que "
            "o DAS na versão 1 e a publicação em nuvem seguiam pendentes: ele foi "
            "publicado antes do fechamento do DAS. Duração, turnos e transcrições "
            "da Figura 40 são os da sessão de 20 de novembro de 2026.",
        ),
        ("caption", "Figura 39 — Planejamento da entrega 9, issue 9"),
        ("picture", shot("issue-9.png")),
        ("caption", "Figura 40 — Registro da sessão-piloto, commit f1466c0"),
        ("picture", shot("s3-registro.png")),
        ("title", "Entrega 10 — Nota de privacidade"),
        (
            "body",
            "O planejamento é a issue 10, fechada. A execução e o resultado são a "
            "nota publicada no commit a26ac63. A nota distingue o descarte do áudio "
            "da permanência da transcrição em memória até o encerramento.",
        ),
        ("caption", "Figura 41 — Planejamento da entrega 10, issue 10"),
        ("picture", shot("issue-10.png")),
        ("caption", "Figura 42 — Nota de privacidade, commit a26ac63"),
        ("picture", shot("s3-nota.png")),
        ("title", "Entrega 11 — DAS versão 1"),
        (
            "body",
            "O planejamento é a issue 11, que segue aberta. A versão 1 não foi "
            "publicada no repositório poc-en-simulator. O documento foi redigido "
            "em arquivo local, com a linha de versão 1.0 e a data de 20 de "
            "novembro de 2026. Os diagramas dessa versão são as Figuras 17 e 18.",
        ),
        ("caption", "Figura 43 — Planejamento da entrega 11, issue 11, ainda aberta"),
        ("picture", shot("issue-11.png")),
        ("caption", "Figura 44 — Cabeçalho do DAS versão 1, arquivo local, não publicado no repositório"),
        ("picture", shot("das-v1-cabecalho.png")),
        ("title", "Entrega 12 — Publicação em nuvem"),
        (
            "body",
            "O planejamento é a issue 12, que segue aberta. A publicação não foi "
            "executada. A prova de conceito permanece local. A Figura 19 é a "
            "topologia proposta. A Figura 46 é o trecho do DAS que declara que "
            "essa proposta não foi implantada.",
        ),
        ("caption", "Figura 45 — Planejamento da entrega 12, issue 12, ainda aberta"),
        ("picture", shot("issue-12.png")),
        (
            "caption",
            "Figura 46 — Trecho do DAS versão 1: a implantação proposta não foi executada",
        ),
        ("picture", shot("das-v1-nao-implantado.png")),
    ]

    doc = Document(str(DOC))
    if any(p.text.startswith("2.4 Evidências por entrega") for p in doc.paragraphs):
        raise SystemExit("A seção 2.4 já existe. Não inseri de novo.")
    heading = next(p for p in doc.paragraphs if p.text == "3. Considerações Finais")
    for kind, payload in blocks:
        paragraph = insert_before(heading)
        render(paragraph, kind, payload)
    doc.save(str(DOC))
    print(DOC)


if __name__ == "__main__":
    main()
