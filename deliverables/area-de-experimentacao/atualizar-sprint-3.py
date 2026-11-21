#!/usr/bin/env python3
"""Completa a Sprint 3 no relatório: sessão-piloto, nota de privacidade e DAS v1.

A publicação em nuvem não foi executada e permanece descrita como proposta.
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.text.paragraph import Paragraph

DOC = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "Relatorio_Projeto_Aplicado_Luiz_Victor.docx"
)
ASSETS = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "area-de-experimentacao/assets"
)
DIAG = Path(
    "/home/luiz-victor/dev/applied-project-planning/deliverables/"
    "proposta-de-arquitetura/diagramas-v2"
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
    if paragraph.runs:
        run = paragraph.runs[0]
        run.text = text
        for extra in paragraph.runs[1:]:
            extra.text = ""
    else:
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


def _new_after(anchor) -> Paragraph:
    element = OxmlElement("w:p")
    anchor._p.addnext(element)
    return Paragraph(element, anchor._parent)


def body_after(anchor, text, *, bold=False, italic=False) -> Paragraph:
    paragraph = _new_after(anchor)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(paragraph)
    _run(paragraph, text, bold=bold, italic=italic)
    return paragraph


def title_after(anchor, text) -> Paragraph:
    paragraph = _new_after(anchor)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(paragraph, after="80", before="200", line="360")
    _run(paragraph, text, bold=True)
    return paragraph


def caption_after(anchor, text) -> Paragraph:
    paragraph = _new_after(anchor)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(paragraph, after="240", before="80", line="276")
    _run(paragraph, text, bold=True, size=Pt(11))
    return paragraph


def picture_after(anchor, path: Path, width_cm: float) -> Paragraph:
    paragraph = _new_after(anchor)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(paragraph, after="40", before="160", line="240")
    paragraph.add_run().add_picture(str(path), width=Cm(width_cm))
    return paragraph


def heading_after(anchor, text, level: int, color) -> Paragraph:
    paragraph = _new_after(anchor)
    paragraph.style = f"Heading {level}"
    _run(paragraph, text, bold=True, color=color)
    return paragraph


def append_body(doc, text, *, bold=False) -> None:
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(paragraph)
    _run(paragraph, text, bold=bold)


def append_heading(doc, text, level: int, color) -> None:
    paragraph = doc.add_heading(text, level=level)
    for run in paragraph.runs:
        run.font.color.rgb = color


def append_title(doc, text) -> None:
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _spacing(paragraph, after="80", before="200", line="360")
    _run(paragraph, text, bold=True)


def replace_exact(doc: Document, old: str, new: str) -> None:
    found = False
    for paragraph in doc.paragraphs:
        if paragraph.text != old:
            continue
        _run(paragraph, new)
        found = True
        break
    if not found:
        raise SystemExit(f"Parágrafo não encontrado:\n{old[:120]}")


def fill_section(heading_text: str, blocks: list) -> None:
    heading = None
    for paragraph in doc.paragraphs:
        if paragraph.text != heading_text:
            continue
        sibling = paragraph._p.getnext()
        if sibling is None or sibling.tag != qn("w:p"):
            continue
        candidate = Paragraph(sibling, paragraph._parent)
        if candidate.text.startswith("A preencher"):
            heading = paragraph
            break
    if heading is None:
        raise SystemExit(f"Título não encontrado: {heading_text}")
    placeholder = None
    sibling = heading._p.getnext()
    if sibling is not None and sibling.tag == qn("w:p"):
        candidate = Paragraph(sibling, heading._parent)
        if candidate.text.startswith("A preencher"):
            placeholder = sibling
    anchor = heading
    for kind, payload in blocks:
        if kind == "title":
            anchor = title_after(anchor, payload)
        elif kind == "body":
            anchor = body_after(anchor, payload)
        elif kind == "caption":
            anchor = caption_after(anchor, payload)
        elif kind == "picture":
            path, width = payload
            anchor = picture_after(anchor, path, width)
        else:
            raise SystemExit(kind)
    if placeholder is not None:
        placeholder.getparent().remove(placeholder)


doc = Document(str(DOC))

replace_exact(
    doc,
    "O cronograma cobre 21 dias, de 2 a 22 de novembro de 2026, em três sprints de sete dias. "
    "Cada uma tem quatro entregas. O quadro Kanban acompanha o andamento. As Sprints 1 e 2 foram "
    "executadas; a Sprint 3 permanece pendente. A publicação em nuvem só entra na última, e somente "
    "se o fluxo local já estiver pronto. O detalhe da execução está no capítulo 2.",
    "O cronograma cobre 21 dias, de 2 a 22 de novembro de 2026, em três sprints de sete dias. "
    "Cada uma tem quatro entregas. O quadro Kanban acompanha o andamento. As Sprints 1 e 2 foram "
    "executadas. Na Sprint 3, a sessão-piloto, a nota de privacidade e o Documento de Arquitetura "
    "de Software (DAS) na versão 1 foram concluídos em 20 de novembro de 2026. A publicação em "
    "nuvem não foi realizada; a prova de conceito permanece local. O detalhe da execução está no "
    "capítulo 2.",
)

replace_exact(
    doc,
    "A área de experimentação registra o planejamento, a execução e o resultado das sprints da "
    "prova de conceito. O quadro Kanban previsto no escopo foi materializado no GitHub Projects "
    "do repositório poc-en-simulator, uma issue por entrega, com as etiquetas sprint-1 e sprint-2, "
    "conforme a Figura 11. As Sprints 1 e 2 foram executadas. A Sprint 3 permanece reservada à "
    "sessão-piloto, à nota de privacidade e ao Documento de Arquitetura de Software (DAS) na versão 1.",
    "A área de experimentação registra o planejamento, a execução e o resultado das sprints da "
    "prova de conceito. O quadro Kanban previsto no escopo foi materializado no GitHub Projects "
    "do repositório poc-en-simulator, uma issue por entrega, com as etiquetas sprint-1 e sprint-2, "
    "conforme a Figura 11. As Sprints 1 e 2 foram executadas. Na Sprint 3, a sessão-piloto, a nota "
    "de privacidade e o Documento de Arquitetura de Software (DAS) na versão 1 foram concluídos em "
    "20 de novembro de 2026. A publicação em nuvem não foi realizada.",
)

replace_exact(
    doc,
    "Período planejado: 16 a 22 de novembro de 2026. Esta sprint ainda não foi executada. Não há "
    "registro de sessão-piloto, nota de privacidade fechada, DAS na versão 1 nem publicação em "
    "nuvem a anexar.",
    "Período: 16 a 22 de novembro de 2026. As entregas 1, 2 e 3 foram executadas em 20 de novembro "
    "de 2026. A entrega 4, publicação em nuvem, não foi realizada. A prova de conceito permanece "
    "local. Essa publicação não é condição para concluir o objetivo.",
)

replace_exact(
    doc,
    "A definição da Sprint 3 consta da Figura 10. O quadro de acompanhamento consta da Figura 11. "
    "As quatro entregas previstas são: registro da sessão-piloto de cinco a dez minutos, com ao "
    "menos quatro turnos de fala reconhecidos; nota de privacidade; DAS versão 1; publicação em "
    "nuvem somente se as três entregas anteriores estiverem concluídas e ainda houver tempo.",
    "A definição da Sprint 3 consta da Figura 10. O quadro de acompanhamento consta da Figura 11. "
    "As quatro entregas previstas são: registro da sessão-piloto de cinco a dez minutos, com ao "
    "menos quatro turnos de fala reconhecidos; nota de privacidade; DAS versão 1; publicação em "
    "nuvem somente se as três entregas anteriores estiverem concluídas e ainda houver tempo. As "
    "três primeiras têm evidência de execução nesta seção. A quarta não foi executada.",
)

fill_section(
    "Evidência da execução de cada requisito:",
    [
        (
            "title",
            "1. Registro da sessão-piloto",
        ),
        (
            "body",
            "A sessão ocorreu na interface local, em http://127.0.0.1:5173, no cenário "
            "“Entrevista de emprego — Tecnologia”. O início foi o clique em “Start interview”. "
            "O encerramento foi o clique em “End interview”. O relógio local marcou 21:11:25 com "
            "a tela em “Starting”, durante o pedido da abertura, e 21:19:47 com a tela em "
            "“Processing”, depois do clique de encerramento. A duração medida foi de oito minutos "
            "e 22 segundos. A rota de encerramento respondeu 200.",
        ),
        (
            "body",
            "Antes da sessão oficial, o diagnóstico usou uma única captura. O modelo "
            "gemini-3.5-transcribe devolveu a frase no campo candidates[].content.parts[].text, "
            "que é o campo já lido pelo extrator em api/gemini_client.py. A transcrição extraída "
            "foi “I am a software engineer and I work with Python and web”. O extrator não foi "
            "alterado e não houve segunda captura de diagnóstico. Essa captura não entra na "
            "contagem dos quatro turnos.",
        ),
        (
            "body",
            "A sessão oficial teve quatro turnos com transcrição não vazia. Cada turno devolveu "
            "a fala seguinte da entrevistadora com áudio. Nenhuma chamada HTTP dessa sessão falhou. "
            "Uma abertura anterior, encerrada sem resposta falada, não entra neste registro. O "
            "áudio da pessoa foi apagado ao fim de cada turno e não está no repositório. O "
            "registro está em docs/sprint-3/registro-sessao-piloto.md, no repositório "
            "poc-en-simulator.",
        ),
        (
            "title",
            "2. Nota de privacidade",
        ),
        (
            "body",
            "A nota foi redigida em 20 de novembro de 2026, a partir da leitura do código. "
            "Nenhum arquivo de aplicação foi alterado. O critério da sprint confirma-se para o "
            "áudio da pessoa: em api/app.py, o corpo do turno segue ao reconhecimento e, na linha "
            "seguinte, audio_bytes = b\"\". api/sessions.py guarda apenas role e text.",
        ),
        (
            "body",
            "A transcrição não segue o mesmo intervalo. O texto entra em session.history e "
            "permanece na memória do processo até POST /api/sessions/{id}/end. Nessa rota a "
            "sessão sai do dicionário e history.clear() é chamado. A transcrição não é gravada "
            "em disco e não some ao fim de cada turno. Se o encerramento não for chamado, o "
            "histórico permanece no processo.",
        ),
        (
            "body",
            "No navegador, web/src/hooks/useInterview.js acumula as falas em messages e, depois "
            "do encerramento, guarda os três blocos em feedback. Esse estado dura enquanto a "
            "página estiver aberta. Não há localStorage, sessionStorage nem IndexedDB. O áudio "
            "do microfone não fica em estado depois do envio. O áudio reproduzido é o da "
            "entrevistadora, em blob URL.",
        ),
        (
            "body",
            "Acima de 1 MB, o parser de formulário do Starlette pode usar arquivo temporário de "
            "spool. await audio.close() ocorre antes do reconhecimento, e o fechamento destrói "
            "esse temporário. Não é um arquivo de áudio gravado pela aplicação. O limite do turno "
            "continua 8 MB, em MAX_AUDIO_BYTES.",
        ),
        (
            "body",
            "A página de preços do provedor foi reaberta nesta data. Na camada gratuita, o "
            "conteúdo enviado pode ser usado para melhoria dos produtos (GOOGLE, 2026a). Nos "
            "três modelos usados, a coluna gratuita de “Used to improve our products” está como "
            "Yes. A aplicação não controla essa retenção. Por isso a sessão usa somente a voz de "
            "quem executa o teste. A nota não afirma conformidade certificada com a Lei Geral de "
            "Proteção de Dados (LGPD) nem que o provedor apague o conteúdo. A suíte local, sem "
            "chamada ao provedor, executou cinco testes em 0,188 s, com resultado OK. Dois deles "
            "cobrem a ausência de áudio no histórico e a remoção da sessão no encerramento. O "
            "arquivo está em docs/sprint-3/nota-de-privacidade.md.",
        ),
        (
            "title",
            "3. DAS versão 1",
        ),
        (
            "body",
            "O DAS na versão 1 foi redigido em 20 de novembro de 2026, a partir da versão 0.2, "
            "do código da prova de conceito, do registro da sessão-piloto e da nota de "
            "privacidade. O documento descreve a arquitetura como construída e validada nessa "
            "sessão. O arquivo parcial do repositório, docs/sprint-1/das-parcial.md, permanece "
            "na versão 0.2 e conserva o registro das sprints anteriores. A versão 1 é o "
            "documento de fechamento e está nos entregáveis do projeto, no arquivo "
            "das-v1-simulador-entrevista.",
        ),
        (
            "body",
            "A arquitetura registrada é a de voz em cascata: reconhecimento, diálogo e síntese, "
            "nesta ordem, em uma requisição síncrona. A interface em React e a API local em "
            "Python 3.12, no padrão Backend for Frontend (BFF), são os dois contêineres. O "
            "provedor externo é a API Gemini, na camada gratuita. O documento reúne os "
            "requisitos RF-01 a RF-08, confrontados com a sessão-piloto, as restrições RC-01 a "
            "RC-09, as premissas P-01 a P-04 e oito decisões arquiteturais, AD-01 a AD-08. "
            "Também distingue o descarte do áudio da pessoa, ao fim do turno, da permanência da "
            "transcrição em memória até o encerramento.",
        ),
        (
            "body",
            "Os diagramas da versão 1 cobrem a visão geral do turno, o contexto, os contêineres, "
            "os componentes da API e a sequência do turno e do encerramento. As Figuras 13 a 15, "
            "da Sprint 2, permanecem a evidência dos três diagramas incorporados à versão 0.2. "
            "A Figura 17 reproduz a visão geral adotada na versão 1. A Figura 18 reproduz os "
            "componentes da API, nível que a versão 0.2 não trazia.",
        ),
        (
            "body",
            "A publicação em nuvem e a arquitetura de um produto mínimo viável (Minimum Viable "
            "Product — MVP) constam do mesmo documento, rotuladas como proposta não implantada e "
            "como evolução fora do escopo da versão 1. A latência de cada etapa do turno não foi "
            "medida. Essa lacuna está declarada no documento.",
        ),
        (
            "title",
            "4. Publicação em nuvem, condicionada ao tempo",
        ),
        (
            "body",
            "Não realizada. A prova de conceito permanece em execução local, em "
            "http://127.0.0.1:5173, com a API em http://127.0.0.1:8765. O DAS versão 1 descreve "
            "uma implantação proposta na Amazon Web Services (AWS), com CloudFront, S3, API "
            "Gateway, Lambda e Parameter Store, e lista os ajustes de código que ela exigiria: "
            "API sem estado, limite de áudio de até 4 MB e tempos-limite por etapa com soma "
            "inferior a 30 s. A Figura 19 reproduz essa proposta. Nenhum desses serviços foi "
            "implantado. A publicação não é condição para concluir o objetivo.",
        ),
    ],
)

fill_section(
    "Evidência dos resultados:",
    [
        (
            "title",
            "1. Sessão-piloto",
        ),
        (
            "body",
            "A abertura, devolvida com áudio, foi: “Hi, thanks for joining me today. Could you "
            "briefly introduce yourself and tell me a bit about your experience with software "
            "development?” Os quatro turnos abaixo reproduzem a transcrição e a fala seguinte "
            "como a interface as mostrou. A abertura não entra na contagem.",
        ),
        (
            "body",
            "Turno 1. Transcrição: “I am a software engineer and I have about five years of "
            "experience. At the moment I worked with closure.” Fala seguinte: “That sounds "
            "interesting. Could you tell me about a recent project you worked on using Clojure?”",
        ),
        (
            "body",
            "Turno 2. Transcrição: “Of course, I explain my experience saying about my of my "
            "current company. Well, my current company is a financial company.” Fala seguinte: "
            "“Thanks for sharing that. What did your role involve on that project at the "
            "financial company?”",
        ),
        (
            "body",
            "Turno 3. Transcrição: “Of course, my current job is about the director on app of "
            "this company.” Fala seguinte: “Could you tell me about a specific technical "
            "difficulty or challenge you ran into while working on that app?”",
        ),
        (
            "body",
            "Turno 4. Transcrição: “Of course, my principal problem that I worked direct in my "
            "company is involve involve latency and other metrics about the.” Fala seguinte: "
            "“How did you go about investigating and resolving that latency issue?”",
        ),
        (
            "body",
            "A Figura 16 é a captura da tela ao encerrar. Nela aparecem o cenário, o estado "
            "“Session ended”, a última pergunta da entrevistadora, o último trecho reconhecido "
            "e os blocos de retorno visíveis nessa captura.",
        ),
        ("caption", "Figura 16 — Tela ao encerrar a sessão-piloto, em 20 de novembro de 2026"),
        ("picture", (ASSETS / "sessao-piloto-app.png", 16.0)),
        (
            "body",
            "O retorno em três blocos é o texto que a tela mostrou depois de “End interview”, "
            "conservado como foi devolvido.",
        ),
        ("title", "Pontos positivos:"),
        (
            "body",
            "Você demonstrou cordialidade e disposição para responder às perguntas ao usar "
            "frases como “Of course, I explain my experience...” e “Of course, my current job "
            "is about...”. Você manteve o foco no contexto profissional ao mencionar o seu "
            "tempo de experiência (“I am a software engineer and I have about five years of "
            "experience”) e o setor da empresa (“a financial company”).",
        ),
        ("title", "Pontos de melhoria:"),
        (
            "body",
            "Houve repetições e hesitações na estrutura das frases que dificultam a clareza, "
            "como em “my principal problem that I worked direct in my company is involve involve "
            "latency and other metrics about the”. A formulação das respostas em alguns momentos "
            "soou truncada ou incompleta, por exemplo, “about the director on app of this "
            "company”, o que prejudica a fluidez esperada em uma entrevista de emprego.",
        ),
        ("title", "Próximo passo:"),
        (
            "body",
            "Pratique responder a uma pergunta de entrevista por vez, escrevendo primeiro um "
            "rascunho de frase curta e direta (por exemplo, focando em um problema técnico e sua "
            "solução) e, em seguida, treinando a fala em voz alta sem repetir palavras.",
        ),
        (
            "body",
            "Este resultado não afirma ganho de fluência, não trata a transcrição como prova "
            "geral de reconhecimento de sotaque brasileiro e não inclui amostra externa. O "
            "critério mensurável do objetivo — cinco a dez minutos, quatro turnos de fala "
            "reconhecidos, resposta oral e retorno em três blocos — foi atingido nesta sessão.",
        ),
        ("title", "2. Nota de privacidade"),
        (
            "body",
            "O resultado é a distinção registrada na nota. O áudio da pessoa é descartado ao fim "
            "do turno. A transcrição permanece só em memória até o encerramento. O navegador "
            "mostra o texto enquanto a página está aberta e não o grava. O provedor, na camada "
            "gratuita, pode usar o conteúdo enviado para melhoria dos próprios produtos. Nenhum "
            "código foi alterado para produzir essa nota.",
        ),
        ("title", "3. DAS versão 1"),
        (
            "body",
            "O resultado é um único documento de fechamento, na versão 1, datado de 20 de "
            "novembro de 2026. Ele reúne a arquitetura como construída, as decisões, as "
            "premissas, as restrições, a distinção de privacidade e o resultado da sessão-piloto. "
            "Os requisitos RF-01 a RF-08 constam como atendidos nessa sessão, inclusive RF-03, "
            "que nas verificações de 10 e de 15 de novembro de 2026 havia ficado sem transcrição. "
            "A Figura 17 mostra o turno em cascata. A Figura 18 mostra os componentes reais da API.",
        ),
        ("caption", "Figura 17 — Visão geral do turno de voz em cascata, DAS versão 1"),
        ("picture", (DIAG / "00-visao-geral.png", 16.0)),
        ("caption", "Figura 18 — Componentes da API local, DAS versão 1"),
        ("picture", (DIAG / "03-c3-componentes.png", 16.0)),
        ("title", "4. Publicação em nuvem"),
        (
            "body",
            "Sem implantação. A saída registrada é a permanência local da prova de conceito. A "
            "Figura 19 reproduz a topologia proposta no DAS e não é evidência de serviço no ar.",
        ),
        (
            "caption",
            "Figura 19 — Implantação proposta na AWS, não implantada, DAS versão 1",
        ),
        ("picture", (DIAG / "05-implantacao-aws.png", 16.0)),
    ],
)

fill_section(
    "2.3.2 Lições Aprendidas",
    [
        (
            "body",
            "1. Reconhecimento. O extrator não era a causa das transcrições vazias de 10 e de "
            "15 de novembro de 2026. No diagnóstico de 20 de novembro de 2026, o provedor "
            "devolveu texto no campo que o código já lia. Na sessão oficial, os quatro turnos "
            "trouxeram transcrição não vazia, dentro de oito minutos e 22 segundos. O requisito "
            "RF-03 passa a ter evidência positiva nesta sessão. As hesitações permaneceram no "
            "texto (“involve involve”, “about the director on app”), o que é compatível com o "
            "modo literal escolhido na Sprint 1. Isso não autoriza afirmar acurácia para sotaque "
            "brasileiro fora desta sessão.",
        ),
        (
            "body",
            "2. Diálogo. A entrevistadora manteve o papel e fez a pergunta seguinte a partir do "
            "texto reconhecido, inclusive quando a frase veio truncada. No turno 1, a transcrição "
            "traz “closure” e a fala seguinte pergunta sobre “Clojure”. O registro conserva as "
            "duas formas.",
        ),
        (
            "body",
            "3. Retorno em três blocos. Desta vez os blocos citam trechos da transcrição da "
            "própria sessão. Em 15 de novembro de 2026, com transcrição vazia, o bloco de pontos "
            "positivos tinha atribuído participação sem citar uma frase dita. A diferença fica "
            "registrada como comportamento observado do modelo, não como validação pedagógica do "
            "retorno.",
        ),
        (
            "body",
            "4. Privacidade. A frase “áudio e transcrição não permanecem armazenados após o "
            "turno” vale, na leitura do código, para o áudio da pessoa. A transcrição fica na "
            "memória do processo até o encerramento, porque o turno seguinte e os três blocos "
            "dependem dela. Acima de 1 MB, o spool temporário do parser não foi tratado como "
            "gravação da aplicação: ele é fechado antes do reconhecimento. A coluna gratuita "
            "“Used to improve our products” igual a Yes, reaberta em 20 de novembro de 2026, "
            "mantém a restrição de usar apenas a voz de quem executa o teste. A nota não "
            "certifica conformidade com a LGPD.",
        ),
        (
            "body",
            "5. DAS versão 1. O fechamento descreveu a arquitetura como construída na "
            "sessão-piloto: cascata de reconhecimento, diálogo e síntese, dois contêineres "
            "locais e provedor único na camada gratuita. A proposta anterior de chat de texto, "
            "com banco, fila e cadastro, ficou na visão de evolução, fora da versão 1. A "
            "latência de cada etapa do turno não foi medida e permanece como lacuna declarada.",
        ),
        (
            "body",
            "6. Publicação em nuvem. Não foi executada. O objetivo não depende dela. A "
            "topologia proposta ficou no DAS, com o rótulo de não implantada. Ela exigiria "
            "ajustes que a versão local não tem: API sem estado, limite de áudio menor e "
            "tempos-limite por etapa.",
        ),
    ],
)

append_heading(doc, "3. Considerações Finais", 1, BLUE)
append_body(
    doc,
    "O texto abaixo incorpora a sessão-piloto, a nota de privacidade e o DAS na versão 1, "
    "todos de 20 de novembro de 2026. A publicação em nuvem não foi realizada.",
)
append_heading(doc, "3.1 Resultados", 3, GREEN)
append_body(
    doc,
    "O resultado do Projeto Aplicado, até 21 de novembro de 2026, é a especificação "
    "fundamentada do desafio e da solução, a prova de conceito local e o DAS na versão 1. "
    "A tela abre com o cenário único, a API local devolve texto e áudio da entrevistadora, "
    "e o encerramento gera os três blocos. Os testes de 10 e de 15 de novembro de 2026 "
    "devolveram transcrição vazia. Em 20 de novembro de 2026, a sessão-piloto percorreu o "
    "fluxo em oito minutos e 22 segundos, com quatro turnos de transcrição não vazia, "
    "resposta oral e retorno em três blocos. A nota de privacidade do mesmo dia confirma "
    "que o áudio da pessoa é descartado ao fim do turno e que a transcrição permanece "
    "apenas em memória até o encerramento. Na camada gratuita, o provedor pode usar o "
    "conteúdo enviado para melhoria dos próprios produtos.",
)
append_body(
    doc,
    "O DAS na versão 1 registra a arquitetura como construída: reconhecimento, diálogo e "
    "síntese em cascata, interface em React, API local em Python 3.12 e provedor único na "
    "camada gratuita. O documento também registra a implantação proposta na AWS e a deixa "
    "identificada como não implantada. A prova de conceito permanece local. O projeto não "
    "afirma ganho de fluência, reconhecimento de sotaque brasileiro fora dessa sessão, nem "
    "conformidade certificada com a LGPD.",
)
append_title(doc, "Pontos positivos do processo:")
append_body(
    doc,
    "Rastreabilidade do problema à persona, à hipótese, ao backlog e às métricas; recusa "
    "de percentuais sem fonte; descarte de artigo retratado; registro explícito do que a "
    "sessão-piloto mostrou e do que ela não autoriza generalizar.",
)
append_title(doc, "Dificuldades:")
append_body(
    doc,
    "Ausência de pesquisa primária; evidência de chatbots oriunda de outros países; prazo "
    "do elemento temporal do objetivo ainda sujeito a confirmação com o orientador; "
    "convenção da matriz GUT, soma versus produto, a confirmar com o orientador. A "
    "latência de cada etapa do turno não foi medida.",
)
append_heading(doc, "3.2 Contribuições", 3, GREEN)
append_body(
    doc,
    "A contribuição é um recorte de arquitetura de solução com inteligência artificial "
    "conversacional aplicado a um problema educacional e profissional documentado: prática "
    "oral de inglês em entrevista de emprego, com restrições explícitas de reconhecimento "
    "de fala, latência, privacidade e qualidade do retorno. O DAS versão 1 separa o que "
    "foi construído e exercitado na sessão-piloto da proposta de publicação e da evolução "
    "de produto. O trabalho posiciona o protótipo como instrumento de teste, não como "
    "produto acabado.",
)
append_heading(doc, "3.3 Próximos passos", 3, GREEN)
append_body(
    doc,
    "1. Confirmar com o orientador o prazo, a fórmula da matriz GUT e se o teste com "
    "usuários será executado nesta edição do curso.",
)
append_body(
    doc,
    "2. A publicação em nuvem não foi executada. A prova de conceito permanece local, e "
    "a topologia proposta está no DAS versão 1, identificada como não implantada. Ela "
    "não é condição para concluir o objetivo. O prazo da sprint segue até 22 de novembro "
    "de 2026.",
)
append_body(
    doc,
    "3. Se a hipótese principal for suportada, avaliar um segundo cenário, de reunião, "
    "e a adaptação de nível.",
)
append_body(
    doc,
    "4. Se a hipótese principal for refutada, redesenhar a interação ou a tecnologia "
    "antes de qualquer expansão.",
)
append_body(
    doc,
    "5. Pesquisa primária futura: situar qual cenário o público prioriza e se o sotaque "
    "brasileiro é reconhecido de forma aceitável fora da sessão já registrada.",
)

doc.save(str(DOC))
print(DOC)
