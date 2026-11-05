import os
import secrets
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from dotenv import load_dotenv

load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

from flask import Flask, g, jsonify, request
from flask_cors import CORS
from werkzeug.security import check_password_hash, generate_password_hash
from mysql.connector import IntegrityError
from app.learning_routes import learning
from app.auth_sessions import issue_parent_token, revoke_parent_token, auth_parent
from app.db import DB_CONFIG, get_db, query, commit
from app.study_guide.routes import study_guides

def load_secret_key():
    configured = os.getenv("SECRET_KEY")
    if configured:
        return configured
    secret_path = os.path.join(PROJECT_ROOT, ".secret_key")
    try:
        with open(secret_path, "r", encoding="utf-8") as secret_file:
            existing = secret_file.read().strip()
            if existing:
                return existing
    except FileNotFoundError:
        pass
    generated = secrets.token_urlsafe(48)
    try:
        with open(secret_path, "x", encoding="utf-8") as secret_file:
            secret_file.write(generated)
        return generated
    except FileExistsError:
        with open(secret_path, "r", encoding="utf-8") as secret_file:
            return secret_file.read().strip()
    except OSError:
        return generated


app = Flask(__name__)
app.config["SECRET_KEY"] = load_secret_key()
app.register_blueprint(learning)
app.register_blueprint(study_guides)
from admin_routes import admin
app.register_blueprint(admin)
from juegos.backend.routes import games
app.register_blueprint(games)
allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.before_request
def initialize_learning_connection():
    if request.path.startswith("/api/learning/children/"):
        get_db()

@app.teardown_appcontext
def close_db(_error=None):
    db = g.pop("db", None)
    if db and db.is_connected(): db.close()

def row_dict(row): return dict(row) if row else None

def public_parent(parent):
    return {
        "id": parent["id"],
        "name": parent["name"],
        "email": parent["email"],
        "role": parent.get("role", "parent"),
    }

@app.get("/api")
def home(): return jsonify({"mensaje": "Backend de Edutopia funcionando con MySQL"})

@app.post("/api/auth/register")
def register():
    data = request.get_json(silent=True) or {}
    name, email, password = data.get("name", "").strip(), data.get("email", "").strip().lower(), data.get("password", "")
    if not name or not email or len(password) < 6: return jsonify({"error": "Completa todos los datos. La contraseña debe tener 6 caracteres."}), 400
    try:
        parent_id = query("INSERT INTO parents (name, email, password_hash) VALUES (%s, %s, %s)", (name, email, generate_password_hash(password))); commit()
    except IntegrityError: return jsonify({"error": "Este correo ya está registrado."}), 409
    return jsonify({"parent": {"id": parent_id, "name": name, "email": email, "role": "parent"}, "token": issue_parent_token(parent_id)}), 201

@app.post("/api/auth/login")
def login():
    data = request.get_json(silent=True) or {}
    rows = query("SELECT * FROM parents WHERE email = %s", (data.get("email", "").strip().lower(),), True)
    if not rows or not check_password_hash(rows[0]["password_hash"], data.get("password", "")): return jsonify({"error": "Correo o contraseña incorrectos."}), 401
    parent = rows[0]
    return jsonify({"parent": public_parent(parent), "token": issue_parent_token(parent["id"])})

@app.post("/api/auth/logout")
def logout():
    data = request.get_json(silent=True) or {}
    revoke_parent_token(request.headers.get("X-Auth-Token") or data.get("token"))
    return jsonify({"ok": True})

@app.get("/api/children")
@auth_parent
def children(): return jsonify({"children": query("SELECT * FROM children WHERE parent_id = %s ORDER BY created_at DESC", (g.parent["id"],), True)})

@app.post("/api/children")
@auth_parent
def add_child():
    data = request.get_json(silent=True) or {}
    try: name, age, grade = data.get("name", "").strip(), int(data.get("age")), int(data.get("grade"))
    except (TypeError, ValueError): return jsonify({"error": "Revisa el nombre, la edad y el grado."}), 400
    if not name or age < 3 or age > 12 or grade < 1 or grade > 5: return jsonify({"error": "Usa una edad entre 3 y 12 años y un grado de 1.º a 5.º."}), 400
    child_id = query("INSERT INTO children (parent_id, name, age, grade, avatar) VALUES (%s, %s, %s, %s, %s)", (g.parent["id"], name, age, grade, data.get("avatar", "🌟"))); commit()
    return jsonify({"child": query("SELECT * FROM children WHERE id = %s", (child_id,), True)[0]}), 201


def child_payload(data):
    """Valida y normaliza los datos editables de un perfil infantil."""
    try:
        name = data.get("name", "").strip()
        age = int(data.get("age"))
        grade = int(data.get("grade"))
    except (AttributeError, TypeError, ValueError):
        return None, "Revisa el nombre, la edad y el grado."
    if not name or age < 3 or age > 12 or grade < 1 or grade > 5:
        return None, "Usa una edad entre 3 y 12 años y un grado de 1.º a 5.º."
    return {"name": name, "age": age, "grade": grade}, None


@app.put("/api/children/<int:child_id>")
@auth_parent
def update_child(child_id):
    child = query(
        "SELECT id FROM children WHERE id = %s AND parent_id = %s",
        (child_id, g.parent["id"]),
        True,
    )
    if not child:
        return jsonify({"error": "No encontramos ese perfil infantil."}), 404

    payload, error = child_payload(request.get_json(silent=True) or {})
    if error:
        return jsonify({"error": error}), 400
    query(
        "UPDATE children SET name = %s, age = %s, grade = %s WHERE id = %s AND parent_id = %s",
        (payload["name"], payload["age"], payload["grade"], child_id, g.parent["id"]),
    )
    commit()
    return jsonify({"child": query("SELECT * FROM children WHERE id = %s", (child_id,), True)[0]})


@app.delete("/api/children/<int:child_id>")
@auth_parent
def delete_child(child_id):
    data = request.get_json(silent=True) or {}
    password = data.get("password", "")
    if not isinstance(password, str) or not check_password_hash(g.parent["password_hash"], password):
        return jsonify({"error": "La contraseña no es correcta. No se eliminó el perfil."}), 403
    child = query(
        "SELECT id FROM children WHERE id = %s AND parent_id = %s",
        (child_id, g.parent["id"]),
        True,
    )
    if not child:
        return jsonify({"error": "No encontramos ese perfil infantil."}), 404
    query("DELETE FROM children WHERE id = %s AND parent_id = %s", (child_id, g.parent["id"]))
    commit()
    return jsonify({"ok": True})

if __name__ == "__main__": app.run(debug=True, port=int(os.getenv("PORT", "5000")))
