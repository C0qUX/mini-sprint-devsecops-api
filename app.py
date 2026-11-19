"""API REST corregida para el mini-sprint DevSecOps."""

import os
import secrets
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("practica.db")


def init_db() -> None:
    """Crea usuarios de demostracion con contrasenas cifradas."""
    demo_users = (
        ("admin", os.getenv("DEMO_ADMIN_PASSWORD")),
        ("estudiante", os.getenv("DEMO_STUDENT_PASSWORD")),
    )

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER PRIMARY KEY, "
            "username TEXT UNIQUE NOT NULL, "
            "password_hash TEXT NOT NULL)"
        )
        for username, password in demo_users:
            if password:
                conn.execute(
                    "INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )


@app.get("/api/health")
def health():
    return jsonify(status="ok", service="API de practica")


@app.get("/api/profile")
def profile():
    configured_key = os.getenv("API_KEY")
    supplied_key = request.headers.get("X-API-Key", "")

    if not configured_key:
        return jsonify(error="Servicio no configurado"), 503
    if not secrets.compare_digest(supplied_key, configured_key):
        return jsonify(error="No autorizado"), 401
    return jsonify(user="admin", message="Acceso de demostracion")


@app.post("/api/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify(error="Formato de credenciales invalido"), 400
    if not username or not password or len(username) > 80 or len(password) > 256:
        return jsonify(error="Credenciales invalidas"), 401

    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()

    if row and check_password_hash(row[2], password):
        return jsonify(message="Login correcto", user={"id": row[0], "username": row[1]})
    return jsonify(error="Credenciales invalidas"), 401


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
