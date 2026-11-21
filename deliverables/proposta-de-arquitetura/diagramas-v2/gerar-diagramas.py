"""Gera os diagramas do DAS v1 em SVG e PNG.

Uso: python3 gerar-diagramas.py
Requer cairosvg (pip install cairosvg) apenas para a conversão em PNG; sem ele, só os SVG são gravados.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent
FONT = "DejaVu Sans, Noto Sans, Arial, sans-serif"

STYLE = {
    "person": {"fill": "#0B3B60", "stroke": "#072A45", "text": "#FFFFFF", "sub": "#CFE0F1"},
    "system": {"fill": "#1168BD", "stroke": "#0B4884", "text": "#FFFFFF", "sub": "#D6E6F7"},
    "container": {"fill": "#438DD5", "stroke": "#2F6FAE", "text": "#FFFFFF", "sub": "#E3EEF9"},
    "component": {"fill": "#85BBF0", "stroke": "#5A97D3", "text": "#0B2540", "sub": "#173A5E"},
    "store": {"fill": "#438DD5", "stroke": "#2F6FAE", "text": "#FFFFFF", "sub": "#E3EEF9"},
    "external": {"fill": "#7B8089", "stroke": "#5C6068", "text": "#FFFFFF", "sub": "#EEEEEE"},
    "infra": {"fill": "#FFFFFF", "stroke": "#E07B00", "text": "#232F3E", "sub": "#4A5563"},
    "infra-app": {"fill": "#438DD5", "stroke": "#2F6FAE", "text": "#FFFFFF", "sub": "#E3EEF9"},
    "future": {"fill": "#FFFFFF", "stroke": "#8A9099", "text": "#3A4250", "sub": "#5A6270"},
    "note": {"fill": "#FFF8E1", "stroke": "#E0C068", "text": "#3A3220", "sub": "#3A3220"},
}

EDGE = "#4A5568"


def text_width(text: str, size: float, bold: bool = False) -> float:
    return len(text) * size * (0.64 if bold else 0.58)


def wrap(text: str, width: float, size: float, bold: bool = False) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if text_width(candidate, size, bold) <= width or not current:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


class Diagram:
    def __init__(self, name: str, width: int, height: int, title: str, subtitle: str = "") -> None:
        self.name = name
        self.width = width
        self.height = height
        self.parts: list[str] = []
        self.overlay: list[str] = []
        self.parts.append(f'<rect width="{width}" height="{height}" fill="#FFFFFF"/>')
        self.text(32, 44, title, 24, "#14202E", bold=True, anchor="start")
        if subtitle:
            self.text(32, 72, subtitle, 14, "#5A6270", anchor="start")

    def text(self, x, y, value, size, color, bold=False, italic=False, anchor="middle", layer=None):
        weight = ' font-weight="700"' if bold else ""
        style = ' font-style="italic"' if italic else ""
        target = self.parts if layer is None else layer
        target.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" fill="{color}"'
            f'{weight}{style} text-anchor="{anchor}">{escape(value)}</text>'
        )

    def boundary(self, x, y, w, h, label, kind="", color="#6B7280", dash="8 6"):
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" '
            f'stroke="{color}" stroke-width="1.6" stroke-dasharray="{dash}"/>'
        )
        self.text(x + 16, y + 24, label, 14, "#2D3748", bold=True, anchor="start")
        if kind:
            self.text(x + 16, y + 42, kind, 12, "#5A6270", anchor="start")

    def box(self, x, y, w, h, kind, title, tech="", desc="", dashed=False):
        st = STYLE[kind]
        dash = ' stroke-dasharray="7 5"' if dashed or kind == "future" else ""
        if kind == "store":
            ry = 12
            self.parts.append(
                f'<path d="M{x},{y + ry} a{w / 2},{ry} 0 0,0 {w},0 v{h - 2 * ry} '
                f'a{w / 2},{ry} 0 0,1 {-w},0 z" fill="{st["fill"]}" stroke="{st["stroke"]}" stroke-width="1.6"/>'
            )
            self.parts.append(
                f'<ellipse cx="{x + w / 2}" cy="{y + ry}" rx="{w / 2}" ry="{ry}" '
                f'fill="{st["fill"]}" stroke="{st["stroke"]}" stroke-width="1.6"/>'
            )
            top = y + 2 * ry + 4
        else:
            self.parts.append(
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{st["fill"]}" '
                f'stroke="{st["stroke"]}" stroke-width="{2.2 if kind in ("infra", "future") else 1.6}"{dash}/>'
            )
            top = y
        if kind == "person":
            cx = x + w / 2
            self.parts.append(
                f'<circle cx="{cx}" cy="{y - 4}" r="26" fill="{st["fill"]}" stroke="{st["stroke"]}" stroke-width="1.6"/>'
            )
            top = y + 16

        title_lines = wrap(title, w - 24, 15, bold=True)
        tech_lines = wrap(tech, w - 24, 11.5) if tech else []
        desc_lines = wrap(desc, w - 24, 12) if desc else []
        block = len(title_lines) * 19 + len(tech_lines) * 15 + (6 if tech_lines else 0)
        block += (8 + len(desc_lines) * 16) if desc_lines else 0
        inner_h = h - (top - y)
        cy = top + max(14, (inner_h - block) / 2) + 14
        for line in title_lines:
            self.text(x + w / 2, cy, line, 15, st["text"], bold=True)
            cy += 19
        if tech_lines:
            cy += 1
            for line in tech_lines:
                self.text(x + w / 2, cy, line, 11.5, st["sub"])
                cy += 15
            cy += 5
        if desc_lines:
            cy += 8
            for line in desc_lines:
                self.text(x + w / 2, cy, line, 12, st["text"])
                cy += 16

    def note(self, x, y, w, h, title, lines):
        st = STYLE["note"]
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{st["fill"]}" '
            f'stroke="{st["stroke"]}" stroke-width="1.4"/>'
        )
        self.text(x + 16, y + 26, title, 13.5, st["text"], bold=True, anchor="start")
        cy = y + 50
        for line in lines:
            for i, part in enumerate(wrap(line, w - 44, 12.5)):
                prefix = "• " if i == 0 else "   "
                self.text(x + 18, cy, prefix + part, 12.5, st["text"], anchor="start")
                cy += 18
            cy += 3

    def edge(self, points, label="", tech="", at=None, dashed=False, align="middle", color=EDGE):
        path = "M" + " L".join(f"{px},{py}" for px, py in points)
        dash = ' stroke-dasharray="6 5"' if dashed else ""
        self.parts.append(
            f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1.7"{dash} marker-end="url(#arrow)"/>'
        )
        if label:
            if at is None:
                (x1, y1), (x2, y2) = points[len(points) // 2 - 1], points[len(points) // 2]
                at = ((x1 + x2) / 2, (y1 + y2) / 2)
            self.label(at[0], at[1], label, tech, align)

    def label(self, x, y, value, tech="", align="middle"):
        lines = value.split("\n")
        rows = [(line, 12, False) for line in lines]
        if tech:
            rows.append((tech, 11, True))
        width = max(text_width(r[0], r[1]) for r in rows) + 12
        height = len(rows) * 15 + 6
        if align == "start":
            left = x
        elif align == "end":
            left = x - width
        else:
            left = x - width / 2
        top = y - height / 2
        self.overlay.append(
            f'<rect x="{left:.1f}" y="{top:.1f}" width="{width:.1f}" height="{height:.1f}" rx="4" '
            f'fill="#FFFFFF" fill-opacity="0.94"/>'
        )
        cy = top + 15
        for value_line, size, italic in rows:
            self.text(left + width / 2, cy, value_line, size, "#2D3748" if not italic else "#5A6270",
                      italic=italic, layer=self.overlay)
            cy += 15

    def legend(self, y, items, x=32):
        self.text(x, y, "Legenda", 13, "#2D3748", bold=True, anchor="start")
        cx = x + 80
        for kind, label in items:
            if kind == "edge":
                self.parts.append(
                    f'<path d="M{cx},{y - 5} L{cx + 34},{y - 5}" stroke="{EDGE}" stroke-width="1.7" marker-end="url(#arrow)"/>'
                )
            elif kind == "edge-dashed":
                self.parts.append(
                    f'<path d="M{cx},{y - 5} L{cx + 34},{y - 5}" stroke="{EDGE}" stroke-width="1.7" '
                    f'stroke-dasharray="6 5" marker-end="url(#arrow)"/>'
                )
            elif kind == "boundary":
                self.parts.append(
                    f'<rect x="{cx}" y="{y - 14}" width="34" height="18" rx="4" fill="none" '
                    f'stroke="#6B7280" stroke-width="1.4" stroke-dasharray="5 4"/>'
                )
            else:
                st = STYLE[kind]
                dash = ' stroke-dasharray="5 4"' if kind == "future" else ""
                self.parts.append(
                    f'<rect x="{cx}" y="{y - 14}" width="34" height="18" rx="4" fill="{st["fill"]}" '
                    f'stroke="{st["stroke"]}" stroke-width="1.6"{dash}/>'
                )
            self.text(cx + 42, y, label, 12, "#2D3748", anchor="start")
            cx += 42 + text_width(label, 12) + 30

    def footer(self, value):
        self.text(32, self.height - 18, value, 11.5, "#6B7280", anchor="start")

    def save(self) -> None:
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}">'
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" '
            f'markerHeight="9" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{EDGE}"/>'
            "</marker></defs>" + "".join(self.parts) + "".join(self.overlay) + "</svg>"
        )
        svg_path = OUT / f"{self.name}.svg"
        svg_path.write_text(svg, encoding="utf-8")
        try:
            import cairosvg
        except ImportError:
            return
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / f"{self.name}.png"), scale=2)


def visao_geral() -> None:
    d = Diagram(
        "00-visao-geral",
        1660,
        900,
        "Visão geral — turno de voz em cascata (ASR → LLM → TTS)",
        "Prova de conceito local: um turno é uma requisição HTTP síncrona; o histórico fica só na memória do processo.",
    )
    d.box(30, 220, 170, 130, "person", "Pessoa", desc="Fala ao microfone e ouve a entrevistadora")
    d.box(270, 200, 220, 150, "container", "Interface web", "[React, Vite]", "Cenário único; grava a resposta e reproduz o áudio")
    d.boundary(550, 110, 1080, 480, "API local (BFF)", "[Python 3.12, FastAPI] — orquestra o turno em sequência")
    d.box(630, 200, 250, 150, "component", "1. Reconhecimento (ASR)", "[gemini-3.5-transcribe, VERBATIM]", "Converte a fala em texto literal, com hesitações")
    d.box(980, 200, 250, 150, "component", "2. Diálogo (LLM)", "[gemini-3.5-flash-lite]", "Gera a próxima pergunta, sem corrigir a pessoa")
    d.box(1330, 200, 250, 150, "component", "3. Síntese (TTS)", "[gemini-3.8-flash-lite-tts, voz Kore]", "Converte a fala da entrevistadora em áudio WAV")
    d.box(980, 420, 250, 120, "store", "Histórico da sessão", "[memória do processo]", "Apenas papel e texto")
    d.box(630, 410, 250, 140, "component", "Retorno em três blocos", "[gemini-3.5-flash-lite]", "Pontos positivos, de melhoria e próximo passo")

    d.edge([(200, 285), (270, 285)], "fala", at=(235, 268))
    d.edge([(490, 290), (630, 290)], "áudio do turno", "[HTTP multipart]", at=(560, 318))
    d.edge([(880, 275), (980, 275)], "transcrição", at=(930, 258))
    d.edge([(1230, 275), (1330, 275)], "próxima fala", at=(1280, 258))
    d.edge([(1455, 200), (1455, 160), (380, 160), (380, 200)], "texto e áudio da entrevistadora", "[JSON, WAV em base64]", at=(1250, 160))
    d.edge([(1070, 350), (1070, 420)], "acrescenta turnos", at=(1062, 385), align="end")
    d.edge([(1140, 420), (1140, 350)], "lê histórico", at=(1148, 385), align="start")
    d.edge([(980, 480), (880, 480)], "ao encerrar", at=(930, 463))
    d.edge([(420, 350), (420, 470), (630, 470)], "encerrar sessão", "[HTTP]", at=(525, 500))
    d.edge([(755, 550), (755, 620), (340, 620), (340, 350)], "três blocos", "[JSON]", at=(550, 620))

    d.box(980, 660, 600, 100, "external", "API Gemini", "[Sistema externo — camada gratuita]", "Três chamadas por turno e uma no encerramento")
    d.edge([(1280, 590), (1280, 660)], "generateContent", "[HTTPS]", at=(1290, 625), align="start")
    d.note(30, 660, 880, 118, "Restrições que o desenho respeita", [
        "O áudio da pessoa é descartado logo após a transcrição; a transcrição fica em memória até o encerramento (RC-04).",
        "Sem banco de dados, fila, cadastro ou canal bidirecional contínuo; a chave do modelo fica só no processo da API (RC-08).",
    ])
    d.legend(820, [("person", "Pessoa"), ("container", "Contêiner"), ("component", "Componente"),
                   ("store", "Armazenamento"), ("external", "Sistema externo"), ("boundary", "Limite"),
                   ("edge", "Fluxo (sentido da seta)")])
    d.footer("Fonte: código do repositório poc-en-simulator (api/app.py, api/gemini_client.py) e DAS v0.2. Nomes de modelos conforme api/settings.py.")
    d.save()


def c1_contexto() -> None:
    d = Diagram(
        "01-c1-contexto",
        1440,
        720,
        "C1 — Diagrama de contexto do sistema",
        "Escopo: simulador de entrevista em inglês por voz, prova de conceito da Sprint 3.",
    )
    d.box(60, 250, 300, 170, "person", "Pessoa candidata", "[Pessoa — quem executa o teste]",
          "Profissional de tecnologia que ensaia entrevista de emprego em inglês, com microfone e alto-falantes")
    d.box(560, 230, 340, 210, "system", "Simulador de entrevista em inglês por voz", "[Sistema de software]",
          "Conduz a entrevista no cenário único, transcreve a fala, gera a próxima pergunta, sintetiza a voz e devolve retorno em três blocos ao encerrar")
    d.box(1100, 250, 300, 170, "external", "API Gemini", "[Sistema externo — Google]",
          "Reconhecimento de fala, modelo de diálogo e síntese de voz na camada gratuita")
    d.edge([(360, 335), (560, 335)], "Responde por voz e\nouve a entrevistadora", "[navegador, microfone]", at=(460, 300))
    d.edge([(900, 335), (1100, 335)], "Envia áudio e texto;\nrecebe transcrição,\nfala e áudio", "[HTTPS, generateContent]", at=(1000, 292))
    d.note(60, 500, 1340, 110, "Fora do contexto da versão 1 (decisão de escopo)", [
        "Não há provedor de identidade, banco de dados, repositório de conteúdo nem outros cenários. A camada gratuita pode usar o conteúdo enviado para melhoria dos produtos do provedor (GOOGLE, 2026); por isso a sessão usa somente a voz de quem executa o teste (RC-09).",
    ])
    d.legend(660, [("person", "Pessoa"), ("system", "Sistema em escopo"), ("external", "Sistema externo"),
                   ("edge", "Relação (sentido da seta)")])
    d.save()


def c2_conteineres() -> None:
    d = Diagram(
        "02-c2-conteineres",
        1620,
        900,
        "C2 — Diagrama de contêineres (prova de conceito local, como construída)",
        "Escopo: simulador de entrevista em inglês por voz. Unidades executáveis e armazenamentos.",
    )
    d.box(110, 130, 260, 120, "person", "Pessoa candidata", "[Pessoa]", "Usa o navegador da própria máquina")
    d.boundary(40, 300, 1080, 470, "Máquina local", "[Limite de implantação: 127.0.0.1]")
    d.box(80, 380, 360, 190, "container", "Interface web", "[Contêiner: JavaScript, React, Vite — porta 5173]",
          "Exibe o cenário único, captura o microfone (MediaRecorder, WebM/Opus), reproduz a voz e mostra os três blocos")
    d.box(660, 380, 400, 190, "container", "API local (BFF)", "[Contêiner: Python 3.12, FastAPI, Uvicorn — porta 8765]",
          "Um turno por requisição: orquestra ASR, diálogo e síntese; guarda a chave do modelo e o histórico só em memória")
    d.box(680, 640, 360, 110, "store", "Instruções de sistema", "[Arquivos de texto: prompts/]",
          "entrevistador.txt e feedback.txt")
    d.box(1260, 380, 320, 190, "external", "API Gemini", "[Sistema externo — camada gratuita]",
          "gemini-3.5-transcribe (ASR); gemini-3.5-flash-lite (diálogo e retorno); gemini-3.8-flash-lite-tts (síntese)")

    d.edge([(330, 250), (330, 380)], "Usa no navegador e\nfala ao microfone", "[HTTP local]", at=(342, 322), align="start")
    d.edge([(440, 440), (660, 440)], "Envia áudio do turno;\nabre e encerra a sessão", "[HTTP, multipart e JSON]", at=(550, 410))
    d.edge([(660, 520), (440, 520)], "Devolve texto, áudio WAV\n(base64) e três blocos", "[JSON]", at=(550, 545))
    d.edge([(860, 570), (860, 640)], "Lê a cada chamada", "[sistema de arquivos]", at=(870, 605), align="start")
    d.edge([(1060, 475), (1260, 475)], "Transcreve, gera fala\ne sintetiza voz", "[HTTPS, REST e SDK google-genai]", at=(1160, 440))
    d.note(1160, 620, 420, 150, "Restrições aplicadas", [
        "Sem banco de dados, fila ou cadastro.",
        "GEMINI_API_KEY só no ambiente do processo da API (RC-08).",
        "Áudio da pessoa não é gravado em disco (RC-04).",
    ])
    d.legend(830, [("person", "Pessoa"), ("container", "Contêiner"), ("store", "Armazenamento"),
                   ("external", "Sistema externo"), ("boundary", "Limite de implantação"), ("edge", "Relação")])
    d.save()


def c3_componentes() -> None:
    d = Diagram(
        "03-c3-componentes",
        1640,
        1140,
        "C3 — Diagrama de componentes da API local (BFF)",
        "Escopo: contêiner API local. Componentes conforme os módulos existentes em api/.",
    )
    d.box(30, 400, 220, 160, "container", "Interface web", "[Contêiner: React]", "Chama a API pela rede local")
    d.boundary(310, 100, 980, 930, "API local (BFF)", "[Contêiner: Python 3.12, FastAPI]")
    d.box(360, 170, 260, 610, "component", "Rotas HTTP", "[Componente: api/app.py, FastAPI]",
          "GET /api/health\n\nPOST /api/sessions\n\nPOST /api/sessions/{id}/turns\n\nPOST /api/sessions/{id}/end\n\n"
          "Valida o limite de 8 MB e zera o áudio logo após o reconhecimento. Traduz falhas do provedor em HTTP 502 ou 503.")
    d.box(360, 870, 260, 120, "component", "Repositório de sessões", "[Componente: api/sessions.py, dict e Lock]",
          "Guarda papel e texto; remove a sessão ao encerrar")
    d.boundary(700, 130, 480, 690, "Cliente do provedor", "[api/gemini_client.py]", color="#5A97D3", dash="4 4")
    d.box(730, 190, 420, 130, "component", "Transcrição", "[transcribe_audio — REST generateContent]",
          "Modo VERBATIM, idioma en-US, sem instrução de sistema")
    d.box(730, 350, 420, 130, "component", "Diálogo", "[interviewer_reply — SDK google-genai]",
          "Instrução da entrevistadora mais histórico")
    d.box(730, 510, 420, 130, "component", "Síntese", "[synthesize_speech — REST generateContent]",
          "responseModalities AUDIO, voz Kore")
    d.box(730, 670, 420, 130, "component", "Retorno", "[generate_feedback — SDK google-genai]",
          "Instrução de retorno mais transcrição acumulada")
    d.box(730, 880, 420, 110, "component", "Separador do retorno", "[Componente: api/feedback.py]",
          "Extrai somente os três blocos; não inventa bloco ausente")
    d.box(1370, 190, 240, 610, "external", "API Gemini", "[Sistema externo]",
          "gemini-3.5-transcribe\n\ngemini-3.5-flash-lite\n\ngemini-3.8-flash-lite-tts")
    d.box(1370, 880, 240, 110, "store", "Instruções", "[Arquivos: prompts/]", "entrevistador.txt; feedback.txt")

    d.edge([(250, 480), (360, 480)], "requisições", "[HTTP, JSON]", at=(305, 450))
    d.edge([(620, 255), (730, 255)], "áudio", at=(675, 240))
    d.edge([(620, 415), (730, 415)], "histórico", at=(675, 400))
    d.edge([(620, 575), (730, 575)], "fala", at=(675, 560))
    d.edge([(620, 735), (730, 735)], "transcrição", at=(675, 720))
    d.edge([(490, 780), (490, 870)], "cria, lê e remove", at=(500, 825), align="start")
    d.edge([(940, 800), (940, 880)], "texto bruto", at=(950, 840), align="start")
    d.edge([(1150, 255), (1370, 255)], "áudio → texto", "[HTTPS]", at=(1260, 232))
    d.edge([(1150, 415), (1370, 415)], "histórico → fala", "[HTTPS]", at=(1260, 392))
    d.edge([(1150, 575), (1370, 575)], "texto → áudio WAV", "[HTTPS]", at=(1260, 552))
    d.edge([(1150, 735), (1370, 735)], "transcrição → blocos", "[HTTPS]", at=(1260, 712))
    d.edge([(1150, 780), (1230, 780), (1230, 935), (1370, 935)], "lê instruções", "[load_prompt]", at=(1300, 900))
    d.legend(1075, [("container", "Contêiner"), ("component", "Componente"), ("store", "Armazenamento"),
                    ("external", "Sistema externo"), ("boundary", "Limite"), ("edge", "Chamada")])
    d.save()


def dinamico_turno() -> None:
    d = Diagram(
        "04-dinamico-turno",
        1600,
        1250,
        "Diagrama dinâmico — um turno de voz e o encerramento da sessão",
        "Sequência real do código: as três chamadas ao provedor ocorrem em série dentro da mesma requisição.",
    )
    lanes = [
        (130, "person", "Pessoa", "[quem executa o teste]"),
        (390, "container", "Interface web", "[React]"),
        (650, "container", "API local", "[FastAPI, BFF]"),
        (910, "external", "ASR", "[gemini-3.5-transcribe]"),
        (1170, "external", "Diálogo e retorno", "[gemini-3.5-flash-lite]"),
        (1430, "external", "Síntese", "[gemini-3.8-flash-lite-tts]"),
    ]
    xs = {}
    for cx, kind, title, tech in lanes:
        xs[title] = cx
        d.parts.append(f'<path d="M{cx},165 L{cx},1170" stroke="#A0AEC0" stroke-width="1.4" stroke-dasharray="5 5"/>')
        d.box(cx - 115, 100, 230, 66, "container" if kind == "person" else kind, title, tech)

    P, UI, API, ASR, LLM, TTS = (xs[k] for k in ("Pessoa", "Interface web", "API local", "ASR", "Diálogo e retorno", "Síntese"))

    def frame(y1, y2, label):
        d.parts.append(f'<rect x="40" y="{y1}" width="1520" height="{y2 - y1}" rx="8" fill="#F7FAFC" fill-opacity="0.55" stroke="#CBD5E0" stroke-width="1.2"/>')
        w = text_width(label, 12.5, True) + 20
        d.parts.append(f'<rect x="40" y="{y1}" width="{w}" height="24" rx="6" fill="#E2E8F0"/>')
        d.text(50, y1 + 17, label, 12.5, "#2D3748", bold=True, anchor="start")

    def msg(y, a, b, label, reply=False):
        d.edge([(a, y), (b + (-6 if b > a else 6), y)], dashed=reply)
        d.label((a + b) / 2, y - 13, label)

    def self_msg(y, x, label):
        d.parts.append(
            f'<path d="M{x},{y - 8} L{x + 34},{y - 8} L{x + 34},{y + 10} L{x + 6},{y + 10}" fill="none" '
            f'stroke="{EDGE}" stroke-width="1.7" marker-end="url(#arrow)"/>'
        )
        d.label(x + 44, y + 1, label, align="start")

    frame(190, 845, "Turno — repete-se a cada resposta")
    msg(240, P, UI, "1. Grava a resposta")
    msg(290, UI, API, "2. POST /turns (áudio WebM/Opus)")
    self_msg(340, API, "3. Valida tamanho (até 8 MB)")
    msg(395, API, ASR, "4. generateContent (áudio, VERBATIM, en-US)")
    msg(445, ASR, API, "5. Transcrição (pode vir vazia)", reply=True)
    self_msg(495, API, "6. Zera o áudio da pessoa")
    msg(550, API, LLM, "7. Instrução da entrevistadora + histórico + transcrição")
    msg(600, LLM, API, "8. Próxima fala, sem correção", reply=True)
    msg(655, API, TTS, "9. generateContent (texto, voz Kore)")
    msg(705, TTS, API, "10. Áudio WAV", reply=True)
    self_msg(750, API, "11. Acrescenta os dois turnos ao histórico")
    msg(800, API, UI, "12. Transcrição, fala e áudio", reply=True)
    msg(830, UI, P, "13. Reproduz a voz", reply=True)

    frame(880, 1160, "Encerramento — uma vez por sessão")
    msg(935, P, UI, "14. Clica em End interview")
    msg(970, UI, API, "15. POST /end")
    self_msg(1005, API, "16. Remove a sessão da memória")
    msg(1050, API, LLM, "17. Instrução de retorno + transcrição acumulada")
    msg(1095, LLM, API, "18. Texto com três blocos", reply=True)
    msg(1140, API, UI, "19. Três blocos (JSON)", reply=True)

    d.legend(1215, [("edge", "Chamada"), ("edge-dashed", "Resposta")])
    d.text(560, 1215, "Latência do turno = ASR + diálogo + síntese + rede. Não foi medida por etapa na sessão-piloto de 20 de novembro de 2026.",
           12, "#5A6270", anchor="start")
    d.save()


def implantacao_aws() -> None:
    d = Diagram(
        "05-implantacao-aws",
        1720,
        1010,
        "Diagrama de implantação — publicação proposta na AWS (opcional na Sprint 3)",
        "Proposta não implantada. Mesmo código da API, executado sem estado; custo previsto dentro do Free plan.",
    )
    d.box(40, 410, 210, 130, "person", "Pessoa candidata", "[Navegador]", "Acessa por HTTPS")
    d.boundary(310, 100, 1110, 790, "Amazon Web Services", "[Conta no Free plan — região a definir]", color="#E07B00")
    d.note(350, 160, 1030, 140, "Ajustes no código exigidos por esta implantação", [
        "API sem estado: o navegador envia o histórico textual a cada turno, porque instâncias Lambda não compartilham memória.",
        "Endereço da API e CORS configuráveis por ambiente (hoje fixos em 127.0.0.1).",
        "Limite do áudio reduzido para até 4 MB: o payload síncrono da Lambda é de 6 MB e o corpo binário chega codificado em base64.",
        "Tempos-limite por etapa cuja soma fique abaixo de 30 s, o teto da integração do HTTP API (hoje 90 s por chamada).",
    ])
    o = -60
    d.box(350, 440 + o, 300, 170, "infra", "Amazon CloudFront", "[Distribuição — HTTPS]",
          "Entrega a interface e encaminha /api/* na mesma origem, sem CORS entre domínios")
    d.box(350, 720 + o, 300, 150, "infra", "Amazon S3", "[Bucket privado, acesso por OAC]", "Arquivos estáticos do build Vite")
    d.box(760, 440 + o, 290, 170, "infra", "Amazon API Gateway", "[HTTP API]",
          "Rota /api/*; limite de requisições por rota; integração de até 30 s")
    d.box(760, 700 + o, 290, 200, "infra-app", "API local (BFF) em AWS Lambda", "[Python 3.12, FastAPI, Lambda Web Adapter]",
          "Mesmo código; histórico recebido na requisição; nada gravado")
    d.box(1130, 440 + o, 250, 150, "infra", "AWS Systems Manager", "[Parameter Store, SecureString]", "GEMINI_API_KEY")
    d.box(1130, 730 + o, 250, 150, "infra", "Amazon CloudWatch", "[Logs e métricas]",
          "Latência por etapa e erros; sem conteúdo de fala")
    d.box(1490, 700 + o, 200, 200, "external", "API Gemini", "[Sistema externo]", "ASR, diálogo e síntese")

    d.edge([(250, 475), (350, 475)], "HTTPS", at=(300, 458))
    d.edge([(500, 610 + o), (500, 720 + o)], "arquivos estáticos", "[OAC]", at=(510, 665 + o), align="start")
    d.edge([(650, 525 + o), (760, 525 + o)], "/api/*", "[HTTPS]", at=(705, 500 + o))
    d.edge([(905, 610 + o), (905, 700 + o)], "invoca", "[proxy]", at=(915, 655 + o), align="start")
    d.edge([(1050, 740 + o), (1090, 740 + o), (1090, 515 + o), (1130, 515 + o)], "lê a chave", "[na inicialização]", at=(1090, 650 + o))
    d.edge([(1050, 805 + o), (1130, 805 + o)], "registra", at=(1090, 788 + o))
    d.edge([(905, 900 + o), (905, 935), (1590, 935), (1590, 900 + o)], "generateContent: 3 chamadas por turno", "[HTTPS, internet]", at=(1250, 935))
    d.legend(980, [("person", "Pessoa"), ("infra", "Serviço AWS"), ("infra-app", "Contêiner da aplicação"),
                    ("external", "Sistema externo"), ("boundary", "Limite da conta"), ("edge", "Fluxo")])
    d.save()


def mapa_evolucao() -> None:
    d = Diagram(
        "06-mapa-de-evolucao",
        1640,
        700,
        "Mapa de evolução — o que entra na arquitetura e sob qual condição",
        "Os elementos tracejados não pertencem à versão 1; cada um depende de um gatilho verificável.",
    )
    cols = [
        (40, "container", False, "Versão 1 — prova de conceito local", "[implementada e validada na sessão-piloto]", [
            "Interface web em React; API BFF em Python 3.12",
            "Turno síncrono em cascata: ASR → LLM → TTS",
            "Histórico só em memória; áudio descartado após o ASR",
            "Retorno em três blocos ao encerrar",
            "Provedor único: API Gemini, camada gratuita",
        ]),
        (580, "infra", False, "Versão 1.1 — publicação opcional", "[gatilho: entregas 1 a 3 da Sprint 3 concluídas e tempo disponível]", [
            "CloudFront e S3 para a interface",
            "API Gateway HTTP API e Lambda para a API",
            "Parameter Store para a chave; CloudWatch para latência por etapa",
            "API sem estado; uso restrito a quem executa o teste (RC-09)",
            "Portas separadas para ASR, LLM e TTS no código",
        ]),
        (1120, "future", True, "Versão 2 — produto", "[gatilho: teste com usuários externos e orçamento]", [
            "Camada paga do provedor ou Amazon Transcribe, Bedrock e Polly, para que o conteúdo não seja usado em treino",
            "Amazon Cognito, se houver contas de usuário",
            "Amazon DynamoDB com consentimento e TTL, se houver histórico",
            "Amazon SQS e worker, se a avaliação demorar além do turno",
            "Streaming por frase ou canal bidirecional, se a latência medida exigir",
        ]),
    ]
    for x, kind, dashed, title, trigger, items in cols:
        st = STYLE[kind]
        dash = ' stroke-dasharray="8 6"' if dashed else ""
        head_fill = st["fill"] if kind != "infra" else "#FFF3E6"
        head_text = st["text"] if kind not in ("infra",) else "#232F3E"
        if kind == "future":
            head_fill, head_text = "#F1F3F5", "#3A4250"
        d.parts.append(f'<rect x="{x}" y="110" width="480" height="440" rx="14" fill="#FFFFFF" stroke="{st["stroke"]}" stroke-width="2"{dash}/>')
        d.parts.append(f'<path d="M{x},124 a14,14 0 0,1 14,-14 h452 a14,14 0 0,1 14,14 v86 h-480 z" fill="{head_fill}"/>')
        d.text(x + 240, 148, title, 16, head_text, bold=True)
        ty = 172
        for line in wrap(trigger, 440, 12):
            d.text(x + 240, ty, line, 12, head_text, italic=True)
            ty += 16
        cy = 250
        for item in items:
            lines = wrap(item, 420, 13.5)
            d.parts.append(f'<circle cx="{x + 30}" cy="{cy - 5}" r="4" fill="{st["stroke"]}"/>')
            for line in lines:
                d.text(x + 46, cy, line, 13.5, "#1F2937", anchor="start")
                cy += 20
            cy += 18
    d.edge([(520, 330), (580, 330)])
    d.edge([(1060, 330), (1120, 330)], dashed=True)
    d.note(40, 580, 1560, 70, "Princípio de evolução", [
        "Cada elemento novo entra somente quando um requisito, uma medição ou uma decisão registrada o justificar; a versão 1 não depende de nenhum deles.",
    ])
    d.save()


if __name__ == "__main__":
    visao_geral()
    c1_contexto()
    c2_conteineres()
    c3_componentes()
    dinamico_turno()
    implantacao_aws()
    mapa_evolucao()
    print("Diagramas gravados em", OUT)
