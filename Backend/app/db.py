"""Conexión y operaciones comunes de la base de datos MySQL."""

import os

import mysql.connector
from flask import g


DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "edutopia"),
}


def get_db():
    """Devuelve la conexión asociada a la petición actual."""
    if "db" not in g:
        g.db = mysql.connector.connect(**DB_CONFIG)
    return g.db


def query(sql, params=(), fetch=False):
    """Ejecuta una consulta y devuelve filas o el último id insertado."""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute(sql, params)
        return cursor.fetchall() if fetch else cursor.lastrowid
    finally:
        cursor.close()


def commit():
    get_db().commit()
