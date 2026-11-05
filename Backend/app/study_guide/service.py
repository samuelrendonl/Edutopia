"""Compone guías a partir del catálogo curricular existente.

Este módulo no duplica las lecciones: ``learning_content`` sigue siendo la
fuente de verdad y aquí solo se transforma en el modelo que consumen las
plantillas PDF.
"""

from __future__ import annotations

import hashlib
import os
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from threading import Lock
from urllib.parse import quote

from ..learning_content import ACTIVITIES, activity_for_grade
from ..subject_units import SUBJECTS


CACHE_RENDER_VERSION = "html-child-render-v4"
CACHE_DIR = Path(__file__).resolve().parents[2] / "cache" / "study_guides"
_CACHE_LOCK = Lock()


def _slug(value):
    """Convierte el nombre visible de una materia en un slug estable."""
    value = unicodedata.normalize("NFKD", value.lower())
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value


GUIDE_SUBJECTS = {
    subject["name"]: {
        "slug": _slug(subject["name"]),
        "icon": subject["icon"],
        "color": subject["color"],
        "description": subject["description"],
    }
    for subject in SUBJECTS
}


LANGUAGE_GUIDE_PROJECTS = {
    1: [
        "Mi cuento ilustrado: crea una historia corta con personaje, lugar, inicio y final.",
        "Cazadores de palabras: arma un mural con palabras, sílabas y dibujos de tu entorno.",
        "Teatro de sonidos: representa un diálogo breve usando pausas, voz y signos de puntuación.",
        "Biblioteca familiar: lee un cuento en casa y cuenta qué ocurrió primero, después y al final.",
    ],
    2: [
        "Taller de párrafos: escribe un párrafo con primero, luego, después y finalmente.",
        "Fábula en voz alta: ilustra una fábula, explica su enseñanza y recítala con expresión.",
        "Diccionario ilustrado: reúne diez palabras, su significado y una oración para cada una.",
        "Reporteros de la escuela: entrevista a un familiar y organiza sus respuestas en un texto claro.",
    ],
    3: [
        "Detectives de pistas: lee un relato, encuentra tres pistas y justifica una inferencia.",
        "Narración con diálogo: escribe una historia de tres párrafos con personajes y diálogo breve.",
        "Mito en viñetas: transforma un mito o leyenda en seis viñetas con globos y cartelas.",
        "Familia léxica mural: construye familias de palabras y explica la raíz que comparten.",
    ],
    4: [
        "Revista expositiva: explica un tema con introducción, datos, ejemplos y síntesis.",
        "Teatro leído: adapta una escena y marca parlamentos, acotaciones, tono y pausas.",
        "Mapa de personajes: relaciona personaje, ambiente, conflicto y evidencia del relato.",
        "Conectores en acción: mejora un texto usando causa, contraste, consecuencia y orden.",
    ],
    5: [
        "Club de lectura crítica: compara dos fuentes, identifica un sesgo y sustenta tu interpretación.",
        "Mini ensayo: escribe una tesis, dos argumentos, evidencias y una conclusión.",
        "Campaña informativa: crea un mensaje para la comunidad diferenciando hechos y opiniones.",
        "Podcast literario: recomienda una obra, analiza su narrador y explica qué te hizo pensar.",
    ],
}


MATH_GUIDE_PROJECTS = {
    1: [
        "Ciudad de números: representa cantidades con tapas, bloques o dibujos y ordénalas de menor a mayor.",
        "Mercado de sumas: inventa cinco compras, calcula cuánto juntas y cuánto te queda.",
        "Museo de formas: busca figuras y cuerpos en casa, dibújalos y describe sus lados o caras.",
        "Patrones con movimiento: crea una secuencia de colores, sonidos o palmadas y reta a alguien a continuarla.",
    ],
    2: [
        "Tienda de operaciones: crea precios, suma compras y resuelve cambios con decenas y unidades.",
        "Medimos nuestra casa: mide tres objetos, compara sus longitudes y registra los resultados.",
        "Gráfica familiar: pregunta una preferencia, organiza los datos y construye un pictograma.",
        "Construcciones geométricas: arma figuras con palitos y explica sus lados, vértices y posiciones.",
    ],
    3: [
        "Diseña un parque: usa multiplicaciones, divisiones, medidas y un plano sencillo para organizarlo.",
        "Recetario de fracciones: representa medios, tercios y cuartos con alimentos o dibujos.",
        "Detectives de datos: recoge información del hogar y presenta una gráfica con una conclusión.",
        "Reto de estrategias: inventa un problema cotidiano, resuélvelo y explica por qué elegiste la operación.",
    ],
    4: [
        "Presupuesto de una excursión: calcula costos, descuentos, multiplicaciones y división del dinero.",
        "Plano a escala: diseña un espacio, calcula perímetros y áreas y explica las medidas utilizadas.",
        "Laboratorio de fracciones y decimales: representa equivalencias con tiras, cuadrículas y números.",
        "Encuesta matemática: recoge datos, calcula resultados y comunica dos conclusiones con argumentos.",
    ],
    5: [
        "Feria matemática: crea puestos con porcentajes, fracciones, decimales y problemas de cambio.",
        "Arquitectura sostenible: diseña un plano a escala, calcula área, perímetro y uso responsable de materiales.",
        "Estudio de datos: analiza una encuesta con promedio, tablas y gráficas y presenta tus conclusiones.",
        "Desafío de problemas: escribe un problema de varias etapas, resuélvelo y justifica cada estrategia.",
    ],
}


SOCIAL_GUIDE_PROJECTS = {
    1: [
        "Mi línea de vida: representa momentos importantes y explica cómo has cambiado.",
        "Mapa de mi comunidad: dibuja casa, escuela, barrio y un lugar donde las personas se ayudan.",
        "Necesidades y deseos: clasifica ejemplos y explica una decisión responsable para tu familia.",
        "Mapa del tesoro: crea una ruta con símbolos, referencias y normas para cuidar el barrio.",
    ],
    2: [
        "Ruta comunitaria: diseña un recorrido con lugares, servicios y señales de orientación.",
        "Historia local: entrevista a una persona mayor y organiza tres cambios de la comunidad.",
        "Bienes y servicios: registra ejemplos del barrio y explica por qué son importantes.",
        "Código de convivencia: crea cinco acuerdos para resolver conflictos con respeto.",
    ],
    3: [
        "Simulador de alcalde: identifica un problema, propone una solución y escucha las necesidades de la comunidad.",
        "Mapa de recursos: representa recursos naturales, actividades económicas y una acción de cuidado.",
        "Fuente histórica: compara una fotografía, un testimonio y un objeto para reconstruir un hecho.",
        "Presupuesto ciudadano: organiza ingresos, gastos y una decisión responsable para un proyecto escolar.",
    ],
    4: [
        "Constitución en acción: presenta un derecho, un deber y una situación de participación ciudadana.",
        "Atlas de Colombia: crea un mapa con relieve, clima, regiones y actividades humanas.",
        "Museo de historia nacional: organiza fuentes y explica cambios entre distintos periodos.",
        "Feria de comercio: representa productores, consumidores, bancos y decisiones de comercio responsable.",
    ],
    5: [
        "Modelo ONU escolar: representa un país, investiga una postura y propone un acuerdo sobre un reto global.",
        "Proyecto ODS local: relaciona un problema del entorno con un Objetivo de Desarrollo Sostenible.",
        "Mapa de globalización: explica una cadena de producción y sus efectos en distintas regiones.",
        "Emprendimiento responsable: diseña una idea que genere valor, respete derechos y cuide recursos.",
    ],
}


SCIENCE_GUIDE_PROJECTS = {
    1: [
        "Diario del tiempo: observa el cielo durante una semana, dibuja los cambios y compáralos.",
        "Mi cuerpo seguro: crea un afiche con hábitos de higiene, descanso y prevención.",
        "Museo de materiales: clasifica objetos por sus propiedades y explica para qué sirven.",
        "Día y noche: construye un modelo sencillo de la Tierra y el Sol y explica la sombra.",
    ],
    2: [
        "Siembra y observa: planta un frijol, registra cambios y dibuja su ciclo de vida.",
        "Agua que cambia: representa evaporación, condensación y congelación con una experiencia segura.",
        "Invento reutilizado: diseña una herramienta con materiales reutilizados y explica su utilidad.",
        "Guardianes del ambiente: crea un plan familiar para ahorrar agua y separar residuos.",
    ],
    3: [
        "Cadena alimentaria: representa una cadena de tu entorno y explica el papel de cada ser vivo.",
        "Máquinas y energía: construye una máquina simple y describe la fuerza que utiliza.",
        "Modelo del sistema solar: organiza los cuerpos celestes y explica un fenómeno de la Tierra.",
        "Circuito seguro: arma un circuito sencillo con acompañamiento adulto y registra tus observaciones.",
    ],
    4: [
        "Mapa de un ecosistema: relaciona seres vivos, factores no vivos y acciones de protección.",
        "Casa con energía limpia: diseña una solución con energía solar o eólica para una necesidad.",
        "Plan de prevención: identifica un riesgo natural y crea una ruta de emergencia para tu comunidad.",
        "Robot biomimético: observa una adaptación de un animal y diseña una máquina inspirada en ella.",
    ],
    5: [
        "Feria de ciencias: formula una pregunta, registra datos, analiza resultados y presenta una conclusión.",
        "Cambio climático local: investiga una evidencia del entorno y propone acciones de adaptación.",
        "Modelo de placas: explica un relieve o fenómeno geológico usando un modelo construido.",
        "Tecnología ética: diseña una solución con datos o IA y explica cómo protege a las personas.",
    ],
}


# La comprensión de la materia debe aceptar tanto nombres visibles como slugs
# para que la API sea cómoda sin exponer la estructura interna del catálogo.
SUBJECT_BY_SLUG = {
    _slug(name): name for name in GUIDE_SUBJECTS
}
SUBJECT_BY_SLUG.update({
    "biologia": "Ciencias Naturales",
    "naturales": "Ciencias Naturales",
})


@dataclass
class GuideQuestion:
    number: str
    prompt: str
    options: list[str]
    answer: int
    answer_text: str
    example: bool = False


@dataclass
class GuideActivity:
    key: str
    title: str
    kind: str
    description: str
    objective: str
    learning_phase: str
    prerequisites: list[str]
    related_activity: str
    minutes: int
    points: int
    lesson: list[str]
    questions: list[GuideQuestion]
    project: str = ""
    qr_url: str = ""


@dataclass
class GuideUnit:
    number: int
    title: str
    description: str
    activities: list[GuideActivity] = field(default_factory=list)


@dataclass
class StudyGuide:
    subject: str
    subject_slug: str
    grade: int
    student_name: str
    color: str
    icon: str
    description: str
    objectives: list[str]
    units: list[GuideUnit]
    projects: list[str]
    calendar: list[dict]
    self_assessment: list[str]
    rubric: list[dict]
    solutions: list[GuideQuestion]
    version: str
    child_id: int | None = None


def normalize_subject(value):
    """Devuelve el nombre canónico o ``None`` si la materia no existe."""
    if not value:
        return None
    value = str(value).strip()
    if value in GUIDE_SUBJECTS:
        return value
    return SUBJECT_BY_SLUG.get(_slug(value))


def _activity_order(activity):
    return (
        activity.get("learning_order", 999),
        0 if activity.get("kind") == "Aprendizaje" else 1,
        activity.get("title", ""),
    )


def _base_url():
    configured = os.getenv("PUBLIC_BASE_URL")
    if configured:
        return configured.rstrip("/")
    if os.getenv("RENDER_SERVICE_ID"):
        return "https://edutopia-frontend.onrender.com"
    return "http://localhost:5173"


def _qr_url(activity_key, grade, child_id=None):
    params = f"grade={grade}&activity={quote(activity_key)}"
    if child_id is not None:
        params = f"child={int(child_id)}&{params}"
    return f"{_base_url()}/aprende?{params}"


def _objectives(subject, grade, activities):
    objectives = [activity.objective for activity in activities if activity.objective]
    if objectives:
        return objectives[:6]
    return [
        f"Desarrollar las habilidades fundamentales de {subject.lower()} en {grade}.º grado.",
        "Explicar lo aprendido con ejemplos y practicar de forma autónoma.",
    ]


def _questions(activity, unit_number):
    questions = []
    for index, question in enumerate(activity.get("questions", []), start=1):
        options = [str(option) for option in question.get("options", [])]
        answer = question.get("answer", 0)
        answer = answer if isinstance(answer, int) and 0 <= answer < len(options) else 0
        questions.append(
            GuideQuestion(
                number=f"U{unit_number}-P{index}",
                prompt=str(question.get("prompt", "")),
                options=options,
                answer=answer,
                answer_text=options[answer] if options else "",
                example=index == 1,
            )
        )
    return questions


def _make_units(subject, grade, child_id=None):
    catalog = [item for item in ACTIVITIES if item["subject"] == subject]
    graded_catalog = [
        (index, base_activity, activity_for_grade(base_activity, grade))
        for index, base_activity in enumerate(catalog)
    ]
    # El orden debe usar la ruta adaptada al grado, igual que Aprende.
    graded_catalog.sort(
        key=lambda pair: (
            pair[2].get("learning_order", 999),
            pair[0],
        )
    )
    titles = {
        base_activity["key"]: activity.get("title", base_activity["key"])
        for _, base_activity, activity in graded_catalog
    }
    units = []
    projects = []
    for unit_number, (_, base_activity, activity) in enumerate(graded_catalog, start=1):
        guide_questions = _questions(activity, unit_number)
        item = GuideActivity(
            key=activity["key"],
            title=activity.get("title", base_activity["key"]),
            kind=activity.get("kind", "Aprendizaje"),
            description=activity.get("description", ""),
            objective=activity.get("objective", ""),
            learning_phase=activity.get("learning_phase", "Practicar"),
            prerequisites=[titles.get(str(item), str(item)) for item in activity.get("prerequisites", [])],
            related_activity=str(activity.get("related_activity", "") or ""),
            minutes=int(activity.get("minutes", 8) or 8),
            points=int(activity.get("points", 100) or 100),
            lesson=[str(line) for line in activity.get("lesson", [])],
            questions=guide_questions,
            project=str(activity.get("project", "") or ""),
            qr_url=_qr_url(activity["key"], grade, child_id),
        )
        if item.project and item.project not in projects:
            projects.append(item.project)
        units.append(
            GuideUnit(
                number=unit_number,
                title=item.title,
                description=item.description,
                activities=[item],
            )
        )
    return units, projects


def _calendar(units):
    """Distribuye las unidades en un calendario sencillo de 36 semanas."""
    activities = [unit.activities[0].title for unit in units if unit.activities]
    if not activities:
        activities = ["Repaso y práctica"]
    result = []
    for week in range(1, 37):
        position = min((week - 1) // 4, len(activities) - 1)
        phase = "Explorar" if week % 4 != 0 else "Demostrar lo aprendido"
        result.append({"week": week, "title": activities[position], "phase": phase})
    return result


def _rubric():
    return [
        {"criterion": "Comprensión", "description": "Explica la idea principal con sus propias palabras."},
        {"criterion": "Aplicación", "description": "Resuelve ejercicios y usa ejemplos de la vida cotidiana."},
        {"criterion": "Comunicación", "description": "Presenta su trabajo de forma clara y respetuosa."},
        {"criterion": "Autonomía", "description": "Revisa sus respuestas y pide ayuda cuando la necesita."},
    ]


def _self_assessment(subject):
    return [
        f"Puedo explicar una idea importante de {subject.lower()}.",
        "Puedo aplicar lo aprendido en una situación nueva.",
        "Puedo revisar mis respuestas y corregir mis errores.",
        "Puedo explicar qué necesito seguir practicando.",
    ]


def build_guide(subject, grade, student_name="", child_id=None):
    """Construye una guía completa para una de las 25 combinaciones."""
    canonical = normalize_subject(subject)
    if canonical is None:
        raise ValueError("Materia no válida.")
    try:
        grade = int(grade)
    except (TypeError, ValueError) as error:
        raise ValueError("El grado no es válido.") from error
    if grade not in range(1, 6):
        raise ValueError("El grado debe estar entre 1 y 5.")

    metadata = GUIDE_SUBJECTS[canonical]
    units, projects = _make_units(canonical, grade, child_id)
    if canonical == "Lengua Castellana":
        projects.extend(LANGUAGE_GUIDE_PROJECTS[grade])
    elif canonical == "Matemáticas":
        projects.extend(MATH_GUIDE_PROJECTS[grade])
    elif canonical == "Sociales":
        projects.extend(SOCIAL_GUIDE_PROJECTS[grade])
    elif canonical == "Ciencias Naturales":
        projects.extend(SCIENCE_GUIDE_PROJECTS[grade])
    solutions = [
        question
        for unit in units
        for activity in unit.activities
        for question in activity.questions
    ]
    fingerprint_parts = [canonical, str(grade), metadata["description"], student_name.strip(), str(child_id or "")]
    for unit in units:
        for activity in unit.activities:
            fingerprint_parts.extend([
                activity.key,
                activity.title,
                activity.description,
                activity.objective,
                activity.learning_phase,
                ",".join(activity.prerequisites),
                activity.related_activity,
                str(activity.minutes),
                str(activity.points),
                "\n".join(activity.lesson),
                activity.project,
                activity.qr_url,
            ])
            fingerprint_parts.extend(
                f"{item.number}:{item.prompt}:{item.answer_text}:{'|'.join(item.options)}"
                for item in activity.questions
            )
    fingerprint_parts.extend(projects)
    fingerprint_source = "|".join(fingerprint_parts)
    version = hashlib.sha256(fingerprint_source.encode("utf-8")).hexdigest()[:12]
    return StudyGuide(
        subject=canonical,
        subject_slug=metadata["slug"],
        grade=grade,
        student_name=student_name.strip() or "Estudiante",
        color=metadata["color"],
        icon=metadata["icon"],
        description=metadata["description"],
        objectives=_objectives(canonical, grade, [u.activities[0] for u in units]),
        units=units,
        projects=projects,
        calendar=_calendar(units),
        self_assessment=_self_assessment(canonical),
        rubric=_rubric(),
        solutions=solutions,
        version=version,
        child_id=child_id,
    )


def cached_pdf_for_guide(guide):
    """Devuelve el PDF guardado y lo genera solo si cambió su contenido."""
    from .pdf_generator import render_pdf

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    child_suffix = f"_child_{guide.child_id}" if guide.child_id is not None else ""
    cache_name = f"Guia_Estudio_{guide.subject_slug}_{guide.grade}{child_suffix}"
    path = CACHE_DIR / f"{cache_name}.pdf"
    marker = CACHE_DIR / f"{cache_name}.meta"
    expected = f"{CACHE_RENDER_VERSION}:{guide.version}"

    with _CACHE_LOCK:
        if path.exists() and marker.exists() and marker.read_text(encoding="utf-8").strip() == expected:
            return path.read_bytes(), True
        pdf_bytes = render_pdf(guide)
        temporary = path.with_suffix(".pdf.tmp")
        temporary.write_bytes(pdf_bytes)
        temporary.replace(path)
        marker.write_text(expected, encoding="utf-8")
        return pdf_bytes, False


def guide_catalog():
    """Catálogo liviano de las 25 guías disponibles."""
    return [
        {
            "subject": subject,
            "subject_slug": metadata["slug"],
            "grade": grade,
            "title": f"Guía de {subject} · {grade}.º grado",
            "color": metadata["color"],
        }
        for subject, metadata in GUIDE_SUBJECTS.items()
        for grade in range(1, 6)
    ]
