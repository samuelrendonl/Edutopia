"""Rutas administrativas protegidas por permisos RBAC."""

from flask import Blueprint, g, jsonify, request

from app.auth_sessions import ROLE_PERMISSIONS, auth_permission
from app.db import commit, query
from app.learning_content import ACTIVITIES, public_activity


admin = Blueprint("admin", __name__, url_prefix="/api/admin")

ROLE_DETAILS = {
    "parent": ("Familia", "Gestiona perfiles infantiles y acompaña su progreso."),
    "teacher": ("Docente", "Consulta aprendizajes y progreso de sus estudiantes."),
    "editor": ("Editor de contenidos", "Consulta y administra el catálogo educativo."),
    "admin": ("Administrador", "Acceso completo a usuarios, permisos, catálogo y reportes."),
}


@admin.get("/catalog")
@auth_permission("learning.view")
def catalog():
    requested_grade = request.args.get("grade", type=int)
    grades = range(1, 6) if requested_grade is None else [requested_grade]
    if any(grade < 1 or grade > 5 for grade in grades):
        return jsonify({"error": "El grado debe estar entre 1 y 5."}), 400

    activities = [
        public_activity(activity, grade)
        for grade in grades
        for activity in ACTIVITIES
        if activity["kind"] == "Aprendizaje"
    ]
    return jsonify({
        "grades": list(grades),
        "activities": activities,
        "total": len(activities),
    })


@admin.get("/roles")
@auth_permission("users.manage")
def roles():
    result = []
    for name, permissions in ROLE_PERMISSIONS.items():
        display_name, description = ROLE_DETAILS[name]
        result.append({
            "name": name,
            "display_name": display_name,
            "description": description,
            "permissions": sorted(permissions),
        })
    return jsonify({"roles": result})


@admin.get("/users")
@auth_permission("users.manage")
def users():
    rows = query(
        "SELECT id, name, email, role, created_at FROM parents ORDER BY created_at DESC",
        fetch=True,
    )
    return jsonify({"users": rows})


@admin.patch("/users/<int:user_id>/role")
@auth_permission("users.manage")
def update_role(user_id):
    data = request.get_json(silent=True) or {}
    role = data.get("role")
    if role not in ROLE_PERMISSIONS:
        return jsonify({"error": "El rol seleccionado no es válido."}), 400

    target = query("SELECT id, role FROM parents WHERE id = %s", (user_id,), True)
    if not target:
        return jsonify({"error": "No encontramos ese usuario."}), 404
    if user_id == g.parent["id"] and role != "admin":
        return jsonify({"error": "No puedes retirar tus propios permisos de administrador."}), 409
    if target[0].get("role") == "admin" and role != "admin":
        admins = query("SELECT COUNT(*) AS total FROM parents WHERE role = 'admin'", fetch=True)
        if admins and admins[0]["total"] <= 1:
            return jsonify({"error": "Debe existir al menos un administrador."}), 409

    query("UPDATE parents SET role = %s WHERE id = %s", (role, user_id))
    commit()
    return jsonify({"ok": True, "user_id": user_id, "role": role})


@admin.get("/overview")
@auth_permission("reports.view")
def overview():
    users = query("SELECT COUNT(*) AS total FROM parents", fetch=True)
    children = query("SELECT COUNT(*) AS total FROM children", fetch=True)
    return jsonify({
        "users": users[0]["total"] if users else 0,
        "children": children[0]["total"] if children else 0,
        "learning_activities": sum(item["kind"] == "Aprendizaje" for item in ACTIVITIES),
        "grades": 5,
    })
