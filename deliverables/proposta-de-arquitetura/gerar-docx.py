"""Gera o DAS em DOCX a partir de das-v1-rascunho.md e dos diagramas em diagramas-v2/.

Uso: python3 gerar-docx.py
Requer python-docx (pip install python-docx).
"""

from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "das-v1-rascunho.md"
OUTPUT = BASE / "das-v1-simulador-entrevista.docx"
FONT = "Arial"
CODE_FONT = "Consolas"
HEADER_FILL = "D9E2F3"
INLINE = re.compile(r"(\*\*.+?\*\*|`[^`]+`|\*[^*\s][^*]*?\*)")


def set_cell_fill(cell, color: str) -> None:
    props = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:val"), "clear")
    shading.set(qn("w:color"), "auto")
    shading.set(qn("w:fill"), color)
    props.append(shading)


def repeat_header(row) -> None:
    props = row._tr.get_or_add_trPr()
    flag = OxmlElement("w:tblHeader")
    flag.set(qn("w:val"), "true")
    props.append(flag)


def add_field(paragraph, instruction: str, placeholder: str = "") -> None:
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    run._r.append(begin)
    run = paragraph.add_run()
    text = OxmlElement("w:instrText")
    text.set(qn("xml:space"), "preserve")
    text.text = f" {instruction} "
    run._r.append(text)
    run = paragraph.add_run()
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    run._r.append(sep)
    paragraph.add_run(placeholder)
    run = paragraph.add_run()
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(end)


def add_inline(paragraph, text: str, size: float | None = None, bold: bool = False) -> None:
    for token in INLINE.split(text):
        if not token:
            continue
        if token.startswith("**") and token.endswith("**") and len(token) > 4:
            add_inline(paragraph, token[2:-2], size, bold=True)
            continue
        if token.startswith("`") and token.endswith("`") and len(token) > 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = CODE_FONT
            run.font.size = Pt((size or 12) - 1.5)
            run.bold = bold
            continue
        if token.startswith("*") and token.endswith("*") and len(token) > 2:
            run = paragraph.add_run(token[1:-1])
            run.italic = True
        else:
            run = paragraph.add_run(token)
        run.bold = bold
        if size:
            run.font.size = Pt(size)


def configure(document: Document) -> None:
    section = document.sections[0]
    section.page_height, section.page_width = Cm(29.7), Cm(21.0)
    section.top_margin, section.left_margin = Cm(3), Cm(3)
    section.bottom_margin, section.right_margin = Cm(2), Cm(2)

    normal = document.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(12)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    fmt = normal.paragraph_format
    fmt.line_spacing = 1.5
    fmt.space_after = Pt(6)

    for name, size in (("Heading 1", 14), ("Heading 2", 12.5), ("Heading 3", 12), ("Title", 20)):
        style = document.styles[name]
        style.font.name = FONT
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0x14, 0x20, 0x2E)
        rpr = style.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is None:
            fonts = OxmlElement("w:rFonts")
            rpr.append(fonts)
        for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            fonts.set(qn(attr), FONT)
        style.paragraph_format.space_before = Pt(18 if name == "Heading 1" else 12)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.keep_with_next = True

    caption = document.styles["Caption"]
    caption.font.name = FONT
    caption.font.size = Pt(10)
    caption.font.italic = False
    caption.font.bold = True
    caption.font.color.rgb = RGBColor(0x14, 0x20, 0x2E)

    settings = document.settings.element
    update = OxmlElement("w:updateFields")
    update.set(qn("w:val"), "true")
    settings.append(update)


def header_footer(section, title: str) -> None:
    section.different_first_page_header_footer = True
    header = section.header.paragraphs[0]
    header.text = ""
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = header.add_run(title)
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x5A, 0x62, 0x70)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_field(footer, "PAGE", "1")


def parse_metadata(lines: list[str]) -> tuple[str, list[tuple[str, str]]]:
    title = ""
    meta: list[tuple[str, str]] = []
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
        match = re.match(r"\*\*(.+?):\*\*\s*(.+)", line.strip())
        if match:
            meta.append((match.group(1), match.group(2).strip()))
    return title, meta


def cover(document: Document, title: str, meta: dict[str, str]) -> None:
    for _ in range(5):
        document.add_paragraph()
    p = document.add_paragraph(style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(title)
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(meta.get("Projeto", ""))
    run.font.size = Pt(15)
    run.bold = True
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(meta.get("Sprint", ""))
    run.font.size = Pt(12)
    for _ in range(6):
        document.add_paragraph()
    table = document.add_table(rows=0, cols=2)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for key in ("Versão", "Data", "Responsável"):
        cells = table.add_row().cells
        cells[0].text = ""
        add_inline(cells[0].paragraphs[0], key, 11, bold=True)
        set_cell_fill(cells[0], HEADER_FILL)
        add_inline(cells[1].paragraphs[0], meta.get(key, ""), 11)
        cells[0].width, cells[1].width = Cm(4), Cm(10)
    document.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def revision_history(document: Document, meta: dict[str, str]) -> None:
    p = document.add_paragraph()
    run = p.add_run("Histórico de revisões")
    run.bold = True
    run.font.size = Pt(14)
    rows = [
        ("Versão", "Data", "Descrição"),
        ("0.2", "Sprint 1", "DAS parcial (`docs/sprint-1/das-parcial.md`, repositório `poc-en-simulator`)"),
        ("1.0", meta.get("Data", ""), "Arquitetura como construída, resultado da sessão-piloto, implantação proposta na AWS, "
                                       "arquitetura-alvo do MVP e catálogo de técnicas de evolução"),
    ]
    table_from_rows(document, rows)
    p = document.add_paragraph()
    run = p.add_run("Sumário")
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_before = Pt(18)
    add_field(document.add_paragraph(), 'TOC \\o "1-3" \\h \\z \\u',
              "Clique com o botão direito e escolha “Atualizar campo” para gerar o sumário.")
    p = document.add_paragraph()
    run = p.add_run("Lista de figuras")
    run.bold = True
    run.font.size = Pt(14)
    p.paragraph_format.space_before = Pt(18)
    add_field(document.add_paragraph(), 'TOC \\h \\z \\c "Figura"',
              "Clique com o botão direito e escolha “Atualizar campo” para gerar a lista de figuras.")
    document.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def table_from_rows(document: Document, rows: list[tuple[str, ...]]) -> None:
    cols = max(len(r) for r in rows)
    table = document.add_table(rows=0, cols=cols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for index, row in enumerate(rows):
        cells = table.add_row().cells
        for col in range(cols):
            value = row[col] if col < len(row) else ""
            paragraph = cells[col].paragraphs[0]
            paragraph.paragraph_format.line_spacing = 1.0
            paragraph.paragraph_format.space_after = Pt(0)
            add_inline(paragraph, value, 9, bold=index == 0)
            if index == 0:
                set_cell_fill(cells[col], HEADER_FILL)
        if index == 0:
            repeat_header(table.rows[0])
    document.add_paragraph().paragraph_format.space_after = Pt(0)


def split_row(line: str) -> tuple[str, ...]:
    return tuple(cell.strip() for cell in line.strip().strip("|").split("|"))


def figure(document: Document, alt: str, path: str, number: int) -> None:
    label = re.sub(r"^Figura\s+\d+\s*[—-]\s*", "", alt)
    p = document.add_paragraph(style="Caption")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.add_run("Figura ")
    add_field(p, "SEQ Figura \\* ARABIC", str(number))
    p.add_run(f" — {label}")
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(str(BASE / path), width=Cm(16))
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Fonte: elaborado pelo autor (2026).")
    run.font.size = Pt(10)


def body(document: Document, lines: list[str]) -> None:
    in_references = False
    buffer: list[str] = []
    figures = 0
    i = 0

    def flush() -> None:
        if not buffer:
            return
        text = " ".join(s.strip() for s in buffer)
        p = document.add_paragraph()
        if in_references:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = Pt(12)
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_inline(p, text)
        buffer.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        heading = re.match(r"^(#{2,4})\s+(.*)", stripped)
        if heading:
            flush()
            level = len(heading.group(1)) - 1
            document.add_heading(heading.group(2), level=level)
            in_references = heading.group(2).endswith("Referências")
        elif stripped in ("", "---"):
            flush()
        elif stripped.startswith(">"):
            flush()
            if "remover este aviso" not in stripped:
                p = document.add_paragraph()
                add_inline(p, stripped.lstrip("> ").strip())
                for run in p.runs:
                    run.italic = True
        elif stripped.startswith("!["):
            flush()
            match = re.match(r"!\[(.*?)\]\((.*?)\)", stripped)
            if match:
                figures += 1
                figure(document, match.group(1), match.group(2), figures)
        elif stripped.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not re.match(r"^\|[\s:|-]+\|$", lines[i].strip()):
                    rows.append(split_row(lines[i]))
                i += 1
            table_from_rows(document, rows)
            continue
        elif re.match(r"^[-*]\s+", stripped):
            flush()
            p = document.add_paragraph(style="List Bullet")
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_after = Pt(3)
            add_inline(p, re.sub(r"^[-*]\s+", "", stripped))
        elif re.match(r"^\d+\.\s+", stripped):
            flush()
            number, text = re.match(r"^(\d+)\.\s+(.*)", stripped).groups()
            p = document.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1)
            p.paragraph_format.first_line_indent = Cm(-0.6)
            p.paragraph_format.space_after = Pt(3)
            p.add_run(f"{number}. ")
            add_inline(p, text)
        else:
            buffer.append(stripped)
        i += 1
    flush()


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    split = lines.index("---")
    title, meta_list = parse_metadata(lines[:split])
    meta = dict(meta_list)
    meta["Versão"] = meta.get("Versão", "").replace(" — rascunho para revisão", "")

    document = Document()
    configure(document)
    header_footer(document.sections[0], f"DAS — {meta.get('Projeto', '')}")
    cover(document, title, meta)
    revision_history(document, meta)
    body(document, lines[split + 1:])
    document.save(OUTPUT)
    print("DOCX gravado em", OUTPUT)


if __name__ == "__main__":
    main()
