"""API de actividades y progreso por perfil infantil."""

from functools import lru_cache, wraps
from flask import Blueprint, g, jsonify, request

from .learning_content import ACTIVITIES, activity_for_grade, public_activity
from .auth_sessions import verify_parent_token, auth_parent
from .subject_units import SUBJECTS
from juegos.backend.catalog import evaluate_game

learning = Blueprint("learning", __name__, url_prefix="/api/learning")
@lru_cache(maxsize=5)
def _catalog_for_grade(grade):
    """Genera una única versión inmutable por grado durante la vida del proceso."""
    return tuple(public_activity(item, grade) for item in ACTIVITIES)


def _query(sql, params=(), fetch=False):
    cursor = g.db.cursor(dictionary=True)
    cursor.execute(sql, params)
    rows = cursor.fetchall() if fetch else cursor.lastrowid
    cursor.close()
    return rows


def _child_access(fn):
    @wraps(fn)
    def wrapped(child_id, *args, **kwargs):
        parent_id = verify_parent_token(request.headers.get("X-Auth-Token"))
        if not parent_id:
            return jsonify({"error": "Inicia sesión para continuar."}), 401
        child = _query(
            "SELECT id, name, grade FROM children WHERE id = %s AND parent_id = %s",
            (child_id, parent_id), True,
        )
        if not child:
            return jsonify({"error": "No encontramos ese perfil infantil."}), 404
        g.child = child[0]
        return fn(child_id, *args, **kwargs)
    return wrapped


@learning.get("/children/<int:child_id>/progress")
@_child_access
def progress(child_id):
    rows = _query(
        "SELECT activity_key, best_score, attempts, completed_at FROM child_activity_progress WHERE child_id = %s",
        (child_id,), True,
    )
    by_key = {row["activity_key"]: row for row in rows}
    known_keys = {item["key"] for item in ACTIVITIES}
    known_progress = [row for key, row in by_key.items() if key in known_keys]
    total_points = sum(row["best_score"] for row in known_progress)
    completed = len(known_progress)
    by_subject = []
    for subject in SUBJECTS:
        subject_activities = [item for item in ACTIVITIES if item["subject"] == subject["name"]]
        subject_keys = {item["key"] for item in subject_activities}
        subject_progress = [by_key[key] for key in subject_keys if key in by_key]
        by_subject.append({
            "subject": subject["name"],
            "total": len(subject_activities),
            "completed": len(subject_progress),
            "points": sum(item["best_score"] for item in subject_progress),
        })
    return jsonify({
        "child": g.child,
        "completed": completed,
        "total": len(ACTIVITIES),
        "progress": round(completed * 100 / len(ACTIVITIES)),
        "points": total_points,
        "activities": by_key,
        "subjects": by_subject,
    })


@learning.post("/children/<int:child_id>/submit")
@_child_access
def submit(child_id):
    data = request.get_json(silent=True) or {}
    activity_key = data.get("activity_key")
    answers = data.get("answers")
    activity = next((item for item in ACTIVITIES if item["key"] == activity_key), None)
    if activity:
        activity = activity_for_grade(activity, g.child["grade"])
    if not activity or not isinstance(answers, list) or len(answers) != len(activity["questions"]):
        return jsonify({"error": "La actividad o las respuestas no son válidas."}), 400
    if any(not isinstance(answer, int) or isinstance(answer, bool) for answer in answers):
        return jsonify({"error": "Selecciona una respuesta para cada pregunta."}), 400
    if any(answer < 0 or answer >= len(question["options"]) for answer, question in zip(answers, activity["questions"])):
        return jsonify({"error": "Una de las respuestas no es válida."}), 400

    correct = evaluate_game(activity, answers) if activity["kind"] == "Juego" else sum(answer == question["answer"] for answer, question in zip(answers, activity["questions"]))
    score = round(correct * activity["points"] / len(activity["questions"]))
    cursor = g.db.cursor()
    cursor.execute(
        """INSERT INTO child_activity_progress (child_id, activity_key, best_score, attempts)
           VALUES (%s, %s, %s, 1)
           ON DUPLICATE KEY UPDATE
             best_score = GREATEST(best_score, VALUES(best_score)),
             attempts = attempts + 1,
             completed_at = CURRENT_TIMESTAMP""",
        (child_id, activity_key, score),
    )
    cursor.close()
    g.db.commit()
    row = _query(
        "SELECT best_score, attempts FROM child_activity_progress WHERE child_id = %s AND activity_key = %s",
        (child_id, activity_key), True,
    )[0]
    return jsonify({
        "correct": correct, "total": len(activity["questions"]), "earned": score,
        "best_score": row["best_score"], "attempts": row["attempts"],
        "message": "¡Excelente trabajo!" if correct == len(activity["questions"]) else "¡Buen intento! Sigue practicando.",
    })


@learning.get("/activities")
@auth_parent
def activities():
    grade = request.args.get("grade", default=3, type=int)
    grade = min(5, max(1, grade or 3))
    return jsonify({"grade": grade, "activities": _catalog_for_grade(grade)})


@learning.get("/subjects")
@auth_parent
def subjects():
    """Metadatos del catálogo para que la interfaz no duplique el currículo."""
    result = []
    for subject in SUBJECTS:
        activities = [item for item in ACTIVITIES if item["subject"] == subject["name"]]
        result.append({
            **subject,
            "available": bool(activities),
            "activity_count": len(activities),
            "learning_count": sum(item["kind"] == "Aprendizaje" for item in activities),
            "game_count": sum(item["kind"] == "Juego" for item in activities),
        })
    return jsonify({"subjects": result, "total_activities": len(ACTIVITIES)})
