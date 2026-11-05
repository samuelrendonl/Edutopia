"""Sesiones revocables, compartidas entre procesos mediante SQLite local.
Los datos educativos siguen en MySQL. No requiere migrar las tablas existentes.
"""
from functools import wraps
import hashlib
import secrets
import sqlite3
import time
from pathlib import Path
from flask import current_app, g
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

from .db import query

SALT = "edutopia-family-session-v2"
# Ventana absoluta máxima del token firmado y ventana de inactividad.
MAX_ABSOLUTE_SECONDS = 60 * 60 * 8
MAX_INACTIVITY_SECONDS = 60 * 30

ROLE_PERMISSIONS = {
    "parent": {"learning.view", "children.manage", "progress.view"},
    "teacher": {"learning.view", "progress.view", "reports.view"},
    "editor": {"learning.view", "learning.manage"},
    "admin": {
        "learning.view", "learning.manage", "children.manage", "progress.view",
        "reports.view", "users.manage",
    },
}


def _db():
    path = current_app.config.get("SESSION_DB_PATH", str(Path(__file__).resolve().parents[2] / "sessions.sqlite3"))
    db = sqlite3.connect(path, timeout=10)
    db.execute("PRAGMA busy_timeout = 10000")
    db.execute("PRAGMA journal_mode = WAL")
    db.execute("CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, parent_id INTEGER NOT NULL, expires REAL NOT NULL)")
    return db


def _digest(token):
    return hashlib.sha256(token.encode()).hexdigest()


def issue_parent_token(parent_id):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=SALT)
    token = serializer.dumps({"parent_id": int(parent_id), "nonce": secrets.token_urlsafe(24)})
    db = _db()
    try:
        with db:
            db.execute("DELETE FROM sessions WHERE expires < ?", (time.time(),))
            db.execute("INSERT INTO sessions VALUES (?, ?, ?)", (_digest(token), int(parent_id), time.time()+MAX_INACTIVITY_SECONDS))
    finally:
        db.close()
    return token


def verify_parent_token(token):
    if not isinstance(token, str) or not token:
        return None
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=SALT)
    try:
        payload = serializer.loads(token, max_age=MAX_ABSOLUTE_SECONDS)
        parent_id = int(payload["parent_id"])
    except (BadSignature, SignatureExpired, KeyError, TypeError, ValueError):
        return None
    db = _db()
    try:
        row = db.execute("SELECT parent_id FROM sessions WHERE id = ? AND expires > ?", (_digest(token), time.time())).fetchone()
        if not (row and row[0] == parent_id):
            return None
        # Deslizamos la ventana de inactividad en cada uso válido.
        with db:
            db.execute("UPDATE sessions SET expires = ? WHERE id = ?", (time.time() + MAX_INACTIVITY_SECONDS, _digest(token)))
        return parent_id
    finally:
        db.close()


def revoke_parent_token(token):
    if not isinstance(token, str) or not token:
        return
    db = _db()
    try:
        with db:
            db.execute("DELETE FROM sessions WHERE id = ?", (_digest(token),))
    finally:
        db.close()


def permissions_for_parent(parent):
    """Obtiene permisos configurados y conserva un fallback seguro por rol."""
    role = parent.get("role", "parent") if isinstance(parent, dict) else "parent"
    fallback = ROLE_PERMISSIONS.get(role, ROLE_PERMISSIONS["parent"])
    try:
        rows = query(
            "SELECT permission_name FROM role_permissions WHERE role_name = %s",
            (role,), True,
        )
        permissions = {row["permission_name"] for row in rows if row.get("permission_name")}
        return permissions or fallback
    except Exception:
        # Permite iniciar sesión durante una actualización gradual de la BD.
        return fallback


def has_permission(permission):
    return permission in getattr(g, "permissions", set())


def auth_parent(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        from flask import request, jsonify, g
        parent_id = verify_parent_token(request.headers.get("X-Auth-Token"))
        if not parent_id:
            return jsonify({"error": "Inicia sesión para continuar."}), 401
        parent = query("SELECT * FROM parents WHERE id = %s", (parent_id,), True)
        if not parent:
            return jsonify({"error": "La sesión no es válida."}), 401
        g.parent = parent[0]
        g.permissions = permissions_for_parent(g.parent)
        return fn(*args, **kwargs)
    return wrapper


def auth_permission(permission):
    """Protege una ruta con autenticación y un permiso RBAC concreto."""
    def decorator(fn):
        @auth_parent
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not has_permission(permission):
                from flask import jsonify
                return jsonify({"error": "No tienes permisos para realizar esta acción."}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
