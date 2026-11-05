"""Renderiza el modelo de guía a PDF usando HTML + CSS y WeasyPrint."""

from __future__ import annotations

import base64
import contextlib
import io
import os
import re
from pathlib import Path

import qrcode
from jinja2 import Environment, FileSystemLoader, select_autoescape

HTML = None


TEMPLATE_DIR = Path(__file__).with_name("templates")
STYLE_PATH = Path(__file__).with_name("static") / "study_guide.css"

SVG_ICONS = {
    "rainbow": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 18a9 9 0 0 1 18 0M6 18a6 6 0 0 1 12 0M9 18a3 3 0 0 1 6 0" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "rocket": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4c3-2 5-1 5-1s1 2-1 5l-5 5-4-4 5-5Z" fill="currentColor"/><path d="m9 9-4 1 5 5 1-4M14 14l-1 5-5-5 4-1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="15.5" cy="6.5" r="1" fill="white"/></svg>',
    "map": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m3 5 6-2 6 2 6-2v16l-6 2-6-2-6 2V5Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 3v16M15 5v16" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    "bulb": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 14.5a6 6 0 1 1 8 0c-.7.7-1 1.4-1 2H9c0-.7-.3-1.2-1-1.5Z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9 19h6M10 22h4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "target": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="1.8" fill="currentColor"/></svg>',
    "star": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-2.9-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z" fill="currentColor"/></svg>',
    "book": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5v-16Z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 5.5v16M8 7h8M8 11h8" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    "phone": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="3" width="12" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 6h4M11 18h2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "brain": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5a3 3 0 0 0-5 2 3 3 0 0 0 1 5 3 3 0 0 0 3 5 3 3 0 0 0 4 2V6a3 3 0 0 0-3-1ZM15 5a3 3 0 0 1 5 2 3 3 0 0 1-1 5 3 3 0 0 1-3 5 3 3 0 0 1-4 2V6a3 3 0 0 1 3-1Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "sparkle": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 1.8 7.2L21 11l-7.2 1.8L12 20l-1.8-7.2L3 11l7.2-1.8L12 2Z" fill="currentColor"/><path d="m19 17 .7 2.3L22 20l-2.3.7L19 23l-.7-2.3L16 20l2.3-.7L19 17Z" fill="currentColor"/></svg>',
    "check": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "palette": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a9 9 0 1 0 0 18h1.5a2 2 0 0 0 0-4H12a2 2 0 0 1 0-4h3.5A5.5 5.5 0 0 0 21 7.5 9 9 0 0 0 12 3Z" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="7" cy="10" r="1" fill="currentColor"/><circle cx="10" cy="7" r="1" fill="currentColor"/><circle cx="15" cy="7" r="1" fill="currentColor"/></svg>',
    "trophy": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 4h8v5a4 4 0 0 1-8 0V4ZM12 13v5M8 21h8M5 5H3v2a4 4 0 0 0 4 4M19 5h2v2a4 4 0 0 1-4 4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "calendar": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7 3v4M17 3v4M3 9h18M7 13h3M14 13h3M7 17h3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "puzzle": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 3h3a2 2 0 1 1 4 0h3v5a2 2 0 1 0 0 4v3h-5a2 2 0 1 1-4 0H5v-4a2 2 0 1 0 0-4V3h4Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    "family": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="6" r="3" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="5.5" cy="9" r="2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="18.5" cy="9" r="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 20v-3a7 7 0 0 1 14 0v3M2 19v-2a3.5 3.5 0 0 1 3-3.45M22 19v-2a3.5 3.5 0 0 0-3-3.45" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "clock": '<svg class="svg-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
}


def _qr_data_uri(url):
    image = qrcode.make(url)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def _template_context(guide):
    logo_path = STYLE_PATH.parent / "Edutopia.svg"
    logo_data = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    context = {
        "guide": guide,
        "css": STYLE_PATH.read_text(encoding="utf-8"),
        "logo_data_uri": f"data:image/svg+xml;base64,{logo_data}",
        "icons": SVG_ICONS,
    }
    for unit in guide.units:
        for activity in unit.activities:
            activity.qr_data_uri = _qr_data_uri(activity.qr_url)
    return context


def render_pdf(guide):
    """Devuelve los bytes del PDF terminado."""
    chromium_pdf = _render_chromium(guide)
    if chromium_pdf is not None:
        return chromium_pdf
    html_renderer = _load_weasyprint()
    if html_renderer is None:
        return _render_fpdf(guide)
    environment = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    html = environment.get_template("guide.html").render(**_template_context(guide))
    return html_renderer(string=html, base_url=str(TEMPLATE_DIR)).write_pdf()


def _render_chromium(guide):
    """Renderiza HTML con Chrome/Edge para conservar el diseño visual completo."""
    try:
        from playwright.sync_api import Error as PlaywrightError, sync_playwright
    except ImportError:  # pragma: no cover - depende de la instalación local
        return None

    environment = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    html = environment.get_template("guide.html").render(**_template_context(guide))
    base_href = TEMPLATE_DIR.as_uri().rstrip("/") + "/"
    html = re.sub(r"<head>", f'<head><base href="{base_href}">', html, count=1)
    requested_channel = os.getenv("PLAYWRIGHT_BROWSER_CHANNEL", "chrome")
    channels = [requested_channel] + [channel for channel in ("chrome", "msedge") if channel != requested_channel]

    try:
        with sync_playwright() as playwright:
            browser = None
            for channel in channels:
                try:
                    browser = playwright.chromium.launch(channel=channel, headless=True)
                    break
                except PlaywrightError:
                    continue
            if browser is None:
                return None
            page = browser.new_page()
            page.set_content(html, wait_until="load")
            page.emulate_media(media="print")
            pdf = page.pdf(
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
            )
            browser.close()
            return pdf
    except (OSError, PlaywrightError):
        return None


def _load_weasyprint():
    """Carga WeasyPrint solo al generar, sin romper el arranque si falta GTK."""
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            from weasyprint import HTML as renderer
        return renderer
    except (ImportError, OSError):  # pragma: no cover - depende de GTK del sistema
        return None


def _font_path():
    candidates = [
        os.path.join(os.environ.get("WINDIR", r"C:\\Windows"), "Fonts", "arial.ttf"),
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    return next((path for path in candidates if Path(path).exists()), None)


def _render_fpdf(guide):
    """Renderizador infantil de respaldo sin GTK para entornos Windows."""
    from fpdf import FPDF

    class GuidePDF(FPDF):
        def footer(self):
            self.set_y(-12)
            self.set_font(font, size=8)
            self.set_text_color(100, 116, 139)
            self.cell(0, 8, str(self.page_no()), align="R")

    pdf = GuidePDF()
    font_path = _font_path()
    if font_path:
        pdf.add_font("Guide", "", font_path)
        pdf.add_font("Guide", "B", font_path)
        font = "Guide"
    else:
        font = "Helvetica"
    pdf.set_auto_page_break(True, margin=16)
    color = _hex_rgb(guide.color)
    light = _mix(color, (255, 255, 255), 0.9)
    dark = _mix(color, (36, 50, 74), 0.35)

    def brand(x=12, y=10, scale=1):
        """Marca vectorial legible incluso cuando el motor no puede leer SVG."""
        pdf.set_fill_color(22, 140, 255)
        pdf.ellipse(x, y, 16 * scale, 16 * scale, style="F")
        pdf.set_fill_color(255, 195, 0)
        pdf.rect(x + 3 * scale, y + 7 * scale, 10 * scale, 2 * scale, style="F")
        pdf.set_fill_color(141, 37, 223)
        pdf.rect(x + 6 * scale, y + 3 * scale, 4 * scale, 5 * scale, style="F")
        pdf.set_text_color(0, 66, 169)
        pdf.set_font(font, "B", int(12 * scale))
        pdf.text(x + 20 * scale, y + 11 * scale, "EDUTOPIA")

    def mascot(x, y, scale=1, shirt=(91, 92, 226), skin=(244, 177, 131), hair=(91, 58, 41)):
        """Dibuja un personaje sencillo con formas vectoriales y colores vivos."""
        head = 18 * scale
        pdf.set_fill_color(*shirt)
        pdf.ellipse(x - 19 * scale, y + 25 * scale, 38 * scale, 43 * scale, style="F")
        pdf.set_fill_color(*skin)
        pdf.ellipse(x - head / 2, y, head, head, style="F")
        pdf.set_fill_color(*hair)
        pdf.ellipse(x - head / 2, y - 3 * scale, head, 8 * scale, style="F")
        pdf.set_fill_color(36, 50, 74)
        pdf.ellipse(x - 4 * scale, y + 8 * scale, 2 * scale, 2 * scale, style="F")
        pdf.ellipse(x + 2 * scale, y + 8 * scale, 2 * scale, 2 * scale, style="F")
        pdf.set_draw_color(36, 50, 74)
        pdf.set_line_width(0.7)
        pdf.arc(x - 4 * scale, y + 8 * scale, 8 * scale, 7 * scale, 25, 155)
        pdf.set_fill_color(255, 195, 0)
        pdf.ellipse(x + 17 * scale, y + 10 * scale, 7 * scale, 7 * scale, style="F")

    def background():
        pdf.set_fill_color(248, 251, 255)
        pdf.rect(0, 0, 210, 297, style="F")
        for x, y, size, fill in ((188, 34, 12, (255, 229, 44)), (12, 260, 16, (213, 106, 255)), (190, 270, 9, (53, 201, 0))):
            pdf.set_fill_color(*fill)
            pdf.ellipse(x, y, size, size, style="F")

    def new_page(label):
        pdf.add_page()
        background()
        pdf.set_fill_color(*color)
        pdf.rect(0, 0, 210, 25, style="F")
        pdf.set_text_color(255, 255, 255)
        pdf.set_font(font, "B", 9)
        pdf.text(12, 10, "EDUTOPIA")
        pdf.set_font(font, "B", 10)
        pdf.text(12, 19, label)
        pdf.set_y(34)

    def heading(text, size=18, accent=True):
        pdf.set_text_color(*(color if accent else dark))
        pdf.set_font(font, "B", size)
        pdf.multi_cell(0, 9, text)
        pdf.ln(2)

    def body(text, size=10, fill=None, width=0):
        pdf.set_text_color(36, 50, 74)
        pdf.set_font(font, size=size)
        if fill:
            pdf.set_fill_color(*fill)
        if not width:
            pdf.set_x(12)
        pdf.multi_cell(width or 0, 6, str(text), fill=bool(fill))
        pdf.ln(1)

    def question_box(question):
        fill = (236, 253, 245) if question.example else (255, 255, 255)
        pdf.set_fill_color(*fill)
        pdf.set_draw_color(*_mix(color, (255, 255, 255), 0.55))
        pdf.rect(12, pdf.get_y(), 186, 8, style="DF")
        prefix = "EJEMPLO RESUELTO" if question.example else question.number
        pdf.set_text_color(*dark)
        pdf.set_font(font, "B", 9)
        pdf.set_x(12)
        pdf.multi_cell(0, 5, f"{prefix}: {question.prompt}")
        if question.example:
            body(f"Respuesta modelo: {question.answer_text}", 9, fill=(236, 253, 245))
        else:
            for index, option in enumerate(question.options):
                body(f"   {chr(97 + index)}) {option}", 8, fill=(248, 250, 252))

    # Portada infantil colorida con marca y personajes.
    pdf.add_page()
    pdf.set_fill_color(255, 249, 232)
    pdf.rect(0, 0, 210, 297, style="F")
    pdf.set_fill_color(*color)
    pdf.rect(0, 0, 210, 12, style="F")
    pdf.set_fill_color(238, 245, 255)
    pdf.ellipse(-35, 180, 105, 105, style="F")
    pdf.set_fill_color(245, 237, 255)
    pdf.ellipse(145, 50, 95, 95, style="F")
    brand(61, 22, 1.35)
    pdf.set_text_color(*color)
    pdf.set_font(font, "B", 11)
    pdf.text(77, 62, "GUÍA DE ESTUDIO")
    pdf.set_font(font, "B", 29)
    pdf.multi_cell(0, 13, guide.subject, align="C")
    pdf.set_font(font, "B", 21)
    pdf.set_text_color(*dark)
    pdf.cell(0, 12, f"{guide.grade}.º grado", align="C")
    pdf.ln(20)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_draw_color(*color)
    pdf.rect(47, 107, 116, 15, style="DF")
    pdf.set_text_color(*dark)
    pdf.set_font(font, "B", 13)
    pdf.cell(0, 15, guide.student_name, align="C")
    mascot(72, 158, 1.35, (91, 92, 226))
    mascot(139, 158, 1.35, (33, 168, 137), skin=(141, 85, 36), hair=(46, 26, 16))
    pdf.set_fill_color(*color)
    pdf.rect(39, 238, 132, 15, style="F")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font(font, "B", 10)
    pdf.cell(0, 15, "APRENDER · PRACTICAR · CREAR", align="C")

    new_page("MI RUTA DE APRENDIZAJE")
    heading("¡Hola, explorador!", 22)
    body("Lee la explicación, resuelve la práctica y revisa el solucionario al final.")
    heading("Objetivos", 14)
    for objective in guide.objectives:
        body(f"* {objective}", 9, fill=light)
    heading("Tus misiones", 14)
    for unit in guide.units:
        activity = unit.activities[0]
        body(f"Misión {unit.number}: {activity.title} · {activity.learning_phase}", 9, fill=(255, 248, 217))

    for unit in guide.units:
        for activity in unit.activities:
            new_page(f"UNIDAD {unit.number} · {activity.learning_phase}")
            heading(activity.title, 22)
            body(activity.description, 10, fill=light)
            if activity.objective:
                body(f"META: {activity.objective}", 9, fill=(255, 248, 217))
            body(f"RUTA EDUTOPIA: {activity.kind} · {activity.learning_phase} · {activity.minutes} min · {activity.points} puntos", 9, fill=(240, 237, 255))
            if activity.prerequisites:
                body("ANTES DE EMPEZAR: " + ", ".join(activity.prerequisites), 8, fill=(240, 237, 255))
            heading("Aprendemos", 14)
            for line in activity.lesson:
                body(f"* {line}", 9)
            qr_buffer = io.BytesIO()
            qrcode.make(activity.qr_url).save(qr_buffer, format="PNG")
            qr_buffer.seek(0)
            pdf.set_fill_color(239, 250, 255)
            pdf.rect(12, pdf.get_y(), 186, 32, style="F")
            qr_y = pdf.get_y()
            pdf.image(qr_buffer, x=15, y=qr_y + 3, w=24)
            pdf.set_xy(45, qr_y + 12)
            body("ESCANEA Y JUEGA EN EDUTOPIA", 9)
            pdf.set_x(12)
            pdf.ln(4)
            if activity.questions:
                heading("Practico", 14)
                for question in activity.questions:
                    question_box(question)
            if activity.project:
                heading("Proyecto para casa", 14)
                body(f"CREA: {activity.project}", 9, fill=(255, 248, 217))

    new_page("MI PROYECTO Y MI PROGRESO")
    mascot(175, 38, 0.65, (242, 140, 40))
    heading("Proyecto y autoevaluación")
    for item in guide.self_assessment:
        body(f"[ ] {item}\n    ( ) Satisfecho   ( ) En proceso   ( ) Necesito practicar", 9, fill=light)
    heading("Rúbrica familiar", 14)
    for row in guide.rubric:
        body(f"{row['criterion']}: {row['description']}", 9, fill=(255, 248, 217))
    heading("Calendario de 36 semanas")
    for week in guide.calendar:
        body(f"SEMANA {week['week']} · {week['title']} · {week['phase']}", 8, fill=(248, 250, 252))

    new_page("RESPUESTAS PARA REVISAR")
    mascot(176, 39, 0.65, (33, 168, 137), skin=(141, 85, 36), hair=(46, 26, 16))
    heading("Solucionario")
    body("Revisa esta sección después de intentarlo y vuelve a practicar los temas que necesites.")
    for answer in guide.solutions:
        body(f"{answer.number}: {answer.answer_text}", 8, fill=(236, 253, 245))
    pdf.set_fill_color(*color)
    pdf.rect(45, 270, 120, 12, style="F")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font(font, "B", 9)
    pdf.cell(0, 12, "¡LO INTENTASTE Y ESO YA ES APRENDER!", align="C")
    return bytes(pdf.output())


def _hex_rgb(value):
    value = value.lstrip("#")
    try:
        return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))
    except (TypeError, ValueError):
        return (79, 97, 216)


def _mix(first, second, amount):
    """Mezcla dos colores RGB para crear fondos suaves de la guía."""
    return tuple(round(a * (1 - amount) + b * amount) for a, b in zip(first, second))
