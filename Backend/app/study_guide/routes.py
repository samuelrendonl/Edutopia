"""Endpoints protegidos para consultar y descargar guías de estudio."""

from __future__ import annotations

import io

from flask import Blueprint, g, jsonify, request, send_file

from ..auth_sessions import auth_parent
from ..db import query
from .service import build_guide, cached_pdf_for_guide, guide_catalog, normalize_subject


study_guides = Blueprint("study_guides", __name__, url_prefix="/api/study-guides")


def _child_for_parent(child_id):
    rows = query(
        "SELECT id, name, grade FROM children WHERE id = %s AND parent_id = %s",
        (child_id, g.parent["id"]),
        True,
    )
    return rows[0] if rows else None


def _child_for_requested_guide(grade):
    """Valida que la guía solicitada corresponda al perfil seleccionado."""
    raw_child_id = request.args.get("child_id")
    if raw_child_id is None:
        return None, None
    try:
        child_id = int(raw_child_id)
    except (TypeError, ValueError):
        return None, (jsonify({"error": "El perfil infantil no es válido."}), 400)
    child = _child_for_parent(child_id)
    if not child:
        return None, (jsonify({"error": "No encontramos ese perfil infantil."}), 404)
    if int(child["grade"]) != int(grade):
        return None, (
            jsonify({
                "error": (
                    f"Esta guía es de {grade}.º, pero el perfil de {child['name']} "
                    f"está en {child['grade']}.º."
                ),
                "child_grade": int(child["grade"]),
                "requested_grade": int(grade),
            }),
            403,
        )
    return child, None


def _params():
    subject = normalize_subject(request.args.get("subject"))
    grade = request.args.get("grade", type=int)
    if subject is None or grade not in range(1, 6):
        return None, (jsonify({"error": "Indica una materia válida y un grado entre 1 y 5."}), 400)
    return (subject, grade), None


@study_guides.get("/catalog")
@auth_parent
def catalog():
    return jsonify({"guides": guide_catalog(), "total": 25})


@study_guides.get("/preview")
@auth_parent
def preview():
    params, error = _params()
    if error:
        return error
    subject, grade = params
    child, child_error = _child_for_requested_guide(grade)
    if child_error:
        return child_error
    # El perfil solo autoriza el grado; el archivo servido es una guía base
    # compartida por todos los estudiantes de esa materia y grado.
    guide = build_guide(subject, grade)
    return jsonify({
        "subject": guide.subject,
        "grade": guide.grade,
        "student_name": "Guía base",
        "version": guide.version,
        "units": [
            {"number": unit.number, "title": unit.title, "description": unit.description}
            for unit in guide.units
        ],
        "objectives": guide.objectives,
        "projects": guide.projects,
        "weeks": len(guide.calendar),
        "solutions": len(guide.solutions),
    })


@study_guides.get("/pdf")
@auth_parent
def pdf():
    params, error = _params()
    if error:
        return error
    subject, grade = params
    child, child_error = _child_for_requested_guide(grade)
    if child_error:
        return child_error
    guide = build_guide(subject, grade)
    pdf_bytes, cache_hit = cached_pdf_for_guide(guide)
    filename = f"Guia_Estudio_{guide.subject_slug}_{grade}.pdf"
    response = send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        as_attachment=True,
        download_name=filename,
        max_age=15 * 24 * 60 * 60,
    )
    response.headers["Cache-Control"] = "private, max-age=1296000"
    response.headers["X-Study-Guide-Cache"] = "hit" if cache_hit else "generated"
    return response
